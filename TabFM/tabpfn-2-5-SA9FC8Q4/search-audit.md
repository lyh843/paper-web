# TabPFN-2.5 · 来源与检索审计

日期/截止：2026-10-26。模式：中文 DEEP READ，`paper-reading/research-prompt-v1`。这是生成者来源审计，非系统综述、科学复现实验或首创证明。

## 原文

- 主条目SA9FC8Q4，附件9IIFU5YD，本地35页PDF；SHA256 `21f3cb0e28e587aef164a79a8ada9e942da51b052f55e6f366d5744a8b97f90f`，本轮与旧provenance一致。
- https://arxiv.org/abs/2511.08667 ：arXiv v1为2025-11-11，v2为2026-02-05；PDF内部报告日期2025-11-06。历史章节明确以已核实的首次arXiv公开为边界，不把内部封面日期冒充已核实公开事件。
- 本轮重读正文pp.1–11、相关Appendix C/D/F/G/H说明及图注，检查Fig3/4、蒸馏、速度、许可与缓存口径。应用案例目录与每个引用没有逐篇重读，未独立重建私有先验或专有蒸馏。
- 旧版全部输出及assets在 `revisions/pre-research-prompt-20261026/`；未修改原PDF或Zotero。无可用Zotero MCP，本轮使用已知主条目和本地PDF指纹，不声称重新查询了整个分类。

## 实际调用的搜索

工具：functions.websearch；来源打开用functions.webfetch。

1. `"TabPFN-2.5" 2026 extension critique distillation evaluation`
2. `"TabPFN" "distillation" "context" "updates" student`
3. `"context" "editable" "distillation" tabular foundation models`
4. `"tabular" "distillation" "incremental" "context"`
5. `"context edit" "distillation" "TabPFN"`

前两项用于后续文献，其余用于提案近邻；无直接命中不代表没有同义工作。

## 采用的主要外部来源

| 来源 | 访问范围与使用方式 |
|---|---|
| https://arxiv.org/abs/2502.05564 | TabICL原摘要/时间，首发前压缩路线；不声称全读前作 |
| https://arxiv.org/abs/2507.03971 | Real-TabPFN原摘要/时间；真实数据续训先例，不与Real-2.5混称 |
| https://arxiv.org/html/2506.16791v4#A2.SS2 | 已核实TabArena TableB.2：credit-g、blood、concrete任务来源/规模；真实任务追踪未执行 |
| https://arxiv.org/html/2605.13986v2 | TabPFN-3报告，重点§2架构/缓存/蒸馏；直接后继，不将其速度或范围记给2.5 |
| https://arxiv.org/html/2609.17895v1 | TabPFN-3.5报告，重点§3编码/预处理/联合训练与§2计时边界；另由abs页核实v2日期09-22，正文明确访问的是v1技术叙述 |
| https://arxiv.org/html/2608.10837v1 | TACTICL，2026-08-11；读§2–4，47任务、保持ICL与分类/回归压缩差异。直接作用于2.5，不是专有学生引擎的复现 |
| https://arxiv.org/html/2610.01435v1 | Jeong等，2026-10-01；读§3–4和成本表。teacher是TabICLv2/TabPFN-3，不能借它补写2.5专有loss；full/OOF仅指训练侧teacher监督 |
| https://arxiv.org/html/2610.06679v1 | Zeldes，2026-10-05；读§3与评估/限制。激活对齐已有先例，用于限制提案新颖性，不将其描述为2.5的直接实验 |
| https://arxiv.org/html/2610.05352v1 | 数据流研究，读摘要与成本/缓存讨论；context变化与缓存状态有效性近邻，不是2.5直接复现 |

## 访问限制与排除

- PriorLabs/TabPFN主仓库本轮访问超时。未验证当前默认版本/2.5构造API，不编造可运行命令；复现计划要求锁版本及权重并先做sanity check。
- *Compiled Task Memory for Efficient Inference with Frozen Tabular Foundation Models*，OpenReview `u92jC6FK2H`返回验证页；未核实全文。任务状态/编译方向可能与提案重叠，保留为未排除新颖性风险。
- 2.5原报告的私有验证任务、完整prior配方与proprietary蒸馏引擎仍不可从公开报告完全重建。公开后作不能代填。
- 未使用新闻/宣传摘要代替原文科学结论。3/3.5、TACTICL与其他论文的首发/修订不混写到2025年背景。
- 没有核实到足以整体推翻本报告的独立完整复现，不等于不存在反驳。未下载/训练teacher、学生或收费API。

## 提案范围

已因TACTICL撤回“压缩且保留ICL”作为新颖点，因activation alignment撤回“对齐隐藏差”本身作为新颖点。候选仅为显式context编辑语义、可组合补丁和独立编辑序列误差/更新成本。MotherNet、增量蒸馏、任务记忆与受限访问工作仍需系统补读；新颖性unknown。
