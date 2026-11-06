# 03 · Catch Regressions

*The AI Workflow Evals Handbook, by Dylan Asdale · published by Asdale Dynamics, LLC*

---

A *regression* is when a change to your setup makes something worse without you noticing. Updates make them constantly — and the sneaky thing about regressions is that they usually come bundled with improvements, so the overall vibe stays positive while one important ability quietly dies. This chapter is a short, mechanical procedure to catch exactly that.

## When to run the comparison

You rerun the canary quiz and compare scorecards whenever **anything that could affect answers changes**:

- The model or tool updates (check the version; note it).
- You tweak your prompt, template, or instructions.
- You change the workflow (a new step, a different order, a new file format).
- You switch to a different model, tier, or local release.

Quarter-on-quarter, even with no changes, is worth a run too — some updates just *happen* silently.

## The comparison, four steps

You have two filled scorecards: **OLD** (last good, known state) and **NEW** (after the change). With both in front of you:

**Step 1 — Compare totals.** NEW total minus OLD total.

- Up or equal → keep going. (Still do Step 3's red-line check.)
- Down by **1–3 points** → a real regression signal. Small, but that's exactly what silent failures look like. Do Step 2 seriously.
- Down by **4+ points** → a strong regression signal. Something material probably broke. Step 2, seriously, and don't ship the new setup for real work until you understand it.

**Step 2 — Compare question-by-question.** For each of the ten questions:

- Same score → fine. Skip.
- Better (0→1, 0→2, 1→2) → good news; note what improved in case it was a side effect of something else.
- **Worse by one** (2→1, 1→0) → worth a note, not necessarily an alarm. Combined with a total drop, this tells you the shape of the failure.
- **Worse by two** (2→0) → the most important signal in the whole system. Any single 2→0, **even if the total went up overall**, is Step 3.

**Step 3 — The red-line check.** Look at your *red-line question* (the one from Chapter 01 whose failure would cost you) and any boundary question.

- If either dropped to a **0**, treat it as an emergency even with a perfect total score. Example: the setup drafts your client emails beautifully now, but it would also happily invent a phone number on a boundary probe. The average says "fine." The red line says "no."
- Read the *notes* under each dropped score. One sentence is usually enough to see what broke: bad formatting, version confusion, a newly confident tone, new habit of rambling until it says one wrong thing.

**Step 4 — The verdict, and writing it down.** End the comparison with one handwritten line in the margin (or under the scorecard):

> `NEW vs OLD: 15/20 → 17/20 · Q7 dropped 2→1 (rambles; loses the actual question) · green-lined, ship it.`

That one line is the log entry you'll thank yourself for in three months, because future-you will otherwise be guessing which change did what.

## The four patterns worth memorizing

Reading dozens of comparisons, the same four shapes keep coming back. Learn to recognize them by total alone:

| Pattern | What the totals say | What it actually means | Verdict |
|---|---|---|---|
| **Clean win** | Up 1–5, no red-line issues | The change worked, or it's a harmless model shift | Ship it |
| **Net-zero bleed** | Same total, but 1–2 questions traded (+1 here, −1 there) | Usually capability shifting under you; watch this trend for 2–3 more runs | Ship with notes |
| **The cliff** | Total crashes 4+ | Something material broke: changed instructions, format handling, a step got skipped | Stop, diagnose before use |
| **The leak** | Total up or flat, red-line or a 2→0 drop | Improvement in one place, sold an ability that matters | **Do not ship** for the affected task; fix or fence it off |

Quietly, **the leak** is the most common way real-life setups drift into trouble, and it's why the red-line check is a step, not a paragraph.

## What to do when you find a regression

Order matters here; do the cheap ones first:

1. **Diff your own changes.** Most regressions come from *you*, and that's great — it means it's fixable. Compare the current prompt/instructions/workflow to the last time you got a clean score.
2. **Roll back and re-run the quiz.** If the score returns to the old level, you've isolated the change. Now you can decide whether the change was necessary and *can it be repaired* (usually yes — often one sentence of instruction fixes it).
3. **Check for a silent model update.** Version numbers, release notes, a changed mood/diction. You can't undo these, but you can often compensate in your own instructions — or decide the new tradeoff is acceptable with your eyes open.
4. **If nothing explains it:** re-run the quiz once, entirely, the day after. Some regressions are flaky rather than systematic. A single flaky run isn't a verdict; two flaky runs in a row is.

## When your grades drift instead of the model

Sometimes a comparison looks like a regression and it isn't. The classic: you grade the same setup two weeks apart, and scores drop 2 points — but the *notes* under the dropped questions read like your standards tightened, not the model failing ("right idea, wanted more structure"). That's grading drift, not a regression.

Fixes that work: rewrite the acceptance bars to be concrete again, re-grade *both* scorecards back-to-back in one sitting for that week only, and use the shorter grading-notes format (it actively prevents drift).

## Your assignment

Fill one OLD scorecard now (even if nothing changed — you want a baseline before the next surprise). Then wait for your next real change, rerun the quiz, run the four steps, and handwrite the one-line verdict under both scorecards. Two comparisons from now, you'll be reading totals like a coal miner reads a canary — and that's the whole skill.

Continue to [04 — When Good Is Good Enough](04-when-good-is-good-enough.md).
