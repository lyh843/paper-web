"""Build the manually refactored readings; never generate paper prose or semantic grades.

review-notes.json contains paper-specific manual review locations. Automated checks
only validate source identity, Markdown structure, rendering, resources and hashes.
Browser delivery findings are supplied separately; render success is not completion.
"""

import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import subprocess


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SKILL = ROOT.parent / ".opencode/skills/paper-reading"
REVISION = "narrative-logic-v1"
DAY = "2026-10-19"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def quality_text(note, browser):
    gates = [
        ("问题、价值与前作缺口", note["problem"] + "；" + note["prior_gap"]),
        ("非循环思路重建", note["idea"]),
        ("核心直觉", note["intuition"]),
        ("贯穿实例与方法", note["example"]),
        ("数学可理解性与忠实度", note["math"]),
        ("实验问答与主张边界", note["evidence"]),
        ("有依据的Takeaways", note["takeaways"]),
    ]
    text = [
        f'# 新版质量记录 · {note["title"]}',
        "",
        f"日期：{DAY}。使用当前 `{REVISION}`，保留发表时背景扩展。旧记录与旧HTML、源文件、图像均归档于 `revisions/pre-narrative-logic-20261019/`。",
        "",
        "本记录区分人工语义自查、原有证据审计的保留，以及自动构建/浏览器检查。没有进行独立读者研究，也没有重新训练模型或复现论文实验。",
        "",
        "## 本轮人工正文逻辑自查",
        "",
        "| 检查 | 状态 | 具体位置与核验内容 |",
        "|---|---|---|",
    ]
    text += [f"| {gate} | pass（生成者自查） | {location} |" for gate, location in gates]
    text += [
        "",
        "以上位置逐项回答当前skill的八问；问题与前作缺口合在第一个背景章。忽略图示后，正文、公式与普通表格仍能连起问题、假设、实际方法和证据；检查标题存在本身不算语义通过。",
        "",
        "## 来源覆盖与保留审计",
        "",
        "- 已核对本地PDF指纹与原始provenance一致，全文可访问，未修改Zotero。",
        "- 本轮重新核对的主干及相关附录页：" + "、".join(map(str, note["source_pages_rechecked"])) + "。",
        "- 原有公式、图表数值、图前提示、版本差异和证据限定保留，并沿用归档中已完成的相应来源审计；不把文本抽取全部页面说成全部页面本轮逐字重读。",
        "- 理论/方法/评测类型分别适配；教学推导、构造实例、作者原图示例和真实任务流程在正文明确区分。",
        "",
        "## 特别边界",
        "",
    ]
    text += ["- " + caution for caution in note["cautions"]]
    text += [
        "",
        "## 自动结构与交付检查",
        "",
        "- 背景结构检查：pass；年代与前作关系为人工来源核验，不由检查器证明。",
        "- 严格HTML/KaTeX渲染：pass；所有引用资源从同目录嵌入，没有修改skill渲染器。",
        "- 交互选择沿用本篇已有静态可视化审计，未为凑数量添加互动；核心内容无需脚本。",
    ]
    if browser:
        text += [
            "- 浏览器检查：" + ("pass" if browser["ok"] else "fail") + "；" + json.dumps(browser, ensure_ascii=False) + "。",
            "- 窄屏通过同页面390px iframe验证，不冒充物理手机测试。来源显示开/关两种模式均检查页面级溢出，宽表/公式应局部滚动。",
        ]
    else:
        text += ["- 浏览器检查：unknown / 等待本轮检查；渲染成功尚不等于完成交付。"]
    text += [
        "",
        "## 尚未执行的验证",
        "",
        "- 独立读者理解测试：unknown / 未执行。",
        "- 模型训练、科学实验复现、完整预训练语料重新去重：unknown / 未执行。",
        "- 原文未披露的内部算法仍标未知，不以通用经验补成作者步骤。",
        "",
    ]
    return "\n".join(text)


def build(directory, note, browser):
    folder = ROOT / directory
    old_path = folder / "revisions/pre-narrative-logic-20261019/provenance.json"
    old = json.loads(old_path.read_text())
    pdf = Path(old["source_pdf_path"])
    assert sha(pdf) == old["source_pdf_sha256"], f"Source changed: {directory}"
    source = folder / "reading.md"
    markdown = source.read_text()
    assert "教学" in markdown and "### 研究问题与价值" in markdown
    subprocess.run(["node", str(SKILL / "scripts/check-background.cjs"), str(source)], check=True)
    subprocess.run(["node", str(SKILL / "scripts/render-reading.cjs"), str(source), str(folder / "index.html")], check=True)
    html = (folder / "index.html").read_text()
    assert '<html lang="zh-CN">' in html
    assert not re.search(r'<(?:script|iframe)\b', html)
    assert not re.search(r'<img\b[^>]*src=["\'](?!data:)', html)
    assert "katex-error" not in html
    assert all((folder / path).is_file() for path in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', markdown))
    browser_result = browser.get(directory)
    (folder / "quality-check.md").write_text(quality_text(note, browser_result))
    current = dict(old)
    current.update({
        "generated_on": DAY,
        "skill_revision": REVISION,
        "preserved_skill_extensions": ["historical-context-v1"],
        "skill_definition_sha256": sha(SKILL / "SKILL.md"),
        "narrative_protocol_sha256": sha(SKILL / "references/narrative-logic.md"),
        "renderer_sha256": sha(SKILL / "scripts/render-reading.cjs"),
        "audit_source_sha256": sha(source),
        "html_sha256": sha(folder / "index.html"),
        "quality_check_sha256": sha(folder / "quality-check.md"),
        "manual_narrative_review": note,
        "manual_review_type": "Generator source-based semantic self-check; not independent reader study",
        "source_pages_rechecked_this_revision": note["source_pages_rechecked"],
        "reused_source_audit": "Unchanged PDF and existing equation/figure/number source audits retained from archived reading; full text accessible, not claimed to have independently rerun experiments or read every appendix table anew",
        "delivery_status": "completed" if browser_result and browser_result["ok"] else "rendered_awaiting_browser",
        "browser_validation_this_revision": browser_result,
        "validation_scope": "Manual narrative and source review plus renderer/browser checks; no independent reader study or scientific reproduction",
    })
    history = list(old.get("local_revisions", []))
    history.append({
        "revision": REVISION,
        "date": DAY,
        "action": "Paper-specific prose refactor: problem/value, prior-only idea reconstruction, intuition, running instance, accessible mathematics, question/test/answer evidence and takeaways; preserve original evidence and visuals",
        "archive_directory": "revisions/pre-narrative-logic-20261019",
        "before": {"audit_source_sha256": old["audit_source_sha256"], "html_sha256": old["html_sha256"]},
    })
    current["local_revisions"] = history
    write_json(folder / "provenance.json", current)
    return {
        "item_key": old["zotero_item_key"], "title": note["title"],
        "directory": directory, "html": f"{directory}/index.html",
        "action": "refactored", "status": current["delivery_status"],
        "language": "zh-CN", "skill_revision": REVISION,
        "source_characters": len(markdown), "sections": len(re.findall(r'^## ', markdown, re.M)),
        "original_figures": len(re.findall(r'!\[', markdown)),
        "pdf_sha256_verified": True, "background_structure": "pass",
        "manual_narrative_review": "pass; self-check only",
        "browser": browser_result,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", action="append")
    args = parser.parse_args()
    notes = json.loads((HERE / "review-notes.json").read_text())
    browser_file = HERE / "browser-results.json"
    browser = json.loads(browser_file.read_text()) if browser_file.exists() else {}
    report_file = ROOT / "narrative-upgrade.json"
    report = json.loads(report_file.read_text()) if report_file.exists() else {
        "date": DAY, "collection": "人工智能/TabFM", "collection_key": "FLT4H9RN",
        "scope": "13 existing direct readings; no new papers or child collections; 12 refactors and 1 current-reading retention",
        "enumerated_items": 13, "enumeration_complete": True, "unique_pdf_fingerprints": 13,
        "skill_revision": REVISION, "independent_reader_study": "not performed", "experiments_rerun": False,
        "items": [],
    }
    by_directory = {entry["directory"]: entry for entry in report["items"]}
    for directory in args.paper or notes:
        by_directory[directory] = build(directory, notes[directory], browser)
    retained = "retrieval-finetuning-5QV5CK9L"
    p = json.loads((ROOT / retained / "provenance.json").read_text())
    assert p["skill_revision"] == REVISION and sha(ROOT / retained / "reading.md") == p["audit_source_sha256"]
    assert sha(ROOT / retained / "index.html") == p["html_sha256"]
    by_directory[retained] = {
        "item_key": "5QV5CK9L", "title": "Retrieval & Fine-Tuning for In-Context Tabular Models",
        "directory": retained, "html": retained + "/index.html", "action": "retained_current",
        "status": "completed", "skill_revision": REVISION,
        "reason": "Already rebuilt on 2026-10-18 with the current skill; hashes unchanged",
        "browser": browser.get(retained),
    }
    report["items"] = [by_directory[key] for key in sorted(by_directory)]
    report["refactored_rendered"] = sum(x["action"] == "refactored" for x in report["items"])
    report["completed"] = sum(x["status"] == "completed" for x in report["items"])
    report["awaiting_browser"] = sum(x["status"] == "rendered_awaiting_browser" for x in report["items"])
    report["failed_items"] = []
    report["pending_directories"] = sorted(set(notes) - set(by_directory))
    write_json(report_file, report)
    print(f"Batch state: {report['refactored_rendered']} refactored, {report['completed']} completed, {report['awaiting_browser']} awaiting browser")


if __name__ == "__main__":
    main()
