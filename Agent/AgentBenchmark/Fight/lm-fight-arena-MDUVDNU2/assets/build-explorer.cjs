const fs = require('node:fs');
const path = require('node:path');
const data = JSON.parse(fs.readFileSync(path.join(__dirname, 'evidence.json'), 'utf8'));
const esc = x => String(x).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const names = Object.fromEntries(data.models.map(m => [m.id,m.name]));
if(data.matches.length !== 15) throw Error('Expected 15 unique matches');
const pairs = new Set();
for(const g of data.matches){
  const pair=[g.winner,g.loser].sort().join('|');
  if(pairs.has(pair) || !names[g.winner] || !names[g.loser] || g.health<0 || g.health>1) throw Error('Invalid match');
  pairs.add(pair);
}
for(const m of data.models){
  if(data.matches.filter(g=>g.winner===m.id).length !== m.wins) throw Error('Win count conflict');
}
const opts = data.models.map(m=>`<option value="${m.id}">${esc(m.name)}</option>`).join('');
const table=data.matches.map(g=>`<tr><td>${esc(names[g.winner])}</td><td>${esc(names[g.loser])}</td><td>${g.health.toFixed(3)} · ${(g.health*100).toFixed(1)}%</td></tr>`).join('');
const html=`<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>对局证据与闭环步骤探索</title><style>
:root{font-family:system-ui,-apple-system,"Noto Sans CJK SC",sans-serif;color:#172b42;background:#f5f8fc;line-height:1.7;color-scheme:light}*{box-sizing:border-box}body{margin:0;padding:24px}h1{font-size:25px;line-height:1.4;margin:0 0 10px}h2{font-size:20px;margin-top:26px}h3{font-size:18px;margin:0 0 12px}p{margin:9px 0}label{display:block;font-weight:650}select,button{font:inherit;color:inherit;border:1px solid #9db2cd;border-radius:8px;background:white;padding:9px 12px;max-width:100%}select{width:100%}button{cursor:pointer}button:focus-visible,select:focus-visible,summary:focus-visible{outline:3px solid #e19224;outline-offset:3px}.controls{display:grid;grid-template-columns:1fr 1fr;gap:16px}.card{background:white;border:1px solid #ccd9e7;padding:20px;border-radius:12px;margin-top:16px;overflow-wrap:anywhere}.badge{font-size:13px;border-radius:20px;background:#e4edfb;color:#234c8e;padding:4px 10px;display:inline-block}.metric{font-size:32px;line-height:1.3;font-weight:750;color:#1e578c}.track{height:18px;border-radius:9px;background:#e4ebf2;overflow:hidden}.fill{height:100%;background:#3479b1;transition:width .15s}.note{border-left:4px solid #d08a26;padding:8px 13px;background:#fff6e7}.muted{color:#52677e;font-size:14px}.stepnav{display:flex;gap:12px;align-items:center;flex-wrap:wrap}.stepnav select{flex:1;min-width:180px}.scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:14px}td,th{text-align:left;padding:9px;border-bottom:1px solid #dbe3ed;min-width:120px}th{background:#e8eff8}summary{cursor:pointer;font-weight:650}details{margin-top:18px}.split{display:grid;grid-template-columns:1fr 1fr;gap:16px}.split>div{border-top:1px solid #d9e3ef;padding-top:10px}#step-card{min-height:230px}noscript{display:block;padding:12px;background:#fff6e7}@media(max-width:560px){body{padding:14px}.controls,.split{grid-template-columns:1fr}h1{font-size:21px}.card{padding:15px}.metric{font-size:27px}}@media print{body{padding:0;background:white}button,select{display:none}.card{break-inside:avoid}.track{border:1px solid #999}details>div{display:block}details{display:block}}
</style></head><body>
<span class="badge">本文重绘 · 证据浏览，不是比赛模拟器</span><h1>把总胜率拆回一场比赛</h1><p>选择模型与对手：胜负回答“谁赢了”，剩余血量回答“这次赢得多险”。两者都不能单独解释原因。</p>
<div class="controls"><label for="model">观察模型<select id="model">${opts}</select></label><label for="opponent">它的对手<select id="opponent">${opts}</select></label></div>
<section class="card" id="match-card" aria-live="polite" aria-atomic="true"></section>
<p class="muted">每对只有 1 场；矩阵的对称格是同一场。条形表示胜者剩余血量占满血比例，绝不代表获胜概率。原始日志未取得。</p>
<details><summary>核验来源与图文冲突</summary><p>来源：arXiv:2510.08928v2，PDF p.4 Fig.3a，4 倍裁图逐行列视觉读取；胜场用 Fig.3b、§4 与 §6 交叉核验。图内红赢蓝输与图注绿赢红输冲突。本文视图不用原图颜色编码胜负，直接标明赢家。正文精细血量冲突在对应配对中保留。Claude+Gemini 按各自胜场为 9/15，§4.2 的 11/15 算术不一致。</p></details>
<h2>同一条构造动作怎样走过闭环</h2><p>选择步骤，跟踪“左侧我方、对手接近 → 假设选择 Left + A”。这不是已执行轨迹；未知的命中后果不会被补成演示结果。</p>
<div class="stepnav"><button id="prev" type="button" aria-label="上一步">← 上一步</button><label for="step" class="muted">流程步骤</label><select id="step">${data.steps.map((s,i)=>`<option value="${i}">${esc(s.title)}</option>`).join('')}</select><button id="next" type="button" aria-label="下一步">下一步 →</button></div>
<section class="card" id="step-card" aria-live="polite" aria-atomic="true"></section>
<details open><summary>全部十五场图读数</summary><div class="scroll"><table><thead><tr><th>胜者</th><th>败者</th><th>胜者剩余血量</th></tr></thead><tbody>${table}</tbody></table></div></details>
<noscript>脚本已关闭：可以阅读上方完整十五场数据表；所有方法步骤与未知项也在主文静态流程和段落中完整保留。</noscript>
<script>const data=${JSON.stringify(data).replace(/</g,'\\u003c')};
const byId=Object.fromEntries(data.models.map(m=>[m.id,m]));
const model=document.getElementById('model'),opponent=document.getElementById('opponent'),step=document.getElementById('step');
const esc=x=>String(x).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
model.value='q72';opponent.value='q32';
function draw(){
 const a=model.value,b=opponent.value,card=document.getElementById('match-card');
 if(a===b){card.innerHTML='<h3>没有同一模型的自对局数据</h3><p>原赛制只安排六个不同模型两两比赛。请选择另一个对手；不补造镜像自测结果。</p>';return;}
 const g=data.matches.find(g=>(g.winner===a&&g.loser===b)||(g.winner===b&&g.loser===a));
 const won=g.winner===a,m=byId[a],health=(g.health*100).toFixed(1);
 card.innerHTML='<span class="badge">Fig. 3a 图读数 · 单场</span><h3>'+esc(m.name)+'：'+(won?'本场获胜':'本场落败')+'</h3><p>胜者：<strong>'+esc(byId[g.winner].name)+'</strong>；败者：'+esc(byId[g.loser].name)+'</p><p class="metric">胜者剩余 '+health+'%</p><div class="track" role="img" aria-label="胜者剩余血量 '+health+'%，满血为100%"><div class="fill" style="width:'+health+'%"></div></div><div class="split"><div><strong>这场怎样计入胜率</strong><p>该模型五场中的 '+(won?'1 场胜利':'0 场胜利')+'；整次比赛共 '+m.wins+'/5 胜，即 '+(m.wins*20)+'%。</p></div><div><strong>这场不能回答什么</strong><p>不能把剩余血量当胜率，也不能仅凭一次结果判定视觉、推理或延迟是原因。</p></div></div><p class="note">'+esc(g.note)+'</p>';
}
function trace(){const s=data.steps[Number(step.value)];document.getElementById('step-card').innerHTML='<h3>'+esc(s.title)+'</h3><p><strong>原文已知操作：</strong>'+esc(s.known)+'</p><p><strong>同一实例：</strong>'+esc(s.example)+'</p><p class="note"><strong>不可补造：</strong>'+esc(s.missing)+'</p>';}
model.addEventListener('change',draw);opponent.addEventListener('change',draw);step.addEventListener('change',trace);
document.getElementById('prev').addEventListener('click',()=>{step.value=(Number(step.value)+data.steps.length-1)%data.steps.length;trace();});
document.getElementById('next').addEventListener('click',()=>{step.value=(Number(step.value)+1)%data.steps.length;trace();});
draw();trace();</script></body></html>`;
fs.writeFileSync(path.join(__dirname,'explorer.html'),html);
console.log('Validated 15 unique bouts, six win counts; built offline explorer.html');
