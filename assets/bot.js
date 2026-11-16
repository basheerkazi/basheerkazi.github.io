---
---
(function(){
var D={{ site.data.bot | jsonify }};
var C=JSON.parse(document.getElementById('bot-cfg').textContent);
var L=C.lang, A=D.answers[L]||D.answers.en;
var btn=document.querySelector('.bot-btn'), panel=document.getElementById('bot-panel');
var log=panel.querySelector('.bot-log'), chips=panel.querySelector('.bot-chips'), form=panel.querySelector('.bot-form'), inp=panel.querySelector('#bot-in');
var started=false;
function gc(p){try{if(window.goatcounter&&goatcounter.count)goatcounter.count({path:'bot-'+p,title:'Bot: '+p,event:true})}catch(e){}}
function today(){return new Date().toISOString().slice(0,10)}
function phase(){var t=today(),i=0;D.phase_starts.forEach(function(s){if(t>=s)i++});return A.phases[Math.min(i,A.phases.length-1)]}
function fill(s){return s.replace('{phase}',phase()).replace('{price}',today()<D.price_until?A.price:'').replace(/\{hd\}/g,C.hd).replace(/\{cd\}/g,C.cd).replace(/\{cc\}/g,C.cc).replace(/\{kit\}/g,C.kit)}
function add(html,who){var d=document.createElement('div');d.className='bot-msg '+(who||'bot');if(who==='me'){d.textContent=html}else{d.innerHTML=html}log.appendChild(d);log.scrollTop=log.scrollHeight;return d}
function waLink(q){var a=document.createElement('a');a.className='btn wa';a.target='_blank';a.rel='noopener';a.href=C.wa+(q?encodeURIComponent(q):'');a.textContent=C.waBtn;a.setAttribute('data-goatcounter-click','bot-whatsapp');var d=add('','bot');d.appendChild(a)}
function answer(id,q){add(fill(A[id]));if(D.wa_after.indexOf(id)>-1)waLink(id==='fallback'?q:'');gc(id)}
function match(q){var s=' '+q.toLowerCase()+' ',best=null,score=0;
 Object.keys(D.kw).forEach(function(id){var n=0;D.kw[id].forEach(function(k){
  if(/^[a-z0-9 \-]+$/.test(k)){if(new RegExp('(^|[^a-z])'+k.replace(/[-]/g,'\\-')+'([^a-z]|$)').test(s))n+=k.length>3?2:1}
  else if(s.indexOf(k)>-1)n+=2});
  if(id==='greet')n=n>0?0.5:0;
  if(n>score){score=n;best=id}});
 return best}
D.chips.forEach(function(id,i){var b=document.createElement('button');b.type='button';b.textContent=D.chip_labels[L][i];b.onclick=function(){add(b.textContent,'me');answer(id)};chips.appendChild(b)});
function open(){panel.hidden=false;btn.setAttribute('aria-expanded','true');if(!started){add(A.greet);started=true}inp.focus()}
function close(){panel.hidden=true;btn.setAttribute('aria-expanded','false');btn.focus()}
btn.onclick=function(){panel.hidden?open():close()};
panel.querySelector('.bot-x').onclick=close;
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!panel.hidden)close()});
form.onsubmit=function(e){e.preventDefault();var q=inp.value.trim();if(!q)return;inp.value='';add(q,'me');var id=match(q);answer(id||'fallback',q)};
})();
