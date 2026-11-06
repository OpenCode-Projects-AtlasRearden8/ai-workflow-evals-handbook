# 00 · Start Here — The Whole Method in Ten Minutes

*The AI Workflow Evals Handbook, by Dylan Asdale · published by Asdale Dynamics, LLC*

---

## The problem this handbook solves

Here's how most people "test" an AI setup. They get something working, they're impressed, and they stop. The setup becomes part of their week — drafting emails, summarizing documents, writing little helper scripts, organizing paperwork. It earns trust.

Then something shifts. The model gets updated. They tweak the prompt. They swap a step in the workflow. And the setup keeps *sounding* exactly as confident as it always did, while quietly getting worse at things they aren't looking at.

You can't prevent updates. You can't freeze your tools. But you can do something that sounds almost too simple: **keep a short, permanent quiz, ask the same ten questions every week, and write the scores down.**

That's it. That's the whole book. Everything else is how to do it well.

## Why a "canary quiz"

In old coal mines, miners brought a canary. The bird was more sensitive to bad air than people were, so as long as the canary seemed okay, the air was probably okay. If the canary dropped off the perch, you didn't need instrumentation to tell you to get out.

A canary quiz is the same idea for your AI setup. It is **not** a scientific benchmark. It's not trying to measure the model against the world. It's measuring *your* setup against *itself*, over time:

- Wrong direction? **Smoking canary:** your setup just got worse at something you care about.
- Same or better? **Canary fine:** breathe easy and get back to work.

Ten questions is the sweet spot. Fewer than ten and one lucky answer can fool you. More than ten and grading becomes a chore, and a chore you skip is a canary you don't have.

## The four moves

**1. Build the quiz.** Write ten questions that mirror how you actually use the tool — real tasks, phrased the way you'd really phrase them, including the messy or tricky ones. Chapter 01 walks you through it, and there's a fillable template.

**2. Score with a rubric.** Every answer gets a 0, 1, or 2 — same scale every time, single best answer captured in one sentence, note *why* in a few words. Chapter 02 shows you how, and how not to fool yourself.

**3. Compare after changes.** Any time something in the setup changes — model update, prompt tweak, workflow edit — rerun the quiz and lay the two scorecards side by side. Chapter 03 gives you the comparison rules, including the one silent-killer pattern to look for.

**4. Decide.** A simple, pre-agreed threshold tells you whether the new version is good enough, and a "red line" rule catches the rare-but-bad case where the total score looks fine and one critical answer collapsed. Chapter 04 covers this; it's shorter than you think.

## What you need

- The AI setup you already use (chatbot, local model, coding assistant — anything).
- A place to keep notes. A plain text or Markdown file is perfect. A paper notebook works too. If you like spreadsheets, they work — but they're optional.
- About 20–30 minutes to do the first round, then 15–20 minutes a week.

## What this isn't

- **Not medical advice.** I'm a nurse by training, so let me be extra clear: nothing in this handbook is healthcare guidance, and no AI setup should ever be treated as a clinical authority. This book is education about *AI tooling*, full stop. (If you're a healthcare worker building AI skills, welcome — the same safety rule applies to every domain: use AI for drafts and understanding, verify anything that matters against an authority you trust.)
- **Not a benchmark.** You're not competing with anyone or proving anything about models in general. A "low" score next to a friend's "high" score means nothing. The only comparison that matters is *your setup this week vs. your setup last week.*
- **Not automation.** This handbook is deliberately tool-free at its core. If you want automation later, I have a separate project, `prompt-regression-cli`, that automates the comparison step — but learn the habit first. The habit is what makes the tool worth having.

## The plan for this chapter-by-chapter reading path

1. **[01 — Build Your Canary Quiz](01-build-your-canary-quiz.md)** — pick ten questions that represent your real usage.
2. **[02 — Score With a Rubric](02-score-with-a-rubric.md)** — the 0/1/2 scale, graded honestly.
3. **[03 — Catch Regressions](03-catch-regressions.md)** — how to compare two scorecards and what patterns to fear.
4. **[04 — When Good Is Good Enough](04-when-good-is-good-enough.md)** — thresholds, red lines, and shipping decisions.
5. **[05 — Keep the Habit](05-keep-the-habit.md)** — the weekly routine, plus what to do when the habit starts slipping.

Then open the folder `templates/` and copy `canary-quiz-template.md` to start yours.

One more time, because it's the thesis of the whole book: **a score you didn't write down last week is a regression you can't spot this week.** Write it down. That's the whole trick.
