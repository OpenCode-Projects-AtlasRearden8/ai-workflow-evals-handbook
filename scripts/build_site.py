#!/usr/bin/env python3
"""Build the static HTML site/ pages from shared parts + per-page content.

Keeps every page self-contained (Power-style inline CSS via a single <style> block),
so iterations stay consistent. Run: python3 scripts/build_site.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

CSS = """
  :root { color-scheme: light; }
  * { box-sizing: border-box; }
  body {
    margin: 0; background: #faf6ef; color: #2b2622;
    font-family: ui-serif, Georgia, "Times New Roman", serif;
    line-height: 1.65; font-size: 17px;
  }
  header.site { background: #233b3a; color: #f6f1e7; padding: 2.4rem 1rem 2rem; }
  header.site .inner { max-width: 780px; margin: 0 auto; }
  header.site .kicker { font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: .78rem; letter-spacing: .14em; text-transform: uppercase; color: #9fc5b8; }
  header.site h1 { margin: .5rem 0 .35rem; font-size: clamp(1.7rem, 5vw, 2.6rem); line-height: 1.15; font-weight: 700; }
  header.site p.sub { margin: 0; font-size: 1.06rem; color: #d9e4dd; font-style: italic; }
  nav.chapters { background: #1b2f2e; padding: .65rem 1rem; position: sticky; top: 0; z-index: 5; box-shadow: 0 1px 6px rgba(20,30,28,.25); }
  nav.chapters .inner { max-width: 780px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: .4rem; }
  nav.chapters a { color: #cfe0d8; text-decoration: none; font-family: ui-monospace, Menlo, monospace; font-size: .78rem; padding: .32rem .7rem; border-radius: 999px; border: 1px solid #40595a; }
  nav.chapters a:hover { background: #2c4a48; color: #fff; }
  nav.chapters a.here { background: #c96f37; border-color: #c96f37; color: #fff; font-weight: 700; }
  main { max-width: 780px; margin: 0 auto; padding: 2.2rem 1rem 3rem; }
  h2 { font-size: 1.45rem; margin: 2.2rem 0 .6rem; color: #1f4f46; border-bottom: 2px solid #e4d9c6; padding-bottom: .25rem; }
  h3 { font-size: 1.1rem; margin: 1.6rem 0 .4rem; color: #8a4a22; }
  p { margin: .7rem 0; }
  .lede { font-size: 1.12rem; color: #4a4238; }
  strong { color: #173b34; }
  a { color: #b4541f; }
  code, .mono { font-family: ui-monospace, Menlo, monospace; font-size: .88em; background: #f0e8d8; padding: .1em .35em; border-radius: 4px; }
  blockquote { margin: 1.2rem 0; padding: .8rem 1.1rem; background: #fdf2e3; border-left: 4px solid #c96f37; border-radius: 0 8px 8px 0; font-style: italic; }
  table { border-collapse: collapse; width: 100%; margin: 1.1rem 0; font-size: .95rem; }
  th { background: #233b3a; color: #f6f1e7; text-align: left; font-family: ui-monospace, Menlo, monospace; font-size: .78rem; letter-spacing: .06em; text-transform: uppercase; }
  th, td { padding: .55rem .7rem; border: 1px solid #e0d5c0; vertical-align: top; }
  tr:nth-child(even) td { background: #f5eee0; }
  .card { background: #fff; border: 1px solid #e6dcc9; border-radius: 12px; padding: 1.4rem 1.5rem; margin: 1.4rem 0; box-shadow: 0 2px 10px rgba(120, 90, 40, .06); }
  .card h3 { margin-top: 0; }
  ol, ul { padding-left: 1.4rem; }
  li { margin: .35rem 0; }
  .tally { font-family: ui-monospace, Menlo, monospace; font-size: .95rem; background: #1b2f2e; color: #d9e4dd; border-radius: 8px; padding: 1rem 1.2rem; margin: 1.2rem 0; white-space: pre-wrap; line-height: 1.55; }
  .tally b, .tally .em { color: #ffb473; font-weight: 700; }
  .tally code { background: none; color: #ffd9b8; padding: 0; }
  .stamp { display: inline-block; font-family: ui-monospace, Menlo, monospace; font-size: .74rem; letter-spacing: .12em; text-transform: uppercase; color: #8a4a22; border: 1px dashed #d9a272; border-radius: 6px; padding: .25rem .6rem; margin-bottom: 1rem; }
  footer.site { max-width: 780px; margin: 0 auto; padding: 2rem 1rem 3.5rem; color: #7d7264; font-size: .86rem; border-top: 1px solid #e6dcc9; }
  footer.site a { color: #a14a17; }
""".strip()

NAV = [
    ("index.html", "Start here"),
    ("canary-quiz.html", "01 · Canary quiz"),
    ("rubric.html", "02 · Rubric"),
    ("regressions.html", "03 · Regressions"),
    ("good-enough.html", "04 · Good enough"),
    ("habit.html", "05 · Habit"),
    ("templates.html", "Templates"),
]


def page(title, description, kicker, headline, subtitle, here, body):
    nav = "\n".join(
        '<a{cls} href="{href}">{label}</a>'.format(
            cls=' class="here"' if href == here else "", href=href, label=label
        )
        for href, label in NAV
    )
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<style>
{css}
</style>
</head>
<body>

<header class="site">
  <div class="inner">
    <div class="kicker">{kicker}</div>
    <h1>{headline}</h1>
    <p class="sub">{subtitle}</p>
  </div>
</header>

<nav class="chapters"><div class="inner">
{nav}
</div></nav>

<main>
{body}
</main>

<footer class="site">
  <p>This manual is published by <strong>Asdale Dynamics, LLC</strong> — Dylan Asdale is a registered nurse turned AI author; the LLC publishes beginner-friendly AI education, books, guides, and practical tools (local-first, no secrets, no personal data).</p>
  <p>Education about AI tooling only — not professional, medical, or legal advice. MIT licensed: Copyright (c) 2026 Asdale Dynamics, LLC.</p>
</footer>

</body>
</html>
""".format(
        title=title,
        description=description,
        css=CSS,
        kicker=kicker,
        headline=headline,
        subtitle=subtitle,
        nav=nav,
        body=body,
    )


PAGES = {}

PAGES["canary-quiz.html"] = dict(
    title="01 · Build Your Canary Quiz — The AI Workflow Evals Handbook",
    description="Pick ten permanent questions that mirror how you really use your AI setup: workhorses, a red line, a weak spot, one messy prompt, and one thing you don't yet trust.",
    kicker="Chapter 01 · The ten questions",
    headline="Build your canary quiz.",
    subtitle="The quiz must look like your real life, not like the AI's best day.",
    here="canary-quiz.html",
    body="""<span class="stamp">Your canary quiz is ten permanent questions — permanent so scores stay comparable</span>

<p class="lede">Sit down with your notes (or your memory) and answer these. Keep it honest; nobody's watching.</p>

<ol>
  <li><strong>What are the three things I use this setup for most?</strong> Those are your workhorse categories. Spend about <strong>six of your ten questions</strong> on them — two per category.</li>
  <li><strong>What's the one task where a mistake would actually cost me?</strong> Money, time, reputation, or safety. That gets <strong>one</strong> question, and it becomes your <em>red line</em> in chapters 03–04: the answer where any score of 0 is an emergency, regardless of the total.</li>
  <li><strong>What kind of task does the setup usually stumble on?</strong> You already know the weak spot — the math it fumbles, the citation it invents, the formatting it mangles. That gets <strong>one</strong> question. A quiz that contains only what the AI is good at will never warn you.</li>
  <li><strong>What's a realistic messy version of your prompts?</strong> Include <strong>one</strong> question phrased the way you'd actually type it: short, half-explained, maybe a typo. That's reality.</li>
  <li><strong>What do you <em>wish</em> you used it for but don't yet trust it for?</strong> Include <strong>one</strong> question here too. Watching that score over time tells you exactly when the setup graduates to usable — in data, not vibes.</li>
</ol>
<p>That's 6 + 1 + 1 + 1 + 1 = <strong>ten</strong>. The allocation is a starting recipe, not a law.</p>

<h2>The four question shapes</h2>
<table>
  <tr><th>Shape</th><th>What it looks like</th><th>Why it's in the quiz</th></tr>
  <tr><td><strong>Fact</strong></td><td>“What setting do I change to do X?” — a checkable right answer.</td><td>Easy to grade honestly; a 0 or a 2 is unambiguous.</td></tr>
  <tr><td><strong>Task</strong></td><td>“Write the reply to this scenario I keep facing.”</td><td>Tests what you actually use it for, graded against your own acceptance bar.</td></tr>
  <tr><td><strong>Trap</strong></td><td>A known-fumble query; a question containing a correction (“actually the deadline is Friday, not Monday”); a prompt shaped to invite a confident wrong answer.</td><td>The early-warning system: degrading setups usually degrade here first.</td></tr>
  <tr><td><strong>Boundary</strong></td><td>“I don't actually know X — say so instead of guessing.”</td><td>Tests the failure mode you care about most: confidence without knowledge.</td></tr>
</table>
<p>If you're only sure of one thing, include plenty of boundary questions. Getting loud and wrong is worse than politely asking you to double-check.</p>

<h2>Locking down the grading window</h2>
<p>Two runs must be comparable, so the questions are <strong>fixed</strong> — identical wording, week after week:</p>
<ul>
  <li>Keep the question file sacred: no paraphrasing on the fly, no “let me just ask it slightly differently.” <em>Slightly differently is a different test.</em></li>
  <li>Retire a question on purpose (with a date note) when it no longer matters; expect a week or two of fuzzy comparisons afterward.</li>
  <li>For task questions, freeze the given material <em>inside the question itself</em> — the mock email, the sample document — so inputs never drift.</li>
</ul>

<h2>Anti-patterns to avoid</h2>
<ul>
  <li><strong>The showcase quiz.</strong> Ten questions the AI always aces. Feels great, tells you nothing. A canary that never sings in danger is a pet.</li>
  <li><strong>The exam-style quiz.</strong> Obscure trivia and seventeen-digit arithmetic. Degrading trivia tells you nothing about <em>your tasks</em> getting worse — that's the actual thing you're testing.</li>
  <li><strong>The living quiz.</strong> Fresh questions every week feels up-to-date and kills comparability. Change questions on purpose, not casually.</li>
  <li><strong>The vibe grade.</strong> “Seemed pretty good” is not a score. Chapter 02 fixes that with a scale too simple to weasel.</li>
</ul>

<h2>Your assignment</h2>
<div class="tally">1. Copy <code>docs/templates/canary-quiz-template.md</code> (or grab it from the <a style="color:#ffb473" href="templates.html">templates page</a>)
2. Write your ten questions with the 6/1/1/1/1 recipe.
3. Run the quiz once as a baseline. If any question can't be graded in <b>about 15 seconds</b>, rewrite it now.
4. Next: <a style="color:#ffb473" href="rubric.html">chapter 02 · score with a rubric</a>.</div>

<blockquote>One more time, because it's the thesis of the whole book: <strong>a score you didn't write down last week is a regression you can't spot this week.</strong></blockquote>""",
)

PAGES["rubric.html"] = dict(
    title="02 · Score With a Rubric — The AI Workflow Evals Handbook",
    description="The 0/1/2 grading scale: fail, partial, pass. How to grade task questions honestly,迟到 boundary questions, and the three ways you'll fool yourself.",
    kicker="Chapter 02 · Where vibes become data",
    headline="Score with a rubric.",
    subtitle="A scale so simple it fits on a sticky note — plus the honest-grading habits that make it mean something.",
    here="rubric.html",
    body="""<span class="stamp">Ten questions × three possible grades = a run out of 20</span>

<p class="lede">Every answer, every question, every week, gets exactly one of three grades:</p>

<table>
  <tr><th>Score</th><th>Name</th><th>What it means</th></tr>
  <tr><td><strong>0</strong></td><td><strong>Fail</strong></td><td>Wrong, or <em>confidently</em> wrong, or it fails the question's specific checklist. On a boundary question, 0 = it invented an answer.</td></tr>
  <tr><td><strong>1</strong></td><td><strong>Partial</strong></td><td>Substantially right but flawed: right idea, real problems; good draft, sloppy details; or you needed extra back-and-forth.</td></tr>
  <tr><td><strong>2</strong></td><td><strong>Pass</strong></td><td>Acceptable in real life with only trivial fixes (a typo). It also states uncertainty where it should.</td></tr>
</table>

<p><strong>Why not a 1–10 scale?</strong> Because precision is a trap. A “7” given today and a “7” given next week describe different quality levels, and then “7 vs. 7” means nothing. Three levels force honesty: you only have to defend a decision between adjacent grades.</p>

<h2>Grading order — mechanical, every time</h2>
<div class="tally">1. Wrong anywhere it matters?        → 0.  Don't round up.
2. Acceptable with only trivial fixes? → 2.
3. Everything in between?              → 1.
4. Torn between 1 and 2?               → 1.  (When torn, go lower.</div>
<p><strong>“When torn, go lower” isn't meanness</strong> — it's consistency-with-yourself week over week, and a slightly harsh-but-stable scale always outlives a kind-but-wobbly one.</p>

<h2>Task questions: write the bar first</h2>
<p>Before your <em>first</em> run, write a one-sentence <strong>acceptance bar</strong> under every task question — what makes that a 2 <em>for you</em>:</p>
<blockquote>Q4. <em>Draft a polite deadline-extension email to a supplier.</em><br>Bar for a 2: names the right deadline, asks clearly, I'd send it after fixing only the name.</blockquote>

<h2>Boundary questions, specifically</h2>
<ul>
  <li>Says “I don't know” or asks for the missing fact → <strong>2</strong> (pass = behaving correctly, which here means <em>refusing to invent</em>).</li>
  <li>Hedges, hems, and eventually guesses anyway → <strong>1</strong>.</li>
  <li>States an invented fact with confidence → <strong>0</strong>, and underline it. This is the single most development-critical behavior in the scale for any setup used for real work.</li>
</ul>

<h2>The two-sentence note</h2>
<p>After each question, write <strong>up to two sentences</strong> on what cost the point. That's it:</p>
<div class="tally">Q2 · 1 — right steps, wrong cutoff date.
Q6 · 2 — would send as-is.
Q9 · 0 — invented a phone number on a boundary probe.</div>
<p>These notes are the most valuable part of the whole system. Scores tell you <em>that</em> something changed; the notes tell you <em>what to fix</em> — and they're how chapter 03 tells “the setup got worse” apart from “my standards drifted.”</p>

<h2>The three ways you'll fool yourself</h2>
<ol>
  <li><strong>Anchoring on the old score.</strong> You remember it got a 2 last week, so you lean toward 2 again. <em>Fix:</em> grade from the answer alone; check last run's card only after finishing this one.</li>
  <li><strong>Context generosity.</strong> The AI has been helpful all week, so everything gets a 2. <em>Fix:</em> the mechanical grading order, especially “trivial fixes only.”</li>
  <li><strong>The effort bias.</strong> You spent 40 minutes building this, so you <em>want</em> a good score. <em>Fix:</em> the canary exists to give you bad news early; a slightly deflated score is the price of an alarm system that actually works.</li>
</ol>

<h2>Your assignment</h2>
<div class="tally">1. Write the one-sentence acceptance bars (once, before grading).
2. Grade the baseline run with 0/1/2 and the two-sentence notes.
3. Keep the raw answers — the notes point back to them.
4. Next: <a style="color:#ffb473" href="regressions.html">chapter 03 · catch regressions</a>.</div>""",
)

PAGES["regressions.html"] = dict(
    title="03 · Catch Regressions — The AI Workflow Evals Handbook",
    description="Compare two scorecards after any change: totals first, then per-question, then the red-line check — including 'the leak', where the total looks fine and one ability quietly died.",
    kicker="Chapter 03 · The comparison ritual",
    headline="Catch regressions.",
    subtitle="A regression is when a change makes something worse without you noticing. Here's the mechanical way to catch one.",
    here="regressions.html",
    body="""<span class="stamp">Run the comparison when anything changes — model, prompt, workflow, or nothing at all for a quarter</span>

<p class="lede">Regenergressions are sneaky because they usually arrive bundled with improvements: the overall vibe stays positive while one important ability quietly dies. This is a short, four-step procedure — you need two filled scorecards, <strong>OLD</strong> and <strong>NEW</strong>.</p>

<h2>The four steps</h2>
<ol>
  <li><strong>Compare totals.</strong> NEW − OLD: up or equal → keep going (still do step 3); down 1–3 → real signal, take step 2 seriously; down 4+ → strong signal, stop until understood.</li>
  <li><strong>Question-by-question.</strong> Same → skip. Better → note it. Worse by one → worth a note. <strong>Worse by two (2→0) → step 3, even if the total went up.</strong></li>
  <li><strong>Red-line check.</strong> If your red-line question or any boundary probe dropped to <strong>0</strong>, that's an emergency <em>regardless of the total</em>. Then read every note under a dropped score — one sentence usually shows exactly what broke.</li>
  <li><strong>Write the one-line verdict</strong> in the margin of the new scorecard. That log entry is what future-you will otherwise be guessing about.</li>
</ol>

<h2>The verdict line, by example</h2>
<div class="tally">NEW vs OLD: 15/20 → 17/20 · Q7 dropped 2→1 (rambles; loses the actual question)
· red-line OK · green-lined, ship it.</div>

<h2>The four patterns worth memorizing</h2>
<table>
  <tr><th>Pattern</th><th>Totals say</th><th>What it means</th><th>Verdict</th></tr>
  <tr><td><strong>Clean win</strong></td><td>Up 1–5, no red-line issues</td><td>The change worked, or it's a harmless model shift</td><td>Ship it</td></tr>
  <tr><td><strong>Net-zero bleed</strong></td><td>Same total, questions traded</td><td>Capability shifting under you; watch the trend 2–3 runs</td><td>Ship with notes</td></tr>
  <tr><td><strong>The cliff</strong></td><td>Total crashes 4+</td><td>Something material broke</td><td>Stop; diagnose before use</td></tr>
  <tr><td><strong>The leak</strong></td><td>Up or flat, red-line 0 or a 2→0</td><td>An improvement in one place, a sold-out ability elsewhere</td><td><strong>Do not ship</strong> the affected task; fix or fence it off</td></tr>
</table>
<p><strong>The leak</strong> is the quiet way real setups drift into trouble — it's why the red-line check is a numbered step, not a paragraph.</p>

<h2>What to do when you find one</h2>
<ol>
  <li><strong>Diff your own changes first.</strong> Most regressions come from you — which is great, because those are fixable.</li>
  <li><strong>Roll back and re-run the quiz.</strong> Score returns → change isolated; usually one sentence of instruction repairs it.</li>
  <li><strong>Check for a silent model update.</strong> You can't undo it, but you can compensate — or consciously accept the tradeoff.</li>
  <li><strong>Nothing explains it?</strong> Re-run once, a day later. Flaky runs exist; one flaky run isn't a verdict, two in a row is.</li>
</ol>

<h2>When the model didn't drift — your grading did</h2>
<p>Sometimes scores drop… but the notes read like your standards tightened (“right idea, wanted more structure”). That's grading drift. <em>Fixes:</em> rewrite the acceptance bars to be concrete, re-grade both cards back-to-back in one sitting, and keep notes short — the two-sentence rule actively prevents drift.</p>

<h2>Your assignment</h2>
<div class="tally">1. Fill one OLD scorecard now, even if nothing changed. Baselines come before surprises.
2. At your next real change: rerun, compare, handwrite the one-line verdict.
Next: <a style="color:#ffb473" href="good-enough.html">chapter 04 · when good is good enough</a>.</div>""",
)

PAGES["good-enough.html"] = dict(
    title="04 · When Good Is Good Enough — The AI Workflow Evals Handbook",
    description="Ship bars and vetoes: 16/20 default ship threshold, the pilot band, the red-line zero veto, the stop rule, and the three honest exceptions.",
    kicker="Chapter 04 · The decision",
    headline="When good is good enough.",
    subtitle="A pre-agreed bar, so the decision is made by calm you-in-advance — not by mood on the day.",
    here="good-enough.html",
    body="""<span class="stamp">Good enough is a stop rule, not just a ship rule</span>

<p class="lede">The score is 17/20. Ship it, or keep pushing? Decide wrong one way and you ship sloppy work; decide wrong the other way and you polish forever and never use the tool. So the decision is pre-agreed:</p>

<table>
  <tr><th>Reading</th><th>Verdict</th><th>Meaning</th></tr>
  <tr><td><strong>16–20 / 20</strong></td><td><strong>Good enough — ship</strong></td><td>Usable for real work, with the usual “verify before it matters” habits.</td></tr>
  <tr><td><strong>12–15 / 20</strong></td><td><strong>Pilot — supervised use</strong></td><td>Fine for drafts, notes, and experiments; anything leaving your desk gets a real check by you.</td></tr>
  <tr><td><strong>8–11 / 20</strong></td><td><strong>Don't rely on it</strong></td><td>Keep working the setup; real tasks stay under your own control.</td></tr>
  <tr><td><strong>0–7 / 20</strong></td><td><strong>Not usable</strong></td><td>Wrong tool, broken setup, or a quiz-and-setup mismatch worth investigating.</td></tr>
</table>

<h2>Why 16?</h2>
<p>16/20 means the run averages a mix of 2s and 1s — you can expect a useful answer most times, and when it's off, it's off in the <em>partial</em> way, not the <em>wrong</em> way. High enough to matter, low enough to be reachable. Perfectionism around 18–20 spends effort you could spend everywhere else.</p>

<h2>The veto that outranks the total</h2>
<blockquote>A red-line or boundary question at <strong>0</strong> is an emergency <em>regardless of the total</em>. A gorgeous 19/20 with a boundary zero still means <strong>do not ship</strong>.</blockquote>

<h2>Good enough is per-task, not per-model</h2>
<p>The same setup can be 18/20 on email drafting and 6/20 on bookkeeping questions — honest verdicts differ per column. Keep a scorecard per job if one setup wears several hats. And when a task <strong>hits the bar two runs in a row, stop working the setup for that task.</strong> Go do the actual work. Ninety percent of further fiddling is anxiety wearing a lab coat.</p>

<h2>The three honest exceptions</h2>
<ol>
  <li><strong>Bar met, trend worrying.</strong> Scores 16–17 for weeks while notes keep mentioning “rambles more now.” Still ship — but write a <em>nagging</em> margin note. That's how you catch slow drift the thresholds are too coarse to see.</li>
  <li><strong>An update you can't refuse.</strong> Score lands just under the bar. Pre-commit the soft landing: pilot band for one week, dated retest note; still under at retest → restore a workaround instead of living under the bar indefinitely.</li>
  <li><strong>Barely any 2s.</strong> Don't lower the bar out of frustration. Mark the task <em>pilot</em>, then fix the <strong>task input</strong> — clearer instructions, better example files, a tighter acceptance bar. The quiz tells you whether the fix worked.</li>
</ol>

<h2>The index card</h2>
<div class="tally">1. Total at or above my ship bar?           → yes ⇒ keep going (run the red-line check)
2. Red-line or boundary question scored 0?  → yes ⇒ STOP. Do not ship.
3. Total in the pilot band (12–15)?         → yes ⇒ usable with supervision only.
4. Notes trending worse across 2–3 runs?    → yes ⇒ write a "nagging" note; watch next run.
5. At/above ship bar two runs in a row?     → yes ⇒ STOP polishing. Go use it for real.</div>

<h2>Your assignment</h2>
<div class="tally">1. Pick your ship bar (default 16/20) into your scorecard header.
2. Name your red-line and boundary questions in that same header.
3. Decide in writing what a pilot-band run may and may not do for you
   (e.g. "drafts are okay; nothing goes out without me reading it").
Next: <a style="color:#ffb473" href="habit.html">chapter 05 · keep the habit</a>.</div>""",
)

PAGES["habit.html"] = dict(
    title="05 · Keep the Habit — The AI Workflow Evals Handbook",
    description="The weekly ritual, a light maintenance calendar, sticking tactics, and the honest limits of the system — when to graduate to automation.",
    kicker="Chapter 05 · The stubborn part",
    headline="Keep the habit.",
    subtitle="Everything before this chapter is clever. This chapter is stubborn.",
    here="habit.html",
    body="""<span class="stamp">The canary only protects you if somebody looks at it, weekly</span>

<p class="lede">The ritual runs about fifteen to twenty minutes:</p>

<div class="tally">1. Rerun the quiz — all ten, in order, no skipping, no "restart to be fair".
2. Grade in one sitting, fresh eyes, before reading anything about old runs.
3. Log it: date and setup version in the header, scorecard kept forever.
4. Glance back two runs: the total, plus any question hit twice. Done.</div>

<p>Compare only when something changed (chapter 03); decide only when the comparison is done (chapter 04). Weekly is about habit — changing weeks are when the habit pays for itself.</p>

<h2>A light maintenance calendar</h2>
<table>
  <tr><th>Interval</th><th>Task</th><th>Time</th></tr>
  <tr><td>Weekly</td><td>Rerun + grade + log</td><td>15–20 min</td></tr>
  <tr><td>Monthly</td><td>Skim the notes since last month; look for repeated complaints</td><td>10 min</td></tr>
  <tr><td>Quarterly, or after big changes</td><td>Retire stale questions, add harder ones, re-pin acceptance bars</td><td>30 min</td></tr>
  <tr><td>Almost never</td><td>Rewrite the whole quiz from scratch</td><td>Only if your actual usage changed wholesale</td></tr>
</table>

<h2>Making it stick</h2>
<ul>
  <li><strong>Anchor it to something that already happens.</strong> Sunday coffee, Monday setup check, month-end — attach new habits to old ones.</li>
  <li><strong>Keep the question file where you can't forget it.</strong> Pinned note, starred file, the folder you open to start your week. The friction is remembering to begin, not the grading.</li>
  <li><strong>Use the pre-committed thresholds.</strong> When the scorecard is filled, the verdict is a lookup, not a debate — that's why chapter 04's index card exists.</li>
  <li><strong>Accept "noisy runs."</strong> Graded tired, interrupted, whatever — log it anyway with a note. A noisy logged run beats a skipped one, always.</li>
  <li><strong>Two misses and a rescue plan.</strong> Missed two weeks? No guilt spiral: run the quiz once, note “back after a break — treat last logged run as OLD, this as NEW,” and see what drifted during the silence. The system is built to forgive gaps; the only unforgivable act is letting a missed week end the habit.</li>
</ul>

<h2>Honest limits — and when to go deeper</h2>
<ul>
  <li><strong>Ten questions is a sample, not a survey.</strong> You're detecting gross regressions, not subtle ones. When a failure mode keeps squeaking into your notes, add a question about it — the system grows with you.</li>
  <li><strong>Human grading scales badly.</strong> Past two or three scorecards a week it tires and wobbles. That's the point to graduate to automation: my separate project <code>prompt-regression-cli</code> runs exactly this rerun-and-compare loop for you, using these same scorecards offline.</li>
  <li><strong>This book teaches judgment, not statistics.</strong> When you genuinely need “how much worse” in a rigorous sense — model choices, stakeholder documentation — you'll want proper eval tooling and bigger question sets. You'll be well-prepared, because you already know what the numbers are <em>for</em>.</li>
</ul>

<h2>The end (which is really the start)</h2>
<p>Ten fixed questions, a three-level rubric, a comparison ritual, a pre-agreed bar. Four small habits, thirty minutes a week, that turn “I think it's fine?” into “15 last week, 16 this week, nothing red-lined — go.”</p>
<blockquote>The coal miner's canary never made the mines safer by being a sophisticated instrument. It made them safer by being there, by being sensitive, and by being looked at. Yours is the same. Good luck — and score honestly. · Dylan</blockquote>""",
)

PAGES["templates.html"] = dict(
    title="Templates — The AI Workflow Evals Handbook",
    description="Copy-paste templates: the ten-question canary quiz, the 0/1/2 rubric, the gradeable scorecard, and a worked example with two filled scorecards.",
    kicker="Appendix · Copy, fill, repeat",
    headline="Templates.",
    subtitle="Everything here is yours to copy. Fill once, then keep it stable — that's what makes week-over-week scores mean something.",
    here="templates.html",
    body="""<span class="stamp">All templates also ship as Markdown files under docs/templates/ in the repository</span>

<div class="card">
  <h3>1 · The canary quiz <span class="mono">(docs/templates/canary-quiz-template.md)</span></h3>
  <p>Setup name + creation date, ten numbered questions (6 workhorse, 1 red line, 1 weak spot, 1 messy phrasing, 1 new frontier), one-sentence acceptance bars under every task question, and a stability note: change questions on purpose, never casually.</p>
  <div class="tally">Setup under test: &lt;name&gt; · Quiz created: &lt;date&gt;
Q1–Q6  workhorses (your top 3 usage categories, ~2 each)
Q7     RED LINE — the task where a mistake would cost you
Q8     WEAK SPOT — the thing it usually fumbles
Q9     MESSY — phrased the way you actually type (typos allowed)
Q10    NEW FRONTIER — what you want to trust it for but don't yet</div>
</div>

<div class="card">
  <h3>2 · The rubric <span class="mono">(docs/templates/rubric-template.md)</span></h3>
  <p>The 0/1/2 scale, your acceptance bars, the mechanical grading order, boundary-question rules, and your named thresholds (ship bar, pilot band, red-line questions).</p>
  <div class="tally">0 = wrong / confidently wrong     1 = right idea, real flaws     2 = trivial fixes only
Wrong anywhere that matters → 0.  Trivial fixes only → 2.  Between → 1.  Torn → 1.
Boundary: "I don't know" = 2 · hedges-then-guesses = 1 · invents = 0.</div>
</div>

<div class="card">
  <h3>3 · The scorecard <span class="mono">(docs/templates/scorecard-template.md)</span></h3>
  <p>One copy per run, kept forever. Header carries setup name, date, version, ship bar, and red-line questions; the body is ten lines a machine can read too:</p>
  <div class="tally">- Q1 · Score: 2 · Notes: reply-ready as-is.
- Q7 (red line) · Score: 2 · Notes: all clauses matched.
...
- Q10 · Score: 1 · Notes: honest refusal, not yet usable.
Verdict: NEW vs OLD: 15/20 → 16/20 · Q4 dropped 2→1 · red-line OK · green-line it.</div>
</div>

<div class="card">
  <h3>4 · The worked example <span class="mono">(example-canary-quiz.md, example-scorecard-1.md, example-scorecard-2.md)</span></h3>
  <p>A realistic filled set from a small-business owner: ten questions mirroring her actual usage, two graded runs (baseline 15/20 pilot, post-update 16/20 ship), and the one-line verdicts in the margins. Copy the <em>shape</em>, not the content.</p>
</div>

<div class="card">
  <h3>5 · The offline grader <span class="mono">(scripts/grade.py)</span></h3>
  <p>Optional helper — plain Python, no dependencies, runs fully offline:</p>
  <div class="tally">python3 scripts/grade.py scorecard.md          # total, verdict, red-line check
python3 scripts/grade.py old.md new.md         # totals, cliffs (2→0), drops, improvements</div>
  <p>It reads the scorecard format above — notes included — and applies the ship bar and red-line veto of chapter 04 for you. It grades the arithmetic; <em>you</em> still grade the answers.</p>
</div>

<p><em>You keep the habit; the templates keep the consistency. That's the division of labor.</em></p>""",
)

# index.html is the fully handcrafted landing page (already written); keep as-is.

def main():
    SITE.mkdir(exist_ok=True)
    for name, spec in PAGES.items():
        path = SITE / name
        path.write_text(page(**spec), encoding="utf-8")
        print("wrote", path)

if __name__ == "__main__":
    main()
