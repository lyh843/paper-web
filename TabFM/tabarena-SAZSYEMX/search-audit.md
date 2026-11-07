# TabArena · 检索与来源审计

日期与截止：2026-10-26。目的：按 `research-prompt-v1` 重生成当前单篇解读，核实发表背景、直接后续工作、批评与提案近邻。此记录是生成者的检索审计，不是系统综述或独立复现实验。

## 原论文身份与阅读范围

- 原文：*TabArena: A Living Benchmark for Machine Learning on Tabular Data*。
- 本地 PDF：`/home/lyh/Zotero/storage/GDLD54RX/Erickson 等 - 2025 - TabArena A Living Benchmark for Machine Learning on Tabular Data.pdf`，66 页。
- SHA256：`8853fd1a1eb09ee7c25bf6f48a194a8e718103774d39af5bcc402b2c41a735e5`；与既有 provenance 一致，原文未修改。
- arXiv https://arxiv.org/abs/2506.16791 ：v1 2025-06-20；v4 2025-11-03。页面 comment 写 51 pages，与实际 66 页 PDF 不同，正文按实际 PDF，不以 comment 推断长度。
- 已读取本地正文、主要图/图注、方法和评估相关附录 A–E；核对 Table A.1 全表、B.2 的 credit-g 行、F.1 的协议/检验说明与相关任务行。搜索空间表阅读用于核实方法差异，不将所有附录数值逐字转写。
- 同版本 HTML：https://arxiv.org/html/2506.16791v4 。与本地 PDF 交叉核对；HTML 的公式/数字可能出现双重可访问文本，如 142142，不作为新数字。
- 本地提取文本与页面渲染仅放在 `/tmp/opencode/tabarena-research-20261026/`，未向 Zotero 写数据。本环境没有可用 Zotero MCP 工具；本次处理已知主条目，不重新枚举分类。

## 实际搜索查询

工具：`functions.websearch`；正文与元数据打开使用 `functions.webfetch`。以下为实际执行查询，不暗示覆盖全部引用文献。

1. `TabArena benchmark 2026 extension replication critique TabArena 2506.16791`
2. `"TabArena" "2026" benchmark limitations validation overfitting`
3. `"TabArena" follow-up TabRepo TabPFN-2.5 TabICLv2`
4. `"TabArena" criticism replication benchmark contamination`
5. `tabular benchmark adaptive overfitting reusable holdout dataset acquisition ranking certificate deployment mixture uncertainty`
6. `machine learning benchmark "ranking" "transportability" "certificate"`
7. `"benchmark" "rankings" "task distribution" "optimal transport"`
8. `"benchmark ranking" "distributionally robust" task`
9. `"active" "benchmark" "ranking" dataset acquisition model evaluation`
10. `"RankBALD" active evaluation`
11. `"benchmark" "task acquisition" ranking`
12. `"benchmark" "decision regions" model ranking`
13. `"The Benchmark Lottery" arxiv`

查询 1–4 用于后续研究；5–13 用于提案近邻与新颖性筛查。搜索得到模型报告、综述和其他扩展线索，但本页只保留核实程度足以支撑所写结论的少数工作。没有找到经本轮核实、足以判定“TabArena 整体被推翻”的独立训练复现；不能据此宣称没有反驳。

## 打开与采用的主要来源

| 标识 | 文献或来源 | 访问范围、定位与使用边界 |
|---|---|---|
| P0 | https://arxiv.org/abs/2506.16791 与本地 v4 PDF | 身份、首发/修订、本文正文与相关附录；所有旧榜单仍为 v0.1 |
| H1 | https://arxiv.org/abs/2003.06505 | AutoGluon 2020 原摘要；只用于多模型组合/stacking 的先例，不声称全文复查 |
| H2 | https://arxiv.org/abs/2305.02997 | TabZilla 2023 首发、2024 v4 摘要；19算法/176表与调参重要性；不把后期研究当早期依据 |
| H3 | https://arxiv.org/abs/2311.02971 | TabRepo 2023 首发、2024 v3 摘要；预测缓存、低成本模拟与迁移；直接基础设施关系另由 P0/代码 README 确认 |
| H4 | https://arxiv.org/abs/2407.04491 | RealMLP 2024 首发、2025-01 v3 摘要；强默认与留出元测试，不转述所有实验 |
| H5 | https://arxiv.org/abs/2406.19380 | TabReD 2024 v4 摘要；8工业数据集与时间/随机切分的不同排序，属于首发前背景 |
| S1 | https://arxiv.org/abs/2606.30410 与 https://arxiv.org/html/2606.30410v1 | BeyondArena，2026-06-29 v1；读摘要、§1–6和分组划分消融 F.2。142表/11模型，直接扩展；不称独立复现，不与旧 Elo 做差 |
| S2 | https://arxiv.org/abs/2606.02384 与 https://arxiv.org/html/2606.02384v1 | TabPrep，2026-06-01 v1；读§1–4及协议相关附录定位，重点§3.5/§4和B.8；不把它的FE等同于旧版完全无预处理 |
| S3 | https://arxiv.org/abs/2605.17273 与 https://arxiv.org/html/2605.17273v3 | 2026-05-17首发、2026-06-03 v3；读§3–4/Table1及B.6。分析2025-12-11快照，独立后续解释性分析；原始误差均值、阈值和Elo不同，不照抄fragility数值当官方排行榜错误率 |
| N1 | https://arxiv.org/abs/2107.07002 | The Benchmark Lottery，2021-07-14，核对原摘要；证明任务选择影响排序不是本提案首创 |
| N2 | https://github.com/bonaventuredossou/al_rankbald | 作者公开README，RankBALD，COLM2026；读摘要、目标与仓库说明。成对排序互信息已有先例；未核实完整论文证明，不照搬数值 |
| C1 | https://github.com/autogluon/tabarena 与 raw README | 当前官方维护入口与artifact分层/依赖。来源状态是2026年，不写进2025年方法能力 |
| C2 | https://api.github.com/repos/autogluon/tabarena/commits/main | 查询到提交95820a2cec37174fe3e25da4df80e11ae76b8761，2026-10-25；冻结访问定位，不声称训练产物自动等于v0.1 |
| C3 | https://raw.githubusercontent.com/autogluon/tabarena/main/examples/plots/run_export_results_per_split.py | 核对逐split导出、字段和下载位置，确为脚本；未安装或执行TabArena，不把存在脚本当可运行复现已通过 |

## 访问限制、排除与诚实边界

- OpenReview PDF `https://openreview.net/pdf?id=kQVC2vQvcx`（搜索线索 *Leaderboards rank finer than they resolve*）返回浏览器验证页，未核实全文，不采用其技术结论或声称提案已胜过它。它可能是相关近邻，仍列为新颖性风险。
- RankBALD raw README 第一次抓取超时，随后 GitHub 仓库页面可读；完整论文证明未核实。正文仅引用作者README中的目标与方法概述。
- 一个早期手工尝试的 arXiv 2103.03012 返回旅行商 Transformer 论文，与目标不符；被排除。正确 Benchmark Lottery 标识通过搜索确认是 2107.07002。未混用身份。
- 两次尝试向临时目录安装PDF工具下载超时，随后使用现有conda环境的PyMuPDF读取本地PDF；未改变项目依赖或Zotero环境内容。
- 未追尽每篇引用链、未访问所有后续模型的全文、未完成主动评估/稳健选择领域的系统综述。提案只称“本次已核实范围内的候选贡献”，不保证首创。
- 未下载TabArena的raw/processed/训练结果全集、未训练、未进行数据污染检测或独立模型复现。第10节给出方案而非完成记录。

## 从证据到新提案的边界

提案对比三类已存在的思路：扩大任务覆盖（BeyondArena）、缩减固定基准评估（BeyondArena-Core/RankBALD）、揭示排名脆弱性（Benchmark Lottery/Oh）。候选不同点是围绕用户声明的任务混合/成本区间，维护可拒绝的决策结论并主动补证。稳健重加权、主动采集和区间估计本身均不被声称为新方法；独立任务来源上的风险–覆盖与获取成本才是拟议判别目标。需要进一步核实上述受限近邻和选择后推断文献。
