#!/usr/bin/env python3
"""Wedge domain: check whether names are free, using public RDAP (no keys).

RDAP is the official successor to WHOIS. A 404 from the registry means no
one has registered the domain, which is a strong (not absolute) signal it is
available. Always confirm at a registrar before you announce a name.

Usage:
    python3 domain.py launchnaut gapkit wedgely --tlds com,io,ai,co
    python3 domain.py launchnaut.com
    python3 domain.py --handles gapkit      # also checks github.com/<name>
"""
import argparse
import json
import socket
import sys
import time
import urllib.error
import urllib.request

UA = "wedge/1.0 (+https://github.com/senavoh/wedge)"
BOOTSTRAP = "https://data.iana.org/rdap/dns.json"
_servers = None


def rdap_server(tld):
    """Look up the registry's RDAP server in IANA's bootstrap file.

    Some TLDs (.io, .co and others) publish no RDAP server. For those a 404
    from a generic proxy means nothing, so we must not report "available".
    """
    global _servers
    if _servers is None:
        _servers = {}
        try:
            req = urllib.request.Request(BOOTSTRAP, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=20) as r:
                for tlds, urls in json.load(r)["services"]:
                    for t in tlds:
                        _servers[t] = urls[0]
        except (OSError, ValueError):
            pass
    return _servers.get(tld)


def status(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/rdap+json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except (urllib.error.URLError, OSError):
        return None


def resolves(domain):
    try:
        socket.getaddrinfo(domain, None)
        return True
    except OSError:
        return False


def check_domain(domain):
    tld = domain.rsplit(".", 1)[-1].lower()
    server = rdap_server(tld)
    if server:
        url = server.rstrip("/") + "/domain/" + domain
        code = status(url)
        if code not in (200, 404):
            time.sleep(2)  # registries rate-limit bursts; one polite retry
            code = status(url)
        if code == 200:
            return "taken"
        if code == 404:
            return "available"
    # No RDAP for this TLD (or it failed): a resolving domain is surely taken,
    # a silent one is unknown and must be checked at a registrar.
    return "taken" if resolves(domain) else "unknown"


def check_handle(name):
    code = status("https://github.com/%s" % name)
    return {200: "taken", 404: "available"}.get(code, "unknown")


def main(argv=None):
    p = argparse.ArgumentParser(description="Wedge: check domain availability via RDAP.")
    p.add_argument("names", nargs="+", help="bare names or full domains")
    p.add_argument("--tlds", default="com", help="comma-separated TLDs for bare names (default: com)")
    p.add_argument("--handles", action="store_true", help="also check the GitHub handle")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    tlds = [t.strip().lstrip(".") for t in a.tlds.split(",") if t.strip()]
    results = []
    for n in a.names:
        n = n.strip().lower()
        domains = [n] if "." in n else ["%s.%s" % (n, t) for t in tlds]
        for d in domains:
            results.append({"name": n, "domain": d, "status": check_domain(d)})
        if a.handles:
            results.append({"name": n, "domain": "github.com/" + n.split(".")[0], "status": check_handle(n.split(".")[0])})
    if a.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            mark = {"available": "+", "taken": "-", "unknown": "?"}[r["status"]]
            print("%s %-32s %s" % (mark, r["domain"], r["status"]))
        print("\n+ available (confirm at a registrar)   - taken   ? registry did not answer")
    return 0


if __name__ == "__main__":
    sys.exit(main())
