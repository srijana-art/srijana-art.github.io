# Selling from srijana-art.github.io — notes

Working notes on turning the site from a portfolio into something that produces
enquiries and sales. Written September 2026.

**A caveat up front:** the German legal and tax section is a summary of publicly
available rules to help you ask the right questions. I'm not a lawyer or a tax
adviser, and the details depend on Srijana's own situation. Anything with money
or an authority attached should be confirmed with a Steuerberater or the relevant
office before acting on it.

---

## 1. What's already in place

| Piece | Status |
| --- | --- |
| Email contact | `srijana.art.art.gallery@gmail.com`, shown in Contact and in the footer |
| "Enquire about this piece" | On every painting in the lightbox. Opens the visitor's mail app with the title, medium and a checklist of questions already written |
| Availability message | Above the gallery grid — says work is available and explains why prices aren't listed |
| Exhibitions section | `exhibitions.html` + one page per event, designed to stay as an archive |
| Instagram / Etsy | Linked from Contact and the availability note |
| Impressum / Datenschutz | Built, linked in every footer, **awaiting real details** |

The single most valuable thing here is the prefilled enquiry email. The reason
"price on request" usually fails is that the visitor has to compose a message
from nothing, and most people won't. Removing that blank page is worth more than
any amount of copywriting.

---

## 2. The funnel, honestly

Realistically it looks like this:

```
Instagram post  →  bio link  →  gallery  →  one painting  →  enquiry email  →  price  →  sale
     (many)         (fewer)      (fewer)      (fewer)          (a handful)
```

Every stage loses people, so the wins are at the top and at the point of enquiry.
Ranked by what I'd expect to actually move the needle:

### 2.1 One page per painting — the biggest missing piece

Right now the whole gallery is one URL. That means:

- Srijana cannot link a specific painting in an Instagram story or a DM. She has
  to say "go to the site and scroll".
- Google has one page to index instead of twenty-five, and nothing to show in
  image search with a title attached.
- Nobody can send a friend a link to *the one they liked*.

Generating a small page per work — `/work/the-morning-pipe.html` — with the
image, the story, the size, the availability and the enquiry button fixes all
three at once. It's the change I'd make first. (Say the word and I'll build the
generator; the artwork data is already structured in `tools/build_site.py`.)

### 2.2 Show the paintings on a wall

For art sales this is the highest-converting single thing after price. People
cannot judge scale from a flat scan. Two or three photos of paintings hanging in
a real room — even her own flat, even a phone photo in decent light — do more
than a page of description. A simple "actual size" line ("A3 — about the size of
two sheets of paper side by side") is the cheap version.

### 2.3 A commissions page

Portraits are her strongest work and commissions are the easiest thing to sell,
because the buyer already knows what they want. A short page covering:

- what she needs from you (a good photograph, ideally not a phone selfie)
- roughly how long it takes
- what changes the price: size, medium, one figure or two, framed or not
- that a deposit is taken up front and the balance on completion
- two or three examples of finished commissions

This also gives her something concrete to link from Instagram, which is where
commission enquiries actually come from.

### 2.4 A link-in-bio page

Instagram allows one link. Rather than pointing it at the homepage, a small
`/links` page with four buttons — *See the gallery · Commission a portrait ·
Where I'm exhibiting · Prints on Etsy* — lets her steer people without changing
the bio every time. Cheap to build, easy to reorder.

### 2.5 Sold / Available markers

Marking a piece **Sold** is not a loss — it's the strongest signal on the whole
site that other people buy her work. Keep sold pieces visible with a quiet
badge. The Kunstwinkel badge already on *The Morning Pipe* does the same job:
it says someone else selected this.

### 2.6 Findability

- **Custom domain.** `srijana-art.de` costs roughly €10–15 a year and points at
  GitHub Pages with two DNS records. `srijana-art.github.io` reads as a hobby
  project to anyone who recognises the domain; a real domain reads as a working
  artist. This is the cheapest credibility upgrade available.
- **Structured data.** A small block of JSON-LD per painting (`VisualArtwork`)
  tells Google the title, artist, medium and material. Helps in image search.
- **`sitemap.xml` and `robots.txt`.** Two small files; helps indexing.
- **Alt text.** Already written for every painting — this is genuinely half of
  image SEO and it's done.
- **Google Business Profile** is worth considering once there's a real address
  and she's exhibiting locally; local searches for "Portraitmalerin Leipzig"
  are low-volume but very high-intent.

### 2.7 Keeping people warm

Most people who like a painting aren't ready to buy that week. An email list is
the standard answer, but it adds GDPR obligations (consent, double opt-in, a
privacy notice update) and a third-party service. A lighter version: an
"exhibitions" page people can bookmark, plus telling them on the site to follow
Instagram for new work. Start there; add the list only if enquiries justify it.

---

## 3. Pricing without publishing prices

Her instinct not to post prices is defensible, but it does cost enquiries —
some people won't ask because they're afraid of being embarrassed or hassled.
Ways to soften that without committing to numbers:

1. **Say why.** One line — "prices depend on size, medium and framing" — turns a
   silence into a reason. Already on the site.
2. **Publish a range, not a price.** "Small studies on paper from €—, large
   acrylic portraits from €—". This is the single change most likely to increase
   enquiry volume, because it lets people self-select. She can revise it any time.
3. **Promise a response time.** "You'll normally get a price within two days."
   Removes the fear of sending mail into a void.
4. **Say it's not a hard sell.** Something like "asking the price doesn't commit
   you to anything" reads as slightly desperate in English but works well in a
   German context, where people are wary of starting an obligation.

My honest recommendation: keep per-piece prices off, but add the range. It costs
nothing and it's reversible.

---

## 4. Payments — and why not on this site

**Short answer: don't build a checkout.** Not yet, and possibly not ever.

GitHub Pages is a static host. It can't process payments, so any checkout means
embedding a third-party service. That's technically easy — the hard part is what
taking money directly triggers legally.

### What selling to consumers online in Germany involves

Selling regularly and with intent to profit — including from a website —
generally means:

- **Registering the activity.** Selling your own original artwork is usually
  treated as *freiberufliche künstlerische Tätigkeit* (§18 EStG), which needs a
  *Fragebogen zur steuerlichen Erfassung* with the Finanzamt but **not** a
  Gewerbeanmeldung. Reselling prints or merchandise can tip it into *gewerblich*,
  which does need a Gewerbeanmeldung. The line between the two is exactly the
  kind of thing to put to a Steuerberater — it's cheap to ask and expensive to
  get wrong.
- **VAT.** Under the *Kleinunternehmerregelung* (§19 UStG) no VAT is charged
  while turnover stays under the current thresholds. If she ever exceeds them,
  original artworks sold by the artist fall under the reduced rate rather than
  the standard one. Either way the invoice has to say which applies.
- **Right of withdrawal.** Consumers buying at a distance get 14 days to return
  the goods, and you must give them a *Widerrufsbelehrung* before they buy.
  Individually commissioned work is exempt (§312g Abs. 2 Nr. 1 BGB) — a stock
  painting sold off the website is not.
- **Packaging.** Shipping packaged goods to German consumers requires
  registration in the **LUCID** packaging register under the Verpackungsgesetz.
  This applies to small sellers too and is often missed.
- **General terms and a proper Impressum.** The Impressum has to carry a real
  postal address — a P.O. box isn't sufficient.

None of that is triggered by *"email me and I'll send you a price and an
invoice."* Selling on request, to a named person, against an invoice, sits in a
much simpler place than running a shop.

### The three sensible options, in order

1. **Enquiry → invoice → bank transfer** (what the site does now). Simplest.
   German buyers are entirely comfortable with Überweisung. No platform fees.
2. **Enquiry → a payment link** (PayPal, Stripe Payment Link, SumUp). She sends a
   one-off link by email after agreeing the price. The site stays static; no
   checkout, no cart, no stored card data. Good middle ground if people ask to
   pay by card.
3. **Etsy for anything shipped.** She already has a shop. Etsy handles VAT,
   invoicing, distance-selling rights and — importantly — the packaging
   obligations. For prints in particular, letting Etsy carry that burden is worth
   the fee. Keep originals as enquiry-only on her own site.

One more practical point, given she's currently between jobs: income from art
sales can interact with benefits and with any Minijob arrangement. Worth a
direct question to the Agentur für Arbeit / Jobcenter before the first sale
rather than after.

Also worth knowing about, separately: the **Künstlersozialkasse (KSK)** gives
self-employed artists access to subsidised health and pension insurance. Getting
accepted takes evidence of professional artistic activity — exhibitions, sales,
a website — which she is now accumulating. It's the kind of thing that's much
easier to apply for with a year of documented activity behind you, so keeping
records of the Kunstwinkel selection and every sale is worth doing from today.

---

## 5. Layout ideas, in priority order

1. **One page per painting** (§2.1) — everything else is smaller than this.
2. **A commissions page** (§2.3) — the highest-margin, easiest-to-close product.
3. **In-situ photographs** (§2.2) — solves the scale problem.
4. **Price ranges** (§3.2) — one paragraph, meaningful lift in enquiries.
5. **Link-in-bio page** (§2.4) — makes the Instagram → site step deliberate.
6. **Custom domain** (§2.6) — €10 a year for a large credibility gain.
7. **Sold badges** (§2.5) — social proof that costs nothing.
8. **A short "about the process" video or photo series** — people buy from
   artists they feel they've met. Her own words about finishing a painting are
   already the best copy on the site; more of that is better than more polish.

What I would *not* do: add a shop, add a cart, add a newsletter, or add
analytics. Each one adds a compliance obligation and none of them is the
bottleneck right now. The bottleneck is that a person on Instagram cannot link
one painting.

---

## 6. Video on a GitHub Pages site

**Do not use Git LFS for this.** GitHub Pages does not resolve LFS objects — it
serves the *pointer file* instead of the video, so the player gets a 130-byte
text file and fails silently. LFS is fine for a normal repo; it is the wrong
tool for anything Pages has to serve to a browser.

The limits that actually apply:

- 100 MB hard limit per file in git (a push with a bigger file is rejected)
- ~1 GB recommended maximum for a Pages site
- 100 GB/month soft bandwidth limit

A one-minute clip does not need to come anywhere near those. `tools/encode-video.sh`
re-encodes an iPhone clip to about **5–12 MB** — long-edge capped at 1280px,
H.264 at CRF 26, AAC audio, `+faststart` so it begins playing before it has
finished downloading. That is small enough to commit directly, with no LFS and
no external host.

Two things specific to iPhone footage:

- **Cinematic mode records HEVC.** Safari plays HEVC; Chrome and Firefox do not.
  Re-encoding to H.264 is what makes the video work everywhere, and it also
  flattens the rack-focus effect into the picture — which is what you want,
  since the depth track is useless on the web.
- Export the clip from Photos the normal way (Share → Save to Files). "Export
  Unmodified Original" gives the raw capture *without* the cinematic effect
  baked in.

The alternative — YouTube or Vimeo unlisted, embedded — costs nothing in repo
size but loads third-party tracking, which means either a consent banner or a
click-to-load facade, plus an update to the Datenschutzerklärung. Not worth it
for one short clip.

---

## 7. Outstanding TODOs in the code

- `impressum.html` — the USt-IdNr. from the Bundeszentralamt für Steuern.
- `exhibition-garage-ost.html` — confirm date/time against the rausgegangen.de
  listing; optionally swap the card image for the organiser's own.
- `exhibition-kunstwinkel.html` — the direct bidding URL, once Markkleeberg
  publishes the 2027 catalogue (see the `TODO 2027` comment in that file).
- `tools/build_site.py` — set `VIDEO` once the studio clip is encoded.
- Titles and mediums for the 21 works that Srijana hasn't named herself.
