# Make consequential methods visible and understandable

This local extension responds to the user's difficulty noticing TabPFN-2.5's 64 learned thinking rows despite their name appearing in the reading. Apply it to every DEEP READ. It strengthens the existing intuition, method, mathematics, and evidence questions; it does not add a compulsory fourteenth chapter or replace the coherent narrative with a component catalog.

## 1. Inventory actual changes before drafting the method

Read the methods, architecture bullets, overview figure/captions, implementation appendices, and ablations, not only the abstract's headline contributions. Build a compact inventory in the Markdown audit, preferably in a comment or other non-reader-facing audit record:

| Mechanism/change | Compared with what | Provenance/status | Source anchor | Why consequential | Visible explanation + visual location | Evidence/limits |
|---|---|---|---|---|---|---|
| Paper-specific item | Actual predecessor or baseline | Proposed/modified, adapted, inherited, or unclear | Exact section/page/figure | Information/computation/objective/protocol change | Named subsection and pipeline view | Isolated test, system-only result, or unknown |

Select mechanisms whose omission would leave a reader with the wrong account of how the method works or what changed. Include consequential supporting choices even if they receive only one bullet in the paper: extra latent rows, target injection, masks, routing, grouping, losses, context selection, caching, calibration, or data construction can matter as much as a named headline module. These are examples to inspect, not required categories to fabricate for every paper. Do not turn ordinary parameter settings into a parade of equally important innovations.

For each inventoried item, record either where it is explained or why it is lower-priority, unchanged, or out of the requested scope. A material, unaccounted-for change is an omission. A conscious selection is not permission to hide a central mechanism because its implementation or ablation is unavailable: explain what is known and mark the rest unknown.

## 2. Separate salience from originality

Use locally clear provenance descriptions:

- **Proposed or substantially modified here:** identify the change relative to the named predecessor. If this is only the authors' novelty claim, attribute it; historical first-priority requires supporting literature, not an adjective.
- **Borrowed and adapted:** name the originating work when verified, then explain what was adapted and why. It still deserves prominence when essential to this paper.
- **Inherited unchanged:** explain enough for comprehension but do not market it as a new contribution.
- **Unclear attribution:** say what is known and what could not be verified rather than guessing an origin.

These provenance categories are separate from the four epistemic information classes. An author's explanation of a newly adopted mechanism remains a paper claim; a possible benefit you infer remains an inference. “Added to version 2.5” does not establish “invented by version 2.5.”

## 3. Reveal the differences after the intuition, then explain in place

After the non-circular idea reconstruction and concise actual intuition, give a short paper-specific orientation to the important changes: **previous operation → introduced/changed operation → bottleneck it targets**. A compact table can help but must not replace explanations. Do not move actual innovations into the publication-time background as prior knowledge. Keep the central intuition concise instead of loading it with every module.

Give each selected key mechanism a distinct, descriptive subsection in the method body, beside the pipeline operation it supports. Name it in the reader's language with its original term at first use, such as **“64个可学习虚拟行（thinking rows）”**. For another requested language, localize accordingly. Preserve meaningful counts, shapes, placements, and trained-versus-fixed status. Avoid an English-only name or a generic heading such as “other improvements.”

In connected prose, explain:

1. **Identity and change:** what the object/operation actually is, what it replaces or adds, and its provenance.
2. **Motivation:** which constraint or failure it targets; distinguish documented author rationale from your reconstruction.
3. **Mechanics:** what enters, what internal state or operation changes, what leaves, where it connects, and how the running example encounters it.
4. **Learning and use:** what is learned during pretraining, adapted on the current task, fixed at inference, or computed anew. Distinguish real observations, labels, latent states, and auxiliary computation.
5. **Cost and scope:** extra parameters, sequence length, memory, latency, information loss, assumptions, or other relevant trade-offs, with numerical estimates labeled as estimates.
6. **Evidence:** what the paper actually tests about this mechanism, what the test can isolate, and what remains unexplained. No separate ablation means no quantified independent contribution; it does not justify omitting the mechanism or claiming it is useless.

Explain missing implementation details at the boundary of the available source. Do not invent tensor shapes, initialization, insertion order, attention masks, labels, optimization rules, or access paths to complete a diagram.

## 4. Highlight the mechanism in a faithful pipeline view

The relevant diagram or interactive view must visibly identify each selected consequential mechanism and show its known placement/connections. Use labels, grouping, or annotations, not color alone. Distinguish added/modified/adapted parts from inherited context where useful. Explain consequential arrows in prose and preserve source anchors in the audit.

If the original overview figure omits a key detail, add a clearly labeled editorial annotation, companion mechanism view, or faithful redraw. Do not silently modify an image while presenting it as the author's original. When the source does not establish exact placement or wiring, show a qualified conceptual role instead of a false implementation graph. Interaction is supplementary; the key explanation remains visible without scripts and without opening a disclosure. There is no quota of diagrams or widgets per mechanism.

## 5. Coverage and visibility gate

Compare the inventory with the Markdown and final HTML, with source citations hidden as in normal reading. For every selected key mechanism, can a reader:

- locate it quickly from its descriptive method subsection, including its localized name and consequential count;
- explain what changed, why, and how it acts on the running example without reopening the PDF;
- see its role/connections in the relevant pipeline view without guessing;
- distinguish its origin, the authors' rationale, your inference, and the experimental evidence;
- state what is not disclosed or not independently tested?

Merely appearing in a hero card, one long paragraph, a figure caption, hidden citations, or a folded panel fails this gate. A heading and a colored node alone also fail: the explanation must carry the mechanism. Record concrete locations and `pass`, `fail`, or `unknown` in the audit. Repair a visibility/coverage failure before delivery. This is a source-based semantic check, not an automated proof of novelty or comprehension.

## Regression example: 64 thinking rows

When the target source is TabPFN-2.5 §3, the reader should be able to find **“64个可学习虚拟行（thinking rows）”** in the method body and explain that the authors add learned rows during pretraining, with stated roles of extra computational capacity and possible attention sinks. Distinguish latent computation from 64 additional independent labeled observations, and from natural-language chain-of-thought. Preserve the source's qualified rationale, note its LLM inspiration without claiming invention, and do not invent the missing independent ablation or exact mask/placement.

This is a regression example for salience and evidence discipline, not a universal module template or a claim that this prompt edit has already repaired the existing TabPFN-2.5 HTML.
