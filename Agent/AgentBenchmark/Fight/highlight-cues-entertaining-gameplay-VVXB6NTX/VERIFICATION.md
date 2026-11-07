# 双语 PDF 验收记录

- 论文：A Fighting Game AI Using Highlight Cues for Generation of Entertaining Gameplay
- Zotero 主条目：VVXB6NTX；原文附件：6SHLC5E7；作者勘误笔记：WKU2QDFH。
- 来源详情见 `SOURCE.md`。
- 引擎：PDF2zh-next 2.9.0，现有 OpenAICompatible 配置及 gpt-6.1-sol 模型。
- 范围：全文 6 页，左英文、右简体中文，仅对照 PDF。
- 产物：`translation-20261031/original.no_watermark.zh-CN.dual.pdf`。
- 引擎退出码：0；文件大小：1,020,624 字节。
- 生成页面：6 页，每页 1224 × 792 pt，左右拼接而非交替页。
- 原文 SHA-256：`b0bcc164cfa4a8a5631510b0ab2072347ce10b8a973e1d84528d7d53b96f7b58`。
- 输出 SHA-256：`f3515ce9627dcfdaa1ff59c799f403f88eee23ce23d6c76620d4ca89ba88faf0`。
- 自动检查：页数匹配；每页均有中文，汉字数依次为 1271、1202、1028、1535、751、1385；左侧各页经 Unicode 规范化及去除空白后的文本均与原文一致。
- 原 PDF 和用户原配置不变；Zotero 中原文附件再次计算的 SHA-256 与上述原文哈希一致。用户随后明确要求将译文存入 Zotero，已将对照 PDF 导入主条目 VVXB6NTX，译文附件 key：G6VSDWHH，文件名：`Ishii-2019-Highlight-Cues-Entertaining-Gameplay.en-zh-CN.lr.pdf`；再次读取确认原文附件和勘误笔记仍保留。

## 可视核验（2026-10-31）

已渲染并检查全部 6 页，覆盖标题和摘要、正文、MCTS 流程图、公式 (1)–(6)、表格、统计图、结论及参考文献。英文在左、中文在右，图表和公式可见，未见明显正文或图表裁切。渲染图保存在 `translation-20261031/visual-review/`。

可见排版局限：第 1 页作者单位和邮箱存在不自然换行，第 3 页表 III 中文表头较紧凑；图片内英文标签保留。上述检查不是逐句人工校译，不保证术语准确或像素级排版一致。

## 阅读时必须结合作者勘误

原文第 3 页关于“移除延迟约束”的表述已被作者主页更正，译文忠实保留原文说法，未擅自改写。作者说明实际实验保留延迟约束，AI 使用预测当前状态的机制。请结合 `SOURCE.md` 或 Zotero 勘误笔记阅读。

综合结果：自动检查通过，6 页均已完成可视排版检查。
