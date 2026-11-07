# Narrative logic for a complete paper reading

This local extension implements the user's [13-question explanatory prompt](user-prompt.md). Read it for every DEEP READ together with [research-extension](research-extension.md), which details questions 9–13. Preserve the visual atlas, source discipline, and publication-time background, but make the prose carry a coherent explanation independently of the layout. SCAN remains a separate, explicitly requested depth.

## Draft the explanatory spine before the visuals

After reading the full relevant source, write a short internal outline answering: **problem and value → existing solutions and gap → plausible route to an idea → actual intuition → worked method → mathematical understanding → experimental questions and answers → takeaways → fragile assumption → one-week reproduction → counterexample → searched subsequent research → substantive follow-up idea**. Check the arrows between these answers before expanding them. This outline is a drafting aid, not another reader-facing recap.

Each substantial section needs explanatory prose, not just cards, bullet labels, or a comparison table. Use paragraphs for causal connections and numbered steps for operations; do not impose paragraph or word quotas. At a transition, resolve the current question and name the next unresolved issue. Avoid repetitive stock phrases. Introduce a term before relying on it; explain an acronym at first meaningful use. Default to a reader who understands the broad task but needs mathematical prerequisites taught.

Use a natural, precise teaching voice: concrete intuition and careful reasoning, as requested by the user's Karpathy/Kaiming He reference, without impersonation. Every sentence should add information. Avoid generic praise, excessive dashes/quotation marks, and formulaic “不是……而是……” contrasts. Locally distinguish **paper claims**, **prior-literature findings**, **evidence-based inferences**, and **uncertain conjectures** through explicit attribution or labels; do not promote a reported observation, plausible explanation, or new proposal into a proven fact.

Use a brief global orientation/map above the first `##` chapter. Keep **problem, value, prior solutions, and gap together in the first navigable publication-time background chapter** under the existing context markers. Explain the plausible idea route next, then the actual intuition and method. This preserves [historical-context](historical-context.md) and `check-background.cjs` without duplicating background or making a separate importance chapter before it. Headings are editorial choices; logical dependencies are not.

## 1. Research problem and value

- Distinguish the broad application area from the narrow research question. Specify the task, available information, desired output or guarantee, constraints, and what would count as success.
- Give a concrete situation in which the gap matters. Explain the consequence of leaving it unsolved and the scientific or practical value of progress, not merely that the field is popular.
- Separate the authors' motivation, source-supported background, and your interpretation. Potential deployment value is not a demonstrated application result.

## 2. What prior work did and did not solve

Use the historical protocol to explain relevant contributions, not a title/year list. Say fairly what already works and under what assumptions. Locate the residual gap: quality, cost, generalization, information access, measurement validity, a missing guarantee, or another source-supported limitation.

Explain why the closest existing solution does not settle the exact question under the same constraints. If the issue is a trade-off or a different task setting rather than a complete failure, say so. If an obvious combination of prior ideas is discussed, explain its documented limitation or label your proposed limitation as an inference. Do not invent failed experiments or exhaustive literature coverage.

## 3. Plausible route to the idea, without using the answer as a premise

This is a **public, evidence-grounded pedagogical reconstruction**, not access to the authors' private reasoning. Use a visible qualifier such as “一种基于当时知识的思路重建，并非作者真实发现过程的记录” / “A plausible reconstruction from knowledge available then, not a record of the authors' discovery process.” Provide a concise rationale, not imagined inner monologue.

Build a small causal chain, with source anchors for the factual premises:

1. **Known starting point:** a relevant capability or result established before this paper.
2. **Obstacle:** a documented failure mode, cost, tension, or unmet requirement.
3. **Connecting observation:** a prior result or principle suggesting another route; explain why it is relevant.
4. **Design hypothesis:** a tentative change one could reasonably consider and what it would predict, without asserting that it must succeed.

Use only evidence available at the established historical boundary as factual premises. A pre-existing observation summarized in this paper may be used if its provenance is clear. The paper's own newly reported diagnosis, ablation, final modules, loss, theorem, or headline result cannot be smuggled in as prior knowledge. Discuss such new evidence later in its proper role. If evidence for a connecting observation is absent, state that limit and offer only a clearly labeled conceptual hypothesis; do not invent an empirical observation to fill the chain.

**Counterfactual check:** if this paper's method and results were hidden, would the premises still make sense and support this hypothesis as one possible direction? If not, rewrite. The hero may preview the answer, but this reconstruction must not depend on that preview. Do not assert that the idea was inevitable, uniquely determined, or historically inspired by a work unless a source establishes the attribution.

Bad pattern: “Since the paper's new module improves the score, the authors realized that they needed that module.” Better pattern: “Earlier work supplied capability X, but under constraint Y it lost information Z. A previously established principle suggests retaining or retrieving Z might help; this motivates a testable direction, not proof that the paper's eventual design works.” Replace placeholders with paper-specific, sourced facts.

## 4. Actual core intuition

Give the essence in roughly two to four clear sentences, without a rigid length rule: **old behavior → proposed change → expected mechanism → necessary condition or trade-off**. Then introduce the actual method names. Explain what the idea changes, not simply which modules it contains. If an analogy helps, map it back to the concrete operations and say where it stops being accurate. Intuition is an explanation of plausibility, not evidence of success.

Keep this distinct from the preceding reconstruction: that section motivates a possible direction without knowing the answer; this section reveals what the paper actually chose. Do not repeat the full motivation or hide implementation in jargon.

## 5. Full method through one running example

Apply [method-salience](method-salience.md): inventory consequential introduced, modified, and noteworthy adopted mechanisms from the actual methods/captions/appendices, not only the abstract. After the core intuition, briefly orient the reader to old→changed→intended effect; then use descriptive localized subsections for selected mechanisms at their actual pipeline locations. Preserve names and meaningful counts, explain provenance/motivation/operation/training-versus-inference/cost/evidence, and mark missing ablations. A mechanism merely named in the overview or buried in a broad architecture paragraph has not been explained. Show the same mechanisms in the relevant pipeline view without inventing undisclosed wiring.

Prefer a real example supplied by the paper, dataset, or an identifiable task source. Identify where it comes from. If unavailable or unsuitable, say so and use an explicitly constructed pedagogical example; do not label it a reported case. Never expose sensitive data to make an example appear real.

Trace the **same instance** through the relevant input → representation/transformation → decision or update → output sequence. For each consequential step explain:

- what enters, with enough concrete content or shape to recognize it;
- what operation occurs, which quantities change, and why the next step needs it;
- what leaves the step, and what assumption or cost the choice introduces.

Do not replace the example midway with unrelated toy cases. Branch when the real algorithm branches; show how state or feedback changes later operations. Separate training and inference, tracing the appropriate example for each when both are essential; evaluation is not another deployment stage.

Label intermediate values as paper-reported, actually computed by you, schematic, or unavailable. A real input does not make invented intermediate activations or a guessed output real. State omitted details rather than fabricate a run. If a source example is too large, use a labeled excerpt and explain the omitted scope. Use the [paper-type route](paper-types.md) for a proof instance, dataset record, benchmark sample, or survey case instead of manufacturing a model pipeline.

## 6. Mathematical understanding from the necessary foundations

First determine what the paper actually provides: a formal derivation/proof, a defined objective or score without a derivation, or no essential mathematics. Do not confuse these cases.

When mathematics is central, teach only the prerequisites needed for this paper, assuming limited mathematical fluency:

1. Explain the underlying concept in words and a small example when helpful, before the compact notation.
2. Define symbols, domains/shapes, assumptions, and what is fixed versus optimized before use.
3. Start at the problem, basic definition, or stated assumption; present each non-obvious algebraic or logical step with the operation/rule that justifies it and what it means intuitively.
4. Distinguish equality, approximation, bound, empirical heuristic, and design choice. State extra assumptions introduced by an explanatory derivation.
5. Connect the final expression or theorem to the pipeline: what is computed, optimized, constrained, or guaranteed, and what is not.

Preserve the original objective's masks, normalizers, expectation distribution, and conditions. Make equivalent rearrangements recognizable. Label an added teaching derivation as your explanatory reconstruction, not a proof supplied by the paper. If the source leaves an unfillable step, name it; do not silently invent justification.

If no theoretical derivation exists, say “本文未给出核心理论推导” or its language equivalent and skip a fabricated derivation. Still explain an essential loss, algorithmic formula, or evaluation score where used; a formula is not automatically a theorem. For a theory paper, follow assumptions → lemma dependencies → proof idea → central steps → guarantee and boundary cases. Do not reduce it to an empirical validation template.

Use `$…$` inline and `$$…$$` for display math, following [renderer-format](renderer-format.md). Keep formulas out of code fences and plain-text visual JSON fields. Check source accuracy as well as KaTeX rendering; a parser cannot establish algebraic correctness.

## 7. Experiments as questions, tests, and bounded answers

For each major claim use this reader-facing pattern:

**提出的问题 / Question → 如何验证 / Test → 答案与边界 / Answer and scope**

- **Question:** a concrete uncertainty or claim, not a dataset name or “is the method good?”
- **Test:** why this task/protocol and comparator/control can answer it; what changes, what is held fixed when relevant, how success is measured, and what observation would favor or weaken the proposed explanation.
- **Answer:** what was actually observed, the narrower conclusion it supports, and any decisive restriction or untested alternative.

Lead with the experimental idea. Use only enough numbers to make the decisive comparison clear; do not transcribe all tables or hyperparameters into the main path. Numerical statements still need the correct units, denominator, baseline, setting, and source in the audit. Quantitative charts still need their compact data tables. A contextual detail that changes the interpretation is essential, not optional clutter.

Group secondary results under the question they address, and cover all central claims. Identify when a claimed mechanism lacks an isolating experiment rather than supplying an imaginary ablation. A whole-system win does not isolate one component; a controlled ablation does not prove a universal mechanism. Retain [paper-type](paper-types.md) adaptations: use proof/assumption checks, dataset validity evidence, or survey coverage where appropriate.

The renderer's existing `paper-experiments` block already fits this logic: `question` = question, `setup` = test/comparator/metric, `observation` = actual result, `conclusion` = bounded answer. Although optional in the parser, include `conclusion` for central claims or state its content in adjacent prose. No renderer change or mandatory new visual block is needed.

## 8. Grounded takeaways

Close the paper-explanation portion with a few specific lessons, usually three to five, not a second abstract; the mandatory research extension follows. Together they should explain:

- which precise bottleneck the paper changes and through what mechanism;
- what reusable principle a reader can carry forward, distinguished from an untested generalization;
- which evidence makes that lesson credible and in what setting;
- when the method is useful and which assumptions, costs, or open questions remain.

Do not introduce unsupported future-work claims, generic praise, or new facts in the takeaways. Put small numerical/source conflicts beside the affected discussion, not in place of synthesis. Then apply [research-extension](research-extension.md) for questions 9–13, keeping untested ideas and retrospective evidence separate from what this paper established.

## Prose-only logic check before rendering and delivery

Temporarily ignore diagrams, card styling, and decorative titles while reading the Markdown. Verify that prose, equations, and ordinary tables still let a reader:

1. State the exact problem, why it matters, and what progress would enable.
2. Explain what the closest prior work achieves and why the same question remains open.
3. Follow the sourced starting points to a plausible hypothesis without assuming this paper's answer; distinguish reconstruction from historical attribution.
4. Explain the actual core idea in plain language before reciting module names.
5. Follow one identifiable example from input to output without invented intermediate facts.
6. Understand the central mathematical steps and prerequisites, or identify the justified absence of a derivation.
7. Match each central claim to a question, an appropriate test/proof, and a bounded answer without drowning in numbers.
8. State specific takeaways grounded in the preceding mechanism and evidence.
9. Identify the most fragile consequential assumption, why it matters, and the evidence or uncertainty behind that diagnosis.
10. Explain which narrow claim a realistic seven-day experiment would test, with access requirements, budget, control, metric, and decision criterion.
11. Describe a fair counterexample, the claim it challenges, and what result would defeat the objection.
12. Explain what verified subsequent research changes or leaves unresolved, or identify the explicitly reported search/access limitation.
13. Evaluate a limitation-and-need-driven follow-up hypothesis against close prior work, a discriminating experiment, and provisional novelty limits.

Also check chapter transitions for missing logical links, repeated motivation, undefined concepts, and circular explanations. Restore visuals and ensure they clarify this same argument rather than introduce a different one. Apply [reading-quality](../evals/reading-quality.md); record `pass`, `fail`, or `unknown` with concrete source/output locations in the Markdown audit, not as a default meta chapter in the HTML. Comments may hold this audit record. This is a manual semantic check, not an independent reader study; neither heading detection nor a successful build can pass it on its own.
