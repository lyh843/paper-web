# TabFM · 当前skill正文逻辑重构报告

日期：2026-10-19。范围：Zotero 人工智能 / TabFM（FLT4H9RN）的13篇现有直接条目解读，不新增其他论文或子分类。

## 结果

- **成功重构：12篇**。逐篇补强问题与价值、前作缺口、非循环思路重建、核心直觉、贯穿实例、数学解释、实验问答和Takeaways；保留原有证据、原图及版本限定。
- **保留当前新版：1篇**，LoCalPFN已在2026-10-18按相同skill重写，本轮指纹不变并重新检查浏览器交付。
- **失败：0篇；未完成：0篇；新增论文：0篇**。
- 13份本地PDF指纹均与原provenance一致，无重复；独立PDF VHVYYSMP已通过Zotero元数据确认无父条目。Zotero未修改。

## 文件与逐篇状态

| 论文 | 本轮动作 | 新版HTML | 质量记录 | 旧版备份 |
|---|---|---|---|---|
| Transformers Can Do Bayesian Inference | 重构完成 | [打开](pfn-bayesian-inference-VHVYYSMP/index.html) | [审计](pfn-bayesian-inference-VHVYYSMP/quality-check.md) | [旧版](pfn-bayesian-inference-VHVYYSMP/revisions/pre-narrative-logic-20261019/index.html) |
| Why do tree-based models still outperform deep learning on tabular data? | 重构完成 | [打开](trees-vs-deep-learning-BKDZDVHC/index.html) | [审计](trees-vs-deep-learning-BKDZDVHC/quality-check.md) | [旧版](trees-vs-deep-learning-BKDZDVHC/revisions/pre-narrative-logic-20261019/index.html) |
| TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second | 重构完成 | [打开](tabpfn-CL7A9HMJ/index.html) | [审计](tabpfn-CL7A9HMJ/quality-check.md) | [旧版](tabpfn-CL7A9HMJ/revisions/pre-narrative-logic-20261019/index.html) |
| Retrieval & Fine-Tuning for In-Context Tabular Models | 当前新版保留 | [打开](retrieval-finetuning-5QV5CK9L/index.html) | [审计](retrieval-finetuning-5QV5CK9L/quality-check.md) | [旧版](retrieval-finetuning-5QV5CK9L/revisions/pre-narrative-logic-20261018/index.html) |
| Accurate predictions on small data with a tabular foundation model | 重构完成 | [打开](tabpfn-v2-KGSUGZNB/index.html) | [审计](tabpfn-v2-KGSUGZNB/quality-check.md) | [旧版](tabpfn-v2-KGSUGZNB/revisions/pre-narrative-logic-20261019/index.html) |
| TabICL: A Tabular Foundation Model for In-Context Learning on Large Data | 重构完成 | [打开](tabicl-XKRXCPY2/index.html) | [审计](tabicl-XKRXCPY2/quality-check.md) | [旧版](tabicl-XKRXCPY2/revisions/pre-narrative-logic-20261019/index.html) |
| TabPFN-2.5: Advancing the State of the Art in Tabular Foundation Models | 重构完成 | [打开](tabpfn-2-5-SA9FC8Q4/index.html) | [审计](tabpfn-2-5-SA9FC8Q4/quality-check.md) | [旧版](tabpfn-2-5-SA9FC8Q4/revisions/pre-narrative-logic-20261019/index.html) |
| TabDPT: Scaling Tabular Foundation Models on Real Data | 重构完成 | [打开](tabdpt-V7LZ2JEQ/index.html) | [审计](tabdpt-V7LZ2JEQ/quality-check.md) | [旧版](tabdpt-V7LZ2JEQ/revisions/pre-narrative-logic-20261019/index.html) |
| TabArena: A Living Benchmark for Machine Learning on Tabular Data | 重构完成 | [打开](tabarena-SAZSYEMX/index.html) | [审计](tabarena-SAZSYEMX/quality-check.md) | [旧版](tabarena-SAZSYEMX/revisions/pre-narrative-logic-20261019/index.html) |
| TabPFN-3: Technical Report | 重构完成 | [打开](tabpfn-3-4ZXDEDKZ/index.html) | [审计](tabpfn-3-4ZXDEDKZ/quality-check.md) | [旧版](tabpfn-3-4ZXDEDKZ/revisions/pre-narrative-logic-20261019/index.html) |
| TabICLv2: A Better, Faster, Scalable, and Open Tabular Foundation Model | 重构完成 | [打开](tabicl-v2-2PKI4VVL/index.html) | [审计](tabicl-v2-2PKI4VVL/quality-check.md) | [旧版](tabicl-v2-2PKI4VVL/revisions/pre-narrative-logic-20261019/index.html) |
| TabDPT-Turbo: Efficient In-Context Learning for Tabular Prediction | 重构完成 | [打开](tabdpt-turbo-DFAGC498/index.html) | [审计](tabdpt-turbo-DFAGC498/quality-check.md) | [旧版](tabdpt-turbo-DFAGC498/revisions/pre-narrative-logic-20261019/index.html) |
| TabFM: A Zero-Shot Foundation Model for Tabular Data | 重构完成 | [打开](tabfm-zero-shot-KZJI8QQR/index.html) | [审计](tabfm-zero-shot-KZJI8QQR/quality-check.md) | [旧版](tabfm-zero-shot-KZJI8QQR/revisions/pre-narrative-logic-20261019/index.html) |

## 检查结果与可解释范围

- 12篇新构建在渲染前均通过背景结构检查，KaTeX严格解析成功；13篇均为离线自包含HTML，无外部呈现资源、无页面脚本。
- 浏览器逐篇检查1280px与390px，共26次布局检查；59张原图成功解码，274处数学表达式无错误。导航、图前提示/图注及来源开关通过，默认与显示来源两种模式均无页面级横向溢出。
- 窄屏使用同页面iframe，不冒称真实手机测试；技术检查不能证明读者已经理解论文。
- skill现有29项回归测试全部通过；skill本身和渲染器没有被本轮改动。
- 正文逻辑是逐篇生成者语义自查，并有具体段落记录，不是检测到标题就自动判通过，也不是独立读者研究。

## 来源纪律与未执行事项

本轮重新核对各篇核心原文及相关附录，保留已有公式、图表数字与来源审计；每篇provenance明确列出本轮重新核对的页码和继承的证据记录。全文均可访问，但不把批量文本提取全部页面宣称成数百页附录在本轮逐字重读。

- 作者图中示例、真实数据任务、可手算教学特例与构造配置逐篇标注。未运行模型时不编造内部激活、概率、延迟或预测结果。
- 原文没有理论保证时明确说明；标准数学补充与作者证明分开。专有蒸馏、Thinking、完整生成器等未披露细节仍标未知。
- **没有重新训练模型、复现科学实验、重跑全部预训练语料去重或执行独立读者理解测试**。

## 备份与重建

12篇旧HTML、reading.md、provenance、质量记录和assets均在各篇 `revisions/pre-narrative-logic-20261019/`。目录页和旧批次状态归档在 `batch-history/narrative-logic-20261019/`。LoCalPFN已有20261018备份继续保留。

本轮手工审查位置与构建程序：`batch-history/narrative-logic-20261019/review-notes.json`、`rebuild.py`。程序只构建手工改写的正文和审计文件，不批量套模板生成论文解释，也不自动验证科学真伪。
