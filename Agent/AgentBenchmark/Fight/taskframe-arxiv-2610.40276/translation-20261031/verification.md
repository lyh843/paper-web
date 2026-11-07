# TaskFrame 中英对照翻译验收

- 论文：TaskFrame: Connecting Task-Level Planning with Frame-Level Control for Game Agents。
- 来源：https://arxiv.org/abs/2610.40276，PDF：https://arxiv.org/pdf/2610.40276v1。
- 版本：v1，arXiv 首发日期 2026-10-29；PDF 内文另印日期 2026-10-30。
- 使用软件：Zotero PDF2zh / PDF2zh-next 2.9.0。
- 使用现有服务：openaicompatible；模型 gpt-6.1-sol；未更改原配置。
- 输出：全文英语→简体中文，仅左右对照，英文在左、中文在右，无水印；包含附录，共 20 页。
- 引擎退出码：0。输出每页 1224 × 792 pt，原文每页 612 × 792 pt。
- 20 页均存在中文，左侧规范化提取文本逐页与原件一致；逐页统计见 translation-status.json。
- 第 20 页中文仅 51 字，已视觉核验该页主要为游戏截图对比及图注，属正常情况。
- 已查看第 1、2、4、5、6、7、9、14、18、20 页渲染图，覆盖首页、正文、架构图、方法公式、实验表格、附录和末页。抽查未见明显整页裁切；图片和公式保留。部分表格中文较小，少量公式邻近英文保留；图片内部英文不保证翻译。未进行逐句人工校译。
- 源 PDF SHA-256：291e0d94d6d47676a94615c0f057690b8d684b4d7c68b34cc3508a4bd396e993。
- 输出 PDF SHA-256：302f35fb657c71f869c8f9b4fd712d05eaab3c346031480ee9bcf2e129752d8b。
- 原 PDF 和原软件配置均未变。

## Zotero 导入：已完成（用户改为 System1 分类）

用户随后指定导入“System1”。已核实该分类为人工智能 / System1（G2VDMDFY），本地写入连接已恢复。重新查重后，已通过 MCP 创建主条目 IGN5D6CY，英文原附件 XHNSL6MK，附回已有双语对照版 F7TU7CM9；重新读取元数据和附件列表，确认分类为 G2VDMDFY、两份附件均存在。Zotero 内原 PDF 和对照 PDF 的 SHA-256 分别与上文记录完全一致。未重新翻译，未产生新的翻译请求。

本地文件仍保留此前生成位置，未移动或删除；Zotero 实际归类以用户最新指定的 System1 为准，未额外归入 Fight。

### 历史失败记录（现已解决）

目标分类：人工智能 / Agent / AgentBenchmark / Fight（EX92BW5T）。导入前分别按 arXiv ID 和 TaskFrame 标题查重，均无匹配。

MCP zotero_add_item 返回 `Error adding by URL: [Errno 111] Connection refused`，没有获得主条目或附件 key。翻译后再次查询 TaskFrame 仍无匹配；write_capabilities 报告本地模式、不支持本地写入、未配置 Web API 凭据。该报告不是对用户实际 Zotero 版本的独立核验，不应仅凭它断定必须升级。

因此目前只完成本地原件下载和翻译，未确认原件或译文入库；未绕过 MCP 修改库。恢复连接后应重新查重，通过 MCP 将论文及原 PDF 导入 EX92BW5T，再将本目录对照 PDF 附到主条目并重新读取核验。无需重新翻译。

来源元数据见上级目录 source.json；自动检查见 translation-status.json；脱敏引擎日志见 translation.log。
