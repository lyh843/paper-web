---
name: zotero translate
description: >-
  使用用户本机已注册的 Zotero PDF2zh / PDF2zh-next 软件，翻译指定 Zotero 文章或本地 PDF；默认只交付左英文右中文的中英对照 PDF。用于“用 Zotero PDF 翻译这篇文章”“用 Zotero PDF2zh 翻译”“生成中英对照”等请求。先从命令行发现桌面启动器、服务、引擎和已有配置，不要因 Zotero MCP 无翻译工具就断言无法调用。
---

# zotero translate

Skill ID 为 **`zotero-translate`**，显示名为 **`zotero translate`**。

默认目标：**全文，英语 → 简体中文，保留图文与公式，仅中英对照 PDF，英文在左、中文在右**。用户指定其他语言、页码或单双语输出时遵循指定范围。不要擅自用自己生成的译文、在线翻译网站或其他模型替代用户指定软件。

## 1. 确认原件和权限

- 对指定 Zotero 文章，通过 MCP 核对标题、作者、来源、主条目/附件 key 与页数，优先取得本地 PDF。
- **不要只查主条目标题**：用户直接拖入的独立 PDF 可能叫 `article`。查不到时分页列举目标分类，核对附件首页和文件指纹。
- 多篇同名、多个版本或多份附件不明确时先澄清；不能把某篇相关论文代替目标文章。
- 读取适用 `AGENTS.md`。本地翻译不需要更改 Zotero；项目只读时仍能读取 PDF 并把译文保存到项目目录，但不能新增译文附件、改条目或写数据库。
- 以独立输出目录处理本地副本，不改动 Zotero 原文件；不得通过插件、HTTP 或本地路径绕过只读规则。

## 2. 从本机发现软件，不要先猜“没有接口”

先读 [本机发现与调用](references/local-software.md)。允许使用 shell 检查相关的命令、`.desktop` 注册项、启动器和 user service，只检查任务所需目录，不遍历或打印所有环境变量、凭据或浏览器数据。

本机已验证线索（每次确认仍存在，不当成跨机器默认值）：

- 桌面项：`~/.local/share/applications/zotero-pdf2zh.desktop`
- 启动器：`~/.local/bin/launch-zotero-pdf2zh`
- 服务：`~/.config/systemd/user/zotero-pdf2zh.service`
- 软件：`~/zotero-pdf2zh/server/`，本地服务通常为 `http://127.0.0.1:8890/`
- 引擎：`~/miniconda3/envs/zotero-pdf2zh-next-venv/bin/pdf2zh_next`
- 既有配置：`~/zotero-pdf2zh/server/config/config.toml`

可以先运行辅助脚本发现已知入口：

```bash
python <skill-dir>/scripts/translate_pdf.py discover
```

CLI 可用时直接使用软件的同一翻译引擎即可；不必为了“使用软件”额外启动 GUI 或后台服务。找不到 CLI 时才研究已发现服务的真实路由/schema，不能猜接口。

## 3. 复用现有配置，保护密钥

- 确认引擎和当前服务已配置；用安装环境中的 `pdf2zh_next --help` 验证参数，不能照搬未验证版本参数。
- 读取配置是为执行用户请求；只输出服务名、模型名及凭据是否设置，不输出密钥值，不把密钥放进命令行、公开日志、状态 JSON 或 skill 文件。
- 使用已配置服务/模型，不擅自替换模型或注册付费服务。翻译会向现有翻译服务发送文章文本，并可能消耗其额度；启动前简短说明使用现有服务，无需重复索要已经配置好的凭据。
- 辅助脚本在权限为 0600 的临时配置中修改本次参数；不写回用户配置，日志按已有敏感值脱敏，临时配置结束后清理。
- 若服务缺少凭据、版本不兼容或网络异常，报告实际错误；不要输出配置原文或开启含凭据的调试日志。不要无限重试造成额外费用。

## 4. 默认只生成中英对照

先确认选中的 PDF 和引擎，再运行：

```bash
<engine-python> <skill-dir>/scripts/translate_pdf.py run \
  --input '<verified-source.pdf>' \
  --output '<new-translation-directory>' \
  --engine '<discovered-pdf2zh_next>' \
  --config '<existing-config.toml>'
```

辅助脚本使用 Python 3.11+ 标准库。为 PDF 自动检查，在实际引擎的 Python 环境运行它（该环境通常已有 PyMuPDF）。参数含 `--source-lang`、`--target-lang`、`--pages`、`--layout lr|alternating`、`--timeout`。**默认禁用单语输出，不先额外生成中文版再删除。** 不设置 `--pages` 才是全文翻译。

- 输出目录必须是新目录，保留原件，不覆盖已有译文。需要单语输出等脚本未覆盖的需求时，按 `--help` 在临时配置上适配，不擅自修改软件源代码。
- 长任务可通过 shell 后台运行并等待完成通知；不要反复 sleep/poll。没有结果前只能报告“运行中”，不能报告“已翻译完成”。
- 用户执行中改为“只要对照版”时，以新要求为准，已进入翻译阶段则不要为取消额外输出重跑全部收费请求；完成后仅清理本次任务生成且明确不需要的单语文件。

## 5. 验收和交付

- 核对引擎退出码和实际输出，不能把日志中单独一句“完成”当作成功，也不能因退出清理日志包含“canceled”就误判成功产物失败。
- 检查对照 PDF 页数与原文范围相符、中文确实存在、原文侧文字保持、图片与公式保留、无明显裁切。英文→中文时检查每页中文字符数量；参考文献/纯图页允许例外，但必须人工核验原因。
- 左右对照时，源页面通常是 A4，生成页宽约为两倍；23 页对照不一定是 46 页。交替页输出才通常页数翻倍。
- 用本地 PDF 工具渲染抽查首页、图片/公式页、正文页和末页。机器翻译可能合并列表、收紧目录、出现术语错误；不要承诺逐句人工校译或像素级排版一致。
- 默认保留原图，**图片内部英文不一定翻译**，交付时明确这一点。
- 用 `browser.preview` 展示并给出对照 PDF 链接、页数和已核验范围；记录来源 key/哈希、引擎版本、输出哈希、原配置是否未变。
- 除非用户要求且项目规则允许，**不自动附回 Zotero**。需要附回时发现 MCP 工具，查重、使用主条目 key 附加，并再次确认；独立 PDF 不是可直接接收子附件的主条目，不擅自整理库。

只创建/更新 skill 时不执行新的翻译任务、不发送测试翻译 API 请求。

## 维护与测试

用引擎的 Python 环境运行 `python -m unittest discover -s <skill-dir>/tests -v`。测试使用模拟引擎和临时 PDF，验证仅对照输出、原文件/原配置不变、页码隔离、密钥脱敏及不覆盖目录，不调用真实翻译 API；未安装 PyMuPDF 时模拟 PDF 集成测试会明确跳过。
