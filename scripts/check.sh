#!/usr/bin/env bash
# Self-tests for the AI Workflow Evals Handbook repo.
# Verifies required files, LICENSE/README credit lines, internal doc links,
# HTML integrity, and grade.py behavior (correct grading, comparison, error paths).
set -u
cd "$(dirname "$0")/.." || exit 1

pass=0
fail=0

ok()   { printf '  ok    %s\n' "$1"; pass=$((pass + 1)); }
bad()  { printf '  FAIL  %s\n' "$1"; fail=$((fail + 1)); }

echo "== required files =="
for f in LICENSE README.md STATUS.md \
         docs/00-start-here.md docs/01-build-your-canary-quiz.md docs/02-score-with-a-rubric.md \
         docs/03-catch-regressions.md docs/04-when-good-is-good-enough.md docs/05-keep-the-habit.md \
         docs/templates/canary-quiz-template.md docs/templates/rubric-template.md \
         docs/templates/scorecard-template.md \
         docs/templates/example-canary-quiz.md docs/templates/example-scorecard-1.md \
         docs/templates/example-scorecard-2.md \
         site/index.html scripts/grade.py; do
  if [ -f "$f" ]; then ok "exists: $f"; else bad "missing: $f"; fi
done

echo "== license and credit lines =="
if grep -qF "Copyright (c) 2026 Asdale Dynamics, LLC" LICENSE; then
  ok "LICENSE copyright line exact"
else
  bad "LICENSE copyright line missing/incorrect"
fi
if grep -q "Asdale Dynamics, LLC" README.md; then
  ok "README credits Asdale Dynamics, LLC"
else
  bad "README missing Asdale Dynamics, LLC credit"
fi

echo "== internal doc links resolve =="
link_failures=0
for md in docs/*.md docs/templates/*.md README.md; do
  while IFS= read -r link; do
    target="${link%%#*}"
    if [ -z "$target" ]; then continue; fi
    dir=$(dirname "$md")
    if [ ! -e "$dir/$target" ]; then
      bad "$md -> broken link: $link"
      link_failures=$((link_failures + 1))
    fi
  done < <(grep -oE '\]\(([^)#]+)(#[^)]*)?\)' "$md" | sed -E 's/^\]\(//; s/\)$//; s/#[^)]*$//')
done
if [ "$link_failures" -eq 0 ]; then ok "all markdown links resolve"; fi

echo "== site html integrity =="
for html in site/*.html; do
  if grep -q "<style" "$html" && grep -q "</html>" "$html" && grep -q "<title>" "$html"; then
    ok "inline CSS + closed html: $html"
  else
    bad "html integrity problem: $html"
  fi
done

echo "== grade.py behavior =="
out1=$(python3 scripts/grade.py docs/templates/example-scorecard-1.md) || bad "grade.py exit on card 1"
echo "$out1" | grep -q "TOTAL: 15/20" && echo "$out1" | grep -q "pilot band" \
  && ok "card 1 grades 15/20 pilot" || bad "card 1 grading wrong: $out1"

out2=$(python3 scripts/grade.py docs/templates/example-scorecard-2.md) || bad "grade.py exit on card 2"
echo "$out2" | grep -q "TOTAL: 16/20" && echo "$out2" | grep -q "good enough" \
  && ok "card 2 grades 16/20 ship" || bad "card 2 grading wrong: $out2"

if python3 scripts/grade.py docs/templates/example-scorecard-1.md docs/templates/example-scorecard-2.md >/dev/null 2>&1; then
  ok "two-card comparison runs"
else
  bad "two-card comparison failed"
fi

if python3 scripts/grade.py docs/templates/scorecard-template.md >/dev/null 2>&1; then
  bad "unfilled template should error, but exited 0"
else
  ok "unfilled template correctly errors"
fi

# red-line veto: build a temporary doctored card where the red-line question scores 0
tmp=$(mktemp)
sed 's/^- Q7 (red line) · Score: 2/- Q7 (red line) · Score: 0/; s/^- Q8 · Score: 2/- Q8 · Score: 0/; s/^- Q9 · Score: 2/- Q9 · Score: 0/' \
  docs/templates/example-scorecard-2.md > "$tmp"
out3=$(python3 scripts/grade.py "$tmp")
echo "$out3" | grep -q "DO NOT SHIP" \
  && ok "red-line zero triggers veto" || bad "red-line veto missing: $out3"
rm -f "$tmp"

echo
tot=$((pass + fail))
printf '%d/%d checks passed\n' "$pass" "$tot"
[ "$fail" -eq 0 ]
