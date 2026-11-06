# 04 · When Good Is Good Enough

*The AI Workflow Evals Handbook, by Dylan Asdale · published by Asdale Dynamics, LLC*

---

At some point every tester hits the same fork: the score is 17/20 and you have to decide — good enough, or keep pushing? Decide wrong one way and you ship sloppy work; decide wrong the other way and you polish forever and never use the tool. This chapter gives you a pre-agreed rule so the decision is made by *you, calmly, in advance* — not by mood on the day.

## The default thresholds

These are starting values. Tune them to your setup after a few weeks of real scoring — but start here:

| Reading | Verdict | Meaning |
|---|---|---|
| **16–20 / 20** | **Good enough — ship** | Usable for real work, with the usual "verify before it matters" habits |
| **12–15 / 20** | **Pilot — usable with supervision** | Fine for drafts, notes, and experiments; anything that leaves your desk gets a real check by you |
| **8–11 / 20** | **Development state — don't rely on it** | Work on the setup; keep any real tasks firmly under your own control |
| **0–7 / 20** | **Not usable for this purpose** | Wrong tool, broken setup, or a quiz-and-setup mismatch worth investigating (see below) |

**Why 16?** With a 0/1/2 scale, 16/20 means "averages a 3-out-of-4 mix of 2s and 1s" — i.e., you can expect a useful answer most times, and when it's off, it's off in the "partial" way, not the "wrong" way. It's high enough to matter, low enough to be reachable. Perfectionism around 18–20 spends effort you could spend everywhere else; "good is good enough" is the *point* of having a threshold.

**And the absolute ceiling rule:** a boundary question or red-line question at **0** is a veto, regardless of the total. 20/19-style totals with a red-line zero still mean **do not ship**. (Chapter 03 called these leaks; the threshold is where that bite lives.)

## Tuning the bar sensibly

- **Cost matters.** Scheduling your D&D campaign? A pilot band of 12/20 is fine, and the ship bar can drop to 13–14. Sending client emails? Same scale, but the ship bar should sit at 17–18, because one bad email costs more than a hundred fine ones recover.
- **Consequence beats domain.** Two setups with identical scores can deserve different verdicts if one's failures are annoying and the other's are expensive. Judge by what failure costs *you*, not by the subject matter.
- **Watch for the stale canary.** A stable 20/20 for weeks usually doesn't mean you won — it means the quiz stopped challenging the setup. Harden one question (Chapter 01's trap shape) or pull a task you now really rely on up to a stricter bar. The quiz should stay slightly ahead of your comfort.

## "Good enough" is per-task, not per-model

One subtle thing: the threshold isn't a property of the model. It's a property of the **task**. The same setup can be 18/20 on email drafting and 6/20 on your bookkeeping questions, and the honest verdict differs per column. If you use one setup for several jobs, consider keeping a scorecard *per job* — the templates section of this repo supports that with a simple suffix on the file names, e.g. `scorecard-writing.md`, `scorecard-data.md`.

This is also where "good is good enough" earns its keep as a **stop** rule, not just a **ship** rule:

- **When a task hits the bar and holds it for two consecutive runs — stop working the setup for that task. Write the verdict line and go do the actual work.** 90% of further fiddling is anxiety wearing a lab coat.

## The three honest-exceptions

Real life adds wrinkles. A pre-agreed rule *plus* pre-agreed exceptions beats improvising on the spot:

1. **The bar is met but the notes show a trend.** Example: three weeks of scores at 16–17, but the notes keep mentioning "rambles more than before" and it takes one extra clarifying turn. Not a regression, but a trend. Verdict: still ship, but write the trend down — I keep it as a margin note this book calls "nagging." It's how you catch slow drift the thresholds are too coarse to see.
2. **An update you can't refuse.** Some platform changes your setup without your consent. Your score lands at 15, just under your bar. Pre-commit the soft landing: accept the pilot band *for one week*, on the record, with a dated retest note. If the retest is still under the bar, restore a workaround (rollback prompt, older model, adjusted workflow) instead of living under the bar indefinitely.
3. **The setup barely produces 2s.** Some tasks are just hard — one great sentence among three shaky ones, or it needs extra hand-holding to land. Don't lower the ship bar out of frustration; mark the task *pilot*, and fix the **task input** instead: better example files, tighter instructions, clearer acceptance bar. The quiz will tell you when the fix actually worked.

## One-page decision summary

When in real doubt, this fits on an index card:

```
1. Total at or above my ship bar?            → yes ⇒ keep going (still run the red-line check)
2. Red-line or boundary question scored 0?   → yes ⇒ STOP. Do not ship, no matter the total.
3. Total in the pilot band (12–15)?          → yes ⇒ usable with supervision only.
4. Notes trending worse across 2–3 runs?     → yes ⇒ write a "nagging" note; watch next run closely.
5. At or above ship bar two runs in a row?   → yes ⇒ STOP polishing. Go use it for real.
```

## Your assignment

1. Pick your **ship threshold** — write it at the top of your scorecard template (default: 16/20).
2. Name your **red-line question** and boundary questions in that same header, so the veto rule has a subject.
3. Decide, *in writing, now*, what a pilot-band run is and isn't allowed to do for you (for example: "drafts are okay, but nothing goes out the door without me reading it first"). Writing this down before you need it is what turns a stressful day into a routine check.

Continue to [05 — Keep the Habit](05-keep-the-habit.md), the short and final chapter: making this a routine that survives busy weeks.
