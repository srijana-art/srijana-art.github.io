#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds every page of srijana-art.github.io, in English and German.

    python3 tools/build_site.py           # writes into build/
    OUT=. python3 tools/build_site.py     # writes in place

English pages live at the site root, German ones under de/. Each page declares
its counterpart with hreflang so search engines treat them as one document in
two languages rather than as duplicates.

All copy lives in tools/lang_data.py — edit there, not in the generated HTML.
"""
import os, sys, html, json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lang_data import ART, ORDER, S, PAGE_FILES

OUT = os.environ.get("OUT", "build")
SITE = "https://srijana-art.github.io/"
EMAIL = "srijana.art.gallery@gmail.com"
INSTA = "https://www.instagram.com/srijana.art.gallery/"
ETSY = "https://www.etsy.com/shop/SrijanaArtGallery"
KW_FEST = "https://www.markkleeberg.de/kunstwinkelfest"
KW_AUCTION_HOUSE = "https://auktion.ikv-fester.de/"
GO_LISTING = "https://rausgegangen.de/en/events/kunstmarkt-227/"

# Video: basename of images/video/<name>.mp4 and .jpg. None hides the section.
VIDEO = "kunstwinkel"
VIDEO_W, VIDEO_H = 1080, 1920

EXHIBITED = {25: "kunstwinkel"}   # artwork id -> page key


def esc(s):
    return html.escape(str(s), quote=True)


class Ctx:
    """Everything that differs between the two language trees."""

    def __init__(self, lang):
        self.lang = lang
        self.t = S[lang]
        # German pages sit one directory deeper, so assets need a ../ prefix
        self.base = "" if lang == "en" else "../"

    def page(self, key):
        """Relative href to another page in the same language."""
        en_file, de_file = PAGE_FILES[key]
        return en_file if self.lang == "en" else de_file

    def other(self, key):
        """Relative href to this same page in the other language."""
        en_file, de_file = PAGE_FILES[key]
        return ("de/" + de_file) if self.lang == "en" else ("../" + en_file)

    def asset(self, path):
        return self.base + path


# --------------------------------------------------------------------- chrome
def head(c, key, title, desc, nav_current=""):
    en_file, de_file = PAGE_FILES[key]
    t = c.t
    return f"""<!DOCTYPE html>
<html lang="{t['html_lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="alternate" hreflang="en" href="{SITE}{en_file}">
<link rel="alternate" hreflang="de" href="{SITE}de/{de_file}">
<link rel="alternate" hreflang="x-default" href="{SITE}{en_file}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{'en_GB' if c.lang == 'en' else 'de_DE'}">
<meta property="og:image" content="{SITE}images/thumbs/art25.jpg">
<link rel="stylesheet" href="{c.asset('css/site.css')}">
<link rel="preload" as="font" type="font/woff2" crossorigin href="{c.asset('fonts/inter-latin-wght-normal.woff2')}">
<link rel="preload" as="font" type="font/woff2" crossorigin href="{c.asset('fonts/fraunces-latin-wght-normal.woff2')}">
<meta name="theme-color" content="#faf6f0" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#15120e" media="(prefers-color-scheme: dark)">
<script>
/* Applied before first paint so the page never flashes the wrong theme.
   An explicit choice wins; otherwise follow the operating system. */
(function () {{
  try {{
    var saved = localStorage.getItem('theme');
    var theme = (saved === 'light' || saved === 'dark') ? saved
      : (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
  }} catch (e) {{
    document.documentElement.setAttribute('data-theme', 'light');
  }}
}})();
</script>
</head>
<body>
<a class="skip-link" href="#main">{esc(t['skip'])}</a>
{nav(c, key, nav_current)}
<main id="main">
"""


def nav(c, key, current):
    t = c.t
    other_lang = 'de' if c.lang == 'en' else 'en'

    def cls(name):
        return ' class="current"' if current == name else ""

    return f"""<header class="site-nav">
  <div class="nav-inner">
    <a class="brand" href="{c.page('index')}">Srijana<span>.</span></a>
    <nav class="links">
      <a href="{c.page('index')}#about"{cls('about')}>{esc(t['nav_about'])}</a>
      <a href="{c.page('index')}#gallery"{cls('gallery')}>{esc(t['nav_gallery'])}</a>
      <a href="{c.page('exhibitions')}"{cls('exhibitions')}>{esc(t['nav_exh'])}</a>
      <a href="{c.page('index')}#contact"{cls('contact')}>{esc(t['nav_contact'])}</a>
    </nav>
    <div class="nav-tools">
      <a class="lang-switch" href="{c.other(key)}" hreflang="{other_lang}" lang="{other_lang}"
         title="{esc(t['lang_switch_label'])}" aria-label="{esc(t['lang_switch_label'])}">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"
             stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <circle cx="12" cy="12" r="9.2"></circle>
          <path d="M2.8 12h18.4M12 2.8a15 15 0 0 1 0 18.4M12 2.8a15 15 0 0 0 0 18.4"></path>
        </svg>
        <span>{esc(t['lang_switch_name'])}</span>
      </a>
      <button class="theme-toggle" id="theme-toggle" type="button"
              aria-label="{esc(t['theme_label'])}" title="{esc(t['theme_label'])}">
        <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"
             stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>
        <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"
             stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <circle cx="12" cy="12" r="4.2"></circle>
          <path d="M12 1.6v2.4M12 20v2.4M4.2 4.2l1.7 1.7M18.1 18.1l1.7 1.7M1.6 12h2.4M20 12h2.4M4.2 19.8l1.7-1.7M18.1 5.9l1.7-1.7"></path>
        </svg>
      </button>
    </div>
  </div>
</header>"""


def contact_section(c):
    t = c.t
    subj = 'Painting%20enquiry' if c.lang == 'en' else 'Bildanfrage'
    return f"""
<section id="contact">
  <div class="wrap">
    <div class="contact-box">
      <h2>{t['contact_h']}</h2>
      <p>{esc(t['contact_p'])}</p>
      <a class="contact-email" href="mailto:{EMAIL}">{EMAIL}</a>
      <div class="contact-links">
        <a href="mailto:{EMAIL}?subject={subj}" class="btn btn-solid">{esc(t['contact_btn'])}</a>
        <a href="{INSTA}" target="_blank" rel="noopener" class="btn btn-outline">@srijana.art.gallery</a>
        <a href="{ETSY}" target="_blank" rel="noopener" class="btn btn-outline">{esc(t['contact_prints'])}</a>
      </div>
    </div>
  </div>
</section>"""


def footer(c, include_contact=True):
    t = c.t
    contact = contact_section(c) if include_contact else ""
    return f"""{contact}
</main>
<footer>
  <div class="wrap">
    <div class="footer-links">
      <a href="{c.page('index')}">{esc(t['foot_home'])}</a>
      <a href="{c.page('exhibitions')}">{esc(t['foot_exh'])}</a>
      <a href="mailto:{EMAIL}">{esc(t['foot_email'])}</a>
      <a href="{c.page('impressum')}">Impressum</a>
      <a href="{c.page('datenschutz')}">Datenschutz</a>
    </div>
    &copy; <span id="year">2026</span> Srijana GS. {esc(t['foot_rights'])}
  </div>
</footer>
<script>
(function () {{
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  var btn = document.getElementById('theme-toggle');
  if (!btn) return;
  var root = document.documentElement;
  function sync() {{
    btn.setAttribute('aria-pressed', root.getAttribute('data-theme') === 'dark' ? 'true' : 'false');
  }}
  sync();
  btn.addEventListener('click', function () {{
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try {{ localStorage.setItem('theme', next); }} catch (e) {{}}
    sync();
  }});
  // Follow the OS only while the visitor has not made a choice of their own.
  if (window.matchMedia) {{
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    var onChange = function (e) {{
      try {{ if (localStorage.getItem('theme')) return; }} catch (err) {{}}
      root.setAttribute('data-theme', e.matches ? 'dark' : 'light');
      sync();
    }};
    if (mq.addEventListener) mq.addEventListener('change', onChange);
    else if (mq.addListener) mq.addListener(onChange);
  }}
}})();
</script>
"""


# ------------------------------------------------------------------ lightbox
def lightbox_markup(c):
    t = c.t
    return f"""
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="{esc(t['viewer'])}">
  <button class="lb-btn lightbox-close" id="lb-close" aria-label="{esc(t['lb_close'])}">&times;</button>
  <button class="lb-btn lightbox-prev" id="lb-prev" aria-label="{esc(t['lb_prev'])}">&#8249;</button>
  <button class="lb-btn lightbox-next" id="lb-next" aria-label="{esc(t['lb_next'])}">&#8250;</button>
  <div class="lightbox-content">
    <img id="lightbox-img" src="" alt="">
    <div class="lightbox-info">
      <strong id="lightbox-title"></strong>
      <span class="medium" id="lightbox-medium"></span>
      <p id="lightbox-desc"></p>
      <div class="lightbox-actions">
        <a class="btn btn-solid" id="lb-enquire" href="#">{esc(t['enquire'])}</a>
        <a class="btn btn-outline hidden" id="lb-exhibition" href="#">{esc(t['see_exhibition'])}</a>
      </div>
    </div>
  </div>
  <div class="lightbox-counter" id="lightbox-counter"></div>
</div>
"""


MAIL_TEMPLATES = {
    "en": {
        "subject": 'Enquiry: "{t}"',
        "body": ('Hello Srijana,\n\n'
                 'I saw "{t}" ({m}) on your website and would like to know more.\n\n'
                 'Could you tell me:\n'
                 '  • the price\n'
                 '  • the size, and whether it is framed\n'
                 '  • whether it can be shipped, and roughly what that would cost\n\n'
                 'Thank you,\n'),
    },
    "de": {
        "subject": 'Anfrage: „{t}“',
        "body": ('Hallo Srijana,\n\n'
                 'ich habe „{t}“ ({m}) auf Ihrer Website gesehen und hätte gern mehr Informationen.\n\n'
                 'Könnten Sie mir sagen:\n'
                 '  • den Preis\n'
                 '  • die Maße, und ob das Bild gerahmt ist\n'
                 '  • ob ein Versand möglich ist und was er ungefähr kosten würde\n\n'
                 'Vielen Dank,\n'),
    },
}

GALLERY_JS = r"""
<script>
(function () {
  var EMAIL = '%EMAIL%';
  var MAIL  = %MAIL%;   // language-specific enquiry template
  var cards    = Array.prototype.slice.call(document.querySelectorAll('.art-card'));
  var lightbox = document.getElementById('lightbox');
  if (!lightbox || !cards.length) return;
  var lbImg    = document.getElementById('lightbox-img');
  var enquire  = document.getElementById('lb-enquire');
  var exhLink  = document.getElementById('lb-exhibition');
  var current  = -1;
  var lastFocus = null;

  // iOS Safari does not honour overflow:hidden on <body>, so the page is
  // pinned with position:fixed and the scroll position restored on close.
  var scrollY = 0;
  function lockScroll() {
    scrollY = window.pageYOffset || document.documentElement.scrollTop || 0;
    document.body.style.top = (-scrollY) + 'px';
    document.body.classList.add('no-scroll');
  }
  function unlockScroll() {
    document.body.classList.remove('no-scroll');
    document.body.style.top = '';
    window.scrollTo(0, scrollY);
  }

  function visibleCards() {
    return cards.filter(function (c) { return !c.classList.contains('hidden'); });
  }

  // Prefilled enquiry email, so the visitor never faces a blank message.
  function mailtoFor(card) {
    var title = card.dataset.title, medium = card.dataset.medium;
    return 'mailto:' + EMAIL +
      '?subject=' + encodeURIComponent(MAIL.subject.split('{t}').join(title)) +
      '&body='    + encodeURIComponent(MAIL.body.split('{t}').join(title).split('{m}').join(medium));
  }

  function show(card) {
    var list = visibleCards();
    var i = list.indexOf(card);
    if (i === -1) return;
    current = i;
    lbImg.src = card.dataset.full;
    lbImg.alt = card.querySelector('img').alt;
    document.getElementById('lightbox-title').textContent  = card.dataset.title;
    document.getElementById('lightbox-medium').textContent = card.dataset.medium;
    document.getElementById('lightbox-desc').textContent   = card.dataset.desc;
    document.getElementById('lightbox-counter').textContent = (i + 1) + ' / ' + list.length;
    enquire.href = mailtoFor(card);
    if (card.dataset.exhibition) {
      exhLink.href = card.dataset.exhibition;
      exhLink.classList.remove('hidden');
    } else {
      exhLink.classList.add('hidden');
    }
  }

  function open(card) {
    lastFocus = document.activeElement;
    show(card);
    lightbox.classList.add('open');
    lockScroll();
    document.getElementById('lb-close').focus();
  }
  function close() {
    lightbox.classList.remove('open');
    unlockScroll();
    lbImg.src = '';
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  function step(delta) {
    var list = visibleCards();
    if (!list.length) return;
    show(list[(current + delta + list.length) % list.length]);
  }

  cards.forEach(function (card) {
    card.addEventListener('click', function () { open(card); });
    card.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(card); }
    });
  });

  document.getElementById('lb-close').addEventListener('click', close);
  document.getElementById('lb-prev').addEventListener('click', function (e) { e.stopPropagation(); step(-1); });
  document.getElementById('lb-next').addEventListener('click', function (e) { e.stopPropagation(); step(1); });

  lightbox.addEventListener('click', function (e) {
    if (e.target === this || e.target.classList.contains('lightbox-content')) close();
  });
  document.addEventListener('keydown', function (e) {
    if (!lightbox.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') step(-1);
    else if (e.key === 'ArrowRight') step(1);
  });

  var touchX = null;
  lightbox.addEventListener('touchstart', function (e) { touchX = e.changedTouches[0].clientX; }, { passive: true });
  lightbox.addEventListener('touchmove', function (e) { if (e.cancelable) e.preventDefault(); }, { passive: false });
  lightbox.addEventListener('touchend', function (e) {
    if (touchX === null) return;
    var dx = e.changedTouches[0].clientX - touchX;
    if (Math.abs(dx) > 55) step(dx < 0 ? 1 : -1);
    touchX = null;
  }, { passive: true });

  document.querySelectorAll('.filter-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      document.querySelectorAll('.filter-btn').forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      var filter = btn.dataset.filter;
      cards.forEach(function (card) {
        card.classList.toggle('hidden', !(filter === 'all' || card.dataset.cat === filter));
      });
    });
  });
})();
</script>
"""


def gallery_js(c):
    return (GALLERY_JS
            .replace('%EMAIL%', EMAIL)
            .replace('%MAIL%', json.dumps(MAIL_TEMPLATES[c.lang], ensure_ascii=False)))


PHOTO_JS = r"""
<script>
(function () {
  var figs = Array.prototype.slice.call(document.querySelectorAll('#photo-strip figure'));
  var lb = document.getElementById('lightbox');
  if (!lb || !figs.length) return;
  var img = document.getElementById('lightbox-img'), i = -1, lastFocus = null;

  var scrollY = 0;
  function lockScroll() {
    scrollY = window.pageYOffset || document.documentElement.scrollTop || 0;
    document.body.style.top = (-scrollY) + 'px';
    document.body.classList.add('no-scroll');
  }
  function unlockScroll() {
    document.body.classList.remove('no-scroll');
    document.body.style.top = '';
    window.scrollTo(0, scrollY);
  }

  function show(n) {
    i = (n + figs.length) % figs.length;
    var el = figs[i].querySelector('img');
    img.src = el.dataset.full; img.alt = el.alt;
    document.getElementById('lightbox-desc').textContent = el.alt;
    document.getElementById('lightbox-counter').textContent = (i + 1) + ' / ' + figs.length;
  }
  function open(n) { lastFocus = document.activeElement; show(n); lb.classList.add('open');
                     lockScroll(); document.getElementById('lb-close').focus(); }
  function close() { lb.classList.remove('open'); unlockScroll();
                     img.src = ''; if (lastFocus && lastFocus.focus) lastFocus.focus(); }

  figs.forEach(function (f, n) {
    f.setAttribute('tabindex', '0'); f.setAttribute('role', 'button');
    f.addEventListener('click', function () { open(n); });
    f.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(n); }
    });
  });
  document.getElementById('lb-close').addEventListener('click', close);
  document.getElementById('lb-prev').addEventListener('click', function (e) { e.stopPropagation(); show(i - 1); });
  document.getElementById('lb-next').addEventListener('click', function (e) { e.stopPropagation(); show(i + 1); });
  lb.addEventListener('click', function (e) {
    if (e.target === this || e.target.classList.contains('lightbox-content')) close();
  });
  document.addEventListener('keydown', function (e) {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') show(i - 1);
    else if (e.key === 'ArrowRight') show(i + 1);
  });
})();
</script>
"""


# ----------------------------------------------------------------- index page
def gallery_cards(c):
    out = []
    for n in ORDER:
        a = ART[n]
        title, medium, desc, alt = a[c.lang]
        badge = exh_attr = ""
        if n in EXHIBITED:
            badge = f'\n        <span class="badge badge-exhibited">{esc(c.t["badge_exhibited"])}</span>'
            exh_attr = f'\n              data-exhibition="{esc(c.page(EXHIBITED[n]))}"'
        out.append(
f'''      <figure class="art-card" data-cat="{a['cat']}" tabindex="0" role="button"
              aria-label="{esc(c.t['view_larger'].replace('{t}', title))}"
              data-full="{c.asset(f'images/web/art{n}.jpg')}"
              data-title="{esc(title)}"
              data-medium="{esc(medium)}"
              data-desc="{esc(desc)}"{exh_attr}>{badge}
        <img src="{c.asset(f'images/thumbs/art{n}.jpg')}" width="{a['w']}" height="{a['h']}"
             loading="lazy" decoding="async" alt="{esc(alt)}">
        <figcaption class="art-caption"><strong>{esc(title)}</strong>{esc(medium)}</figcaption>
      </figure>''')
    return "\n\n".join(out)


def counts():
    c = {"portrait": 0, "landscape": 0, "still-life": 0}
    for n in ORDER:
        c[ART[n]["cat"]] += 1
    return c


def build_index(c):
    t, n = c.t, counts()
    filters = [f'<button class="filter-btn active" data-filter="all">{esc(t["filter_all"])} '
               f'<span class="count">{len(ORDER)}</span></button>']
    for cat in ("portrait", "landscape", "still-life"):
        filters.append(f'<button class="filter-btn" data-filter="{cat}">{esc(t["cat"][cat])} '
                       f'<span class="count">{n[cat]}</span></button>')

    return head(c, "index", t["meta_title"], t["meta_desc"], "gallery") + f"""
<section class="hero">
  <div class="wrap">
    <div class="kicker">{esc(t['hero_kicker'])}</div>
    <h1>Srijana GS</h1>
    <p class="lede">{esc(t['hero_lede'])}</p>
    <div class="cta-row">
      <a href="#gallery" class="btn btn-solid">{esc(t['hero_cta1'])}</a>
      <a href="{c.page('exhibitions')}" class="btn btn-outline">{esc(t['hero_cta2'])}</a>
    </div>
  </div>
</section>

<section id="about">
  <div class="wrap about-grid">
    <div class="about-portrait">
      <img src="{c.asset('images/web/art1.jpg')}" width="1275" height="1800" alt="{esc(ART[1][c.lang][3])}">
    </div>
    <div class="about-text">
      <div class="section-head" style="text-align:left; margin: 0 0 20px;">
        <div class="kicker">{esc(t['about_kicker'])}</div>
        <h2 style="margin-bottom: 0;">{esc(t['about_h'])}</h2>
      </div>
      <p>{esc(t['about_p1'])}</p>
      <p>{esc(t['about_p2'])}</p>
      <div class="quote">{esc(t['about_quote'])}</div>
      <p>{esc(t['about_p3'])}</p>
      <div class="about-facts">
        <div class="fact"><span class="num">{len(ORDER)}</span><span class="label">{esc(t['fact1'])}</span></div>
        <div class="fact"><span class="num">{esc(t['fact2_n'])}</span><span class="label">{esc(t['fact2'])}</span></div>
        <div class="fact"><span class="num">{esc(t['fact3_n'])}</span><span class="label">{esc(t['fact3'])}</span></div>
      </div>
    </div>
  </div>
</section>

<section id="gallery" style="background: var(--paper-warm);">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">{esc(t['gal_kicker'])}</div>
      <h2>{esc(t['gal_h'])}</h2>
      <p>{esc(t['gal_p'])}</p>
    </div>

    <div class="avail-note">{t['avail'].format(etsy=ETSY)}</div>

    <div class="gallery-filter">
      {chr(10).join('      ' + f for f in filters).strip()}
    </div>

    <div class="gallery-grid">
{gallery_cards(c)}
    </div>
  </div>
</section>
{film_section(c)}
<section id="process" class="process">
  <div class="wrap process-grid">
    <div class="section-head" style="margin-bottom: 28px;">
      <div class="kicker">{esc(t['proc_kicker'])}</div>
      <h2 style="margin-bottom: 0;">{esc(t['proc_h'])}</h2>
    </div>
    <div class="process-text">
      <p>{esc(t['proc_q1'])}</p>
      <p>{esc(t['proc_q2'])}</p>
      <p style="color: var(--ink); font-style: normal; font-size: 1rem;">{esc(t['proc_sig'])}</p>
    </div>
  </div>
</section>
""" + footer(c) + lightbox_markup(c) + gallery_js(c) + "\n</body>\n</html>\n"


def film_section(c):
    """Only rendered on the Kunstwinkel page; kept here for the index if wanted."""
    return ""


# ------------------------------------------------------------------ exhibitions
def build_exhibitions(c):
    t = c.t
    return head(c, "exhibitions", t["exh_title"], t["exh_desc"], "exhibitions") + f"""
<section class="event-hero">
  <div class="wrap">
    <div class="kicker">{t['exh_kicker']}</div>
    <h1>{esc(t['exh_h'])}</h1>
    <p class="lede">{esc(t['exh_lede'])}</p>
  </div>
</section>

<section style="padding-top: 20px;">
  <div class="wrap">
    <div class="exh-list">

      <a class="exh-card" href="{c.page('garageost')}" style="text-decoration:none">
        <img src="{c.asset('images/events/garage-ost-sm.jpg')}" alt="{esc(t['go_poster_alt'])}" loading="lazy">
        <div class="body">
          <span class="status-pill status-upcoming">{esc(t['pill_up'])}</span>
          <div class="when">{esc(t['card_go_when'])}</div>
          <h3>{esc(t['card_go_h'])}</h3>
          <p>{esc(t['card_go_p'])}</p>
          <span class="go">{t['go_details']}</span>
        </div>
      </a>

      <a class="exh-card" href="{c.page('kunstwinkel')}" style="text-decoration:none">
        <img src="{c.asset('images/events/kw-board-sm.jpg')}" alt="{esc(t['kw_alt_board'])}" loading="lazy">
        <div class="body">
          <span class="status-pill status-live">{esc(t['pill_live'])}</span>
          <div class="when">{esc(t['card_kw_when'])}</div>
          <h3>{esc(t['card_kw_h'])}</h3>
          <p>{esc(t['card_kw_p'])}</p>
          <span class="go">{t['go_details_bid']}</span>
        </div>
      </a>

    </div>

    <div class="callout" style="margin-top: 44px;">
      <p>{t['exh_cta'].format(email=EMAIL)}</p>
    </div>
  </div>
</section>
""" + footer(c, include_contact=False) + "\n</body>\n</html>\n"


# ------------------------------------------------------------------ Kunstwinkel
def film_block(c):
    """The artist film. Rendered only when VIDEO points at real files."""
    if not VIDEO:
        return ""
    t = c.t
    return f"""
<section class="film">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">{esc(t['kw_film_kicker'])}</div>
      <h2>{esc(t['kw_film_h'])}</h2>
      <p>{esc(t['kw_film_p'])}</p>
    </div>
    <div class="film-frame">
      <video controls playsinline preload="none" width="{VIDEO_W}" height="{VIDEO_H}"
             poster="{c.asset(f'images/video/{VIDEO}.jpg')}">
        <source src="{c.asset(f'images/video/{VIDEO}.mp4')}" type="video/mp4">
        <p>{esc(t['kw_film_fallback'])}
           <a href="{c.asset(f'images/video/{VIDEO}.mp4')}">{esc(t['kw_film_download'])}</a>.</p>
      </video>
    </div>
    <p class="film-caption">{esc(t['kw_film_cap'])}</p>
  </div>
</section>"""


def build_kunstwinkel(c):
    t = c.t
    photos = [("kw-board", t['kw_alt_board']),
              ("kw-artist-wall", t['kw_alt_artist_wall']),
              ("kw-panel-detail", t['kw_alt_detail']),
              ("kw-wall-lettering", t['kw_alt_lettering']),
              ("kw-artist", t['kw_alt_artist']),
              ("kw-board-angle", t['kw_alt_angle']),
              ("kw-wall-wide", t['kw_alt_wide']),
              ("kw-artist-full", t['kw_alt_artist_full'])]
    strip = "\n".join(
        f'''      <figure><img src="{c.asset(f'images/events/{n}-sm.jpg')}" '''
        f'''data-full="{c.asset(f'images/events/{n}.jpg')}" '''
        f'''loading="lazy" decoding="async" alt="{esc(a)}"></figure>'''
        for n, a in photos)

    art_title, art_medium, _, art_alt = ART[25][c.lang]

    return head(c, "kunstwinkel", t["kw_title"], t["kw_desc"], "exhibitions") + f"""
<section class="event-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="{c.page('index')}">{esc(t['breadcrumb_home'])}</a> · <a href="{c.page('exhibitions')}">{esc(t['nav_exh'])}</a></div>
    <span class="status-pill status-live">{esc(t['kw_pill'])}</span>
    <h1>{esc(t['kw_h'])}</h1>
    <p class="lede">{t['kw_lede']}</p>
  </div>
</section>

<section style="padding-top: 30px;">
  <div class="wrap event-grid">

    <div>
      <div class="featured-work">
        <img src="{c.asset('images/web/art25.jpg')}" alt="{esc(art_alt)}" loading="lazy">
        <div class="body">
          <h3>{esc(art_title)}</h3>
          <span class="medium">{esc(art_medium)}</span>
          <p>{esc(t['kw_work_p'])}</p>
          <a class="btn btn-outline" href="{c.page('index')}#gallery">{esc(t['kw_see_gallery'])}</a>
        </div>
      </div>
    </div>

    <div>
      <h2 style="margin-top:0;">{esc(t['kw_how_h'])}</h2>
      <p style="color: var(--ink-soft);">{esc(t['kw_how_p'])}</p>

      <table class="facts-table">
        <tr><th>{esc(t['kw_f_exh'])}</th><td>{esc(t['kw_f_exh_v'])}</td></tr>
        <tr><th>{esc(t['kw_f_motto'])}</th><td>&bdquo;Mein Bild f&uuml;r Dich&ldquo;</td></tr>
        <tr><th>{esc(t['kw_f_work'])}</th><td>{esc(art_title)}</td></tr>
        <tr><th>{esc(t['kw_f_unveiled'])}</th><td>{esc(t['kw_f_unveiled_v'])}</td></tr>
        <tr><th>{esc(t['kw_f_until'])}</th><td>{esc(t['kw_f_until_v'])}</td></tr>
        <tr><th>{esc(t['kw_f_where'])}</th><td>Rathausstra&szlig;e 23, 04416 Markkleeberg</td></tr>
        <tr><th>{esc(t['kw_f_selected'])}</th><td>{esc(t['kw_f_selected_v'])}</td></tr>
        <tr><th>{esc(t['kw_f_org'])}</th><td><a href="{KW_FEST}" target="_blank" rel="noopener">{esc(t['kw_f_org_v'])}</a></td></tr>
      </table>

      <div class="callout">
        <p><strong>{esc(t['kw_bid_h'])}</strong> {esc(t['kw_bid_p1'])}</p>
        <p>{esc(t['kw_bid_p2'])}</p>
        <p>
          <a class="btn btn-outline" href="{KW_FEST}" target="_blank" rel="noopener">{esc(t['kw_bid_b1'])}</a>
          <a class="btn btn-outline" href="{KW_AUCTION_HOUSE}" target="_blank" rel="noopener">{esc(t['kw_bid_b2'])}</a>
        </p>
        <!-- TODO 2027: replace the two buttons above with the direct lot URL, e.g.
             <a class="btn btn-solid" href="https://auktion.ikv-fester.de/...">Place a bid on this painting</a> -->
      </div>

      <p style="color: var(--ink-soft);">{t['kw_alt_p'].format(gallery=c.page('index'), email=EMAIL)}</p>
    </div>

  </div>
</section>
{film_block(c)}
<section style="background: var(--paper-warm);">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">{esc(t['kw_film_kicker'])}</div>
      <h2>{esc(t['kw_photos_h'])}</h2>
      <p>{esc(t['kw_photos_p'])}</p>
    </div>
    <div class="photo-strip" id="photo-strip">
{strip}
    </div>
  </div>
</section>
""" + footer(c, include_contact=False) + f"""
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="{esc(t['photo_viewer'])}">
  <button class="lb-btn lightbox-close" id="lb-close" aria-label="{esc(t['lb_close'])}">&times;</button>
  <button class="lb-btn lightbox-prev" id="lb-prev" aria-label="{esc(t['lb_photo_prev'])}">&#8249;</button>
  <button class="lb-btn lightbox-next" id="lb-next" aria-label="{esc(t['lb_photo_next'])}">&#8250;</button>
  <div class="lightbox-content">
    <img id="lightbox-img" src="" alt="">
    <div class="lightbox-info"><p id="lightbox-desc"></p></div>
  </div>
  <div class="lightbox-counter" id="lightbox-counter"></div>
</div>
""" + PHOTO_JS + "\n</body>\n</html>\n"


# ------------------------------------------------------------------ Garage Ost
def build_garage_ost(c):
    t = c.t
    return head(c, "garageost", t["go_title"], t["go_desc"], "exhibitions") + f"""
<section class="event-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="{c.page('index')}">{esc(t['breadcrumb_home'])}</a> · <a href="{c.page('exhibitions')}">{esc(t['nav_exh'])}</a></div>
    <span class="status-pill status-upcoming">{esc(t['pill_up'])}</span>
    <h1>{esc(t['go_h'])}</h1>
    <p class="lede">{esc(t['go_lede'])}</p>
  </div>
</section>

<section style="padding-top: 30px;">
  <div class="wrap event-grid">

    <div>
      <figure class="event-poster">
        <img src="{c.asset('images/events/garage-ost.jpg')}" width="1200" height="675"
             alt="{esc(t['go_poster_alt'])}" loading="lazy">
        <figcaption>{esc(t['go_poster_credit'])}</figcaption>
      </figure>

      <h2 style="margin-top:0;">{esc(t['go_come_h'])}</h2>
      <p style="color: var(--ink-soft);">{esc(t['go_p1'])}</p>
      <p style="color: var(--ink-soft);">{t['go_p2'].format(gallery=c.page('index'), email=EMAIL)}</p>

      <table class="facts-table">
        <tr><th>{esc(t['go_f_event'])}</th><td>{esc(t['go_f_event_v'])}</td></tr>
        <tr><th>{esc(t['go_f_date'])}</th><td>{esc(t['go_f_date_v'])}</td></tr>
        <tr><th>{esc(t['go_f_time'])}</th><td>{esc(t['go_f_time_v'])}</td></tr>
        <tr><th>{esc(t['go_f_venue'])}</th><td>Garage Ost</td></tr>
        <tr><th>{esc(t['go_f_addr'])}</th><td>{esc(t['go_f_addr_v'])}</td></tr>
        <tr><th>{esc(t['go_f_entry'])}</th><td>{esc(t['go_f_entry_v'])}</td></tr>
        <tr><th>{esc(t['go_f_pay'])}</th><td>{esc(t['go_f_pay_v'])}</td></tr>
      </table>

      <!-- TODO before publishing:
           - confirm the date/time against the rausgegangen.de listing
           - swap images/events/garage-ost.jpg for the organiser's own event image
             (only if they allow reuse) or a photo of her table after the event -->

      <div class="callout">
        <p>{t['go_note'].format(insta=INSTA, email=EMAIL, listing=GO_LISTING)}</p>
      </div>
    </div>

    <div>
      <div class="featured-work">
        <img src="{c.asset('images/web/art16.jpg')}" alt="{esc(ART[16][c.lang][3])}" loading="lazy">
        <div class="body">
          <h3>{esc(t['go_table_h'])}</h3>
          <span class="medium">{esc(t['go_table_medium'])}</span>
          <p>{esc(t['go_table_p'])}</p>
          <a class="btn btn-outline" href="{c.page('index')}#gallery">{esc(t['go_browse'])}</a>
        </div>
      </div>
    </div>

  </div>
</section>
""" + footer(c, include_contact=False) + "\n</body>\n</html>\n"


# ------------------------------------------------------------------ legal pages
IMPRESSUM_NAME    = "Srijana Gurung Shrestha"
IMPRESSUM_STREET  = "Torgauer Straße 44A"
IMPRESSUM_CITY    = "04315 Leipzig"
IMPRESSUM_COUNTRY = "Deutschland"
IMPRESSUM_PHONE   = "+49 151 56076479"
IMPRESSUM_PHONE_HREF = "+4915156076479"


def build_impressum(c):
    """Legally German in both trees; the English page adds a short summary."""
    t = c.t
    summary = "" if c.lang == "de" else f"""
    <hr>
    <p class="updated">English summary: this is the legal notice required of German
       websites. The artist can be reached at <a href="mailto:{EMAIL}">{EMAIL}</a>.
       All artwork shown on this site remains the property of the artist.</p>"""

    return head(c, "impressum", t["imp_title"], t["imp_desc"]) + f"""
<section>
  <div class="wrap prose">
    <div class="breadcrumb"><a href="{c.page('index')}">{esc(t['breadcrumb_home'])}</a></div>
    <h1>Impressum</h1>
    <p class="updated">Angaben gem&auml;&szlig; &sect; 5 DDG (ehemals &sect; 5 TMG)</p>

    <h2>Diensteanbieter</h2>
    <address>
      {IMPRESSUM_NAME}<br>
      {IMPRESSUM_STREET}<br>
      {IMPRESSUM_CITY}<br>
      {IMPRESSUM_COUNTRY}
    </address>

    <h2>Kontakt</h2>
    <address>
      E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a><br>
      Telefon: <a href="tel:{IMPRESSUM_PHONE_HREF}">{IMPRESSUM_PHONE}</a>
    </address>

    <h2>Verantwortlich f&uuml;r den Inhalt</h2>
    <address>{IMPRESSUM_NAME}, Anschrift wie oben</address>

    <h2>T&auml;tigkeit</h2>
    <p>Selbstst&auml;ndige bildende K&uuml;nstlerin.</p>

    <h2>Umsatzsteuer</h2>
    <p>Als Kleinunternehmerin im Sinne von &sect; 19 UStG wird keine Umsatzsteuer ausgewiesen.
       Eine Umsatzsteuer-Identifikationsnummer nach &sect; 27 a UStG liegt nicht vor.</p>
    <!-- Confirmed against the Finanzamt Leipzig I letter: she is registered as a
         Kleinunternehmerin (§ 19 UStG), self-employed artist, profit determined
         under § 4 Abs. 3 EStG. No USt-IdNr. was issued, so none is listed.
         DO NOT publish the Steuernummer or the persönliche Identifikationsnummer
         here — § 5 DDG asks only for a USt-IdNr., and only if one exists. -->

    <h2>Streitbeilegung</h2>
    <p>Die Europ&auml;ische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit:
       <a href="https://ec.europa.eu/consumers/odr/" target="_blank" rel="noopener">https://ec.europa.eu/consumers/odr/</a>.
       Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer
       Verbraucherschlichtungsstelle teilzunehmen.</p>

    <h2>Urheberrecht</h2>
    <p>S&auml;mtliche auf dieser Website gezeigten Kunstwerke, Abbildungen und Texte sind
       urheberrechtlich gesch&uuml;tzt und verbleiben Eigentum der K&uuml;nstlerin. Eine Vervielf&auml;ltigung,
       Bearbeitung oder Verbreitung &mdash; insbesondere der Bilder der Gem&auml;lde &mdash; bedarf der
       schriftlichen Zustimmung der K&uuml;nstlerin.</p>

    <h2>Haftung f&uuml;r Links</h2>
    <p>Diese Website enth&auml;lt Links zu externen Websites Dritter, auf deren Inhalte wir keinen
       Einfluss haben. F&uuml;r die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter
       oder Betreiber verantwortlich.</p>
{summary}
  </div>
</section>
""" + footer(c, include_contact=False) + "\n</body>\n</html>\n"


def build_datenschutz(c):
    t = c.t
    summary = "" if c.lang == "de" else f"""
    <hr>
    <p class="updated">English summary: this site sets no cookies and runs no analytics.
       It is hosted on GitHub Pages and loads fonts from Google Fonts, both of which see
       your IP address. Contact happens by email only.</p>"""

    return head(c, "datenschutz", t["ds_title"], t["ds_desc"]) + f"""
<section>
  <div class="wrap prose">
    <div class="breadcrumb"><a href="{c.page('index')}">{esc(t['breadcrumb_home'])}</a></div>
    <h1>Datenschutzerkl&auml;rung</h1>
    <p class="updated">Stand: September 2026</p>

    <h2>1. Verantwortliche Stelle</h2>
    <address>
      {IMPRESSUM_NAME}<br>
      {IMPRESSUM_STREET}<br>
      {IMPRESSUM_CITY}<br>
      E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a>
    </address>

    <h2>2. Grundsatz</h2>
    <p>Diese Website ist eine rein statische Seite. Sie setzt <strong>keine Cookies</strong>,
       verwendet <strong>kein Tracking</strong> und <strong>keine Analyse-Werkzeuge</strong>.
       Es gibt kein Kontaktformular &mdash; die Kontaktaufnahme erfolgt ausschlie&szlig;lich &uuml;ber einen
       E-Mail-Link. Die gew&auml;hlte Sprache und die Einstellung f&uuml;r den hellen oder dunklen Modus
       werden ausschlie&szlig;lich lokal im Browser gespeichert und nicht &uuml;bertragen.</p>

    <h2>3. Hosting (GitHub Pages)</h2>
    <p>Diese Website wird von GitHub Pages gehostet, einem Dienst der GitHub, Inc.,
       88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Beim Aufruf der Seite
       werden durch GitHub automatisch Server-Logdaten verarbeitet, insbesondere die
       IP-Adresse, Datum und Uhrzeit des Zugriffs, die aufgerufene Seite, der verwendete
       Browser und das Betriebssystem. Diese Verarbeitung erfolgt zur technischen
       Bereitstellung und Sicherheit der Website auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO
       (berechtigtes Interesse). Weitere Informationen:
       <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" target="_blank" rel="noopener">GitHub Privacy Statement</a>.</p>

    <h2>4. Schriftarten</h2>
    <p>Alle verwendeten Schriftarten werden von diesem Server selbst ausgeliefert. Es besteht
       <strong>keine Verbindung zu Google Fonts</strong> oder zu einem anderen externen
       Schriftarten-Dienst; es werden dabei keine Daten an Dritte &uuml;bertragen.</p>

    <h2>5. Kontaktaufnahme per E-Mail</h2>
    <p>Wenn Sie per E-Mail Kontakt aufnehmen, werden Ihre Angaben zur Bearbeitung der Anfrage
       und f&uuml;r den Fall von Anschlussfragen gespeichert. Rechtsgrundlage ist Art. 6 Abs. 1
       lit. b DSGVO (vorvertragliche Ma&szlig;nahmen) bzw. lit. f DSGVO. Die Daten werden gel&ouml;scht,
       sobald sie f&uuml;r den Zweck nicht mehr erforderlich sind.</p>

    <h2>6. Externe Links</h2>
    <p>Diese Website verlinkt auf Instagram, Etsy sowie die Seiten der Stadt Markkleeberg und
       des Auktionshauses. F&uuml;r die Datenverarbeitung auf diesen Seiten gelten die jeweiligen
       Datenschutzerkl&auml;rungen der Anbieter. Es werden keine Inhalte dieser Dienste direkt in
       diese Website eingebettet; das Video wird von dieser Website selbst ausgeliefert.</p>

    <h2>7. Ihre Rechte</h2>
    <ul>
      <li>Auskunft &uuml;ber die verarbeiteten Daten (Art. 15 DSGVO)</li>
      <li>Berichtigung unrichtiger Daten (Art. 16 DSGVO)</li>
      <li>L&ouml;schung (Art. 17 DSGVO) und Einschr&auml;nkung der Verarbeitung (Art. 18 DSGVO)</li>
      <li>Daten&uuml;bertragbarkeit (Art. 20 DSGVO)</li>
      <li>Widerspruch gegen die Verarbeitung (Art. 21 DSGVO)</li>
      <li>Beschwerde bei einer Aufsichtsbeh&ouml;rde (Art. 77 DSGVO)</li>
    </ul>
    <p>Zur Aus&uuml;bung gen&uuml;gt eine E-Mail an <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
{summary}
  </div>
</section>
""" + footer(c, include_contact=False) + "\n</body>\n</html>\n"


# ------------------------------------------------------------------------ main
BUILDERS = {
    "index": build_index,
    "exhibitions": build_exhibitions,
    "kunstwinkel": build_kunstwinkel,
    "garageost": build_garage_ost,
    "impressum": build_impressum,
    "datenschutz": build_datenschutz,
}


def sitemap():
    urls = []
    for key, (en_file, de_file) in PAGE_FILES.items():
        urls.append(f"{SITE}{en_file}")
        urls.append(f"{SITE}de/{de_file}")
    body = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f'{body}\n</urlset>\n')


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(os.path.join(OUT, "de"), exist_ok=True)
    total = 0
    for lang in ("en", "de"):
        c = Ctx(lang)
        for key, build in BUILDERS.items():
            name = c.page(key)
            path = os.path.join(OUT, name) if lang == "en" else os.path.join(OUT, "de", name)
            content = build(c)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
            total += len(content)
            rel = name if lang == "en" else "de/" + name
            print(f"{rel:36s} {len(content):>7,} bytes")

    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(sitemap())
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
    print(f"\n{total:,} bytes of HTML, plus sitemap.xml and robots.txt")


if __name__ == "__main__":
    main()
