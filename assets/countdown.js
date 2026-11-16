(function(){
  function pad(n){return n<10?'0'+n:''+n}
  var cds=[].slice.call(document.querySelectorAll('.cd'));
  function tick(){
    var now=Date.now();
    cds.forEach(function(el){
      var t=new Date(el.getAttribute('data-target')).getTime(), p=new Date(el.getAttribute('data-prac')).getTime();
      var d=t-now, q=function(u){return el.querySelector('[data-u="'+u+'"]')};
      if(d<=0){el.querySelector('.cd-num').hidden=true;el.querySelector('.cd-sub').hidden=true;el.querySelector('.cd-done').hidden=false;return}
      var s=Math.floor(d/1000);
      q('d').textContent=Math.floor(s/86400);q('h').textContent=pad(Math.floor(s%86400/3600));
      q('m').textContent=pad(Math.floor(s%3600/60));q('s').textContent=pad(s%60);
      var pd=Math.ceil((p-now)/86400000);
      if(pd>0){q('pd').textContent=pd}else{el.querySelector('.cd-sub').hidden=true}
    });
  }
  tick();setInterval(tick,1000);
  [].forEach.call(document.querySelectorAll('.cd-share'),function(a){
    a.href='https://wa.me/?text='+encodeURIComponent(a.getAttribute('data-text')+'\n'+a.getAttribute('data-url'));
  });
})();
