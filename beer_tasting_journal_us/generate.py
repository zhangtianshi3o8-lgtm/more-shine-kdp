#!/usr/bin/env python3
"""
Beer Tasting Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Craft beer enthusiasts, homebrewers
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "beer_tasting_journal_us_V1.0.html")

BOOK_TITLE = "Beer Tasting Journal"
BOOK_SUBTITLE = "Track Every Pint, Every Brewery, Every Flavor"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

def nl(n):
    return "\n".join('<div class="notes-line"></div>' for _ in range(n))

def rating_circles_html(n):
    return " ".join(
        '<span class="rating-circle">%d</span>' % i for i in range(1, n + 1)
    )

def flavor_items_html(items):
    return "\n".join(
        '<div class="check-item"><div class="check-box"></div><span>%s</span></div>'
        % H.escape(item)
        for item in items
    )

# ============================================================
# CSS
# ============================================================
CSS = r"""
@page { size: 6in 9in; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: Georgia, "Iowan Old Style", "Palatino", serif;
  color: #2A2A2A;
  background: white;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

.page {
  width: 6in; height: 9in;
  padding: 0.5in 0.5in 0.4in 0.5in;
  page-break-after: always;
  position: relative;
  background: white;
  overflow: hidden;
}
.page:last-child { page-break-after: auto; }

@media screen { .page { border: 1px dashed #ccc; margin: 8px auto; } }
@media print  { .page { border: none; margin: 0; } }

/* ================ INTERIOR TITLE PAGE ================ */
.cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(165deg, #161210 0%, #231A15 30%, #161210 65%, #0D0A08 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.cover .glow-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #E8A838, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #B87333, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #E8A838, transparent);
}

.cover .title-main {
  font-size: 32pt;
  font-weight: 700;
  color: #FAF6F0;
  line-height: 1.2;
  letter-spacing: 1pt;
  position: relative;
  z-index: 2;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 100px;
  height: 2px;
  background: #C4A04A;
  margin: 20px auto;
  position: relative;
  z-index: 2;
}

.cover .subtitle {
  font-size: 12pt;
  color: #D4B896;
  font-style: italic;
  line-height: 1.5;
  position: relative;
  z-index: 2;
}

.cover .pub {
  position: absolute;
  bottom: 0.6in;
  left: 0; right: 0;
  text-align: center;
  font-size: 9pt;
  color: #C4A04A;
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  font-weight: 700;
}

/* ================ PAGE HEADER ================ */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  padding-bottom: 4px;
  border-bottom: 0.5px solid #eee;
}

.page-header .ph-left {
  font-size: 8pt;
  color: #B87333;
  text-transform: uppercase;
  letter-spacing: 1pt;
  font-weight: 700;
}

.page-header .ph-right {
  font-size: 8pt;
  color: #999;
}

/* ================ SECTION HEADERS ================ */
.section-header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 14px;
}

.section-title {
  font-size: 14pt;
  font-weight: 700;
  color: #161210;
  letter-spacing: 0.5pt;
  text-transform: uppercase;
}

.section-line {
  flex: 1;
  height: 1px;
  background: #C4A04A;
  margin: 0 12px;
  opacity: 0.5;
}

/* ================ TASTING SPREAD LEFT ================ */
.session-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1.5px solid #B87333;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.session-banner .sb-num {
  display: inline-block;
  border: 1.5px solid #B87333;
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 8pt;
  color: #B87333;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
  margin-bottom: 8px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #B87333;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  display: block;
  margin-bottom: 1px;
}

.info-field .if-write {
  height: 16px;
  border-bottom: 1px dotted #ccc;
}

/* Rating circles */
.rating-group {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4px 12px;
  margin-bottom: 8px;
}

.rating-row {
  display: flex;
  align-items: center;
  gap: 4px;
}

.rating-row .rr-label {
  font-size: 7.5pt;
  color: #2A2A2A;
  width: 65px;
  flex-shrink: 0;
}

.rating-circle {
  width: 12px;
  height: 12px;
  border: 1.5px solid #B87333;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 5pt;
  color: #B87333;
  margin-right: 1px;
}

/* ================ TASTING SPREAD RIGHT ================ */
.flavor-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2px 12px;
  margin-bottom: 8px;
}

.check-item {
  display: flex;
  align-items: center;
  gap: 4px;
  height: 16px;
}

.check-box {
  width: 9px;
  height: 9px;
  border: 1px solid #B87333;
  border-radius: 2px;
  flex-shrink: 0;
}

.check-item span {
  font-size: 7.5pt;
  color: #2A2A2A;
}

.write-box {
  border: 1px solid #C4A04A;
  border-radius: 3px;
  padding: 6px 8px;
  margin-bottom: 8px;
}

.write-box .wb-label {
  font-size: 7pt;
  color: #B87333;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 2px;
}

.write-box .wb-area {
  height: 28px;
}

/* Star rating */
.stars {
  font-size: 14pt;
  color: #ccc;
  letter-spacing: 3pt;
}

/* ================ HOW TO USE ================ */
.howto-text {
  font-size: 10pt;
  line-height: 1.7;
  color: #2A2A2A;
}

.howto-text p {
  margin-bottom: 8px;
}

.howto-text .ht-title {
  font-size: 11pt;
  font-weight: 700;
  color: #161210;
  margin-bottom: 4px;
  margin-top: 6px;
}

.howto-text .ht-icon {
  color: #B87333;
  font-weight: 700;
  margin-right: 4px;
}

/* ================ REFERENCE TABLES ================ */
.ref-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
}

.ref-table th {
  font-size: 7pt;
  color: #B87333;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 5px 4px;
  border-bottom: 1.5px solid #B87333;
  text-align: left;
}

.ref-table td {
  padding: 5px 4px;
  border-bottom: 1px solid #eee;
  font-size: 8.5pt;
  vertical-align: top;
}

.ref-table td:first-child {
  font-weight: 700;
  color: #161210;
  width: 1in;
}

/* ============ YEAR REVIEW ============ */
.review-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-bottom: 10px;
}

.review-card {
  border: 1px solid #C4A04A;
  border-radius: 4px;
  padding: 8px;
  background: #FAF6F0;
}

.review-card .rc-label {
  font-size: 7pt;
  color: #B87333;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 4px;
}

.review-card .rc-write {
  height: 28px;
  border-bottom: 1px dotted #ccc;
}

/* Notes */
.notes-line {
  border-bottom: 1px solid #ddd;
  height: 22px;
}

/* Final */
.final-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100%;
}

.final-page .fp-text {
  font-size: 12pt;
  color: #999;
  font-style: italic;
  line-height: 1.8;
  margin-bottom: 20px;
}

.final-page .fp-logo {
  font-size: 11pt;
  color: #C4A04A;
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  font-weight: 700;
}

.final-page .fp-line {
  width: 60px;
  height: 1.5px;
  background: #C4A04A;
  margin: 12px auto;
  opacity: 0.5;
}
"""

# ============================================================
# PAGE GENERATORS
# ============================================================

def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 120" width="90" height="108" xmlns="http://www.w3.org/2000/svg">
      <!-- Mug body -->
      <path d="M 20 40 L 20 100 Q 20 108 28 108 L 68 108 Q 76 108 76 100 L 76 40 Z"
            stroke="#C4A04A" stroke-width="1.8" fill="none"/>
      <!-- Foam -->
      <path d="M 18 42 Q 22 30 30 34 Q 36 26 44 32 Q 50 24 58 30 Q 66 26 72 34 Q 78 30 78 42"
            stroke="#E8A838" stroke-width="1.5" fill="none"/>
      <!-- Foam bubbles -->
      <circle cx="30" cy="36" r="3" stroke="#E8A838" stroke-width="1" fill="none" opacity="0.5"/>
      <circle cx="50" cy="32" r="2.5" stroke="#E8A838" stroke-width="1" fill="none" opacity="0.5"/>
      <circle cx="62" cy="36" r="3" stroke="#E8A838" stroke-width="1" fill="none" opacity="0.5"/>
      <!-- Handle -->
      <path d="M 76 55 Q 88 55 88 70 Q 88 85 76 85"
            stroke="#C4A04A" stroke-width="1.8" fill="none"/>
      <!-- Liquid line -->
      <line x1="22" y1="48" x2="74" y2="48" stroke="#B87333" stroke-width="0.8" opacity="0.4"/>
      <!-- Bubbles -->
      <circle cx="35" cy="60" r="1.5" fill="#E8A838" opacity="0.3"/>
      <circle cx="50" cy="72" r="1.5" fill="#E8A838" opacity="0.3"/>
      <circle cx="60" cy="64" r="1" fill="#E8A838" opacity="0.3"/>
      <circle cx="42" cy="84" r="1.5" fill="#E8A838" opacity="0.3"/>
      <circle cx="58" cy="92" r="1" fill="#E8A838" opacity="0.3"/>
    </svg>
  </div>

  <div class="title-main">Beer Tasting<br>Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Track Every Pint, Every Brewery, Every Flavor</div>

  <div class="pub">More Shine Press</div>
</div>""" % pn()


def how_to_use_page():
    pg = pn()
    return """<!-- PAGE %d: How to Use -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">How to Use This Journal</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Craft Beer Journey</div>
    <p>This journal is your companion for exploring the world of craft beer.
    From hoppy IPAs to rich stouts, tart sours to crisp lagers, every beer
    has a story. Capture it here.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Tasting Spread</div>
    <p>Each tasting uses a <strong>two-page spread</strong>. The left page records
    beer details: name, brewery, style, ABV, IBU, color, serving type, and
    your 1-5 ratings across six sensory categories. The right page dives
    deeper with a 20-note flavor checklist, appearance notes, aroma, overall
    rating, freeform tasting notes, and food pairing ideas.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tasting Tips</div>
    <p>&#9679; <strong>Look.</strong> Note the color, clarity, and head retention.</p>
    <p>&#9679; <strong>Smell.</strong> Swirl gently. What aromas come through?</p>
    <p>&#9679; <strong>Taste.</strong> Take a sip. Let it coat your palate. Note flavors.</p>
    <p>&#9679; <strong>Feel.</strong> Body, carbonation, warmth, astringency.</p>
    <p>&#9679; <strong>Finish.</strong> What lingers after you swallow?</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Key Terms</div>
    <p><strong>ABV</strong> = Alcohol by Volume. <strong>IBU</strong> = International Bitterness Units
    (higher = more bitter). <strong>SRM</strong> = color scale (pale straw to black).</p>
  </div>
</div>""" % (pg, pg)


def style_guide_page_1():
    pg = pn()
    styles = [
        ("IPA", "Hop-forward, bitter, citrusy or piney. 5.5-7.5%% ABV. 40-70 IBU."),
        ("Pale Ale", "Balanced hops and malt. Sessionable. 4.5-6.2%% ABV. 30-50 IBU."),
        ("Stout", "Dark, roasted, coffee and chocolate notes. 4-8%% ABV. 30-60 IBU."),
        ("Porter", "Dark, roasted malt, smooth. 4-6.5%% ABV. 20-40 IBU."),
        ("Pilsner", "Crisp, clean, floral hops. 4-5.5%% ABV. 25-40 IBU."),
        ("Wheat Beer", "Hazy, light, notes of banana and clove. 4-5.5%% ABV. 10-20 IBU."),
    ]
    rows = ""
    for name, desc in styles:
        rows += "<tr><td>%s</td><td>%s</td></tr>\n" % (H.escape(name), H.escape(desc))

    return """<!-- PAGE %d: Style Guide 1 -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Beer Style Guide (1 of 2)</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Major Beer Styles</div>
    <div class="section-line"></div>
  </div>

  <table class="ref-table">
    <thead>
      <tr><th>Style</th><th>Characteristics</th></tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>

  <div class="howto-text">
    <p style="font-size: 8.5pt; font-style: italic; color: #777;">
    ABV and IBU ranges are general guidelines. Individual beers may vary.
    Use this guide to identify what you are tasting and discover new styles
    to try.
    </p>
  </div>
</div>""" % (pg, pg, rows)


def style_guide_page_2():
    pg = pn()
    styles = [
        ("Saison", "Farmhouse ale, spicy, fruity, dry. 5-8%% ABV. 20-35 IBU."),
        ("Belgian", "Complex fruit and spice, high carbonation. 6-10%% ABV. 20-40 IBU."),
        ("Sour", "Tart, acidic, funky. Wide range. 3-9%% ABV. 5-15 IBU."),
        ("Lager", "Clean, crisp, smooth. 4-5.5%% ABV. 15-30 IBU."),
        ("Brown Ale", "Nutty, caramel, toffee. 4-6%% ABV. 15-25 IBU."),
        ("Barleywine", "Strong, rich, sweet or hoppy. 8-12%% ABV. 35-70 IBU."),
    ]
    rows = ""
    for name, desc in styles:
        rows += "<tr><td>%s</td><td>%s</td></tr>\n" % (H.escape(name), H.escape(desc))

    return """<!-- PAGE %d: Style Guide 2 -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Beer Style Guide (2 of 2)</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">More Beer Styles</div>
    <div class="section-line"></div>
  </div>

  <table class="ref-table">
    <thead>
      <tr><th>Style</th><th>Characteristics</th></tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Understanding SRM (Color)</div>
    <p style="font-size: 9pt;">SRM measures beer color from pale straw (2) to
    black (40+). Use this when recording the appearance of each beer:</p>
    <p style="font-size: 8.5pt; color: #555; margin-top: 4px;">
    2-3 = Pale Straw &nbsp;|&nbsp; 3-4 = Straw &nbsp;|&nbsp; 4-6 = Gold<br>
    6-8 = Amber &nbsp;|&nbsp; 8-15 = Copper/Brown &nbsp;|&nbsp; 15-25 = Dark Brown<br>
    25+ = Black
    </p>
  </div>
</div>""" % (pg, pg, rows)


def flavor_wheel_page():
    pg = pn()
    categories = [
        ("Hoppy", ["Pine", "Resinous", "Grapefruit", "Citrus", "Floral", "Herbal"]),
        ("Malty", ["Caramel", "Toffee", "Bread", "Biscuit", "Toast", "Grainy"]),
        ("Roasted", ["Coffee", "Chocolate", "Dark cocoa", "Smoke", "Burnt", "Char"]),
        ("Fruity", ["Citrus", "Tropical", "Stone fruit", "Berry", "Banana", "Apple"]),
        ("Spice", ["Clove", "Pepper", "Coriander", "Ginger", "Allspice", "Cinnamon"]),
        ("Sour/Funky", ["Tart", "Vinegar", "Barnyard", "Leather", "Earth", "Horse"]),
        ("Sweet", ["Honey", "Vanilla", "Maple", "Molasses", "Sugar", "Creamy"]),
        ("Other", ["DMS", "Oxidized", "Metallic", "Grassy", "Yeasty", "Alcohol"]),
    ]
    sections = ""
    for cat, notes in categories:
        items_html = "\n".join(
            '<div class="check-item"><div class="check-box"></div><span>%s</span></div>'
            % H.escape(n)
            for n in notes
        )
        sections += """<div class="write-box">
  <div class="wb-label">%s</div>
  <div class="flavor-grid">%s</div>
</div>
""" % (H.escape(cat), items_html)

    return """<!-- PAGE %d: Flavor Wheel -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Beer Flavor Wheel</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Flavor Reference</div>
    <div class="section-line"></div>
  </div>

  <div class="howto-text">
    <p style="font-size: 8.5pt; margin-bottom: 6px;">
    Use this reference when filling out the flavor checklist on each tasting
    page. These are the most common flavor and aroma descriptors in craft beer.
    </p>
  </div>

  %s
</div>""" % (pg, pg, sections)


def brewery_tracker_page():
    pg = pn()
    rows = ""
    for _ in range(12):
        rows += """<tr>
    <td></td><td></td><td></td><td></td>
  </tr>
"""
    return """<!-- PAGE %d: Brewery Tracker -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Brewery Tracker</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Breweries I've Visited</div>
    <div class="section-line"></div>
  </div>

  <table class="ref-table">
    <thead>
      <tr>
        <th>Brewery</th>
        <th>Location</th>
        <th>Favorite Beer</th>
        <th>Rating</th>
      </tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>
</div>""" % (pg, pg, rows)


def glassware_page():
    pg = pn()
    glasses = [
        ("Pint Glass", "The all-purpose workhorse. Good for most ales and lagers."),
        ("Tulip", "Flared lip captures aromas. Great for IPAs and Belgian ales."),
        ("Snifter", "Bowl shape concentrates aroma. Ideal for stouts and barleywines."),
        ("Weizen", "Tall and curved. Designed for wheat beers with large heads."),
        ("Pilsner", "Tall and slender. Shows off clarity and carbonation."),
        ("Goblet", "Wide bowl for sipping. Good for strong Belgian ales."),
    ]
    rows = ""
    for name, desc in glasses:
        rows += "<tr><td>%s</td><td>%s</td></tr>\n" % (H.escape(name), H.escape(desc))

    return """<!-- PAGE %d: Glassware Guide -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Glassware Guide</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Common Beer Glassware</div>
    <div class="section-line"></div>
  </div>

  <table class="ref-table">
    <thead>
      <tr><th>Glass</th><th>Best For</th></tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Why Glassware Matters</div>
    <p style="font-size: 9pt;">The right glass enhances your beer experience.
    Aroma is a huge part of flavor, and glasses designed to trap or release
    aromas can completely change how a beer tastes.</p>
  </div>
</div>""" % (pg, pg, rows)


def terminology_page():
    pg = pn()
    terms = [
        ("ABV", "Alcohol by Volume. The percentage of alcohol in the beer."),
        ("IBU", "International Bitterness Units. Measures hop bitterness. Most beers range 5-80."),
        ("SRM", "Standard Reference Method. Measures beer color from pale (2) to black (40+)."),
        ("Gravity", "Density of wort or beer. Original Gravity (OG) and Final Gravity (FG) determine ABV."),
        ("Attenuation", "The percentage of sugars converted to alcohol during fermentation."),
        ("Head", "The foam on top of poured beer. Good head retention indicates quality."),
        ("Lace", "The foam residue left on the glass as you drink. A sign of a well-made beer."),
        ("Body", "The thickness or mouthfeel of a beer. Described as thin, medium, or full."),
        ("Conditioning", "The period after fermentation where beer matures and develops flavor."),
        ("Dry-Hopping", "Adding hops after fermentation for aroma without added bitterness."),
        ("Session Beer", "A low-ABV beer designed for extended drinking sessions."),
        ("Imperial", "A stronger version of a style, typically 8%% ABV or higher."),
    ]
    items = ""
    for term, definition in terms:
        items += """<div style="margin-bottom: 5px;">
    <span style="font-weight: 700; color: #B87333; font-size: 9pt;">%s</span>
    <span style="font-size: 9pt; color: #2A2A2A; margin-left: 8px;">%s</span>
  </div>
""" % (H.escape(term), H.escape(definition))

    return """<!-- PAGE %d: Terminology -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Tasting Terminology</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Beer Glossary</div>
    <div class="section-line"></div>
  </div>

  %s
</div>""" % (pg, pg, items)


def tasting_left(session_num):
    pg = pn()
    return """<!-- PAGE %d: Tasting Left #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Beer Tasting</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="session-banner">
    <span class="sb-num">Tasting #%03d</span>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Beer Name</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Brewery</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Style</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">ABV</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">IBU</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">SRM / Color</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Price</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Location</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Serving</span>
      <div style="display: flex; gap: 6px; padding-top: 2px;">
        <span style="font-size: 7pt; color: #555;"><span class="check-box" style="display:inline-block; width:8px; height:8px; border:1px solid #B87333; border-radius:2px;"></span> Draft</span>
        <span style="font-size: 7pt; color: #555;"><span class="check-box" style="display:inline-block; width:8px; height:8px; border:1px solid #B87333; border-radius:2px;"></span> Bottle</span>
        <span style="font-size: 7pt; color: #555;"><span class="check-box" style="display:inline-block; width:8px; height:8px; border:1px solid #B87333; border-radius:2px;"></span> Can</span>
      </div>
    </div>
  </div>

  <div style="font-size: 8pt; font-weight: 700; color: #B87333; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px; margin-top: 4px;">
    Sensory Ratings (1 = faint, 5 = intense)
  </div>

  <div class="rating-group">
    <div class="rating-row">
      <span class="rr-label">Hop Bitterness</span>
      %s
    </div>
    <div class="rating-row">
      <span class="rr-label">Malt Sweetness</span>
      %s
    </div>
    <div class="rating-row">
      <span class="rr-label">Body</span>
      %s
    </div>
    <div class="rating-row">
      <span class="rr-label">Carbonation</span>
      %s
    </div>
    <div class="rating-row">
      <span class="rr-label">Aroma</span>
      %s
    </div>
    <div class="rating-row">
      <span class="rr-label">Finish</span>
      %s
    </div>
  </div>
</div>""" % (pg, session_num, pg, session_num,
             rating_circles_html(5), rating_circles_html(5), rating_circles_html(5),
             rating_circles_html(5), rating_circles_html(5), rating_circles_html(5))


def tasting_right():
    pg = pn()
    flavors = [
        "Citrus", "Pine", "Tropical", "Floral",
        "Caramel", "Chocolate", "Coffee", "Roasted",
        "Smoke", "Spice", "Clove", "Banana",
        "Tart", "Sour", "Funky", "Bready",
        "Biscuit", "Toffee", "Dried Fruit", "Herbal",
    ]
    flavor_items = flavor_items_html(flavors)

    return """<!-- PAGE %d: Tasting Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Flavor Notes</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div style="font-size: 8pt; font-weight: 700; color: #B87333; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">
    Flavor Checklist (check all that apply)
  </div>

  <div class="flavor-grid" style="border: 1px solid #C4A04A; border-radius: 4px; padding: 6px; margin-bottom: 8px;">
    %s
  </div>

  <div class="write-box">
    <div class="wb-label">Appearance (Color, Clarity, Head)</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Aroma Notes</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Overall Tasting Notes</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
    <div class="write-box">
      <div class="wb-label">Overall Rating</div>
      <div class="stars">&#9734; &#9734; &#9734; &#9734; &#9734;</div>
    </div>
    <div class="write-box">
      <div class="wb-label">Would Drink Again?</div>
      <div style="display: flex; gap: 8px; padding-top: 2px; font-size: 8pt; color: #555;">
        <span><span class="check-box" style="display:inline-block; width:10px; height:10px; border:1px solid #B87333; border-radius:2px;"></span> Yes</span>
        <span><span class="check-box" style="display:inline-block; width:10px; height:10px; border:1px solid #B87333; border-radius:2px;"></span> Maybe</span>
        <span><span class="check-box" style="display:inline-block; width:10px; height:10px; border:1px solid #B87333; border-radius:2px;"></span> No</span>
      </div>
    </div>
  </div>

  <div class="write-box">
    <div class="wb-label">Food Pairing Suggestion</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg, flavor_items)


def year_review_page():
    pg = pn()
    cards = [
        "Total Tastings", "Styles Explored", "Top Beer of the Year",
        "Favorite Brewery", "Biggest Surprise", "Most Memorable Pour",
    ]
    grid = ""
    for label in cards:
        grid += """<div class="review-card">
  <div class="rc-label">%s</div>
  <div class="rc-write"></div>
</div>
""" % H.escape(label)

    return """<!-- PAGE %d: Year in Review -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Year in Review</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">My Beer Year</div>
    <div class="section-line"></div>
  </div>

  <div class="review-grid">
    %s
  </div>

  <div class="write-box">
    <div class="wb-label">New Styles I Discovered</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Breweries I Want to Visit Next Year</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>
</div>""" % (pg, pg, grid)


def notes_page():
    pg = pn()
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes</span>
    <span class="ph-right">Page %d</span>
  </div>
  <div>%s</div>
</div>""" % (pg, pg, nl(28))


def final_page():
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="page">
  <div class="final-page">
    <div class="fp-text">
      Here's to good beer<br>
      and the stories<br>
      behind every pour.
    </div>
    <div class="fp-line"></div>
    <div class="fp-logo">More Shine Press</div>
    <div class="fp-line"></div>
  </div>
</div>""" % pg


# ============================================================
# MAIN
# ============================================================
def generate(output_path=HTML_FILE):
    pages = []

    # 1. Title
    pages.append(interior_title_page())

    # 2. How to use
    pages.append(how_to_use_page())

    # 3-4. Style guide (2 pages)
    pages.append(style_guide_page_1())
    pages.append(style_guide_page_2())

    # 5. Flavor wheel
    pages.append(flavor_wheel_page())

    # 6. Glassware
    pages.append(glassware_page())

    # 7-8. Brewery tracker (2 pages)
    pages.append(brewery_tracker_page())
    pages.append(brewery_tracker_page())

    # 9. Terminology
    pages.append(terminology_page())

    # 10-89. 40 tasting spreads (2 pages each = 80 pages)
    for session in range(1, 41):
        pages.append(tasting_left(session))
        pages.append(tasting_right())

    # 90. Year in review
    pages.append(year_review_page())

    # 91-93. Notes
    for _ in range(3):
        pages.append(notes_page())

    # 94. Final
    pages.append(final_page())

    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>%s</title>
  <style>%s</style>
</head>
<body>
%s
</body>
</html>""" % (H.escape(BOOK_TITLE), CSS, "\n".join(pages))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    return output_path, page_no[0]


if __name__ == "__main__":
    path, count = generate()
    print("[OK] Interior generated: %s" % path)
    print("     Total pages: %d" % count)
