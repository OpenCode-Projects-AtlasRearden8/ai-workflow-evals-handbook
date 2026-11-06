# Canary Scorecard — TEMPLATE (copy per run; grade.py can grade this format)

Setup: `<name>` · Run date: `<YYYY-MM-DD>` · Setup version: `<model/tool version or prompt set>`
Quiz file: `<path or name>` · Ship bar: `<e.g., 16/20>` · Red-line questions: `<e.g., Q7 + boundary questions>`

## Scores

Format rule (so `scripts/grade.py` can read it): one bullet per question, containing
`Score: 0|1|2`. Keep the notes to one or two sentences.

- Q1 · Score: `<0|1|2>` · Notes: `<≤2 sentences, only if a point was lost>`
- Q2 · Score: `<0|1|2>` · Notes: `…`
- Q3 · Score: `<0|1|2>` · Notes: `…`
- Q4 · Score: `<0|1|2>` · Notes: `…`
- Q5 · Score: `<0|1|2>` · Notes: `…`
- Q6 · Score: `<0|1|2>` · Notes: `…`
- Q7 (red line) · Score: `<0|1|2>` · Notes: `…`
- Q8 · Score: `<0|1|2>` · Notes: `…`
- Q9 · Score: `<0|1|2>` · Notes: `…`
- Q10 · Score: `<0|1|2>` · Notes: `…`

## Verdict (fill after any comparison — one handwritten line style)

`<NEW vs OLD: a/20 → b/20 · Qx dropped 2→1 (reason) · red-line OK · verdict: ship / pilot / stop>`

## Optional: raw answers

Paste (or link) the raw answers under each question, or keep them in a sibling file
`<date>-answers.md`. Keep them — the notes point back to them.
