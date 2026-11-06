# The AI Workflow Evals Handbook

*Test your AI setups before you trust them — a beginner manual by Dylan Asdale, published by Asdale Dynamics, LLC.*

**Copyright (c) 2026 Asdale Dynamics, LLC. MIT licensed. See [LICENSE](LICENSE).**

---

Hi, I'm Dylan. I'm a registered nurse turned AI author, and I explain AI the same way a friend would: plain English, step by step, never condescending.

Here's a mistake almost everybody makes with AI tools. They try a new setup once, it does something impressive, and they quietly decide it works. Then three months and six updates later, it's quietly failing half the time and nobody noticed — because nobody ever wrote down what "working" looked like in the first place.

This handbook fixes that. It's not a lecture about AI safety and it's not a programmer's eval framework. It's a repeatable set of *habits* you can do with a text editor and twenty minutes a week:

1. **Build a ten-question canary quiz** — a small, permanent test set that represents what you *actually* use your AI setup for. Like the canary in the coal mine: if the canary is fine, you're probably fine.
2. **Score the answers with a rubric** — the same simple 0/1/2 scale every time, so your scores mean something across weeks and models.
3. **Spot regressions after an update** — rerun the quiz whenever anything changes (model update, new prompt, new workflow) and catch the things that got *worse*, not just the things that got better.
4. **Decide when good is good enough** — a sane rule for shipping and for stopping, so you're neither paralyzed nor careless.

Everything ships with fillable templates, a filled-in example you can copy, and a tiny offline grading script (plain Python, no dependencies).

## What's in the box

```
docs/
  00-start-here.md            Read this first: the whole method in 10 minutes
  01-build-your-canary-quiz.md  Pick your ten questions
  02-score-with-a-rubric.md     The 0/1/2 scale and how to use it honestly
  03-catch-regressions.md       Compare scorecards before/after a change
  04-when-good-is-good-enough.md  Thresholds, red lines, and shipping rules
  05-keep-the-habit.md          The 20-minute weekly routine + troubleshooting
  templates/                    Fillable quiz, rubric, scorecard + worked example
site/                           A polished static HTML version of the manual
scripts/grade.py                Optional helper: grade a filled scorecard offline
scripts/check.sh                Self-tests for this repo's files and links
```

No accounts, no API keys, no cloud calls, no personal data. Everything runs locally with a text editor; Python is only needed if you want `grade.py` to do the arithmetic for you.

## How this is different from my other test-related projects

If you've landed here from my catalog, quick orientation — these three projects are siblings, not duplicates:

| Project | What it is | The one-liner |
|---|---|---|
| **This handbook** | A beginner manual of **repeatable testing habits** | "How and why to test your own AI setups, by hand, forever." |
| **prompt-regression-cli** | A **command-line tool** that automates prompt regression checks | "Run the diff so I don't have to." |
| **when-ai-gets-it-wrong-guide** | **Failure stories** and what they teach | "Learn from real mistakes." |

This one is deliberately tool-free at its core. You can do every exercise here with a sticky note and a mug of coffee. If you later want automation, the CLI picks up right where this manual's habits leave off — and the habits make the tool worth having.

## Who it's for

- Beginners who use AI tools (chatbots, coding assistants, local models, agents) and want to stop flying blind — no coding background needed.
- Small-business owners and authors who've folded AI into real work and need to know when an update breaks something.
- Healthcare workers curious about AI tooling: **education only, never medical advice.** Nothing here should ever be used to make clinical decisions; see "What this isn't" in [docs/00-start-here.md](docs/00-start-here.md).

## How to use it

Reading path: start at [`docs/00-start-here.md`](docs/00-start-here.md) and go in order — it's about an hour of reading for a lifetime habit. Prefer a browser? Open `site/index.html` (it's plain HTML with inline CSS — no install, works offline).

To grade a filled-in scorecard offline:

```bash
python3 scripts/grade.py docs/templates/example-scorecard.md
```

To run this repo's own self-checks:

```bash
bash scripts/check.sh
```

## About Dylan and Asdale Dynamics, LLC

Dylan Asdale is a registered nurse turned AI author and the founder of **Asdale Dynamics, LLC** (Indiana, formed 2026), which publishes beginner-friendly AI education: books, guides, and practical tools — including *The Massive AI Manual* and the hub at `dylanasdale.github.io`. The LLC's projects are local-first, tested, and free of secrets or personal data.

This handbook, and every file in this repo, is published by **Asdale Dynamics, LLC**.

## License

MIT — see [LICENSE](LICENSE). Copy the templates freely; the whole point is that you keep running the habit.
