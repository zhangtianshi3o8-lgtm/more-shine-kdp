#!/usr/bin/env python3
"""
Coffee Tasting Log Book — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: American coffee enthusiasts (all levels, all brewing methods)
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "coffee_tasting_log_book_us_V1.0.html")

BOOK_TITLE = "Coffee Tasting Log Book"
BOOK_SUBTITLE = "Track Every Cup, Every Origin, Every Flavor"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

# ============================================================
# CSS  (raw string — never f-string, to avoid backslash issues)
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

/* ---- Colors ---- */
/* Espresso: #3B2417, #4A3020 */
/* Coffee: #6F4E37, #8B5E3C */
/* Caramel/Gold: #C8A041, #D4A017 */
/* Cream: #FAF6F0, #F5EDE3 */
/* Mocha: #A0826D */
/* Foam: #F8F0E3 */

.page {
  width: 6in; height: 9in;
  padding: 0.45in 0.5in 0.38in 0.5in;
  page-break-after: always;
  position: relative;
  background: white;
  overflow: hidden;
}
.page:last-child { page-break-after: auto; }

@media screen { .page { border: 1px dashed #ccc; margin: 8px auto; } }
@media print  { .page { border: none; margin: 0; } }

/* ================ COVER (INTERIOR TITLE PAGE) ================ */
.cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(165deg, #2A1810 0%, #3B2417 25%, #4A3020 55%, #3B2417 85%, #2A1810 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Coffee bean texture */
.cover .bean-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 24px 14px at 15% 20%, #C8A041, transparent),
    radial-gradient(ellipse 22px 13px at 80% 15%, #C8A041, transparent),
    radial-gradient(ellipse 26px 15px at 70% 70%, #C8A041, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, #C8A041, transparent),
    radial-gradient(ellipse 18px 11px at 50% 45%, #C8A041, transparent),
    radial-gradient(ellipse 22px 13px at 10% 55%, #C8A041, transparent),
    radial-gradient(ellipse 16px 10px at 90% 40%, #C8A041, transparent),
    radial-gradient(ellipse 14px 9px at 40% 90%, #C8A041, transparent);
}

/* CSS Coffee Cup illustration */
.cover .cup-wrap {
  width: 130px; height: 100px;
  position: relative;
  margin: 0 auto 24px;
}

/* Cup body — trapezoid */
.cover .cup-body {
  width: 100px; height: 70px;
  background: linear-gradient(180deg, #FAF6F0 0%, #F0E6D6 100%);
  position: absolute;
  top: 15px; left: 5px;
  border-radius: 0 0 12px 12px;
  clip-path: polygon(8% 0, 92% 0, 82% 100%, 18% 100%);
  box-shadow: 2px 2px 8px rgba(0,0,0,0.4);
}

/* Cup rim — ellipse at top */
.cover .cup-rim {
  width: 100px; height: 16px;
  background: #3B2417;
  border-radius: 50%;
  position: absolute;
  top: 10px; left: 5px;
  border: 2px solid #FAF6F0;
  box-shadow: 0 2px 6px rgba(0,0,0,0.3);
}

/* Coffee surface inside cup */
.cover .cup-coffee {
  width: 90px; height: 12px;
  background: linear-gradient(180deg, #6F4E37 0%, #3B2417 100%);
  border-radius: 50%;
  position: absolute;
  top: 12px; left: 10px;
}

/* Crema swirl */
.cover .cup-crema {
  width: 40px; height: 5px;
  background: rgba(200,160,65,0.5);
  border-radius: 50%;
  position: absolute;
  top: 14px; left: 30px;
  transform: rotate(-15deg);
}

/* Cup handle */
.cover .cup-handle {
  width: 28px; height: 32px;
  border: 5px solid #FAF6F0;
  border-left: none;
  border-radius: 0 50% 50% 0;
  position: absolute;
  top: 30px; left: 100px;
  box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
}

/* Saucer */
.cover .cup-saucer {
  width: 120px; height: 12px;
  background: #F0E6D6;
  border-radius: 50%;
  position: absolute;
  top: 82px; left: 5px;
  box-shadow: 2px 3px 8px rgba(0,0,0,0.4);
}

/* Steam */
.cover .steam1 {
  width: 3px; height: 30px;
  background: linear-gradient(180deg, transparent, rgba(250,246,240,0.4), transparent);
  position: absolute;
  top: -15px; left: 30px;
  border-radius: 50%;
  transform: rotate(-10deg);
}
.cover .steam2 {
  width: 3px; height: 35px;
  background: linear-gradient(180deg, transparent, rgba(250,246,240,0.3), transparent);
  position: absolute;
  top: -20px; left: 55px;
  border-radius: 50%;
  transform: rotate(8deg);
}
.cover .steam3 {
  width: 3px; height: 28px;
  background: linear-gradient(180deg, transparent, rgba(250,246,240,0.25), transparent);
  position: absolute;
  top: -12px; left: 75px;
  border-radius: 50%;
  transform: rotate(-5deg);
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 30pt;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.15;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 6px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 110px; height: 2.5px;
  background: #C8A041;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 11pt;
  color: #D4B896;
  font-style: italic;
  line-height: 1.5;
  margin-bottom: 20px;
}

.cover .features {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.cover .feature-badge {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(200,160,65,0.4);
  color: #C8A041;
  font-size: 7pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 9px;
  border-radius: 3px;
  text-transform: uppercase;
}

.cover .tagline {
  font-size: 8.5pt;
  color: #D4B896;
  letter-spacing: 2pt;
  text-transform: uppercase;
  margin-top: 8px;
}

.cover .publisher {
  position: absolute;
  bottom: 0.4in;
  left: 0; right: 0;
  text-align: center;
  font-size: 9pt;
  color: #C8A041;
  letter-spacing: 2pt;
  text-transform: uppercase;
  font-weight: 700;
}

/* ================ SECTION DIVIDER ================ */
.divider {
  width: 6in; height: 9in;
  page-break-after: always;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  background: linear-gradient(165deg, #2A1810 0%, #3B2417 50%, #2A1810 100%);
  position: relative;
  overflow: hidden;
}

.divider .div-bean {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C8A041, transparent),
    radial-gradient(ellipse 25px 15px at 80% 30%, #C8A041, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #C8A041, transparent),
    radial-gradient(ellipse 18px 11px at 25% 85%, #C8A041, transparent);
}

.divider .div-num {
  font-size: 60pt;
  color: rgba(200,160,65,0.12);
  font-weight: 700;
  position: absolute;
  top: 1in;
}

.divider .div-label {
  font-size: 10pt;
  color: #C8A041;
  letter-spacing: 3pt;
  text-transform: uppercase;
  margin-bottom: 10px;
  position: relative;
}

.divider .div-title {
  font-size: 24pt;
  color: #ffffff;
  font-weight: 700;
  line-height: 1.2;
  position: relative;
  padding: 0 0.6in;
}

.divider .div-sub {
  font-size: 11pt;
  color: #D4B896;
  font-style: italic;
  margin-top: 14px;
  position: relative;
}

/* ================ CONTENT PAGES ================ */
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 7.5pt;
  color: #999;
  padding-bottom: 4px;
  border-bottom: 1.5px solid #6F4E37;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #3B2417;
  text-transform: uppercase;
}
.section-header .sh-right {
  color: #aaa;
}

.page-footer {
  position: absolute;
  bottom: 0.22in;
  left: 0.5in; right: 0.5in;
  font-size: 6.5pt;
  color: #bbb;
  display: flex;
  justify-content: space-between;
  border-top: 0.5px solid #eee;
  padding-top: 3px;
}

.page-title {
  font-size: 14pt;
  font-weight: 700;
  color: #3B2417;
  margin-bottom: 3px;
}

.page-subtitle {
  font-size: 8pt;
  color: #888;
  font-style: italic;
  margin-bottom: 12px;
}

/* ---- Writing Lines ---- */
.wline {
  border-bottom: 0.5px solid #ccc;
  height: 22px;
  margin-bottom: 2px;
}
.wline-sm {
  border-bottom: 0.5px solid #ddd;
  height: 18px;
  margin-bottom: 1px;
}

/* ---- Data Tables ---- */
table.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
}
table.data-table th {
  background: #6F4E37;
  color: white;
  font-weight: 700;
  text-align: left;
  padding: 4px 5px;
  font-size: 7pt;
  letter-spacing: 0.3pt;
  text-transform: uppercase;
}
table.data-table td {
  padding: 4px 5px;
  border-bottom: 0.5px solid #ddd;
  vertical-align: top;
}
table.data-table tr:nth-child(even) td {
  background: #FAF6F0;
}

/* ---- Field Grid ---- */
.field-grid {
  display: grid;
  gap: 6px;
  margin-bottom: 8px;
}
.field-row {
  display: flex;
  gap: 8px;
  align-items: baseline;
}
.field-label {
  font-size: 7.5pt;
  font-weight: 700;
  color: #3B2417;
  text-transform: uppercase;
  letter-spacing: 0.4pt;
  white-space: nowrap;
  min-width: 60px;
}
.field-line {
  flex: 1;
  border-bottom: 0.5px solid #bbb;
  height: 16px;
}

/* ---- Checkbox Row ---- */
.check-row {
  display: flex;
  flex-wrap: wrap;
  gap: 5px 10px;
  font-size: 8pt;
  color: #555;
  align-items: center;
}
.check-row .check-item {
  display: inline-flex;
  align-items: center;
  gap: 3px;
}
.check-box {
  width: 10px; height: 10px;
  border: 1px solid #888;
  border-radius: 2px;
  display: inline-block;
}

/* ---- Star Rating ---- */
.stars {
  font-size: 13pt;
  color: #ccc;
  letter-spacing: 2pt;
}

/* ---- Info Box ---- */
.info-box {
  background: #FAF6F0;
  border-left: 3px solid #6F4E37;
  padding: 8px 10px;
  margin-bottom: 10px;
  font-size: 8pt;
  color: #333;
  line-height: 1.5;
}
.info-box .info-title {
  font-weight: 700;
  color: #3B2417;
  font-size: 8.5pt;
  margin-bottom: 4px;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
}

/* ---- Rating Bars (1-5 scale) ---- */
.rating-bar-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 5px;
}
.rating-bar-label {
  font-size: 7pt;
  font-weight: 700;
  color: #3B2417;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  min-width: 68px;
}
.rating-bar-circles {
  display: flex;
  gap: 4px;
}
.rating-circle {
  width: 14px; height: 14px;
  border: 1.5px solid #6F4E37;
  border-radius: 50%;
  display: inline-block;
}

/* ---- Flavor Category Card ---- */
.flavor-cat {
  border: 1px solid #e0d8cc;
  border-radius: 4px;
  padding: 6px 8px;
  margin-bottom: 5px;
  background: #FCFAF7;
}
.flavor-cat-label {
  font-size: 7pt;
  font-weight: 700;
  color: #6F4E37;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 3px;
}
.flavor-cat-notes {
  font-size: 7.5pt;
  color: #888;
  line-height: 1.5;
}

/* ---- Stat Card ---- */
.stat-card {
  text-align: center;
  padding: 6px 4px;
  background: #FAF6F0;
  border-radius: 4px;
  border: 1px solid #E8DDD0;
}
.stat-card .stat-label {
  font-size: 6.5pt;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 2px;
}
.stat-card .stat-value {
  font-size: 11pt;
  font-weight: 700;
  color: #3B2417;
}

/* ---- Gear Card ---- */
.gear-card {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 8px;
  margin-bottom: 6px;
  background: #FCFAF7;
}
.gear-card .gear-label {
  font-size: 7pt;
  font-weight: 700;
  color: #6F4E37;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 4px;
}
.gear-card .gear-line {
  border-bottom: 0.5px solid #ddd;
  height: 16px;
  margin-bottom: 2px;
}

/* ---- Dot Grid ---- */
.dot-grid {
  background-image: radial-gradient(circle, #d0d0d0 1px, transparent 1px);
  background-size: 0.20in 0.20in;
  background-position: 0.10in 0.10in;
}

/* ---- Origin List ---- */
table.origin-list th {
  background: #8B5E3C;
}
table.origin-list td:first-child {
  width: 22px;
  text-align: center;
  font-weight: 700;
  color: #8B5E3C;
}
table.origin-list td:last-child {
  width: 28px;
  text-align: center;
}
"""

# ============================================================
# PAGE BUILDERS
# ============================================================

def cover():
    return f'''
<!-- Page {pn()}: Cover -->
<div class="cover">
  <div class="bean-bg"></div>
  <div class="cup-wrap">
    <div class="steam1"></div>
    <div class="steam2"></div>
    <div class="steam3"></div>
    <div class="cup-saucer"></div>
    <div class="cup-body"></div>
    <div class="cup-handle"></div>
    <div class="cup-rim"></div>
    <div class="cup-coffee"></div>
    <div class="cup-crema"></div>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">40 Tasting Sessions</span>
      <span class="feature-badge">Flavor Wheel</span>
      <span class="feature-badge">Brewing Tracker</span>
      <span class="feature-badge">Bean Inventory</span>
    </div>
    <div class="tagline">For Coffee Lovers &amp; Home Brewers</div>
  </div>
  <div class="publisher">More Shine Press</div>
</div>
'''


def owner_page():
    return f'''
<!-- Page {pn()}: Owner -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">This Book Belongs To</span>
    <span class="sh-right"></span>
  </div>

  <div style="height: 2.5in;"></div>

  <div style="text-align: center; margin-bottom: 30px;">
    <div style="font-size: 16pt; font-weight: 700; color: #3B2417; margin-bottom: 6px;">This Log Book Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #3B2417; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #6F4E37; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Origin</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #6F4E37; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Brewing Method</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #6F4E37; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Daily Cups</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #6F4E37; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Coffee Shop I Frequent</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Coffee Tasting Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def how_to_use():
    return f'''
<!-- Page {pn()}: How to Use -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Getting Started</span>
    <span class="sh-right">More Shine Press</span>
  </div>

  <div class="page-title">How to Use This Log Book</div>
  <div class="page-subtitle">Make every cup a learning experience</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Coffee Log?</div>
    The difference between drinking coffee and understanding coffee is attention. A tasting log helps you discover patterns &mdash; which origins you gravitate toward, how grind size affects flavor, what brewing methods bring out the best in each bean. Over time, your log becomes your personal coffee roadmap.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #3B2417; font-size: 10pt; margin-bottom: 6px;">Tips for Better Tasting</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Taste with intention.</strong> Before you drink, pause. Smell the coffee. Take a small sip and let it coat your tongue. Note the first flavors that come to mind &mdash; these initial impressions are the most honest.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Record the basics.</strong> Origin, process, roast level, and brewing method are the foundation. The more consistently you log these, the easier it becomes to spot what you love.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Rate the fundamentals.</strong> Acidity, body, sweetness, and aftertaste are the building blocks of every cup. Rate each on a 1&ndash;5 scale. These numbers reveal your preferences over time.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Use the flavor wheel.</strong> The flavor categories on the reference page help you find the right words. Chocolate, citrus, berry, floral &mdash; trained cuppers use these terms, and so can you.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Compare and contrast.</strong> Taste two coffees side by side when you can. The differences become obvious when you have a reference point. Note what stood out in each.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Pro Tip:</strong> Let your coffee cool for a few minutes before tasting. Flavors bloom as the temperature drops. The sweet spot is around 140&ndash;160&deg;F.
  </div>

  <div class="page-footer">
    <span>Coffee Tasting Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def flavor_wheel():
    categories = [
        ("Fruity",
         "Berry (blueberry, strawberry, raspberry, blackberry) &bull; Citrus (orange, lemon, grapefruit, lime) &bull; Stone Fruit (peach, apricot, cherry, plum) &bull; Tropical (mango, pineapple, coconut, lychee)"),
        ("Floral",
         "Jasmine &bull; Rose &bull; Hibiscus &bull; Chamomile &bull; Tea-like &bull; Elderflower"),
        ("Sweet &amp; Syrup",
         "Honey &bull; Maple Syrup &bull; Caramel &bull; Brown Sugar &bull; Molasses &bull; Vanilla &bull; Butterscotch"),
        ("Nutty &amp; Cocoa",
         "Dark Chocolate &bull; Milk Chocolate &bull; Cocoa Powder &bull; Almond &bull; Hazelnut &bull; Walnut &bull; Peanut"),
        ("Spices",
         "Cinnamon &bull; Clove &bull; Black Pepper &bull; Nutmeg &bull; Ginger &bull; Cardamom"),
        ("Roasted",
         "Toasty &bull; Smoky &bull; Tobacco &bull; Burnt Sugar &bull; Charred &bull; Pipe Tobacco"),
        ("Vegetal &amp; Green",
         "Grassy &bull; Herbal &bull; Olive &bull; Green Tea &bull; Pea &bull; Hay &bull; Fresh Herbs"),
        ("Fermented &amp; Other",
         "Winey &bull; Whisky &bull; Rum &bull; Fermented &bull; Funky &bull; Earthy &bull; Mushroom"),
    ]

    rows = ""
    for cat, notes in categories:
        rows += f'''
      <div class="flavor-cat">
        <div class="flavor-cat-label">{cat}</div>
        <div class="flavor-cat-notes">{notes}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Flavor Wheel -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Flavor Categories</span>
  </div>

  <div class="page-title">Coffee Flavor Wheel</div>
  <div class="page-subtitle">Find the words for what you taste</div>

  {rows}

  <div style="margin-top: 8px; padding: 6px 8px; background: #FAF6F0; border-radius: 3px; font-size: 7pt; color: #888; font-style: italic;">
    Use these categories as a starting point. Your palate is unique &mdash; trust your own descriptions. The goal is to recognize patterns in what you enjoy.
  </div>

  <div class="page-footer">
    <span>Coffee Tasting Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def brewing_methods_reference():
    methods = [
        ("Pour Over", "Clean, bright cup that highlights subtle flavors. Requires a gooseneck kettle and practice with pour technique.", "Best for: Light roasts, single-origin beans"),
        ("French Press", "Full-bodied, rich cup with heavy mouthfeel. Immersion brewing extracts oils and sediment. No paper filter needed.", "Best for: Medium and dark roasts, bold flavors"),
        ("Espresso", "Concentrated, intense shot with crema. Requires an espresso machine and fine grind. The base for lattes and cappuccinos.", "Best for: Blends, medium-dark to dark roasts"),
        ("Cold Brew", "Smooth, low-acidity coffee steeped in cold water for 12&ndash;24 hours. Naturally sweet and mellow.", "Best for: Hot summer days, sensitive stomachs"),
        ("Moka Pot", "Stovetop brewing that produces strong, espresso-like coffee. Rich and bold without expensive equipment.", "Best for: Strong coffee lovers on a budget"),
        ("Drip Coffee", "Automatic and convenient. Consistent results with minimal effort. The everyday workhorse of coffee brewing.", "Best for: Busy mornings, larger batches"),
        ("Siphon", "Dramatic vacuum brewing that produces a very clean, delicate cup. A showpiece method for coffee enthusiasts.", "Best for: Delicate, floral, light-roast coffees"),
        ("Turkish", "Finely ground coffee simmered in a special pot (cezve). Unfiltered, thick, and traditionally sweetened.", "Best for: Cultural experience, strong and bold palates"),
    ]

    rows = ""
    for name, desc, best in methods:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #6F4E37; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 72px; font-size: 8pt; font-weight: 700; color: #3B2417;">{name}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4; flex: 1;">{desc}<br><span style="color: #6F4E37; font-weight: 700;">{best}</span></div>
      </div>'''

    return f'''
<!-- Page {pn()}: Brewing Methods -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Common Brewing Methods</span>
  </div>

  <div class="page-title">Brewing Methods Guide</div>
  <div class="page-subtitle">How you brew shapes what you taste</div>

  {rows}

  <div class="page-footer">
    <span>Coffee Tasting Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def growing_regions_reference():
    regions = [
        ("Ethiopia", "The birthplace of coffee. Bright, floral, tea-like, with notes of jasmine, bergamot, and blueberry. Complex and elegant."),
        ("Colombia", "Balanced and approachable. Medium body, bright acidity, with caramel, nut, and citrus notes. A crowd favorite."),
        ("Brazil", "Low acidity, heavy body, with chocolate, nut, and caramel flavors. The backbone of many espresso blends."),
        ("Guatemala", "Complex and full-bodied. Notes of cocoa, spice, and dark fruit. Bright finish with wine-like acidity."),
        ("Kenya", "Bold and juicy. Wine-like acidity with blackberry, black currant, and tomato notes. Distinctive and memorable."),
        ("Costa Rica", "Clean and sweet. Classic cup with citrus, honey, and caramel notes. High-grown beans with bright acidity."),
        ("Indonesia (Sumatra)", "Earthy, full-bodied, and low in acidity. Notes of cedar, tobacco, dark chocolate, and mushroom. Bold and savory."),
        ("Honduras", "Mild and sweet. Notes of caramel, brown sugar, and citrus. Increasingly recognized for quality."),
        ("Panama", "Home of some of the world's most sought-after coffees. Delicate, floral, jasmine, and bergamot. Bright and tea-like."),
        ("Yemen", "Wild, complex, and earthy. Winey, dried fruit, and chocolate notes. One of the oldest coffee origins."),
        ("Rwanda", "Clean, sweet, and complex. Notes of red apple, cherry, and black tea. Bright with a syrupy body."),
        ("Peru", "Smooth and mild. Notes of nuts, caramel, and gentle citrus. Often organic and fair-trade certified."),
    ]

    rows = ""
    for country, desc in regions:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #8B5E3C; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 105px; font-size: 8.5pt; font-weight: 700; color: #3B2417;">{country}</div>
        <div style="font-size: 7.5pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Growing Regions -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Coffee Belt Origins</span>
  </div>

  <div class="page-title">Coffee Growing Regions</div>
  <div class="page-subtitle">Where your coffee comes from shapes what it tastes like</div>

  {rows}

  <div class="page-footer">
    <span>Coffee Tasting Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def tasting_terms_reference():
    terms = [
        ("Acidity", "The bright, lively, tangy quality of coffee. Not the same as bitterness. A good acidity is pleasant and crisp, like a lemon or apple. Often called brightness."),
        ("Body", "The weight and texture of coffee in your mouth. Can be thin and tea-like, or heavy and syrupy. Also called mouthfeel."),
        ("Sweetness", "The natural, pleasant sweetness in coffee. Not added sugar. Caramel, honey, and brown sugar notes indicate sweetness."),
        ("Bitterness", "A sharp, sometimes harsh quality. In small amounts it adds complexity. Too much can overpower other flavors. Dark roasts tend to be more bitter."),
        ("Aftertaste", "The flavors that linger after swallowing. Also called the finish. Can be short and clean, or long and lingering."),
        ("Balance", "How well acidity, body, sweetness, and bitterness work together. A balanced coffee has no single element dominating the others."),
        ("Complexity", "The range and layering of flavors. A complex coffee reveals different notes as it cools. Simple coffees taste one-dimensional."),
        ("Clean Cup", "A coffee with no off-flavors or interference. Clarity and transparency of flavor. The opposite of muddy or murky."),
    ]

    rows = ""
    for term, desc in terms:
        rows += f'''
      <div style="border: 1px solid #e0d8cc; border-radius: 3px; padding: 7px 9px; margin-bottom: 6px; background: #FCFAF7;">
        <div style="font-size: 9.5pt; font-weight: 700; color: #3B2417; margin-bottom: 3px;">{term}</div>
        <div style="font-size: 8pt; color: #555; line-height: 1.5;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Tasting Terms -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Cupping Vocabulary</span>
  </div>

  <div class="page-title">Tasting Terminology</div>
  <div class="page-subtitle">Speak the language of coffee</div>

  {rows}

  <div class="page-footer">
    <span>Coffee Tasting Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def divider_section(num, label, title, subtitle):
    labels = ["One", "Two", "Three", "Four", "Five", "Six"]
    label_text = labels[num-1] if num <= 6 else label
    return f'''
<!-- Page {pn()}: Divider -->
<div class="divider">
  <div class="div-bean"></div>
  <div class="div-num">{num:02d}</div>
  <div class="div-label">Part {label_text}</div>
  <div class="div-title">{title}</div>
  <div class="div-sub">{subtitle}</div>
</div>
'''


def tasting_log_left(session_num):
    """Left page of two-page tasting spread — coffee info + brewing + flavor ratings"""
    return f'''
<!-- Page {pn()}: Session {session_num} Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Session #{session_num:02d}</span>
    <span class="sh-right">Coffee Tasting Log Book</span>
  </div>

  <div class="page-title">Tasting #{session_num:02d}</div>
  <div class="page-subtitle">Coffee Details &amp; Brewing Parameters</div>

  <!-- Coffee Info -->
  <div style="background: #FAF6F0; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; min-width: 36px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; min-width: 36px;">Time</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; min-width: 42px;">Coffee</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; min-width: 36px;">Origin</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; min-width: 42px;">Roaster</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; min-width: 48px;">Roast Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; min-width: 36px;">Price</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Process -->
  <div style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Process</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Washed</span>
    <span class="check-item"><span class="check-box"></span> Natural</span>
    <span class="check-item"><span class="check-box"></span> Honey</span>
    <span class="check-item"><span class="check-box"></span> Wet-Hulled</span>
    <span class="check-item"><span class="check-box"></span> Anaerobic</span>
  </div>

  <!-- Roast Level -->
  <div style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Roast Level</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Light</span>
    <span class="check-item"><span class="check-box"></span> Medium-Light</span>
    <span class="check-item"><span class="check-box"></span> Medium</span>
    <span class="check-item"><span class="check-box"></span> Medium-Dark</span>
    <span class="check-item"><span class="check-box"></span> Dark</span>
  </div>

  <!-- Brewing Method -->
  <div style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Brewing Method</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Pour Over</span>
    <span class="check-item"><span class="check-box"></span> French Press</span>
    <span class="check-item"><span class="check-box"></span> Espresso</span>
    <span class="check-item"><span class="check-box"></span> Cold Brew</span>
    <span class="check-item"><span class="check-box"></span> Moka Pot</span>
    <span class="check-item"><span class="check-box"></span> Drip</span>
    <span class="check-item"><span class="check-box"></span> Siphon</span>
    <span class="check-item"><span class="check-box"></span> Turkish</span>
  </div>

  <!-- Brewing Parameters -->
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 10px;">
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #6F4E37; text-transform: uppercase;">Grind Size</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #6F4E37; text-transform: uppercase;">Water Temp</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #6F4E37; text-transform: uppercase;">Dose (g)</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #6F4E37; text-transform: uppercase;">Yield (g)</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #6F4E37; text-transform: uppercase;">Ratio</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #6F4E37; text-transform: uppercase;">Brew Time</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
  </div>

  <!-- Flavor Ratings (1-5 scale) -->
  <div style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Flavor Ratings &mdash; Fill in circles (1 = weak, 5 = strong)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Acidity</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Body</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Sweetness</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Bitterness</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Aftertaste</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Balance</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>

  <div class="page-footer">
    <span>Session #{session_num:02d} &mdash; Details</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def tasting_log_right(session_num):
    """Right page of two-page tasting spread — flavor notes, rating, freeform"""
    return f'''
<!-- Page {pn()}: Session {session_num} Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Session #{session_num:02d}</span>
    <span class="sh-right">Flavor Notes &amp; Impressions</span>
  </div>

  <div class="page-title">Tasting Notes #{session_num:02d}</div>
  <div class="page-subtitle">Flavors, aromas, and your overall impression</div>

  <!-- Aroma -->
  <div style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Aroma (Dry &amp; Wet)</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Flavor Notes Checklist -->
  <div style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Flavor Notes &mdash; Check What You Taste</div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Chocolate</span>
    <span class="check-item"><span class="check-box"></span> Caramel</span>
    <span class="check-item"><span class="check-box"></span> Nutty</span>
    <span class="check-item"><span class="check-box"></span> Vanilla</span>
    <span class="check-item"><span class="check-box"></span> Honey</span>
    <span class="check-item"><span class="check-box"></span> Brown Sugar</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Citrus</span>
    <span class="check-item"><span class="check-box"></span> Berry</span>
    <span class="check-item"><span class="check-box"></span> Stone Fruit</span>
    <span class="check-item"><span class="check-box"></span> Tropical</span>
    <span class="check-item"><span class="check-box"></span> Floral</span>
    <span class="check-item"><span class="check-box"></span> Apple</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Cinnamon</span>
    <span class="check-item"><span class="check-box"></span> Clove</span>
    <span class="check-item"><span class="check-box"></span> Earthy</span>
    <span class="check-item"><span class="check-box"></span> Smoky</span>
    <span class="check-item"><span class="check-box"></span> Tobacco</span>
    <span class="check-item"><span class="check-box"></span> Winey</span>
  </div>

  <!-- Other flavors -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-top: 4px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; min-width: 50px;">Other</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Overall Rating -->
  <div style="display: flex; align-items: center; gap: 8px; margin-top: 8px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; letter-spacing: 0.4pt;">Overall Rating</span>
    <span class="stars">&starf; &starf; &starf; &starf; &starf;</span>
  </div>

  <!-- Would Buy Again? -->
  <div class="check-row" style="margin-bottom: 10px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Would Buy Again</span>
    <span class="check-item"><span class="check-box"></span> Would Recommend</span>
    <span class="check-item"><span class="check-box"></span> New Favorite</span>
  </div>

  <!-- Tasting Notes (freeform) -->
  <div style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Detailed Tasting Notes</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- What to Try Next Time -->
  <div style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">What to Adjust Next Time</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Session #{session_num:02d} &mdash; Notes</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def bean_inventory(page_of, total_pages):
    """Bean purchase inventory page"""
    return f'''
<!-- Page {pn()}: Bean Inventory -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Bean Inventory</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Bean Collection</div>
  <div class="page-subtitle">Keep track of what you have and what to restock</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Coffee / Origin</th>
      <th style="width:58px;">Roaster</th>
      <th style="width:40px;">Process</th>
      <th style="width:42px;">Roast Lvl</th>
      <th style="width:38px;">Roast Date</th>
      <th style="width:30px;">Rating</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">1</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">2</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">3</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">4</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">5</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">6</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">7</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">8</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">9</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">10</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">11</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">12</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Rating: 1&ndash;5 (5 = best) | Roast Lvl: L/ML/M/MD/D</div>

  <div class="page-footer">
    <span>Coffee Tasting Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def roaster_log(page_of, total_pages):
    """Favorite roasters and coffee shops"""
    return f'''
<!-- Page {pn()}: Roaster Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Roasters &amp; Shops</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Roaster &amp; Coffee Shop Log</div>
  <div class="page-subtitle">Where to find great beans</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Name</th>
      <th style="width:70px;">Location</th>
      <th style="width:62px;">Specialty</th>
      <th>Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">6</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">7</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">8</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">9</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">10</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">11</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B5E3C;">12</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Go-To Shop</div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #6F4E37; text-transform: uppercase; min-width: 38px;">Name</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #6F4E37; text-transform: uppercase; min-width: 38px;">Why I Love It</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #6F4E37; text-transform: uppercase; min-width: 38px;">Usual Order</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Coffee Tasting Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def brew_equipment():
    """Brewing equipment inventory"""
    return f'''
<!-- Page {pn()}: Brew Equipment -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Equipment</span>
    <span class="sh-right">My Coffee Gear</span>
  </div>

  <div class="page-title">Brew Equipment</div>
  <div class="page-subtitle">Know your kit</div>

  <div class="gear-card">
    <div class="gear-label">Brewers</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Brand / Model</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Grinder</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Brand / Model</th><th>Burrs</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Kettle &amp; Scale</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Brand / Model</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Filters &amp; Accessories</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Item</th><th>Type / Size</th><th>Spare?</th></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Coffee Tasting Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def coffee_origins_checklist():
    """Coffee origins checklist — the coffee belt"""
    origins = [
        "Ethiopia", "Kenya", "Rwanda", "Burundi",
        "Yemen", "Tanzania", "Uganda", "Malawi",
        "Colombia", "Brazil", "Guatemala", "Costa Rica",
        "Honduras", "Panama", "El Salvador", "Nicaragua",
        "Peru", "Mexico", "Bolivia", "Ecuador",
        "Indonesia (Sumatra)", "Indonesia (Java)", "Indonesia (Sulawesi)", "Papua New Guinea",
        "Vietnam", "India", "Thailand", "Philippines",
        "Hawaii (USA)", "Jamaica", "Dominican Republic", "Cuba",
    ]

    rows = ""
    for i, origin in enumerate(origins, 1):
        rows += f'''
    <tr>
      <td>{i}</td>
      <td>{origin}</td>
      <td></td>
      <td></td>
      <td><span class="check-box" style="vertical-align: middle;"></span></td>
    </tr>'''

    return f'''
<!-- Page {pn()}: Origins Checklist -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Origins Checklist</span>
    <span class="sh-right">Coffee Belt Tour</span>
  </div>

  <div class="page-title">Coffee Origins Checklist</div>
  <div class="page-subtitle">Taste your way around the coffee belt</div>

  <table class="data-table origin-list" style="font-size: 7.5pt;">
    <tr>
      <th style="width:22px;">#</th>
      <th>Origin</th>
      <th style="width:70px;">First Tried</th>
      <th style="width:70px;">Rating</th>
      <th style="width:28px;">&#10003;</th>
    </tr>
    {rows}
  </table>

  <div class="page-footer">
    <span>Coffee Tasting Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def favorites_summary():
    """Year-in-review and favorites page"""
    return f'''
<!-- Page {pn()}: Favorites Summary -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Favorites &amp; Stats</span>
    <span class="sh-right">Your Coffee Year in Review</span>
  </div>

  <div class="page-title">Coffee Year in Review</div>
  <div class="page-subtitle">Fill in at the end of your tasting journey</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Cups Tasted</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Origins Tried</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Roasters Sampled</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Top 5 Coffees</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Coffee / Origin</th>
      <th style="width:55px;">Roaster</th>
      <th style="width:35px;">Rating</th>
      <th>Why It Stood Out</th>
    </tr>
    <tr><td style="font-weight:700;color:#C8A041;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C8A041;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C8A041;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C8A041;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C8A041;">5</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Personal Discoveries</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Winner</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#3B2417;">Favorite Origin</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#3B2417;">Favorite Process</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#3B2417;">Favorite Roast Level</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#3B2417;">Favorite Brewing Method</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#3B2417;">Best New Discovery</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #3B2417; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">What I Want to Explore Next</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Coffee Tasting Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def notes_page(page_num):
    """Blank lined notes page"""
    lines = ""
    for _ in range(18):
        lines += '<div class="wline"></div>\n'

    return f'''
<!-- Page {pn()}: Notes -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Notes</span>
    <span class="sh-right"></span>
  </div>

  <div class="page-title">Coffee Notes</div>
  <div class="page-subtitle">Recipes, ideas, and reminders</div>

  {lines}

  <div class="page-footer">
    <span>Coffee Tasting Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def sketch_page():
    """Dot grid page for sketching brew setups and labels"""
    return f'''
<!-- Page {pn()}: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Sketch Pad</span>
    <span class="sh-right">Brew Recipes &amp; Label Sketches</span>
  </div>

  <div class="page-title">Sketch Pad</div>
  <div class="page-subtitle">Draw brew recipes, dial in grind settings, sketch label ideas</div>

  <div class="dot-grid" style="width: 100%; height: 6.5in; border-radius: 4px;"></div>

  <div class="page-footer">
    <span>Coffee Tasting Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


# ============================================================
# MAIN — ASSEMBLE BOOK
# ============================================================

def main():
    pages = []

    # ---- Front Matter ----
    pages.append(cover())                          # 1: Cover
    pages.append(owner_page())                     # 2: Owner page

    # ---- Educational Reference ----
    pages.append(how_to_use())                     # 3: How to use
    pages.append(flavor_wheel())                   # 4: Flavor wheel
    pages.append(brewing_methods_reference())      # 5: Brewing methods
    pages.append(growing_regions_reference())      # 6: Growing regions
    pages.append(tasting_terms_reference())        # 7: Tasting terms

    # ---- Section 1: Tasting Logs ----
    pages.append(divider_section(1, "One", "Tasting Logs", "40 sessions &mdash; your coffee journey"))
    NUM_SESSIONS = 40
    for i in range(1, NUM_SESSIONS + 1):
        pages.append(tasting_log_left(i))          # Left page: details
        pages.append(tasting_log_right(i))         # Right page: notes

    # ---- Section 2: Bean Inventory ----
    pages.append(divider_section(2, "Two", "Bean Collection", "Your coffee shelf at a glance"))
    pages.append(bean_inventory(1, 3))
    pages.append(bean_inventory(2, 3))
    pages.append(bean_inventory(3, 3))

    # ---- Section 3: Roasters & Shops ----
    pages.append(divider_section(3, "Three", "Roasters &amp; Shops", "Where to find great beans"))
    pages.append(roaster_log(1, 2))
    pages.append(roaster_log(2, 2))

    # ---- Section 4: Equipment ----
    pages.append(divider_section(4, "Four", "Equipment", "Your brewing kit"))
    pages.append(brew_equipment())

    # ---- Section 5: Origins & Stats ----
    pages.append(divider_section(5, "Five", "Origins &amp; Favorites", "Your coffee world map"))
    pages.append(coffee_origins_checklist())
    pages.append(favorites_summary())
    pages.append(sketch_page())

    # ---- Section 6: Notes ----
    pages.append(divider_section(6, "Six", "Notes", "Ideas, recipes, and reminders"))
    for i in range(10):
        pages.append(notes_page(i + 1))

    # Assemble HTML
    body_content = "\n".join(pages)
    total_pages = page_no[0]

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{BOOK_TITLE} &mdash; More Shine Press</title>
<style>{CSS}</style>
</head>
<body>
{body_content}
</body>
</html>'''

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Generated: {HTML_FILE}")
    print(f"Total pages: {total_pages}")

    # Print breakdown
    print(f"\nPage breakdown:")
    print(f"  Cover: 1")
    print(f"  Owner page: 1")
    print(f"  Reference (how-to, flavor wheel, brewing, regions, terms): 5")
    print(f"  Section dividers: 6")
    print(f"  Tasting logs ({NUM_SESSIONS} sessions x 2 pages): {NUM_SESSIONS * 2}")
    print(f"  Bean inventory: 3")
    print(f"  Roaster log: 2")
    print(f"  Equipment: 1")
    print(f"  Origins checklist: 1")
    print(f"  Favorites summary: 1")
    print(f"  Sketch page: 1")
    print(f"  Notes pages: 10")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
