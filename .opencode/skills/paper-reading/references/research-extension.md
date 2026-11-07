# Mandatory research extension · questions 9–13

Apply this protocol to every default DEEP READ after explaining the paper and its takeaways. These five questions are mandatory under the [user prompt](user-prompt.md), not dependent on a REVIEW or RESEARCH lens. Keep them in the same HTML and navigable body, using short headings and flowing explanations. An explicit user request to narrow scope takes precedence. A research card may supplement this section but cannot replace it.

## 9. Identify the most fragile assumption

Select an assumption that materially supports the method, proof, measurement, or interpretation. Examples of assumption types include input information availability, train/test stability, evaluator validity, identifiability, or affordable resource access; do not substitute this generic list for a paper-specific diagnosis.

Explain **assumption → why the mechanism or conclusion needs it → evidence of fragility → consequence if it fails → a diagnostic**. Anchor the relevant method or claim to the source. Distinguish an explicit author limitation from your evidence-based inference. If available evidence cannot establish which assumption is most fragile, name the best-supported candidate and the ranking uncertainty. Lack of an experiment is an evidence gap, not proof that the method fails.

## 10. Design a realistic one-week minimal reproduction

Choose one central, narrow claim that can be checked without rebuilding the entire system. State the scientific target first: what result would this experiment teach us? Then specify:

- **Scope and access:** public code/checkpoint version, data subset and split, license/access constraints, and any paper details that are missing. Verify availability when possible; an announced repository is not necessarily runnable code.
- **Budget:** assumed hardware, approximate runtime and human effort, storage/API cost when relevant. Label unmeasured estimates. Do not assume the user owns a GPU; offer a reduced-cost route or explicitly state the minimum requirement.
- **Design:** baseline and treatment, matched resources and other controls, metric, repetitions/seeds or a justified limitation, and the expected noise or uncertainty.
- **Decision:** a pre-specified numerical or directional success criterion, a negative-result criterion, and what neither outcome would establish. Do not invent an effect-size threshold without a rationale.
- **Seven-day plan:** concrete setup/sanity-check, baseline, intervention, repeat/error-analysis, and reporting milestones. Give a fallback if code, data, model access, or budget blocks the main plan.

Distinguish exact replication, scaled-down reproduction, and a mechanism sanity check. A small proxy may test a mechanism without reproducing the headline score. For a theory paper, use an assumption check, small computational instance, or independently reconstructed proof step; do not manufacture a training experiment. This section authorizes a plan, not running paid jobs, training, or downloading large datasets without a user request.

## 11. Construct a fair counterexample

Start from a precise claim and its quantifiers or applicability conditions. Build a concrete input, family of tasks, data-generating process, or boundary case that challenges it. Explain why the targeted mechanism should struggle, how a suitable comparator would behave, and what measurement distinguishes a real failure from noise or implementation error.

State **claim → counterexample construction → predicted failure → discriminating test → possible conclusions**. Include the result that would defeat your objection. A universal claim may be contradicted by a valid counterexample; an average empirical improvement is not refuted merely because one sample fails. Label out-of-distribution stress tests and assumption violations as scope probes, not automatic refutations of an in-scope result. Keep the design proposed unless it has actually been executed; do not fabricate outputs, scores, or negative results. Keep this distinct from the reproduction section: one checks a supported finding, the other challenges its boundary or explanation.

## 12. Search and verify subsequent research

**Actually invoke available search tools.** Search the exact title and identifiers, the method name with relevant terms such as extension, replication, limitation, critique, negative result, and the specific assumption/mechanism being examined. Follow citation links or author project pages where accessible. Search beyond exact-title citations when checking whether a proposed idea already exists. Search is scoped evidence gathering, not an exhaustive survey or a guarantee of completeness.

Record in the Markdown audit the **search date/cutoff, queries, tools/sources, URLs/identifiers, accessed version, and inaccessible material**. In the visible HTML, state the cutoff and provide retrievable source links. Open the primary text for consequential claims; metadata and snippets are discovery aids. If only an abstract is accessible, label that limit and avoid asserting detailed mechanisms or a verified refutation. If search tools are unavailable, explicitly mark this section incomplete; do not silently replace it with memory.

For each consequential work, explain:

1. Identity and chronology: title, authors/year, first release versus revision, and whether it is subsequent or concurrent work.
2. Relationship: extension, independent replication, critique, negative result, different formulation, or merely related work. Verify that relationship instead of inferring it from a citation.
3. Actual contribution or evidence and the specific earlier claim it changes, supports, or leaves unresolved.
4. Conditions and uncertainty: matched versus unmatched protocols, preprint versus reviewed status when relevant, source access, and strength of the claimed rebuttal.

Synthesize what understanding changed rather than listing papers. Seek both supportive and contradictory evidence without inventing either for symmetry. When none is verified, report “在本次检索范围内未找到可核实的直接后续研究” with the scope; this does not prove absence. Never feed later findings into the pre-publication idea reconstruction.

## 13. Propose one substantive, provisionally novel follow-up

Use the paper's limitation, the fragile assumption, a concrete unmet need, and the searched literature to motivate a research question. The target is a new useful capability, problem formulation, explanatory principle, or testable mechanism. Merely adding a loss term, replacing a backbone, scaling data, or combining named modules is insufficient without a distinct question and consequence.

Explain this chain in connected prose, with a compact experiment plan if helpful:

**limitation + unmet need → new question → hypothesis/mechanism → closest work and substantive difference → falsifiable prediction → smallest discriminating experiment → failure/stop criterion → value if supported**.

Separate what the paper establishes, what later literature establishes, your inference, and your untested proposal. Compare against the strongest close alternative and a simple null explanation. State resource and evaluation risks, what could falsify the mechanism, and whether the one-week test can screen the idea or a larger study is needed.

Perform a targeted novelty search for the proposed question/mechanism, including synonymous formulations, and revise or withdraw the novelty claim if close prior work is found. Cite the closest work and state the searched scope. Use language such as “在已核实的检索范围内，这个方向的候选新意是……；尚不能保证首创”. Do not promise novelty, publication acceptance, a successful outcome, or an experimentally validated contribution. A well-motivated proposal with unresolved novelty is more useful than a false claim of originality.

## Audit before delivery

Check that all five questions are answered in visible content, not only comments or a separate card. Verify source anchors and the four information classes, the reproducibility budget, fairness of the counterexample, actual search provenance, and the follow-up's contrast with closest work. Record missing access, unavailable search, unknown feasibility, and unresolved novelty honestly. No execution or verification may be claimed merely because a plan or a heading exists.
