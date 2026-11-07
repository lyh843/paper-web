# DareFightingICE gRPC 论文翻译验收

- 论文：Improving Data Transfer Efficiency for AIs in the DareFightingICE using gRPC。
- 来源：https://arxiv.org/abs/2303.10001，v1，2023-03-11，5 页。
- 已通过 Zotero MCP 新增主条目 YICE4ZGU，并核验元数据、作者、分类 EX92BW5T（Agent / AgentBenchmark / Fight）和英文原附件 UQNX4E8Q。
- 使用软件：Zotero PDF2zh / PDF2zh-next 2.9.0；现有服务 openaicompatible；模型 gpt-6.1-sol。
- 仅生成全文左右对照 PDF：英文在左、简体中文在右。引擎退出码 0。
- 输出 5 页，每页 1224 × 792 pt；原文每页 612 × 792 pt。
- 逐页中文字符数：927、1397、189、1339、514。第 3 页以架构图和流程图为主，故中文较少；已人工查看。
- 5 页左侧原文规范化提取文本均与源 PDF 一致。
- 已查看全部 5 页渲染图，架构图、流程图、延迟曲线和表格保留，未见明显整页裁切。首页作者单位和邮箱换行较零碎。图片内部英文保留；未逐句人工校译。
- 源 PDF SHA-256：4a41209931bc76f50644f35d783b198f78806ac9b92332e0c746c220bef9e48c。
- 输出 PDF SHA-256：71197d4ccea54a78a4fd3f0d89b614dbbfc16e287239a5c0d0e73f97c4e51368。
- 原配置和原 PDF 均未变。

## 附回状态：待完成

译文已生成并完成上述检查，但两次 MCP `zotero_attach_file` 均返回 `Item 'YICE4ZGU' not found ([Errno 111] Connection refused)`。写入能力工具显示支持本地写入，读取附件列表正常，然而实际写入连接被拒绝；最后读取的主条目下仅有英文原件，没有确认新增对照附件。未绕过 MCP 直接写入存储或数据库。

拟新增附件名：`DareFightingICE-gRPC-2023.en-zh-CN.lr.pdf2zh-next-20261031.pdf`。恢复 Zotero 本地写入连接后，先查重，再将本目录 `arxiv_2303.10001.no_watermark.zh-CN.dual.pdf` 附到主条目 YICE4ZGU，并读取核验。无需重新翻译或重发翻译请求。
