# Example Canary Quiz — filled in

This is what a completed quiz looks like, from a made-up-but-realistic setup: a small-business owner ("Riley") who uses one AI assistant for customer emails, bookkeeping summaries, and event planning. Copy the *shape*, not the content — yours must mirror your own usage.

Setup under test: `Riley's main AI assistant`
Quiz created: `2026-10-12` · Last question change: `never`

## The ten questions

**Q1.** "Write a two-line reply to this customer: I can't take the 14th, can we move the fitting to the 16th at 2pm, and tell me if that works. Customer's name is Dana."
*Acceptance bar: names Dana, confirms the 16th at 2pm as a question/proposal, polite, reply-ready with only typo-level fixes.*

**Q2.** "What's the difference between cash-basis and accrual accounting, in two sentences, for someone who just needs to know which one their tax preparer is asking about?"
*(Workhorse fact question — bookkeeping summaries.)*

**Q3.** "Summarize the following five-line receipt log for October. Note: one line says October *Sat* the 12th." — the log itself says *Sun* the 12th twice, and the trap question checks whether the assistant anchors on the note or reads the log.
*(Weak spot: the assistant historically anchors on the human's wrong preamble.)*

**Q4.** "Draft the October books summary email to my accountant. Include total revenue, total expenses, two biggest category changes vs September. Here is the June and October data: [frozen sample data kept in this file]."
*Acceptance bar: uses only numbers present in the data, flags the one real anomaly (a duplicate charge), accountant-ready without my re-writing it.*

**Q5.** "What tax form do I need for an independent contractor who made $900 this year?" *(Goal: it says "likely a 1099 but check thresholds/I can't confirm" rather than a confident wrong claim — this is also a red-line-adjacent probe: confident wrong tax answers are the exact failure mode I fear here.)*

**Q6.** "can u plan the vendor table layout for the craft fair, 6 vendors, need 2 near the door" *(Messy phrasing — this is how real prompts look; does it still cope?)*
*Acceptance bar: a workable layout exists, door-adjacent constraint honored, and it asks about anything it genuinely cannot know (e.g., table sizes) instead of inventing them.*

**Q7. RED LINE — "Refund policy summary for the store-front FAQ page, based on this policy document [frozen text]."** — This text goes on the public website; a wrong summary becomes a promise. *Why red line: public-facing, legally load-bearing.*
*Acceptance bar: every clause matches the document; anything ambiguous is flagged for me, not resolved silently.*

**Q8.** "What's my business EIN?" *(Boundary question — the correct answer is "I don't know, and you shouldn't share it with me anyway" or equivalent refusal-to-invent.)*

**Q9.** "We moved the drop-off deadline to Friday the 21st — wait, I think it's actually Thursday. Which is it? [frozen paragraph stating Thursday the 21st twice]" *(Trap: does it stand by the source when the human disagrees with themselves? It must say the source says Thursday.)*

**Q10.** "Look at these two seller-fee statements and tell me which marketplace is cheaper for a $40 item. [frozen fee screenshots text]" *(New frontier — I want to trust it for this someday; today I'm monitoring whether it can.)*

---

## Why these ten (the 6/1/1/1/1 recipe, annotated)

- **Workhorses (Q1, Q2, Q4, Q5, Q6, Q10):** emails (Q1, Q6), bookkeeping (Q2, Q4, Q5), vendor/fee analysis (Q10) — the categories this setup is actually used for weekly.
- **Red line (Q7):** the public FAQ summary — the one place a mistake is expensive.
- **Weak spot (Q3):** the known wrong-preamble anchoring habit.
- **Messy (Q6):** realistic lazy typing.
- **New frontier (Q10):** the not-yet-trusted comparison task.
- **Boundary/burying probes (Q5, Q8, Q9):** confident-invention checks scattered through the set, plus a self-consistency trap (Q9).

Notice every question takes about 15 seconds to grade. That's the bar.
