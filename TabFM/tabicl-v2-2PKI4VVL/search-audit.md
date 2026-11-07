# TabICLv2 · 来源与检索审计

日期/截止：2026-10-26；中文13问完整深读。来源读取、教学推导、待验证提案与自动页面检查分别记录，不声称独立读者研究或科学复现。

## 原文与版本

- 主条目2PKI4VVL/附件HU3LBRYN，本地79页v2；SHA256 `71554be35ba3847a14267912d9738f6049545cf74a30d860de1ed23d14d95246`，与旧记录相同。
- https://arxiv.org/abs/2602.11139 ：2026-02-11 v1，2026-09-16 v2；ICML2026。背景按首发，具体公式/消融/后加Appendix L按本地版本。
- 本轮重读主文pp.1–9，Appendix A结构/多类、B课程、H资源、I分位数与排序、L新增实验，核对相关图和数据定义；J/K聚合延用原审计并核对其正文解释。全文均可访问，不把提取79页说成每个GP证明和表格数值都独立重验。
- 旧版归档 `revisions/pre-research-prompt-20261026/`；不修改PDF/Zotero。无可用Zotero MCP，按已知条目指纹处理。

## 实际搜索查询

functions.websearch检索，functions.webfetch打开原始来源：

1. `"TabICLv2" 2026 follow up calibration prior limitations`
2. `"attention" "duplicate" "length" "measure" transformer invariance`
3. `"TabICL" "duplicates" attention context multiplicity`
4. `"Diagnosing and Repairing Context Vulnerabilities"`
5. `"cardinality" "multiplicity" attention "set transformer"`（无直接搜索结果）
6. `"attention" "replication invariance"`
7. `"set transformer" "cardinality" "softmax"`
8. `"softmax" "duplicate invariance"`

搜索不是穷尽综述；复制/相关证据/温度同义方向仍可能漏检。

## 主要已核实来源

| 来源 | 访问范围与用途 |
|---|---|
| https://arxiv.org/abs/2502.05564 | 原TabICL摘要与时间，确认压缩路线；不声称完整复核前作 |
| https://arxiv.org/abs/2507.03971 与 https://arxiv.org/abs/2511.08667 | Real和2.5身份/时间；不能把真实续训与纯合成混为一个checkpoint |
| https://github.com/soda-inria/tabicl | 官方README完整可读：v2分类/回归权重名、kv_cache、预训练脚本、微调/forecast，以及AMP/cautious_wd复现备注。当前软件状态不倒写为原论文全部实验 |
| https://arxiv.org/html/2605.13986v2#S2.SS1 | TabPFN-3明确引用三阶段/早期目标/分组/QASSMax，为直接技术承接，不只是citation |
| https://arxiv.org/html/2606.30410v1 | BeyondArena§1–6与协议，142表/11模型含TabICLv2；更广数据范围与不同预算，不从新旧Elo估计单机制效应 |
| https://arxiv.org/html/2606.11473v1 | CRUMB摘要、§1–5及限制；三冻结backbone含TabICLv2。full-context与0.1N预算排名不是同信息预算，不称full必劣 |
| https://arxiv.org/html/2610.01435v1 | Jeong等蒸馏§3–4/表4，TabICLv2是teacher；静态学生不自动有任意context更新能力 |
| https://arxiv.org/html/2610.05352v1 | 数据流研究§3–5、缓存proof-of-concept与限制；直接包含TabICLv2，但增量缓存模型另行训练，不冒称公开v2原生支持 |
| https://arxiv.org/html/2609.27679v2 | RefineICL摘要、机制与distinct-evidence实验定位；已有“新增独立证据 vs 重复”近邻，不能声称复制诊断首创。没有独立重验其全部证明 |
| https://arxiv.org/html/2610.06679v1 | 激活对齐近邻，读方法/限制；不是本文QASSMax消融或直接v2复现 |

## 访问限制与未完成项

- DiReCT，OpenReview `I6F1jtMsum`：搜索摘要给出context漏洞/重复线索，但PDF实际打开为验证页。未核实完整方法、时间和结果；不将搜索snippet当实验事实，正文将其列为新颖性风险。
- Set-Transformer/softmax通用搜索用来发现方向，未将未打开论文的结论写成事实。固定logit复制公式自行推导，显著标为教学计算，不能描述成原模型实验。
- 未取得原Fig3全部生成坐标和三个280K对照checkpoint；一周计划明确精确复现与同类新构造诊断的区别。推理期identity干预不是重新预训练的No-SSMax模型。
- 正文承认原v2 Appendix L.6随机噪声稳健性证据；未宣称任何噪声都会失败。针对anchor的误标须有可识别真值和对照。
- 无独立模型训练、权重下载、污染重查或完整附录GP证明复核。未找到经核实的整体反驳不等于不存在。

## 提案新颖性边界

复制敏感性、加权attention、query gate及新增证据诊断都不声称新。候选目标是有来源/采样元信息条件下，同时学习机械复制不变、独立观测敏感与校准/拒绝；看不到来源可能不可识别。受限DiReCT及概率测度/相关样本的统计文献需补读，novelty unknown，不保证首创。
