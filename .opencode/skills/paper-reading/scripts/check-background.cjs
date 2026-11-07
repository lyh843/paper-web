const fs = require('node:fs');

const START = '<!-- paper-reading-context:start -->';
const END = '<!-- paper-reading-context:end -->';

function checkBackground(markdown) {
  const errors = [];
  const occurrences = (token) => markdown.split(token).length - 1;
  if (occurrences(START) !== 1 || occurrences(END) !== 1) {
    return { ok: false, errors: ['Include exactly one publication-time context start/end marker pair.'] };
  }
  const start = markdown.indexOf(START);
  const end = markdown.indexOf(END);
  if (end <= start) return { ok: false, errors: ['Context end marker must follow its start marker.'] };
  const body = markdown.slice(start + START.length, end);
  const firstChapter = markdown.match(/^##\s+.+$/m);
  const contextChapter = body.match(/^##\s+.+$/m);
  if (!contextChapter || !firstChapter || firstChapter.index < start ||
      firstChapter.index >= end || (body.match(/^##\s+.+$/gm) || []).length !== 1) {
    errors.push('Make context exactly one visible first ## body chapter, before the method.');
  }
  const cutoff = body.match(/<!--\s*context-cutoff:\s*(\d{4}(?:-\d{2})?(?:-\d{2})?)(?:\s*;[^>]*?)?\s*-->/);
  if (!cutoff) errors.push('Record a verified context-cutoff audit comment inside the background.');
  const english = /^<!-- paper-reading-lang: en -->/.test(markdown);
  const headings = english
    ? ['Time boundary and field state', 'Prior work and remaining gaps', 'Why this paper now']
    : ['当时的领域状态', '关键前作与尚存缺口', '本文为何在此时提出'];
  const positions = headings.map((heading) => body.indexOf(`### ${heading}`));
  if (positions.some((p) => p < 0) || !(positions[0] < positions[1] && positions[1] < positions[2])) {
    errors.push(`Include these explanatory subsections in order: ${headings.join(' / ')}.`);
  } else {
    for (const i of [0, 2]) {
      const text = body.slice(positions[i] + headings[i].length + 4, i === 0 ? positions[1] : body.length)
        .replace(/<!--[\s\S]*?-->/g, '').trim();
      if (text.length < 100) errors.push(`Explain ${headings[i]} in prose; a title or source pointer alone is insufficient.`);
    }
    const prior = body.slice(positions[1], positions[2]);
    const rows = prior.split('\n').filter((line) => /^\s*\|.*\|\s*$/.test(line));
    const cells = rows.map((line) => line.trim().slice(1, -1).split(/(?<!\\)\|/).map((s) => s.trim()));
    const separator = cells.findIndex((row) => row.length >= 4 && row.every((c) => /^:?-{3,}:?$/.test(c)));
    const data = separator >= 1 ? cells.slice(separator + 1) : [];
    const exception = body.match(/<!--\s*context-related-work-exception:\s*([^>]+?)\s*-->/);
    if (data.length < 3 && (!exception || exception[1].trim().length < 20)) {
      errors.push('Provide at least three contribution/gap/source rows, or explain a genuine narrow-literature exception.');
    }
    for (const [i, row] of data.entries()) {
      if (row.length < 4 || row.some((c) => !c)) errors.push(`Prior-work row ${i + 1} needs non-empty work, contribution, remaining gap, and source cells.`);
      if (!/PDF|https?:\/\/|arXiv|DOI|§/i.test(row.at(-1) || '')) errors.push(`Prior-work row ${i + 1} lacks an identifiable source pointer.`);
    }
  }
  return { ok: errors.length === 0, cutoff: cutoff?.[1] || null, errors };
}

if (require.main === module) {
  const files = process.argv.slice(2);
  if (!files.length) {
    console.error('Usage: node check-background.cjs <reading.md> [more-readings.md ...]');
    process.exitCode = 1;
  }
  for (const file of files) {
    try {
      const result = checkBackground(fs.readFileSync(file, 'utf8'));
      if (!result.ok) {
        process.exitCode = 1;
        console.error(`${file}: background structure failed\n${result.errors.map((e) => `- ${e}`).join('\n')}`);
      } else {
        console.log(`${file}: background structure present (cutoff ${result.cutoff}); chronology and content still require source review.`);
      }
    } catch (error) {
      process.exitCode = 1;
      console.error(`${file}: ${error.message}`);
    }
  }
}

module.exports = { checkBackground };
