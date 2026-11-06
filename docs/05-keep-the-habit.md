# 05 · Keep the Habit

*The AI Workflow Evals Handbook, by Dylan Asdale · published by Asdale Dynamics, LLC*

---

Everything before this chapter is clever. This chapter is stubborn. The canary quiz only protects you if it happens regularly, so this page is about making the routine almost insultingly easy to keep — including on the weeks you don't feel like it.

## The weekly routine, end to end

**The ritual (or don't): weekly, ~15–20 minutes**

1. **Rerun the quiz.** Open your question file, ask all ten questions, in order, no skipping. If your setup changes between questions (say, a chat session), that's fine — real life does that too. Don't restart to make it "fair." This is a canary, not a lab.
2. **Grade immediately, in one sitting.** 0/1/2 per question, one-line note where a point was dropped. Fresh eyes, same sitting, before you read anything about the old runs.
3. **Log the scorecard.** New file: `2026-11-06.md` or entry #7 of the same file. Date it in the header. Model/version in the header too.
4. **Glance at trend.** Look back two runs: total, plus any question hit twice. Two minutes. Done.

Then compare only when something changed (Chapter 03), and decide only when the comparison is done (Chapter 04). Weekly is about habit; changing weeks are when the quiz pays for itself.

## The maintenance calendar (light)

| Interval | Task | Time |
|---|---|---|
| Weekly | Rerun + grade + log | 15–20 min |
| Monthly | Skim all notes since the last month; look for any repeated complaint | 10 min |
| Quarterly, or after any big change | Retire stale questions, add harder ones, re-pin the acceptance bars | 30 min |
| Never — *almost* never | Rewrite the whole quiz from scratch | only if your actual usage changed wholesale |

## Making it stick (plain tools only)

- **Anchor it to something that already happens.** Pair the quiz with your regular setup check, your Sunday grid-review, Monday morning coffee — whatever existing routine you already trust. Attach new habits to old ones; the anchoring effect is real.
- **Keep the question file where you *can't forget it exists*** — pinned note, starred file, the same folder you open to start your work week. The friction is in *remembering to begin*, not in the grading. Solve remembering; grading takes care of itself.
- **Use the pre-committed thresholds.** When the scorecard is done, the verdict is a lookup, not a debate. Chapter 04's index card exists because deciding at quiz-time is where people stall out.
- **Accept and record "messy runs."** If a week is noisy — you got interrupted, you graded tired — log it anyway, with a "noisy run" note, instead of skipping. A noisy logged run still tells you far more than a skipped one.
- **Two misses and a rescue plan.** If you miss two consecutive weeks, don't guilt-spiral: run the quiz once, note "back after a break — treat the last logged run as OLD and this as NEW," and see whether anything drifted during the silence. That's it. The system is designed to forgive gaps; the important thing is to come back to it rather than letting a missed week end the whole habit.

## When you should go deeper than this book

This system is deliberately minimal, and for most people, most of the time, that's the feature. Its honest limits:

- **Ten questions is a sample, not a survey.** Confidence intervals around ten questions are wide. You're detecting *gross* regressions, not subtle ones. If a failure mode keeps squeaking into your notes, *add a question about it* — that's the system growing with you.
- **Human grading scales like anything human: badly.** Past maybe two or three scorecards per week, grading gets tired and inconsistent (Chapter 02's drift rules help, but only so much). That's the point to graduate to automation — my separate project `prompt-regression-cli` does exactly this rerun-and-compare loop for you, using the same scorecards as input, with an offline-friendly setup.
- **This book teaches judgment, not statistics.** Nothing here replaces careful measurement when you genuinely need to know "how much worse" in a rigorous sense. If you get to a point where you need that rigor — say, choosing between two models on cost, or documenting degradation for stakeholders — you'll want proper eval tooling and larger question sets, and you'll be well-prepared to learn them, because you already know what the numbers are *for*.

## The end (which is really the start)

That's the whole handbook: ten fixed questions, a three-level rubric, a comparison ritual, a pre-agreed bar. Four small habits, anchored on thirty minutes a week, that turn "I think it's fine?" into "my setup scored 16 last week, 17 this week, nothing red-lined — go."

The coal miner's canary never made the mines safer by being a sophisticated instrument. It made them safer by being there, by being sensitive, and by being looked at. Yours is the same.

Good luck — and score honestly. · *Dylan*

---

*Published by Asdale Dynamics, LLC. This handbook is education about AI tooling; it is not professional, medical, or legal advice. Copyright (c) 2026 Asdale Dynamics, LLC — MIT licensed.*
