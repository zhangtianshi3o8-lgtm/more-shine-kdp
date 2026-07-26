#!/usr/bin/env python3
"""
Sake Tasting Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Sake enthusiasts worldwide (English-speaking markets)
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "sake_tasting_journal_us_V1.0.html")

BOOK_TITLE = "Sake Tasting Journal"
BOOK_SUBTITLE = "Discover Every Brew, Every Aroma, Every Kura"

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
/* Deep indigo-charcoal: #0F1628, #16203A */
/* Indigo: #1E3A5F, #2A4A73 */
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
  background: linear-gradient(165deg, #0F1628 0%, #16203A 30%, #0F1628 65%, #080D18 100%);
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
    radial-gradient(ellipse 28px 17px at 70% 70%, #1E3A5F, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #2A4A73, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 90% 40%, #2A4A73, transparent),
    radial-gradient(ellipse 16px 10px at 40% 90%, #C4A04A, transparent);
}

/* ===== CSS Tokkuri (Sake Flask) Illustration ===== */
.cover .tokkuri-wrap {
  width: 130px; height: 170px;
  position: relative;
  margin: 0 auto 20px;
}

/* Flask body — rounded bottom, narrow neck */
.cover .flask-body {
  width: 80px; height: 80px;
  position: absolute;
  top: 55px; left: 25px;
  background: linear-gradient(160deg,
    rgba(250,246,240,0.10) 0%,
    rgba(250,246,240,0.04) 40%,
    rgba(30,58,95,0.06) 80%,
    rgba(15,22,40,0.08) 100%);
  border-radius: 45% 45% 48% 48%;
}

/* Flask body outline glow */
.cover .flask-glow {
  width: 84px; height: 84px;
  position: absolute;
  top: 53px; left: 23px;
  background: linear-gradient(180deg, rgba(196,160,74,0.25), rgba(196,160,74,0.05));
  border-radius: 45% 45% 48% 48%;
  filter: blur(3px);
  z-index: 0;
}

/* Flask neck */
.cover .flask-neck {
  width: 24px; height: 28px;
  position: absolute;
  top: 40px; left: 53px;
  background: linear-gradient(160deg,
    rgba(250,246,240,0.08) 0%,
    rgba(250,246,240,0.03) 100%);
  border-left: 1.5px solid rgba(196,160,74,0.4);
  border-right: 1.5px solid rgba(196,160,74,0.4);
}

/* Flask lip */
.cover .flask-lip {
  width: 30px; height: 8px;
  position: absolute;
  top: 36px; left: 50px;
  border: 1.5px solid rgba(196,160,74,0.5);
  border-radius: 50%;
  background: transparent;
}

/* Flask shine */
.cover .flask-shine {
  width: 8px; height: 30px;
  position: absolute;
  top: 68px; left: 38px;
  background: linear-gradient(180deg, rgba(250,246,240,0.4), rgba(250,246,240,0.03));
  border-radius: 50%;
  transform: rotate(-8deg);
  z-index: 3;
}

/* Ochoko (small sake cup) beside flask */
.cover .ochoko {
  width: 34px; height: 24px;
  position: absolute;
  top: 110px; left: 15px;
  background: linear-gradient(180deg,
    rgba(250,246,240,0.06),
    rgba(196,160,74,0.10));
  border: 1.5px solid rgba(196,160,74,0.35);
  border-radius: 0 0 40% 40%;
  z-index: 2;
}

/* Ochoko liquid */
.cover .ochoko-liquid {
  width: 28px; height: 10px;
  position: absolute;
  top: 120px; left: 18px;
  background: linear-gradient(180deg,
    rgba(250,246,240,0.20),
    rgba(196,160,74,0.15));
  border-radius: 0 0 35% 35%;
  z-index: 3;
}

/* Vapor/aroma lines rising from flask */
.cover .vapor1 {
  width: 2px; height: 22px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.35), transparent);
  position: absolute;
  top: 12px; left: 60px;
  border-radius: 50%;
  transform: rotate(-8deg);
}
.cover .vapor2 {
  width: 2px; height: 28px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.25), transparent);
  position: absolute;
  top: 6px; left: 70px;
  border-radius: 50%;
  transform: rotate(6deg);
}
.cover .vapor3 {
  width: 2px; height: 20px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.2), transparent);
  position: absolute;
  top: 14px; left: 50px;
  border-radius: 50%;
  transform: rotate(-3deg);
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
  background: linear-gradient(165deg, #0F1628 0%, #16203A 50%, #0F1628 100%);
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
    radial-gradient(ellipse 22px 13px at 70% 75%, #1E3A5F, transparent),
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
  border-bottom: 1.5px solid #1E3A5F;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #0F1628;
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
  color: #0F1628;
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
  background: #1E3A5F;
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
  color: #0F1628;
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
  border-left: 3px solid #1E3A5F;
  padding: 8px 10px;
  margin-bottom: 10px;
  font-size: 8pt;
  color: #333;
  line-height: 1.5;
}
.info-box .info-title {
  font-weight: 700;
  color: #0F1628;
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
  color: #0F1628;
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
  border: 1.5px solid #1E3A5F;
  border-radius: 50%;
  display: inline-block;
}

/* ---- Flavor Category Card ---- */
.flavor-cat {
  border: 1px solid #D8D8E8;
  border-radius: 4px;
  padding: 6px 8px;
  margin-bottom: 5px;
  background: #FCFAF7;
}
.flavor-cat-label {
  font-size: 7pt;
  font-weight: 700;
  color: #1E3A5F;
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
  border: 1px solid #D8D8E8;
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
  color: #0F1628;
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
  color: #1E3A5F;
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

/* ---- Region List ---- */
table.region-list th {
  background: #2A4A73;
}
table.region-list td:first-child {
  width: 22px;
  text-align: center;
  font-weight: 700;
  color: #2A4A73;
}
table.region-list td:last-child {
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
  <div class="glow-bg"></div>
  <div class="tokkuri-wrap">
    <div class="vapor1"></div>
    <div class="vapor2"></div>
    <div class="vapor3"></div>
    <div class="flask-glow"></div>
    <div class="flask-body"></div>
    <div class="flask-neck"></div>
    <div class="flask-lip"></div>
    <div class="flask-shine"></div>
    <div class="ochoko"></div>
    <div class="ochoko-liquid"></div>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">40 Tasting Sessions</span>
      <span class="feature-badge">Flavor Wheel</span>
      <span class="feature-badge">Kura Guide</span>
      <span class="feature-badge">Sake Types</span>
    </div>
    <div class="tagline">For Sake Lovers &amp; Explorers</div>
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
    <div style="font-size: 16pt; font-weight: 700; color: #0F1628; margin-bottom: 6px;">This Journal Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #0F1628; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #1E3A5F; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Sake Style</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #1E3A5F; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Brewery (Kura)</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #1E3A5F; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Region</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #1E3A5F; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Preferred Vessel</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Sake Tasting Journal</span>
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
  <div class="page-subtitle">Make every cup a learning experience</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Sake Journal?</div>
    The difference between drinking sake and understanding sake is attention. A tasting journal helps you discover patterns &mdash; which styles you gravitate toward, how rice polishing and yeast shape flavor, what regions deliver the character you love. Over time, your journal becomes your personal sake roadmap.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #0F1628; font-size: 10pt; margin-bottom: 6px;">The Five S's of Sake Tasting</div>

    <div style="margin-bottom: 10px;">
      <strong>1. See.</strong> Pour the sake into an ochoko or white wine glass. Observe the color &mdash; most premium sake is water-clear, but some styles show a faint yellow or cloudy white. Clarity and viscosity hint at the brewing method.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Swirl.</strong> Gently rotate the vessel to expose the sake to air. This releases aromas. Notice the legs (tears) that form on the glass wall &mdash; thicker legs can indicate a richer body or higher sweetness.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Sniff.</strong> Bring the vessel to your nose and take short, gentle sniffs. Ginjo-grade sakes offer dramatic fruity and floral aromas. Try to identify melon, apple, pear, banana, anise, or rice notes. Your nose reveals more than your palate.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Sip.</strong> Take a small sip and let it spread across your tongue. Note the sweetness, acidity, body, umami, and bitterness. Sake has a unique savory dimension (umami) that other beverages lack. The texture is just as important as the taste.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Savor.</strong> Pay attention to the finish &mdash; the sensations that linger after you swallow. Some sakes are clean and crisp (tanrei); others are rich and persistent (nojun). Note how long it lasts and whether the aftertaste changes character.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #F0F4FA; border: 1px solid #C0D0E0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #1E3A5F;">Pro Tip:</strong> Temperature transforms sake dramatically. Try the same sake chilled (5&ndash;10&deg;C), at room temperature (15&ndash;20&deg;C), and warmed (35&ndash;45&deg;C). Each temperature reveals different aromas and flavors. Junmai-style sakes often shine warm; Ginjo-grade sakes are best chilled.
  </div>

  <div class="page-footer">
    <span>Sake Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def flavor_wheel():
    categories = [
        ("Fruity &amp; Floral",
         "Melon &bull; Green Apple &bull; Pear &bull; Banana &bull; Lychee &bull; Strawberry &bull; Peach &bull; Pineapple &bull; Grape &bull; Citrus &bull; Anise &bull; Rose"),
        ("Rice &amp; Umami",
         "Steamed Rice &bull; Rice Pudding &bull; Yogurt &bull; Lactic &bull; Creamy &bull; Savory &bull; Mushroom &bull; Miso &bull; Soy Sauce"),
        ("Cereal &amp; Grain",
         "Oatmeal &bull; Cereal &bull; Buckwheat &bull; Wheat &bull; Toasted Grain &bull; Bread Dough &bull; Cracker"),
        ("Sweet &amp; Honeyed",
         "Honey &bull; Caramel &bull; Brown Sugar &bull; Molasses &bull; Maple &bull; Vanilla &bull; Butterscotch"),
        ("Nutty &amp; Roasted",
         "Almond &bull; Walnut &bull; Hazelnut &bull; Chestnut &bull; Roasted Nut &bull; Coffee &bull; Dark Chocolate"),
        ("Earthy &amp; Herbal",
         "Mineral &bull; Wet Stone &bull; Forest Floor &bull; Dried Leaves &bull; Dill &bull; Fennel &bull; Green Tea &bull; Herbs"),
        ("Spice",
         "White Pepper &bull; Cinnamon &bull; Clove &bull; Ginger &bull; Nutmeg &bull; Sansho Pepper"),
        ("Other",
         "Alcoholic &bull; Estery &bull; Astringent &bull; Bitter &bull; Metallic &bull; Sulfur &bull; Fungal"),
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

  <div class="page-title">Sake Flavor Wheel</div>
  <div class="page-subtitle">Find the words for what you taste</div>

  {rows}

  <div style="margin-top: 8px; padding: 6px 8px; background: #FAF6F0; border-radius: 3px; font-size: 7pt; color: #888; font-style: italic;">
    Use these categories as a starting point. Sake has a unique aromatic range from ginjo-style tropical fruits to junmai-style savory umami. Trust your own descriptions &mdash; the goal is to recognize patterns in what you enjoy.
  </div>

  <div class="page-footer">
    <span>Sake Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def sake_types_reference():
    methods = [
        ("Junmai", "Pure rice sake &mdash; no added distilled alcohol. Rice polished to at least 70%% remaining (30%% milled away). Rich, full-bodied with deep umami and rice-driven flavors. Served at various temperatures.", "Best for: Warm service, food pairing, exploring tradition"),
        ("Honj&omacr;z&omacr;", "A small amount of brewer's alcohol is added to extract aromas and lighten the body. Rice polished to at least 70%% remaining. Cleaner and lighter than Junmai but still rice-forward.", "Best for: Easy drinking, warming, everyday meals"),
        ("Ginj&omacr;", "Highly polished rice (at least 60%% remaining) with long, low-temperature fermentation. Complex fruity and floral aromas. May contain a small amount of added alcohol. Elegant and aromatic.", "Best for: Chilled service, special occasions, sipping"),
        ("Daiginj&omacr;", "The pinnacle of the brewer's art. Rice polished to at least 50%% remaining (often much more). Extraordinary aromatic complexity, refined texture, and layered flavors. Premium pricing reflects the labor and rice waste.", "Best for: Connoisseur tasting, gifts, contemplation"),
        ("Junmai Ginj&omacr;", "Ginjo-level polishing (60%% remaining) with NO added alcohol. Combines ginjo aromatics with junmai body and umami. A beautiful balance of elegance and substance.", "Best for: Food pairing, discovering balance"),
        ("Junmai Daiginj&omacr;", "Daiginjo-level polishing (50%%+ removed) with NO added alcohol. The ultimate expression of pure rice sake at the highest polish level. Rare, expensive, and transcendent.", "Best for: The finest occasions, deep exploration"),
        ("Nigorizake", "Coarsely filtered or unfiltered sake with visible rice sediment. Cloudy white appearance with sweet, creamy texture and lactic flavors. Some are unpasteurized (nama-nigori) for lively fizz.", "Best for: Dessert pairings, adventurous drinkers"),
        ("Namazake (Nama)", "Unpasteurized sake &mdash; fresh, vibrant, and lively. Must be kept refrigerated. Available across all style categories. Crisp aromatics with a youthful energy that pasteurized sake cannot match.", "Best for: Spring and summer, freshness seekers"),
    ]

    rows = ""
    for name, desc, best in methods:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #1E3A5F; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 88px; font-size: 8pt; font-weight: 700; color: #0F1628;">{name}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4; flex: 1;">{desc}<br><span style="color: #1E3A5F; font-weight: 700;">{best}</span></div>
      </div>'''

    return f'''
<!-- Page {pn()}: Sake Types -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Sake Types Guide</span>
  </div>

  <div class="page-title">Sake Types Guide</div>
  <div class="page-subtitle">Every classification has its own character and purpose</div>

  {rows}

  <div class="page-footer">
    <span>Sake Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def sake_regions_reference():
    regions = [
        ("Japan &mdash; Niigata", "The sake capital of Japan. Cold winters and pure snowmelt water produce crisp, clean, dry sakes known as tanrei karakuchi. Home to legendary breweries and the annual sake competition. The benchmark for refined sake."),
        ("Japan &mdash; Hy&omacr;go", "The largest sake-producing prefecture, growing Yamada Nishiki &mdash; the king of sake rice. Home of Nada, one of Japan's most historic brewing districts. Diverse styles from rich and full to elegant and dry."),
        ("Japan &mdash; Ky&omacr;to (Fushimi)", "Famed for soft, low-mineral water (gosui) that produces gentle, rounded, feminine sakes. Historic kura line the Fushimi district. Known for balanced, food-friendly styles with elegant aromatics."),
        ("Japan &mdash; Hiroshima", "Hard water with high mineral content produces bold, full-bodied sakes with pronounced sweetness. A major center for ginjo-style sake production. The hard water drives vigorous fermentation."),
        ("Japan &mdash; Akita", "Cold-region brewing at its finest. Long winters allow slow, low-temperature fermentation for refined flavors. Known for crisp, clean sakes with elegant rice character. Famous for sake rice variety Yamada Nishiki and Sake Komachi."),
        ("Japan &mdash; Yamagata", "The first prefecture to earn a collective geographic indication for premium sake. Known for soft water, elegant ginjo aromatics, and a balanced style. Home to several award-winning kura."),
        ("Japan &mdash; Fukui", "Coastal prefecture on the Sea of Japan, known for clean brewing water and traditional methods. Produces full-flavored sakes with depth and character. Home of the legendary Banshu Iwai sake rice."),
        ("Japan &mdash; Iwate", "Northern cold-climate brewing region. Produces clean, dry, well-structured sakes. Famous for the Nanbu Toji guild &mdash; one of Japan's most respected brewing traditions. Crisp and food-friendly."),
    ]

    rows = ""
    for region, desc in regions:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #2A4A73; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 120px; font-size: 8.5pt; font-weight: 700; color: #0F1628;">{region}</div>
        <div style="font-size: 7.5pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Sake Regions -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Sake Regions of Japan</span>
  </div>

  <div class="page-title">Sake Regions Guide</div>
  <div class="page-subtitle">Where your sake is born shapes what it tastes like</div>

  {rows}

  <div class="page-footer">
    <span>Sake Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def tasting_terms_reference():
    terms = [
        ("Seimaibuai (Rice Polishing Ratio)", "The percentage of the rice grain that remains after polishing. Lower numbers mean more of the grain is milled away. 70%% remaining = Junmai/Honjozo; 60%% = Ginjo; 50%% or less = Daiginjo. More polishing removes proteins and fats that cause off-flavors, resulting in cleaner, more refined sake."),
        ("Nihonshudo (Sake Meter Value)", "A measure of sweetness vs. dryness. Also called SMV. Zero is neutral; positive numbers (e.g., +5) indicate drier sake; negative numbers (e.g., -5) indicate sweeter sake. It measures the density of the sake relative to water."),
        ("K&omacr;ji", "Aspergillus oryzae mold cultivated on steamed rice. Essential to sake brewing &mdash; it converts rice starches into fermentable sugars (the role malting plays in beer). The quality of koji determines the quality of the sake. No koji, no sake."),
        ("Umami", "The fifth taste &mdash; savory depth. In sake, umami comes from amino acids produced during fermentation. Junmai-style sakes typically have more umami than ginjo styles. Umami-rich sake pairs beautifully with savory foods."),
        ("Tanrei Karakuchi", "A tasting descriptor meaning crisp, clean, light, and dry. The quintessential Niigata style. Associated with snow country water and cold-region brewing. The opposite of nojun (rich and full-bodied)."),
        ("Kura (Brewery)", "The traditional term for a sake brewery. Also called sakagura. Japan has approximately 1,200 kura, each with its own water source, yeast strains, and brewing philosophy. Many kura have operated for centuries within the same family."),
        ("Yamahai / Kimoto", "Traditional starter methods that produce sake with deeper body, higher acidity, and more complex flavors. These methods forgo the modern shortcut of adding lactic acid, instead allowing natural lactic bacteria to develop over weeks. Bold, gamey, and food-friendly."),
        ("Namazake (Unpasteurized)", "Sake that has not been heat-treated. Almost all sake is pasteurized twice to stabilize it; nama skips one or both pasteurizations. Result: fresh, vivid, aromatic, with a slight effervescence. Must be refrigerated and consumed promptly."),
    ]

    rows = ""
    for term, desc in terms:
        rows += f'''
      <div style="border: 1px solid #D8D8E8; border-radius: 3px; padding: 7px 9px; margin-bottom: 6px; background: #FCFAF7;">
        <div style="font-size: 9.5pt; font-weight: 700; color: #0F1628; margin-bottom: 3px;">{term}</div>
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
  <div class="page-subtitle">Speak the language of sake</div>

  {rows}

  <div class="page-footer">
    <span>Sake Tasting Journal</span>
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


def tasting_log_left(session_num):
    """Left page of two-page tasting spread — sake info + flavor ratings"""
    return f'''
<!-- Page {pn()}: Session {session_num} Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Session #{session_num:02d}</span>
    <span class="sh-right">Sake Tasting Journal</span>
  </div>

  <div class="page-title">Tasting #{session_num:02d}</div>
  <div class="page-subtitle">Sake Details &amp; Tasting Parameters</div>

  <!-- Sake Info -->
  <div style="background: #FAF6F0; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 36px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 36px;">Time</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 38px;">Name</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 50px;">Kura</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 38px;">Region</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 54px;">Rice Type</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 48px;">Yeast</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 48px;">Polishing</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 48px;">SMV</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 48px;">Acidity</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 36px;">ABV%</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 36px;">Price</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 54px;">Bottle Size</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Sake Type -->
  <div style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Type</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Junmai</span>
    <span class="check-item"><span class="check-box"></span> Honj&omacr;z&omacr;</span>
    <span class="check-item"><span class="check-box"></span> Ginj&omacr;</span>
    <span class="check-item"><span class="check-box"></span> Daiginj&omacr;</span>
    <span class="check-item"><span class="check-box"></span> Junmai Ginj&omacr;</span>
    <span class="check-item"><span class="check-box"></span> Junmai Daiginj&omacr;</span>
    <span class="check-item"><span class="check-box"></span> Nigori</span>
    <span class="check-item"><span class="check-box"></span> Nama</span>
    <span class="check-item"><span class="check-box"></span> Other</span>
  </div>

  <!-- Serving Temperature -->
  <div style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Serving Temperature</div>
  <div class="check-row" style="margin-bottom: 10px;">
    <span class="check-item"><span class="check-box"></span> Chilled (5&ndash;10&deg;C)</span>
    <span class="check-item"><span class="check-box"></span> Cool (10&ndash;15&deg;C)</span>
    <span class="check-item"><span class="check-box"></span> Room (15&ndash;20&deg;C)</span>
    <span class="check-item"><span class="check-box"></span> Warm (35&ndash;40&deg;C)</span>
    <span class="check-item"><span class="check-box"></span> Hot (40&ndash;45&deg;C)</span>
  </div>

  <!-- Appearance -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
    <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 60px;">Appearance</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Flavor Ratings (1-5 scale) -->
  <div style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 6px;">Flavor Ratings &mdash; Fill in circles (1 = weak, 5 = strong)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Sweetness</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Acidity</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Umami</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Body</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Aroma</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Finish</span>
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
  <div class="page-subtitle">Aromas, flavors, and your overall impression</div>

  <!-- Nose (Aroma) -->
  <div style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Nose / Aroma</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Flavor Notes Checklist -->
  <div style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Flavor Notes &mdash; Check What You Taste</div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Melon</span>
    <span class="check-item"><span class="check-box"></span> Apple</span>
    <span class="check-item"><span class="check-box"></span> Pear</span>
    <span class="check-item"><span class="check-box"></span> Banana</span>
    <span class="check-item"><span class="check-box"></span> Lychee</span>
    <span class="check-item"><span class="check-box"></span> Strawberry</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Anise</span>
    <span class="check-item"><span class="check-box"></span> Rice</span>
    <span class="check-item"><span class="check-box"></span> Lactic</span>
    <span class="check-item"><span class="check-box"></span> Umami</span>
    <span class="check-item"><span class="check-box"></span> Mushroom</span>
    <span class="check-item"><span class="check-box"></span> Cereal</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Honey</span>
    <span class="check-item"><span class="check-box"></span> Caramel</span>
    <span class="check-item"><span class="check-box"></span> Nutty</span>
    <span class="check-item"><span class="check-box"></span> Mineral</span>
    <span class="check-item"><span class="check-box"></span> Earthy</span>
    <span class="check-item"><span class="check-box"></span> Herbal</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Pepper</span>
    <span class="check-item"><span class="check-box"></span> Cinnamon</span>
    <span class="check-item"><span class="check-box"></span> Ginger</span>
    <span class="check-item"><span class="check-box"></span> Floral</span>
    <span class="check-item"><span class="check-box"></span> Green Tea</span>
    <span class="check-item"><span class="check-box"></span> Vanilla</span>
  </div>

  <!-- Other flavors -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-top: 4px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; min-width: 50px;">Other</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Overall Rating -->
  <div style="display: flex; align-items: center; gap: 8px; margin-top: 8px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; letter-spacing: 0.4pt;">Overall Rating</span>
    <span class="stars">&starf; &starf; &starf; &starf; &starf;</span>
  </div>

  <!-- Would Buy Again? -->
  <div class="check-row" style="margin-bottom: 8px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Would Buy Again</span>
    <span class="check-item"><span class="check-box"></span> Would Recommend</span>
    <span class="check-item"><span class="check-box"></span> New Favorite</span>
  </div>

  <!-- Detailed Tasting Notes (freeform) -->
  <div style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Detailed Tasting Notes</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Food Pairing Suggestions -->
  <div style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Food Pairing Suggestions</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- What to Try Next Time -->
  <div style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">What to Try Next</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Session #{session_num:02d} &mdash; Notes</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def cellar_inventory(page_of, total_pages):
    """Sake cellar inventory page"""
    return f'''
<!-- Page {pn()}: Sake Cellar -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Sake Shelf</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Sake Shelf</div>
  <div class="page-subtitle">Keep track of what you have and what to seek out</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Sake &amp; Kura</th>
      <th style="width:42px;">Type</th>
      <th style="width:38px;">Polish</th>
      <th style="width:48px;">Region</th>
      <th style="width:28px;">Rating</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">1</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">2</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">3</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">4</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">5</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">6</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">7</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">8</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">9</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">10</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">11</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">12</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Rating: 1&ndash;5 (5 = best) | Type: Junmai/Honjozo/Ginjo/Daiginjo/etc. | Polish: Seimaibuai (%% remaining)</div>

  <div class="page-footer">
    <span>Sake Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def kura_log(page_of, total_pages):
    """Favorite breweries and sake shops"""
    return f'''
<!-- Page {pn()}: Kura Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Kura &amp; Shops</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Kura &amp; Shop Log</div>
  <div class="page-subtitle">Where to find great sake</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Name</th>
      <th style="width:70px;">Location</th>
      <th style="width:62px;">Specialty</th>
      <th>Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">6</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">7</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">8</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">9</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">10</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">11</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A4A73;">12</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Go-To Shop</div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #1E3A5F; text-transform: uppercase; min-width: 38px;">Name</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #1E3A5F; text-transform: uppercase; min-width: 38px;">Why I Love It</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #1E3A5F; text-transform: uppercase; min-width: 38px;">Usual Pick</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Sake Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def vessels_accessories():
    """Sake vessels & accessories inventory"""
    return f'''
<!-- Page {pn()}: Vessels & Accessories -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Vessels</span>
    <span class="sh-right">My Tasting Kit</span>
  </div>

  <div class="page-title">Vessels &amp; Accessories</div>
  <div class="page-subtitle">Know your kit</div>

  <div class="gear-card">
    <div class="gear-label">Sake Vessels</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Material / Style</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Tokkuri (Flasks)</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Material / Size</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Warming Tools</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Material / Model</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Notebook &amp; Accessories</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Item</th><th>Type / Size</th><th>Spare?</th></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Sake Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def sake_regions_checklist():
    """Sake regions checklist — prefectures around Japan"""
    origins = [
        "Niigata", "Hy&omacr;go (Nada)", "Ky&omacr;to (Fushimi)",
        "Hiroshima", "Akita", "Yamagata",
        "Fukui", "Iwate", "Miyagi",
        "Yamanashi", "Nagano", "Shizuoka",
        "Aichi", "Gifu", "Mie",
        "Shiga", "Osaka", "Okayama",
        "Shimane", "Tottori", "Kagawa",
        "Tokushima", "K&omacr;chi", "Ehime",
        "Fukuoka", "Saga", "Nagasaki",
        "Kumamoto", "Kagoshima", "Okinawa",
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
<!-- Page {pn()}: Regions Checklist -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Regions Checklist</span>
    <span class="sh-right">Japan Sake Tour</span>
  </div>

  <div class="page-title">Sake Regions Checklist</div>
  <div class="page-subtitle">Taste your way through Japan's prefectures</div>

  <table class="data-table region-list" style="font-size: 7.5pt;">
    <tr>
      <th style="width:22px;">#</th>
      <th>Prefecture</th>
      <th style="width:70px;">First Tried</th>
      <th style="width:70px;">Rating</th>
      <th style="width:28px;">&#10003;</th>
    </tr>
    {rows}
  </table>

  <div class="page-footer">
    <span>Sake Tasting Journal</span>
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
    <span class="sh-right">Your Sake Year in Review</span>
  </div>

  <div class="page-title">Sake Year in Review</div>
  <div class="page-subtitle">Fill in at the end of your tasting journey</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Sakes Tasted</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Regions Tried</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Styles Discovered</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Top 5 Sakes</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Sake / Kura</th>
      <th style="width:55px;">Region</th>
      <th style="width:35px;">Rating</th>
      <th>Why It Stood Out</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Personal Discoveries</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Winner</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#0F1628;">Favorite Style</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#0F1628;">Favorite Region</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#0F1628;">Favorite Kura</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#0F1628;">Best Value Sake</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#0F1628;">Best New Discovery</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1628; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">What I Want to Explore Next</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Sake Tasting Journal</span>
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

  <div class="page-title">Sake Notes</div>
  <div class="page-subtitle">Ideas, pairings, and reminders</div>

  {lines}

  <div class="page-footer">
    <span>Sake Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def sketch_page():
    """Dot grid page for sketching tasting notes and label ideas"""
    return f'''
<!-- Page {pn()}: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Sketch Pad</span>
    <span class="sh-right">Tasting Maps &amp; Label Sketches</span>
  </div>

  <div class="page-title">Sketch Pad</div>
  <div class="page-subtitle">Draw flavor maps, sketch labels, plan tasting flights</div>

  <div class="dot-grid" style="width: 100%; height: 6.5in; border-radius: 4px;"></div>

  <div class="page-footer">
    <span>Sake Tasting Journal</span>
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
    pages.append(sake_types_reference())           # 5: Sake types
    pages.append(sake_regions_reference())         # 6: Sake regions
    pages.append(tasting_terms_reference())        # 7: Tasting terms

    # ---- Section 1: Tasting Logs ----
    pages.append(divider_section(1, "One", "Tasting Logs", "40 sessions &mdash; your sake journey"))
    NUM_SESSIONS = 40
    for i in range(1, NUM_SESSIONS + 1):
        pages.append(tasting_log_left(i))          # Left page: details
        pages.append(tasting_log_right(i))         # Right page: notes

    # ---- Section 2: Sake Shelf ----
    pages.append(divider_section(2, "Two", "Sake Shelf", "Your sake collection at a glance"))
    pages.append(cellar_inventory(1, 3))
    pages.append(cellar_inventory(2, 3))
    pages.append(cellar_inventory(3, 3))

    # ---- Section 3: Kura & Shops ----
    pages.append(divider_section(3, "Three", "Kura &amp; Shops", "Where to find great sake"))
    pages.append(kura_log(1, 2))
    pages.append(kura_log(2, 2))

    # ---- Section 4: Vessels & Accessories ----
    pages.append(divider_section(4, "Four", "Vessels &amp; Accessories", "Your tasting kit"))
    pages.append(vessels_accessories())

    # ---- Section 5: Regions & Favorites ----
    pages.append(divider_section(5, "Five", "Regions &amp; Favorites", "Your sake world map"))
    pages.append(sake_regions_checklist())
    pages.append(favorites_summary())
    pages.append(sketch_page())

    # ---- Section 6: Notes ----
    pages.append(divider_section(6, "Six", "Notes", "Ideas, pairings, and reminders"))
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
    print(f"  Reference (how-to, flavor wheel, types, regions, terms): 5")
    print(f"  Section dividers: 6")
    print(f"  Tasting logs ({NUM_SESSIONS} sessions x 2 pages): {NUM_SESSIONS * 2}")
    print(f"  Sake shelf: 3")
    print(f"  Kura log: 2")
    print(f"  Vessels & accessories: 1")
    print(f"  Regions checklist: 1")
    print(f"  Favorites summary: 1")
    print(f"  Sketch page: 1")
    print(f"  Notes pages: 10")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
