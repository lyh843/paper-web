# FightLadder 项目网页归档说明

- 用户输入：`http://sites.google.com/view/fightladder/home?utm_source=chatgpt.com`
- 规范来源：<https://sites.google.com/view/fightladder/home>（移除跟踪参数并使用 HTTPS）。
- 范围：该项目网页，不是其所链接的 arXiv/ICML 论文，也不自动归档外链页面。
- 作者：Wenzhe Li、Zihan Ding、Seth Karten、Chi Jin；机构 Princeton University。
- 网页未声明发布日期，CSL 元数据留空；正文中的 2024 年是所引用论文的年份。

## 经用户确认的缺图版本

本次已向用户说明 24 张正文图片中 23 张返回 HTTP 403、14 个 Google Drive 视频尚不能离线保存；用户明确选择“继续制作缺图版”。这不是图文完整归档。

- 完整保留 68 个原网页文本块，涵盖标题、作者、摘要、全部正文、图注、目录和 Citation 中的 BibTeX。
- 仅 1 张正文 GIF 成功下载（Fatal Fury 2）；HTML 保留动画，PDF 仅显示静态帧。图片内部文字未翻译。
- 23 张不可获取的图片用编号占位说明替代，每处保留该原图片的在线链接；未用论文中的其他图片或自制图冒充原图。
- 14 个视频保留文件名和原始 Google Drive 在线链接，不声称可离线播放。
- 第三方 Elfsight 组件未保留；原始嵌入代码仍在溯源文件 `source.html` 中。
- Google Sites 动态网格布局改为安全的单栏静态阅读/打印布局；保留正文内联格式并下载原网站字体，但不声称原站像素级复刻。

## 验证

原文 PDF 共 6 页，逐页查看了首页、唯一可用图片页、正文页和引用末页。排除打印页码后，全部 68 个原文文本块在 PDF 中均可匹配，HTML 亦全部匹配。

Chromium 在离线上下文中加载阅读入口，未产生远程资源请求；唯一可用 GIF 可正常解码。原页面没有独立 HTML 数学公式或表格；部分无法保存的图表位于缺失图片中。

`source.html` 为原始溯源 HTML，可能含原网站脚本；安全阅读入口为 `index.html` 或 PDF。所有图像、字体及来源和文件哈希见 `manifest.json`；逐处缺失资源清单见 `verification.json`。

## Zotero

目标分类：人工智能 / 网页博客（`3CSJ9YAV`）。

已有同名 ICML 论文 `QTGVUCDF` 的 URL、条目类型和附件均已核实，它与本次网页归档不是同一载体，未修改或重建。网页使用单独的 `webpage` 条目，key 为 `ITXN4SQT`。附件状态与哈希核验结果见 `import-status.json`。
