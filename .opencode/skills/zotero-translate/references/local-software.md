# 本机软件发现与版本适配

## 从注册项追踪真实程序

优先使用文件工具读取以下相关目录，不要仅依赖 `which zotero-pdf`：

1. `command -v zotero`、`command -v pdf2zh_next`、`command -v pdf2zh`。
2. `~/.local/share/applications/` 和 `/usr/share/applications/` 中名称/内容含 `zotero`、`pdf2zh` 的 `.desktop` 文件。
3. 读取匹配桌面项的 `Exec`，**先检查脚本内容再执行**，不要把桌面项任意参数当作安全命令直接 shell-eval。
4. 若是启动器，读取它指向的 systemd user service 或软件目录，确认实际引擎、配置和端口。
5. 引擎不在 PATH 时，检查启动器明确引用的 conda/venv；不要无边界扫描主目录。

本机案例：`Zotero PDF2zh` 桌面项启动 `launch-zotero-pdf2zh`；脚本启动用户服务，再打开 Chromium app 页面。该网页是监控界面；软件源码显示 `/translate` 才是翻译接口，**不是所有此类软件都使用这个路由**。

## CLI 优先

已安装 PDF2zh-next 2.9.0 在本机提供：

```text
pdf2zh_next <input.pdf> --config-file <temporary-config.toml>
  --openaicompatible --lang-in en --lang-out zh-CN
  --output <new-directory> --no-mono --watermark-output-mode no_watermark
```

仅当用户已配置 `openaicompatible` 时使用该选择器；其他服务应使用实际选中的 flag。不要硬编码模型名/API 地址/密钥；本 skill 脚本从现有配置读取选择。

本机测试时，`no_mono=true` 表示只生成对照版；左右对照需要 `use_alternating_pages_dual=false`。源配置可能含 `no_dual=true`，必须在临时副本明确设为 `false`，否则会禁掉需要的输出。

全篇翻译时应清除临时副本中旧的 `pdf.pages`、`translation.only_include_translated_page` 或 `pdf.only_include_translated_page` 限制；不得因上次选择页码而只翻译本篇一部分。不要改用户原配置。

辅助脚本支持已安装版本的 TOML 结构；若新版本将字段移动或改名，检查 `--help` 和对应配置模型再适配，不能悄悄猜测。

## 必须改用本地服务时

先确认服务已经运行；未运行且确实需要时可启动已发现的 `systemctl --user start zotero-pdf2zh.service`。不要更改 autostart、软件源码、原有模型配置或默认监听范围。

本机 4.1.x 服务的已读实现：

- `GET /health`：健康检查。
- `POST /translate`：JSON 请求包含 `fileName`、base64 `fileContent` 和配置。
- `asyncJob=true`：接受任务后返回 `taskId`，后续查询/通知方式必须根据当前实现确认。
- `GET /api/tasks` / `GET /api/history`：进度和历史。
- `GET /translatedFile/<filename>`：输出下载。

**服务的 `Config.update_config_file()` 会写回配置**，因此本 skill 优先使用 CLI + 临时配置。不满足“不改原配置”时不要默认改走服务。

## 失败处理

- 没有相关桌面项和 CLI：说明实际检查过的范围，再请用户提供软件名称或安装路径。
- 输入文件不明确：查 Zotero 附件或向用户澄清，不挑任意 PDF。
- API 鉴权/余额错误：停止本次任务，不换服务、不充值，不打印令牌。
- 引擎安装缺包：先报告，取得用户同意后修复独立环境，不自动更新整个软件。
- 超时：终止本次创建的进程组，记录 failed；重试前检查残留输出与缓存，避免重复收费。
- 译文已生成但检查未完成：报告 generated/unverified，不冒充 checked/verified。

## 最小本机测试（无翻译 API）

脚本单元测试只验证临时配置、默认仅对照、页码、密钥不进入命令行等逻辑；不调用翻译 API。真实质量验收只在用户请求的翻译任务上执行。
