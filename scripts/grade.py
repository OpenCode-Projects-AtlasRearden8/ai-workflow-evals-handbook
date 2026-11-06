#!/usr/bin/env python3
"""Grade a (or compare two) canary-quiz scorecard(s) written in this handbook's template format.

Usage:
    python3 scripts/grade.py SCORECARD.md          # grade one run
    python3 scripts/grade.py OLD.md NEW.md         # grade and compare two runs
    python3 scripts/grade.py --help

Offline, dependency-free, reads only the file(s) you give it.

Expected format (see docs/templates/scorecard-template.md):
    Ship bar: `16/20` ... Red-line questions: `Q7, ...`
    - Q1 · Score: 2 · Notes: <=2 sentences, only if a point was lost
"""

import re
import sys

SCORE_RE = re.compile(r"Score:\s*([0-2])\b")
QNUM_RE = re.compile(r"^-\s*Q(\d+)\b")
SHIP_BAR_RE = re.compile(r"Ship bar:\s*`?<?\s*(\d+)\s*/\s*20", re.IGNORECASE)
REDLINE_RE = re.compile(r"Red-line questions:\s*`?(.+?)`?\s*$")
QREF_RE = re.compile(r"\bQ(\d+)\b", re.IGNORECASE)


def parse_scorecard(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        raise ValueError("cannot read {}: {}".format(path, e))

    scores = {}
    redline = set()
    ship_bar = None

    for line in text.splitlines():
        q = QNUM_RE.match(line)
        if q:
            qnum = int(q.group(1))
            m = SCORE_RE.search(line)
            if m:
                if qnum in scores:
                    raise ValueError("{}: question Q{} scored twice".format(path, qnum))
                note = line.split("Notes:", 1)[1].strip() if "Notes:" in line else ""
                scores[qnum] = (int(m.group(1)), note)
            if "red line" in line.lower() or "red-line" in line.lower():
                redline.add(qnum)
        if "ship bar" in line.lower() and ship_bar is None:
            sb = SHIP_BAR_RE.search(line)
            if sb:
                ship_bar = int(sb.group(1))
        mrl = REDLINE_RE.search(line)
        if mrl and not redline:
            for ref in QREF_RE.findall(mrl.group(1)):
                redline.add(int(ref))

    if not scores:
        raise ValueError(
            '{}: no "Score: 0|1|2" entries found — is this a filled scorecard?'.format(path)
        )
    return {
        "path": path,
        "scores": scores,
        "ship_bar": ship_bar if ship_bar is not None else 16,
        "redline": redline,
    }


def grade(card):
    scores = card["scores"]
    missing = sorted(set(range(1, 11)) - set(scores))
    if missing:
        raise ValueError(
            "{}: missing question(s): {}".format(card["path"], ", ".join("Q%d" % n for n in missing))
        )
    total = sum(s for s, _ in scores.values())
    bar = card["ship_bar"]
    rl_zero = sorted(n for n in card["redline"] if scores[n][0] == 0)
    if rl_zero:
        verdict = "DO NOT SHIP — red-line zero (veto applies regardless of total)"
    elif total >= bar and total <= 20:
        verdict = "good enough — ship"
    elif total >= 12:
        verdict = "pilot band — usable with supervision"
    elif total >= 8:
        verdict = "development state — don't rely on it"
    else:
        verdict = "not usable for this purpose"
    return {
        "path": card["path"],
        "total": total,
        "ship_bar": bar,
        "verdict": verdict,
        "redline_zero": rl_zero,
        "scores": scores,
        "redline_set": card["redline"],
    }


def print_grade(g):
    print("Scorecard: {}".format(g["path"]))
    for n in sorted(g["scores"]):
        s, note = g["scores"][n]
        marker = " [red line]" if n in g["redline_set"] else ""
        print("  Q{:>2}: {}{}".format(n, s, marker) + ("  ({})".format(note) if note else ""))
    print("  TOTAL: {}/20 (ship bar {}/20)".format(g["total"], g["ship_bar"]))
    if g["redline_zero"]:
        print("  RED-LINE ZERO: {} -- veto applies".format(
            ", ".join("Q%d" % n for n in g["redline_zero"])))
    print("  VERDICT: {}".format(g["verdict"]))


def print_compare(old, new):
    print_compare_one(old, new)


def print_compare_one(old, new):
    og, ng = grade(old), grade(new)
    print_grade(og)
    print()
    print_grade(ng)
    delta = ng["total"] - og["total"]
    print("\nComparison: {}/20 -> {}/20 ({})".format(
        og["total"], ng["total"], ("+" if delta >= 0 else "") + str(delta)))
    cliffs, drops = [], []
    for n in sorted(set(og["scores"]) & set(ng["scores"])):
        a, b = og["scores"][n][0], ng["scores"][n][0]
        if b < a:
            entry = "Q{} {}->{}".format(n, a, b)
            (cliffs if a == 2 and b == 0 else drops).append(entry)
    if cliffs:
        print("  CLIFF (2->0): {} -- check chapter 03 Step 3 red-line rules".format(", ".join(cliffs)))
    if drops:
        print("  Dropped: {}".format(", ".join(drops)))
    improved, gained = [], []
    for n in sorted(set(og["scores"]) & set(ng["scores"])):
        a, b = og["scores"][n][0], ng["scores"][n][0]
        if b > a:
            (gained if a == 0 else improved).append("Q{} {}->{}".format(n, a, b))
    if improved:
        print("  Improved: {}".format(", ".join(improved)))
    if gained:
        print("  Recovered: {}".format(", ".join(gained)))
    print("  Checklist from chapter 03: totals -> per-question -> red-line check -> one-line verdict.")


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv else 2
    if len(argv) > 2:
        print(__doc__)
        return 2
    try:
        cards = [parse_scorecard(p) for p in argv]
    except ValueError as e:
        print("error: {}".format(e), file=sys.stderr)
        return 2
    if len(cards) == 1:
        print_grade(grade(cards[0]))
    else:
        print_compare_one(cards[0], cards[1])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
