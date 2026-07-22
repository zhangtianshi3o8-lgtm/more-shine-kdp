#!/usr/bin/env python3
"""
Beekeeping Log Book — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: American colony beekeepers and nature enthusiasts (all levels)
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "beekeeping_log_book_us_V1.0.html")

BOOK_TITLE = "Beekeeping Log Book"
BOOK_SUBTITLE = "Track Every Hive, Every Harvest, Every Season"

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
/* Forest charcoal: #141A12, #1E2820 */
/* Honey gold: #C4A04A, #B8861C */
/* Beeswax: #E8C547 */
/* Gold accent: #C4A04A */
/* Warm cream: #FAF8F2, #F5F2EA */

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
  background: linear-gradient(165deg, #141A12 0%, #1E2820 30%, #141A12 65%, #0C100A 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Sage glow background */
.cover .glow-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #7A8B6A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #7A8B6A, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 90% 40%, #7A8B6A, transparent),
    radial-gradient(ellipse 16px 10px at 40% 90%, #C4A04A, transparent);
}

/* ===== CSS Colony Illustration ===== */
.cover .colony-wrap {
  width: 130px; height: 170px;
  position: relative;
  margin: 0 auto 20px;
}

/* Colony cap — dome shape using border-radius */
.cover .cap {
  width: 100px; height: 65px;
  position: absolute;
  top: 0; left: 15px;
  background: linear-gradient(170deg,
    rgba(250,248,242,0.12) 0%,
    rgba(250,248,242,0.04) 40%,
    rgba(196,160,74,0.06) 80%,
    rgba(122,139,106,0.08) 100%);
  border-radius: 50% 50% 22% 22% / 80% 80% 20% 20%;
  border: 1.5px solid rgba(196,160,74,0.5);
}

/* Cap highlight */
.cover .cap-shine {
  width: 35px; height: 18px;
  position: absolute;
  top: 10px; left: 32px;
  background: linear-gradient(160deg, rgba(250,248,242,0.25), rgba(250,248,242,0.03));
  border-radius: 50%;
  transform: rotate(-15deg);
}

/* Gills under cap */
.cover .gills {
  width: 80px; height: 14px;
  position: absolute;
  top: 58px; left: 25px;
  background: repeating-linear-gradient(
    90deg,
    transparent 0px,
    transparent 4px,
    rgba(196,160,74,0.2) 4px,
    rgba(196,160,74,0.2) 5px);
  border-radius: 0 0 50% 50% / 0 0 100% 100%;
  clip-path: ellipse(50% 100% at 50% 0%);
}

/* Stem */
.cover .stem {
  width: 26px; height: 85px;
  position: absolute;
  top: 65px; left: 52px;
  background: linear-gradient(90deg,
    rgba(250,248,242,0.04) 0%,
    rgba(250,248,242,0.12) 40%,
    rgba(250,248,242,0.06) 60%,
    rgba(250,248,242,0.02) 100%);
  border-radius: 3px 3px 8px 8px;
  border-left: 1px solid rgba(196,160,74,0.35);
  border-right: 1px solid rgba(196,160,74,0.35);
}

/* Ring/annulus on stem */
.cover .ring {
  width: 36px; height: 8px;
  position: absolute;
  top: 80px; left: 47px;
  background: rgba(196,160,74,0.15);
  border: 1px solid rgba(196,160,74,0.35);
  border-radius: 50%;
}

/* Base/volva */
.cover .base {
  width: 38px; height: 16px;
  position: absolute;
  top: 144px; left: 46px;
  background: linear-gradient(180deg,
    rgba(250,248,242,0.08),
    rgba(250,248,242,0.02));
  border: 1px solid rgba(196,160,74,0.4);
  border-radius: 50%;
  box-shadow: 0 3px 8px rgba(0,0,0,0.4);
}

/* Base shadow */
.cover .base-shadow {
  width: 50px; height: 4px;
  position: absolute;
  top: 158px; left: 40px;
  background: rgba(0,0,0,0.25);
  border-radius: 50%;
  filter: blur(2px);
}

/* Small colony companion */
.cover .cap2 {
  width: 50px; height: 32px;
  position: absolute;
  top: 118px; left: 100px;
  background: linear-gradient(170deg,
    rgba(250,248,242,0.08) 0%,
    rgba(122,139,106,0.08) 100%);
  border-radius: 50% 50% 18% 18% / 75% 75% 25% 25%;
  border: 1px solid rgba(196,160,74,0.35);
}

.cover .stem2 {
  width: 12px; height: 38px;
  position: absolute;
  top: 145px; left: 119px;
  background: rgba(250,248,242,0.05);
  border-left: 0.8px solid rgba(196,160,74,0.25);
  border-right: 0.8px solid rgba(196,160,74,0.25);
  border-radius: 2px;
}

/* Vapor/spore lines */
.cover .spore1 {
  width: 2px; height: 20px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.3), transparent);
  position: absolute;
  top: -6px; left: 45px;
  border-radius: 50%;
  transform: rotate(-8deg);
}
.cover .spore2 {
  width: 2px; height: 26px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.2), transparent);
  position: absolute;
  top: -12px; left: 62px;
  border-radius: 50%;
  transform: rotate(6deg);
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
  color: #D4C49A;
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
  color: #D4C49A;
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
  background: linear-gradient(165deg, #141A12 0%, #1E2820 50%, #141A12 100%);
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
    radial-gradient(ellipse 22px 13px at 70% 75%, #7A8B6A, transparent),
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
  color: #D4C49A;
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
  border-bottom: 1.5px solid #7A8B6A;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #141A12;
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
  color: #141A12;
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
  background: #7A8B6A;
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
  background: #FAF8F2;
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
  color: #141A12;
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
  background: #FAF8F2;
  border-left: 3px solid #7A8B6A;
  padding: 8px 10px;
  margin-bottom: 10px;
  font-size: 8pt;
  color: #333;
  line-height: 1.5;
}
.info-box .info-title {
  font-weight: 700;
  color: #141A12;
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
  color: #141A12;
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
  border: 1.5px solid #7A8B6A;
  border-radius: 50%;
  display: inline-block;
}

/* ---- Category Card ---- */
.cat-card {
  border: 1px solid #D8E0D0;
  border-radius: 4px;
  padding: 6px 8px;
  margin-bottom: 5px;
  background: #FCFBF8;
}
.cat-card-label {
  font-size: 7pt;
  font-weight: 700;
  color: #7A8B6A;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 3px;
}
.cat-card-notes {
  font-size: 7.5pt;
  color: #888;
  line-height: 1.5;
}

/* ---- Stat Card ---- */
.stat-card {
  text-align: center;
  padding: 6px 4px;
  background: #FAF8F2;
  border-radius: 4px;
  border: 1px solid #D8E0D0;
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
  color: #141A12;
}

/* ---- Gear Card ---- */
.gear-card {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 8px;
  margin-bottom: 6px;
  background: #FCFBF8;
}
.gear-card .gear-label {
  font-size: 7pt;
  font-weight: 700;
  color: #7A8B6A;
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

/* ---- Species List ---- */
table.species-list th {
  background: #7A8B6A;
}
table.species-list td:first-child {
  width: 22px;
  text-align: center;
  font-weight: 700;
  color: #7A8B6A;
}
table.species-list td:last-child {
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
  <div class="colony-wrap" style="width:120px; height:130px; position:relative; margin:0 auto 20px;">
    <svg viewBox="0 0 120 130" width="120" height="130" xmlns="http://www.w3.org/2000/svg">
      <!-- Honeycomb hexagons -->
      <polygon points="40,10 70,10 85,35 70,60 40,60 25,35" fill="none" stroke="#C4A04A" stroke-width="1.8" opacity="0.7"/>
      <polygon points="10,60 40,60 55,85 40,110 10,110 -5,85" fill="none" stroke="#C4A04A" stroke-width="1.8" opacity="0.5"/>
      <polygon points="70,60 100,60 115,85 100,110 70,110 55,85" fill="none" stroke="#C4A04A" stroke-width="1.8" opacity="0.5"/>
      <!-- Small bee -->
      <ellipse cx="60" cy="35" rx="5" ry="3" fill="#C4A04A" opacity="0.8"/>
      <line x1="57" y1="34" x2="63" y2="34" stroke="#141A12" stroke-width="0.6"/>
      <line x1="57" y1="36" x2="63" y2="36" stroke="#141A12" stroke-width="0.6"/>
    </svg>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">40 Hive Inspections</span>
      <span class="feature-badge">Hive Health Tracker</span>
      <span class="feature-badge">Honey Harvest Log</span>
      <span class="feature-badge">Seasonal Calendar</span>
    </div>
    <div class="tagline">For Beekeepers &amp; Apiarists</div>
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
    <div style="font-size: 16pt; font-weight: 700; color: #141A12; margin-bottom: 6px;">This Journal Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #141A12; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #7A8B6A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Home Region</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #7A8B6A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Hive</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #7A8B6A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Years Beekeeping</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #7A8B6A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Apiary Location</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
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
  <div class="page-subtitle">Make every inspection a learning experience</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Beekeeping Journal?</div>
    The difference between having hives and understanding them is attention. A beekeeping journal helps you track patterns &mdash; which colonies are thriving, how weather and nectar flows affect production, and which management practices work best. Over time, your journal becomes your personal beekeeping roadmap.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #141A12; font-size: 10pt; margin-bottom: 6px;">Tips for Better Beekeeping</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Inspect regularly but not too often.</strong> A 7-10 day inspection cycle during active season keeps you informed without disrupting the colony. Each opening sets back their work &mdash; be efficient and deliberate.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Always wear protective gear.</strong> Even gentle colonies can become defensive. A veil at minimum, full suit for new beekeepers. Keep a smoker lit and ready before opening any hive.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Record what you see, not what you expect.</strong> Note the brood pattern, queen status, stores, temperament, and any irregularities. Honest observations over time reveal which management decisions lead to success.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Monitor for pests and disease.</strong> Check for varroa mites monthly during active season. Watch for small hive beetles, wax moths, and signs of brood disease. Early detection saves colonies.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Time your inspections wisely.</strong> Inspect on calm, sunny days between 50-90&deg;F when foragers are out working. Avoid disturbing the colony during rain, high wind, or when neighbors are outdoors.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #F5F2E8; border: 1px solid #D8E0C0; border-radius: 3px; font-size: 8pt; color: #555; font-style: italic;">
    <strong style="color: #5A7042;">Pro Tip:</strong> Keep a dedicated hive tool, smoker fuel (pine needles or burlap work well), and a spray bottle of sugar water handy. Sugar water mist calms bees without smoke when you need a gentler approach.
  </div>

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''



def colony_anatomy():
    """Parts of a beehive — educational reference"""
    parts = [
        ("Outer Cover (Telescoping)",
         "The roof of the hive. Protects the colony from rain and weather. "
         "Typically metal-clad or wooden. Should extend slightly over the edges "
         "like a telescoping cover to shed water away from the hive body."),
        ("Inner Cover",
         "A flat board with an oval hole that sits between the outer cover and "
         "the top super. Provides ventilation, prevents the bees from gluing down "
         "the outer cover with propolis, and guides the bees during honey removal."),
        ("Honey Super",
         "The upper boxes where bees store surplus honey. These are the boxes you "
         "harvest from. Shallow supers are lighter when full; medium supers are "
         "versatile. Note the number and size of supers in your inspection log."),
        ("Queen Excluder",
         "A screened or slatted barrier between the brood chamber and honey supers. "
         "Prevents the queen from laying eggs in the honey supers while allowing "
         "worker bees to pass through. Some beekeepers avoid them; others swear by them."),
        ("Brood Chamber (Deep)",
         "The lower boxes where the queen lays eggs and the colony raises new bees. "
         "Contains brood in all stages: eggs, larvae, and capped pupae. This is the "
         "heart of the colony. Note the brood pattern during each inspection."),
        ("Frames & Foundation",
         "Removable wooden or plastic frames hold the wax comb. Foundation can be "
         "pure beeswax, wax-coated plastic, or drone-sized. Standard Langstroth hives "
         "use 10 or 8 frames per box. Inspect frames in order during hive checks."),
        ("Bottom Board",
         "The floor of the hive. Can be solid or screened. Screened bottom boards "
         "aid ventilation and varroa mite monitoring &mdash; fallen mites drop through "
         "and cannot climb back. Some have a removable tray for counting mite drop."),
        ("Entrance Reducer",
         "A small wooden block that narrows the hive entrance. Used in winter and "
         "for new or weak colonies to help them defend against robbers and maintain "
         "temperature. Remove during strong nectar flows for maximum ventilation."),
    ]

    rows = ""
    for name, desc in parts:
        rows += f'''
      <div style="border: 1px solid #D8E0D0; border-radius: 3px; padding: 6px 9px; margin-bottom: 5px; background: #FCFBF8;">
        <div style="font-size: 9pt; font-weight: 700; color: #141A12; margin-bottom: 3px;">{name}</div>
        <div style="font-size: 7.5pt; color: #555; line-height: 1.5;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Hive Anatomy -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Hive Anatomy</span>
  </div>

  <div class="page-title">Hive Anatomy &amp; Components</div>
  <div class="page-subtitle">Know your hive &mdash; understanding starts here</div>

  {rows}

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''



def habitat_guide():
    """Apiary setup and placement considerations"""
    habitats = [
        ("Sun Exposure",
         "Morning sun is ideal &mdash; it warms the hive early, encouraging foraging. "
         "Dappled afternoon shade in hot climates prevents overheating. Avoid full "
         "deep shade, which can make colonies damp and sluggish. Face the entrance "
         "southeast if possible."),
        ("Wind Protection",
         "Site hives behind a windbreak &mdash; a hedge, fence, or building. Winter "
         "winds are the biggest threat to colony survival. A 6-foot barrier reduces "
         "wind chill significantly. Avoid exposed hilltops and open fields."),
        ("Water Source",
         "Bees need water year-round for cooling and brood food. Provide a shallow "
         "water source within 50 feet: a birdbath with rocks, a dripping faucet, or "
         "a chicken waterer with marbles. Without a nearby source, bees will visit "
         "neighbor\'s pools."),
        ("Forage Availability",
         "Assess nectar and pollen sources within a 2-mile radius. Diversity is key: "
         "flowering trees (maples, locusts, lindens), wildflowers, clover fields, "
         "and gardens all contribute. Note bloom times in your journal to anticipate "
         "nectar flows and potential dearth periods."),
        ("Ground & Elevation",
         "Place hives on level, well-drained ground. Elevate on stands (cinder blocks "
         "or pallets) to keep the bottom board dry and deter skunks. Slight forward "
         "tilt prevents rain from blowing into the entrance. Avoid low-lying frost "
         "pockets."),
        ("Flight Path Safety",
         "Direct bee flight paths away from high-traffic areas. A 10-foot buffer "
         "from walkways, patios, and property lines is courteous and often legally "
         "required. Tall plants or a fence force bees to fly upward, keeping them "
         "above head height as they leave the hive."),
        ("Pest & Predator Defense",
         "Elevated stands deter skunks and raccoons. Fencing keeps livestock away. "
         "Watch for bears in rural areas &mdash; electric fencing is the only reliable "
         "deterrent. Ant and small hive beetle management starts with proper siting."),
        ("Accessibility",
         "You will visit your hives often, carrying heavy boxes of honey. Ensure "
         "year-round access: a gravel path, paved walkway, or firm mowed strip. "
         "Consider vehicle access for moving equipment and harvested supers. "
         "Avoid muddy or steep sites that become treacherous in wet weather."),
    ]

    rows = ""
    for name, desc in habitats:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #C4A04A; background: #FAF8F2; border-radius: 0 3px 3px 0;">
        <div style="min-width: 100px; font-size: 8pt; font-weight: 700; color: #141A12;">{name}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Apiary Setup -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Apiary Setup</span>
  </div>

  <div class="page-title">Apiary Setup Guide</div>
  <div class="page-subtitle">Location is the most important decision you will make</div>

  {rows}

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''



def beekeeping_safety():
    """Safety rules for beekeeping"""
    return f'''
<!-- Page {pn()}: Beekeeping Safety -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Safety First</span>
    <span class="sh-right">Read Before You Open a Hive</span>
  </div>

  <div class="page-title">Beekeeping Safety Rules</div>
  <div class="page-subtitle">Respect the bees, protect yourself, protect your neighbors</div>

  <div style="background: #FFF5F5; border: 1.5px solid #C04040; border-radius: 4px; padding: 10px 12px; margin-bottom: 12px;">
    <div style="font-size: 10pt; font-weight: 700; color: #C04040; margin-bottom: 6px;">Allergy Warning</div>
    <div style="font-size: 8.5pt; color: #555; line-height: 1.55;">
      <strong>Know your allergy status before opening any hive.</strong>
      Bee venom can cause severe allergic reactions including anaphylaxis. If you have
      a known allergy, consult your doctor about an EpiPen before keeping bees. Even
      without a known allergy, a beekeeper should know the signs of anaphylaxis and
      keep emergency contact information nearby.
    </div>
  </div>

  <div style="font-size: 8.5pt; line-height: 1.65; color: #333;">
    <div style="margin-bottom: 8px;">
      <strong>1. Always suit up.</strong> Wear at minimum a veil and gloves. New beekeepers
      should use a full suit. As you gain confidence you may reduce protection, but
      never skip the veil &mdash; a sting to the face or eye is always serious.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>2. Use your smoker correctly.</strong> Light the smoker 10 minutes before
      opening the hive. Puffs of cool smoke mask alarm pheromones and trigger feeding
      behavior. Never use hot smoke or blow smoke directly onto bees &mdash; it burns
      their wings.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>3. Move slowly and deliberately.</strong> Quick movements and vibrations
      alarm bees. Frame each action: lift slowly, examine calmly, replace gently. If
      bees become aggressive, close the hive and return another day.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>4. Inform your neighbors.</strong> A jar of honey goes a long way. Let
      neighbors know you keep bees, share your harvest, and provide your phone number
      for any swarming concerns. Good relations prevent complaints and zoning issues.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>5. Keep an emergency plan.</strong> Have antihistamines on hand. Know
      the location of the nearest emergency room. If stung and you feel dizzy, have
      trouble breathing, or develop hives away from the sting site, seek emergency
      care immediately.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>6. Register your apiary.</strong> Many states require apiary registration
      for disease tracking. Check your local agricultural extension office for
      regulations. Registration also connects you with local inspectors and resources.
    </div>
  </div>

  <div style="margin-top: 10px; padding: 7px 10px; background: #FAF8F2; border: 1px solid #E0D8C0; border-radius: 3px; font-size: 7.5pt; color: #777; font-style: italic;">
    This journal is a record-keeping tool. It is not a beekeeping manual and cannot replace hands-on training. Always consult experienced local beekeepers and your state extension service for region-specific guidance.
  </div>

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''



def seasonal_calendar():
    """Seasonal beekeeping calendar reference"""
    seasons = [
        ("Spring (Mar &ndash; May)",
         "The critical season. Queens begin laying rapidly as days lengthen. "
         "Inspect for queen health and brood pattern. Reverse brood boxes if "
         "the cluster has moved up. Add supers before the first nectar flow. "
         "Watch for swarming &mdash; create splits or add space to prevent it. "
         "This is when you set up the colony\'s success for the entire year.",
         "Monitor: Queen status, swarm cells, brood pattern, varroa mites, food stores"),
        ("Summer (Jun &ndash; Aug)",
         "Peak honey production and nectar flows. Check supers every 7-10 days "
         "during heavy flows and add space as needed. Monitor for robbing during "
         "dearth periods. Keep water sources full. Extract honey when frames are "
         "capped at least 80%. Watch for small hive beetles and wax moths in hot "
         "weather. Do your varroa mite treatments after honey harvest.",
         "Monitor: Honey supers, mite levels, robbing, beetles, queen performance"),
        ("Fall (Sep &ndash; Nov)",
         "Prepare for winter. Ensure colonies have 50-60 lbs of honey stores. "
         "Treat for varroa mites after harvesting honey. Combine weak colonies "
         "with stronger ones. Install entrance reducers. Check for adequate "
         "bee numbers &mdash; a winter cluster needs at least a full deep box of "
         "bees. Feed syrup (2:1) if stores are light.",
         "Monitor: Honey stores, mite levels, colony strength, winter weight, mouse guards"),
        ("Winter (Dec &ndash; Feb)",
         "Do not open hives unless temperature is above 50&deg;F. Heft hives by "
         "tilting the back to gauge honey stores &mdash; heavy is good. Check "
         "entrances are clear of dead bees and snow. Ensure ventilation to prevent "
         "condensation. Order new packages and queens for spring delivery. Read, "
         "plan, and maintain equipment for the coming season.",
         "Monitor: Hive weight, entrance clearance, wind damage, food emergency stores"),
    ]

    rows = ""
    for season, desc, monitor in seasons:
        rows += f'''
      <div style="border: 1px solid #D8E0D0; border-radius: 4px; padding: 8px 10px; margin-bottom: 6px; background: #FCFBF8;">
        <div style="font-size: 9.5pt; font-weight: 700; color: #5A7042; margin-bottom: 4px;">{season}</div>
        <div style="font-size: 7.5pt; color: #555; line-height: 1.5; margin-bottom: 4px;">{desc}</div>
        <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.3pt;">Key Monitoring</div>
        <div style="font-size: 7.5pt; color: #888; font-style: italic;">{monitor}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Seasonal Calendar -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Seasonal Calendar</span>
  </div>

  <div class="page-title">Seasonal Beekeeping Calendar</div>
  <div class="page-subtitle">What to do and when &mdash; timing is everything</div>

  {rows}

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
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


def beekeeping_log_left(session_num):
    """Left page of two-page hive inspection spread — colony details"""
    return f'''
<!-- Page {pn()}: Inspection {session_num} Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Inspection #{session_num:02d}</span>
    <span class="sh-right">Beekeeping Log Book</span>
  </div>

  <div class="page-title">Inspection #{session_num:02d}</div>
  <div class="page-subtitle">Colony Details &amp; Conditions</div>

  <!-- Date/Time/Weather -->
  <div style="background: #FAF8F2; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 30px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 30px;">Time</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 40px;">Temp</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 40px;">Weather</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 36px;">Wind</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 44px;">Forage</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Hive ID -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 6px;">
    <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 52px;">Hive ID</span>
    <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 16px;"></div>
  </div>
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 52px;">Apiary</span>
    <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 16px;"></div>
  </div>

  <!-- Colony Status -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Colony Status</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Queen Seen</span>
    <span class="check-item"><span class="check-box"></span> Eggs Present</span>
    <span class="check-item"><span class="check-box"></span> Larvae</span>
    <span class="check-item"><span class="check-box"></span> Capped Brood</span>
    <span class="check-item"><span class="check-box"></span> Swarm Cells</span>
    <span class="check-item"><span class="check-box"></span> Queen Cells</span>
    <span class="check-item"><span class="check-box"></span> Drones Seen</span>
  </div>

  <!-- Temperament & Strength -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 54px;">Temper</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Colony Details Grid -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Inspection Details</div>
  <div style="background: #FCFBF8; border: 1px solid #E0E0E0; border-radius: 4px; padding: 8px 10px; margin-bottom: 8px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 38px;">Brood</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 38px;">Frames</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 38px;">Honey</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 38px;">Pollen</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 38px;">Boxes</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 38px;">Mites</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 38px;">Feed?</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Actions Taken -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Actions Taken</div>
  <div class="check-row" style="margin-bottom: 6px;">
    <span class="check-item"><span class="check-box"></span> Added Super</span>
    <span class="check-item"><span class="check-box"></span> Removed Super</span>
    <span class="check-item"><span class="check-box"></span> Fed Syrup</span>
    <span class="check-item"><span class="check-box"></span> Requeened</span>
    <span class="check-item"><span class="check-box"></span> Split</span>
    <span class="check-item"><span class="check-box"></span> Treated Mites</span>
    <span class="check-item"><span class="check-box"></span> Combined</span>
    <span class="check-item"><span class="check-box"></span> Harvested</span>
  </div>

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''



def beekeeping_log_right(session_num):
    """Right page of two-page hive inspection spread — notes & assessment"""
    return f'''
<!-- Page {pn()}: Inspection {session_num} Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Inspection #{session_num:02d} &mdash; Notes</span>
    <span class="sh-right">Beekeeping Log Book</span>
  </div>

  <!-- Hive Health Assessment -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Health &amp; Concerns</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Healthy</span>
    <span class="check-item"><span class="check-box"></span> Queenless</span>
    <span class="check-item"><span class="check-box"></span> Laying Workers</span>
    <span class="check-item"><span class="check-box"></span> Varroa Seen</span>
    <span class="check-item"><span class="check-box"></span> SHB Seen</span>
    <span class="check-item"><span class="check-box"></span> Wax Moth</span>
    <span class="check-item"><span class="check-box"></span> Chilled Brood</span>
    <span class="check-item"><span class="check-box"></span> Deformed Wing</span>
  </div>

  <!-- Nectar Flow -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 6px;">
    <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 60px;">Nectar Flow</span>
    <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 16px;"></div>
  </div>
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 60px;">Bloom Seen</span>
    <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 16px;"></div>
  </div>

  <!-- Inspection Rating -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 3px;">Overall Colony Rating</div>
  <div style="font-size: 20pt; color: #C4A04A; letter-spacing: 6pt; margin-bottom: 8px;">&#9734; &#9734; &#9734; &#9734; &#9734;</div>

  <!-- Flags -->
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Needs Attention</span>
    <span class="check-item"><span class="check-box"></span> Reinspect Soon</span>
    <span class="check-item"><span class="check-box"></span> Ready to Harvest</span>
    <span class="check-item"><span class="check-box"></span> Swarm Risk</span>
  </div>

  <!-- Observations -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 3px;">Observations &amp; Notes</div>
  <div style="border: 0.5px solid #ccc; border-radius: 3px; padding: 6px 8px; margin-bottom: 8px;">
    <div style="border-bottom: 0.5px solid #ddd; height: 16px; margin-bottom: 2px;"></div>
    <div style="border-bottom: 0.5px solid #ddd; height: 16px; margin-bottom: 2px;"></div>
    <div style="border-bottom: 0.5px solid #ddd; height: 16px; margin-bottom: 2px;"></div>
    <div style="border-bottom: 0.5px solid #ddd; height: 16px; margin-bottom: 2px;"></div>
    <div style="border-bottom: 0.5px solid #ddd; height: 16px; margin-bottom: 2px;"></div>
    <div style="border-bottom: 0.5px solid #ddd; height: 16px; margin-bottom: 2px;"></div>
    <div style="height: 16px;"></div>
  </div>

  <!-- Next Steps -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 3px;">Next Steps / To Do</div>
  <div style="border: 0.5px solid #ccc; border-radius: 3px; padding: 6px 8px; margin-bottom: 8px;">
    <div style="border-bottom: 0.5px solid #ddd; height: 16px; margin-bottom: 2px;"></div>
    <div style="border-bottom: 0.5px solid #ddd; height: 16px; margin-bottom: 2px;"></div>
    <div style="border-bottom: 0.5px solid #ddd; height: 16px; margin-bottom: 2px;"></div>
    <div style="height: 16px;"></div>
  </div>

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''



def species_checklist(page_of, total_pages):
    """Nectar and pollen plant checklist — what your bees forage"""
    all_plants = [
        # Page 1: Trees and early bloomers
        "Red Maple (Acer rubrum)", "Silver Maple (Acer saccharinum)",
        "Black Locust (Robinia pseudoacacia)", "Tulip Poplar (Liriodendron)",
        "Black Tupelo / Tupelo Gum", "American Linden / Basswood",
        "Sourwood (Oxydendrum)", "Willow (Salix spp.)",
        "Apple / Crabapple (Malus)", "Blackberry / Raspberry (Rubus)",
        "Clethra / Sweet Pepperbush", "Sumac (Rhus spp.)",
        # Page 2: Herbs, flowers, crops
        "White Clover (Trifolium repens)", "Crimson Clover (Trifolium incarnatum)",
        "Alsike Clover", "Sweet Clover (Melilotus)",
        "Vetch (Vicia spp.)", "Birds-foot Trefoil",
        "Goldenrod (Solidago)", "Aster (Symphyotrichum)",
        "Buckwheat (Fagopyrum)", "Sage (Salvia spp.)",
        "Lavender (Lavandula)", "Rosemary (Rosmarinus)",
        # Page 3: Blanks for user's local forage
    ]

    per_page = 12
    start = (page_of - 1) * per_page
    page_plants = all_plants[start:start + per_page]
    while len(page_plants) < per_page:
        page_plants.append("")

    rows = ""
    start_num = start + 1
    for i, plant in enumerate(page_plants):
        n = start_num + i
        if plant:
            rows += f'''
      <tr><td class="num-col">{n}</td>
          <td style="font-style:italic; font-size:7.5pt; color:#555;">{plant}</td>
          <td></td><td></td>
          <td class="check-col"><span class="check-circle"></span></td></tr>'''
        else:
            rows += f'''
      <tr><td class="num-col">{n}</td>
          <td></td><td></td><td></td>
          <td class="check-col"><span class="check-circle"></span></td></tr>'''

    page_title = "Nectar &amp; Pollen Plant Checklist"
    page_sub = f"Page {page_of} of {total_pages} &mdash; "

    return f'''
<!-- Page {pn()}: Plant Checklist {page_of} -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Forage Checklist</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">{page_title}</div>
  <div class="page-subtitle">Track which plants your bees visit throughout the year</div>

  <table class="data-table">
    <tr>
      <th style="width: 24px;">#</th>
      <th>Plant Name</th>
      <th style="width: 1in;">Bloom Date</th>
      <th style="width: 0.8in;">Rating</th>
      <th style="width: 24px;">&check;</th>
    </tr>
    {rows}
  </table>

  <div style="font-size: 6.5pt; color: #999; margin-top: 4px;">
    Track bloom dates to anticipate nectar flows and plan your honey harvest timing.
  </div>

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''



def location_log(page_of, total_pages):
    """Apiary location and hive inventory log"""
    rows = ""
    for i in range(1, 13):
        n = (page_of - 1) * 12 + i
        rows += f'''
      <tr><td class="num-col">{n}</td>
          <td></td><td></td><td></td><td></td></tr>'''

    return f'''
<!-- Page {pn()}: Hive Inventory {page_of} -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Hive Inventory</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Hive &amp; Apiary Inventory</div>
  <div class="page-subtitle">Track your colonies, locations, and equipment</div>

  <table class="data-table">
    <tr>
      <th style="width: 24px;">#</th>
      <th>Hive ID / Name</th>
      <th style="width: 1in;">Location</th>
      <th style="width: 0.8in;">Type</th>
      <th style="width: 0.8in;">Notes</th>
    </tr>
    {rows}
  </table>

  <div style="font-size: 6.5pt; color: #999; margin-top: 4px;">
    Type: Langstroth, Top Bar, Warre, Nuc, etc.
  </div>

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''



def equipment_kit():
    """Beekeeping equipment and tools inventory"""
    sections = [
        ("Hive Components", [
            "Deep brood boxes (10-frame or 8-frame)",
            "Medium or shallow supers",
            "Bottom boards (solid or screened)",
            "Inner covers and telescoping outer covers",
            "Frames with foundation (wax or plastic)",
            "Queen excluders",
        ]),
        ("Tools & Gear", [
            "Smoker and fuel (pine needles, burlap, pellets)",
            "Hive tool (standard or J-hook)",
            "Frame grip / frame lifter",
            "Bee brush",
            "Entrance reducers",
            "Queen marking kit",
        ]),
        ("Protective Wear", [
            "Full bee suit or jacket with veil",
            "Goat-skin or nitrile beekeeping gloves",
            "High-top boots (duct-tape ankles)",
        ]),
        ("Feeding & Health", [
            "Boardman or top feeder",
            "Sugar syrup (1:1 spring, 2:1 fall)",
            "Pollen substitute patties",
            "Varroa mite treatment (per local recommendations)",
            "Fume board for honey removal",
        ]),
        ("Harvest Equipment", [
            "Honey extractor (radial or tangential)",
            "Uncapping knife or fork",
            "Strainer / filter bags",
            "Food-grade buckets with gate valves",
            "Jars and labels",
        ]),
    ]

    rows = ""
    for section_name, items in sections:
        item_rows = ""
        for item in items:
            item_rows += f'''
        <div style="display: flex; align-items: center; gap: 5px; margin-bottom: 2px;">
          <span style="width: 10px; height: 10px; border: 1px solid #aaa; border-radius: 2px; display: inline-block;"></span>
          <span style="font-size: 7.5pt; color: #555;">{item}</span>
          <div style="flex:1; border-bottom: 0.5px dotted #ccc; height: 12px; margin-left: 4px;"></div>
        </div>'''
        rows += f'''
      <div style="border: 1px solid #D8E0D0; border-radius: 4px; padding: 6px 8px; margin-bottom: 5px; background: #FCFBF8;">
        <div style="font-size: 8.5pt; font-weight: 700; color: #141A12; margin-bottom: 4px;">{section_name}</div>
        {item_rows}
      </div>'''

    return f'''
<!-- Page {pn()}: Equipment -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Equipment Checklist</span>
  </div>

  <div class="page-title">Beekeeping Equipment Checklist</div>
  <div class="page-subtitle">What you need for each season</div>

  {rows}

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''



def beekeeping_favorites():
    """Honey harvest log and year-in-review summary"""
    return f'''
<!-- Page {pn()}: Honey Harvest & Year Summary -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Summary</span>
    <span class="sh-right">Honey Harvest Log</span>
  </div>

  <div class="page-title">Honey Harvest &amp; Year Summary</div>
  <div class="page-subtitle">Track your season\'s bounty</div>

  <!-- Stat Cards -->
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 8px; margin-bottom: 12px;">
    <div style="background: #FAF8F2; border: 1px solid #E0D8C0; border-radius: 5px; padding: 10px 8px; text-align: center;">
      <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.3pt;">Total Honey</div>
      <div style="font-size: 18pt; font-weight: 700; color: #141A12; margin: 4px 0;">___ lbs</div>
    </div>
    <div style="background: #FAF8F2; border: 1px solid #E0D8C0; border-radius: 5px; padding: 10px 8px; text-align: center;">
      <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.3pt;">Hives</div>
      <div style="font-size: 18pt; font-weight: 700; color: #141A12; margin: 4px 0;">___</div>
    </div>
    <div style="background: #FAF8F2; border: 1px solid #E0D8C0; border-radius: 5px; padding: 10px 8px; text-align: center;">
      <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.3pt;">Inspections</div>
      <div style="font-size: 18pt; font-weight: 700; color: #141A12; margin: 4px 0;">___</div>
    </div>
    <div style="background: #FAF8F2; border: 1px solid #E0D8C0; border-radius: 5px; padding: 10px 8px; text-align: center;">
      <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.3pt;">Swarms</div>
      <div style="font-size: 18pt; font-weight: 700; color: #141A12; margin: 4px 0;">___</div>
    </div>
  </div>

  <!-- Harvest Log -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Harvest Log</div>
  <table class="data-table">
    <tr>
      <th style="width: 24px;">#</th>
      <th>Date</th>
      <th>Hive ID</th>
      <th>Weight</th>
      <th>Notes</th>
    </tr>
    <tr><td class="num-col">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td class="num-col">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td class="num-col">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td class="num-col">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td class="num-col">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td class="num-col">6</td><td></td><td></td><td></td><td></td></tr>
    <tr><td class="num-col">7</td><td></td><td></td><td></td><td></td></tr>
    <tr><td class="num-col">8</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <!-- Year Reflection -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 3px;">Best Decisions This Year</div>
  <div style="border: 0.5px solid #ccc; border-radius: 3px; padding: 4px 8px; margin-bottom: 6px;">
    <div style="border-bottom: 0.5px solid #ddd; height: 14px; margin-bottom: 2px;"></div>
    <div style="border-bottom: 0.5px solid #ddd; height: 14px; margin-bottom: 2px;"></div>
    <div style="height: 14px;"></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 3px;">Lessons Learned &amp; Goals for Next Year</div>
  <div style="border: 0.5px solid #ccc; border-radius: 3px; padding: 4px 8px;">
    <div style="border-bottom: 0.5px solid #ddd; height: 14px; margin-bottom: 2px;"></div>
    <div style="border-bottom: 0.5px solid #ddd; height: 14px; margin-bottom: 2px;"></div>
    <div style="border-bottom: 0.5px solid #ddd; height: 14px; margin-bottom: 2px;"></div>
    <div style="height: 14px;"></div>
  </div>

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
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

  <div class="page-title">Beekeeping Notes</div>
  <div class="page-subtitle">Species to research, recipes, and reminders</div>

  {lines}

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def sketch_page():
    """Dot grid page for sketching colonies and location maps"""
    return f'''
<!-- Page {pn()}: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Sketch Pad</span>
    <span class="sh-right">Specimen Drawings &amp; Spot Maps</span>
  </div>

  <div class="page-title">Sketch Pad</div>
  <div class="page-subtitle">Draw colonies, map locations, plan forays</div>

  <div class="dot-grid" style="width: 100%; height: 6.5in; border-radius: 4px;"></div>

  <div class="page-footer">
    <span>Beekeeping Log Book</span>
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
    pages.append(colony_anatomy())               # 4: Colony anatomy
    pages.append(habitat_guide())                  # 5: Habitat guide
    pages.append(beekeeping_safety())                # 6: Beekeeping safety
    pages.append(seasonal_calendar())              # 7: Seasonal calendar

    # ---- Section 1: Beekeeping Logs ----
    pages.append(divider_section(1, "One", "Hive Inspection Logs", "40 inspections &mdash; your beekeeping journey"))
    NUM_SESSIONS = 40
    for i in range(1, NUM_SESSIONS + 1):
        pages.append(beekeeping_log_left(i))          # Left page: details
        pages.append(beekeeping_log_right(i))         # Right page: notes

    # ---- Section 2: Species Checklist ----
    pages.append(divider_section(2, "Two", "Forage Checklist", "Track nectar &amp; pollen plants"))
    pages.append(species_checklist(1, 3))
    pages.append(species_checklist(2, 3))
    pages.append(species_checklist(3, 3))

    # ---- Section 3: Spot & Location Log ----
    pages.append(divider_section(3, "Three", "Hive &amp; Apiary Inventory", "Track your colonies and locations"))
    pages.append(location_log(1, 3))
    pages.append(location_log(2, 3))
    pages.append(location_log(3, 3))

    # ---- Section 4: Equipment & Kit ----
    pages.append(divider_section(4, "Four", "Equipment Checklist", "What you need for each season"))
    pages.append(equipment_kit())

    # ---- Section 5: Seasonal Favorites ----
    pages.append(divider_section(5, "Five", "Harvest &amp; Year Summary", "Track your honey harvest and reflect"))
    pages.append(beekeeping_favorites())
    pages.append(sketch_page())

    # ---- Section 6: Notes ----
    pages.append(divider_section(6, "Six", "Notes", "Observations, plans, and reminders"))
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
    print(f"  Reference (how-to, anatomy, habitat, safety, seasonal): 5")
    print(f"  Section dividers: 6")
    print(f"  Beekeeping logs ({NUM_SESSIONS} sessions x 2 pages): {NUM_SESSIONS * 2}")
    print(f"  Species checklist: 2")
    print(f"  Location log: 2")
    print(f"  Equipment & kit: 1")
    print(f"  Favorites summary: 1")
    print(f"  Sketch page: 1")
    print(f"  Notes pages: 10")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
