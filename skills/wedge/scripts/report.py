#!/usr/bin/env python3
"""Wedge report: render a run into one self-contained HTML report + share card.

Reads ideas/<slug>/report.json (schema: references/report-schema.md) and
ideas/<slug>/evidence.jsonl, then writes:

    ideas/<slug>/report.html   one file, no external requests, works offline
    ideas/<slug>/card.svg      1200x630 share card for X / LinkedIn / README

Every quote shown carries its verification status from verify.py, so a
reader can see at a glance what is proven and what is not.

Usage:
    python3 report.py ideas/<slug>
"""
import collections
import html
import json
import os
import sys
from datetime import date

E = html.escape


def load(folder):
    with open(os.path.join(folder, "report.json"), encoding="utf-8") as f:
        rep = json.load(f)
    ev = {}
    path = os.path.join(folder, "evidence.jsonl")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    ev[r.get("id")] = r
    return rep, ev


# --- pieces ----------------------------------------------------------------

def badge(status):
    label = {"yes": "verified", "captured": "captured at fetch", "partial": "partial match", "no": "not found",
             "unreachable": "unreachable"}.get(status, "unchecked")
    cls = {"yes": "ok", "captured": "ok", "partial": "warn", "no": "bad"}.get(status, "muted")
    return '<span class="badge %s">%s</span>' % (cls, label)


def quotes(ids, ev, limit=None):
    out = []
    for i in (ids or [])[:limit]:
        r = ev.get(i)
        if not r:
            out.append('<li class="q missing">Missing evidence <code>%s</code></li>' % E(str(i)))
            continue
        src = r.get("source") or "source"
        out.append('<li class="q"><blockquote>&ldquo;%s&rdquo;</blockquote><div class="cite">'
                   '<a href="%s" target="_blank" rel="noopener">%s%s</a> %s</div></li>'
                   % (E(r.get("quote", "")), E(r.get("url", "#")), E(src),
                      (" &middot; " + E(r["date"])) if r.get("date") else "", badge(r.get("verified"))))
    return '<ul class="quotes">%s</ul>' % "".join(out) if out else ""


def claim_status(ids, ev, need=2):
    urls = {ev[i]["url"] for i in (ids or []) if i in ev and ev[i].get("verified") in ("yes", "captured")}
    if len(urls) >= need:
        return '<span class="badge ok">%d sources</span>' % len(urls)
    return '<span class="badge bad">unverified &middot; %d source%s</span>' % (len(urls), "" if len(urls) == 1 else "s")


def section(id_, num, title, body, lede=""):
    if not body:
        return ""
    return ('<section id="%s"><header class="sh"><span class="num">%s</span><h2>%s</h2></header>%s%s</section>'
            % (id_, num, E(title), ('<p class="lede">%s</p>' % E(lede)) if lede else "", body))


def ul(items, cls=""):
    items = [i for i in (items or []) if i]
    return ('<ul class="%s">%s</ul>' % (cls, "".join("<li>%s</li>" % E(str(i)) for i in items))) if items else ""


def bar(v, mx=10):
    try:
        pct = max(0, min(100, float(v) / mx * 100))
    except (TypeError, ValueError):
        pct = 0
    return '<span class="bar"><i style="width:%.0f%%"></i></span>' % pct


# --- sections --------------------------------------------------------------

def s_verdict(rep):
    v = rep.get("verdict") or {}
    call = (v.get("call") or "").upper()
    cls = {"GO": "go", "PIVOT": "pivot", "KILL": "kill", "INCONCLUSIVE": "inconclusive"}.get(call, "pivot")
    f = rep.get("founder") or {}
    fit = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (E(k.replace("_", " ")), E(str(val))) for k, val in f.items() if val)
    return ('<div class="verdict %s"><div class="call">%s</div><div class="vtext"><p>%s</p>%s</div>%s</div>%s'
            % (cls, E(call or "-"), E(v.get("summary", "")),
               ('<p class="score"><b>%s</b> / 100</p>' % E(str(v["score"]))) if v.get("score") is not None else "",
               "", ('<dl class="fit">%s</dl>' % fit) if fit else ""))


def s_opps(rep, ev):
    ops = rep.get("opportunities") or []
    if not ops:
        return ""
    keys = []
    for o in ops:
        for k in (o.get("scores") or {}):
            if k not in keys:
                keys.append(k)
    head = "".join("<th>%s</th>" % E(k.replace("_", " ")) for k in keys)
    rows = []
    for n, o in enumerate(sorted(ops, key=lambda o: -(o.get("score") or 0)), 1):
        sc = o.get("scores") or {}
        cells = "".join("<td>%s %s</td>" % (bar(sc.get(k)), E(str(sc.get(k, "")))) for k in keys)
        rows.append('<tr><td class="rank">%d</td><td><b>%s</b><div class="sub">%s</div></td><td class="tot">%s</td>%s</tr>'
                    % (n, E(o.get("name", "")), E(o.get("one_liner", "")), E(str(o.get("score", ""))), cells))
    why = "".join('<div class="why"><h4>%s</h4><p>%s</p>%s</div>' % (E(o.get("name", "")), E(o.get("why", "")), quotes(o.get("evidence"), ev, 2))
                  for o in ops if o.get("why"))
    return ('<div class="scroll"><table class="opps"><thead><tr><th>#</th><th>Opportunity</th><th>Score</th>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>%s' % (head, "".join(rows), why))


def s_gap(rep, ev):
    g = rep.get("gap") or {}
    if not g.get("statement"):
        return ""
    return ('<div class="gap"><p class="statement">%s</p>%s</div>%s'
            % (E(g["statement"]), claim_status(g.get("evidence"), ev), quotes(g.get("evidence"), ev)))


def s_pains(rep, ev):
    pains = rep.get("pains") or []
    if not pains:
        return ""
    comps = []
    for p in pains:
        for c in (p.get("by_competitor") or {}):
            if c not in comps:
                comps.append(c)
    heat = ""
    if comps:
        mx = max([v for p in pains for v in (p.get("by_competitor") or {}).values()] or [1]) or 1
        rows = []
        for p in pains:
            bc = p.get("by_competitor") or {}
            cells = "".join('<td style="--h:%.2f">%s</td>' % ((bc.get(c, 0) / float(mx)), bc.get(c, "") or "")
                            for c in comps)
            rows.append("<tr><th>%s</th>%s</tr>" % (E(p.get("theme", "")), cells))
        heat = ('<div class="scroll"><table class="heat"><thead><tr><th></th>%s</tr></thead><tbody>%s</tbody></table></div>'
                % ("".join("<th>%s</th>" % E(c) for c in comps), "".join(rows)))
    cards = "".join('<article class="pain sev-%s"><header><h3>%s</h3><span class="sev">%s</span>%s</header><p>%s</p>%s</article>'
                    % (E(p.get("severity", "medium")), E(p.get("theme", "")), E(p.get("severity", "")),
                       claim_status(p.get("evidence"), ev), E(p.get("summary", "")), quotes(p.get("evidence"), ev, 3))
                    for p in pains)
    return heat + '<div class="pains">%s</div>' % cards


def s_competitors(rep, ev):
    cs = rep.get("competitors") or []
    cards = "".join(
        '<article class="comp"><header><h3><a href="%s" target="_blank" rel="noopener">%s</a></h3><span class="price">%s</span></header>'
        '<p class="pos">%s</p><div class="two"><div><h4>Strong at</h4>%s</div><div><h4>Weak at</h4>%s</div></div>%s</article>'
        % (E(c.get("url", "#")), E(c.get("name", "")), E(c.get("pricing", "")), E(c.get("positioning", "")),
           ul(c.get("strengths")), ul(c.get("weaknesses"), "weak"), quotes(c.get("evidence"), ev, 2))
        for c in cs)
    f = rep.get("features") or {}
    matrix = ""
    if f.get("columns") and f.get("rows"):
        sym = {"yes": '<span class="y">&#10003;</span>', "no": '<span class="n">&#10005;</span>',
               "partial": '<span class="p">&#9681;</span>', "unknown": '<span class="u" title="unknown">?</span>'}
        body = "".join("<tr><th>%s</th>%s</tr>" % (E(r.get("name", "")), "".join(
            "<td>%s</td>" % sym.get(str(v).lower(), E(str(v))) for v in r.get("values", []))) for r in f["rows"])
        matrix = ('<h3 class="mt">Feature matrix</h3><div class="scroll"><table class="matrix"><thead><tr><th></th>%s</tr></thead><tbody>%s</tbody></table></div>'
                  % ("".join("<th>%s</th>" % E(c) for c in f["columns"]), body))
    return ('<div class="comps">%s</div>' % cards if cards else "") + matrix


def s_critic(rep):
    cr = rep.get("critic") or []
    return "".join('<div class="crit sev-%s"><p class="risk"><b>Risk:</b> %s</p><p class="reb"><b>Answer:</b> %s</p></div>'
                   % (E(c.get("severity", "medium")), E(c.get("risk", "")), E(c.get("rebuttal", "Unresolved.")))
                   for c in cr)


def s_win(rep, ev):
    w = rep.get("win_plan") or {}
    if not w:
        return ""
    out = []
    if w.get("positioning"):
        out.append('<p class="positioning">%s</p>' % E(w["positioning"]))
    if w.get("switching_triggers"):
        out.append('<h3>Switching triggers</h3><div class="triggers">%s</div>' % "".join(
            '<div class="trig"><p class="t">%s</p><p class="m">&rarr; %s</p>%s</div>'
            % (E(t.get("trigger", "")), E(t.get("move", "")), quotes(t.get("evidence"), ev, 1))
            for t in w["switching_triggers"]))
    if w.get("offers"):
        out.append("<h3>Offers that win switchers</h3>" + ul(w["offers"], "check"))
    if w.get("build_first"):
        out.append('<h3>Build first</h3><ol class="build">%s</ol>' % "".join(
            "<li><b>%s</b> %s</li>" % (E(b.get("feature", "")), E(b.get("why", ""))) for b in w["build_first"]))
    if w.get("where_to_find"):
        out.append('<h3>Where unhappy customers are</h3><ul class="where">%s</ul>' % "".join(
            '<li><a href="%s" target="_blank" rel="noopener">%s</a> <span>%s</span></li>'
            % (E(x.get("url", "#")), E(x.get("place", "")), E(x.get("why", ""))) for x in w["where_to_find"]))
    if w.get("trust"):
        out.append("<h3>Trust signals to show</h3>" + ul(w["trust"], "check"))
    if w.get("stop_doing"):
        out.append("<h3>Do not copy</h3>" + ul(w["stop_doing"], "weak"))
    if w.get("assets"):
        out.append('<h3>Ready-made assets</h3><ul class="assets">%s</ul>' % "".join(
            '<li><a href="%s">%s</a></li>' % (E(a.get("path", "#")), E(a.get("name", ""))) for a in w["assets"]))
    return "".join(out)


def s_business(rep):
    out = []
    p = rep.get("pricing") or {}
    if p:
        out.append('<div class="kv"><h3>Pricing</h3><p class="big">%s</p><p>%s</p><p class="sub">Competitors: %s</p></div>'
                   % (E(p.get("recommendation", "")), E(p.get("rationale", "")), E(p.get("competitor_range", ""))))
    c = rep.get("cost") or {}
    if c:
        rows = "".join("<tr><td>%s</td><td>%s</td></tr>" % (E(s.get("item", "")), E(s.get("cost", ""))) for s in c.get("stack", []))
        out.append('<div class="kv"><h3>Cost to run</h3><p class="big">%s</p><table class="cost">%s</table></div>'
                   % (E(c.get("monthly", "")), rows))
    return '<div class="biz">%s</div>' % "".join(out) if out else ""


def s_first10(rep):
    f = rep.get("first_10") or []
    return '<ol class="first10">%s</ol>' % "".join(
        "<li><b>%s</b>%s%s</li>" % (E(x.get("step", "")), (' <span class="where">%s</span>' % E(x["where"])) if x.get("where") else "",
                                    ('<p class="script">%s</p>' % E(x["script"])) if x.get("script") else "")
        for x in f) if f else ""


def s_validate(rep):
    v = rep.get("validation") or {}
    k = rep.get("kill_criteria") or []
    out = ""
    if v:
        out += ('<div class="test"><p class="exp">%s</p><p class="pass"><b>Pass bar (%s days):</b> %s</p>%s</div>'
                % (E(v.get("experiment", "")), E(str(v.get("days", 7))), E(v.get("pass_bar", "")), ul(v.get("steps"))))
    if k:
        out += "<h3>Kill it if</h3>" + ul(k, "weak")
    return out


def s_launch(rep):
    l = rep.get("launch") or {}
    if not l:
        return ""
    alts = ul(["%s (%s)" % (a.get("domain", ""), a.get("status", "")) if isinstance(a, dict) else a for a in l.get("alternatives", [])])
    lp = ('<p><a class="btn" href="%s">Open landing page</a></p>' % E(l["landing_page"])) if l.get("landing_page") else ""
    return ('<div class="launch"><p class="name">%s</p><p class="dom">%s <span class="badge %s">%s</span></p>%s%s</div>'
            % (E(l.get("name", "")), E(l.get("domain", "")), "ok" if l.get("domain_status") == "available" else "muted",
               E(l.get("domain_status", "unchecked")), alts, lp))


def s_evidence(ev):
    if not ev:
        return ""
    rows = "".join('<tr><td><code>%s</code></td><td>%s</td><td>&ldquo;%s&rdquo;</td><td><a href="%s" target="_blank" rel="noopener">%s</a></td><td>%s</td></tr>'
                   % (E(str(i)), E(", ".join(r["claim"]) if isinstance(r.get("claim"), list) else str(r.get("claim", ""))), E(r.get("quote", "")), E(r.get("url", "#")), E(r.get("source", "link")), badge(r.get("verified")))
                   for i, r in ev.items())
    n = len(ev)
    ok = sum(1 for r in ev.values() if r.get("verified") == "yes")
    cap = sum(1 for r in ev.values() if r.get("verified") == "captured")
    return ('<p class="lede">%d of %d quotes verified against the live source by <code>verify.py</code>%s.</p>'
            '<div class="scroll"><table class="ev"><thead><tr><th>ID</th><th>Claim</th><th>Quote</th><th>Source</th><th>Status</th></tr></thead><tbody>%s</tbody></table></div>'
            % (ok, n, (", %d more matched the text saved when they were fetched" % cap) if cap else "", rows))


# --- page ------------------------------------------------------------------

CSS = """
:root{--bg:#f6f5f2;--card:#fff;--sunk:#efeee9;--ink:#111110;--text:#2b2a27;--mute:#6f6d67;--faint:#a8a59e;--line:#e5e3dd;--sig:#111110;--ok:#16794a;--okbg:#e5f3eb;--warn:#9a6512;--warnbg:#fbf0dc;--bad:#b3261e;--badbg:#fbe7e5;--soft:#efeee9;--mark:#fff1a8;--shadow:0 1px 2px rgba(17,17,16,.04),0 8px 24px -8px rgba(17,17,16,.10)}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0e0e0d;--card:#171716;--sunk:#1d1d1b;--ink:#f4f3ef;--text:#d9d7d1;--mute:#9b9891;--faint:#5f5d58;--line:#2a2a27;--sig:#f4f3ef;--ok:#4cc38a;--okbg:#12291d;--warn:#e0a84a;--warnbg:#2b2210;--bad:#ff7b70;--badbg:#2e1513;--soft:#1d1d1b;--mark:#4a3f0c;--shadow:0 1px 2px rgba(0,0,0,.3),0 8px 24px -8px rgba(0,0,0,.5)}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:16px/1.6 "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration-color:var(--faint);text-underline-offset:3px}a:hover{text-decoration-color:var(--ink)}
code{font:13px ui-monospace,SFMono-Regular,Menlo,monospace}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
.top{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;padding:20px 0;border-bottom:1px solid var(--line);font-size:14px;color:var(--mute)}
.top b{display:inline-flex;align-items:center;gap:9px;color:var(--ink);font-weight:600;font-size:15px}
.mk{width:24px;height:24px;border-radius:7px;background:var(--ink);position:relative;display:inline-block}.mk:after{content:"";position:absolute;inset:6px;background:var(--bg);clip-path:polygon(100% 0,100% 100%,0 100%)}
.meta{display:inline-flex;gap:6px;flex-wrap:wrap}.meta span{background:var(--card);border:1px solid var(--line);border-radius:99px;padding:3px 11px;font-size:13px}
h1{font-size:clamp(34px,6vw,60px);line-height:1.02;letter-spacing:-.045em;font-weight:600;color:var(--ink);margin:56px 0 14px}
.subtitle{font-size:18px;color:var(--mute);max-width:720px;margin:0 0 26px}
nav.toc{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 48px}
nav.toc a{text-decoration:none;color:var(--mute);font-size:13px;background:var(--card);border:1px solid var(--line);border-radius:99px;padding:5px 12px}nav.toc a:hover{color:var(--ink);border-color:var(--faint)}
section{padding:48px 0 8px}
.sh{display:flex;align-items:baseline;gap:12px;margin-bottom:6px}.num{font:500 13px ui-monospace,Menlo,monospace;color:var(--faint)}
h2{font-size:clamp(26px,3.6vw,34px);line-height:1.1;letter-spacing:-.035em;font-weight:600;color:var(--ink);margin:0 0 14px}
h3{font-size:13px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--mute);margin:30px 0 12px}
h4{margin:0 0 6px;font-size:15px;color:var(--ink)}.lede{color:var(--mute);margin:-4px 0 22px;max-width:680px}.sub{color:var(--mute);font-size:14px}.mt{margin-top:36px}
.card,.verdict,.why,.q,.pain,.comp,.crit,.trig,.kv,.test,.launch,.scrollbox{background:var(--card);border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow)}
.verdict{display:grid;grid-template-columns:auto 1fr;gap:28px;align-items:center;padding:28px}
.call{font:600 22px ui-monospace,Menlo,monospace;letter-spacing:.06em;padding:16px 22px;border-radius:12px}
.inconclusive .call{background:var(--sunk);color:var(--mute)}.go .call{background:var(--okbg);color:var(--ok)}.pivot .call{background:var(--warnbg);color:var(--warn)}.kill .call{background:var(--badbg);color:var(--bad)}
.vtext p{margin:0 0 8px;font-size:17px;color:var(--ink)}.score{color:var(--mute)!important;font-size:15px!important}.score b{font-size:28px;letter-spacing:-.03em;color:var(--ink)}
dl.fit{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 0}dl.fit div{background:var(--card);border:1px solid var(--line);padding:8px 14px;border-radius:12px}dl.fit dt{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--mute)}dl.fit dd{margin:0;font-weight:500;color:var(--ink)}
.scroll{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow)}
table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}tr:last-child td,tr:last-child th{border-bottom:0}
thead th{font-size:12px;font-weight:500;text-transform:uppercase;letter-spacing:.05em;color:var(--mute);background:var(--sunk)}
.rank{font:600 18px ui-monospace,monospace;color:var(--faint)}.tot{font:600 22px ui-monospace,monospace;color:var(--ink)}
.bar{display:inline-block;width:44px;height:6px;border-radius:99px;background:var(--sunk);vertical-align:middle;margin-right:6px;overflow:hidden}.bar i{display:block;height:100%;background:var(--ink);border-radius:99px}
.why{margin:14px 0;padding:22px}.why p{margin:0 0 4px}
.gap .statement{font-size:clamp(20px,2.8vw,26px);line-height:1.4;letter-spacing:-.02em;color:var(--ink);font-weight:500;margin:0 0 12px}
.quotes{list-style:none;padding:0;margin:14px 0;display:grid;gap:10px}
.q{padding:16px 18px;box-shadow:none}.q blockquote{margin:0;font-size:16px;line-height:1.5;color:var(--ink)}
.cite{font-size:12px;color:var(--mute);margin-top:8px;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.badge{font:500 12px "Geist",system-ui,sans-serif;padding:2px 9px;border-radius:99px;white-space:nowrap}
.badge.ok{background:var(--okbg);color:var(--ok)}.badge.warn{background:var(--warnbg);color:var(--warn)}.badge.bad{background:var(--badbg);color:var(--bad)}.badge.muted{background:var(--sunk);color:var(--mute)}
.heat td{text-align:center;font:500 13px ui-monospace,monospace;background:color-mix(in srgb,#e8431c calc(var(--h)*70%),transparent)}
.pains,.comps{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px;margin-top:18px}
.pain,.comp{padding:22px}.pain header,.comp header{display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:space-between;margin-bottom:6px}
.pain h3,.comp h3{margin:0;text-transform:none;letter-spacing:-.01em;font-size:18px;color:var(--ink)}
.sev{font-size:12px;font-weight:500;border-radius:99px;padding:2px 9px;background:var(--sunk);color:var(--mute);text-transform:capitalize}
.sev-high .sev{background:var(--badbg);color:var(--bad)}.sev-medium .sev{background:var(--warnbg);color:var(--warn)}
.price{font:13px ui-monospace,monospace;color:var(--mute)}.pos{color:var(--mute)}.two{display:grid;grid-template-columns:1fr 1fr;gap:12px}.two ul{padding-left:18px;margin:0;font-size:14px}
ul.weak li::marker{content:"\\2715  ";color:var(--bad)}ul.check li::marker{content:"\\2713  ";color:var(--ok)}
.matrix td{text-align:center}.y{color:var(--ok);font-weight:600}.n{color:var(--bad)}.p{color:var(--warn)}.u{color:var(--faint)}
.crit{padding:16px 20px;margin:10px 0}.crit p{margin:4px 0}.crit.sev-high{border-left:4px solid var(--bad)}.crit.sev-medium{border-left:4px solid var(--warn)}
.positioning{font-size:clamp(20px,2.8vw,26px);line-height:1.35;letter-spacing:-.02em;font-weight:500;background:var(--ink);color:var(--bg);padding:28px;border-radius:16px;margin:0}
.triggers{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}.trig{padding:18px}.trig .t{font-weight:600;color:var(--ink);margin:0}.trig .m{color:var(--text);margin:6px 0 0}
ol.build li,ol.first10 li{margin:10px 0}.where span,ol.first10 .where{color:var(--mute);font-size:14px}.script{background:var(--sunk);padding:10px 14px;border-radius:10px;font-size:14px;margin:8px 0 0}
.biz{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}.kv{padding:22px}.kv h3{margin-top:0}.big{font-size:28px;font-weight:600;letter-spacing:-.03em;color:var(--ink);margin:0 0 6px}
.cost td{padding:8px 0;border:0}
.test{padding:22px;border:1px dashed var(--faint);box-shadow:none}.exp{font-size:18px;font-weight:500;color:var(--ink);margin-top:0}
.launch{padding:28px}.launch .name{font-size:40px;line-height:1;letter-spacing:-.04em;font-weight:600;color:var(--ink);margin:0 0 10px}.dom{font:15px ui-monospace,monospace}
.btn{display:inline-block;background:var(--ink);color:var(--bg);text-decoration:none;padding:12px 20px;border-radius:99px;font-weight:500}
.ev td:nth-child(3){max-width:440px;color:var(--ink)}
footer{border-top:1px solid var(--line);margin-top:64px;padding:28px 0 60px;color:var(--mute);font-size:13px}
@media (max-width:640px){.verdict{grid-template-columns:1fr}.two{grid-template-columns:1fr}.call{text-align:center}h1{margin-top:36px}}
@media print{section{break-inside:avoid-page}nav.toc{display:none}}
"""

SECTIONS = [
    ("verdict", "Verdict", lambda r, e: s_verdict(r), ""),
    ("ranking", "Opportunities, ranked", s_opps, "Scored with the reasoning shown. Higher is better on every axis."),
    ("gap", "The gap", s_gap, "The opening competitors leave, backed by what their customers say."),
    ("pain", "What customers complain about", s_pains, "Heat map counts complaints per competitor. Each theme needs two verified sources."),
    ("competitors", "Competitor map", s_competitors, ""),
    ("critic", "The case against", lambda r, e: s_critic(r), "A separate critic pass argued against this. Here is what it found."),
    ("win", "How to win", s_win, "Specific moves that pull customers to you instead of them."),
    ("business", "Pricing and cost", lambda r, e: s_business(r), ""),
    ("first10", "First 10 customers", lambda r, e: s_first10(r), ""),
    ("validate", "7-day test", lambda r, e: s_validate(r), "One experiment, one pass bar. Run it before writing code."),
    ("launch", "Launch kit", lambda r, e: s_launch(r), ""),
    ("evidence", "Evidence", lambda r, e: s_evidence(e), ""),
]


def render(rep, ev):
    parts, toc, n = [], [], 0
    for id_, title, fn, lede in SECTIONS:
        body = fn(rep, ev)
        if not body:
            continue
        n += 1
        num = "%02d" % n
        parts.append(section(id_, num, title, body, lede))
        toc.append('<a href="#%s">%s %s</a>' % (id_, num, E(title)))
    mode = {"scratch": "From scratch", "expertise": "From what you know", "idea": "Stress-test an idea",
            "compete": "Beat my competitors"}.get(rep.get("mode"), rep.get("mode", ""))
    return """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title><meta name="description" content="%(sub)s"><style>%(css)s</style></head><body>
<div class="wrap"><div class="top"><b><span class="mk" aria-hidden="true"></span>Wedge report</b><span class="meta"><span>%(mode)s</span><span>%(depth)s</span><span>%(date)s</span></span></div>
<h1>%(title)s</h1><p class="subtitle">%(sub)s</p><nav class="toc">%(toc)s</nav>%(body)s
<footer>Generated by Wedge &middot; getwedge.dev &middot; github.com/senavoh/wedge &middot; every quote links to its source. Check the badges before you bet money on it.</footer></div></body></html>""" % {
        "title": E(rep.get("title", "Wedge report")), "sub": E(rep.get("subtitle", "")), "css": CSS,
        "mode": E(mode), "depth": E(rep.get("depth", "deep")), "date": E(rep.get("date") or date.today().isoformat()),
        "toc": "".join(toc), "body": "".join(parts)}


def _all_ids(obj):
    """Every evidence id referenced anywhere in report.json."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "evidence" and isinstance(v, list):
                for i in v:
                    yield i
            else:
                yield from _all_ids(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _all_ids(v)


# --- share card ------------------------------------------------------------

def clip(lines, n):
    """Keep n lines; end the last one with an ellipsis if text was cut."""
    if len(lines) <= n:
        return lines
    out = lines[:n]
    out[-1] = out[-1].rstrip(" ,;:") + "\u2026"
    return out


def wrap_text(s, width):
    words, lines, cur = (s or "").split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines


def card(rep, ev):
    v = rep.get("verdict") or {}
    call = (v.get("call") or "").upper()
    fg, bg = {"GO": ("#16794a", "#e5f3eb"), "PIVOT": ("#9a6512", "#fbf0dc"),
              "KILL": ("#b3261e", "#fbe7e5"), "INCONCLUSIVE": ("#6f6d67", "#efeee9")}.get(call, ("#6f6d67", "#efeee9"))
    gap = (rep.get("gap") or {}).get("statement") or rep.get("subtitle", "")
    # The card shows a customer's words: the shortest verified, non-vendor
    # quote behind the gap that is long enough to read as a sentence.
    verified = [ev[i] for i in (rep.get("gap") or {}).get("evidence", []) if i in ev
                and ev[i].get("verified") in ("yes", "captured") and not ev[i].get("official")]
    readable = [r for r in verified if len(r.get("quote", "")) >= 40] or verified
    best = min(readable, key=lambda r: len(r.get("quote", ""))) if readable else None
    sans = "Geist,Inter,Helvetica Neue,Helvetica,Arial,sans-serif"
    title = rep.get("title", "")
    tsize, twrap, tlead = (58, 30, 66) if len(title) <= 58 else (48, 38, 56)  # long titles get a smaller size
    title_lines = clip(wrap_text(title, twrap), 2)
    gap_lines = clip(wrap_text(gap, 70), 3)
    q_lines = clip(wrap_text(best["quote"], 64), 2) if best else []
    y = 200
    t = ['<text x="72" y="%d" font-family="%s" font-size="%d" font-weight="600" letter-spacing="-2" fill="#111110">%s</text>'
         % (y + i * tlead, sans, tsize, E(l)) for i, l in enumerate(title_lines)]
    y += len(title_lines) * tlead + 18
    g = ['<text x="72" y="%d" font-family="%s" font-size="26" fill="#6f6d67">%s</text>' % (y + i * 36, sans, E(l))
         for i, l in enumerate(gap_lines)]
    y += len(gap_lines) * 36 + 34
    box_h = len(q_lines) * 32 + 36
    q = ""
    if q_lines:
        q = '<rect x="72" y="%d" width="1056" height="%d" rx="16" fill="#ffffff" stroke="#e5e3dd"/>' % (y - 30, box_h)
        q += "".join('<text x="100" y="%d" font-family="%s" font-size="23" fill="#111110">%s</text>'
                     % (y + 4 + i * 32, sans, E(("\u201c" if i == 0 else "") + l + ("\u201d" if i == len(q_lines) - 1 else "")))
                     for i, l in enumerate(q_lines))
        q += ('<rect x="%d" y="%d" width="96" height="28" rx="14" fill="#e5f3eb"/><text x="%d" y="%d" text-anchor="middle" '
              'font-family="%s" font-size="15" font-weight="500" fill="#16794a">&#10003; Verified</text>'
              % (1108 - 96, y - 22, 1108 - 48, y - 3, sans))
    score = ('<text x="1128" y="94" text-anchor="end" font-family="%s" font-size="22" fill="#a8a59e">%s / 100</text>'
             % (sans, E(str(v["score"])))) if v.get("score") is not None else ""
    pill_w = 26 + 17 * len(call or "?")
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<rect width="1200" height="630" fill="#f6f5f2"/>
<rect x="72" y="64" width="40" height="40" rx="11" fill="#111110"/><path d="M102 74v20H82z" fill="#f6f5f2"/>
<text x="126" y="93" font-family="%(sans)s" font-size="26" font-weight="600" fill="#111110">Wedge</text>
<rect x="%(px)d" y="60" width="%(pw)d" height="46" rx="12" fill="%(bg)s"/>
<text x="%(tx)d" y="91" text-anchor="middle" font-family="ui-monospace,Menlo,monospace" font-size="22" font-weight="700" letter-spacing="1" fill="%(fg)s">%(call)s</text>%(score)s
%(t)s%(g)s%(q)s
<text x="72" y="606" font-family="%(sans)s" font-size="18" fill="#a8a59e">getwedge.dev  &#183;  every claim cited and checked</text>
</svg>""" % {"sans": sans, "fg": fg, "bg": bg, "call": E(call or "?"), "score": score, "t": "".join(t), "g": "".join(g), "q": q,
             "pw": pill_w, "px": 1128 - 150 - pill_w, "tx": 1128 - 150 - pill_w // 2}


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if not argv or argv[0] in ("-h", "--help"):
        sys.stdout.write(__doc__)
        return 0 if argv else 2
    folder = argv[0]
    rep, ev = load(folder)
    with open(os.path.join(folder, "report.html"), "w", encoding="utf-8") as f:
        f.write(render(rep, ev))
    with open(os.path.join(folder, "card.svg"), "w", encoding="utf-8") as f:
        f.write(card(rep, ev))
    print("wrote %s and %s" % (os.path.join(folder, "report.html"), os.path.join(folder, "card.svg")))
    weak = collections.Counter(r.get("verified", "unchecked") for r in ev.values())
    bad = {k: v for k, v in weak.items() if k not in ("yes", "captured")}
    if bad:
        print("note: %s. These show with warning badges in the report." % ", ".join("%d %s" % (v, k) for k, v in sorted(bad.items())))
    missing = sorted({i for i in _all_ids(rep) if i not in ev})
    if missing:
        print("warning: report.json cites evidence ids not in evidence.jsonl: %s" % ", ".join(missing))
    return 0


if __name__ == "__main__":
    sys.exit(main())
