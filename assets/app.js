/* Mehdi Jahaan Merch · Gaslight Studios — bulletproof.
   Loader is pure CSS animation (auto-fades at 1.2s) — NO JS DEPENDENCY.
   JS only adds behavior: navbar, cart, toasts, swipe transition. */
(function(){
  'use strict';
  function $(id){return document.getElementById(id)}
  // Navbar scroll
  window.addEventListener('scroll',function(){
    var n=$('nav'); if(n) n.classList.toggle('scrolled',window.scrollY>18);
  });
  // Cart
  function cartGet(){try{return JSON.parse(localStorage.getItem('mjm_cart')||'[]')}catch(e){return []}}
  function cartSet(c){localStorage.setItem('mjm_cart',JSON.stringify(c));updBadge()}
  function updBadge(){var b=$('badge');if(b)b.textContent=cartGet().length}
  window.addCart=function(s){var c=cartGet();if(c.indexOf(s)<0)c.push(s);cartSet(c);toast('به سبد اضافه شد 🛒💸')};
  window.remCart=function(s){cartSet(cartGet().filter(function(x){return x!==s}));location.reload()};
  updBadge();
  // Toast
  window.toast=function(msg){
    var t=$('toast');
    if(!t){t=document.createElement('div');t.id='toast';document.body.appendChild(t)}
    t.textContent=msg;t.classList.add('show');
    clearTimeout(window.__tt);
    window.__tt=setTimeout(function(){t.classList.remove('show')},1700);
  };
  // Swipe transition on internal link clicks (best-effort)
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[data-link]');
    if(!a)return;
    var h=a.getAttribute('href');
    if(!h||h.charAt(0)==='#'||a.target==='_blank')return;
    if(/^https?:/.test(h))return;
    // if modifier keys, let it go
    if(e.metaKey||e.ctrlKey||e.shiftKey)return;
    var s=$('swipe');
    if(!s)return;
    e.preventDefault();
    s.classList.remove('down');
    s.classList.add('up');
    setTimeout(function(){location.href=h},400);
  });
})();
