#!/usr/bin/env python3
"""
Cocktail Mixology Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Home bartenders, cocktail enthusiasts, amateur mixologists
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "cocktail_mixology_journal_us_V1.0.html")

BOOK_TITLE = "Cocktail Mixology Journal"
BOOK_SUBTITLE = "Craft, Record, and Perfect Every Drink You Make"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

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

/* ---- Colors ---- */
/* Deep charcoal: #161616, #1E1E1E */
/* Gold accent: #C4A04A */
/* Warm cream: #FAF6F0, #F5EDE3 */
/* Text: #2A2A2A */

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
  background: linear-gradient(165deg, #161616 0%, #1E1E1E 30%, #161616 65%, #0D0D0D 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Gold glow background */
.cover .glow-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #C4A04A, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 90% 40%, #C4A04A, transparent),
    radial-gradient(ellipse 16px 10px at 40% 90%, #C4A04A, transparent);
}

.cover .glass-wrap {
  width: 110px; height: 150px;
  position: relative;
  margin: 0 auto 16px;
}

/* Martini glass bowl — inverted triangle */
.cover .glass-bowl {
  width: 70px; height: 55px;
  position: absolute;
  top: 8px; left: 20px;
  background: linear-gradient(160deg,
    rgba(250,246,240,0.08) 0%,
    rgba(250,246,240,0.03) 40%,
    rgba(196,160,74,0.04) 80%);
  clip-path: polygon(0% 0%, 100% 0%, 52% 100%, 48% 100%);
}

/* Glass bowl outline */
.cover .glass-bowl-outline {
  width: 72px; height: 56px;
  position: absolute;
  top: 7px; left: 19px;
  border: none;
  background: linear-gradient(180deg, rgba(196,160,74,0.3), rgba(196,160,74,0.08));
  clip-path: polygon(
    0% 0%, 100% 0%,
    52% 100%, 48% 100%);
  filter: blur(2px);
  z-index: 0;
}

/* Liquid inside glass */
.cover .glass-liquid {
  width: 56px; height: 36px;
  position: absolute;
  top: 15px; left: 27px;
  background: linear-gradient(180deg,
    rgba(196,160,74,0.15) 0%,
    rgba(180,140,50,0.25) 50%,
    rgba(140,100,35,0.3) 100%);
  clip-path: polygon(
    0% 0%, 100% 0%,
    55% 100%, 45% 100%);
  z-index: 1;
}

/* Liquid surface highlight */
.cover .glass-liquid-shine {
  width: 48px; height: 3px;
  position: absolute;
  top: 15px; left: 31px;
  background: linear-gradient(90deg, transparent, rgba(250,246,240,0.3), transparent);
  border-radius: 50%;
  z-index: 2;
}

/* Olive on a pick */
.cover .olive-pick {
  position: absolute;
  top: 18px; left: 54px;
  z-index: 3;
}
.cover .olive-pick .pick-stick {
  width: 1.5px; height: 30px;
  background: rgba(196,160,74,0.5);
  transform: rotate(20deg);
  position: absolute;
  top: 0; left: 0;
}
.cover .olive-pick .olive {
  width: 8px; height: 8px;
  border-radius: 50%;
  background: rgba(196,160,74,0.3);
  border: 1px solid rgba(196,160,74,0.6);
  position: absolute;
  top: 20px; left: 8px;
}

/* Glass rim */
.cover .glass-rim {
  width: 72px; height: 4px;
  position: absolute;
  top: 8px; left: 19px;
  border: 1.5px solid rgba(196,160,74,0.5);
  border-radius: 50%;
  background: transparent;
  z-index: 2;
}

/* Stem */
.cover .glass-stem {
  width: 3px; height: 50px;
  position: absolute;
  top: 62px; left: 53px;
  background: linear-gradient(180deg, rgba(196,160,74,0.4), rgba(196,160,74,0.15));
}

/* Base */
.cover .glass-base {
  width: 44px; height: 6px;
  position: absolute;
  top: 112px; left: 33px;
  border: 1px solid rgba(196,160,74,0.4);
  border-radius: 50%;
  background: rgba(196,160,74,0.08);
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
  background: #C4A04A;
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
  border: 1px solid rgba(196,160,74,0.4);
  color: #C4A04A;
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
  color: #C4A04A;
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
  background: linear-gradient(165deg, #161616 0%, #1E1E1E 50%, #161616 100%);
  position: relative;
  overflow: hidden;
}

.divider .div-glow {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 25px 15px at 80% 30%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 25% 85%, #C4A04A, transparent);
}

.divider .div-num {
  font-size: 60pt;
  color: rgba(196,160,74,0.12);
  font-weight: 700;
  position: absolute;
  top: 1in;
}

.divider .div-label {
  font-size: 10pt;
  color: #C4A04A;
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
  border-bottom: 1.5px solid #C4A04A;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #161616;
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
  color: #161616;
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
  background: #C4A04A;
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
.field-row {
  display: flex;
  gap: 8px;
  align-items: baseline;
}
.field-label {
  font-size: 7.5pt;
  font-weight: 700;
  color: #161616;
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
  border-left: 3px solid #C4A04A;
  padding: 8px 10px;
  margin-bottom: 10px;
  font-size: 8pt;
  color: #333;
  line-height: 1.5;
}
.info-box .info-title {
  font-weight: 700;
  color: #161616;
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
  color: #161616;
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
  border: 1.5px solid #C4A04A;
  border-radius: 50%;
  display: inline-block;
}

/* ---- Flavor Category Card ---- */
.flavor-cat {
  border: 1px solid #E8DCC8;
  border-radius: 4px;
  padding: 6px 8px;
  margin-bottom: 5px;
  background: #FCFAF7;
}
.flavor-cat-label {
  font-size: 7pt;
  font-weight: 700;
  color: #C4A04A;
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
  border: 1px solid #E8DCC8;
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
  color: #161616;
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
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 4px;
}
.gear-card .gear-line {
  border-bottom: 0.5px solid #ddd;
  height: 16px;
  margin-bottom: 2px;
}
"""

# ============================================================
# PAGE BUILDERS
# ============================================================

def cover_page():
    return f'''
<!-- Page {pn()}: Cover -->
<div class="cover">
  <div class="glow-bg"></div>
  <div class="glass-wrap">
    <div class="glass-bowl-outline"></div>
    <div class="glass-bowl"></div>
    <div class="glass-rim"></div>
    <div class="glass-liquid"></div>
    <div class="glass-liquid-shine"></div>
    <div class="olive-pick">
      <div class="pick-stick"></div>
      <div class="olive"></div>
    </div>
    <div class="glass-stem"></div>
    <div class="glass-base"></div>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">40 Recipe Pages</span>
      <span class="feature-badge">Flavor Wheel</span>
      <span class="feature-badge">Bar Inventory</span>
      <span class="feature-badge">Classic Recipes</span>
    </div>
    <div class="tagline">For Home Bartenders &amp; Mixology Enthusiasts</div>
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
    <div style="font-size: 16pt; font-weight: 700; color: #161616; margin-bottom: 6px;">This Journal Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #161616; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Spirit</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Cocktail</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Home Bar Setup</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Signature Serve</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Cocktail Mixology Journal</span>
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

  <div class="page-title">How to Use This Journal</div>
  <div class="page-subtitle">Make every drink a creation worth remembering</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Cocktail Journal?</div>
    The best bartenders and mixologists are also the best record-keepers. A journal helps you track what works, refine your technique, and build a personal repertoire of signature drinks. Whether you're a weekend host or an aspiring mixologist, your journal becomes your cocktail playbook.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Tips for Better Cocktails</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Measure everything.</strong> Good cocktails are about balance. Use a jigger for every pour, even when you think you can eyeball it. The difference between a great cocktail and an average one is often a quarter ounce.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Taste as you go.</strong> Use a straw to sample before you serve. Adjust sweetness, acidity, or strength before the drink leaves your hands. A tiny adjustment can transform a drink.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Use fresh ingredients.</strong> Fresh citrus juice and quality ice make an enormous difference. Squeeze citrus the day you use it, and never settle for bottled lemon or lime juice in a cocktail you care about.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Chill your glassware.</strong> A pre-chilled glass keeps your cocktail colder, longer. Pop it in the freezer for a few minutes while you mix. The drink will taste noticeably crisper.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Record the details.</strong> Base spirit, ratios, method, glass, garnish, and your impression. Note what you'd change next time. Every great recipe started as an experiment.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Pro Tip:</strong> When adapting a recipe, change only one ingredient at a time so you know exactly what made the difference.
  </div>

  <div class="page-footer">
    <span>Cocktail Mixology Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def flavor_wheel():
    categories = [
        ("Citrus &amp; Sour",
         "Lemon &bull; Lime &bull; Orange &bull; Grapefruit &bull; Yuzu &bull; Cranberry &bull; Pomegranate &bull; Pineapple"),
        ("Sweet &amp; Syrupy",
         "Simple Syrup &bull; Honey &bull; Agave &bull; Maple &bull; Grenadine &bull; Caramel &bull; Vanilla &bull; Coconut"),
        ("Herbal &amp; Botanical",
         "Mint &bull; Basil &bull; Rosemary &bull; Thyme &bull; Elderflower &bull; Absinthe &bull; Chartreuse &bull; Lavender"),
        ("Bitter &amp; Amaro",
         "Campari &bull; Aperol &bull; Angostura &bull; Orange Bitters &bull; Espresso &bull; Tonic &bull; Cinchona &bull; Gentian"),
        ("Spice &amp; Warmth",
         "Cinnamon &bull; Clove &bull; Nutmeg &bull; Ginger &bull; Chili &bull; Black Pepper &bull; Cardamom &bull; Allspice"),
        ("Fruity &amp; Tropical",
         "Mango &bull; Passion Fruit &bull; Papaya &bull; Banana &bull; Coconut &bull; Watermelon &bull; Peach &bull; Berry"),
        ("Smoky &amp; Woody",
         "Mezcal &bull; Charred Oak &bull; Tobacco &bull; Cedar &bull; Peated Whiskey &bull; Bitters &bull; Lapsang"),
        ("Cream &amp; Rich",
         "Egg White &bull; Cream &bull; Coconut Cream &bull; Baileys &bull; Kahlua &bull; Dulce de Leche &bull; Avocado"),
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

  <div class="page-title">Cocktail Flavor Wheel</div>
  <div class="page-subtitle">Find the words for what you taste</div>

  {rows}

  <div style="margin-top: 8px; padding: 6px 8px; background: #FAF6F0; border-radius: 3px; font-size: 7pt; color: #888; font-style: italic;">
    Use these categories as a starting point. Trust your own palate &mdash; the goal is to recognize patterns in the drinks you enjoy and the flavors you love to combine.
  </div>

  <div class="page-footer">
    <span>Cocktail Mixology Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def spirits_guide():
    spirits = [
        ("Vodka", "Neutral spirit distilled from grain or potato. Clean, versatile, and the base for countless classic and modern cocktails. Carries other flavors without competing.", "Best for: Martini, Moscow Mule, Cosmopolitan"),
        ("Gin", "Distilled grain spirit infused with botanicals, led by juniper. Adds herbal, floral, and citrus complexity. The backbone of classic cocktail culture.", "Best for: Martini, Negroni, Gimlet, Gin &amp; Tonic"),
        ("Rum", "Distilled from sugarcane juice or molasses. Ranges from light and crisp to dark and rich. The spirit of tropical and tiki cocktails.", "Best for: Mojito, Daiquiri, Mai Tai, Dark &amp; Stormy"),
        ("Tequila", "Distilled from blue agave in Mexico. Blanco is bright and agave-forward; reposado and anejo are oak-aged and complex. Essential for Margaritas.", "Best for: Margarita, Paloma, Tequila Sunrise"),
        ("Whiskey", "Grain spirit aged in oak barrels. Bourbon, rye, Scotch, and Irish each bring unique character. Adds warmth and depth to cocktails.", "Best for: Old Fashioned, Manhattan, Whiskey Sour"),
        ("Brandy &amp; Cognac", "Distilled from wine or fruit. Cognac is the premier French brandy. Smooth, complex, and elegant in classic and after-dinner drinks.", "Best for: Sidecar, Brandy Alexander, French Connection"),
        ("Mezcal", "Distilled from agave, traditionally smoked underground. Smoky, earthy, and complex. Adds depth and character to any cocktail.", "Best for: Mezcal Negroni, Oaxaca Old Fashioned"),
        ("Liqueurs &amp; Aperitifs", "Sweetened, flavored spirits: Campari, Aperol, Triple Sec, Amaretto, St-Germain. Build complexity, sweetness, and color.", "Best for: Modifiers in countless cocktails"),
    ]

    rows = ""
    for name, desc, best in spirits:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 100px; font-size: 8pt; font-weight: 700; color: #161616;">{name}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4; flex: 1;">{desc}<br><span style="color: #C4A04A; font-weight: 700;">{best}</span></div>
      </div>'''

    return f'''
<!-- Page {pn()}: Spirits Guide -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Base Spirits Guide</span>
  </div>

  <div class="page-title">Base Spirits Guide</div>
  <div class="page-subtitle">Know your foundations</div>

  {rows}

  <div class="page-footer">
    <span>Cocktail Mixology Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def techniques_reference():
    techniques = [
        ("Shake", "Fill shaker with ice, add ingredients, seal, and shake vigorously 10-15 seconds. Strain into glass. Use for cloudy, juice-heavy, or egg-white drinks."),
        ("Stir", "Add ingredients to a mixing glass with ice. Stir gently 20-30 seconds with a bar spoon. Strain. Use for clear, spirit-forward drinks like Martinis and Manhattans."),
        ("Muddle", "Press ingredients (mint, fruit, sugar) in the bottom of the glass with a muddler to release flavors. Do not crush &mdash; gentle pressure extracts oils without bitterness."),
        ("Build", "Pour ingredients directly into the serving glass over ice. Stir once. Use for highballs and simple mixed drinks like Gin &amp; Tonic."),
        ("Blend", "Combine ingredients with ice in a blender until smooth. Essential for frozen cocktails like Margaritas, Daiquiris, and Pina Coladas."),
        ("Layer", "Carefully pour spirits over the back of a spoon so they float on top of each other. Works with liquids of different densities."),
        ("Double Strain", "Strain through a Hawthorne strainer AND a fine mesh strainer. Removes ice chips and fruit pulp for a silky-smooth drink."),
        ("Fat Wash", "Infuse spirit with rendered fat (bacon, butter), freeze, then skim solid fat off the top. Adds savory depth to spirits."),
    ]

    rows = ""
    for name, desc in techniques:
        rows += f'''
      <div style="border: 1px solid #E8DCC8; border-radius: 3px; padding: 7px 9px; margin-bottom: 6px; background: #FCFAF7;">
        <div style="font-size: 9.5pt; font-weight: 700; color: #161616; margin-bottom: 3px;">{name}</div>
        <div style="font-size: 8pt; color: #555; line-height: 1.5;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Techniques -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Mixology Techniques</span>
  </div>

  <div class="page-title">Essential Techniques</div>
  <div class="page-subtitle">Master the fundamentals of mixology</div>

  {rows}

  <div class="page-footer">
    <span>Cocktail Mixology Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def glassware_reference():
    glasses = [
        ("Coupe", "V-shaped shallow bowl on a stem. The classic vintage cocktail glass. Best for shaken drinks served 'up' without ice."),
        ("Martini Glass", "Iconic inverted cone on a stem. Best for spirit-forward, chilled drinks served without ice."),
        ("Rocks / Old Fashioned", "Short, wide tumbler. Best for drinks served over ice, spirit-forward cocktails, and muddled drinks."),
        ("Highball / Collins", "Tall, narrow tumbler. Best for mixed drinks with a large proportion of mixer, served over ice."),
        ("Nick &amp; Nora", "Elegant curved bowl on a stem. A vintage style making a comeback. Best for stirred, spirit-forward drinks."),
        ("Hurricane", "Curved, tulip-shaped glass. Best for tropical and tiki cocktails, frozen drinks, and large-format serves."),
        ("Margarita", "Distinctive double-bowl shape with a wide rim for salt or sugar. Best for Margaritas and frozen cocktails."),
        ("Snifter", "Round bowl that narrows at the top. Best for aged spirits neat, and aromatic cocktails served warm."),
    ]

    rows = ""
    for name, desc in glasses:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 100px; font-size: 8.5pt; font-weight: 700; color: #161616;">{name}</div>
        <div style="font-size: 7.5pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Glassware -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Glassware Guide</span>
  </div>

  <div class="page-title">Glassware Guide</div>
  <div class="page-subtitle">The right glass makes the right drink</div>

  {rows}

  <div class="page-footer">
    <span>Cocktail Mixology Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def classics_reference():
    """Classic cocktail recipes for quick reference"""
    classics = [
        ("Old Fashioned", "2 oz Bourbon or Rye, 1 sugar cube (or 1/4 oz syrup), 2-3 dashes Angostura bitters, orange peel", "Stir. Rocks glass. Orange peel garnish."),
        ("Negroni", "1 oz Gin, 1 oz Campari, 1 oz Sweet Vermouth", "Stir. Rocks glass. Orange peel garnish."),
        ("Margarita", "2 oz Tequila, 1 oz Lime juice, 1 oz Triple Sec (Cointreau)", "Shake. Salt-rimmed coupe or rocks. Lime wheel."),
        ("Martini", "2.5 oz Gin, 0.5 oz Dry Vermouth, dash orange bitters", "Stir. Martini glass. Lemon twist or olive."),
        ("Manhattan", "2 oz Rye, 1 oz Sweet Vermouth, 2 dashes Angostura", "Stir. Coupe. Cherry garnish."),
        ("Daiquiri", "2 oz White Rum, 1 oz Lime juice, 3/4 oz Simple syrup", "Shake. Coupe. No garnish needed."),
        ("Mojito", "2 oz White Rum, 1 oz Lime juice, 1/2 oz Syrup, mint, soda", "Build. Highball glass. Mint sprig."),
        ("Whiskey Sour", "2 oz Bourbon, 3/4 oz Lemon, 1/2 oz Syrup, egg white", "Dry shake, then shake w/ ice. Rocks. Cherry."),
        ("Mai Tai", "2 oz Rum, 3/4 oz Lime, 1/2 oz Orange Curacao, 1/2 oz Orgeat", "Shake. Rocks glass. Mint &amp; fruit garnish."),
        ("Cosmopolitan", "1.5 oz Vodka, 0.5 oz Cointreau, 0.5 oz Lime, 1 oz Cranberry", "Shake. Martini glass. Orange twist."),
        ("Aperol Spritz", "3 oz Prosecco, 2 oz Aperol, 1 oz Soda", "Build. Wine glass over ice. Orange slice."),
        ("Moscow Mule", "2 oz Vodka, 4-6 oz Ginger Beer, 0.5 oz Lime", "Build. Copper mug. Lime wedge &amp; mint."),
    ]

    rows = ""
    for i, (name, ingredients, method) in enumerate(classics, 1):
        rows += f'''
      <div style="display: flex; gap: 6px; margin-bottom: 4px; padding: 5px 7px; border-left: 2px solid #C4A04A; background: #FCFAF7; border-radius: 0 3px 3px 0;">
        <div style="min-width: 80px; font-size: 7.5pt; font-weight: 700; color: #161616;">{name}</div>
        <div style="font-size: 6.5pt; color: #666; line-height: 1.35; flex: 1;">{ingredients}<br><span style="color: #999;">{method}</span></div>
      </div>'''

    return f'''
<!-- Page {pn()}: Classics -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Classic Recipes</span>
  </div>

  <div class="page-title">Classic Cocktail Recipes</div>
  <div class="page-subtitle">The foundations every bartender should know</div>

  {rows}

  <div style="margin-top: 6px; padding: 5px 8px; background: #FAF6F0; border-radius: 3px; font-size: 7pt; color: #888; font-style: italic;">
    These are starting points. Adjust ratios to taste, then record your perfected version in the recipe section.
  </div>

  <div class="page-footer">
    <span>Cocktail Mixology Journal</span>
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
  <div class="div-glow"></div>
  <div class="div-num">{num:02d}</div>
  <div class="div-label">Part {label_text}</div>
  <div class="div-title">{title}</div>
  <div class="div-sub">{subtitle}</div>
</div>
'''


def recipe_log_left(session_num):
    """Left page: cocktail details + flavor ratings"""
    return f'''
<!-- Page {pn()}: Recipe {session_num} Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Recipe #{session_num:02d}</span>
    <span class="sh-right">Cocktail Mixology Journal</span>
  </div>

  <div class="page-title">Recipe #{session_num:02d}</div>
  <div class="page-subtitle">Cocktail Details &amp; Flavor Profile</div>

  <!-- Cocktail Info -->
  <div style="background: #FAF6F0; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Time</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Cocktail</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Base Spirit</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Glass</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Garnish</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">ABV%</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Method -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Method</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Shake</span>
    <span class="check-item"><span class="check-box"></span> Stir</span>
    <span class="check-item"><span class="check-box"></span> Build</span>
    <span class="check-item"><span class="check-box"></span> Blend</span>
    <span class="check-item"><span class="check-box"></span> Muddle</span>
    <span class="check-item"><span class="check-box"></span> Layer</span>
    <span class="check-item"><span class="check-box"></span> Other</span>
  </div>

  <!-- Glass Type checkboxes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Serve</div>
  <div class="check-row" style="margin-bottom: 10px;">
    <span class="check-item"><span class="check-box"></span> Up (no ice)</span>
    <span class="check-item"><span class="check-box"></span> On the Rocks</span>
    <span class="check-item"><span class="check-box"></span> Blended</span>
    <span class="check-item"><span class="check-box"></span> Salt Rim</span>
    <span class="check-item"><span class="check-box"></span> Sugar Rim</span>
  </div>

  <!-- Flavor Ratings (1-5 scale) -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Flavor Balance &mdash; Fill in circles (1 = subtle, 5 = dominant)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Sweetness</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Sourness</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Booziness</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Bitterness</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Complexity</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Finish Length</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>

  <div class="page-footer">
    <span>Recipe #{session_num:02d} &mdash; Details</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def recipe_log_right(session_num):
    """Right page: ingredients, steps, rating, notes"""
    return f'''
<!-- Page {pn()}: Recipe {session_num} Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Recipe #{session_num:02d}</span>
    <span class="sh-right">Ingredients, Steps &amp; Notes</span>
  </div>

  <div class="page-title">Recipe #{session_num:02d}</div>
  <div class="page-subtitle">Ingredients, method &amp; your impression</div>

  <!-- Ingredients -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Ingredients &mdash; list with measurements (oz / ml)</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2px 12px; margin-bottom: 8px;">
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
  </div>

  <!-- Steps -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Method &amp; Steps</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Overall Rating -->
  <div style="display: flex; align-items: center; gap: 8px; margin-top: 10px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt;">Overall Rating</span>
    <span class="stars">&starf; &starf; &starf; &starf; &starf;</span>
  </div>

  <!-- Would Make Again? -->
  <div class="check-row" style="margin-bottom: 10px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Would Make Again</span>
    <span class="check-item"><span class="check-box"></span> Would Serve Guests</span>
    <span class="check-item"><span class="check-box"></span> Signature Drink</span>
  </div>

  <!-- Tasting Notes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Tasting Notes</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- What to Adjust -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">What to Adjust Next Time</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Recipe #{session_num:02d} &mdash; Notes</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def bar_inventory(page_of, total_pages):
    """Home bar inventory — spirits and modifiers"""
    return f'''
<!-- Page {pn()}: Bar Inventory -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Home Bar Inventory</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Home Bar Inventory</div>
  <div class="page-subtitle">Know what you have and what to restock</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Bottle</th>
      <th style="width:52px;">Category</th>
      <th style="width:36px;">Volume</th>
      <th style="width:30px;">Level</th>
      <th>Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Level: F = Full, 3/4, 1/2, 1/4, L = Low/Empty | Category: Vodka/Gin/Rum/Tequila/Whiskey/Brandy/Liqueur/Vermouth/Bitters/Mixer</div>

  <div class="page-footer">
    <span>Cocktail Mixology Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def equipment_log():
    """Bar equipment and tools inventory"""
    return f'''
<!-- Page {pn()}: Equipment -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Bar Equipment</span>
    <span class="sh-right">My Bartending Kit</span>
  </div>

  <div class="page-title">Bar Equipment &amp; Tools</div>
  <div class="page-subtitle">Know your kit</div>

  <div class="gear-card">
    <div class="gear-label">Shakers &amp; Mixing Tools</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Tool</th><th>Type / Brand</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Measuring &amp; Straining</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Tool</th><th>Type / Brand</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Glassware Collection</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Quantity</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Accessories</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Item</th><th>Type / Size</th><th>Spare?</th></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Cocktail Mixology Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def glassware_checklist():
    """Glass types to collect"""
    glass_types = [
        "Coupe", "Martini Glass", "Rocks / Old Fashioned", "Highball / Collins",
        "Nick &amp; Nora", "Hurricane", "Margarita", "Snifter",
        "Wine Glass", "Copper Mug", "Tiki Mug", "Shot Glass",
        "Cordial Glass", "Flute", "Pint Glass", "Absinthe Glass",
        "Punch Cup", "Rocks (double)", "Coupe (large)", "Nick &amp; Nora (vintage)",
    ]

    rows = ""
    for i, glass in enumerate(glass_types, 1):
        rows += f'''
    <tr>
      <td>{i}</td>
      <td>{glass}</td>
      <td></td>
      <td><span class="check-box" style="vertical-align: middle;"></span></td>
    </tr>'''

    return f'''
<!-- Page {pn()}: Glassware Checklist -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Glassware Checklist</span>
    <span class="sh-right">Build Your Collection</span>
  </div>

  <div class="page-title">Glassware Checklist</div>
  <div class="page-subtitle">A glass for every occasion</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:22px;">#</th>
      <th>Glass Type</th>
      <th style="width:70px;">Brand / Source</th>
      <th style="width:28px;">&#10003;</th>
    </tr>
    {rows}
  </table>

  <div class="page-footer">
    <span>Cocktail Mixology Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def favorites_summary():
    """Favorites and stats page"""
    return f'''
<!-- Page {pn()}: Favorites Summary -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Favorites &amp; Stats</span>
    <span class="sh-right">Your Cocktail Year in Review</span>
  </div>

  <div class="page-title">Cocktail Year in Review</div>
  <div class="page-subtitle">Fill in at the end of your mixology journey</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Cocktails Made</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Original Recipes</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Spirits Tried</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Top 5 Cocktails</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Cocktail Name</th>
      <th style="width:55px;">Base Spirit</th>
      <th style="width:35px;">Rating</th>
      <th>Why It Stood Out</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Personal Discoveries</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Winner</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">Favorite Base Spirit</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Favorite Classic</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Original Creation</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Party Drink</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best New Discovery</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">What I Want to Explore Next</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Cocktail Mixology Journal</span>
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

  <div class="page-title">Cocktail Notes</div>
  <div class="page-subtitle">Ideas, pairings, and reminders</div>

  {lines}

  <div class="page-footer">
    <span>Cocktail Mixology Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


# ============================================================
# MAIN
# ============================================================
def main():
    pages = []

    # ---- Front Matter ----
    pages.append(cover_page())                          # 1: Cover
    pages.append(owner_page())                           # 2: Owner page

    # ---- Educational Reference ----
    pages.append(how_to_use())                           # 3: How to use
    pages.append(flavor_wheel())                         # 4: Flavor wheel
    pages.append(spirits_guide())                        # 5: Base spirits
    pages.append(techniques_reference())                 # 6: Techniques
    pages.append(glassware_reference())                  # 7: Glassware guide
    pages.append(classics_reference())                   # 8: Classic recipes

    # ---- Section 1: Recipe Logs ----
    pages.append(divider_section(1, "One", "Recipe Logs", "40 cocktails &mdash; your mixology journey"))
    NUM_SESSIONS = 40
    for i in range(1, NUM_SESSIONS + 1):
        pages.append(recipe_log_left(i))                 # Left page: details
        pages.append(recipe_log_right(i))                # Right page: ingredients + notes

    # ---- Section 2: Home Bar Inventory ----
    pages.append(divider_section(2, "Two", "Home Bar Inventory", "Your spirits shelf at a glance"))
    pages.append(bar_inventory(1, 3))
    pages.append(bar_inventory(2, 3))
    pages.append(bar_inventory(3, 3))

    # ---- Section 3: Equipment & Tools ----
    pages.append(divider_section(3, "Three", "Equipment &amp; Tools", "Your bartending kit"))
    pages.append(equipment_log())

    # ---- Section 4: Glassware Collection ----
    pages.append(divider_section(4, "Four", "Glassware", "A glass for every drink"))
    pages.append(glassware_checklist())

    # ---- Section 5: Favorites ----
    pages.append(divider_section(5, "Five", "Favorites &amp; Stats", "Your cocktail year in review"))
    pages.append(favorites_summary())

    # ---- Section 6: Notes ----
    pages.append(divider_section(6, "Six", "Notes", "Ideas, pairings, and reminders"))
    for i in range(6):
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

    print(f"\nPage breakdown:")
    print(f"  Cover: 1")
    print(f"  Owner page: 1")
    print(f"  Reference (how-to, flavor wheel, spirits, techniques, glassware, classics): 6")
    print(f"  Section dividers: 6")
    print(f"  Recipe logs ({NUM_SESSIONS} x 2 pages): {NUM_SESSIONS * 2}")
    print(f"  Bar inventory: 3")
    print(f"  Equipment log: 1")
    print(f"  Glassware checklist: 1")
    print(f"  Favorites summary: 1")
    print(f"  Notes pages: 6")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
