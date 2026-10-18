#!/usr/bin/env python3
"""Wedge state: save and resume a run, across sessions and across agents.

Each run lives in ideas/<slug>/ with a state.json that records which stages
are done. Any agent can open the folder, run `status`, and pick up at the
first unfinished stage.

Usage:
    python3 state.py init <slug> --mode scratch|expertise|idea|compete --depth quick|deep [--root ideas]
    python3 state.py done <slug> <stage> [--note "..."]
    python3 state.py status <slug>
    python3 state.py list
"""
import argparse
import json
import os
import sys
from datetime import datetime

STAGES = ["founder", "scout", "competitors", "reviews", "gaps", "critic", "win", "launch", "verify", "report"]
SKIP = {
    "compete": {"scout"},     # you already have a business: go straight to competitors
    "idea": {"scout"},        # you already have an idea: no niche hunt
}


def path(root, slug):
    return os.path.join(root, slug, "state.json")


def find_root(root, slug):
    """Find the ideas/ folder for a run from wherever the command is run.

    Checks ./ideas, then parent folders, then whether we are already inside
    ideas/ or inside the run folder itself.
    """
    if os.path.exists(path(root, slug)):
        return root
    here = os.path.abspath(os.getcwd())
    while True:
        cand = os.path.join(here, root)
        if os.path.exists(path(cand, slug)):
            return cand
        if os.path.basename(here) == slug and os.path.exists(os.path.join(here, "state.json")):
            return os.path.dirname(here)
        if os.path.exists(path(here, slug)):
            return here
        parent = os.path.dirname(here)
        if parent == here:
            return root
        here = parent


def load(root, slug):
    try:
        with open(path(root, slug), encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        sys.exit("wedge state: no run called '%s' in %s/. Run this from the folder that contains ideas/, "
                 "or start it with: state.py init %s" % (slug, os.path.abspath(root), slug))


def save(root, slug, st):
    st["updated"] = datetime.now().isoformat(timespec="seconds")
    with open(path(root, slug), "w", encoding="utf-8") as f:
        json.dump(st, f, indent=2)


def plan(st):
    return [s for s in STAGES if s not in SKIP.get(st.get("mode"), set())]


def main(argv=None):
    p = argparse.ArgumentParser(description="Wedge: save and resume runs.")
    p.add_argument("--root", default="ideas")
    sp = p.add_subparsers(dest="cmd", required=True)
    a = sp.add_parser("init"); a.add_argument("slug")
    a.add_argument("--mode", choices=["scratch", "expertise", "idea", "compete"], default="scratch")
    a.add_argument("--depth", choices=["quick", "deep"], default="quick")
    a = sp.add_parser("done"); a.add_argument("slug"); a.add_argument("stage", choices=STAGES); a.add_argument("--note", default="")
    a = sp.add_parser("status"); a.add_argument("slug")
    sp.add_parser("list")
    a = p.parse_args(argv)
    if a.cmd in ("done", "status"):
        a.root = find_root(a.root, a.slug)

    if a.cmd == "init":
        os.makedirs(os.path.join(a.root, a.slug, "raw"), exist_ok=True)
        if os.path.exists(path(a.root, a.slug)):
            print("exists: resuming %s" % a.slug)
            a.cmd = "status"
        else:
            save(a.root, a.slug, {"slug": a.slug, "mode": a.mode, "depth": a.depth, "done": {},
                                  "created": datetime.now().isoformat(timespec="seconds")})
            print("created %s (%s, %s)" % (os.path.join(a.root, a.slug), a.mode, a.depth))
            a.cmd = "status"

    if a.cmd == "done":
        st = load(a.root, a.slug)
        stages = plan(st)
        skipped = [s for s in stages[:stages.index(a.stage)] if s not in st["done"]] if a.stage in stages else []
        st["done"][a.stage] = {"at": datetime.now().isoformat(timespec="seconds"), "note": a.note}
        save(a.root, a.slug, st)
        if skipped:
            print("warning: marked %s done before %s. Run those first unless you skipped them on purpose."
                  % (a.stage, ", ".join(skipped)))
        nxt = next((s for s in stages if s not in st["done"]), None)
        print("%s done. next: %s" % (a.stage, nxt or "complete"))
        return 0

    if a.cmd == "status":
        st = load(a.root, a.slug)
        stages = plan(st)
        nxt = next((s for s in stages if s not in st["done"]), None)
        print("%s  mode=%s depth=%s" % (st["slug"], st["mode"], st["depth"]))
        for s in stages:
            print("  [%s] %s%s" % ("x" if s in st["done"] else " ", s, "   <- next" if s == nxt else ""))
        print("next: %s" % (nxt or "complete"))
        return 0

    if a.cmd == "list":
        if not os.path.isdir(a.root):
            print("no runs yet")
            return 0
        for slug in sorted(os.listdir(a.root)):
            if os.path.exists(path(a.root, slug)):
                st = load(a.root, slug)
                stages = plan(st)
                print("%-32s %s %d/%d" % (slug, st["mode"], len([s for s in stages if s in st["done"]]), len(stages)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
