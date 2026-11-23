(function(){
  try { if (window.hljs) { document.querySelectorAll('details.file pre code').forEach(function(el){ window.hljs.highlightElement(el); }); } } catch(e) {}

  function fallback(text){
    var ta = document.createElement('textarea'); ta.value = text; ta.style.position = 'absolute'; ta.style.left = '-9999px';
    document.body.appendChild(ta); ta.select(); try { document.execCommand('copy'); } catch(e) {} document.body.removeChild(ta);
  }
  document.querySelectorAll('.copy').forEach(function(btn){
    btn.addEventListener('click', function(){
      var code = btn.closest('details').querySelector('code').innerText;
      var done = function(){ btn.textContent = 'Copiato'; setTimeout(function(){ btn.textContent = 'Copia'; }, 1500); };
      try { navigator.clipboard.writeText(code).then(done, function(){ fallback(code); done(); }); } catch(e) { fallback(code); done(); }
    });
  });

  document.querySelectorAll('.toggle-files').forEach(function(btn){
    btn.addEventListener('click', function(){
      var all = document.querySelectorAll('details.file[id^="' + btn.getAttribute('data-group') + '-"]');
      var open = Array.prototype.some.call(all, function(d){ return !d.open; });
      all.forEach(function(d){ d.open = open; });
      btn.textContent = open ? 'Chiudi tutti' : 'Apri tutti';
    });
  });
  document.querySelectorAll('a.flink').forEach(function(a){
    a.addEventListener('click', function(){ var d = document.querySelector(a.getAttribute('href')); if (d) d.open = true; });
  });

  var links = {};
  document.querySelectorAll('.toc a').forEach(function(a){ links[a.getAttribute('href').slice(1)] = a; });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if (e.isIntersecting && links[e.target.id]) {
          Object.keys(links).forEach(function(k){ links[k].removeAttribute('aria-current'); });
          links[e.target.id].setAttribute('aria-current', 'true');
          if (window.matchMedia('(max-width:980px)').matches) { links[e.target.id].scrollIntoView({block:'nearest', inline:'center'}); }
        }
      });
    }, {rootMargin:'-20% 0px -70% 0px'});
    document.querySelectorAll('main section[id]').forEach(function(s){ io.observe(s); });
  }

  var root = document.documentElement, key = 'dispensa-filtri-tema';
  try { var saved = localStorage.getItem(key); if (saved) root.setAttribute('data-theme', saved); } catch(e) {}
  document.getElementById('theme').addEventListener('click', function(){
    var cur = root.getAttribute('data-theme');
    var dark = cur ? cur === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
    var next = dark ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem(key, next); } catch(e) {}
  });
})();
