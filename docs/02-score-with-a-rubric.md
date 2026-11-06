# 02 · Score With a Rubric

*The AI Workflow Evals Handbook, by Dylan Asdale · published by Asdale Dynamics, LLC*

---

Scores are where vibes become data. This chapter gives you a scale so simple it fits on a sticky note, plus the honest-grading habits that make the numbers mean something.

## The scale

Every answer, every question, every week, gets exactly one of three grades:

| Score | Name | What it means | Full-sheet shorthand |
|---|---|---|---|
| **0** | **Fail** | Wrong, or confidently wrong, or it fails the question's specific checklist. If a boundary question, 0 means it invented an answer. | `0` |
| **1** | **Partial** | Substantially right but flawed: right answer, wrong detail; good draft, sloppy formatting; right but only after hand-holding you needed two extra turns for. | `1` |
| **2** | **Pass** | You'd accept this answer in real life with no fixes, or one trivial fix (a typo). It also states uncertainty where it should. | `2` |

Ten questions, so every full run is **out of 20**.

Why not a 1–10 scale, or 0–100? Because precision is a trap. When you give a 7, you start giving 7s to different levels of quality, and then "7 this week vs. 7 last week" means nothing. Three levels force honesty: you only have to defend a decision between *adjacent* grades, and 1–2 total is too much to overthink.

## Grading a task question (the ones without a "right answer")

For fact, trap, and boundary questions the grade is usually obvious. Task questions — "draft the email," "summarize this" — need a little structure so the grade isn't just a mood.

Before your *first* run, write a **one sentence acceptance bar** under each task question: what would make an answer a 2 *for you*. Example:

> *Q4. Draft a polite deadline-extension email to a supplier.*
> *Bar for a 2: names the right deadline, asks clearly for the extension, I'd send it after fixing only the name.*

When grading a task answer, run three quick checks in order; each check has an effect on the score:

1. **Is it wrong anywhere it matters?** (wrong detail, wrong tone for the audience, invented facts) → **0**. Don't round up. Confidently wrong is the failure mode this whole handbook exists to catch.
2. **Would you accept it with only trivial fixes?** (typo, one-word swap) → **2**.
3. **Everything in between** — right idea, real flaws, or needed extra back-and-forth → **1**.

If you're genuinely torn between 1 and 2: **give the 1.** Not because you're mean, but because your grading should be consistent-with-itself week over week, and "when torn, go lower" is a rule you can apply the same way every time. Consistency beats generosity; a slightly harsh-but-stable scale tells you more over time than a kind-but-wobbly one.

## The two paragraph rule (grading notes)

Under each question, after the score, write **up to one or two sentences** — no more — explaining what cost the point. Examples:

- `Q2 · 1 — right answer, invented the version number.` Wait, that one's an example of a note worth keeping... `Q2 · 1 — right steps, wrong cutoff date.`
- `Q6 · 2 — would send as-is.`
- `Q9 · 0 — invented a phone number for the boundary question.`

These notes are the most valuable part of the whole system. Scores tell you *that* something changed; notes tell you *what to fix*. And when you hit Chapter 03's regression check, the notes are how you tell "this question got worse" apart from "my standards drifted."

## Honest grading: the three ways you'll fool yourself

A rubric everyone can read is worthless if you grade differently every week. Watch for these three drift patterns — they're the common ones, and I've done all of them:

1. **Anchoring on the old score.** You remember the last run scored `2` here, so you lean toward `2` again. *Fix:* grade from the answer alone. Check your last scorecard only *after* finishing this one.
2. **Context generosity.** The AI has been helpful all week, so you're in a good mood and everything gets a 2. *Fix:* the three checks above, applied mechanically, especially "trivial fixes only."
3. **The effort bias.** You spent 40 minutes building this setup, so you *want* a good score. The result: a 20-point run that conceals real problems. *Fix:* remember the canary exists to give you bad news early. A slightly deflated score is the price of an alarm system that actually works.

## Grading boundaries, specifically

Boundary questions ("say 'I don't know' instead of guessing") get a special note:

- The setup **says it doesn't know** (or asks you for the missing fact): that's a **2**, even though the answer is "no answer." Pass means it behaved *correctly*, which here means *refusing to invent*.
- It hedges, hems, and eventually guesses anyway: **1**.
- It states an invented fact with confidence: **0**, and underline it in your notes — this is the single most development-critical behavior in the whole scale for any setup you use for real work.

## Your assignment

1. Grade your baseline run from Chapter 01 using the 0/1/2 scale, with the one-sentence acceptance bars written under every task question (do it *before* grading, this is a one-time setup).
2. Copy the scorecard into `templates/scorecard-template.md` — or keep grading in your own notes with the same structure. Keep the raw AI answers too (copy/paste them under the question or in a sibling file).
3. Grade a *second* run a day or two later, without looking at the first scorecard, then compare your two grades per question. Any question where your grades disagree by more than one point means your question (or your bar) is too fuzzy — tighten it now, while you're early.

When you have two full scorecards, you're ready for [03 — Catch Regressions](03-catch-regressions.md).
