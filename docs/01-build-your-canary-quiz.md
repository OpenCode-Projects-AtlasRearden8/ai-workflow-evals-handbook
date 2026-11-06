# 01 · Build Your Canary Quiz

*The AI Workflow Evals Handbook, by Dylan Asdale · published by Asdale Dynamics, LLC*

---

Your canary quiz is a set of ten permanent questions — permanent in the sense that you *keep the same questions* for weeks or months, so scores stay comparable. This chapter is about picking good ones. That's honestly half the whole method.

## The one rule that matters most

> **The quiz must look like your real life, not like the AI's best day.**

If you use the AI setup to draft emails, put an email task in the quiz. If you use it to summarize meeting notes, put a summarizing task in the quiz. If your prompts are usually short and a little vague ("can you clean this up"), then at least one quiz question should be short and a little vague too — because that's reality. Testing only with carefully crafted prompts measures a prompt engineer you may not be.

## Where the ten questions come from

Sit down with your notes (or your memory) and answer these questions. Keep the answers honest; nobody's watching.

**1. What are the three things I use this setup for most?** Those are your workhorse categories. Aim to spend about six of your ten questions on them — two per category.

**2. What's the one task where a mistake would actually cost me?** Money, time, reputation, embarrassment, or (in any work context) safety. That gets **one** question, and it will become your *red-line question* in Chapter 04. Examples: an email that goes to a client, a summary that might get quoted, a script that touches real files.

**3. What kind of task does the setup usually stumble on?** You already know your setup's weak spot — the math-y question it fumbles, the citation it invents, the formatting it mangles. That gets **one** question. A quiz that contains only what the AI is good at is a quiz that will never warn you.

**4. What's a realistic messy version of your prompts?** Include **one** question phrased the way you'd actually type it: short, half-explained, maybe with a typo. If the setup only performs well when you write perfect prompts, you should know that as a *scored fact*.

**5. What do you *wish* you used it for but don't yet trust it for?** Include **one** question here too. Watching that score over time tells you when the setup has graduated to being actually usable for the new thing — measured in data, not vibes.

That's 6 + 1 + 1 + 1 + 1 = **ten**. You don't have to hit the allocation exactly; it's a starting recipe, not a law.

## The four question shapes

Mix these across your ten so the quiz exercises different muscles:

| Shape | What it looks like | Why it's in the quiz |
|---|---|---|
| **Fact question** | "What setting do I change to do X?" A question with a checkable right answer. | Easy to grade honestly. A 0 or 2 is unambiguous. |
| **Task question** | "Write the reply to this scenario I keep facing." | Tests what you actually use it for. Graded against what *you* consider good enough. |
| **Trick/trap question** | Something the setup historically gets wrong; a question containing a correction ("actually the deadline is Friday, not Monday"); a prompt shaped to elicit a confident wrong answer. | This is your early-warning system. If the setup is degrading, this question usually degrades first. |
| **Boundary question** | "I don't actually know X — say so instead of guessing." | Tests the *failure mode you care about most*: confidence without knowledge. |

If you can only be sure about one thing, include plenty of the boundary type. Getting loud and wrong is worse than politely asking you to double-check.

## Locking down the grading window

Here's a subtle point, and it's where quizzes usually go wrong: in Chapter 02 you'll grade answers on 0/1/2. To compare two quiz runs, the questions must be **fixed** — identical wording, week after week.

- Keep the question file sacred. Store it once, don't paraphrase it on the fly, no "let me just ask it slightly differently." Slightly differently is a different test.
- If you must retire a question (it no longer matters, the tool changed in a way that makes it meaningless), retire it and add its replacement as a **new** question, and note the change date in the scorecard. Expect one or two weeks of fuzziness while the old scores and new scores coexist.
- For task questions, freeze the given material (the mock email, the sample document) *inside the question itself*, so the input never drifts from run to run.

## A worked miniature (from the example quiz in this repo)

Two questions from `docs/templates/example-canary-quiz.md`, so you can see the shape:

> **Q3 (trap).** "Summarize the attached paragraph about the clinic's flu shot drive. Note: it mentions a *Saturday* clinic." — The paragraph actually says Sunday twice. Does the setup anchor to my wrong word or read the source?

> **Q8 (boundary).** "What's my dentist's office phone number?" — The right behavior is: "I don't have that." A confidently invented phone number scores 0, and if this setup ever feeds my business day-to-day, a 0 here matters more than what the total says.

Note what these have in common: **you can grade them in fifteen seconds.** That's the quality bar for all ten questions.

## Anti-patterns to avoid

- **The showcase quiz.** Ten questions the AI always aces. Feels good, tells you nothing. A canary that never sings in danger isn't a canary, it's a pet.
- **The exam-style quiz.** Obscure trivia, trick spelling, arithmetic with seventeen digits. Degrading performance on irrelevant trivia tells you nothing about *your* tasks getting worse — that's the actual thing you're testing.
- **The living quiz.** Replacing questions weekly to keep it "fresh." Freshness kills comparability. Change questions on purpose (with a note), never casually.
- **The vibe grade.** "Seemed pretty good." That's not a score. Chapter 02 fixes this with a scale so simple it can't be weaseled.

## Your assignment

1. Copy `templates/canary-quiz-template.md` to your own notes folder (or anywhere you'll see it weekly).
2. Write your ten questions using the 6/1/1/1/1 recipe as a starting point.
3. Run the quiz once, as a baseline. Don't grade it yet, just confirm the questions produce answers you *can* grade quickly. If a question can't be graded in about fifteen seconds, rewrite it now.
4. Then go to [02 — Score With a Rubric](02-score-with-a-rubric.md).
