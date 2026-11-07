/* Mehdi Jahaan Merch · Gaslight Studios
   Multi-page static build — hard-kill loader by 1500ms to avoid any hangs */
(function(){
  const L=document.getElementById('loader');
  const bar=document.getElementById('ld-bar');
  const app=document.getElementById('app');
  const big=document.getElementById('ld-big');
  const top=document.getElementById('ld-top');
  const b1=document.getElementById('ld-b1');
  const b2=document.getElementById('ld-b2');

  const TEXT="گــســلایــت اســتــودیــو";
  if(big){
    big.innerHTML=TEXT.split('').map(c=>'<span>'+(c===' '?'\u00a0':c)+'</span>').join('');
    Array.from(big.children).forEach((s,i)=>{
      s.style.opacity=0;
      s.style.transform='translateY(12px)';
      s.style.display='inline-block';
      setTimeout(()=>{s.style.opacity=1;s.style.transform='translateY(0)'},450+i*55);
    });
  }
  if(top) setTimeout(()=>top.style.opacity=1,120);
  if(b1) setTimeout(()=>b1.style.opacity=1,900);
  if(b2) setTimeout(()=>b2.style.opacity=1,1000);
  let pct=0;
  const iv=setInterval(()=>{
    pct=Math.min(100,pct+8+Math.random()*8);
    if(bar) bar.style.width=pct+'%';
    if(pct>=100) clearInterval(iv);
  },60);

  function killLoader(){
    if(!L) return;
    clearInterval(iv);
    if(bar) bar.style.width='100%';
    document.body.classList.remove('loading');
    L.classList.add('gone');
    if(app) app.classList.add('ready');
    setTimeout(()=>{L.style.display='none'},600);
  }

  // Multi-layered safety: DOM ready, window load, and hard 1.5s ceiling
  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded',()=>setTimeout(killLoader,350));
  } else {
    setTimeout(killLoader,350);
  }
  window.addEventListener('load',()=>setTimeout(killLoader,200));
  setTimeout(killLoader,1500); // ULTIMATE FUSE — never stuck
})();

/* Navbar scroll state */
window.addEventListener('scroll',()=>{
  const n=document.getElementById('nav');if(!n)return;
  n.classList.toggle('scrolled',window.scrollY>18);
});

/* Cart (localStorage) */
function cartGet(){try{return JSON.parse(localStorage.getItem('mjm_cart')||'[]')}catch(e){return []}}
function cartSet(c){localStorage.setItem('mjm_cart',JSON.stringify(c));updBadge()}
function addCart(slug){const c=cartGet();if(!c.includes(slug))c.push(slug);cartSet(c);toast('به سبد اضافه شد 🛒💸')}
function remCart(slug){cartSet(cartGet().filter(x=>x!==slug));location.reload()}
function updBadge(){const b=document.getElementById('badge');if(b)b.textContent=cartGet().length}
document.addEventListener('DOMContentLoaded',updBadge);

/* Toast */
function toast(msg){
  let t=document.getElementById('toast');
  if(!t){t=document.createElement('div');t.id='toast';document.body.appendChild(t)}
  t.textContent=msg;t.classList.add('show');
  clearTimeout(window.__tt);
  window.__tt=setTimeout(()=>t.classList.remove('show'),1700);
}

/* Swipe transition overlay on internal link clicks */
document.addEventListener('click',e=>{
  const a=e.target.closest('a[data-link]');
  if(!a)return;
  const href=a.getAttribute('href');
  if(!href||href.startsWith('#')||a.target==='_blank')return;
  if(href.startsWith('http'))return;
  const s=document.getElementById('swipe');if(!s)return;
  e.preventDefault();
  s.classList.remove('down');s.classList.add('up');
  setTimeout(()=>{location.href=href},420);
});
