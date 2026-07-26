#!/usr/bin/env python3
"""
Bonsai Tree Care Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Bonsai enthusiasts, from beginner to advanced
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "bonsai_tree_care_journal_us_V1.0.html")

BOOK_TITLE = "Bonsai Tree Care Journal"
BOOK_SUBTITLE = "Nurture Every Tree, Track Every Season"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

# ============================================================
# CSS (raw string — never f-string)
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

/* Colors:
   Charcoal: #161616, #1E1E1E
   Moss green: #4A6B3E, #5A7A4A, #7A9A6A
   Terracotta: #B5704A, #C8825A
   Gold: #C4A04A
   Cream: #FAF8F4
*/

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
  background: linear-gradient(165deg, #161616 0%, #1E1E1E 30%, #161616 65%, #100F0F 100%);
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #5A7A4A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #B5704A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #5A7A4A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #7A9A6A, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #B5704A, transparent);
}

/* ===== Bonsai SVG ===== */
.cover .bonsai-wrap {
  width: 120px; height: 170px;
  position: relative;
  margin: 0 auto 18px;
}

/* Bonsai trunk */
.cover .trunk-base {
  width: 14px; height: 50px;
  position: absolute;
  top: 85px; left: 53px;
  background: linear-gradient(170deg,
    rgba(107,68,35,0.22),
    rgba(80,50,25,0.15));
  border: 1px solid rgba(107,68,35,0.30);
  border-radius: 3px 3px 0 0;
  transform: rotate(-3deg);
}

/* Trunk curve */
.cover .trunk-curve {
  width: 10px; height: 40px;
  position: absolute;
  top: 50px; left: 55px;
  background: linear-gradient(170deg,
    rgba(107,68,35,0.18),
    rgba(80,50,25,0.10));
  border: 1px solid rgba(107,68,35,0.25);
  border-radius: 2px;
  transform: rotate(5deg);
}

/* Foliage pads (clouds) */
.cover .pad-1 {
  width: 45px; height: 22px;
  position: absolute;
  top: 30px; left: 18px;
  background: radial-gradient(ellipse,
    rgba(90,122,74,0.22) 0%,
    rgba(74,107,62,0.12) 60%,
    transparent 100%);
  border-radius: 50%;
}
.cover .pad-2 {
  width: 55px; height: 26px;
  position: absolute;
  top: 15px; left: 32px;
  background: radial-gradient(ellipse,
    rgba(90,122,74,0.25) 0%,
    rgba(74,107,62,0.15) 60%,
    transparent 100%);
  border-radius: 50%;
}
.cover .pad-3 {
  width: 40px; height: 20px;
  position: absolute;
  top: 40px; left: 60px;
  background: radial-gradient(ellipse,
    rgba(90,122,74,0.20) 0%,
    rgba(74,107,62,0.10) 60%,
    transparent 100%);
  border-radius: 50%;
}
.cover .pad-4 {
  width: 35px; height: 18px;
  position: absolute;
  top: 55px; left: 5px;
  background: radial-gradient(ellipse,
    rgba(90,122,74,0.18) 0%,
    rgba(74,107,62,0.08) 60%,
    transparent 100%);
  border-radius: 50%;
}

/* Pot */
.cover .pot-rim {
  width: 80px; height: 5px;
  position: absolute;
  top: 130px; left: 20px;
  background: rgba(181,112,74,0.25);
  border: 1px solid rgba(181,112,74,0.35);
  border-radius: 2px;
}
.cover .pot-body {
  width: 70px; height: 28px;
  position: absolute;
  top: 135px; left: 25px;
  background: linear-gradient(180deg,
    rgba(181,112,74,0.22),
    rgba(150,90,60,0.15));
  border: 1px solid rgba(181,112,74,0.30);
  border-radius: 0 0 3px 3px;
}

/* Soil line */
.cover .soil-line {
  width: 70px; height: 3px;
  position: absolute;
  top: 130px; left: 25px;
  background: rgba(60,40,20,0.20);
  border-radius: 1px;
}

/* Sparkle accents */
.cover .sparkle1 {
  width: 4px; height: 4px;
  background: rgba(196,160,74,0.4);
  border-radius: 50%;
  position: absolute;
  top: 25px; left: 10px;
  box-shadow: 0 0 4px rgba(196,160,74,0.3);
}
.cover .sparkle2 {
  width: 3px; height: 3px;
  background: rgba(250,248,244,0.3);
  border-radius: 50%;
  position: absolute;
  top: 60px; left: 100px;
  box-shadow: 0 0 3px rgba(250,248,244,0.2);
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 24pt;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.15;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 6px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 110px; height: 2.5px;
  background: #5A7A4A;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 11pt;
  color: #7A9A6A;
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
  border: 1px solid rgba(90,122,74,0.45);
  color: #7A9A6A;
  font-size: 7pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 9px;
  border-radius: 3px;
  text-transform: uppercase;
}

.cover .tagline {
  font-size: 8.5pt;
  color: #B5704A;
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #5A7A4A, transparent),
    radial-gradient(ellipse 25px 15px at 80% 30%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #B5704A, transparent),
    radial-gradient(ellipse 18px 11px at 25% 85%, #5A7A4A, transparent);
}

.divider .div-num {
  font-size: 60pt;
  color: rgba(90,122,74,0.12);
  font-weight: 700;
  position: absolute;
  top: 1in;
}

.divider .div-label {
  font-size: 10pt;
  color: #5A7A4A;
  letter-spacing: 3pt;
  text-transform: uppercase;
  margin-bottom: 10px;
  position: relative;
}

.divider .div-title {
  font-size: 22pt;
  color: #ffffff;
  font-weight: 700;
  line-height: 1.2;
  position: relative;
  padding: 0 0.6in;
}

.divider .div-sub {
  font-size: 11pt;
  color: #7A9A6A;
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
  border-bottom: 1.5px solid #5A7A4A;
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

table.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
}
table.data-table th {
  background: #5A7A4A;
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
  background: #FAF8F4;
}

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

.stars {
  font-size: 13pt;
  color: #ccc;
  letter-spacing: 2pt;
}

.info-box {
  background: #FAF8F4;
  border-left: 3px solid #5A7A4A;
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
  border: 1.5px solid #5A7A4A;
  border-radius: 50%;
  display: inline-block;
}

.prop-card {
  border: 1px solid #D0DDC8;
  border-radius: 4px;
  padding: 6px 8px;
  margin-bottom: 5px;
  background: #FCFAF7;
}
.prop-card-label {
  font-size: 7pt;
  font-weight: 700;
  color: #5A7A4A;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 3px;
}
.prop-card-value {
  font-size: 7.5pt;
  color: #888;
  line-height: 1.5;
}

.stat-card {
  text-align: center;
  padding: 6px 4px;
  background: #FAF8F4;
  border-radius: 4px;
  border: 1px solid #D0DDC8;
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
  color: #5A7A4A;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 4px;
}

.dot-grid {
  background-image: radial-gradient(circle, #d0d0d0 1px, transparent 1px);
  background-size: 0.20in 0.20in;
  background-position: 0.10in 0.10in;
}

/* Season color strip */
.season-strip {
  display: flex;
  height: 16px;
  border-radius: 3px;
  overflow: hidden;
  margin-bottom: 4px;
}
.season-cell {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 5.5pt;
  font-weight: 700;
  color: white;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
}
"""

# ============================================================
# PAGE BUILDERS
# ============================================================

def cover():
    pg = pn()
    return """<!-- PAGE %d: Cover -->
<div class="cover">
  <div class="glow-bg"></div>
  <div class="bonsai-wrap">
    <div class="sparkle1"></div>
    <div class="sparkle2"></div>
    <div class="pad-4"></div>
    <div class="pad-1"></div>
    <div class="pad-3"></div>
    <div class="pad-2"></div>
    <div class="trunk-curve"></div>
    <div class="trunk-base"></div>
    <div class="soil-line"></div>
    <div class="pot-rim"></div>
    <div class="pot-body"></div>
  </div>
  <div class="title-block">
    <div class="main-title">%s</div>
    <div class="accent-bar"></div>
    <div class="subtitle">%s</div>
    <div class="features">
      <span class="feature-badge">40 Tree Logs</span>
      <span class="feature-badge">Pruning Calendar</span>
      <span class="feature-badge">Season Care</span>
      <span class="feature-badge">Growth Tracking</span>
    </div>
    <div class="tagline">For Bonsai Enthusiasts &amp; Tree Keepers</div>
  </div>
  <div class="publisher">More Shine Press</div>
</div>
""" % (pg, BOOK_TITLE, BOOK_SUBTITLE)


def owner_page():
    pg = pn()
    return """<!-- PAGE %d: Owner -->
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
      <div style="font-size: 8pt; font-weight: 700; color: #5A7A4A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Years Growing Bonsai</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #5A7A4A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Number of Trees</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #5A7A4A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Species</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #5A7A4A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Growing Zone</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def how_to_use():
    pg = pn()
    return """<!-- PAGE %d: How to Use -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Getting Started</span>
    <span class="sh-right">More Shine Press</span>
  </div>

  <div class="page-title">How to Use This Journal</div>
  <div class="page-subtitle">The art of patient cultivation, one record at a time</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Bonsai Journal?</div>
    Bonsai is a relationship measured in decades, not days. A journal captures the slow unfolding of each tree's story &mdash; when you pruned, how it responded, what the weather did, and how your skills grew alongside your collection. Without records, years of learning fade. With them, every tree becomes a teacher.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Guidelines</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Log on the same day.</strong> Record work immediately after performing it. Details like soil moisture level, exact branch angles, and fertilizer ratios fade quickly from memory.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Photograph before and after.</strong> A photo from the same angle each season reveals growth that is invisible day to day. Note the photo date in your journal entry.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Track the seasons.</strong> Bonsai care follows nature's calendar. Record when buds break, when fall color peaks, and when your tree goes dormant. Patterns emerge over the years.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Note your mistakes honestly.</strong> A dead tree teaches more than a healthy one. Record what went wrong &mdash; overwatering, wrong soil, late pruning &mdash; so you never repeat it.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Plan before you cut.</strong> Sketch the tree and draw your intended design before pruning. Every cut is permanent. A drawing helps you see the future silhouette.
    </div>
  </div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def species_reference():
    pg = pn()
    return """<!-- PAGE %d: Species Reference -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Common Bonsai Species</span>
  </div>

  <div class="page-title">Common Bonsai Species</div>
  <div class="page-subtitle">Popular species with care characteristics</div>

  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th>Species</th>
      <th style="width:28px;">Type</th>
      <th style="width:32px;">Light</th>
      <th style="width:28px;">Water</th>
      <th style="width:40px;">Hardiness</th>
      <th>Key Notes</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Juniper</td>
      <td>Evergreen</td>
      <td>Full Sun</td>
      <td>Med</td>
      <td>Hardy</td>
      <td>Outdoor. Pinch growth, do not cut. Needs winter dormancy.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Chinese Elm</td>
      <td>Semi-Dec.</td>
      <td>Full Sun</td>
      <td>Med-High</td>
      <td>Hardy</td>
      <td>Great for beginners. Forgiving of mistakes. Indoor or outdoor.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Ficus (Retusa)</td>
      <td>Tropical</td>
      <td>Bright</td>
      <td>High</td>
      <td>Tender</td>
      <td>Indoor. Loves humidity. Aerial roots. Cannot freeze.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Japanese Maple</td>
      <td>Deciduous</td>
      <td>Part Sun</td>
      <td>Med</td>
      <td>Hardy</td>
      <td>Protect from hot afternoon sun. Stunning fall color.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Pine (Black/White)</td>
      <td>Evergreen</td>
      <td>Full Sun</td>
      <td>Low-Med</td>
      <td>Hardy</td>
      <td>Candle pruning in spring. Needs cold winter dormancy.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Azalea (Satsuki)</td>
      <td>Flowering</td>
      <td>Part Sun</td>
      <td>High</td>
      <td>Semi-Hardy</td>
      <td>Acidic soil. Stunning blooms. Prune after flowering.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Jade (Portulacaria)</td>
      <td>Succulent</td>
      <td>Bright</td>
      <td>Low</td>
      <td>Tender</td>
      <td>Indoor. Drought tolerant. Easy for beginners. Thick trunk.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Trident Maple</td>
      <td>Deciduous</td>
      <td>Full Sun</td>
      <td>Med</td>
      <td>Hardy</td>
      <td>Excellent nebari (root flare). Fast growing. Good for forests.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Bougainvillea</td>
      <td>Tropical</td>
      <td>Full Sun</td>
      <td>Low-Med</td>
      <td>Tender</td>
      <td>Vibrant blooms. Thick trunks. Loves heat. Protect below 40&deg;F.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Cypress (Bald)</td>
      <td>Deciduous</td>
      <td>Full Sun</td>
      <td>High</td>
      <td>Hardy</td>
      <td>Loves water. Great for swamp styles. Feathery foliage.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Boxwood</td>
      <td>Evergreen</td>
      <td>Part-Full</td>
      <td>Med</td>
      <td>Hardy</td>
      <td>Dense foliage. Great for clip-and-grow. Forgiving.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Wisteria</td>
      <td>Deciduous</td>
      <td>Full Sun</td>
      <td>High</td>
      <td>Hardy</td>
      <td>Cascading flower racemes. Needs strong root system. Heavy feeder.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Serissa</td>
      <td>Evergreen</td>
      <td>Bright</td>
      <td>Med</td>
      <td>Semi-Hardy</td>
      <td>"Tree of a Thousand Stars." Tiny white flowers. Sensitive to changes.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Olive</td>
      <td>Evergreen</td>
      <td>Full Sun</td>
      <td>Low-Med</td>
      <td>Semi-Tender</td>
      <td>Drought tolerant. Beautiful bark. Hardy in Mediterranean climates.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Zelkova</td>
      <td>Deciduous</td>
      <td>Full Sun</td>
      <td>Med</td>
      <td>Hardy</td>
      <td>Classic broom style. Fine twigging. Golden fall color.</td>
    </tr>
  </table>

  <div style="margin-top: 6px; padding: 5px 8px; background: #F5F8F0; border-radius: 3px; font-size: 6.5pt; color: #777; font-style: italic;">
    Type: Evergreen retains foliage. Deciduous loses all leaves. Semi-Dec. partially retains. Tropical needs indoor protection. | Light: Full Sun = 6+ hrs direct. Part Sun = 4-6 hrs. Bright = bright indirect. | Hardiness: Hardy = freezing OK. Semi-Hardy = light frost only. Tender = protect below 40&deg;F.
  </div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def pruning_calendar():
    pg = pn()
    return """<!-- PAGE %d: Pruning Calendar -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Seasonal Pruning Calendar</span>
  </div>

  <div class="page-title">Seasonal Pruning Calendar</div>
  <div class="page-subtitle">When to prune, wire, and work on each species</div>

  <div class="season-strip">
    <div class="season-cell" style="background: #4A8B4A;">Spring</div>
    <div class="season-cell" style="background: #D4AC0D;">Summer</div>
    <div class="season-cell" style="background: #B5704A;">Fall</div>
    <div class="season-cell" style="background: #6B7A8A;">Winter</div>
  </div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:50px;">Season</th>
      <th>Deciduous</th>
      <th>Evergreen (Juniper/Pine)</th>
      <th>Tropical</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#4A8B4A;">Spring</td>
      <td>Best time for structural pruning. Prune before buds open. Repot when buds swell. Wire new growth.</td>
      <td>Pine: candle pruning. Juniper: pinch new growth. Major styling OK. Repot late spring.</td>
      <td>Active growth. Prune and wire freely. Repot as new growth starts.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#D4AC0D;">Summer</td>
      <td>Defoliation (maples). Pinch new growth. Light pruning only. Do not wire heavily in heat.</td>
      <td>Pinch and trim. Wire branches. Avoid heavy pruning. Water vigilantly.</td>
      <td>Peak growth season. Heavy pruning OK. Fertilize regularly. Watch for pests.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#B5704A;">Fall</td>
      <td>Light pruning only. Remove dead growth. No wiring &mdash; branches are brittle. Apply wire to refine only.</td>
      <td>Light maintenance pruning. Good time for jin/shari work. Stop fertilizing.</td>
      <td>Bring indoors before nights drop below 50&deg;F. Reduce watering. Stop pruning.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#6B7A8A;">Winter</td>
      <td>Dormant. Structural pruning of bare branches. Major pruning cuts heal slow but safe. Protect from frost.</td>
      <td>Dormant period. Minimal work. Protect from freezing winds. Do not prune.</td>
      <td>Indoor care. Grow lights may be needed. Reduce water. No pruning or repotting.</td>
    </tr>
  </table>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Golden Rules of Pruning</div>
    <div style="font-size: 8pt; line-height: 1.6; color: #444;">
      <div style="margin-bottom: 5px;"><strong>1.</strong> Prune to enhance the tree's natural character, not to force an unnatural shape.</div>
      <div style="margin-bottom: 5px;"><strong>2.</strong> Never remove more than 1/3 of foliage in a single session.</div>
      <div style="margin-bottom: 5px;"><strong>3.</strong> Always cut to a node or branch collar. Flush cuts leave wounds.</div>
      <div style="margin-bottom: 5px;"><strong>4.</strong> Use sharp, clean tools. Disinfect between trees.</div>
      <div style="margin-bottom: 5px;"><strong>5.</strong> Seal large cuts with cut paste on deciduous trees to prevent dieback.</div>
    </div>
  </div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def watering_guide():
    pg = pn()
    return """<!-- PAGE %d: Watering Guide -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Watering Fundamentals</span>
  </div>

  <div class="page-title">Watering Guide</div>
  <div class="page-subtitle">The most critical skill in bonsai</div>

  <div class="info-box">
    <div class="info-title">The Golden Rule</div>
    Water when the soil surface begins to feel dry &mdash; not on a fixed schedule. Soil, weather, species, pot size, and season all change how fast water is used. Learn to read each tree individually.
  </div>

  <div style="font-size: 8pt; line-height: 1.6; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 9.5pt; margin-bottom: 6px;">How to Water Properly</div>
    <div style="margin-bottom: 8px;">
      <strong>1. Check before watering.</strong> Push your finger 1/2 inch into the soil. If it feels moist, wait. If it feels dry, water thoroughly. The surface can look dry while the root ball is still wet.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>2. Water twice.</strong> Water the entire surface until water runs from the drainage holes. Wait a minute, then water again. The first pass moistens the surface; the second penetrates the root ball.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>3. Use a fine rose.</strong> A watering can with a fine rose attachment prevents soil erosion and ensures even distribution. Never blast the soil with a hose nozzle.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>4. Morning is best.</strong> Water in early morning so excess moisture evaporates during the day. Evening watering can promote fungal problems. Avoid midday watering in summer (hot roots).
    </div>
  </div>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Signs of Trouble</div>
    <table class="data-table" style="font-size: 7.5pt;">
      <tr><th style="width:90px;">Symptom</th><th>Likely Cause</th><th>Action</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Yellow leaves falling</td><td>Overwatering &mdash; roots suffocating</td><td>Check drainage. Reduce watering frequency.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Crisp brown edges</td><td>Underwatering or wind burn</td><td>Water more frequently. Add humidity tray.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Wilted but soil wet</td><td>Root rot from chronic overwatering</td><td>Repot. Trim dead roots. Fresh soil.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Sudden leaf drop</td><td>Shock: temperature, location, or watering change</td><td>Stabilize conditions. Do not fertilize.</td></tr>
    </table>
  </div>

  <div style="margin-top: 10px; padding: 6px 10px; background: #FFF8E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 7.5pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Remember:</strong> There is no watering schedule that works every day. A tree may need water twice a day in summer heat and once a week in winter. Always check the soil.
  </div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def soil_reference():
    pg = pn()
    return """<!-- PAGE %d: Soil Reference -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Soil &amp; Repotting</span>
  </div>

  <div class="page-title">Soil Mixtures &amp; Repotting</div>
  <div class="page-subtitle">The foundation of tree health</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th>Component</th>
      <th style="width:60px;">Function</th>
      <th>Notes</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Akadama</td>
      <td>Moisture retention</td>
      <td>Japanese clay. Breaks down over 1-2 years, signaling repot time. Gold standard.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Pumice</td>
      <td>Drainage / aeration</td>
      <td>Light volcanic rock. Holds some water and air. Essential component.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Lava Rock (Scoria)</td>
      <td>Drainage / structure</td>
      <td>Provides aeration and structural stability. Does not break down.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Kanuma</td>
      <td>Acidic (azaleas)</td>
      <td>Japanese acidic soil. Ideal for azaleas and other acid-loving species.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Perlite</td>
      <td>Budget alternative</td>
      <td>Accessible drainage additive. Lighter than pumice. Good for beginners.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Bark fines</td>
      <td>Organic matter</td>
      <td>Retains moisture and nutrients. Use sparingly in bonsai mixes.</td>
    </tr>
  </table>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Recommended Mix Ratios</div>
    <table class="data-table" style="font-size: 8pt;">
      <tr>
        <th>Species Type</th>
        <th>Akadama</th>
        <th>Pumice</th>
        <th>Lava Rock</th>
      </tr>
      <tr><td style="font-weight:700;color:#161616;">Conifers (Pine/Juniper)</td><td style="text-align:center;">1 part</td><td style="text-align:center;">1 part</td><td style="text-align:center;">1 part</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Deciduous (Maple/Elm)</td><td style="text-align:center;">2 parts</td><td style="text-align:center;">1 part</td><td style="text-align:center;">1 part</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Tropical (Ficus/Jade)</td><td style="text-align:center;">1 part</td><td style="text-align:center;">1 part</td><td style="text-align:center;">1 part + bark</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Azalea</td><td style="text-align:center;">&mdash;</td><td style="text-align:center;">1 part</td><td style="text-align:center;">Kanuma 2 parts</td></tr>
    </table>
  </div>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">When to Repot</div>
    <div style="font-size: 8pt; line-height: 1.6; color: #444;">
      <div style="margin-bottom: 4px;"><strong>Frequency:</strong> Young/fast-growing trees every 1-2 years. Mature trees every 3-5 years. Conifers less frequently than deciduous.</div>
      <div style="margin-bottom: 4px;"><strong>Timing:</strong> Late winter / early spring, just before buds break. Tropicals: mid-summer when actively growing.</div>
      <div style="margin-bottom: 4px;"><strong>Signs:</strong> Water drains slowly. Roots circling the pot. Akadama breaking into mush. Tree lifting from pot.</div>
      <div><strong>Process:</strong> Remove 1/3 to 1/2 of old soil. Trim 1/3 of roots. Repot with fresh mix. Water thoroughly. Keep in shade 2 weeks.</div>
    </div>
  </div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def wiring_reference():
    pg = pn()
    return """<!-- PAGE %d: Wiring Reference -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Wiring &amp; Styling</span>
  </div>

  <div class="page-title">Wiring &amp; Styling Guide</div>
  <div class="page-subtitle">Shaping branches with patience and precision</div>

  <div class="info-box">
    <div class="info-title">The Purpose of Wiring</div>
    Wiring allows you to bend and position branches precisely. Unlike pruning (which removes material), wiring reshapes what already exists. It is the primary technique for creating the artistic form of your bonsai.
  </div>

  <div style="font-size: 8pt; line-height: 1.6; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 9.5pt; margin-bottom: 6px;">Wire Selection</div>
    <div style="margin-bottom: 4px;"><strong>Anodized aluminum:</strong> Easier for beginners. Softer, reusable. Good for deciduous and tropical species.</div>
    <div style="margin-bottom: 4px;"><strong>Annealed copper:</strong> Hardens when bent. Stronger hold for a thinner gauge. Preferred for conifers.</div>
    <div style="margin-bottom: 8px;"><strong>Rule of thumb:</strong> Use wire that is about 1/3 the thickness of the branch you are wiring.</div>

    <div style="font-weight: 700; color: #161616; font-size: 9.5pt; margin-bottom: 6px;">Application Steps</div>
    <div style="margin-bottom: 4px;"><strong>1.</strong> Anchor the wire by pushing the end deep into the soil at the trunk base.</div>
    <div style="margin-bottom: 4px;"><strong>2.</strong> Wrap at a 45-degree angle, evenly spaced. Keep wire firm but not crushing the bark.</div>
    <div style="margin-bottom: 4px;"><strong>3.</strong> Wire in the direction you intend to bend. Clockwise wrap = clockwise bend.</div>
    <div style="margin-bottom: 4px;"><strong>4.</strong> Use both hands to bend. Support the branch on both sides of the wire.</div>
    <div style="margin-bottom: 8px;"><strong>5.</strong> Check weekly. Remove before the wire cuts into the bark (bark biting).</div>
  </div>

  <div style="margin-top: 8px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">When to Remove Wire</div>
    <table class="data-table" style="font-size: 7.5pt;">
      <tr><th style="width:90px;">Species</th><th>Typical Duration</th><th>Watch For</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Fast-growing (Maple)</td><td>2-4 months in growing season</td><td>Bark swells quickly. Check weekly.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Juniper</td><td>6-12 months</td><td>Slow to set. Be patient.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Pine</td><td>6-18 months</td><td>Very slow. Can stay on through dormancy.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Tropical (Ficus)</td><td>1-3 months</td><td>Fast growth. Watch for marks.</td></tr>
    </table>
  </div>

  <div style="margin-top: 8px; padding: 6px 10px; background: #F5F8F0; border: 1px solid #C8D8B8; border-radius: 3px; font-size: 7.5pt; color: #666; font-style: italic;">
    <strong style="color: #4A6B3E;">Caution:</strong> Wire marks are permanent scars on the bark. It is always better to remove wire too early than too late. If in doubt, remove it and rewire later.
  </div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def pest_reference():
    pg = pn()
    return """<!-- PAGE %d: Pest Reference -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Pests &amp; Diseases</span>
  </div>

  <div class="page-title">Common Pests &amp; Diseases</div>
  <div class="page-subtitle">Identify and treat problems early</div>

  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:60px;">Problem</th>
      <th>Signs</th>
      <th>Treatment</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Aphids</td>
      <td>Clusters of tiny green/black insects on new growth. Sticky sap (honeydew) on leaves below.</td>
      <td>Spray with water. Neem oil. Insecticidal soap. Encourage ladybugs.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Spider Mites</td>
      <td>Fine webbing between leaves. Yellow stippling on foliage. Worse in dry heat.</td>
      <td>Spray underside of leaves with water daily. Neem oil. Increase humidity.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Scale</td>
      <td>Brown bumps on branches and leaves. Sticky residue. Ants farming them.</td>
      <td>Scrape off manually with toothpick. Systemic insecticide for severe cases.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Mealybugs</td>
      <td>White cottony masses in leaf joints and branch crotches.</td>
      <td>Remove with alcohol swab. Neem oil spray. Systemic for persistent cases.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Fungus Gnats</td>
      <td>Small black flies around soil. Larvae in topsoil damaging fine roots.</td>
      <td>Allow surface to dry between watering. Yellow sticky traps. BTI drench.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Powdery Mildew</td>
      <td>White powdery spots on leaves. Worse in high humidity / poor airflow.</td>
      <td>Improve airflow. Remove affected leaves. Fungicide spray. Reduce humidity.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Root Rot</td>
      <td>Soft black roots. Foul smell. Tree declining despite adequate water.</td>
      <td>Repot immediately. Remove all dead roots. Fresh gritty soil. Reduce water.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Leaf Burn</td>
      <td>Brown crispy leaf edges or tips. Not a pest &mdash; environmental.</td>
      <td>Protect from hot afternoon sun. Check watering. Provide wind protection.</td>
    </tr>
  </table>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Prevention</div>
    <div style="font-size: 8pt; line-height: 1.6; color: #444;">
      <div style="margin-bottom: 3px;">&bull; Inspect trees weekly, especially new growth and leaf undersides.</div>
      <div style="margin-bottom: 3px;">&bull; Good airflow between trees. Do not crowd.</div>
      <div style="margin-bottom: 3px;">&bull; Quarantine new trees for 2 weeks before adding to display.</div>
      <div style="margin-bottom: 3px;">&bull; Clean tools between trees with rubbing alcohol.</div>
      <div style="margin-bottom: 3px;">&bull; Healthy trees resist pests better &mdash; proper watering and feeding is the best defense.</div>
    </div>
  </div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def styles_reference():
    pg = pn()
    return """<!-- PAGE %d: Styles Reference -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Bonsai Styles</span>
  </div>

  <div class="page-title">Classical Bonsai Styles</div>
  <div class="page-subtitle">The five foundational forms and their variations</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px;">
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Formal Upright (Chokkan)</div>
      <div class="prop-card-value">Perfectly straight trunk, tapering from base to apex. Branches alternate left-right-back. The most challenging form. Best: Pine, Juniper, Maple.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Informal Upright (Moyogi)</div>
      <div class="prop-card-value">Curving S-shaped trunk. Most popular style. Natural look. Branches on outside of curves. Best: Most species.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Slanting (Shakan)</div>
      <div class="prop-card-value">Trunk leans at 60-80 degrees. Root mass anchors the leaning side. Suggests wind or cliff-side growth. Best: Pine, Juniper, Elm.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Cascade (Kengai)</div>
      <div class="prop-card-value">Trunk grows downward below the pot rim, mimicking a tree on a cliff. Needs a deep pot. Best: Juniper, Pine, Cotoneaster.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Semi-Cascade (Han-Kengai)</div>
      <div class="prop-card-value">Trunk extends horizontally then cascades but does not go below the pot base. Less dramatic than full cascade. Best: Juniper, Flowering species.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Literati (Bunjingi)</div>
      <div class="prop-card-value">Tall slender trunk with minimal foliage at top. Elegant and sparse. Inspired by Chinese scholar paintings. Best: Pine, Juniper.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Broom (Hokidachi)</div>
      <div class="prop-card-value">Straight trunk branching into a fan-shaped canopy at the top. Resembles a broom. Best: Zelkova, Elm, Maple.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Forest (Yose-ue)</div>
      <div class="prop-card-value">Multiple trees planted together to create a miniature forest. Odd numbers (3, 5, 7) look most natural. Best: Maple, Elm, Larch.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Root-over-Rock (Ishitsuki)</div>
      <div class="prop-card-value">Roots grow over and grip a rock, then descend into soil. Dramatic and ancient look. Best: Ficus, Maple, Juniper.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Windswept (Fukinagashi)</div>
      <div class="prop-card-value">All branches grow in one direction, as if shaped by constant wind. Evokes struggle and survival. Best: Juniper, Pine.</div>
    </div>
  </div>

  <div style="margin-top: 6px; padding: 5px 10px; background: #F5F8F0; border-radius: 3px; font-size: 7pt; color: #666; font-style: italic;">
    These forms are guides, not rules. The best bonsai reflects the natural character of the tree and the vision of the artist. Study mature trees in nature for inspiration.
  </div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def divider_section(num, label, title, subtitle):
    labels = ["One", "Two", "Three", "Four", "Five"]
    label_text = labels[num-1] if num <= 5 else label
    pg = pn()
    return """<!-- PAGE %d: Divider -->
<div class="divider">
  <div class="div-glow"></div>
  <div class="div-num">%02d</div>
  <div class="div-label">Part %s</div>
  <div class="div-title">%s</div>
  <div class="div-sub">%s</div>
</div>
""" % (pg, num, label_text, title, subtitle)


def tree_log_left(tree_num):
    """Left page: tree identification and basic info"""
    pg = pn()
    return """<!-- PAGE %d: Tree %d Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Tree #%02d</span>
    <span class="sh-right">Identity &amp; Status</span>
  </div>

  <div class="page-title">Tree #%02d &mdash; Profile</div>
  <div class="page-subtitle">The tree's identity and history</div>

  <!-- Basic Info -->
  <div style="background: #FAF8F4; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Acquired</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Species</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Common Name</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Source</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Physical -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Physical Description</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-bottom: 8px;">
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Style</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Approx. Age</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Height (cm)</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Trunk Caliper</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">Pot Size</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Pot Type</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Last Repot</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
  </div>

  <!-- Design Goal -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Design Vision &amp; Long-Term Goal</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Current photo note -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Front Photo (Today)</div>
  <div style="width: 100%%; height: 1.4in; border: 1px dashed #bbb; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 7pt; color: #ccc;">Photo or sketch here</div>

  <div class="page-footer">
    <span>Tree #%02d &mdash; Profile</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, tree_num, tree_num, tree_num, tree_num, page_no[0])


def tree_log_right(tree_num):
    """Right page: care log, health, and observations"""
    pg = pn()
    return """<!-- PAGE %d: Tree %d Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Tree #%02d</span>
    <span class="sh-right">Care Log &amp; Health</span>
  </div>

  <div class="page-title">Tree #%02d &mdash; Care Record</div>
  <div class="page-subtitle">Work performed, health status, observations</div>

  <!-- Work performed -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Work Performed This Session &mdash; Check All That Apply</div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Watered</span>
    <span class="check-item"><span class="check-box"></span> Fertilized</span>
    <span class="check-item"><span class="check-box"></span> Pruned</span>
    <span class="check-item"><span class="check-box"></span> Pinched</span>
    <span class="check-item"><span class="check-box"></span> Wired</span>
    <span class="check-item"><span class="check-box"></span> Wire Removed</span>
  </div>
  <div class="check-row" style="margin-bottom: 6px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Repotted</span>
    <span class="check-item"><span class="check-box"></span> Root Pruned</span>
    <span class="check-item"><span class="check-box"></span> Defoliated</span>
    <span class="check-item"><span class="check-box"></span> Repositioned</span>
    <span class="check-item"><span class="check-box"></span> Pest Treatment</span>
    <span class="check-item"><span class="check-box"></span> Winterized</span>
  </div>

  <!-- Care details -->
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-bottom: 8px;">
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Fertilizer Used</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Soil Mix</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Wire Gauge</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Weather / Temp</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
  </div>

  <!-- Health ratings -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Health &amp; Vigor &mdash; Rate 1 (Poor) to 5 (Excellent)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Foliage</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Roots</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Bark</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>

  <div style="display: flex; align-items: center; gap: 8px; margin-top: 6px; margin-bottom: 6px;">
    <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt;">Overall</span>
    <span class="stars">&#10022; &#10022; &#10022; &#10022; &#10022;</span>
  </div>

  <!-- Issues -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Pests / Issues / Concerns</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Notes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Observations &amp; Next Steps</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Tree #%02d &mdash; Care Record</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, tree_num, tree_num, tree_num, tree_num, page_no[0])


def collection_overview(page_of, total_pages):
    pg = pn()
    return """<!-- PAGE %d: Collection Overview -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Collection Overview</span>
    <span class="sh-right">Page %d of %d</span>
  </div>

  <div class="page-title">Collection Overview</div>
  <div class="page-subtitle">Quick-reference inventory of all trees</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Species</th>
      <th style="width:45px;">Style</th>
      <th style="width:28px;">Age</th>
      <th style="width:30px;">Health</th>
      <th style="width:28px;">Rating</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">1</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">2</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">3</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">4</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">5</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">6</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">7</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">8</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">9</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">10</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">11</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">12</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Style: Upright/Slanting/Cascade/Forest/Literati/etc. | Health: 1-5 | Rating: 1-5 stars</div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_of, total_pages, page_no[0])


def seasonal_calendar():
    """Year-round seasonal task calendar"""
    pg = pn()
    return """<!-- PAGE %d: Seasonal Calendar -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Seasonal Care</span>
    <span class="sh-right">My Year-Round Task Calendar</span>
  </div>

  <div class="page-title">Seasonal Care Calendar</div>
  <div class="page-subtitle">Plan and track recurring tasks by season</div>

  <div class="season-strip">
    <div class="season-cell" style="background: #4A8B4A;">Spring</div>
    <div class="season-cell" style="background: #D4AC0D;">Summer</div>
    <div class="season-cell" style="background: #B5704A;">Fall</div>
    <div class="season-cell" style="background: #6B7A8A;">Winter</div>
  </div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:60px;">Season</th>
      <th>Key Tasks</th>
      <th style="width:50px;">Done?</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#4A8B4A;">Spring</td>
      <td>Repot deciduous when buds swell. Structural pruning. Apply wire. Start feeding (low nitrogen first). Protect from late frost.</td>
      <td style="text-align:center;"><span class="check-box"></span></td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#4A8B4A;">Spring</td>
      <td>Pine: decandle. Juniper: pinch growth. Check for aphids on new growth. Move outdoor trees to full sun.</td>
      <td style="text-align:center;"><span class="check-box"></span></td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#D4AC0D;">Summer</td>
      <td>Water 1-2x daily in heat. Defoliate maples (mid-summer). Fertilize regularly. Shade sensitive species from afternoon sun.</td>
      <td style="text-align:center;"><span class="check-box"></span></td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#D4AC0D;">Summer</td>
      <td>Watch for spider mites. Trim long shoots. Apply wire to summer growth. Tropicals: peak growing season, prune hard.</td>
      <td style="text-align:center;"><span class="check-box"></span></td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#B5704A;">Fall</td>
      <td>Stop nitrogen fertilizer (switch to 0-10-10 for hardening). Remove wire before dormancy. Clean dead leaves.</td>
      <td style="text-align:center;"><span class="check-box"></span></td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#B5704A;">Fall</td>
      <td>Light pruning only. Jin and shari work on junipers. Bring tropicals indoors. Prepare winter shelter for hardy trees.</td>
      <td style="text-align:center;"><span class="check-box"></span></td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#6B7A8A;">Winter</td>
      <td>Structural pruning of bare deciduous branches. Major branch removal. Protect pots from freezing. Minimal watering.</td>
      <td style="text-align:center;"><span class="check-box"></span></td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#6B7A8A;">Winter</td>
      <td>Plan next year's design changes. Order supplies (soil, wire, pots). Study and sketch. Inventory tool condition.</td>
      <td style="text-align:center;"><span class="check-box"></span></td>
    </tr>
  </table>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Notes &amp; Reminders</div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
  </div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def supplies_log(page_of, total_pages):
    """Supplies and tools inventory"""
    pg = pn()
    return """<!-- PAGE %d: Supplies -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Supplies &amp; Tools</span>
    <span class="sh-right">Page %d of %d</span>
  </div>

  <div class="page-title">Supplies &amp; Tools Inventory</div>
  <div class="page-subtitle">Track your bonsai toolkit and consumables</div>

  <div class="gear-card">
    <div class="gear-label">Tools</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Tool</th><th style="width:50px;">Brand/Type</th><th style="width:30px;">Have?</th><th>Notes</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Concave Cutter</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Shears (Long)</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Shears (Short)</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Wire Cutter</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Knob Cutter</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Root Hook</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Chopstick</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Wire Stock</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th style="width:50px;">Gauge</th><th>Type (Al/Cu)</th><th style="width:40px;">Quantity</th><th>Notes</th></tr>
      <tr><td style="font-weight:700;color:#161616;">1.0 mm</td><td></td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">1.5 mm</td><td></td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">2.0 mm</td><td></td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">3.0 mm</td><td></td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">4.0 mm</td><td></td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">5.0 mm</td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Soil Components &amp; Fertilizer</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Item</th><th style="width:40px;">Quantity</th><th>Reorder?</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Akadama</td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Pumice</td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Lava Rock</td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Fertilizer (cakes)</td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Liquid Feed</td><td></td><td></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_of, total_pages, page_no[0])


def show_record():
    """Exhibition and show record"""
    pg = pn()
    return """<!-- PAGE %d: Show Record -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Exhibition</span>
    <span class="sh-right">Show &amp; Display Records</span>
  </div>

  <div class="page-title">Exhibition Records</div>
  <div class="page-subtitle">Track shows, displays, and feedback</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th style="width:45px;">Date</th>
      <th>Show / Event</th>
      <th style="width:40px;">Tree(s)</th>
      <th>Result / Feedback</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">6</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">7</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#5A7A4A;">8</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Preparation Checklist for Next Show</div>
    <div class="check-row" style="margin-bottom: 4px; font-size: 8pt;">
      <span class="check-item"><span class="check-box"></span> Clean pot</span>
      <span class="check-item"><span class="check-box"></span> Top dress moss</span>
      <span class="check-item"><span class="check-box"></span> Remove wire marks</span>
      <span class="check-item"><span class="check-box"></span> Final pruning</span>
      <span class="check-item"><span class="check-box"></span> Select accent plant</span>
      <span class="check-item"><span class="check-box"></span> Select scroll</span>
    </div>
  </div>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Judge's Comments &amp; Lessons Learned</div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
  </div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def favorites_summary():
    """Year-in-review"""
    pg = pn()
    return """<!-- PAGE %d: Favorites -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Year in Review</span>
    <span class="sh-right">Reflections &amp; Favorites</span>
  </div>

  <div class="page-title">Collection Year in Review</div>
  <div class="page-subtitle">Reflect on the year and plan the next</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Total Trees</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Species Count</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">New This Year</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Best Trees This Year</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Tree Name</th>
      <th style="width:45px;">Style</th>
      <th style="width:30px;">Rating</th>
      <th>Why It Stands Out</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Personal Milestones</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Winner</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">Best Progress</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Most Challenging</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Styling Result</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Lesson</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Losses / Failures</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">Goals for Next Year</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def notes_page():
    pg = pn()
    lines = ""
    for _ in range(18):
        lines += '<div class="wline"></div>\n'
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Notes</span>
    <span class="sh-right"></span>
  </div>
  <div class="page-title">Notes</div>
  <div class="page-subtitle">Observations, ideas, and reminders</div>
  %s
  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, lines, page_no[0])


def sketch_page():
    pg = pn()
    return """<!-- PAGE %d: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Sketch Pad</span>
    <span class="sh-right">Design &amp; Styling Drawings</span>
  </div>
  <div class="page-title">Sketch Pad</div>
  <div class="page-subtitle">Draw tree designs, styling plans, and future visions</div>
  <div class="dot-grid" style="width: 100%%; height: 6.5in; border-radius: 4px;"></div>
  <div class="page-footer">
    <span>Bonsai Tree Care Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def final_page():
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="cover">
  <div class="glow-bg"></div>
  <div class="title-block">
    <div style="font-size: 18pt; font-weight: 700; color: #ffffff; margin-bottom: 10px;">Patience Is the Greatest Tool</div>
    <div class="accent-bar"></div>
    <div class="subtitle" style="font-size: 10pt; color: #7A9A6A; font-style: italic;">
      The best time to shape a bonsai was twenty years ago.<br>The second best time is today.
    </div>
    <div style="margin-top: 30px;">
      <div class="tagline">More Shine Press</div>
    </div>
  </div>
</div>
""" % pg


# ============================================================
# MAIN
# ============================================================

def main():
    pages = []

    # ---- Front Matter ----
    pages.append(cover())                          # 1: Cover
    pages.append(owner_page())                     # 2: Owner

    # ---- Reference Section ----
    pages.append(how_to_use())                     # 3: How to use
    pages.append(species_reference())              # 4: Species reference
    pages.append(pruning_calendar())               # 5: Pruning calendar
    pages.append(watering_guide())                 # 6: Watering
    pages.append(soil_reference())                 # 7: Soil & repotting
    pages.append(wiring_reference())               # 8: Wiring
    pages.append(pest_reference())                 # 9: Pests & diseases
    pages.append(styles_reference())               # 10: Styles

    # ---- Section 1: Tree Logs ----
    pages.append(divider_section(1, "One", "Tree Records", "40 individual tree profiles and care logs"))
    NUM_TREES = 40
    for i in range(1, NUM_TREES + 1):
        pages.append(tree_log_left(i))
        pages.append(tree_log_right(i))

    # ---- Section 2: Collection Management ----
    pages.append(divider_section(2, "Two", "Collection Management", "Inventory, seasonal care, and supplies"))
    pages.append(collection_overview(1, 4))
    pages.append(collection_overview(2, 4))
    pages.append(collection_overview(3, 4))
    pages.append(collection_overview(4, 4))
    pages.append(seasonal_calendar())
    pages.append(supplies_log(1, 2))
    pages.append(supplies_log(2, 2))
    pages.append(show_record())

    # ---- Section 3: Reflection & Notes ----
    pages.append(divider_section(3, "Three", "Reflection &amp; Notes", "Year in review and observations"))
    pages.append(favorites_summary())
    pages.append(sketch_page())
    pages.append(sketch_page())
    for _ in range(5):
        pages.append(notes_page())

    # ---- Final ----
    pages.append(final_page())

    body_content = "\n".join(pages)
    total_pages = page_no[0]

    full_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>%s &mdash; More Shine Press</title>
<style>%s</style>
</head>
<body>
%s
</body>
</html>""" % (BOOK_TITLE, CSS, body_content)

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)

    print("Generated: %s" % HTML_FILE)
    print("Total pages: %d" % total_pages)

    print("\nPage breakdown:")
    print("  Cover: 1")
    print("  Owner: 1")
    print("  Reference (how-to, species, pruning, watering, soil, wiring, pests, styles): 8")
    print("  Section dividers: 3")
    print("  Tree logs (%d x 2 pages): %d" % (NUM_TREES, NUM_TREES * 2))
    print("  Collection overview: 4")
    print("  Seasonal calendar: 1")
    print("  Supplies & tools: 2")
    print("  Show records: 1")
    print("  Year in review: 1")
    print("  Sketch pages: 2")
    print("  Notes pages: 5")
    print("  Final: 1")
    print("  TOTAL: %d" % total_pages)

    assert total_pages % 2 == 0, "Page count %d is odd — KDP requires even" % total_pages


if __name__ == "__main__":
    main()
