# TabDPT-Turbo · 来源、时间修正与检索审计

日期/截止：2026-10-26；中文13问完整深读。主条目DFAGC498，附件FMN7AKYM，本地9页PDF SHA256 `ce6c969a9591305afc101e6042c5713195e3bb0a68a84bade802e75bffbef366`；本轮重读完整9页正文/附录/图注，原PDF未修改。

## 关键时间修正

- arXiv https://arxiv.org/abs/2608.01400 ：2026-08-02 v1、2026-08-25 v2，非归档ICML FMSD workshop poster；本地结果对应v2/v1.2模型。
- 官方 https://github.com/layer6ai-labs/TabDPT-inference/releases/tag/v1.2.0 ：release页面显示17 Jun，README明确为June17,2026；提交 `9cfb05e0a6bc380ae6c99c08adc8d50dacd4f246`。已公开无检索默认/full context/新权重，当时写Paper link coming soon。背景cutoff修正为2026-06-17，basis=first-official-software-release；完整论文实验不声称当时已披露。
- 官方 https://github.com/layer6ai-labs/TabDPT-inference/releases/tag/v1.3.0 ：2026-09-08后继，提交 `97e5494431e9527c7edb31cb4dcfc5f00b232fdf`；不能用当前v1.3权重跑完后称复现本文。
- https://arxiv.org/abs/2606.11473 ：CRUMB 2026-06-09已公开，故放在已有方案，不误称Turbo后作，也不推断作者受它启发。
- Shaheen等2608.17957v1于2026-08-18公开，是6月软件发布后的机制解释/同期研究，不能当最初动机。

旧输出和assets在 `revisions/pre-research-prompt-20261026/`，更早归档保留。无可用Zotero MCP，本轮只核实已知条目本地指纹，未声称枚举整个分类；未改Zotero。

## 实际搜索

functions.websearch查询，functions.webfetch打开来源：

1. `"TabDPT-Turbo" follow up criticism 2026`
2. `"tabular" "shared context" "retrieval" "adaptive" caching`
3. `"TabDPT" "batch" "cache" "retrieval" scheduling`
4. `"compiled task memory" tabular`
5. `"tabular" "context" "query batching"`

CRUMB由已打开LoGIC原文参考文献21追溯到2606.11473，并直接打开其abs/HTML，不只依赖搜索摘要。候选新意随实际检索撤回“聚类query共享检索”为原创。

## 已核实的主要来源

| 来源 | 读取范围与使用边界 |
|---|---|
| https://arxiv.org/abs/2406.05207 | LoCalPFN原摘要/日期，检索+微调先例；不声称此轮全文核验 |
| https://arxiv.org/abs/2502.05564 与 https://arxiv.org/abs/2602.11139 | TabICL/v2首发和结构背景，具体机制由本地v2正文核实 |
| https://arxiv.org/html/2605.13986v2 | TabPFN-3架构/缓存已有路线，不能把cell模型都写成从未解决服务问题 |
| https://github.com/layer6ai-labs/TabDPT-inference | 官方README：v1.2/v1.3状态、版本选择、权重下载、复现说明；README混合版本/旧表，不将所有表格认作Turbo论文结果 |
| v1.2.0/v1.3.0 release页 | 先后关系/默认接口/commit；准确时间与功能取自官方页面，不凭arXiv月份推断 |
| https://arxiv.org/html/2608.17957v1 | Shaheen等摘要、§2–4/限制，真实SSL任务与内部检索解释。有作者重叠，非独立完整Turbo复现；dataset去重结论限其设置 |
| https://arxiv.org/html/2606.11473v1 | CRUMB§1–5/限制和在线附录定位；cluster-shared context已有方案，质量/预算与full不同，非直接Turbo实验 |
| https://arxiv.org/html/2609.05955v1 | LoGIC摘要、相关工作与§III–IV：图任务的两预算与簇共享，不冒充同机Turbo计时；揭示CRUMB参考文献 |
| https://arxiv.org/html/2609.37959v1 | TabFM摘要、§3.3/表2、限制，包含Turbo质量比较；绝对Elo/文本协议与原快照不能拼接 |
| https://arxiv.org/html/2610.05352v1 | 数据流研究§3–5与缓存/延迟限制；未直接评估Turbo，不能写成Turbo的独立反证 |
| https://arxiv.org/html/2610.01435v1 与 https://arxiv.org/html/2610.06679v1 | 服务/蒸馏/激活近邻，用于提醒缓存/静态任务模型不同，不写成Turbo已支持的功能 |

## 限制与科学边界

- GitHub release API两次返回403，改为官方release网页和README核实成功；不是没有查到就编造日期。
- *Compiled Task Memory for Efficient Inference with Frozen Tabular Foundation Models*，OpenReview `u92jC6FK2H`返回验证页；未核实方法/结果，保留为提案近邻风险，不拿搜索片段证明不同。
- 原文未披露长度温度精确函数，不移植QASSMax公式当原实现。CRPS标准积分和attention配对数是教学解释，未运行网络。
- 原文0.76秒总体口径与Table1的0.44/0.19分项未强行统一；原文§3.2简写输出支持范围与§3.3明确[-10,10]的表述差异按更具体目标段落说明，没伪造实现。
- 复现计划锁定v1.2；最新库默认v1.3，任何替换需另标。预算/硬件可行性是条件估计，未实测安装、模型运行或收费算力。
- 没有核实到整体推翻效率主张的独立完整复现；不证明没有反驳。本轮非穷尽综述、未执行模型训练或预训练去重。

## 提案范围

CRUMB/MixturePFN/LoGIC已覆盖共享局部context，故新提案不以它为首创。候选对象是固定每query context契约、对伴随query/batch不变，以及在该语义误差容限内复用计算。深层context状态非线性相依，overlap不等于可直接拼KV；若只能复用少量初始计算可能无价值。需补读受限task-memory与精确attention复用近邻，novelty unknown。
