# Local extensions: publication-time background and 13-part reading prompt

- Upstream: <https://github.com/xiaofengShi/paper-reading-skill>
- Original copied commit: `eadd0cd61d276d082938d80eb0d3fbb85614f2e1`
- Local revision: `method-salience-v1` (preserves `research-prompt-v1`, `narrative-logic-v1`, and `historical-context-v1`)
- Requested by the user on 2026-10-17 to make the historical research background a mandatory part of paper readings and backfill the existing project outputs.

## Publication-time background extension · 2026-10-17

- `SKILL.md`: required publication-time context before the method; explicit first-release / revision / concurrent-work distinctions.
- `references/historical-context.md`: source discipline, predecessor contribution–gap mapping, Markdown layout, and manual checks.
- `evals/reading-quality.md`: additional context gate and historical-placement depth dimension.
- `references/renderer-format.md`: body-marker and companion-check workflow documentation.
- `scripts/check-background.cjs` and tests: structural omission checks, deliberately separate from historical fact verification.

## Narrative-logic extension · 2026-10-18

Requested by the user after observing strong visualization but weak prose logic, based on their eight-part explanatory prompt. This is an instruction and evaluation update, not a claim that existing paper outputs have been rewritten or independently validated.

- `SKILL.md`: prose-first workflow and mandatory explanatory spine: problem/value → prior solutions/gap → evidence-grounded idea reconstruction → actual intuition → worked input/processing/output pipeline → accessible mathematics → question/test/answer experiments → grounded takeaways. Explicit matching-full-text retrieval and source/version discipline.
- `references/narrative-logic.md`: full drafting protocol, pre-paper-premise counterfactual check, qualified inspiration attribution, running-example provenance, beginner-accessible mathematical steps, selective experimental numbers, and prose-only semantic self-check.
- `references/historical-context.md`: integrates problem/value into the first navigable chapter and ends on the unmet need, avoiding reliance on the eventual method as a premise. Existing context markers and checker-recognized headings remain compatible.
- `references/reading-modes.md`: aligns the deep-read explanation pass with the new narrative spine.
- `evals/reading-quality.md` and `evals/reader-tasks.md`: blocking logic/accessibility/example gates and eight-question comprehension prompts; renderer success and heading presence are explicitly insufficient evidence.
- `README.md` and `README.zh-CN.md`: describe the local enhanced reading logic and distinguish it from upstream gallery examples.
- No renderer, CSS, math syntax, dependencies, Zotero data, or existing paper output is changed. No new automated semantic checker is claimed; use the manual narrative gate alongside the existing background checker and renderer tests.

## Thirteen-part prompt extension · 2026-10-26

Requested by the user to replace the default reading prompt with the supplied 13-part specification. This updates future reading instructions, not existing readings or their validation status.

- `references/user-prompt.md`: preserves the supplied Chinese prompt and writing requirements.
- `SKILL.md` and `references/narrative-logic.md`: all 13 questions are default DEEP READ obligations, including fragile assumptions, one-week reproduction, fair counterexamples, actual subsequent-literature search, and a substantive limitation-and-need-driven follow-up. Natural, precise prose and four distinct information classes are explicit requirements.
- `references/research-extension.md`: source/access checks, seven-day experimental feasibility, fair falsification, actual search provenance, chronology separation, and targeted novelty checking without a false originality guarantee.
- `references/reading-modes.md` and `references/research-card.md`: remove the old implication that these five research questions need an optional lens; card formatting and lens-specific expansion remain optional.
- `references/visual-reading.md`, `evals/reading-quality.md`, and `evals/reader-tasks.md`: require meaningful offline interaction alongside faithful core visuals, extend semantic checks to all 13 questions, and preserve static/no-script readability and scientific provenance.
- `README.md`, `README.zh-CN.md`, and the project's `AGENTS.md`: align the default-scope description with the new prompt.
- No renderer, dependencies, Zotero records, or existing paper outputs are changed. Search, novelty, and prose checks remain evidence-based manual work, not newly automated guarantees.

## Key method salience extension · 2026-10-26

Requested after the user found the 64 thinking rows in TabPFN-2.5 insufficiently visible despite existing mentions. Updates future reading instructions, not existing paper outputs or their certification.

- `references/user-prompt.md`: adds the user's method-emphasis requirement without replacing the original 13 questions. Important introduced, modified, and adopted methods need explicit localized headings, mechanism explanations, pipeline visibility, provenance, and evidence limits.
- `SKILL.md` and `references/narrative-logic.md`: require the method-salience protocol and make this a blocking method-coverage/visibility obligation within questions 4–7, without introducing a fourteenth question or circular historical premises.
- `references/method-salience.md`: source-grounded change inventory, selective prioritization of consequential non-headline details, introduced/adapted/inherited/unclear attribution, connected mechanism explanation, diagram consistency, and a 64-thinking-rows regression example. New to a system is not automatically new to the field.
- `references/visual-reading.md`, `evals/reading-quality.md`, and `evals/reader-tasks.md`: align visual labels and semantic checks; a keyword mention or attractive node cannot substitute for visible prose. No invented ablation, originality, mask, or implementation to satisfy the template.
- No renderer, CSS, dependencies, Zotero data, or existing paper output changed. The new gate is source-based/manual, not a new automated semantic checker.

The original HTML renderer and published gallery are retained. The skill is now a locally enhanced derivative, not a byte-identical upstream installation. Preserve these changes when updating upstream. The original MIT license and attribution remain in place.
