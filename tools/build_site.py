#!/usr/bin/env python3
"""Builds every page of srijana-art.github.io from shared parts."""
import os, html

OUT = os.environ.get("OUT", "build")
EMAIL = "srijana.art.art.gallery@gmail.com"
INSTA = "https://www.instagram.com/srijana.art.gallery/"
ETSY = "https://www.etsy.com/shop/SrijanaArtGallery"
KW_FEST = "https://www.markkleeberg.de/kunstwinkelfest"
KW_AUCTION_HOUSE = "https://auktion.ikv-fester.de/"

def esc(s):
    return html.escape(s, quote=True)

# ----------------------------------------------------------------- artwork data
# (title, category, medium, description, alt, thumb_w, thumb_h)
ART = {
 1:  ("Carried", "portrait", "Watercolour",
      "A painting close to the artist's heart — begun in Thailand and completed in Germany before travelling on to New Zealand for the start of a PhD. “I have carried this painting wherever I go, and each time I see it, it reminds me to keep practicing art.”",
      "Watercolour portrait of a mother carrying her child on her back in a plaid woven wrap", 1275, 1800),
 2:  ("Winter Smile", "portrait", "Watercolour",
      "A child grinning out from under a knitted cap, bundled in red against the snow and the open sky behind.",
      "Watercolour portrait of a smiling child in a knitted hat and red clothing in a snowy landscape", 1275, 1800),
 3:  ("Honey Hunters of Nepal", "portrait", "Acrylic on 180gsm paper, A3",
      "Begun in February 2022 and completed over a year and a half later, referenced from a documentary cover photo by a French journalist. “I was captivated by the intensity in their eyes, the fearless expression on their faces, and their unwavering courage.”",
      "Painting of two honey hunters of Nepal on a rock, one standing with a pole and one crouching", 1275, 1800),
 4:  ("Butter Tea", "portrait", "Acrylic",
      "An older man in saffron pauses over a bowl held in both hands — prayer beads, long hair, and a face weathered by altitude.",
      "Acrylic portrait of an older man in an orange robe drinking from a bowl held in both hands", 1275, 1800),
 5:  ("Tulips in a Glass", "still-life", "Acrylic",
      "Red tulips leaning out of a plain drinking glass, painted loosely against a wash of spring blue.",
      "Acrylic still life of red tulips in a clear glass against a blue background", 1273, 1800),
 6:  ("Waiting", "portrait", "Watercolour & mixed media",
      "The second time the artist has returned to this scene: a goat consoling a child who is home alone, waiting for her mother to return. “I can never get enough of this picture.”",
      "Painting of a young child in a red dress comforted by a white goat in a doorway", 1275, 1800),
 7:  ("Street at Dusk", "landscape", "Watercolour",
      "Tram wires strung across a European street as the evening sky turns coral above the rooftops.",
      "Watercolour of a European city street with tram wires and coral clouds at sunset", 1275, 1800),
 8:  ("Adorned", "portrait", "Acrylic",
      "A portrait built around silver — headdress, choker, and the steady, unblinking gaze beneath them.",
      "Portrait of a woman wearing an ornate silver headdress and choker with dark curled hair", 1275, 1800),
 9:  ("Carrying Rhododendrons", "portrait", "Acrylic on canvas",
      "A girl steadies a doko basket heavy with lali gurans, caught mid-step on the walk home.",
      "Painting of a girl carrying a woven basket filled with red rhododendron branches", 1275, 1800),
 10: ("Evening Sky I", "landscape", "Watercolour",
      "A small study of dusk — lit windows appearing one by one beneath a sky still burning at the edges.",
      "Small watercolour study of a city skyline at sunset with lit windows", 1275, 1800),
 11: ("Evening Sky II", "landscape", "Watercolour",
      "The same hour, painted again — banks of cloud catching fire above a low, darkening skyline.",
      "Watercolour of red and orange sunset clouds above a dark rooftop skyline", 1275, 1800),
 12: ("Corner House", "landscape", "Acrylic",
      "An orange corner block under a big, moving sky — a quiet street painted from an upstairs window.",
      "Acrylic painting of an orange corner building on a street beneath a cloudy blue sky", 1275, 1800),
 13: ("Sky on Fire", "landscape", "Acrylic",
      "A bare winter tree held against a sunset that fills the whole upper half of the paper.",
      "Acrylic painting of a bare tree silhouetted against a fiery red and orange sunset over buildings", 1275, 1800),
 14: ("Milky Way", "landscape", "Watercolour",
      "Pines cut black against the galaxy, with the last of the sunset still glowing along the horizon.",
      "Watercolour of the Milky Way over silhouetted pine trees with a pink horizon", 1275, 1800),
 15: ("In the Doorway", "portrait", "Pastel",
      "Two figures pausing at a threshold, drawn in soft pastel on a sun-warmed ochre wall.",
      "Pastel drawing of a man and a woman in a red headscarf standing beside a dark doorway", 1275, 1800),
 16: ("Laughter", "portrait", "Acrylic on canvas",
      "A woman caught mid-laugh, eyes closed, coral and pearl at her throat — a portrait about joy more than likeness.",
      "Portrait of a laughing woman wearing red coral and white pearl necklaces", 1275, 1800),
 17: ("The Green Dress", "portrait", "Acrylic & watercolour",
      "Embroidery, mirrorwork and silver rendered thread by thread around a calm, direct gaze.",
      "Portrait of a woman in an embroidered green and orange dress with silver jewellery and long braids", 1275, 1800),
 18: ("Red Roofs", "landscape", "Watercolour",
      "Tiled rooftops climbing towards a green copper dome — an old European city seen from above.",
      "Watercolour of red tiled rooftops and a green copper dome in an old European city", 1275, 1800),
 19: ("Two Pots", "still-life", "Watercolour",
      "Pansies and lavender sharing a blue bistro table, painted in a single quiet sitting.",
      "Watercolour of two terracotta pots of pansies and lavender on a blue garden table", 1114, 1241),
 20: ("Poppies, Study", "still-life", "Watercolour sketchbook",
      "A sketchbook study of poppies, made while the artist was studying the work of painter Thomas Braun and his admiration for Monet. “His way of thinking about painting felt honest, generous, and perspective-shifting.”",
      "Watercolour sketchbook study of red poppies and seed heads", 1178, 1187),
 21: ("Window Box", "still-life", "Watercolour",
      "Dark pansies crowding a terracotta trough set into a cool stone window ledge.",
      "Watercolour of purple pansies in a terracotta window box on a stone ledge", 1122, 1170),
 22: ("Home Below the Mountains", "landscape", "Acrylic",
      "A thatched house among banana palms, with the snow peaks standing over the valley behind it.",
      "Acrylic painting of a thatched Nepali house among green palms with snow mountains behind", 1725, 1102),
 23: ("Berries Against the Sky", "still-life", "Acrylic",
      "Looking straight up through a berry-laden branch into a clouded blue — painted from below.",
      "Acrylic painting of red berries and green foliage against a blue and white sky", 1275, 1800),
 24: ("Wildflowers", "still-life", "Watercolour",
      "A handful of garden flowers dropped into a coiled clay vase, loose and unfussed.",
      "Watercolour of small wildflowers in a coiled pink clay vase", 1275, 1800),
 25: ("The Morning Pipe", "portrait", "Acrylic on canvas",
      "An elderly woman draws on her pipe, both hands cupped around it, the whole painting held within one range of warm ochre and rose. This is the work now hanging in the open-air gallery at Am Kunstwinkel in Markkleeberg.",
      "Painting of an elderly woman with grey hair smoking a pipe held in both cupped hands", 1510, 1545),
}

ORDER = [25, 3, 1, 16, 6, 9, 4, 13, 17, 22, 2, 7, 8, 14, 5, 18, 15, 23, 11, 20, 12, 19, 10, 24, 21]

# Works currently on public exhibition -> badge text + link
EXHIBITED = {25: ("On exhibition", "exhibition-kunstwinkel.html")}

CAT_LABEL = {"portrait": "Portraits", "landscape": "Landscapes", "still-life": "Still Life"}


# ----------------------------------------------------------------- page chrome
def head(title, desc, rel_current, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="images/thumbs/art25.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500;9..144,600&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css">
{extra_head}</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{nav(rel_current)}
<main id="main">
"""


def nav(current):
    def cls(name):
        return ' class="current"' if current == name else ""
    return f"""<header class="site-nav">
  <div class="nav-inner">
    <a class="brand" href="index.html" style="color:inherit;text-decoration:none">Srijana<span>.</span></a>
    <nav class="links">
      <a href="index.html#about"{cls('about')}>About</a>
      <a href="index.html#gallery"{cls('gallery')}>Gallery</a>
      <a href="exhibitions.html"{cls('exhibitions')}>Exhibitions</a>
      <a href="index.html#contact"{cls('contact')}>Contact</a>
    </nav>
  </div>
</header>"""


def contact_section():
    return f"""
<section id="contact">
  <div class="wrap">
    <div class="contact-box">
      <h2>Commissions, prices &amp; enquiries</h2>
      <p>Every painting on this site is an original, and most are available. Prices depend on size, medium and whether the piece is framed — write with the title you're interested in and you'll get a quote, usually within a couple of days.</p>
      <a class="contact-email" href="mailto:{EMAIL}">{EMAIL}</a>
      <div class="contact-links">
        <a href="mailto:{EMAIL}?subject=Painting%20enquiry" class="btn btn-solid">Email Srijana</a>
        <a href="{INSTA}" target="_blank" rel="noopener" class="btn btn-outline">@srijana.art.gallery</a>
        <a href="{ETSY}" target="_blank" rel="noopener" class="btn btn-outline">Prints on Etsy</a>
      </div>
    </div>
  </div>
</section>"""


def footer(include_contact=True):
    contact = contact_section() if include_contact else ""
    return f"""{contact}
</main>
<footer>
  <div class="wrap">
    <div class="footer-links">
      <a href="index.html">Home</a>
      <a href="exhibitions.html">Exhibitions</a>
      <a href="mailto:{EMAIL}">Email</a>
      <a href="impressum.html">Impressum</a>
      <a href="datenschutz.html">Datenschutz</a>
    </div>
    &copy; <span id="year">2026</span> Srijana GS. All artwork shown remains the property of the artist.
  </div>
</footer>
<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
"""


def lightbox_markup():
    return """
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Artwork viewer">
  <button class="lb-btn lightbox-close" id="lb-close" aria-label="Close">&times;</button>
  <button class="lb-btn lightbox-prev" id="lb-prev" aria-label="Previous artwork">&#8249;</button>
  <button class="lb-btn lightbox-next" id="lb-next" aria-label="Next artwork">&#8250;</button>
  <div class="lightbox-content">
    <img id="lightbox-img" src="" alt="">
    <div class="lightbox-info">
      <strong id="lightbox-title"></strong>
      <span class="medium" id="lightbox-medium"></span>
      <p id="lightbox-desc"></p>
      <div class="lightbox-actions">
        <a class="btn btn-solid" id="lb-enquire" href="#">Enquire about this piece</a>
        <a class="btn btn-outline hidden" id="lb-exhibition" href="#">See it on exhibition</a>
      </div>
    </div>
  </div>
  <div class="lightbox-counter" id="lightbox-counter"></div>
</div>
"""


GALLERY_JS = """
<script>
(function () {
  var EMAIL = '%EMAIL%';
  var cards    = Array.prototype.slice.call(document.querySelectorAll('.art-card'));
  var lightbox = document.getElementById('lightbox');
  if (!lightbox || !cards.length) return;
  var lbImg    = document.getElementById('lightbox-img');
  var enquire  = document.getElementById('lb-enquire');
  var exhLink  = document.getElementById('lb-exhibition');
  var current  = -1;
  var lastFocus = null;

  function visibleCards() {
    return cards.filter(function (c) { return !c.classList.contains('hidden'); });
  }

  // Builds the prefilled enquiry email so the visitor never has to describe the piece.
  function mailtoFor(card) {
    var title  = card.dataset.title;
    var medium = card.dataset.medium;
    var subject = 'Enquiry: "' + title + '"';
    var body =
      'Hello Srijana,\\n\\n' +
      'I saw "' + title + '" (' + medium + ') on your website and would like to know more.\\n\\n' +
      'Could you tell me:\\n' +
      '  \\u2022 the price\\n' +
      '  \\u2022 the size, and whether it is framed\\n' +
      '  \\u2022 whether it can be shipped, and roughly what that would cost\\n\\n' +
      'Thank you,\\n';
    return 'mailto:' + EMAIL +
           '?subject=' + encodeURIComponent(subject) +
           '&body='   + encodeURIComponent(body);
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
    document.body.classList.add('no-scroll');
    document.getElementById('lb-close').focus();
  }

  function close() {
    lightbox.classList.remove('open');
    document.body.classList.remove('no-scroll');
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
""".replace('%EMAIL%', EMAIL)


# ----------------------------------------------------------------- index page
def gallery_cards():
    out = []
    for n in ORDER:
        title, cat, medium, desc, alt, w, h = ART[n]
        badge = ""
        exh_attr = ""
        if n in EXHIBITED:
            label, link = EXHIBITED[n]
            badge = f'\n        <span class="badge badge-exhibited">{esc(label)}</span>'
            exh_attr = f'\n              data-exhibition="{esc(link)}"'
        out.append(
f'''      <figure class="art-card" data-cat="{cat}" tabindex="0" role="button" aria-label="View {esc(title)} larger"
              data-full="images/web/art{n}.jpg"
              data-title="{esc(title)}"
              data-medium="{esc(medium)}"
              data-desc="{esc(desc)}"{exh_attr}>{badge}
        <img src="images/thumbs/art{n}.jpg" width="{w}" height="{h}" loading="lazy" decoding="async" alt="{esc(alt)}">
        <figcaption class="art-caption"><strong>{esc(title)}</strong>{esc(medium)}</figcaption>
      </figure>''')
    return "\n\n".join(out)


def counts():
    c = {"portrait": 0, "landscape": 0, "still-life": 0}
    for n in ORDER:
        c[ART[n][1]] += 1
    return c


def build_index():
    c = counts()
    return head(
        "Srijana GS — Artist",
        "Original paintings by Srijana GS — portraits, landscapes and still life in acrylic and watercolour, made between Nepal and Leipzig. Works available; prices on request.",
        "gallery",
    ) + f"""
<section class="hero">
  <div class="wrap">
    <div class="kicker">Painter · Leipzig, Germany</div>
    <h1>Srijana GS</h1>
    <p class="lede">Self-taught artist working in acrylic and watercolor — painting faces, memory, and quiet moments carried between Nepal, and every place life has taken her since.</p>
    <div class="cta-row">
      <a href="#gallery" class="btn btn-solid">View the gallery</a>
      <a href="exhibitions.html" class="btn btn-outline">Where to see the work</a>
    </div>
  </div>
</section>

<section id="about">
  <div class="wrap about-grid">
    <div class="about-portrait">
      <img src="images/web/art1.jpg" width="1275" height="1800" alt="Portrait painting by Srijana GS of a mother carrying her child in a traditional woven wrap">
    </div>
    <div class="about-text">
      <div class="section-head" style="text-align:left; margin: 0 0 20px;">
        <div class="kicker">About the artist</div>
        <h2 style="margin-bottom: 0;">Painting as a way of looking closely</h2>
      </div>
      <p>Srijana is a self-taught artist who paints in acrylic, watercolor, and mixed media — portraits of people she encounters through photographs, memory, and travel, alongside landscapes and quiet still life studies of flowers she's grown or gathered along the way.</p>
      <p>Her portraits often return to faces that carry a story: honey hunters from the mountains of Nepal, mothers carrying children through the cold, a child comforted by an animal while waiting for someone to come home. She's drawn to expressions that hold both hardship and quiet dignity.</p>
      <div class="quote">"Painting has always served as my inner world — allowing me to dive in and sit with the characters I paint."</div>
      <p>One painting travelled with her from Thailand to Germany, and on to New Zealand before a PhD — carried along not because it was finished, but because, as she puts it, finishing a piece can feel like its own quiet grief. She's currently based in Leipzig, Germany, still learning — most recently inspired by the work of painter Thomas Braun and a growing love for Impressionism.</p>
      <div class="about-facts">
        <div class="fact"><span class="num">25</span><span class="label">Works shown</span></div>
        <div class="fact"><span class="num">Nepal → Leipzig</span><span class="label">Journey</span></div>
        <div class="fact"><span class="num">Self-taught</span><span class="label">Practice</span></div>
      </div>
    </div>
  </div>
</section>

<section id="gallery" style="background: var(--paper-warm);">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">Selected work</div>
      <h2>Gallery</h2>
      <p>Twenty-five paintings — portraits, landscapes, and still life studies. Click any piece to see it larger.</p>
    </div>

    <div class="avail-note">
      <strong>Most of these paintings are available.</strong> Prices aren't listed because they depend on size, medium and framing — open any piece and use <em>Enquire about this piece</em>, and Srijana will come back to you with a price. Prints of selected works are on <a href="{ETSY}" target="_blank" rel="noopener">Etsy</a>.
    </div>

    <div class="gallery-filter">
      <button class="filter-btn active" data-filter="all">All <span class="count">{len(ORDER)}</span></button>
      <button class="filter-btn" data-filter="portrait">Portraits <span class="count">{c['portrait']}</span></button>
      <button class="filter-btn" data-filter="landscape">Landscapes <span class="count">{c['landscape']}</span></button>
      <button class="filter-btn" data-filter="still-life">Still Life <span class="count">{c['still-life']}</span></button>
    </div>

    <div class="gallery-grid">
{gallery_cards()}
    </div>
  </div>
</section>

<section id="process" class="process">
  <div class="wrap process-grid">
    <div class="section-head" style="margin-bottom: 28px;">
      <div class="kicker">In the studio</div>
      <h2 style="margin-bottom: 0;">On finishing a painting</h2>
    </div>
    <div class="process-text">
      <p>"There is this particular kind of sadness or grief wherever I finish a painting. It feels like the end of something — like the end of intimacy, closing the door, letting go."</p>
      <p>"Maybe it's because I find the beauty in the process more than the final output — in the becoming, in the possibilities and uncertainty of an incomplete work."</p>
      <p style="color: var(--ink); font-style: normal; font-size: 1rem;">— Srijana, from her studio in Leipzig</p>
    </div>
  </div>
</section>
""" + footer() + lightbox_markup() + GALLERY_JS + "\n</body>\n</html>\n"


# ----------------------------------------------------------------- exhibitions
def build_exhibitions():
    return head(
        "Exhibitions — Srijana GS",
        "Where to see Srijana GS's paintings in person: the open-air gallery Am Kunstwinkel in Markkleeberg, and upcoming markets and exhibitions around Leipzig.",
        "exhibitions",
    ) + f"""
<section class="event-hero">
  <div class="wrap">
    <div class="kicker">Exhibitions &amp; markets</div>
    <h1>Where to see the work</h1>
    <p class="lede">Paintings shown in public, past and upcoming. Some pieces travel; if you want to see a particular painting in person, just ask.</p>
  </div>
</section>

<section style="padding-top: 20px;">
  <div class="wrap">
    <div class="exh-list">

      <a class="exh-card" href="exhibition-garagenhof.html" style="text-decoration:none">
        <img src="images/events/kw-artist-wall-sm.jpg" alt="Srijana standing in front of the open-air gallery wall" loading="lazy">
        <div class="body">
          <span class="status-pill status-upcoming">Upcoming</span>
          <div class="when">Saturday 12 September 2026 · 13:00–16:00</div>
          <h3>Garagenhof, Leipzig</h3>
          <p>A table of her own at the Garagenhof — originals, studies and prints, and the chance to talk to her about a commission in person.</p>
          <span class="go">Event details →</span>
        </div>
      </a>

      <a class="exh-card" href="exhibition-kunstwinkel.html" style="text-decoration:none">
        <img src="images/events/kw-board-sm.jpg" alt="The Am Kunstwinkel open-air gallery wall in Markkleeberg" loading="lazy">
        <div class="body">
          <span class="status-pill status-live">On show until 2027</span>
          <div class="when">From 5 September 2026 · Markkleeberg</div>
          <h3>Am Kunstwinkel — “Mein Bild für Dich”</h3>
          <p>“The Morning Pipe” was selected as one of 24 works for the open-air gallery wall in Markkleeberg. It hangs there for a year, then goes to auction.</p>
          <span class="go">Event details &amp; bidding →</span>
        </div>
      </a>

    </div>

    <div class="callout" style="margin-top: 44px;">
      <p><strong>Organising something?</strong> Srijana is open to markets, group shows and café or practice exhibitions in and around Leipzig. Write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
  </div>
</section>
""" + footer(include_contact=False) + "\n</body>\n</html>\n"


# ----------------------------------------------------------------- Kunstwinkel
def build_kunstwinkel():
    photos = [
        ("kw-board", "The open-air gallery wall at Am Kunstwinkel, Markkleeberg, with the 24 newly unveiled works"),
        ("kw-artist-wall", "Srijana in front of the Kunstwinkel wall on the day of the unveiling"),
        ("kw-panel-detail", "Close view of the wall showing “The Morning Pipe” among the neighbouring works"),
        ("kw-crowd", "Visitors gathered in front of the Kunstwinkel wall during the Kunstwinkelfest"),
        ("kw-artist", "Srijana at the Kunstwinkelfest"),
        ("kw-board-angle", "The gallery wall seen from the side, with the painted lake mural below"),
        ("kw-crowd-close", "The crowd looking up at the newly unveiled collection"),
        ("kw-artist-full", "Srijana beneath the Am Kunstwinkel lettering"),
    ]
    strip = "\n".join(
        f'''      <figure><img src="images/events/{n}-sm.jpg" data-full="images/events/{n}.jpg" loading="lazy" decoding="async" alt="{esc(a)}"></figure>'''
        for n, a in photos)

    return head(
        "Am Kunstwinkel, Markkleeberg 2026/27 — Srijana GS",
        "“The Morning Pipe” by Srijana GS is one of 24 works in the open-air gallery Am Kunstwinkel in Markkleeberg, on show until 2027 and then auctioned.",
        "exhibitions",
    ) + f"""
<section class="event-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Home</a> · <a href="exhibitions.html">Exhibitions</a></div>
    <span class="status-pill status-live">On show until autumn 2027</span>
    <h1>Am Kunstwinkel, Markkleeberg</h1>
    <p class="lede">“The Morning Pipe” was selected as one of 24 works for the 2026/27 open-air gallery on the Kunstwinkel wall, under the motto <em>“Mein Bild für Dich”</em>. It was unveiled at the 8th Kunstwinkelfest on 5 September 2026 and hangs there for a full year.</p>
  </div>
</section>

<section style="padding-top: 30px;">
  <div class="wrap event-grid">

    <div>
      <div class="featured-work">
        <img src="images/web/art25.jpg" alt="{esc(ART[25][4])}" loading="lazy">
        <div class="body">
          <h3>The Morning Pipe</h3>
          <span class="medium">{esc(ART[25][2])}</span>
          <p>An elderly woman draws on her pipe, both hands cupped around it. The whole painting is held within one narrow range of warm ochre and rose — the light doing the work that colour usually does.</p>
          <a class="btn btn-outline" href="index.html#gallery">See it in the gallery</a>
        </div>
      </div>
    </div>

    <div>
      <h2 style="margin-top:0;">How this one works</h2>
      <p style="color: var(--ink-soft);">The Kunstwinkel is a permanent open-air gallery on a house wall at Rathausstraße 23 in Markkleeberg. Each year the town selects 24 works from submitted artists, mounts them on the wall for twelve months, and then auctions them at the following year's Kunstwinkelfest — with the proceeds going to the artists and the project.</p>

      <table class="facts-table">
        <tr><th>Exhibition</th><td>Am Kunstwinkel — open-air gallery, 2026/27 collection</td></tr>
        <tr><th>Motto</th><td>“Mein Bild für Dich”</td></tr>
        <tr><th>Work shown</th><td>The Morning Pipe</td></tr>
        <tr><th>Unveiled</th><td>5 September 2026, at the 8th Kunstwinkelfest</td></tr>
        <tr><th>On show until</th><td>Kunstwinkelfest 2027</td></tr>
        <tr><th>Where</th><td>Rathausstraße 23, 04416 Markkleeberg</td></tr>
        <tr><th>Selected works</th><td>24, by 24 different artists</td></tr>
        <tr><th>Organiser</th><td><a href="{KW_FEST}" target="_blank" rel="noopener">Stadt Markkleeberg</a></td></tr>
      </table>

      <div class="callout">
        <p><strong>Bidding is not open yet.</strong> The 2026/27 collection — the one this painting belongs to — goes to auction at the Kunstwinkelfest in September 2027. The town publishes an online catalogue a few weeks beforehand, run by the auction house IKV Fester, where bids can be placed in advance of the live auction.</p>
        <p>This page will carry the direct bidding link as soon as the town publishes it. Until then:</p>
        <p>
          <a class="btn btn-outline" href="{KW_FEST}" target="_blank" rel="noopener">Kunstwinkelfest page</a>
          <a class="btn btn-outline" href="{KW_AUCTION_HOUSE}" target="_blank" rel="noopener">Auction house</a>
        </p>
        <!-- TODO 2027: replace the two buttons above with the direct lot URL, e.g.
             <a class="btn btn-solid" href="https://auktion.ikv-fester.de/...">Place a bid on this painting</a> -->
      </div>

      <p style="color: var(--ink-soft);">If you'd rather not wait for the auction, Srijana has other originals available directly — <a href="index.html#gallery">see the gallery</a> or <a href="mailto:{EMAIL}?subject=Painting%20enquiry">write to her</a>.</p>
    </div>

  </div>
</section>

<section style="background: var(--paper-warm);">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">5 September 2026</div>
      <h2>The unveiling</h2>
      <p>The 8th Kunstwinkelfest, when the new collection went up on the wall.</p>
    </div>
    <div class="photo-strip" id="photo-strip">
{strip}
    </div>
  </div>
</section>
""" + footer(include_contact=False) + """
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer">
  <button class="lb-btn lightbox-close" id="lb-close" aria-label="Close">&times;</button>
  <button class="lb-btn lightbox-prev" id="lb-prev" aria-label="Previous photo">&#8249;</button>
  <button class="lb-btn lightbox-next" id="lb-next" aria-label="Next photo">&#8250;</button>
  <div class="lightbox-content">
    <img id="lightbox-img" src="" alt="">
    <div class="lightbox-info"><p id="lightbox-desc"></p></div>
  </div>
  <div class="lightbox-counter" id="lightbox-counter"></div>
</div>
<script>
(function () {
  var figs = Array.prototype.slice.call(document.querySelectorAll('#photo-strip figure'));
  var lb = document.getElementById('lightbox');
  if (!lb || !figs.length) return;
  var img = document.getElementById('lightbox-img'), i = -1, lastFocus = null;
  function show(n) {
    i = (n + figs.length) % figs.length;
    var el = figs[i].querySelector('img');
    img.src = el.dataset.full; img.alt = el.alt;
    document.getElementById('lightbox-desc').textContent = el.alt;
    document.getElementById('lightbox-counter').textContent = (i + 1) + ' / ' + figs.length;
  }
  function open(n) { lastFocus = document.activeElement; show(n); lb.classList.add('open');
                     document.body.classList.add('no-scroll'); document.getElementById('lb-close').focus(); }
  function close() { lb.classList.remove('open'); document.body.classList.remove('no-scroll');
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
</body>
</html>
"""


# ----------------------------------------------------------------- Garagenhof
def build_garagenhof():
    return head(
        "Garagenhof, Leipzig — Srijana GS",
        "Srijana GS shows and sells original paintings at her own table at the Garagenhof in Leipzig, Saturday 12 September 2026, 13:00–16:00.",
        "exhibitions",
    ) + f"""
<section class="event-hero">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Home</a> · <a href="exhibitions.html">Exhibitions</a></div>
    <span class="status-pill status-upcoming">Upcoming</span>
    <h1>A table at the Garagenhof</h1>
    <p class="lede">One afternoon in Leipzig with the originals on the table — the paintings from this website, some studies that never made it online, and the chance to talk about a commission face to face.</p>
  </div>
</section>

<section style="padding-top: 30px;">
  <div class="wrap event-grid">

    <div>
      <h2 style="margin-top:0;">Come and say hello</h2>
      <p style="color: var(--ink-soft);">Srijana will have her own table, showing original paintings and smaller works on paper. Everything on the table is for sale, and there is no obligation at all — it's just as good a reason to come and look closely at the brushwork, ask how a piece was made, or talk about a portrait of someone in your own family.</p>
      <p style="color: var(--ink-soft);">If there's a particular painting from the <a href="index.html#gallery">gallery</a> you'd like to see in person, <a href="mailto:{EMAIL}?subject=Garagenhof%20-%20can%20you%20bring%20a%20painting%3F">send a message beforehand</a> and she'll bring it along.</p>

      <table class="facts-table">
        <tr><th>What</th><td>Srijana's table — original paintings, studies and prints</td></tr>
        <tr><th>Date</th><td>Saturday, 12 September 2026</td></tr>
        <tr><th>Time</th><td>13:00 – 16:00</td></tr>
        <tr><th>Where</th><td>Garagenhof, Leipzig <span style="color:var(--accent)">— full address to be confirmed</span></td></tr>
        <tr><th>Entry</th><td>Free</td></tr>
        <tr><th>Payment</th><td>Cash, or bank transfer by arrangement</td></tr>
      </table>

      <!-- TODO before publishing:
           - confirm the exact venue name and full street address
           - confirm the date (assumed: the Saturday after 5 Sep 2026)
           - add the organiser's event link if there is one
           - add a photo of her table once the event has happened -->

      <div class="callout">
        <p><strong>Details still being confirmed.</strong> The venue address and organiser link will be added here shortly. Follow <a href="{INSTA}" target="_blank" rel="noopener">@srijana.art.gallery</a> for the final details, or <a href="mailto:{EMAIL}?subject=Garagenhof%20details">ask by email</a>.</p>
      </div>
    </div>

    <div>
      <div class="featured-work">
        <img src="images/web/art16.jpg" alt="{esc(ART[16][4])}" loading="lazy">
        <div class="body">
          <h3>What's likely to be on the table</h3>
          <span class="medium">Originals · studies · prints</span>
          <p>A mix of the portraits and the smaller watercolour studies — the sketchbook pieces are the easiest place to start a collection, and the large acrylic portraits are the ones people tend to stand in front of longest.</p>
          <a class="btn btn-outline" href="index.html#gallery">Browse the gallery first</a>
        </div>
      </div>
    </div>

  </div>
</section>
""" + footer(include_contact=False) + "\n</body>\n</html>\n"


# ----------------------------------------------------------------- legal pages
IMPRESSUM_NAME    = "[TO FILL: full legal name]"
IMPRESSUM_STREET  = "[TO FILL: street and number]"
IMPRESSUM_CITY    = "[TO FILL: postcode and city]"
IMPRESSUM_COUNTRY = "Germany"
IMPRESSUM_PHONE   = "[TO FILL: phone number, or delete this line]"


def build_impressum():
    return head(
        "Impressum — Srijana GS",
        "Legal notice (Impressum) for srijana-art.github.io according to § 5 DDG.",
        "",
    ) + f"""
<section>
  <div class="wrap prose">
    <div class="breadcrumb"><a href="index.html">Home</a></div>
    <h1>Impressum</h1>
    <p class="updated">Angaben gemäß § 5 DDG (ehemals § 5 TMG)</p>

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
      Telefon: {IMPRESSUM_PHONE}
    </address>

    <h2>Verantwortlich für den Inhalt</h2>
    <address>{IMPRESSUM_NAME}, Anschrift wie oben</address>

    <h2>Umsatzsteuer</h2>
    <p>Als Kleinunternehmerin im Sinne von § 19 UStG wird keine Umsatzsteuer berechnet und
       daher auch keine Umsatzsteuer-Identifikationsnummer geführt.</p>
    <p><em>[TO CHECK: only keep this section if she is registered as a Kleinunternehmerin.
       If she has a USt-IdNr., replace this with it. If she is not registered at all,
       delete this section and see the notes in README.md.]</em></p>

    <h2>Streitbeilegung</h2>
    <p>Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit:
       <a href="https://ec.europa.eu/consumers/odr/" target="_blank" rel="noopener">https://ec.europa.eu/consumers/odr/</a>.
       Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer
       Verbraucherschlichtungsstelle teilzunehmen.</p>

    <h2>Urheberrecht</h2>
    <p>Sämtliche auf dieser Website gezeigten Kunstwerke, Abbildungen und Texte sind
       urheberrechtlich geschützt und verbleiben Eigentum der Künstlerin. Eine Vervielfältigung,
       Bearbeitung oder Verbreitung — insbesondere der Bilder der Gemälde — bedarf der
       schriftlichen Zustimmung der Künstlerin.</p>

    <h2>Haftung für Links</h2>
    <p>Diese Website enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen
       Einfluss haben. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter
       oder Betreiber verantwortlich.</p>

    <hr>
    <p class="updated">English summary: this is the legal notice required of German websites.
       The artist can be reached at <a href="mailto:{EMAIL}">{EMAIL}</a>. All artwork shown on
       this site remains the property of the artist.</p>
  </div>
</section>
""" + footer(include_contact=False) + "\n</body>\n</html>\n"


def build_datenschutz():
    return head(
        "Datenschutzerklärung — Srijana GS",
        "Privacy notice for srijana-art.github.io.",
        "",
    ) + f"""
<section>
  <div class="wrap prose">
    <div class="breadcrumb"><a href="index.html">Home</a></div>
    <h1>Datenschutzerklärung</h1>
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
       Es gibt kein Kontaktformular — die Kontaktaufnahme erfolgt ausschließlich über einen
       E-Mail-Link.</p>

    <h2>3. Hosting (GitHub Pages)</h2>
    <p>Diese Website wird von GitHub Pages gehostet, einem Dienst der GitHub, Inc.,
       88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Beim Aufruf der Seite
       werden durch GitHub automatisch Server-Logdaten verarbeitet, insbesondere die
       IP-Adresse, Datum und Uhrzeit des Zugriffs, die aufgerufene Seite, der verwendete
       Browser und das Betriebssystem. Diese Verarbeitung erfolgt zur technischen
       Bereitstellung und Sicherheit der Website auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO
       (berechtigtes Interesse). Weitere Informationen:
       <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" target="_blank" rel="noopener">GitHub Privacy Statement</a>.</p>

    <h2>4. Schriftarten (Google Fonts)</h2>
    <p>Diese Website lädt Schriftarten von Google Fonts (Google Ireland Limited). Dabei wird
       die IP-Adresse des Besuchers an Google übertragen. Rechtsgrundlage ist Art. 6 Abs. 1
       lit. f DSGVO. <em>[Hinweis: Sollen keine Daten an Google übertragen werden, können die
       Schriftarten lokal eingebunden werden — siehe README.md.]</em></p>

    <h2>5. Kontaktaufnahme per E-Mail</h2>
    <p>Wenn Sie per E-Mail Kontakt aufnehmen, werden Ihre Angaben zur Bearbeitung der Anfrage
       und für den Fall von Anschlussfragen gespeichert. Rechtsgrundlage ist Art. 6 Abs. 1
       lit. b DSGVO (vorvertragliche Maßnahmen) bzw. lit. f DSGVO. Die Daten werden gelöscht,
       sobald sie für den Zweck nicht mehr erforderlich sind.</p>

    <h2>6. Externe Links</h2>
    <p>Diese Website verlinkt auf Instagram, Etsy und die Seiten der Stadt Markkleeberg bzw.
       des Auktionshauses. Für die Datenverarbeitung auf diesen Seiten gelten die jeweiligen
       Datenschutzerklärungen der Anbieter. Es werden keine Inhalte dieser Dienste direkt in
       diese Website eingebettet.</p>

    <h2>7. Ihre Rechte</h2>
    <ul>
      <li>Auskunft über die verarbeiteten Daten (Art. 15 DSGVO)</li>
      <li>Berichtigung unrichtiger Daten (Art. 16 DSGVO)</li>
      <li>Löschung (Art. 17 DSGVO) und Einschränkung der Verarbeitung (Art. 18 DSGVO)</li>
      <li>Datenübertragbarkeit (Art. 20 DSGVO)</li>
      <li>Widerspruch gegen die Verarbeitung (Art. 21 DSGVO)</li>
      <li>Beschwerde bei einer Aufsichtsbehörde (Art. 77 DSGVO)</li>
    </ul>
    <p>Zur Ausübung genügt eine E-Mail an <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

    <hr>
    <p class="updated">English summary: this site sets no cookies and runs no analytics.
       It is hosted on GitHub Pages and loads fonts from Google Fonts, both of which see your
       IP address. Contact happens by email only.</p>
  </div>
</section>
""" + footer(include_contact=False) + "\n</body>\n</html>\n"


# ----------------------------------------------------------------- main
def main():
    os.makedirs(OUT, exist_ok=True)
    pages = {
        "index.html": build_index(),
        "exhibitions.html": build_exhibitions(),
        "exhibition-kunstwinkel.html": build_kunstwinkel(),
        "exhibition-garagenhof.html": build_garagenhof(),
        "impressum.html": build_impressum(),
        "datenschutz.html": build_datenschutz(),
    }
    for name, content in pages.items():
        with open(os.path.join(OUT, name), "w") as fh:
            fh.write(content)
        print(f"{name:32s} {len(content):>7,} bytes")


if __name__ == "__main__":
    main()
