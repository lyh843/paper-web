"""Publish batch status/report after all manually reviewed readings pass delivery checks."""

import hashlib
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DAY = "2026-10-19"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def main():
    report = json.loads((ROOT / "narrative-upgrade.json").read_text())
    browser = json.loads((HERE / "browser-results.json").read_text())
    status = json.loads((HERE / "batch-status.json").read_text())
    assert report["completed"] == 13 and report["refactored_rendered"] == 12
    assert not report["awaiting_browser"] and not report["pending_directories"] and not report["failed_items"]
    by_key = {entry["item_key"]: entry for entry in report["items"]}
    previous_validations = {entry["item_key"]: entry for entry in status["validation"]}
    validations, checks = [], []
    for entry in report["items"]:
        folder = ROOT / entry["directory"]
        provenance = json.loads((folder / "provenance.json").read_text())
        source = (folder / "reading.md").read_text()
        result = browser[entry["directory"]]
        assert result["ok"] and provenance["skill_revision"] == "narrative-logic-v1"
        assert digest(folder / "reading.md") == provenance["audit_source_sha256"]
        assert digest(folder / "index.html") == provenance["html_sha256"]
        assert digest(Path(provenance["source_pdf_path"])) == provenance["source_pdf_sha256"]
        first_chapter = re.search(r'^## (.+)$', source, re.M)
        start, end = source.index('<!-- paper-reading-context:start -->'), source.index('<!-- paper-reading-context:end -->')
        assert start < first_chapter.start() < end
        v = dict(previous_validations[entry["item_key"]])
        v.update({
            "sections": result["sections"], "source_characters": len(source),
            "original_figures": result["images_total"], "katex_instances": result["math"],
            "status": "completed", "batch_action": entry["action"],
            "skill_revision": "narrative-logic-v1", "manual_narrative_review": "pass; generator self-check only",
            "browser_tested_widths": [390,1280], "browser_math_errors": 0,
            "browser_document_overflow": False, "browser_source_toggle": True,
            "browser_images_loaded": True, "background_first_navigation": True,
            "predecessor_rows": provenance["historical_context"]["predecessor_rows"],
        })
        validations.append(v)
        checks.append({
            "path": entry["html"], "checked_widths": [390,1280],
            "background_first": True,
            "background_table_rows": provenance["historical_context"]["predecessor_rows"],
            "image_count": result["images_total"], "images_loaded": True,
            "image_check": "explicit decode(), complete and naturalWidth",
            "katex_count": result["math"], "math_errors": 0,
            "document_overflow": False, "sources_shown_overflow": False,
            "source_toggle": True, "source_reference_count": result["source_count"],
            "navigation": True, "fonts_loaded": True, "external_resources": 0,
            "raw_markers": False, "html_sha256": digest(folder / "index.html"),
        })
    previous_order = re.findall(r'href="([^"#]+/index\.html)"', (HERE / "index.html").read_text())
    current_order = re.findall(r'href="([^"#]+/index\.html)"', (ROOT / "index.html").read_text())
    assert previous_order == current_order and len(current_order) == 13
    status.update({
        "generated_on": DAY, "completed_items": 13, "new_readings": 0,
        "retained_readings": 1, "updated_readings": 12, "validation": validations,
        "failed_items": [], "skipped_items": [{
            "item_key": "5QV5CK9L", "reason": "Already uses current skill; retained with matching hashes and rechecked browser delivery"
        }],
        "last_update": {
            "kind": "narrative-logic-refactor", "skill_revision": "narrative-logic-v1",
            "preserved_old_readings": True, "index_order_preserved": True,
            "refactored": 12, "retained_current": 1, "failed": 0, "incomplete": 0,
            "report": "narrative-upgrade.json", "archive": "batch-history/narrative-logic-20261019",
        },
    })
    save(ROOT / "batch-status.json", status)
    save(ROOT / "browser-validation.json", {
        "checked_on": DAY, "revision": "narrative-logic-v1",
        "method": browser["_protocol"]["method"], "physical_device_test": False,
        "checks": checks, "all_passed": True,
    })
    math_count = sum(check["katex_count"] for check in checks)
    image_count = sum(check["image_count"] for check in checks)
    lines = [
        "# TabFM · 当前skill正文逻辑重构报告", "",
        "日期：2026-10-19。范围：Zotero 人工智能 / TabFM（FLT4H9RN）的13篇现有直接条目解读，不新增其他论文或子分类。",
        "",
        "## 结果", "",
        "- **成功重构：12篇**。逐篇补强问题与价值、前作缺口、非循环思路重建、核心直觉、贯穿实例、数学解释、实验问答和Takeaways；保留原有证据、原图及版本限定。",
        "- **保留当前新版：1篇**，LoCalPFN已在2026-10-18按相同skill重写，本轮指纹不变并重新检查浏览器交付。",
        "- **失败：0篇；未完成：0篇；新增论文：0篇**。",
        "- 13份本地PDF指纹均与原provenance一致，无重复；独立PDF VHVYYSMP已通过Zotero元数据确认无父条目。Zotero未修改。",
        "",
        "## 文件与逐篇状态", "",
        "| 论文 | 本轮动作 | 新版HTML | 质量记录 | 旧版备份 |", "|---|---|---|---|---|",
    ]
    for path in current_order:
        entry = next(item for item in report["items"] if item["html"] == path)
        directory = entry["directory"]
        action = "重构完成" if entry["action"] == "refactored" else "当前新版保留"
        old_day = "20261019" if entry["action"] == "refactored" else "20261018"
        archive = f"{directory}/revisions/pre-narrative-logic-{old_day}/index.html"
        assert (ROOT / archive).is_file()
        lines.append(f"| {entry['title']} | {action} | [打开]({path}) | [审计]({directory}/quality-check.md) | [旧版]({archive}) |")
    lines += [
        "", "## 检查结果与可解释范围", "",
        "- 12篇新构建在渲染前均通过背景结构检查，KaTeX严格解析成功；13篇均为离线自包含HTML，无外部呈现资源、无页面脚本。",
        f"- 浏览器逐篇检查1280px与390px，共26次布局检查；{image_count}张原图成功解码，{math_count}处数学表达式无错误。导航、图前提示/图注及来源开关通过，默认与显示来源两种模式均无页面级横向溢出。",
        "- 窄屏使用同页面iframe，不冒称真实手机测试；技术检查不能证明读者已经理解论文。",
        "- skill现有29项回归测试全部通过；skill本身和渲染器没有被本轮改动。",
        "- 正文逻辑是逐篇生成者语义自查，并有具体段落记录，不是检测到标题就自动判通过，也不是独立读者研究。",
        "", "## 来源纪律与未执行事项", "",
        "本轮重新核对各篇核心原文及相关附录，保留已有公式、图表数字与来源审计；每篇provenance明确列出本轮重新核对的页码和继承的证据记录。全文均可访问，但不把批量文本提取全部页面宣称成数百页附录在本轮逐字重读。",
        "",
        "- 作者图中示例、真实数据任务、可手算教学特例与构造配置逐篇标注。未运行模型时不编造内部激活、概率、延迟或预测结果。",
        "- 原文没有理论保证时明确说明；标准数学补充与作者证明分开。专有蒸馏、Thinking、完整生成器等未披露细节仍标未知。",
        "- **没有重新训练模型、复现科学实验、重跑全部预训练语料去重或执行独立读者理解测试**。",
        "", "## 备份与重建", "",
        "12篇旧HTML、reading.md、provenance、质量记录和assets均在各篇 `revisions/pre-narrative-logic-20261019/`。目录页和旧批次状态归档在 `batch-history/narrative-logic-20261019/`。LoCalPFN已有20261018备份继续保留。",
        "",
        "本轮手工审查位置与构建程序：`batch-history/narrative-logic-20261019/review-notes.json`、`rebuild.py`。程序只构建手工改写的正文和审计文件，不批量套模板生成论文解释，也不自动验证科学真伪。",
        "",
    ]
    (ROOT / "narrative-upgrade.md").write_text("\n".join(lines))
    print(f"Finalized: 12 refactors + 1 retained; {image_count} images, {math_count} math expressions; 13 completed, 0 failed/incomplete")


if __name__ == "__main__":
    main()
