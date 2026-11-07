# 中英对照 PDF 补入 Zotero

- 日期：2026-11-06。
- 用户已确认将四份既有译文附回对应论文主条目。
- 分类：人工智能 / Agent / CodePolicyGames（代码策略博弈），key `N32ZMEPM`。
- 来源清单：`translation-batch-20261105-191944.json`。该清单中的 `zoteroModified: false` 描述原翻译批次；本次补入是后续独立操作。
- 写入方式：Zotero MCP `zotero_attach_file`，本机运行中的 Zotero Local API，导入型子附件。
- 写入前核实分类、四篇标题与父条目 key；每篇原来仅有一份英文 PDF，无双语附件。

| 论文 | 主条目 key | 英文原附件 key | 新增双语附件 key | 文件名 |
|---|---|---|---|---|
| Policy-Conditioned Policies for Multi-Agent Task Solving | 3RVNLC7T | HVMXABJ9 | BWVILBP8 | arxiv_2512.21024.no_watermark.zh-CN.dual.pdf |
| Code-Space Response Oracles: Generating Interpretable Multi-Agent Policies with Large Language Models | KD862EQK | UXYRIZJ8 | 56HXU4L4 | arxiv_2603.10098.no_watermark.zh-CN.dual.pdf |
| Evaluating LLMs in Open-Source Games | HSDVNEPH | 7XVCIG4J | 5MM9ZRTS | arxiv_2512.00371.no_watermark.zh-CN.dual.pdf |
| Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in a Long-Running Game Agent Competition | 3UP5TTIW | B4VHEQMK | A99XW2YH | arxiv_2610.12341.no_watermark.zh-CN.dual.pdf |

## 回读核验

- MCP 回读四篇子条目，均为一份英文原附件及一份新增双语附件；父子关系与文件名正确。
- MCP 返回四份新增附件的本地路径；逐份读取 `/home/lyh/Zotero/storage/<新增附件 key>/<文件名>`，SHA-256 均与来源清单一致。
- 四份英文原件 SHA-256 再次核验未变；本地译文保留。
- 成功 4，失败 0；未重新翻译、未覆盖或删除原件、未执行实验。未核验跨设备同步状态，未刷新语义检索索引。
- 译文既有排版限制仍适用，见 `bilingual-translations-20261105-191944.md`。
