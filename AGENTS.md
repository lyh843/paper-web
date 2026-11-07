# Zotero 论文阅读库

## 目录映射

- `/repo/paper-web` 对应 Zotero「人工智能」分类（collection key: `JETPAJW9`），不是整个 Zotero 文献库。
- 其子目录与 Zotero「人工智能」内的分类同名、同层级，保留大小写与中文名称。例如「人工智能 / TabFM」对应 `/repo/paper-web/TabFM`，「人工智能 / Agent / AgentBenchmark / LongHorizon」对应 `/repo/paper-web/Agent/AgentBenchmark/LongHorizon`。
- 不为「学习资料」「kr's」「计算方法」「网络科学」等其他顶层分类生成目录。
- Zotero 连接允许读取和写入。用户明确要求或授权的任务范围内，可以通过 Zotero MCP 新增和更新文献、附件、分类、标签、笔记及批注，包括导入网页归档和添加中英对照 PDF。
- 写入前核实目标文献、附件和分类，检查重复；保留原始文件和无关内容，完成后读取核验实际结果。删除、清空或批量覆盖等破坏性操作必须先确认具体范围；禁止直接修改 Zotero SQLite 数据库。

## 阅读 skill

- 用户指定使用 `paper-reading`，安装于 `.opencode/skills/paper-reading/`。它以指定上游为基础，现已按用户要求本地增强“发表时研究背景”；不要用其他阅读 skill 替代，也不要在更新上游时覆盖本地增强。
- 来源：<https://github.com/xiaofengShi/paper-reading-skill>
- 本次复制的上游 commit：`eadd0cd61d276d082938d80eb0d3fbb85614f2e1`。
- 本地增强与来源记录见 skill 目录的 `LOCAL_CHANGES.md`；不再将增强版称为与上游逐字节一致。
- 执行论文阅读前加载此 skill，并按需阅读它的 references 和质量检查要求。
- 默认中文、完整深读；用户另行指定语言、深度或视角时遵循其要求。
- 默认深读采用 skill 中的 13 项 Prompt（`references/user-prompt.md`）：前 8 项完整理解之外，必须包括脆弱假设、一周最小复现方案、公平反例、实际搜索核实的后续研究，以及从局限与需求出发并经新颖性检索的 follow-up idea。严格区分原文、已有文献、合理推断与不确定猜测，交付包含丰富可视化和有效交互的离线 HTML；检索或来源受限时如实标记，不保证 idea 首创。仅提出实验方案，不自动执行实验。

## 批量读取 Zotero 分类

当用户要求“对 TabFM 中的所有论文执行这个 skill”等任务时：

1. 通过 Zotero MCP 确认目标分类及 key，分页枚举该分类的全部条目，不能只读取第一页。若包含子分类，先明确处理范围并将输出映射回各自分类；默认只处理指定分类的直接条目。
2. 以论文主条目为单位处理，不把其子 PDF 附件、笔记再算作独立论文。无父条目的独立 PDF 经确认确实是一篇未处理论文时，可按其自身 key 处理。用 PDF 指纹核对重复；同一全文只保留一份解读，优先保留当前分类仍在使用的主条目目录，记录被移除的重复输出，不能删除 Zotero 原文或条目。
3. 获取并核实论文身份、版本及完整原文，优先使用本地 PDF；缺少全文时尝试可访问的原文来源。无法完成全文阅读的条目如实报告，不生成冒充完整深读的内容。
4. 逐篇执行 `paper-reading`，遵循全文覆盖、发表时研究背景、图表和公式核验、证据锚点、可视化与最终质量检查要求。方法之前必须解释当时领域状态、具体前作贡献、尚存缺口与本文动机；区分首发时间和后期修订，禁止用后来的研究倒推当时背景。渲染前运行 `scripts/check-background.cjs`，再做历史内容的人工核验；结构检查不能代替事实核查。不能用通用模板或摘要替代逐篇解析。
5. 每篇输出到对应分类下独立目录：`<分类路径>/<paper-slug>-<zotero-item-key>/index.html`。例如 `/repo/paper-web/TabFM/<paper-slug>-<zotero-item-key>/index.html`。
6. 同目录保留 `reading.md` 审计源及需要的 `assets/`。HTML 必须按 skill 要求自包含、离线可读；不能依赖 skill 安装目录中的资源才能打开。
7. 从已安装的 skill 目录调用渲染器：`node /repo/paper-web/.opencode/skills/paper-reading/scripts/render-reading.cjs <reading.md> <index.html>`。已安装 npm 依赖；缺失时在 skill 目录运行 `npm ci`。
8. 不覆盖不明来源的已有输出。完成时列出成功、失败、跳过的论文及生成文件路径，区分真正通过检查的成果和未完成项。

仅搭建目录或安装 skill 时，不自动开始解析论文。
