#!/usr/bin/env python3
"""
Tea Tasting Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: American tea enthusiasts (all levels, all steeping methods)
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "tea_tasting_journal_us_V1.0.html")

BOOK_TITLE = "Tea Tasting Journal"
BOOK_SUBTITLE = "Track Every Steep, Every Blend, Every Discovery"

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
/* Gongfu: #2A4A30, #3A5A40 */
/* Tea: #5A7A5A, #7A9B6E */
/* Caramel/Gold: #C8A041, #D4A017 */
/* Cream: #FAF6F0, #F5EDE3 */
/* Mocha: #8A9B7A */
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
  background: linear-gradient(165deg, #1A2E1F 0%, #2A4A30 25%, #3A5A40 55%, #2A4A30 85%, #1A2E1F 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Tea leaf texture */
.cover .leaf-bg {
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

/* CSS Tea Cup illustration */
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
  background: #2A4A30;
  border-radius: 50%;
  position: absolute;
  top: 10px; left: 5px;
  border: 2px solid #FAF6F0;
  box-shadow: 0 2px 6px rgba(0,0,0,0.3);
}

/* Tea surface inside cup */
.cover .cup-tea {
  width: 90px; height: 12px;
  background: linear-gradient(180deg, #5A7A5A 0%, #2A4A30 100%);
  border-radius: 50%;
  position: absolute;
  top: 12px; left: 10px;
}

/* Tea Liquor swirl */
.cover .cup-tea liquor {
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
  background: linear-gradient(165deg, #1A2E1F 0%, #2A4A30 50%, #1A2E1F 100%);
  position: relative;
  overflow: hidden;
}

.divider .div-leaf {
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
  border-bottom: 1.5px solid #5A7A5A;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #2A4A30;
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
  color: #2A4A30;
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
  background: #5A7A5A;
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
  color: #2A4A30;
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
  border-left: 3px solid #5A7A5A;
  padding: 8px 10px;
  margin-bottom: 10px;
  font-size: 8pt;
  color: #333;
  line-height: 1.5;
}
.info-box .info-title {
  font-weight: 700;
  color: #2A4A30;
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
  color: #2A4A30;
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
  border: 1.5px solid #5A7A5A;
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
  color: #5A7A5A;
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
  color: #2A4A30;
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
  color: #5A7A5A;
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
  background: #7A9B6E;
}
table.origin-list td:first-child {
  width: 22px;
  text-align: center;
  font-weight: 700;
  color: #7A9B6E;
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
  <div class="leaf-bg"></div>
  <div class="cup-wrap">
    <div class="steam1"></div>
    <div class="steam2"></div>
    <div class="steam3"></div>
    <div class="cup-saucer"></div>
    <div class="cup-body"></div>
    <div class="cup-handle"></div>
    <div class="cup-rim"></div>
    <div class="cup-tea"></div>
    <div class="cup-tea liquor"></div>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">40 Tasting Sessions</span>
      <span class="feature-badge">Flavor Wheel</span>
      <span class="feature-badge">Brewing Tracker</span>
      <span class="feature-badge">Tea Collection</span>
    </div>
    <div class="tagline">For Tea Lovers &amp; Home Brewers</div>
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
    <div style="font-size: 16pt; font-weight: 700; color: #2A4A30; margin-bottom: 6px;">This Log Book Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #2A4A30; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #5A7A5A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Origin</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #5A7A5A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Steeping Method</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #5A7A5A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Daily Cups</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #5A7A5A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Tea Shop I Frequent</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Tea Tasting Journal</span>
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
    <div class="info-title">Why Keep a Tea Log?</div>
    The difference between drinking tea and understanding tea is attention. A tasting log helps you discover patterns &mdash; which origins you gravitate toward, how leaf grade affects flavor, what steeping methods bring out the best in each leaf. Over time, your log becomes your personal tea roadmap.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #2A4A30; font-size: 10pt; margin-bottom: 6px;">Tips for Better Tasting</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Taste with intention.</strong> Before you drink, pause. Smell the tea. Take a small sip and let it coat your tongue. Note the first flavors that come to mind &mdash; these initial impressions are the most honest.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Record the basics.</strong> Origin, process, tea type, and steeping method are the foundation. The more consistently you log these, the easier it becomes to spot what you love.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Rate the fundamentals.</strong> Astringency, body, sweetness, and huigan are the building blocks of every cup. Rate each on a 1&ndash;5 scale. These numbers reveal your preferences over time.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Use the flavor wheel.</strong> The flavor categories on the reference page help you find the right words. Chestnut, citrus, berry, floral &mdash; trained cuppers use these terms, and so can you.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Compare and contrast.</strong> Taste two teas side by side when you can. The differences become obvious when you have a reference point. Note what stood out in each.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Pro Tip:</strong> Let your tea cool for a few minutes before tasting. Flavors awakening as the temperature drops. The sweet spot is around 140&ndash;160&deg;F.
  </div>

  <div class="page-footer">
    <span>Tea Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def flavor_wheel():
    categories = [
        ("Fruity",
         "Plum (blueberry, strawberry, raspberry, blackberry) &bull; Citrus (orange, lemon, grapefruit, lime) &bull; Orchid (peach, apricot, fresh leaf, plum) &bull; Tropical (mango, pineapple, coconut, lychee)"),
        ("Jasmine",
         "Jasmine &bull; Rose &bull; Hibiscus &bull; Chamomile &bull; Tea-like &bull; Elderflower"),
        ("Sweet &amp; Syrup",
         "Pan-Fired &bull; Maple Syrup &bull; Caramel &bull; Brown Sugar &bull; Molasses &bull; Vanilla &bull; Butterscotch"),
        ("Nutty &amp; Cocoa",
         "Dark Chestnut &bull; Milk Chestnut &bull; Cocoa Powder &bull; Almond &bull; Hazelnut &bull; Walnut &bull; Peanut"),
        ("Spices",
         "Honey &bull; Grassy &bull; Dried Fruit &bull; Nutmeg &bull; Ginger &bull; Cardamom"),
        ("Roasted",
         "Toasty &bull; Roasted &bull; Tobacco &bull; Burnt Sugar &bull; Charred &bull; Pipe Tobacco"),
        ("Vegetal &amp; Green",
         "Grassy &bull; Herbal &bull; Olive &bull; Green Tea &bull; Pea &bull; Hay &bull; Fresh Herbs"),
        ("Fermented &amp; Other",
         "Mineral &bull; Whisky &bull; Rum &bull; Fermented &bull; Funky &bull; Seaweed &bull; Mushroom"),
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

  <div class="page-title">Tea Flavor Wheel</div>
  <div class="page-subtitle">Find the words for what you taste</div>

  {rows}

  <div style="margin-top: 8px; padding: 6px 8px; background: #FAF6F0; border-radius: 3px; font-size: 7pt; color: #888; font-style: italic;">
    Use these categories as a starting point. Your palate is unique &mdash; trust your own descriptions. The goal is to recognize patterns in what you enjoy.
  </div>

  <div class="page-footer">
    <span>Tea Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def brewing_methods_reference():
    methods = [
        ("Gaiwan", "Clean, bright cup that highlights subtle flavors. Requires a gooseneck kettle and practice with pour technique.", "Best for: Light roasts, single-origin leaves"),
        ("Teapot", "Full-bodied, rich cup with heavy mouthfeel. Immersion brewing extracts oils and sediment. No paper filter needed.", "Best for: Medium and dark roasts, bold flavors"),
        ("Gongfu", "Concentrated, intense shot with tea liquor. Requires an gongfu machine and fine grind. The base for lattes and cappuccinos.", "Best for: Blends, medium-dark to dark roasts"),
        ("Cold Brew", "Smooth, low-astringency tea steeped in cold water for 12&ndash;24 hours. Sun-Driedly sweet and mellow.", "Best for: Hot summer days, sensitive stomachs"),
        ("Grandpa Style", "Stovetop brewing that produces strong, gongfu-like tea. Rich and bold without expensive equipment.", "Best for: Strong tea lovers on a budget"),
        ("Kyusu Tea", "Automatic and convenient. Consistent results with minimal effort. The everyday workhorse of tea brewing.", "Best for: Busy mornings, larger batches"),
        ("Samovar", "Dramatic vacuum brewing that produces a very clean, delicate cup. A showpiece method for tea enthusiasts.", "Best for: Delicate, floral, light-roast teas"),
        ("Piao Yi", "Finely ground tea simmered in a special pot (cezve). Unfiltered, thick, and traditionally sweetened.", "Best for: Cultural experience, strong and bold palates"),
    ]

    rows = ""
    for name, desc, best in methods:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #5A7A5A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 72px; font-size: 8pt; font-weight: 700; color: #2A4A30;">{name}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4; flex: 1;">{desc}<br><span style="color: #5A7A5A; font-weight: 700;">{best}</span></div>
      </div>'''

    return f'''
<!-- Page {pn()}: Steeping Methods -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Common Steeping Methods</span>
  </div>

  <div class="page-title">Steeping Methods Guide</div>
  <div class="page-subtitle">How you brew shapes what you taste</div>

  {rows}

  <div class="page-footer">
    <span>Tea Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def growing_regions_reference():
    regions = [
        ("China (Zhejiang)", "The birthplace of tea. Bright, floral, tea-like, with notes of jasmine, bergamot, and blueberry. Complex and elegant."),
        ("Japan (Shizuoka)", "Balanced and approachable. Medium body, bright astringency, with caramel, nut, and citrus notes. A crowd favorite."),
        ("India (Darjeeling)", "Low astringency, heavy body, with chocolate, nut, and caramel flavors. The backbone of many gongfu blends."),
        ("Sri Lanka (Ceylon)", "Complex and full-bodied. Notes of cocoa, spice, and dark fruit. Bright finish with wine-like astringency."),
        ("Taiwan (Alishan)", "Bold and juicy. Wine-like astringency with blackberry, black currant, and tomato notes. Distinctive and memorable."),
        ("Nepal", "Clean and sweet. Classic cup with citrus, honey, and caramel notes. High-grown leaves with bright astringency."),
        ("Vietnam (Sumatra)", "Seaweed, full-bodied, and low in astringency. Notes of cedar, tobacco, dark chocolate, and mushroom. Bold and savory."),
        ("South Korea", "Mild and sweet. Notes of caramel, brown sugar, and citrus. Increasingly recognized for quality."),
        ("Turkey (Rize)", "Home of some of the world's most sought-after teas. Delicate, floral, jasmine, and bergamot. Bright and tea-like."),
        ("Georgia", "Wild, complex, and earthy. Mineral, dried fruit, and chocolate notes. One of the oldest tea origins."),
        ("Kenya", "Clean, sweet, and complex. Notes of red apple, fresh leaf, and black tea. Bright with a syrupy body."),
        ("Rwanda", "Smooth and mild. Notes of nuts, caramel, and gentle citrus. Often organic and fair-trade certified."),
    ]

    rows = ""
    for country, desc in regions:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #7A9B6E; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 105px; font-size: 8.5pt; font-weight: 700; color: #2A4A30;">{country}</div>
        <div style="font-size: 7.5pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Growing Regions -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Tea Belt Origins</span>
  </div>

  <div class="page-title">Tea Growing Regions</div>
  <div class="page-subtitle">Where your tea comes from shapes what it tastes like</div>

  {rows}

  <div class="page-footer">
    <span>Tea Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def tasting_terms_reference():
    terms = [
        ("Astringency", "The bright, lively, tangy quality of tea. Not the same as bitterness. A good astringency is pleasant and crisp, like a lemon or apple. Often called brightness."),
        ("Body", "The weight and texture of tea in your mouth. Can be thin and tea-like, or heavy and syrupy. Also called mouthfeel."),
        ("Sweetness", "The natural, pleasant sweetness in tea. Not added sugar. Caramel, honey, and brown sugar notes indicate sweetness."),
        ("Bitterness", "A sharp, sometimes harsh quality. In small amounts it adds complexity. Too much can overpower other flavors. Dark roasts tend to be more bitter."),
        ("Huigan", "The flavors that linger after swallowing. Also called the finish. Can be short and clean, or long and lingering."),
        ("Balance", "How well astringency, body, sweetness, and bitterness work together. A balanced tea has no single element dominating the others."),
        ("Complexity", "The range and layering of flavors. A complex tea reveals different notes as it cools. Simple teas taste one-dimensional."),
        ("Clean Cup", "A tea with no off-flavors or interference. Clarity and transparency of flavor. The opposite of muddy or murky."),
    ]

    rows = ""
    for term, desc in terms:
        rows += f'''
      <div style="border: 1px solid #e0d8cc; border-radius: 3px; padding: 7px 9px; margin-bottom: 6px; background: #FCFAF7;">
        <div style="font-size: 9.5pt; font-weight: 700; color: #2A4A30; margin-bottom: 3px;">{term}</div>
        <div style="font-size: 8pt; color: #555; line-height: 1.5;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Tasting Terms -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Tasting Vocabulary</span>
  </div>

  <div class="page-title">Tasting Terminology</div>
  <div class="page-subtitle">Speak the language of tea</div>

  {rows}

  <div class="page-footer">
    <span>Tea Tasting Journal</span>
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
  <div class="div-leaf"></div>
  <div class="div-num">{num:02d}</div>
  <div class="div-label">Part {label_text}</div>
  <div class="div-title">{title}</div>
  <div class="div-sub">{subtitle}</div>
</div>
'''


def tasting_log_left(session_num):
    """Left page of two-page tasting spread — tea info + brewing + flavor ratings"""
    return f'''
<!-- Page {pn()}: Session {session_num} Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Session #{session_num:02d}</span>
    <span class="sh-right">Tea Tasting Journal</span>
  </div>

  <div class="page-title">Tasting #{session_num:02d}</div>
  <div class="page-subtitle">Tea Details &amp; Steeping Parameters</div>

  <!-- Tea Info -->
  <div style="background: #FAF6F0; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; min-width: 36px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; min-width: 36px;">Time</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; min-width: 42px;">Tea</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; min-width: 36px;">Origin</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; min-width: 42px;">Brand/Seller</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; min-width: 48px;">Harvest Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; min-width: 36px;">Price</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Process -->
  <div style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Process</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Steamed</span>
    <span class="check-item"><span class="check-box"></span> Sun-Dried</span>
    <span class="check-item"><span class="check-box"></span> Pan-Fired</span>
    <span class="check-item"><span class="check-box"></span> Rolled</span>
    <span class="check-item"><span class="check-box"></span> Oxidized</span>
  </div>

  <!-- Tea Type -->
  <div style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Tea Type</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Light</span>
    <span class="check-item"><span class="check-box"></span> Green</span>
    <span class="check-item"><span class="check-box"></span> Medium</span>
    <span class="check-item"><span class="check-box"></span> Black</span>
    <span class="check-item"><span class="check-box"></span> Dark</span>
  </div>

  <!-- Steeping Method -->
  <div style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Steeping Method</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Gaiwan</span>
    <span class="check-item"><span class="check-box"></span> Teapot</span>
    <span class="check-item"><span class="check-box"></span> Gongfu</span>
    <span class="check-item"><span class="check-box"></span> Cold Brew</span>
    <span class="check-item"><span class="check-box"></span> Grandpa Style</span>
    <span class="check-item"><span class="check-box"></span> Kyusu</span>
    <span class="check-item"><span class="check-box"></span> Samovar</span>
    <span class="check-item"><span class="check-box"></span> Piao Yi</span>
  </div>

  <!-- Steeping Parameters -->
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 10px;">
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #5A7A5A; text-transform: uppercase;">Leaf Grade</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #5A7A5A; text-transform: uppercase;">Water Temp</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #5A7A5A; text-transform: uppercase;">Leaf Amount (g)</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #5A7A5A; text-transform: uppercase;">Water (ml)</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #5A7A5A; text-transform: uppercase;">Ratio</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #5A7A5A; text-transform: uppercase;">Steep Time (sec)</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
  </div>

  <!-- Flavor Ratings (1-5 scale) -->
  <div style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Flavor Ratings &mdash; Fill in circles (1 = weak, 5 = strong)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Astringency</span>
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
    <span class="rating-bar-label">Huigan</span>
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
  <div style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Aroma (Dry &amp; Wet)</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Flavor Notes Checklist -->
  <div style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Flavor Notes &mdash; Check What You Taste</div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Chestnut</span>
    <span class="check-item"><span class="check-box"></span> Caramel</span>
    <span class="check-item"><span class="check-box"></span> Nutty</span>
    <span class="check-item"><span class="check-box"></span> Vanilla</span>
    <span class="check-item"><span class="check-box"></span> Pan-Fired</span>
    <span class="check-item"><span class="check-box"></span> Brown Sugar</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Citrus</span>
    <span class="check-item"><span class="check-box"></span> Plum</span>
    <span class="check-item"><span class="check-box"></span> Orchid</span>
    <span class="check-item"><span class="check-box"></span> Tropical</span>
    <span class="check-item"><span class="check-box"></span> Jasmine</span>
    <span class="check-item"><span class="check-box"></span> Apple</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Honey</span>
    <span class="check-item"><span class="check-box"></span> Grassy</span>
    <span class="check-item"><span class="check-box"></span> Seaweed</span>
    <span class="check-item"><span class="check-box"></span> Roasted</span>
    <span class="check-item"><span class="check-box"></span> Tobacco</span>
    <span class="check-item"><span class="check-box"></span> Mineral</span>
  </div>

  <!-- Other flavors -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-top: 4px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; min-width: 50px;">Other</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Overall Rating -->
  <div style="display: flex; align-items: center; gap: 8px; margin-top: 8px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; letter-spacing: 0.4pt;">Overall Rating</span>
    <span class="stars">&starf; &starf; &starf; &starf; &starf;</span>
  </div>

  <!-- Would Buy Again? -->
  <div class="check-row" style="margin-bottom: 10px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Would Buy Again</span>
    <span class="check-item"><span class="check-box"></span> Would Recommend</span>
    <span class="check-item"><span class="check-box"></span> New Favorite</span>
  </div>

  <!-- Tasting Notes (freeform) -->
  <div style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Detailed Tasting Notes</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- What to Try Next Time -->
  <div style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">What to Adjust Next Time</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Session #{session_num:02d} &mdash; Notes</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def leaf_inventory(page_of, total_pages):
    """Leaf purchase inventory page"""
    return f'''
<!-- Page {pn()}: Tea Collection -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Tea Collection</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Leaf Collection</div>
  <div class="page-subtitle">Keep track of what you have and what to restock</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Tea / Origin</th>
      <th style="width:58px;">Brand/Seller</th>
      <th style="width:40px;">Process</th>
      <th style="width:42px;">Roast Lvl</th>
      <th style="width:38px;">Harvest Date</th>
      <th style="width:30px;">Rating</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">1</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">2</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">3</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">4</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">5</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">6</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">7</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">8</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">9</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">10</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">11</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">12</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Rating: 1&ndash;5 (5 = best) | Roast Lvl: L/ML/M/MD/D</div>

  <div class="page-footer">
    <span>Tea Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def tea_shop_log(page_of, total_pages):
    """Favorite brand/sellers and tea shops"""
    return f'''
<!-- Page {pn()}: Brand/Seller Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Brand/Sellers &amp; Shops</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Brand/Seller &amp; Tea Shop Log</div>
  <div class="page-subtitle">Where to find great leaves</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Name</th>
      <th style="width:70px;">Location</th>
      <th style="width:62px;">Specialty</th>
      <th>Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">6</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">7</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">8</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">9</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">10</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">11</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A9B6E;">12</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Go-To Shop</div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #5A7A5A; text-transform: uppercase; min-width: 38px;">Name</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #5A7A5A; text-transform: uppercase; min-width: 38px;">Why I Love It</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #5A7A5A; text-transform: uppercase; min-width: 38px;">Usual Order</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Tea Tasting Journal</span>
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
    <span class="sh-right">My Tea Gear</span>
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
    <span>Tea Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def tea_origins_checklist():
    """Tea origins checklist — the tea belt"""
    origins = [
        "China (Zhejiang)", "Taiwan (Alishan)", "Kenya", "Burundi",
        "Georgia", "Tanzania", "Uganda", "Malawi",
        "Japan (Shizuoka)", "India (Darjeeling)", "Sri Lanka (Ceylon)", "Nepal",
        "South Korea", "Turkey (Rize)", "El Salvador", "Nicaragua",
        "Rwanda", "Mexico", "Bolivia", "Ecuador",
        "Vietnam (Sumatra)", "Vietnam (Java)", "Vietnam (Sulawesi)", "Papua New Guinea",
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
    <span class="sh-right">Tea Belt Tour</span>
  </div>

  <div class="page-title">Tea Origins Checklist</div>
  <div class="page-subtitle">Taste your way around the tea belt</div>

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
    <span>Tea Tasting Journal</span>
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
    <span class="sh-right">Your Tea Year in Review</span>
  </div>

  <div class="page-title">Tea Year in Review</div>
  <div class="page-subtitle">Fill in at the end of your tasting journey</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Steeps Tasted</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Origins Tried</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Brand/Sellers Sampled</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Top 5 Teas</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Tea / Origin</th>
      <th style="width:55px;">Brand/Seller</th>
      <th style="width:35px;">Rating</th>
      <th>Why It Stood Out</th>
    </tr>
    <tr><td style="font-weight:700;color:#C8A041;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C8A041;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C8A041;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C8A041;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C8A041;">5</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Personal Discoveries</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Winner</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#2A4A30;">Favorite Origin</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#2A4A30;">Favorite Process</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#2A4A30;">Favorite Tea Type</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#2A4A30;">Favorite Steeping Method</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#2A4A30;">Best New Discovery</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #2A4A30; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">What I Want to Explore Next</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Tea Tasting Journal</span>
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

  <div class="page-title">Tea Notes</div>
  <div class="page-subtitle">Recipes, ideas, and reminders</div>

  {lines}

  <div class="page-footer">
    <span>Tea Tasting Journal</span>
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
    <span>Tea Tasting Journal</span>
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
    pages.append(divider_section(1, "One", "Tasting Logs", "40 sessions &mdash; your tea journey"))
    NUM_SESSIONS = 40
    for i in range(1, NUM_SESSIONS + 1):
        pages.append(tasting_log_left(i))          # Left page: details
        pages.append(tasting_log_right(i))         # Right page: notes

    # ---- Section 2: Tea Collection ----
    pages.append(divider_section(2, "Two", "Leaf Collection", "Your tea shelf at a glance"))
    pages.append(leaf_inventory(1, 3))
    pages.append(leaf_inventory(2, 3))
    pages.append(leaf_inventory(3, 3))

    # ---- Section 3: Brand/Sellers & Shops ----
    pages.append(divider_section(3, "Three", "Brand/Sellers &amp; Shops", "Where to find great leaves"))
    pages.append(tea_shop_log(1, 2))
    pages.append(tea_shop_log(2, 2))

    # ---- Section 4: Equipment ----
    pages.append(divider_section(4, "Four", "Equipment", "Your brewing kit"))
    pages.append(brew_equipment())

    # ---- Section 5: Origins & Stats ----
    pages.append(divider_section(5, "Five", "Origins &amp; Favorites", "Your tea world map"))
    pages.append(tea_origins_checklist())
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
    print(f"  Leaf inventory: 3")
    print(f"  Brand/Seller log: 2")
    print(f"  Equipment: 1")
    print(f"  Origins checklist: 1")
    print(f"  Favorites summary: 1")
    print(f"  Sketch page: 1")
    print(f"  Notes pages: 10")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
