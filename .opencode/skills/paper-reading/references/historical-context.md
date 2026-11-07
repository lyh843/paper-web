# Publication-time research background

This is a project-local extension requested by the user. Every DEEP READ must help a reader enter the research environment in which the paper was proposed, not only understand its final algorithm.

## Establish the historical boundary first

1. Record the earliest verified public release, publication venue/year, and the local PDF's revision separately. Prefer the arXiv submission history, proceedings, publisher, or dated author release. Do not infer exact dates from a Zotero import timestamp, filename, or PDF creation date.
2. Default to the first-publication horizon. Explain later-revision context separately when the supplied version introduces new comparators, results, acknowledgements, or attribution. If early text is unavailable, do not claim that the complete local revision's method or experiments were already present in v1.
3. Treat independently emerging contemporary work as concurrent. A citation or similar idea does not by itself establish influence. Verify publication dates before saying one work responded to another.
4. A modern survey, repository README, or current leaderboard can aid discovery, but must not silently replace a contemporary source. Clearly label hindsight if it is useful; do not make it the historical rationale.

## What the reader must learn

- **Problem and value:** State the exact research question and success conditions, why the remaining problem matters, and what progress could enable. Separate potential value from demonstrated benefit.
- **Field state:** What task, workflow, assumptions, and evaluation conventions were common? What had become feasible, and what was still expensive, unreliable, or untested? Explain essential terms in the task's own language.
- **Predecessor contributions:** Usually select 3–6 relevant works or tightly related lines, not a comprehensive bibliography. For each give a concrete mechanism or result it introduced, what it did not settle, and why that matters to this paper. State the year/era and a verifiable source.
- **Unresolved bottleneck:** Explain why stacking the existing ideas did not automatically solve the authors' problem. Distinguish limits stated by the authors from the reader's reconstruction. Avoid universal negative claims such as “nobody had ever tried” without supporting evidence.
- **Bridge to the idea:** Close on the unresolved need and constraints that a plausible solution would have to meet. The following idea-reconstruction chapter must motivate a hypothesis using only pre-paper evidence; reserve the paper's actual design and its new evidence for the intuition, method, and experiment chapters. Do not use the eventual contribution or its success to retroactively justify the motivation. Follow [narrative-logic](narrative-logic.md).

For theory, trace earlier assumptions, guarantees, and the gap in what can be proved. For a benchmark, explain earlier measurement practices and what they could not establish. For a system/report, distinguish new algorithmic choices from integration, scale, engineering, and product availability.

## Source discipline

Start with Introduction / Background / Related Work and the bibliography. Verify pivotal predecessor claims and uncertain timing using primary abstracts, papers, proceedings, or official histories as needed. Keep source pointers per contribution, not just one citation after a whole era. A target paper's own summary is useful evidence of its positioning but is not an independent replication of the cited work. Say when only that summary or a primary abstract was checked. Do not invent precise historical rankings or priority claims.

The visible chapter must stand on its own. Names and years alone, a glossary alone, a generic “this field is important” paragraph, or a source-only timeline does not satisfy the requirement. A table helps compare contributions but needs prose explaining the causal connection between the remaining gap and this paper's direction.

## Audit-source layout

Put this after the short global orientation/map and make it the **first `##` body chapter**, before method details. It renders with the existing Markdown pipeline. Use these body markers so the companion checker can detect omissions; they are not new positional header markers.

```markdown
<!-- paper-reading-context:start -->
## 00 / 发表时的研究背景
<!-- context-cutoff: 2022-07-05; basis: first-publication -->

### 研究问题与价值

Define the precise task, success criterion, why the gap matters, and what solving
it could enable. Distinguish hoped-for benefits from demonstrated outcomes.

### 当时的领域状态

State the verified first release and source revision separately, then explain
what researchers could do at that point. Cite dates and factual claims.

### 关键前作与尚存缺口

| 工作与时间 | 已有贡献 | 当时未解问题及与本文的关系 | 来源 |
|---|---|---|---|
| Specific work A | Concrete contribution | Remaining bottleneck | PDF §2 or primary URL |
| Specific work B | Concrete contribution | Remaining bottleneck | PDF §2 or primary URL |
| Specific work C | Concrete contribution | Remaining bottleneck | PDF §2 or primary URL |

### 本文为何在此时提出

Explain why the gap remained and which requirements a new direction would have
to satisfy, without assuming this paper's contribution or successful results.
Label reader inferences. Keep later developments outside the historical boundary.
<!-- paper-reading-context:end -->
```

For English, use `### Time boundary and field state`, `### Prior work and remaining gaps`, and `### Why this paper now`. A niche paper genuinely requiring fewer than three predecessors can add `<!-- context-related-work-exception: a substantive explanation -->`; do not invent extra works merely to fill rows.

The added problem/value subsection may use `### Research problem and value` in English. The three existing checker-recognized subsections keep their exact names and relative order. The checker does not enforce the added narrative requirements; the manual quality gates do. Keep questions 1–2 of the 13-question spine together here so context remains the first `##` chapter.

## Checks before delivery

Run `node <skill-dir>/scripts/check-background.cjs <source>.md`. It detects missing markers, cutoff, chapter placement, subsections, or sourced predecessor rows. It **cannot** verify dates, scientific truth, completeness, originality, priority, or whether a limitation is fairly represented.

Then manually check: could a reader explain (1) an earlier method's specific advance, (2) why that still left this problem, and (3) why this paper's direction made sense at that time? The quality report must record a historical-context gate with concrete source locations and any unknowns. Do not confuse passing this check with an independent reader study.
