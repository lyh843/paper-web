const test = require('node:test');
const assert = require('node:assert/strict');
const { checkBackground } = require('./check-background.cjs');

function sample(language = 'zh-CN') {
  const headings = language === 'en'
    ? ['Time boundary and field state', 'Prior work and remaining gaps', 'Why this paper now']
    : ['当时的领域状态', '关键前作与尚存缺口', '本文为何在此时提出'];
  return `<!-- paper-reading-lang: ${language} -->
# Reading

<!-- paper-reading-context:start -->
## 00 / Context
<!-- context-cutoff: 2022-07-05; basis: first-publication -->

### ${headings[0]}
${'Substantive source-grounded explanation of the historical field state. '.repeat(3)}

### ${headings[1]}
| Work | Contribution | Gap | Source |
|---|---|---|---|
| A (2018) | Specific mechanism | Remaining problem | PDF §2 |
| B (2020) | Specific mechanism | Remaining problem | https://arxiv.org/abs/example |
| C (2021) | Specific mechanism | Remaining problem | PDF pp. 2–3 |

### ${headings[2]}
${'Explain how the remaining bottleneck motivated this specific paper without hindsight. '.repeat(3)}
<!-- paper-reading-context:end -->

## 01 / Method
Mechanism.
`;
}

test('background checker accepts complete Chinese and English background structure', () => {
  for (const lang of ['zh-CN', 'en']) assert.equal(checkBackground(sample(lang)).ok, true);
});

test('background checker rejects missing and duplicate markers', () => {
  assert.equal(checkBackground('# Paper\n## Method').ok, false);
  assert.equal(checkBackground(sample() + '<!-- paper-reading-context:start -->').ok, false);
});

test('background checker rejects reversed markers and a background placed after methods', () => {
  assert.equal(checkBackground(sample().replace('<!-- paper-reading-context:start -->', '<!-- paper-reading-context:end -->')
    .replace('<!-- paper-reading-context:end -->\n\n## 01', '<!-- paper-reading-context:start -->\n\n## 01')).ok, false);
  assert.equal(checkBackground(sample().replace('<!-- paper-reading-context:start -->', '## Earlier method\n<!-- paper-reading-context:start -->')).ok, false);
});

test('background checker requires the historical cutoff and explanatory subsections', () => {
  assert.equal(checkBackground(sample().replace(/<!-- context-cutoff:.*-->/, '')).ok, false);
  assert.equal(checkBackground(sample().replace('### 本文为何在此时提出', '### Miscellaneous')).ok, false);
});

test('background checker rejects a bibliography-only or generic one-line rationale', () => {
  assert.equal(checkBackground(sample().replace(/Explain how[^\n]+/, 'Important topic.')).ok, false);
});

test('background checker requires actual contribution/gap/source cells', () => {
  assert.equal(checkBackground(sample().replace('| Specific mechanism | Remaining problem | PDF §2 |', '| | Remaining problem | PDF §2 |')).ok, false);
  assert.equal(checkBackground(sample().replace('https://arxiv.org/abs/example', 'trust me')).ok, false);
});

test('background checker permits fewer predecessors only with a substantive exception', () => {
  const fewer = sample().replace('| C (2021) | Specific mechanism | Remaining problem | PDF pp. 2–3 |\n', '');
  assert.equal(checkBackground(fewer).ok, false);
  assert.equal(checkBackground(fewer.replace('<!-- paper-reading-context:end -->',
    '<!-- context-related-work-exception: This narrowly scoped topic has only two source-verified directly relevant predecessors. -->\n<!-- paper-reading-context:end -->')).ok, true);
});

test('background structure checker does not claim to verify chronological truth', () => {
  const result = checkBackground(sample().replace('A (2018)', 'A (2099)'));
  assert.equal(result.ok, true);
  // Deliberately documents the limit: historical date and priority review is manual.
});
