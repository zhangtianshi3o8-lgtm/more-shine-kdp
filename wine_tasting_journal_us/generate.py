#!/usr/bin/env python3
"""
Wine Tasting Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: American wine enthusiasts (all levels, all types)
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "wine_tasting_journal_us_V1.0.html")

BOOK_TITLE = "Wine Tasting Journal"
BOOK_SUBTITLE = "Track Every Glass, Every Vintage, Every Discovery"

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
/* Deep charcoal: #15080B, #231016 */
/* Wine red: #6B1F2A, #8B2D3A */
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
  background: linear-gradient(165deg, #15080B 0%, #231016 30%, #15080B 65%, #0E0506 100%);
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
    radial-gradient(ellipse 28px 17px at 70% 70%, #8B2D3A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #8B2D3A, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 90% 40%, #8B2D3A, transparent),
    radial-gradient(ellipse 16px 10px at 40% 90%, #C4A04A, transparent);
}

/* ===== CSS Wine Glass Illustration ===== */
.cover .glass-wrap {
  width: 130px; height: 170px;
  position: relative;
  margin: 0 auto 20px;
}

/* Glass bowl — tulip shape using clip-path */
.cover .glass-bowl {
  width: 80px; height: 70px;
  position: absolute;
  top: 10px; left: 25px;
  background: linear-gradient(160deg,
    rgba(250,246,240,0.10) 0%,
    rgba(250,246,240,0.04) 40%,
    rgba(139,45,58,0.06) 80%,
    rgba(107,31,42,0.08) 100%);
  clip-path: polygon(
    18% 0%, 82% 0%,
    88% 40%, 96% 75%,
    78% 98%, 22% 98%,
    4% 75%, 12% 40%
  );
}

/* Glass bowl outline glow */
.cover .glass-bowl-glow {
  width: 84px; height: 74px;
  position: absolute;
  top: 8px; left: 23px;
  background: linear-gradient(180deg, rgba(196,160,74,0.25), rgba(196,160,74,0.05));
  clip-path: polygon(
    18% 0%, 82% 0%,
    88% 40%, 96% 75%,
    78% 98%, 22% 98%,
    4% 75%, 12% 40%
  );
  filter: blur(3px);
  z-index: 0;
}

/* Wine liquid inside bowl */
.cover .glass-liquid {
  width: 64px; height: 32px;
  position: absolute;
  top: 42px; left: 33px;
  background: linear-gradient(180deg,
    #8B2D3A 0%,
    #6B1F2A 40%,
    #4A1520 100%);
  clip-path: polygon(
    0% 0%, 100% 0%,
    90% 100%, 10% 100%
  );
  border-radius: 0 0 4px 4px;
  box-shadow: inset 0 -5px 8px rgba(0,0,0,0.3);
  z-index: 1;
}

/* Liquid surface highlight */
.cover .glass-liquid-shine {
  width: 52px; height: 4px;
  position: absolute;
  top: 42px; left: 39px;
  background: linear-gradient(90deg, transparent, rgba(250,246,240,0.4), transparent);
  border-radius: 50%;
  z-index: 2;
}

/* Glass shine highlight */
.cover .glass-shine {
  width: 8px; height: 40px;
  position: absolute;
  top: 25px; left: 36px;
  background: linear-gradient(180deg, rgba(250,246,240,0.5), rgba(250,246,240,0.05));
  border-radius: 50%;
  transform: rotate(-8deg);
  z-index: 3;
}

/* Glass rim — top ellipse */
.cover .glass-rim {
  width: 48px; height: 7px;
  position: absolute;
  top: 10px; left: 41px;
  border: 1.5px solid rgba(196,160,74,0.6);
  border-radius: 50%;
  background: transparent;
  z-index: 2;
}

/* Stem of wine glass */
.cover .glass-stem {
  width: 10px; height: 55px;
  position: absolute;
  top: 78px; left: 60px;
  background: linear-gradient(90deg,
    rgba(250,246,240,0.05) 0%,
    rgba(250,246,240,0.15) 40%,
    rgba(250,246,240,0.05) 60%,
    rgba(250,246,240,0.02) 100%);
  border-radius: 2px;
}

/* Stem outline */
.cover .glass-stem-outline {
  width: 12px; height: 57px;
  position: absolute;
  top: 77px; left: 59px;
  border-left: 1px solid rgba(196,160,74,0.35);
  border-right: 1px solid rgba(196,160,74,0.35);
  border-radius: 2px;
}

/* Base of glass */
.cover .glass-base {
  width: 54px; height: 10px;
  position: absolute;
  top: 131px; left: 38px;
  background: linear-gradient(180deg,
    rgba(250,246,240,0.12),
    rgba(250,246,240,0.03));
  border: 1px solid rgba(196,160,74,0.4);
  border-radius: 50%;
  box-shadow: 0 3px 8px rgba(0,0,0,0.4);
}

/* Base reflection */
.cover .glass-base-shine {
  width: 28px; height: 3px;
  position: absolute;
  top: 134px; left: 43px;
  background: rgba(196,160,74,0.3);
  border-radius: 50%;
}

/* Vapor/aroma lines rising from glass */
.cover .vapor1 {
  width: 2px; height: 22px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.35), transparent);
  position: absolute;
  top: -2px; left: 53px;
  border-radius: 50%;
  transform: rotate(-8deg);
}
.cover .vapor2 {
  width: 2px; height: 28px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.25), transparent);
  position: absolute;
  top: -8px; left: 66px;
  border-radius: 50%;
  transform: rotate(6deg);
}
.cover .vapor3 {
  width: 2px; height: 20px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.2), transparent);
  position: absolute;
  top: 0px; left: 41px;
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
  background: linear-gradient(165deg, #15080B 0%, #231016 50%, #15080B 100%);
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
    radial-gradient(ellipse 22px 13px at 70% 75%, #8B2D3A, transparent),
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
  border-bottom: 1.5px solid #6B1F2A;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #15080B;
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
  color: #15080B;
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
  background: #6B1F2A;
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
  color: #15080B;
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
  border-left: 3px solid #6B1F2A;
  padding: 8px 10px;
  margin-bottom: 10px;
  font-size: 8pt;
  color: #333;
  line-height: 1.5;
}
.info-box .info-title {
  font-weight: 700;
  color: #15080B;
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
  color: #15080B;
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
  border: 1.5px solid #6B1F2A;
  border-radius: 50%;
  display: inline-block;
}

/* ---- Flavor Category Card ---- */
.flavor-cat {
  border: 1px solid #E8D8C8;
  border-radius: 4px;
  padding: 6px 8px;
  margin-bottom: 5px;
  background: #FCFAF7;
}
.flavor-cat-label {
  font-size: 7pt;
  font-weight: 700;
  color: #6B1F2A;
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
  border: 1px solid #E8D8C8;
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
  color: #15080B;
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
  color: #6B1F2A;
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
  background: #8B2D3A;
}
table.region-list td:first-child {
  width: 22px;
  text-align: center;
  font-weight: 700;
  color: #8B2D3A;
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
  <div class="glass-wrap">
    <div class="vapor1"></div>
    <div class="vapor2"></div>
    <div class="vapor3"></div>
    <div class="glass-bowl-glow"></div>
    <div class="glass-bowl"></div>
    <div class="glass-rim"></div>
    <div class="glass-liquid"></div>
    <div class="glass-liquid-shine"></div>
    <div class="glass-shine"></div>
    <div class="glass-stem-outline"></div>
    <div class="glass-stem"></div>
    <div class="glass-base"></div>
    <div class="glass-base-shine"></div>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">40 Tasting Sessions</span>
      <span class="feature-badge">Flavor Wheel</span>
      <span class="feature-badge">Wine Cellar</span>
      <span class="feature-badge">Regions Guide</span>
    </div>
    <div class="tagline">For Wine Lovers &amp; Explorers</div>
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
    <div style="font-size: 16pt; font-weight: 700; color: #15080B; margin-bottom: 6px;">This Journal Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #15080B; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #6B1F2A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Wine Type</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #6B1F2A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Varietal</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #6B1F2A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Region</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #6B1F2A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Preferred Glass</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Wine Tasting Journal</span>
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
  <div class="page-subtitle">Make every glass a learning experience</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Wine Journal?</div>
    The difference between drinking wine and understanding wine is attention. A tasting journal helps you discover patterns &mdash; which varietals you gravitate toward, how oak and terroir shape flavor, what regions deliver the character you love. Over time, your journal becomes your personal wine roadmap.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #15080B; font-size: 10pt; margin-bottom: 6px;">The Five S's of Wine Tasting</div>

    <div style="margin-bottom: 10px;">
      <strong>1. See.</strong> Hold your glass at a 45-degree angle over a white surface. Note the color, depth, and clarity. Young reds are purple and opaque; older wines show brick-orange at the rim. White wines deepen from pale straw to gold with age.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Swirl.</strong> Give the glass a few gentle rotations on the table. This exposes the wine to air and releases its aromas. The tears (or legs) that drip down the glass hint at the wine's alcohol and body.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Sniff.</strong> Lower your nose into the glass and take short, gentle sniffs. Your nose detects far more than your palate ever will. Try to identify fruit, floral, spice, and earth notes. With practice, the aromas become vivid and specific.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Sip.</strong> Take a small sip and let it coat your tongue. Move it around your mouth. Note the sweetness, acidity, tannins, body, and flavor intensity. The texture is just as important as the taste.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Savor.</strong> Pay attention to the finish &mdash; the flavors and sensations that linger after you swallow. A long, evolving finish is the hallmark of a quality wine. Note how long it lasts and what it reveals.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Pro Tip:</strong> Always taste wine at the right temperature. Reds are best slightly below room temperature (60&ndash;65&deg;F). Whites and ros&eacute;s should be chilled but not ice-cold (45&ndash;50&deg;F). Temperature dramatically affects how aromas and flavors come across.
  </div>

  <div class="page-footer">
    <span>Wine Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def flavor_wheel():
    categories = [
        ("Red Fruit",
         "Cherry &bull; Raspberry &bull; Strawberry &bull; Cranberry &bull; Red Plum &bull; Red Currant"),
        ("Dark Fruit",
         "Blackberry &bull; Black Cherry &bull; Blueberry &bull; Cassis &bull; Fig &bull; Prune"),
        ("Oak &amp; Toast",
         "Vanilla &bull; Toasted Oak &bull; Cedar &bull; Smoke &bull; Coconut &bull; Mocha &bull; Char"),
        ("Earth &amp; Mineral",
         "Mushroom &bull; Forest Floor &bull; Wet Stone &bull; Leather &bull; Tobacco &bull; Petrichor"),
        ("Floral &amp; Herbal",
         "Violet &bull; Rose &bull; Lavender &bull; Thyme &bull; Sage &bull; Mint &bull; Eucalyptus"),
        ("Spice",
         "Black Pepper &bull; White Pepper &bull; Cinnamon &bull; Clove &bull; Nutmeg &bull; Licorice &bull; Anise"),
        ("Citrus &amp; Orchard",
         "Lemon &bull; Lime &bull; Grapefruit &bull; Green Apple &bull; Pear &bull; Quince &bull; White Peach"),
        ("Tropical &amp; Sweet",
         "Pineapple &bull; Mango &bull; Melon &bull; Passion Fruit &bull; Honey &bull; Caramel &bull; Butterscotch"),
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

  <div class="page-title">Wine Flavor Wheel</div>
  <div class="page-subtitle">Find the words for what you taste</div>

  {rows}

  <div style="margin-top: 8px; padding: 6px 8px; background: #FAF6F0; border-radius: 3px; font-size: 7pt; color: #888; font-style: italic;">
    Use these categories as a starting point. Your palate is unique &mdash; trust your own descriptions. The goal is to recognize patterns in what you enjoy.
  </div>

  <div class="page-footer">
    <span>Wine Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def wine_types_reference():
    methods = [
        ("Red Wine", "Made from dark-skinned grapes fermented with the grape skins, giving it color, tannin, and body. Ranges from light and elegant Pinot Noir to bold and structured Cabernet Sauvignon.", "Best for: Pairing with red meat, hearty pasta, aging"),
        ("White Wine", "Made from green or dark-skinned grapes pressed immediately to avoid skin contact. From crisp, mineral Sauvignon Blanc to rich, buttery Chardonnay.", "Best for: Seafood, poultry, sipping chilled"),
        ("Ros&eacute;", "Made from red grapes with limited skin contact (a few hours), resulting in a pink color. Fresh, vibrant, and food-friendly. Can be dry or slightly sweet.", "Best for: Summer sipping, salads, light appetizers"),
        ("Sparkling Wine", "Wine with significant carbonation from a secondary fermentation. Methods include traditional bottle fermentation and tank methods. Ranges from bone-dry to sweet.", "Best for: Celebrations, oysters, brunch"),
        ("Dessert Wine", "Sweet wines made from late-harvest, frozen, or botrytis-affected grapes. Concentrated, luscious, and complex. Includes late harvest and ice wine styles.", "Best for: Pairing with dessert, blue cheese, foie gras"),
        ("Fortified Wine", "Wine fortified with a distilled spirit (brandy). Includes Port, Sherry, and Madeira. Rich, complex, and higher in alcohol (17&ndash;22% ABV).", "Best for: After-dinner sipping, pairings with strong cheese"),
        ("Orange Wine", "White wine made with extended skin contact, like a red wine process. Amber color with tannic structure and unusual flavor profile. An ancient winemaking style.", "Best for: Adventurous drinkers, pairing with bold flavors"),
        ("Natural Wine", "Wine made with minimal intervention &mdash; native yeast, little or no sulfur, no additives. Unfiltered and unpredictable. Growing in popularity among wine enthusiasts.", "Best for: Curious palates, exploring new flavors"),
    ]

    rows = ""
    for name, desc, best in methods:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #6B1F2A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 88px; font-size: 8pt; font-weight: 700; color: #15080B;">{name}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4; flex: 1;">{desc}<br><span style="color: #6B1F2A; font-weight: 700;">{best}</span></div>
      </div>'''

    return f'''
<!-- Page {pn()}: Wine Types -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Wine Types Guide</span>
  </div>

  <div class="page-title">Wine Types Guide</div>
  <div class="page-subtitle">Every style has a story and a flavor profile</div>

  {rows}

  <div class="page-footer">
    <span>Wine Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def wine_regions_reference():
    regions = [
        ("France &mdash; Bordeaux", "The world's largest fine wine region, famous for Cabernet Sauvignon and Merlot blends. Left Bank is Cabernet-dominant; Right Bank favors Merlot. Structured, age-worthy reds."),
        ("France &mdash; Burgundy", "The spiritual home of Pinot Noir and Chardonnay. Tiny, fragmented vineyards produce some of the world's most sought-after wines. Elegant, terroir-driven, and expensive."),
        ("France &mdash; Champagne", "The birthplace of sparkling wine made by the traditional method. Only three grapes: Chardonnay, Pinot Noir, and Pinot Meunier. Bubbles, elegance, and prestige."),
        ("France &mdash; Rh&ocirc;ne Valley", "Syrah rules the north (bold, peppery, dark); Grenache leads the south (ripe, spicy, generous). Outstanding value and character at every level."),
        ("Italy &mdash; Tuscany", "Home of Sangiovese-based wines: Chianti, Brunello, and Super Tuscans. Bright acidity, cherry fruit, and earthy undertones. Food-friendly and classic."),
        ("Italy &mdash; Piedmont", "Nebbiolo country &mdash; Barolo and Barbaresco are among Italy's most prestigious reds. Tar and roses, high tannin, and extraordinary aging potential."),
        ("Spain &mdash; Rioja", "Tempranillo-based reds aged in American and French oak. Known for vanilla, leather, and dried fruit notes. Classified by aging: Crianza, Reserva, Gran Reserva."),
        ("Germany &mdash; Mosel", "The world's premier Riesling region. Steep slate slopes along the river produce wines with electric acidity, delicate fruit, and a distinctive mineral edge."),
        ("USA &mdash; California", "America's largest wine state. Napa Valley is famous for world-class Cabernet Sauvignon; Sonoma offers diversity from Pinot Noir to Zinfandel. Bold, ripe, and fruit-forward."),
        ("USA &mdash; Oregon", "Willamette Valley is Pinot Noir paradise &mdash; cool climate, elegant wines with bright acidity. Often compared to Burgundy in style. Also excellent Pinot Gris and Chardonnay."),
        ("Australia &mdash; Barossa Valley", "Old-vine Shiraz with rich, concentrated dark fruit, spice, and soft tannins. Also outstanding Grenache and Riesling from nearby Clare Valley."),
        ("New Zealand &mdash; Marlborough", "The defining region for Sauvignon Blanc: pungent, zesty, with passion fruit and grapefruit. Also producing excellent Pinot Noir and sparkling wines."),
    ]

    rows = ""
    for country, desc in regions:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #8B2D3A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 115px; font-size: 8.5pt; font-weight: 700; color: #15080B;">{country}</div>
        <div style="font-size: 7.5pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Wine Regions -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Wine Regions of the World</span>
  </div>

  <div class="page-title">Wine Regions Guide</div>
  <div class="page-subtitle">Where your wine comes from shapes what it tastes like</div>

  {rows}

  <div class="page-footer">
    <span>Wine Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def tasting_terms_reference():
    terms = [
        ("Nose", "The aroma of the wine &mdash; what you smell before you taste. Swirl the glass to release aromas, then take short sniffs. The nose reveals the grape variety, oak treatment, and age."),
        ("Palate", "The flavors and textures you experience as the wine enters your mouth. Take a small sip and let it coat your tongue. Note sweetness, acidity, tannin, body, and flavor intensity."),
        ("Finish", "The lingering flavors and sensations after you swallow. Can be short (fades quickly), medium, or long (lasts 30+ seconds). A great finish evolves and lingers."),
        ("Tannins", "Natural compounds from grape skins, seeds, and oak that create a drying, astringent sensation in your mouth. Essential for red wine structure and aging. Softer in older wines."),
        ("Acidity", "The crisp, tart quality that makes your mouth water. High in cool-climate whites and reds like Sangiovese. Acidity gives wine freshness and makes it food-friendly."),
        ("Body", "The weight and texture of the wine in your mouth &mdash; light (like water), medium (like whole milk), or full (like cream). Determined by alcohol, tannin, sugar, and extract."),
        ("Terroir", "The unique combination of soil, climate, and topography that gives a wine its sense of place. A wine that tastes like where it's from has terroir expression."),
        ("Vintage", "The year the grapes were harvested. Weather varies year to year, so the same wine from different vintages can taste quite different. Great vintages age longer and cost more."),
    ]

    rows = ""
    for term, desc in terms:
        rows += f'''
      <div style="border: 1px solid #E8D8C8; border-radius: 3px; padding: 7px 9px; margin-bottom: 6px; background: #FCFAF7;">
        <div style="font-size: 9.5pt; font-weight: 700; color: #15080B; margin-bottom: 3px;">{term}</div>
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
  <div class="page-subtitle">Speak the language of wine</div>

  {rows}

  <div class="page-footer">
    <span>Wine Tasting Journal</span>
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
    """Left page of two-page tasting spread — wine info + flavor ratings"""
    return f'''
<!-- Page {pn()}: Session {session_num} Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Session #{session_num:02d}</span>
    <span class="sh-right">Wine Tasting Journal</span>
  </div>

  <div class="page-title">Tasting #{session_num:02d}</div>
  <div class="page-subtitle">Wine Details &amp; Tasting Parameters</div>

  <!-- Wine Info -->
  <div style="background: #FAF6F0; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; min-width: 36px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; min-width: 36px;">Time</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; min-width: 54px;">Wine</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; min-width: 54px;">Producer</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; min-width: 36px;">Vintage</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; min-width: 54px;">Varietal</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; min-width: 36px;">Region</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; min-width: 54px;">Cask/Oak</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; min-width: 36px;">ABV%</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; min-width: 36px;">Price</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; min-width: 54px;">Bottle Size</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Wine Type -->
  <div style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Type</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Red</span>
    <span class="check-item"><span class="check-box"></span> White</span>
    <span class="check-item"><span class="check-box"></span> Ros&eacute;</span>
    <span class="check-item"><span class="check-box"></span> Sparkling</span>
    <span class="check-item"><span class="check-box"></span> Dessert</span>
    <span class="check-item"><span class="check-box"></span> Fortified</span>
    <span class="check-item"><span class="check-box"></span> Orange</span>
    <span class="check-item"><span class="check-box"></span> Other</span>
  </div>

  <!-- Color Description -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 10px;">
    <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; min-width: 42px;">Color</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Flavor Ratings (1-5 scale) -->
  <div style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Flavor Ratings &mdash; Fill in circles (1 = weak, 5 = strong)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Tannin</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
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
    <span class="rating-bar-label">Alcohol</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Finish Length</span>
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

  <!-- Nose (Aroma) -->
  <div style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Nose / Aroma</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Flavor Notes Checklist -->
  <div style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Flavor Notes &mdash; Check What You Taste</div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Cherry</span>
    <span class="check-item"><span class="check-box"></span> Blackberry</span>
    <span class="check-item"><span class="check-box"></span> Raspberry</span>
    <span class="check-item"><span class="check-box"></span> Cassis</span>
    <span class="check-item"><span class="check-box"></span> Plum</span>
    <span class="check-item"><span class="check-box"></span> Fig</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Vanilla</span>
    <span class="check-item"><span class="check-box"></span> Oak</span>
    <span class="check-item"><span class="check-box"></span> Cedar</span>
    <span class="check-item"><span class="check-box"></span> Smoke</span>
    <span class="check-item"><span class="check-box"></span> Toast</span>
    <span class="check-item"><span class="check-box"></span> Coconut</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Pepper</span>
    <span class="check-item"><span class="check-box"></span> Clove</span>
    <span class="check-item"><span class="check-box"></span> Licorice</span>
    <span class="check-item"><span class="check-box"></span> Earth</span>
    <span class="check-item"><span class="check-box"></span> Mineral</span>
    <span class="check-item"><span class="check-box"></span> Leather</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Floral</span>
    <span class="check-item"><span class="check-box"></span> Violet</span>
    <span class="check-item"><span class="check-box"></span> Citrus</span>
    <span class="check-item"><span class="check-box"></span> Apple</span>
    <span class="check-item"><span class="check-box"></span> Peach</span>
    <span class="check-item"><span class="check-box"></span> Tropical</span>
  </div>

  <!-- Other flavors -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-top: 4px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; min-width: 50px;">Other</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Overall Rating -->
  <div style="display: flex; align-items: center; gap: 8px; margin-top: 8px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; letter-spacing: 0.4pt;">Overall Rating</span>
    <span class="stars">&starf; &starf; &starf; &starf; &starf;</span>
  </div>

  <!-- Would Buy Again? -->
  <div class="check-row" style="margin-bottom: 8px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Would Buy Again</span>
    <span class="check-item"><span class="check-box"></span> Would Recommend</span>
    <span class="check-item"><span class="check-box"></span> New Favorite</span>
  </div>

  <!-- Detailed Tasting Notes (freeform) -->
  <div style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Detailed Tasting Notes</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Food Pairing Suggestions -->
  <div style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Food Pairing Suggestions</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- What to Try Next Time -->
  <div style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">What to Try Next</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Session #{session_num:02d} &mdash; Notes</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def cellar_inventory(page_of, total_pages):
    """Wine cellar inventory page"""
    return f'''
<!-- Page {pn()}: Wine Cellar -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Wine Cellar</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Wine Cellar</div>
  <div class="page-subtitle">Keep track of what you have and what to seek out</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Wine &amp; Producer</th>
      <th style="width:38px;">Type</th>
      <th style="width:32px;">Vintage</th>
      <th style="width:48px;">Varietal</th>
      <th style="width:48px;">Region</th>
      <th style="width:28px;">Rating</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">1</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">2</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">3</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">4</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">5</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">6</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">7</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">8</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">9</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">10</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">11</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">12</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Rating: 1&ndash;5 (5 = best) | Type: Red/White/Ros&#233;/Sparkling/Dessert/Fortified/Orange/Other | ABV: % vol</div>

  <div class="page-footer">
    <span>Wine Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def winery_log(page_of, total_pages):
    """Favorite wineries and wine shops"""
    return f'''
<!-- Page {pn()}: Winery Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Wineries &amp; Shops</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Winery &amp; Shop Log</div>
  <div class="page-subtitle">Where to find great wine</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Name</th>
      <th style="width:70px;">Location</th>
      <th style="width:62px;">Specialty</th>
      <th>Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">6</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">7</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">8</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">9</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">10</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">11</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B2D3A;">12</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Go-To Shop</div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #6B1F2A; text-transform: uppercase; min-width: 38px;">Name</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #6B1F2A; text-transform: uppercase; min-width: 38px;">Why I Love It</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #6B1F2A; text-transform: uppercase; min-width: 38px;">Usual Pick</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Wine Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def glassware_accessories():
    """Glassware & accessories inventory"""
    return f'''
<!-- Page {pn()}: Glassware & Accessories -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Glassware</span>
    <span class="sh-right">My Tasting Kit</span>
  </div>

  <div class="page-title">Glassware &amp; Accessories</div>
  <div class="page-subtitle">Know your kit</div>

  <div class="gear-card">
    <div class="gear-label">Glassware</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Brand / Model</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Decanter &amp; Aerator</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Brand / Model</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Wine Tools</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Brand / Model</th><th>Notes</th></tr>
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
    <span>Wine Tasting Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def wine_regions_checklist():
    """Wine regions checklist — origins around the world"""
    origins = [
        "France &mdash; Bordeaux", "France &mdash; Burgundy", "France &mdash; Champagne", "France &mdash; Rh&ocirc;ne",
        "France &mdash; Loire Valley", "France &mdash; Alsace",
        "Italy &mdash; Tuscany", "Italy &mdash; Piedmont", "Italy &mdash; Veneto", "Italy &mdash; Sicily",
        "Spain &mdash; Rioja", "Spain &mdash; Ribera del Duero", "Spain &mdash; Priorat",
        "Portugal &mdash; Douro", "Portugal &mdash; Vinho Verde",
        "Germany &mdash; Mosel", "Germany &mdash; Rheingau", "Austria &mdash; Wachau",
        "USA &mdash; Napa Valley", "USA &mdash; Sonoma", "USA &mdash; Oregon (Willamette)",
        "Australia &mdash; Barossa Valley", "Australia &mdash; Margaret River",
        "New Zealand &mdash; Marlborough", "Chile &mdash; Central Valley",
        "Argentina &mdash; Mendoza", "South Africa &mdash; Stellenbosch", "Greece &mdash; Santorini",
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
    <span class="sh-right">Wine World Tour</span>
  </div>

  <div class="page-title">Wine Regions Checklist</div>
  <div class="page-subtitle">Taste your way around the wine world</div>

  <table class="data-table region-list" style="font-size: 7.5pt;">
    <tr>
      <th style="width:22px;">#</th>
      <th>Region</th>
      <th style="width:70px;">First Tried</th>
      <th style="width:70px;">Rating</th>
      <th style="width:28px;">&#10003;</th>
    </tr>
    {rows}
  </table>

  <div class="page-footer">
    <span>Wine Tasting Journal</span>
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
    <span class="sh-right">Your Wine Year in Review</span>
  </div>

  <div class="page-title">Wine Year in Review</div>
  <div class="page-subtitle">Fill in at the end of your tasting journey</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Wines Tasted</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Regions Tried</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Varietals Discovered</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Top 5 Wines</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Wine / Producer</th>
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

  <div style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Personal Discoveries</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Winner</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#15080B;">Favorite Wine Type</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#15080B;">Favorite Region</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#15080B;">Favorite Producer</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#15080B;">Best Value Bottle</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#15080B;">Best New Discovery</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #15080B; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">What I Want to Explore Next</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Wine Tasting Journal</span>
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

  <div class="page-title">Wine Notes</div>
  <div class="page-subtitle">Ideas, pairings, and reminders</div>

  {lines}

  <div class="page-footer">
    <span>Wine Tasting Journal</span>
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
  <div class="page-subtitle">Draw flavor maps, sketch bottle labels, plan tasting flights</div>

  <div class="dot-grid" style="width: 100%; height: 6.5in; border-radius: 4px;"></div>

  <div class="page-footer">
    <span>Wine Tasting Journal</span>
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
    pages.append(wine_types_reference())           # 5: Wine types
    pages.append(wine_regions_reference())         # 6: Wine regions
    pages.append(tasting_terms_reference())        # 7: Tasting terms

    # ---- Section 1: Tasting Logs ----
    pages.append(divider_section(1, "One", "Tasting Logs", "40 sessions &mdash; your wine journey"))
    NUM_SESSIONS = 40
    for i in range(1, NUM_SESSIONS + 1):
        pages.append(tasting_log_left(i))          # Left page: details
        pages.append(tasting_log_right(i))         # Right page: notes

    # ---- Section 2: Wine Cellar ----
    pages.append(divider_section(2, "Two", "Wine Cellar", "Your wine shelf at a glance"))
    pages.append(cellar_inventory(1, 3))
    pages.append(cellar_inventory(2, 3))
    pages.append(cellar_inventory(3, 3))

    # ---- Section 3: Wineries & Shops ----
    pages.append(divider_section(3, "Three", "Wineries &amp; Shops", "Where to find great wine"))
    pages.append(winery_log(1, 2))
    pages.append(winery_log(2, 2))

    # ---- Section 4: Glassware & Accessories ----
    pages.append(divider_section(4, "Four", "Glassware &amp; Accessories", "Your tasting kit"))
    pages.append(glassware_accessories())

    # ---- Section 5: Regions & Favorites ----
    pages.append(divider_section(5, "Five", "Regions &amp; Favorites", "Your wine world map"))
    pages.append(wine_regions_checklist())
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
    print(f"  Wine cellar: 3")
    print(f"  Winery log: 2")
    print(f"  Glassware & accessories: 1")
    print(f"  Regions checklist: 1")
    print(f"  Favorites summary: 1")
    print(f"  Sketch page: 1")
    print(f"  Notes pages: 10")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
