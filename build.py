#!/usr/bin/env python3
"""Multi-page static builder for Mehdi Jahaan Merch. Pure CSS loader = zero JS needed to see the page."""
import os, shutil, json, re

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

# ============== PRODUCTS / CATEGORIES ==============
PRODS=[
    dict(s='tshirt-classic',t='تیشرت کلاسیک بادمجون',p=3200000000,f='p-tshirt',c='tshirts',h=True,col='#c6ff00'),
    dict(s='tshirt-black',t='تیشرت مشکی لشکر ۲۰۰۰ نفری',p=3800000000,f='p-tshirt2',c='tshirts',h=True,col='#a78bfa'),
    dict(s='tshirt-lime',t='تیشرت گسلایت سبز لیمویی',p=3500000000,f='p-tshirt',c='tshirts2',h=False,col='#c6ff00'),
    dict(s='tshirt-purple',t='تیشرت بنفش دیوار بن',p=3400000000,f='p-tshirt2',c='tshirts2',h=False,col='#a78bfa'),
    dict(s='tshirt-pink',t='تیشرت صورتی مهندس هوافضا',p=3600000000,f='p-tshirt',c='tshirts2',h=True,col='#f472b6'),
    dict(s='tshirt-white',t='تیشرت سفید آلمان را',p=3300000000,f='p-tshirt2',c='tshirts2',h=False,col='#f5f7fa'),
    dict(s='tshirt-navy',t='تیشرت سرمه‌ای ادیتور',p=3400000000,f='p-tshirt',c='tshirts2',h=False,col='#60a5fa'),
    dict(s='tshirt-orange',t='تیشرت نارنجی غروب',p=3500000000,f='p-tshirt2',c='tshirts2',h=False,col='#fb923c'),
    dict(s='hoodie-dark',t='هودی مشکی ادیتور ثروتمند',p=8500000000,f='p-hoodie',c='hoodies',h=True,col='#60a5fa'),
    dict(s='hoodie-lime',t='هودی سبز گسلایت',p=8900000000,f='p-hoodie',c='hoodies',h=False,col='#c6ff00'),
    dict(s='hoodie-purple',t='هودی بنفش بادمجون',p=8400000000,f='p-hoodie',c='hoodies',h=False,col='#a78bfa'),
    dict(s='hoodie-gray',t='هودی طوسی لشکر',p=8200000000,f='p-hoodie',c='hoodies',h=False,col='#aab0bd'),
    dict(s='mug-classic',t='ماگ بادمجون رییس',p=1200000000,f='p-mug',c='mugs',h=True,col='#fb923c'),
    dict(s='mug-lime',t='ماگ گسلایت',p=1300000000,f='p-mug',c='mugs',h=False,col='#c6ff00'),
    dict(s='mug-wall',t='ماگ از دیوار معلم زبان گرفتم',p=1400000000,f='p-mug',c='mugs',h=False,col='#f472b6'),
    dict(s='mug-black',t='ماگ مشکی ادیتور',p=1250000000,f='p-mug',c='mugs',h=False,col='#2d3340'),
    dict(s='cap-black',t='کلاه کپ مشکی گسلایت',p=2100000000,f='p-cap',c='caps',h=True,col='#a78bfa'),
    dict(s='cap-lime',t='کلاه کپ سبز بادمجون',p=2200000000,f='p-cap',c='caps',h=False,col='#c6ff00'),
    dict(s='cap-white',t='کلاه کپ سفید',p=2000000000,f='p-cap',c='caps',h=False,col='#f5f7fa'),
    dict(s='tote-egg',t='توت‌بگ بادمجون',p=1500000000,f='p-tote',c='accessories',h=True,col='#a78bfa'),
    dict(s='tote-gas',t='توت‌بگ گسلایت',p=1600000000,f='p-tote',c='accessories',h=False,col='#c6ff00'),
    dict(s='sticker-pack',t='پک ۱۰ عددی استیکر میم',p=450000000,f='p-sticker',c='stickers',h=True,col='#c6ff00'),
    dict(s='sticker-egg',t='استیکر بادمجون عینک‌دار',p=180000000,f='p-sticker',c='stickers',h=False,col='#a78bfa'),
    dict(s='sticker-gas',t='استیکر لوگو گسلایت',p=180000000,f='p-sticker',c='stickers',h=False,col='#c6ff00'),
    dict(s='sticker-wall',t='استیکر دیوار',p=180000000,f='p-sticker',c='stickers',h=False,col='#fb923c'),
    dict(s='mask-black',t='ماسک صورت لشکر',p=800000000,f='p-mask',c='accessories',h=False,col='#60a5fa'),
    dict(s='socks-lime',t='جوراب گسلایت',p=900000000,f='p-socks',c='accessories',h=False,col='#c6ff00'),
    dict(s='socks-purple',t='جوراب بنفش',p=900000000,f='p-socks',c='accessories',h=False,col='#a78bfa'),
    dict(s='phone-egg',t='کاور موبایل بادمجون',p=1800000000,f='p-phone',c='accessories',h=False,col='#f472b6'),
    dict(s='mouse-pad',t='ماوس‌پد گسلایت XXL',p=1700000000,f='p-mousepad',c='accessories',h=False,col='#a78bfa'),
    dict(s='poster-meme',t='پوستر میم اصلی',p=2200000000,f='p-poster',c='poster',h=True,col='#c6ff00'),
    dict(s='poster-army',t='پوستر لشکر ۲۰۰۰ نفری',p=2400000000,f='p-poster',c='poster',h=False,col='#fb923c'),
    dict(s='poster-wall',t='پوستر دیوار معلم زبان',p=2300000000,f='p-poster',c='poster',h=False,col='#f472b6'),
    dict(s='keychain-egg',t='جاسوئیچی بادمجون',p=650000000,f='p-keychain',c='accessories',h=False,col='#f472b6'),
    dict(s='keychain-gas',t='جاسوئیچی گسلایت',p=650000000,f='p-keychain',c='accessories',h=False,col='#c6ff00'),
]
BY_SLUG={p['s']:p for p in PRODS}
CATS=[
    dict(slug='tshirts',t='تیشرت‌ها',d='تیشرت‌های اصلی بادمجون و لشکر',col='#c6ff00',icon='p-tshirt'),
    dict(slug='tshirts2',t='تیشرت‌های ویژه',d='کالکشن محدود رنگی‌رنگی',col='#a78bfa',icon='p-tshirt2'),
    dict(slug='hoodies',t='هودی‌ها',d='هودی‌های گرم برای روزهای سرد آلمان',col='#60a5fa',icon='p-hoodie'),
    dict(slug='mugs',t='ماگ‌ها',d='صبحونه‌ات رو با بادمجون بنوش',col='#fb923c',icon='p-mug'),
    dict(slug='caps',t='کلاه و کپ',d='سرت رو با استایل لشکر بپوش',col='#f472b6',icon='p-cap'),
    dict(slug='stickers',t='استیکر',d='بچسبون رو لپ‌تاپ، دیوار، آلمان',col='#c6ff00',icon='p-sticker'),
    dict(slug='accessories',t='اکسسوری',d='جاسوئیچی، توت‌بگ، جوراب، ماوس‌پد',col='#a78bfa',icon='p-tote'),
    dict(slug='poster',t='پوستر',d='دیوار اتاقت رو میم کن',col='#fb923c',icon='p-poster'),
]
CAT_BY={c['slug']:c for c in CATS}
TOMAN='<svg class="toman" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C7 2 4 6 4 11c0 5 3 10 8 11 5-1 8-6 8-11 0-5-3-9-8-9zm2.4 13.5h-1.6v2h-1.5v-2H9.7v-1.4h1.6v-1.7H9.7V11h1.6V7.5h1.6l-.1 3.5h1.6v1.4h-1.6v1.7h1.6v1.4z"/></svg>'

def fmt(n):
    return f"{n:,}".replace(",","،")

# ============== LOADER (pre-rendered letters) ==============
TITLE="گــســلایــت اســتــودیــو"
LETTERS=''.join('<span>'+(c if c!=' ' else '&nbsp;')+'</span>' for c in TITLE)

def loader_html(pre):
    return f'''<div id="loader" aria-hidden="true">
  <div class="topline">ســاخــتــه شــده تــوســط</div>
  <div class="mark"><img src="{pre}images/gaslight.png" alt="Gaslight"/></div>
  <div class="big">{LETTERS}</div>
  <div class="bottomline">
    <div class="row1">در حال ارسال به وبسایت مورد نظر</div>
    <div class="row2">سرور گسلایت ← وبسایت مرچ مهدی جهان</div>
  </div>
  <div class="bar"></div>
</div>'''

# ============== PAGE SHELL ==============
NAV_ITEMS=[
    ('home','خانه',''),
    ('products','محصولات','products/'),
    ('cat1','تیشرت','category/tshirts/'),
    ('cat2','هودی','category/hoodies/'),
    ('cat3','اکسسوری','category/accessories/'),
    ('blog','بلاگ','blog/'),
    ('faq','سؤالات','faq/'),
    ('ship','ارسال','shipping/'),
    ('about','درباره','about/'),
    ('contact','تماس','contact/'),
]
def nav(active, pre):
    lis=''
    for k,t,h in NAV_ITEMS:
        on=' on' if active==k else ''
        svg='<svg width="18" height="18" style="display:inline"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12l9-9 9 9"/><path d="M5 10v10h14V10"/></svg></svg>' if k=='home' else ''
        lis+=f'<a class="l{on}" data-link href="{pre}{h}">{svg}{t}</a>'
    cart_badge='<span class="badge" id="badge">0</span>'
    return f'''<nav class="nav" id="nav"><div class="ctn"><div class="nav-in">
  <a href="{pre}" data-link class="brand">
    <div class="sq"><img src="{pre}images/gaslight.png" alt="M"/></div>
    <div class="b-txt"><b>مهدی‌مرچ</b><span>MEHDI JAHAN MERCH</span></div>
  </a>
  <div class="divider"></div>
  <div class="search">
    <svg class="ic" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
    <input type="text" placeholder="دنبال چی می‌گردی؟ ادیتور ثروتمند؟ عینک قرمز؟ 🤡" readonly onclick="toast('جست‌وجو در حال بارگذاری توسط مهندس هوافضا 🚀')"/>
  </div>
  <div class="nav-act">
    <button class="nb" onclick="toast('علاقه‌مندی‌ها هنوز آماده نیست 🍆')" aria-label="like"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 1 0-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/></svg></button>
    <a class="nb" href="{pre}cart/" data-link aria-label="cart"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6h15l-1.5 9h-12z"/><circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M6 6L5 3H2"/></svg>{cart_badge}</a>
  </div>
</div></div></nav>'''

def subnav(active, pre):
    lis=''
    for k,t,h in NAV_ITEMS:
        on=' on' if active==k else ''
        svg='<svg width="18" height="18" style="display:inline"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12l9-9 9 9"/><path d="M5 10v10h14V10"/></svg></svg>' if k=='home' else ''
        lis+=f'<a class="l{on}" data-link href="{pre}{h}">{svg}{t}</a>'
    return f'<div class="sub-bar" style="position:sticky;top:66px;background:var(--bg);z-index:50;border-bottom:1px solid var(--line)"><div class="ctn"><div class="sub">{lis}</div></div></div>'

def crumb(items, pre):
    out='<div class="crumb"><div class="ctn"><div class="crumb-in">'
    for i,it in enumerate(items):
        if i:out+='<span class="s">/</span>'
        if it.get('h') is not None:
            out+=f'<a href="{pre}{it["h"]}" data-link>{it["t"]}</a>'
        else:
            out+=f'<b>{it["t"]}</b>'
    out+='</div></div></div>'
    return out

def footer(pre):
    return f'''<footer>
<div class="ctn">
  <div class="f-grid">
    <div>
      <a class="brand-big" href="{pre}" data-link>
        <div class="sq"><img src="{pre}images/gaslight.png" alt="G"/></div>
        <div><b>مهدی‌مرچ</b><span>MEHDI JAHAN MERCH</span></div>
      </a>
      <p class="f-desc">مرجع غیررسمی مرچ‌های میم و خنده‌دار مهدی جهان. این سایت فنه و توسط لشکر ۲۰۰۰ نفری ساخته شده. هیچ بادمجونی آزاری ندیده. 🍆</p>
      <div class="soc">
        <a href="#"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h3l-7.5 8.6L22 22h-6.9l-5.4-7-6.2 7H.5l8-9.2L0 2z"/></svg></a>
        <a href="#"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg></a>
        <a href="#"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M23 7.2s-.2-1.6-.9-2.3c-.8-.9-1.8-.9-2.2-1C17 3.6 12 3.6 12 3.6s-5 0-7.9.3c-.4.1-1.4.1-2.2 1C1.2 5.6 1 7.2 1 7.2S.8 9 .8 10.8v1.8c0 1.8.2 3.6.2 3.6s.2 1.6.9 2.3c.8.9 1.9.9 2.4 1 1.8.2 7.7.3 7.7.3s5 0 7.9-.3c.4-.1 1.4-.1 2.2-1 .7-.7.9-2.3.9-2.3s.2-1.8.2-3.6v-1.8c0-1.8-.2-3.7-.2-3.7zM9.7 14.8V8.2L15.8 11.5l-6.1 3.3z"/></svg></a>
        <a href="#"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M22 3L2 10.5l6 2.2L20 5l-11 9.1-.4 5.9 2.6-2.5 6 4.4L22 3z"/></svg></a>
      </div>
    </div>
    <div class="f-col"><b>فروشگاه</b>
      <a href="{pre}products/" data-link>همه محصولات</a>
      <a href="{pre}category/tshirts/" data-link>تیشرت‌ها</a>
      <a href="{pre}category/hoodies/" data-link>هودی‌ها</a>
      <a href="{pre}category/accessories/" data-link>اکسسوری</a>
      <a href="{pre}cart/" data-link>سبد خرید</a>
      <a href="{pre}collections/" data-link>کالکشن‌ها</a>
      <a href="{pre}gift-cards/" data-link>کارت هدیه</a>
    </div>
    <div class="f-col"><b>پشتیبانی</b>
      <a href="{pre}faq/" data-link>سؤالات متداول</a>
      <a href="{pre}shipping/" data-link>اطلاعات ارسال</a>
      <a href="{pre}returns/" data-link>شرایط بازگشت</a>
      <a href="{pre}privacy/" data-link>حریم خصوصی</a>
      <a href="{pre}terms/" data-link>قوانین</a>
      <a href="{pre}track-order/" data-link>پیگیری سفارش</a>
      <a href="{pre}size-guide/" data-link>راهنمای سایز</a>
      <a href="{pre}help/" data-link>مرکز راهنما</a>
    </div>
    <div class="f-col"><b>کمپانی</b>
      <a href="{pre}about/" data-link>درباره ما</a>
      <a href="{pre}blog/" data-link>وبلاگ</a>
      <a href="{pre}contact/" data-link>تماس با ما</a>
      <a href="{pre}careers/" data-link>همکاری</a>
      <a href="{pre}press/" data-link>مطبوعات</a>
      <a href="{pre}news/" data-link>اخبار</a>
      <a href="{pre}team/" data-link>تیم</a>
    </div>
  </div>
  <div class="f-bot">
    <div>© ۱۴۰۳ — تمام حقوق خنده‌های این سایت متعلق به لشکر ۲۰۰۰ نفری است. 🤣</div>
    <div class="studio">GASLIGHT STUDIOS</div>
  </div>
</div>
</footer>
<div id="swipe"></div>
<div id="toast"></div>
<script src="{pre}assets/app.js"></script>
</body></html>'''

def page(title, active, crumbs, content, pre, is_root=False):
    # pre is the path prefix back to root
    return f'''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title} | مهدی جهان مرچ</title>
<link rel="icon" type="image/svg+xml" href="{pre}images/favicon.svg"/>
<link rel="stylesheet" href="{pre}assets/style.css"/>
</head>
<body>
{loader_html(pre)}
<div id="app">
{nav(active,pre)}
<div class="topsp"></div>
{crumb(crumbs,pre) if crumbs else subnav(active,pre)}
<main class="page"><div class="ctn">{content}</div></main>
</div>
{footer(pre)}'''

# ============== COMPONENTS ==============
def card(p, pre):
    hot='<span class="hot">داغ 🔥</span>' if p.get('h') else ''
    return f'''<a class="card" href="{pre}product/{p['s']}/" data-link>
  <div class="th"><div class="bg" style="background:{p['col']}33"></div>{hot}
    <div class="cv"><svg viewBox="0 0 200 200"><use href="{pre}images/products.svg#{p['f']}"/></svg></div>
  </div>
  <div class="info">
    <div class="tt">{p['t']}</div>
    <div class="pr"><div class="pri"><span class="u">{fmt(p['p'])}</span>{TOMAN}</div>
    <button class="add" onclick="event.preventDefault();event.stopPropagation();addCart('{p['s']}')">+</button></div>
  </div>
</a>'''

def cat_card(c, pre):
    return f'''<a class="cat" href="{pre}category/{c['slug']}/" data-link style="background:radial-gradient(circle at 80% 20%,{c['col']}25 0%,transparent 55%),var(--bg2)">
  <div><h3>{c['t']}</h3><p>{c['d']}</p></div>
  <div class="arr">←</div>
  <div class="cg"><svg viewBox="0 0 200 200"><use href="{pre}images/products.svg#{c['icon']}"/></svg></div>
</a>'''

def post_card(slug,title,date,ex,pre):
    return f'<a class="post-card" href="{pre}{slug}/" data-link><div class="date">{date}</div><h3>{title}</h3><p>{ex}</p></a>'

def write(path, html):
    full=os.path.join(ROOT,path)
    os.makedirs(os.path.dirname(full),exist_ok=True)
    with open(full,'w',encoding='utf-8') as f:f.write(html)

# ============== PAGES ==============
def build_home():
    hot=[p for p in PRODS if p.get('h')][:8]
    new=PRODS[:8]
    pre=''
    c=f'''
<section><div class="hero-grid">
  <div class="hero-banner">
    <div class="hero-mascot"><svg viewBox="0 0 200 200"><use href="images/products.svg#egg"/></svg></div>
    <div>
      <h1>مرچ رسمی میم‌های <em>مهدی جهان</em><br/>رسیده به لشکر ۲۰۰۰ نفر</h1>
      <p>تیشرت، هودی، ماگ، استیکر و همه چیزی که یک ادیتور ثروتمند برای خندیدن به مهدی نیاز داره. قیمت‌ها از ۱ میلیارد تومان شروع می‌شن (چرا که نه؟) 💸</p>
      <div class="btns"><a class="btn p" href="products/" data-link>مشاهده محصولات ←</a><a class="btn g" href="about/" data-link>درباره ما</a></div>
    </div>
  </div>
  <div class="hero-stat lg">
    <div><div class="n">{len(PRODS)}+</div><div class="t">محصول مختلف<br/>در ۸ دسته</div></div>
    <div class="hero-feats">
      <a class="feat o" href="category/tshirts/" data-link><span class="arr">←</span><div class="t">تیشرت‌های<br/>بادمجون 🍆</div></a>
      <a class="feat k" href="category/accessories/" data-link><span class="arr">←</span><div class="t">اکسسوری<br/>لشکرکشی 🎯</div></a>
      <a class="feat m" href="category/hoodies/" data-link><span class="arr">←</span><div class="t">هودی‌های<br/>ادیتوری 🧥</div></a>
      <a class="feat b" href="category/poster/" data-link><span class="arr">←</span><div class="t">پوسترهای<br/>میم 🖼️</div></a>
    </div>
  </div>
  <div class="hero-stat"><div class="n">∞</div><div class="t">تعداد خنده در هر ویدیو<br/>مهندس هوافضا ۱۰۰٪</div></div>
</div></section>
<section class="section"><div class="section-head"><div><h2>دسته‌بندی‌ها</h2><div class="sub-t">همه چیز برای طرفداران میم</div></div><a class="more" href="products/" data-link>همه محصولات ←</a></div>
<div class="grid-c">{''.join(cat_card(c,'') for c in CATS)}</div></section>
<section class="section"><div class="section-head"><div><h2>داغ‌ترین‌ها 🔥</h2><div class="sub-t">پرفروش‌های همین هفته از لشکر</div></div><a class="more" href="products/" data-link>مشاهده همه ←</a></div>
<div class="grid-p">{''.join(card(p,'') for p in hot)}</div></section>
<section class="section"><div class="section-head"><div><h2>محصولات جدید ✨</h2><div class="sub-t">کالکشن گسلایت استودیو</div></div></div>
<div class="grid-p">{''.join(card(p,'') for p in new)}</div></section>
<section class="section"><div class="section-head"><h2>چرا مهدی‌مرچ؟</h2></div>
<div class="grid-stats">
  <div class="hero-stat"><div><div class="n">۱۰۰٪</div><div class="t">غیررسمی و فان</div></div></div>
  <div class="hero-stat"><div><div class="n">{len(PRODS)}+</div><div class="t">محصول در رنگ‌های مختلف</div></div></div>
  <div class="hero-stat"><div><div class="n">۲۴/۷</div><div class="t">توسط بادمجون‌ها پشتیبانی</div></div></div>
  <div class="hero-stat"><div><div class="n">۱B+</div><div class="t">قیمت به تومان (شوخی)</div></div></div>
</div></section>'''
    write('index.html', page('خانه','home',None,c,'',is_root=True))

def build_products():
    c=f'<h1 class="pg-title">همه محصولات</h1><p class="pg-lede">کامل‌ترین آرشیو مرچ میم مهدی جهان.</p><div class="grid-p">'+''.join(card(p,'../') for p in PRODS)+'</div>'
    write('products/index.html', page('محصولات','products',[{'t':'خانه','h':''},{'t':None}],c,'../'))

def build_category(cat):
    items=[p for p in PRODS if p['c']==cat['slug']]
    c=f'<h1 class="pg-title">{cat["t"]}</h1><p class="pg-lede">{cat["d"]}</p><div class="grid-p">'+''.join(card(p,'../../') for p in items)+'</div>'
    key='cat1' if cat['slug'] in ('tshirts','tshirts2') else ('cat2' if cat['slug']=='hoodies' else ('cat3' if cat['slug']=='accessories' else 'products'))
    write(f'category/{cat["slug"]}/index.html', page(cat['t'],key,[{'t':'خانه','h':''},{'t':'محصولات','h':'products/'},{'t':None}],c,'../../'))

def build_product(p):
    pre='../../'
    rel=[x for x in PRODS if x['c']==p['c'] and x['s']!=p['s']][:4]
    c=f'''<div class="pdp">
  <div class="img"><div class="bg" style="background:{p['col']}33"></div><svg viewBox="0 0 200 200"><use href="{pre}images/products.svg#{p['f']}"/></svg></div>
  <div class="info">
    <div class="tag" style="color:var(--acc);border-color:var(--acc-dim);background:var(--acc-dim)">{CAT_BY[p['c']]['t']}</div>
    <h1 style="font-size:32px;margin:14px 0 6px">{p['t']}</h1>
    <div class="price"><span>{fmt(p['p'])}</span>{TOMAN}</div>
    <p class="desc">این {p['t']} با بهترین کیفیت بادمجونی تولید شده. مناسب استایل خیابانی لشکر ۲۰۰۰ نفری، ادیتور ثروتمند، و کسانی که هنوز از پرش مهدی از دیوار خندونشون نمیاد.</p>
    <div class="sizes"><button class="sz on">S</button><button class="sz">M</button><button class="sz">L</button><button class="sz">XL</button><button class="sz">XXL</button></div>
    <div class="act"><button class="btn p" onclick="addCart('{p['s']}');toast('اضافه شد به سبد 🛒')">افزودن به سبد</button><a class="btn g" href="{pre}cart/" data-link>سبد خرید</a></div>
    <div style="margin-top:30px"><h3 style="font-size:14px;color:var(--fg3);letter-spacing:.1em;margin-bottom:10px">مشخصات</h3>
    <div class="kvs"><div class="kv"><div class="k">جنس</div><div class="v">۱۰۰٪ بادمجون</div></div><div class="kv"><div class="k">رنگ</div><div class="v">چند رنگ</div></div><div class="kv"><div class="k">تولید</div><div class="v">گسلایت استودیو</div></div><div class="kv"><div class="k">ارسال</div><div class="v">از آلمان 🚀</div></div></div></div>
  </div></div>
<section class="section"><div class="section-head"><h2>محصولات مشابه</h2></div><div class="grid-p">{''.join(card(x,'../../') for x in rel)}</div></section>'''
    write(f'product/{p["s"]}/index.html', page(p['t'],'products',[{'t':'خانه','h':''},{'t':'محصولات','h':'products/'},{'t':CAT_BY[p['c']]['t'],'h':f'category/{p["c"]}/'},{'t':None}],c,pre))

def build_cart():
    slugs_json=json.dumps({p['s']:{'t':p['t'],'p':p['p'],'f':p['f'],'col':p['col']} for p in PRODS},ensure_ascii=False)
    c=f'''<h1 class="pg-title">سبد خرید</h1>
<div id="cart-items"><div class="empty"><div class="big">🛒</div><h2>سبدت خالیه</h2><p>یه چرخ تو فروشگاه بزن و از بادمجون‌ها چند تا بردار.</p><a class="btn p" href="../products/" data-link>شروع خرید ←</a></div></div>
<div id="cart-sum" style="display:none"></div>
<script>
(function(){{
  const SLUGS={slugs_json};
  const TOMAN=`{TOMAN}`;
  const fmt=n=>n.toLocaleString('en-US').replaceAll(',','،');
  const cart=cartGet();
  const box=document.getElementById('cart-items');
  const sum=document.getElementById('cart-sum');
  if(!cart.length)return;
  let tot=0;
  const html=cart.map(s=>{{
    const p=SLUGS[s];if(!p)return'';
    tot+=p.p;
    return `<div class="cart-item"><div class="th"><div class="bg" style="background:${{p.col}}33"></div><svg viewBox="0 0 200 200"><use href="../images/products.svg#${{p.f}}"/></svg></div><div class="meta"><div class="t">${{p.t}}</div><div class="p">${{fmt(p.p)}} تومان</div></div><button class="rm" onclick="remCart('${{s}}')">حذف</button></div>`;
  }}).join('');
  box.innerHTML=html;
  sum.style.display='flex';
  sum.innerHTML=`<div><div class="lbl">مجموع سبد</div><div class="tot">${{fmt(tot)}} ${{TOMAN}}</div></div><div style="display:flex;gap:10px"><button class="btn g" onclick="toast('در حال ارسال به درگاه بادمجون... 🍆')">پرداخت (شوخی)</button><a class="btn p" href="../products/" data-link>ادامه خرید</a></div>`;
}})();
</script>'''
    write('cart/index.html', page('سبد خرید','cart',[{'t':'خانه','h':''},{'t':None}],c,'../'))

def doc_page(slug,title,active,crumbs,body,pre='../',depth=1):
    write(f'{slug}/index.html', page(title,active,crumbs,f'<div class="doc">{body}</div>',pre))

def build_all():
    # Clear previous page folders (keep assets/, images/, fonts/, .git/, .nojekyll)
    keep={'assets','images','fonts','.git'}
    for d in os.listdir('.'):
        if d.startswith('.') and d!='.nojekyll': continue
        if d in keep: continue
        if os.path.isdir(d): shutil.rmtree(d)
        elif d.endswith('.html'): os.remove(d)
    open('.nojekyll','w').close()

    build_home(); build_products(); build_cart()
    for c in CATS: build_category(c)
    for p in PRODS: build_product(p)

    # ====== DOZENS OF CONTENT PAGES ======
    PAGES=[
      ('about','درباره ما','about',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>درباره مهدی‌مرچ 🍆</h2>
        <p>مهدی‌مرچ یک فروشگاه کاملاً فان و غیررسمی برای طرفداران میم‌های مهدی جهانه. این پروژه توسط <strong>گسلایت استودیو</strong> به نشون دادن ارادت به لشکر ۲۰۰۰ نفری ساخته شده.</p>
        <h3>داستان ما</h3><p>یک شب یکی از اعضای لشکر دید ویدیویی از مهدی روی دیوار و فکر کرد «چرا مرچ بادمجون نداشته باشیم؟» — نتیجه‌اش هم همین سایت شد.</p>
        <h3>چشم‌انداز</h3><p>رسیدن به یک میلیون بادمجون در سراسر جهان.</p>
        <h3>ارزش‌ها</h3><ul><li>خنده اول از همه</li><li>کیفیت در حد بادمجون درجه یک</li><li>احترام به همه حتی کسانی که از دیوار پریدن</li></ul>'''),

      ('contact','تماس با ما','contact',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>تماس با ما 📮</h2>
        <p>برای هر سوال، پیشنهاد، شکایت، یا ارسال بادمجون تازه، از راه‌های زیر با ما در ارتباط باش:</p>
        <div class="kvs" style="margin-top:20px">
          <div class="kv"><div class="k">ایمیل</div><div class="v" style="direction:ltr">hi@gaslight.studio</div></div>
          <div class="kv"><div class="k">تلگرام</div><div class="v">@MehdiMerch</div></div>
          <div class="kv"><div class="k">اینستاگرام</div><div class="v">@mehdi.merch</div></div>
          <div class="kv"><div class="k">آدرس</div><div class="v">یه جایی نزدیک دیوار معلم زبان 🏫</div></div>
        </div>'''),

      ('faq','سؤالات متداول','faq',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>سؤالاتی که زیاد پرسیده می‌شن ❓</h2>
        <details class="faq-i"><summary>این سایت واقعیه؟</summary><p>فقط از نظر خنده واقعیه. یک دمو کامل است.</p></details>
        <details class="faq-i"><summary>قیمت‌ها چرا اینقدر بالان؟</summary><p>چون میلیاردر بودن آرزوی ادیتوره 😂</p></details>
        <details class="faq-i"><summary>ارسال به آلمان هم دارید؟</summary><p>حتماً، مهندس هوافضا شخصاً تحویل می‌ده.</p></details>
        <details class="faq-i"><summary>می‌تونم عضو لشکر بشم؟</summary><p>بله، کافیه به یکی از میم‌های مهدی بخندی.</p></details>
        <details class="faq-i"><summary>چرا بادمجون؟</summary><p>چون مثل بنفش، شاد، و از دیوار می‌تونه بپره. 🍆</p></details>'''),

      ('shipping','اطلاعات ارسال','ship',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>اطلاعات ارسال 🚚</h2>
        <p>ارسال بادمجون‌ها به همه جای دنیا:</p>
        <table class="tbl"><thead><tr><th>مقصد</th><th>زمان تحویل</th><th>هزینه</th></tr></thead><tbody>
        <tr><td>تهران</td><td>۲ روز</td><td class="acc">۱۵۰,۰۰۰,۰۰۰</td></tr>
        <tr><td>شهرستان‌ها</td><td>۳-۵ روز</td><td class="acc">۲۵۰,۰۰۰,۰۰۰</td></tr>
        <tr><td>آلمان 🚀</td><td>۱ هفته</td><td class="acc">۱,۲۰۰,۰۰۰,۰۰۰</td></tr>
        <tr><td>بالای دیوار معلم زبان</td><td>همون لحظه</td><td class="acc">رایگان 🤣</td></tr>
        </tbody></table>'''),

      ('returns','شرایط بازگشت','faq',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>شرایط بازگشت ↩️</h2>
        <p>اگه بادمجونی خوشحالت نکرد، می‌تونی پسش بدی:</p>
        <ul><li>تا ۳۰ روز بعد از تحویل</li><li>کالا باید هنوز خنده‌دار باشه</li><li>هزینه بازگشت با لشکر است</li></ul>'''),

      ('privacy','حریم خصوصی','faq',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>حریم خصوصی 🔒</h2>
        <p>ما هیچ اطلاعاتی ازت جمع نمی‌کنیم. سبد خرید تو localStorage مرورگر خودت ذخیره می‌شه.</p>
        <h3>کوکی‌ها</h3><p>ما کوکی نمی‌کاریم. فقط بادمجون. 🍆</p>'''),

      ('terms','قوانین','faq',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>قوانین ⚖️</h2><p>با استفاده از این سایت قبول می‌کنی:</p>
        <ul><li>به ویدیوهای مهدی بخندی</li><li>ادیتور رو تشویق کنی</li><li>به بادمجون‌ها احترام بزنی</li></ul>'''),

      ('careers','همکاری','about',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>عضو تیم گسلایت شو 🤝</h2>
        <p>موقعیت‌های باز:</p>
        <ul><li><strong>ادیتور ارشد بادمجون</strong></li><li><strong>مدیر جامعه لشکر</strong></li><li><strong>طراح مرچ</strong></li><li><strong>مهندس هوافضا</strong> 🚀</li></ul>'''),

      ('press','مطبوعات','about',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>اتاق مطبوعات 📰</h2><p>رسانه‌ها می‌تونن از منابع زیر استفاده کنن:</p>
        <ul><li>پرس‌کیتی شامل لوگو و بادمجون</li><li>عکس‌های با کیفیت</li></ul>'''),

      ('help','مرکز راهنما','faq',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>مرکز راهنما 💡</h2><p>از اینجا به بخش‌های مختلف دسترسی داشته باش:</p>
        <div class="grid-stats">
          <a class="hero-stat" data-link href="../faq/"><div><div class="n" style="font-size:24px">❓</div><div class="t">سؤالات متداول</div></div></a>
          <a class="hero-stat" data-link href="../shipping/"><div><div class="n" style="font-size:24px">🚚</div><div class="t">اطلاعات ارسال</div></div></a>
          <a class="hero-stat" data-link href="../track-order/"><div><div class="n" style="font-size:24px">📦</div><div class="t">پیگیری سفارش</div></div></a>
          <a class="hero-stat" data-link href="../size-guide/"><div><div class="n" style="font-size:24px">📏</div><div class="t">راهنمای سایز</div></div></a>
          <a class="hero-stat" data-link href="../contact/"><div><div class="n" style="font-size:24px">📮</div><div class="t">تماس</div></div></a>
          <a class="hero-stat" data-link href="../returns/"><div><div class="n" style="font-size:24px">↩️</div><div class="t">بازگشت</div></div></a>
        </div>'''),

      ('team','تیم ما','about',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>تیم گسلایت 👥</h2><p>گروه کوچیکی از بادمجون‌های داوطلب.</p>
        <div class="team-grid">
          <div class="team"><div class="av">🍆</div><h4>بادمجون اول</h4><div class="role">بنیان‌گذار</div></div>
          <div class="team"><div class="av">🎨</div><h4>طراح ارشد</h4><div class="role">طراحی بادمجون</div></div>
          <div class="team"><div class="av">💻</div><h4>دِو</h4><div class="role">توسعه وب</div></div>
          <div class="team"><div class="av">🚀</div><h4>مهندس هوافضا</h4><div class="role">لجستیک هوایی</div></div>
          <div class="team"><div class="av">🎭</div><h4>کمدین</h4><div class="role">نویسنده میم</div></div>
          <div class="team"><div class="av">📱</div><h4>کامیونیتی منیجر</h4><div class="role">مدیر لشکر</div></div>
        </div>'''),

      ('size-guide','راهنمای سایز','faq',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>راهنمای سایز 📏</h2>
        <table class="tbl"><thead><tr><th>سایز</th><th>سینه</th><th>قد</th><th>مناسب</th></tr></thead><tbody>
        <tr><td>S</td><td>۴۸</td><td>۶۸</td><td>بادمجون‌های کوچیک</td></tr>
        <tr><td>M</td><td>۵۲</td><td>۷۱</td><td>بادمجون‌های معمولی</td></tr>
        <tr><td>L</td><td>۵۶</td><td>۷۴</td><td>بادمجون‌های درشت</td></tr>
        <tr><td>XL</td><td>۶۰</td><td>۷۷</td><td>لشکر حرفه‌ای</td></tr>
        <tr><td>XXL</td><td>۶۴</td><td>۸۰</td><td>مهندس هوافضا</td></tr>
        </tbody></table>'''),

      ('track-order','پیگیری سفارش','faq',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>پیگیری سفارش 📦</h2>
        <p>کد سفارشت رو وارد کن (هر چی دوست داری):</p>
        <div style="display:flex;gap:10px;margin-top:20px;max-width:500px">
        <input style="flex:1;background:var(--bg);border:1px solid var(--line2);color:var(--fg);padding:12px 16px;border-radius:14px" placeholder="مثلاً BJM-1337"/>
        <button class="btn p" onclick="toast('بادمجون شما در حال ارسال از آلمان 🚀')">پیگیری</button></div>
        <h3 style="margin-top:30px">وضعیت‌ها</h3><ul>
        <li>🍆 در حال برداشت از مزرعه بادمجون</li>
        <li>🎨 در حال چاپ میم</li>
        <li>✈️ در حال پرواز</li>
        <li>🏃 در حال پرش از روی دیوار</li>
        <li>✅ تحویل</li></ul>'''),

      ('gift-cards','کارت هدیه','products',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>کارت هدیه 🎁</h2><p>به دوستات بادمجون هدیه بده.</p>
        <div class="grid-p">
        <div class="card"><div class="th" style="background:linear-gradient(135deg,#c6ff00,#a78bfa)"><div style="color:#000;font-weight:700;font-size:22px">۵۰۰M</div></div><div class="info"><div class="tt">کارت هدیه ۵۰۰ میلیون</div><div class="pr"><div class="pri"><span class="u">۵۰۰,۰۰۰,۰۰۰</span>'''+TOMAN+'''</div><button class="add" onclick="addCart('gift-500m')">+</button></div></div></div>
        <div class="card"><div class="th" style="background:linear-gradient(135deg,#a78bfa,#f472b6)"><div style="color:#fff;font-weight:700;font-size:22px">۱B</div></div><div class="info"><div class="tt">کارت هدیه ۱ میلیارد</div><div class="pr"><div class="pri"><span class="u">۱,۰۰۰,۰۰۰,۰۰۰</span>'''+TOMAN+'''</div><button class="add" onclick="addCart('gift-1b')">+</button></div></div></div>
        <div class="card"><div class="th" style="background:linear-gradient(135deg,#000,#c6ff00)"><div style="color:var(--acc);font-weight:700;font-size:22px">∞</div></div><div class="info"><div class="tt">کارت هدیه بی‌نهایت</div><div class="pr"><div class="pri"><span class="u">۱۰,۰۰۰,۰۰۰,۰۰۰</span>'''+TOMAN+'''</div><button class="add" onclick="addCart('gift-inf')">+</button></div></div></div>
        </div>'''),

      ('collections','کالکشن‌ها','products',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>کالکشن‌ها 🎨</h2><div class="grid-c">
        <a class="cat" data-link href="../category/tshirts/" style="background:radial-gradient(circle at 80% 20%,#c6ff0025,transparent 55%),var(--bg2)"><div><h3>بادمجون 🍆</h3><p>سری اصلی</p></div><div class="arr">←</div></a>
        <a class="cat" data-link href="../category/hoodies/" style="background:radial-gradient(circle at 80% 20%,#a78bfa33,transparent 55%),var(--bg2)"><div><h3>گسلایت 💡</h3><p>مونوگرم سیاه/سفید/سبز</p></div><div class="arr">←</div></a>
        <a class="cat" data-link href="../category/accessories/" style="background:radial-gradient(circle at 80% 20%,#f472b633,transparent 55%),var(--bg2)"><div><h3>لشکر 🎯</h3><p>برای سربازان</p></div><div class="arr">←</div></a>
        <a class="cat" data-link href="../category/poster/" style="background:radial-gradient(circle at 80% 20%,#60a5fa33,transparent 55%),var(--bg2)"><div><h3>دیوار 🧱</h3><p>یادبود خاطره</p></div><div class="arr">←</div></a>
        </div>'''),

      ('news','اخبار','about',[{'t':'خانه','h':''},{'t':None}],'''
        <h2>آخرین اخبار 🗞️</h2>
        <div class="post-card"><div class="date">۲۵ آبان</div><h3>راه‌اندازی مهدی‌مرچ توسط گسلایت استودیو</h3><p>سایت جدید بالاخره آماده شد.</p></div>
        <div class="post-card" style="margin-top:10px"><div class="date">۲۰ آبان</div><h3>کالکشن گسلایت معرفی شد</h3><p>کپسول جدید با رنگ سبز لیمویی #c6ff00.</p></div>
        <div class="post-card" style="margin-top:10px"><div class="date">۱۲ آبان</div><h3>لشکر به ۳۰۰۰ نفر نزدیک شد</h3><p>رشد روزافزون جامعه.</p></div>'''),
    ]
    for slug,title,act,cr,body in PAGES:
        doc_page(slug,title,act,cr,body)

    # More extra pages (shorter bodies)
    EXTRA=[
      ('wholesale','فروش عمده','about','<h2>فروش عمده 🏭</h2><p>حداقل ۵۰ عدد بادمجون. تخفیف لشکر تا ۳۰٪.</p>'),
      ('affiliate','همکاری در فروش','about','<h2>افیلیت 💰</h2><p>کمیسیون ۲۰٪ از هر فروش.</p>'),
      ('ambassadors','سفیران برند','about','<h2>سفیران 🌟</h2><p>مرچ رایگان و کد اختصاصی.</p>'),
      ('sustainability','پایداری','about','<h2>پایداری 🌱</h2><p>بادمجون‌ها قابل بازیافت، بسته‌بندی کاغذی.</p>'),
      ('manufacturing','تولید','about','<h2>تولید 🏭</h2><p>هر بادمجون قبل از ارسال تست خنده می‌گذرونه.</p>'),
      ('investors','سرمایه‌گذاران','about','<h2>سرمایه‌گذاران 💼</h2><p>ارزش‌گذاری: ۱۳ میلیارد بادمجون.</p>'),
      ('events','رویدادها','about','<h2>رویدادها 🎪</h2><p>میت‌آپ لشکر، ورکشاپ میم، فلش‌موب دیوار.</p>'),
      ('podcast','پادکست','blog','<h2>بادمجون رادیو 🎙️</h2><p>هر هفته با میم‌سازان گفتگو می‌کنیم.</p>'),
      ('newsletter','خبرنامه','about','<h2>خبرنامه 📬</h2><p>هر هفته ایمیل خنده‌دار.</p>'),
      ('partners','همکاران','about','<h2>همکاران 🤝</h2><p>مزرعه بادمجون، خط هوایی لشکر، دیوار معلم زبان.</p>'),
      ('testimonials','نظرات','products','<h2>نظرات 💬</h2><p>نظرات واقعی از مشتریان.</p>'),
      ('campus','تخفیف دانشجویی','products','<h2>تخفیف دانشجویی 🎓</h2><p>۲۰٪ تخفیف با کارت دانشجویی.</p>'),
      ('community','جامعه لشکر','about','<h2>جامعه لشکر 🎯</h2><p>تلگرام، اینستاگرام، توییتر.</p>'),
      ('wall-of-fame','دیوار مشاهیر','about','<h2>دیوار مشاهیر 🏆</h2><p>برترین بادمجون‌های هفته.</p>'),
      ('memes','آرشیو میم','blog','<h2>آرشیو میم 🤣</h2><p>بهترین میم‌های مهدی.</p>'),
      ('eggplant-army','ارتش بادمجون','about','<h2>ارتش بادمجون 🎖️</h2><p>درجات: تازه‌وارد، سرباز، فرمانده، مهندس هوافضا.</p>'),
      ('editor-academy','آکادمی ادیتور','blog','<h2>آکادمی ادیتور 🎬</h2><p>یاد بگیر میم درست کنی.</p>'),
      ('germany','آلمان','blog','<h2>مهدی و آلمان 🇩🇪</h2><p>تحلیل طنز یک شایعه.</p>'),
      ('alumni','دانش‌آموختگان','about','<h2>دانش‌آموختگان 🎓</h2><p>کسانی که از لشکر رفتن.</p>'),
      ('airplane','مهندس هوافضا','blog','<h2>مهندس هوافضا ✈️</h2><p>یک عنوان میم ماندگار.</p>'),
      ('wall','دیوار معلم زبان','blog','<h2>دیوار معلم زبان 🧱</h2><p>تاریخ‌سازترین پرش.</p>'),
      ('behind','پشت صحنه','blog','<h2>پشت صحنه 🎥</h2><p>چطور این سایت ساخته شد.</p>'),
      # Extra filler pages for MORE
      ('refunds','استرداد','faq','<h2>استرداد وجه 💸</h2><p>اگه بادمجون نرسید، پولت برمی‌گرده.</p>'),
      ('accessibility','دسترس‌پذیری','about','<h2>دسترس‌پذیری ♿</h2><p>همه باید بتونن بخندن.</p>'),
      ('cookies','کوکی‌ها','faq','<h2>کوکی‌ها 🍪</h2><p>این سایت کوکی نمی‌کارد.</p>'),
      ('licenses','لایسنس‌ها','about','<h2>لایسنس‌ها 📜</h2><p>فونت یکان‌باخ، SVG های دست‌ساز.</p>'),
      ('sitemap','نقشه سایت','about','<h2>نقشه سایت 🗺️</h2><p>همه صفحات در یک نگاه.</p>'),
      ('changelog','تغییرات','about','<h2>تغییرات 📝</h2><p>نسخه ۲.۰ با CSS-only لودر.</p>'),
      ('roadmap','نقشه راه','about','<h2>نقشه راه 🛣️</h2><p>صفحات بیشتر، محصولات بیشتر، خنده بیشتر.</p>'),
      ('sponsors','اسپانسرها','about','<h2>اسپانسرها 💚</h2><p>بادمجون‌های طلایی.</p>'),
      ('contribute','مشارکت','about','<h2>مشارکت 🤲</h2><p>ایده‌هات رو باهامون در میون بذار.</p>'),
      ('guidelines','قوانین جامعه','about','<h2>قوانین جامعه 📘</h2><p>احترام، خنده، بادمجون.</p>'),
      ('api','مستندات API','about','<h2>API 🔌</h2><p>شوخی کردیم، API نداریم.</p>'),
      ('status','وضعیت سایت','about','<h2>وضعیت 🟢</h2><p>همه چیز آنلاین است.</p>'),
      ('security','امنیت','about','<h2>امنیت 🔒</h2><p>هیچ داده‌ای ذخیره نمی‌شه.</p>'),
      ('brand','منابع برند','about','<h2>منابع برند 🎨</h2><p>رنگ‌ها: #c6ff00 سبز گسلایت.</p>'),
    ]
    for slug,title,act,body in EXTRA:
        doc_page(slug,title,act,[{'t':'خانه','h':''},{'t':None}],body)

    # Blog posts (depth=2)
    posts=[
      ('behind','پشت صحنه ساخت سایت','۲۲ آبان','چطور در چند شب این سایت ساخته شد؟'),
      ('wall','چرا دیوار میم شد؟','۱۵ آبان','تحلیل طنز یکی از خنده‌دارترین ویدیوها.'),
      ('army','لشکر ۲۰۰۰ نفری','۱۰ آبان','تاریخچه جامعه هواداران.'),
      ('airplane','چرا هوافضا؟','۲ آبان','مسیر مهندس هوافضا.'),
      ('germany','مهدی و آلمان','۲۵ مهر','شایعه رفتن به آلمان.'),
      ('editor','درآمد ادیتورها','۲۰ مهر','درآمد ادیتورها چطوریه؟'),
      ('red','عینک قرمز','۱۵ مهر','چرا عینک قرمز آیکونیک شد 🕶️'),
      ('lime','سبز لیمویی','۱۰ مهر','داستان رنگ برند گسلایت.'),
    ]
    blog_list='<div class="grid-p" style="grid-template-columns:repeat(auto-fill,minmax(300px,1fr))">'
    for slug,t,d,ex in posts:
        blog_list+=f'<a class="post-card" href="{slug}/" data-link><div class="date">{d}</div><h3>{t}</h3><p>{ex}</p></a>'
    blog_list+='</div>'
    write('blog/index.html', page('وبلاگ','blog',[{'t':'خانه','h':''},{'t':None}],f'<h1 class="pg-title">وبلاگ</h1><p class="pg-lede">نوشته‌های طنز و پشت صحنه.</p>{blog_list}','../'))
    for slug,t,d,ex in posts:
        body=f'<div class="notice">این پست جنبه طنز داره.</div><div class="date" style="color:var(--fg3);font-size:12px;letter-spacing:.1em;margin-bottom:10px">{d}</div><h2>{t}</h2>'
        for _ in range(5):
            body+=f'<p style="margin-top:14px">{ex} لشکر بادمجون هر روز بزرگ‌تر از دیروز شده و این باعث افتخاره. همه چیز از یک ویدیوی ساده شروع شد و حالا به یک کلچر تبدیل شده.</p>'
        body+='<h3>نتیجه‌گیری</h3><p>مهدی بخشی از کمدی اینترنتی این نسله.</p>'
        write(f'blog/{slug}/index.html', page(t,'blog',[{'t':'خانه','h':''},{'t':'وبلاگ','h':'blog/'},{'t':None}],f'<div class="doc">{body}</div>','../../'))

    # 404
    nf='''<div class="empty"><div class="big">💀</div>
    <h2 style="font-size:32px;font-weight:700;margin-bottom:10px">404 — اینجا بن شدی!</h2>
    <p>همونطور که مهدی از دیوار بن شد، تو هم از این صفحه بن شدی 🤣</p>
    <a class="btn p" href="../" data-link style="margin-top:20px;display:inline-flex">برگرد به خانه ←</a></div>'''
    write('404/index.html', page('404','home',None,nf,'../'))
    with open('404.html','w',encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n<html><head><meta charset="UTF-8"><script>location.replace("/");</script></head><body></body></html>')

if __name__=='__main__':
    build_all()
    # Quick verification
    import glob
    pages=glob.glob('**/index.html',recursive=True)
    print(f'Built {len(pages)} pages.')
