#!/usr/bin/env python3
"""Build docs/demo.svg, an animated terminal for the README, from docs/demo.txt.

The SVG uses SMIL animation, so it plays inside GitHub READMEs and any browser
with no JavaScript. Commands type out, output lines appear, then it loops.

    python3 docs/make_demo.py
"""
import html
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
W, PAD, LH, FS = 860, 28, 23, 14
CHAR = FS * 0.6  # monospace advance width
COLORS = {">": "#f4f3ef", "$": "#f4f3ef", "~": "#7d7a73", "!": "#e0a84a", "": "#b9b6ae"}


def load():
    lines = []
    for raw in open(os.path.join(HERE, "demo.txt"), encoding="utf-8"):
        raw = raw.rstrip("\n")
        if not raw.strip() or raw.startswith("#"):
            continue
        kind = raw[0] if raw[0] in "$>~!" else ""
        text = raw[2:] if kind else raw
        lines.append((kind, text))
    return lines


def build():
    lines = load()
    top = 46
    height = top + PAD + len(lines) * LH + PAD
    t, out = 0.6, []
    for i, (kind, text) in enumerate(lines):
        y = top + PAD + i * LH + FS
        x = PAD
        prefix = {"$": "$ ", ">": "> ", "!": "verdict "}.get(kind, "")
        full = prefix + text
        color = COLORS[kind]
        typed = kind in "$>"
        dur = min(1.2, 0.018 * len(full)) if typed else 0.0
        width = len(full) * CHAR + 4
        cid = "c%d" % i
        weight = ' font-weight="600"' if kind in ">!" else ""
        body = html.escape(full)
        if kind == "$":
            body = '<tspan fill="#7d7a73">$ </tspan>' + html.escape(text)
        if kind == "" and text.split(" ", 1)[0] in ("yes", "captured", "+"):
            head, rest = (text.split(" ", 1) + [""])[:2]
            body = '<tspan fill="#4cc38a">%s</tspan> %s' % (html.escape(head), html.escape(rest))
        if kind == "" and text.startswith(("Quotes:", "Claims:")):
            color = "#4cc38a"
        if kind == "!":
            body = ('<tspan fill="#7d7a73">verdict </tspan><tspan fill="#e0a84a">%s</tspan>' % html.escape(text.split(" ", 1)[0])
                    + '<tspan fill="#f4f3ef"> %s</tspan>' % html.escape(text.split(" ", 1)[1] if " " in text else ""))
        # SVG text collapses repeated spaces; keep column alignment with no-break spaces.
        body = re.sub(r"(?<=[^<]) {2,}", lambda m: "\u00a0" * len(m.group()), body)
        if typed:
            # Reveal the line left to right in steps, like typing.
            out.append('<clipPath id="%s"><rect x="%d" y="%d" width="0" height="%d">'
                       '<animate attributeName="width" from="0" to="%.0f" begin="loop.begin+%.2fs" dur="%.2fs" '
                       'calcMode="discrete" values="%s" fill="freeze"/>'
                       '<set attributeName="width" to="0" begin="loop.begin"/></rect></clipPath>'
                       % (cid, x - 2, y - FS, LH, width, t, dur,
                          ";".join("%.0f" % (width * k / max(1, len(full))) for k in range(len(full) + 1)) ))
            out.append('<text x="%d" y="%d" fill="%s"%s clip-path="url(#%s)">%s</text>' % (x, y, color, weight, cid, body))
            t += dur + 0.3
        else:
            out.append('<text x="%d" y="%d" fill="%s"%s opacity="0">%s'
                       '<set attributeName="opacity" to="1" begin="loop.begin+%.2fs"/>'
                       '<set attributeName="opacity" to="0" begin="loop.begin"/></text>'
                       % (x, y, color, weight, body, t))
            t += 0.55 if kind == "!" else 0.18
    total = t + 5.0
    svg = """<svg xmlns="http://www.w3.org/2000/svg" width="%(w)d" height="%(h)d" viewBox="0 0 %(w)d %(h)d" role="img" aria-label="A Wedge run in the terminal: fetching reviews, mining complaints, verifying every quote, and a PIVOT verdict">
<rect width="%(w)d" height="%(h)d" rx="14" fill="#141413"/>
<rect width="%(w)d" height="38" rx="14" fill="#1d1d1b"/><rect y="24" width="%(w)d" height="14" fill="#1d1d1b"/>
<circle cx="22" cy="19" r="6" fill="#3a3a37"/><circle cx="42" cy="19" r="6" fill="#3a3a37"/><circle cx="62" cy="19" r="6" fill="#3a3a37"/>
<text x="%(mid)d" y="24" text-anchor="middle" fill="#7d7a73" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="12">wedge</text>
<rect width="0" height="0"><animate id="loop" attributeName="width" from="0" to="0" begin="0s;loop.end" dur="%(total).2fs"/></rect>
<g font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="%(fs)d" xml:space="preserve" style="white-space:pre">
%(body)s
</g></svg>
""" % {"w": W, "h": height, "mid": W // 2, "total": total, "fs": FS, "body": "\n".join(out)}
    path = os.path.join(HERE, "demo.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote %s (%d lines, %.1fs loop)" % (path, len(lines), total))


if __name__ == "__main__":
    build()
