#!/usr/bin/env python3
"""
Metal Detecting Logbook — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Metal detecting hobbyists, relic hunters, coin shooters, beach combers
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "metal_detecting_logbook_us_V1.0.html")

BOOK_TITLE = "Metal Detecting Logbook"
BOOK_SUBTITLE = "Every Signal Tells a Story"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

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
   Copper: #8A6A3A, #A07D4A, #6B4E2E
   Verdigris: #5A8A6A, #7AAA8A, #4A7A5A
   Gold: #C4A04A
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

/* ================ INTERIOR COVER ================ */
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #8A6A3A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #5A8A6A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #8A6A3A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #7AAA8A, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #6B4E2E, transparent);
}

/* CSS Metal Detecting Coil Illustration */
.cover .coil-wrap {
  width: 120px; height: 170px;
  position: relative;
  margin: 0 auto 18px;
}

/* Search coil (ellipse) */
.cover .coil-base {
  width: 78px; height: 40px;
  position: absolute;
  top: 95px; left: 21px;
  background: linear-gradient(180deg,
    rgba(138,106,58,0.15) 0%,
    rgba(90,138,106,0.10) 100%);
  border: 1px solid rgba(138,106,58,0.30);
  border-radius: 50%;
}

/* Coil inner ring */
.cover .coil-inner {
  width: 64px; height: 30px;
  position: absolute;
  top: 100px; left: 28px;
  border: 1px solid rgba(138,106,58,0.20);
  border-radius: 50%;
}

/* Coil center dot */
.cover .coil-center {
  width: 8px; height: 8px;
  position: absolute;
  top: 111px; left: 56px;
  border-radius: 50%;
  background: rgba(196,160,74,0.20);
  border: 1px solid rgba(196,160,74,0.30);
}

/* Signal waves */
.cover .wave1 {
  width: 50px; height: 20px;
  position: absolute;
  top: 85px; left: 35px;
  border: 1px solid rgba(196,160,74,0.20);
  border-bottom: none;
  border-radius: 50% 50% 0 0;
}
.cover .wave2 {
  width: 65px; height: 28px;
  position: absolute;
  top: 78px; left: 27px;
  border: 1px solid rgba(196,160,74,0.15);
  border-bottom: none;
  border-radius: 50% 50% 0 0;
}
.cover .wave3 {
  width: 80px; height: 35px;
  position: absolute;
  top: 70px; left: 20px;
  border: 1px solid rgba(196,160,74,0.10);
  border-bottom: none;
  border-radius: 50% 50% 0 0;
}

/* Shaft line */
.cover .shaft {
  width: 3px; height: 55px;
  position: absolute;
  top: 40px; left: 58px;
  background: rgba(90,138,106,0.15);
  border-radius: 1px;
}

/* Old coin (found treasure) */
.cover .coin {
  width: 22px; height: 22px;
  position: absolute;
  top: 30px; left: 49px;
  border-radius: 50%;
  background: rgba(196,160,74,0.15);
  border: 1.5px solid rgba(196,160,74,0.30);
}
.cover .coin-inner {
  width: 14px; height: 14px;
  position: absolute;
  top: 34px; left: 53px;
  border-radius: 50%;
  border: 0.8px solid rgba(196,160,74,0.20);
}

/* Ground line */
.cover .ground {
  width: 90px; height: 2px;
  position: absolute;
  top: 135px; left: 15px;
  background: rgba(90,90,90,0.15);
}

/* Buried item dashes */
.cover .buried1 {
  width: 14px; height: 6px;
  position: absolute;
  top: 145px; left: 25px;
  background: rgba(138,106,58,0.12);
  border-radius: 2px;
}
.cover .buried2 {
  width: 10px; height: 5px;
  position: absolute;
  top: 150px; left: 65px;
  background: rgba(90,138,106,0.12);
  border-radius: 50%;
}

/* Sparkle */
.cover .sparkle1 {
  width: 4px; height: 4px;
  background: rgba(196,160,74,0.4);
  border-radius: 50%;
  position: absolute;
  top: 25px; left: 85px;
  box-shadow: 0 0 4px rgba(196,160,74,0.3);
}
.cover .sparkle2 {
  width: 3px; height: 3px;
  background: rgba(196,160,74,0.3);
  border-radius: 50%;
  position: absolute;
  top: 20px; left: 20px;
  box-shadow: 0 0 3px rgba(196,160,74,0.2);
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 23pt;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.15;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 6px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 110px; height: 2.5px;
  background: #8A6A3A;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 11pt;
  color: #7AAA8A;
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
  border: 1px solid rgba(138,106,58,0.40);
  color: #8A6A3A;
  font-size: 7pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 9px;
  border-radius: 3px;
  text-transform: uppercase;
}

.cover .tagline {
  font-size: 8.5pt;
  color: #7AAA8A;
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #8A6A3A, transparent),
    radial-gradient(ellipse 25px 15px at 80% 30%, #5A8A6A, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 25% 85%, #8A6A3A, transparent);
}

.divider .div-num {
  font-size: 60pt;
  color: rgba(138,106,58,0.12);
  font-weight: 700;
  position: absolute;
  top: 1in;
}

.divider .div-label {
  font-size: 10pt;
  color: #8A6A3A;
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
  color: #7AAA8A;
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
  border-bottom: 1.5px solid #8A6A3A;
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
  background: #8A6A3A;
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
  border-left: 3px solid #8A6A3A;
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
  border: 1.5px solid #8A6A3A;
  border-radius: 50%;
  display: inline-block;
}

.prop-card {
  border: 1px solid #D8D0C0;
  border-radius: 4px;
  padding: 6px 8px;
  margin-bottom: 5px;
  background: #FCFAF7;
}
.prop-card-label {
  font-size: 7pt;
  font-weight: 700;
  color: #8A6A3A;
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
  border: 1px solid #D8D0C0;
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
  color: #8A6A3A;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 4px;
}

.dot-grid {
  background-image: radial-gradient(circle, #d0d0d0 1px, transparent 1px);
  background-size: 0.20in 0.20in;
  background-position: 0.10in 0.10in;
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
  <div class="coil-wrap">
    <div class="sparkle1"></div>
    <div class="sparkle2"></div>
    <div class="coin"></div>
    <div class="coin-inner"></div>
    <div class="wave3"></div>
    <div class="wave2"></div>
    <div class="wave1"></div>
    <div class="shaft"></div>
    <div class="coil-base"></div>
    <div class="coil-inner"></div>
    <div class="coil-center"></div>
    <div class="ground"></div>
    <div class="buried1"></div>
    <div class="buried2"></div>
  </div>
  <div class="title-block">
    <div class="main-title">%s</div>
    <div class="accent-bar"></div>
    <div class="subtitle">%s</div>
    <div class="features">
      <span class="feature-badge">40 Finds</span>
      <span class="feature-badge">GPS Log</span>
      <span class="feature-badge">ID Guide</span>
      <span class="feature-badge">Care Tips</span>
    </div>
    <div class="tagline">For Detectorists &amp; Treasure Hunters</div>
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
    <div style="font-size: 16pt; font-weight: 700; color: #161616; margin-bottom: 6px;">This Logbook Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #161616; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #8A6A3A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Years Detecting</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #8A6A3A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Detector Model(s)</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #8A6A3A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Hunting Ground</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #8A6A3A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Best Find So Far</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Metal Detecting Logbook</span>
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

  <div class="page-title">How to Use This Logbook</div>
  <div class="page-subtitle">Every find has a story worth preserving</div>

  <div class="info-box">
    <div class="info-title">Why Document Your Finds?</div>
    Metal detecting is as much about the story as the object. Without records, details fade — where you found it, what settings you used, how deep it was. A logbook helps you identify patterns, return to productive sites, and preserve the provenance that gives each find meaning.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Tips for Better Records</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Record GPS coordinates.</strong> Mark every productive spot. Phone GPS apps work well. Future you will thank present you when you want to revisit a site that produced silver.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Note detector settings.</strong> Record sensitivity, discrimination, frequency, and search mode. Different settings find different things. Knowing what worked helps you repeat success.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Log depth and signal.</strong> Record the depth reading and the signal tone (high/low/choppy/whisper). This builds your ear for interpreting signals before you dig.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Photograph in situ.</strong> Take a photo of the find in the hole before removing it. Context and soil conditions help with identification and dating.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Clean carefully.</strong> Wrong cleaning destroys value. Note what method you used and the results. Coins especially need gentle handling.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>6. Research your finds.</strong> Spend time identifying items. Old coins, buckles, buttons, and relics all have stories. Note your research findings in the notes section.
    </div>
  </div>

  <div class="page-footer">
    <span>Metal Detecting Logbook</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def metal_identification_reference():
    pg = pn()
    return """<!-- PAGE %d: Metal ID -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Metal Identification</span>
  </div>

  <div class="page-title">Identifying Common Finds</div>
  <div class="page-subtitle">What the ground gives up</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:70px;">Metal Type</th>
      <th style="width:30px;">Signal</th>
      <th style="width:30px;">Tone</th>
      <th>Identification Tips</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Copper</td>
      <td style="text-align:center;">Med-High</td>
      <td style="text-align:center;">Smooth</td>
      <td>Green patina (verdigris). Pennies, old tokens, copper artifacts. Conductive, strong signal.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Silver</td>
      <td style="text-align:center;">High</td>
      <td style="text-align:center;">Bright</td>
      <td>Tarnishes black/brown. Coins, jewelry. Very conductive. High-pitched bell tone. Rings clear.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Gold</td>
      <td style="text-align:center;">Low-Med</td>
      <td style="text-align:center;">Smooth</td>
      <td>Does not tarnish. Rings, coins, nuggets. Low conductive. Often same VDI as foil/pulltab.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Brass</td>
      <td style="text-align:center;">Med-High</td>
      <td style="text-align:center;">Smooth</td>
      <td>Yellow-gold color. Buckles, buttons, cartridge cases. Strong, smooth signal. Similar to copper.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Bronze</td>
      <td style="text-align:center;">Med</td>
      <td style="text-align:center;">Smooth</td>
      <td>Brownish-green patina. Ancient coins, statues, relics. Harder than copper, similar signal.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Iron</td>
      <td style="text-align:center;">Low</td>
      <td style="text-align:center;">Choppy</td>
      <td>Rusts red-brown. Nails, wire, tools, horseshoes. Usually discriminated out. Jumpy signal.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Steel</td>
      <td style="text-align:center;">Low</td>
      <td style="text-align:center;">Choppy</td>
      <td>Silver-gray, rusts. Modern items, bottle caps, screws. Magnetic. Loud, jumpy, often double blips.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Lead</td>
      <td style="text-align:center;">Low</td>
      <td style="text-align:center;">Soft</td>
      <td>Heavy, dull gray-white. Bullets, fishing weights, toy soldiers, pipes. Soft signal, heavy for size.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Aluminum</td>
      <td style="text-align:center;">Med-High</td>
      <td style="text-align:center;">Var.</td>
      <td>Lightweight, silver. Pull tabs, cans, foil. Frustrating &mdash; reads similar to gold. Light for size.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Nickel</td>
      <td style="text-align:center;">Low-Med</td>
      <td style="text-align:center;">Smooth</td>
      <td>Coins, buttons, buckles. Falls between foil and pull tab on VDI scale. Moderate conductivity.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Zinc</td>
      <td style="text-align:center;">Med</td>
      <td style="text-align:center;">Var.</td>
      <td>Bluish-white. Modern pennies (1982+). Corrodes with white crust in soil. Crumbly if buried long.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Platinum</td>
      <td style="text-align:center;">Low</td>
      <td style="text-align:center;">Smooth</td>
      <td>Silver-white. Rare &mdash; rings, jewelry. Very low conductivity. Similar to iron but smooth tone.</td>
    </tr>
  </table>

  <div style="margin-top: 6px; padding: 5px 8px; background: #FAF8F4; border-radius: 3px; font-size: 6.5pt; color: #777; font-style: italic;">
    Signal = strength relative to other metals. Tone = audio character. VDI (Visual Discrimination Indicator) numbers vary by detector brand. Always dig questionable targets &mdash; the best finds often mask as trash.
  </div>

  <div class="page-footer">
    <span>Metal Detecting Logbook</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def cleaning_reference():
    pg = pn()
    return """<!-- PAGE %d: Cleaning -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Cleaning &amp; Preservation</span>
  </div>

  <div class="page-title">Cleaning &amp; Preservation</div>
  <div class="page-subtitle">Handle with care &mdash; you only get one chance</div>

  <div class="info-box">
    <div class="info-title">The Golden Rule of Cleaning</div>
    When in doubt, do nothing. A dirty, uncleaned coin with original patina is worth more than a cleaned, scratched one. Aggressive cleaning destroys collector value instantly. Research before you touch anything that might be valuable.
  </div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:65px;">Material</th>
      <th style="width:30px;">Safe?</th>
      <th>Cleaning Method</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Coins (Valuable)</td>
      <td style="text-align:center;">NO</td>
      <td>Do not clean. Leave patina intact. Professional conservation only. Handling reduces grade.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Coins (Common)</td>
      <td style="text-align:center;">Soak</td>
      <td>Soak in distilled water 24-48 hrs. Gently brush with soft toothbrush. Never scrub. Olive oil soak for stubborn dirt (days to weeks).</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Silver</td>
      <td style="text-align:center;">Gentle</td>
      <td>Soak in water. Baking soda paste, gentle rub. Aluminum foil + baking soda bath removes tarnish. Never use abrasives on numismatic pieces.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Copper</td>
      <td style="text-align:center;">Careful</td>
      <td>Soak in olive oil for weeks. Soft brush only. Never remove green patina &mdash; it protects the surface and adds character.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Brass/Bronze</td>
      <td style="text-align:center;">Careful</td>
      <td>Soak in soapy water. Brass brushes only if heavily corroded. Preserve patina on relics. Wax to protect after cleaning.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Iron</td>
      <td style="text-align:center;">Yes</td>
      <td>Wire brush to remove loose rust. Soak in evaporust or molasses/water (weeks). Dry immediately. Coat with wax or oil to prevent re-rusting.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Lead</td>
      <td style="text-align:center;">Gentle</td>
      <td>Soak in water. Very soft &mdash; never scrub hard. White corrosion can be gently picked off. Handle carefully &mdash; lead is soft and toxic.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Gold</td>
      <td style="text-align:center;">Yes</td>
      <td>Rinse in water. Gentle dish soap. Gold does not tarnish. Ultrasonic cleaner is safe. Jewelry polish cloth for shine.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Relics (Unknown)</td>
      <td style="text-align:center;">Research</td>
      <td>Identify material first. When in doubt, leave dirt on. Photograph before cleaning. Consult experts for potentially historic items.</td>
    </tr>
  </table>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">What Never to Do</div>
    <table class="data-table" style="font-size: 8pt;">
      <tr><th style="width:80px;">Don't</th><th>Why</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Polish coins</td><td>Removes toning and destroys numismatic value completely.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Use acids/chemicals</td><td>Eats metal surface. Vinegar, lemon juice, commercial cleaners all strip patina.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Scrub with abrasives</td><td>Creates hairline scratches that are visible under magnification. Lowers grade.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Tumble clean</td><td>Destroys surface detail on coins and delicate relics. Only for modern clad coins.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Use steel brushes</td><td>Scratches soft metals (copper, silver, lead). Embeds steel particles.</td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Metal Detecting Logbook</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def legal_reference():
    pg = pn()
    return """<!-- PAGE %d: Legal -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Permissions &amp; Laws</span>
  </div>

  <div class="page-title">Permissions &amp; Laws</div>
  <div class="page-subtitle">Always hunt legally and ethically</div>

  <div class="info-box">
    <div class="info-title">The Most Important Rule</div>
    Always get permission before detecting on private property. Trespassing is a crime. On public land, know the regulations before you go. When in doubt, ask the landowner or managing authority. A good reputation benefits every detectorist.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Private Property</div>
    <div style="margin-bottom: 5px;"><strong>1.</strong> Always get written permission from the landowner. A handshake is good, but a signed permission slip protects you.</div>
    <div style="margin-bottom: 5px;"><strong>2.</strong> Agree in advance on what happens to finds. Some landowners want a share. Be fair and build relationships.</div>
    <div style="margin-bottom: 5px;"><strong>3.</strong> Fill all holes. Leave the property as you found it. Carry a plug-cutting tool and learn proper digging technique.</div>
    <div style="margin-bottom: 12px;"><strong>4.</strong> Offer to share interesting finds or photos with the landowner. Good relationships lead to return visits and referrals.</div>

    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Public Lands (United States)</div>
    <div style="margin-bottom: 5px;"><strong>5.</strong> National Parks, Monuments, and Historic Sites: Detecting is generally prohibited. Do not detect in these areas.</div>
    <div style="margin-bottom: 5px;"><strong>6.</strong> State Parks: Regulations vary by state. Many require permits. Check with the state parks department before detecting.</div>
    <div style="margin-bottom: 5px;"><strong>7.</strong> City and County Parks: Often allowed, but check local ordinances. Some cities prohibit detecting or require permits.</div>
    <div style="margin-bottom: 5px;"><strong>8.</strong> Schoolyards and sports fields: Usually public property but may have restrictions. Check with the school district or recreation department.</div>
    <div style="margin-bottom: 12px;"><strong>9.</strong> Beaches: Many public beaches allow detecting. Some states require permits. Research the specific beach rules &mdash; rules differ even within the same county.</div>

    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Ethical Considerations</div>
    <div style="margin-bottom: 5px;"><strong>10.</strong> Report significant historical finds to local historians or museums. Context matters for understanding history.</div>
    <div style="margin-bottom: 5px;"><strong>11.</strong> Remove trash you dig. Every pull tab you take out makes the site cleaner for the next visit.</div>
    <div style="margin-bottom: 5px;"><strong>12.</strong> Respect archaeological sites. If you find something potentially significant, photograph in place, note location, and contact professionals.</div>
    <div><strong>13.</strong> Follow the Detectorist Code: leave no trace, fill holes, respect property, share knowledge, and represent the hobby well.</div>
  </div>

  <div class="page-footer">
    <span>Metal Detecting Logbook</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def detector_settings_reference():
    pg = pn()
    return """<!-- PAGE %d: Detector Settings -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Detector Settings Guide</span>
  </div>

  <div class="page-title">Detector Settings Guide</div>
  <div class="page-subtitle">Understanding your machine</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:70px;">Setting</th>
      <th style="width:45px;">Range</th>
      <th>What It Does</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Sensitivity</td>
      <td style="text-align:center;">1-10 / Max</td>
      <td>Detection depth and signal strength. Higher = deeper but more noise/interference. Lower in mineralized soil or near power lines.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Discrimination</td>
      <td style="text-align:center;">0-100</td>
      <td>Filters out unwanted metals (iron, foil). Higher = rejects more but may miss good targets. Low discrimination = dig everything.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Ground Balance</td>
      <td style="text-align:center;">0-100</td>
      <td>Tunes out mineralization in soil. Manual or auto. Essential in mineralized ground. Wrong GB = reduced depth and false signals.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Threshold</td>
      <td style="text-align:center;">Off-Max</td>
      <td>Background hum. Set barely audible. Changes in hum indicate targets. Key for small/deep targets in quiet hunting.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Tone ID</td>
      <td style="text-align:center;">1-4 / Multi</td>
      <td>Number of audio tones for different metals. More tones = more info but harder to learn. Multi-tone gives pitch per target ID number.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Frequency</td>
      <td style="text-align:center;">3-100 kHz</td>
      <td>Low (5 kHz) = depth, silver, high conductors. High (18+ kHz) = small gold, low conductors, separation in trash. Multi-frequency does both.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Notch Filter</td>
      <td style="text-align:center;">On/Off</td>
      <td>Rejects specific target ID categories while accepting others. Useful to notch out pull tabs while keeping nickel/gold range.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Pinpoint Mode</td>
      <td style="text-align:center;">Toggle</td>
      <td>Non-motion mode that locates exact target position. Signal gets louder as coil centers over target. Use before digging.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Search Mode</td>
      <td style="text-align:center;">Presets</td>
      <td>Pre-configured settings (Coins, Jewelry, Relic, Beach, All Metal). Good starting point. Customize as you learn your machine.</td>
    </tr>
  </table>

  <div style="margin-top: 12px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">VDI Number Guide (approximate &mdash; varies by detector)</div>
    <table class="data-table" style="font-size: 7.5pt;">
      <tr><th style="width:60px;">VDI Range</th><th>Likely Target</th></tr>
      <tr><td style="font-weight:700;color:#161616;">-10 to 0</td><td>Iron (nails, wire, horseshoes)</td></tr>
      <tr><td style="font-weight:700;color:#161616;">0 to 15</td><td>Foil, tiny gold nuggets, small bits</td></tr>
      <tr><td style="font-weight:700;color:#161616;">15 to 25</td><td>Pull tabs, nickels, small gold rings</td></tr>
      <tr><td style="font-weight:700;color:#161616;">25 to 40</td><td>Aluminum, screw caps, large gold</td></tr>
      <tr><td style="font-weight:700;color:#161616;">40 to 60</td><td>Pennies (copper), small brass, shotgun shells</td></tr>
      <tr><td style="font-weight:700;color:#161616;">60 to 80</td><td>Dimes, quarters, halves, silver coins</td></tr>
      <tr><td style="font-weight:700;color:#161616;">80 to 99</td><td>Large silver, copper, brass buttons, silver dollars</td></tr>
    </table>
  </div>

  <div style="margin-top: 8px; padding: 6px 10px; background: #FAF8F4; border-radius: 3px; font-size: 7pt; color: #777; font-style: italic;">
    <strong style="color: #8A6A3A;">Pro Tip:</strong> The best detectorists dig everything in new sites. Once you understand the trash pattern, start using discrimination. Silver and gold can hide in the same VDI range as trash &mdash; trust your ears and dig the smooth, repeatable signals.
  </div>

  <div class="page-footer">
    <span>Metal Detecting Logbook</span>
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


def find_log_left(find_num):
    """Left page: find identity, location, detector settings"""
    pg = pn()
    return """<!-- PAGE %d: Find %d Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Find #%02d</span>
    <span class="sh-right">Discovery</span>
  </div>

  <div class="page-title">Find #%02d &mdash; Discovery</div>
  <div class="page-subtitle">Location, conditions, and detector data</div>

  <!-- Find Info -->
  <div style="background: #FAF8F4; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
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
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Item Name</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 42px;">Material</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 42px;">Est. Age</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Location -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Location</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">Site Name</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">GPS Lat</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">GPS Long</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 8px;">
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Terrain Type</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Soil Condition</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
  </div>

  <!-- Detector Settings -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Detector Settings</div>
  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Setting</th>
      <th style="width:40px;">Value</th>
      <th>Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">1</td><td>Detector Model</td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">2</td><td>Search Mode</td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">3</td><td>Sensitivity</td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">4</td><td>Discrimination</td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">5</td><td>Ground Balance</td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">6</td><td>Coil Type</td><td></td><td></td></tr>
  </table>

  <!-- Signal -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Signal Data</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 5px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">VDI No.</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Depth</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Tone Type</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Signal Str.</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Find #%02d &mdash; Discovery</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, find_num, find_num, find_num, find_num, page_no[0])


def find_log_right(find_num):
    """Right page: cleaning, value, photo, notes"""
    pg = pn()
    return """<!-- PAGE %d: Find %d Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Find #%02d</span>
    <span class="sh-right">Care &amp; Notes</span>
  </div>

  <div class="page-title">Find #%02d &mdash; Care &amp; Notes</div>
  <div class="page-subtitle">Cleaning, preservation, and research</div>

  <!-- Cleaning -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Cleaning &amp; Preservation &mdash; Method Used</div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> None</span>
    <span class="check-item"><span class="check-box"></span> Water Soak</span>
    <span class="check-item"><span class="check-box"></span> Soft Brush</span>
    <span class="check-item"><span class="check-box"></span> Olive Oil</span>
    <span class="check-item"><span class="check-box"></span> Chemical</span>
    <span class="check-item"><span class="check-box"></span> Electrolysis</span>
  </div>
  <div class="check-row" style="margin-bottom: 6px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Professional</span>
    <span class="check-item"><span class="check-box"></span> Left As-Found</span>
  </div>

  <!-- Physical details -->
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-bottom: 8px;">
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Dimensions</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Weight</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Identifying Marks</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Patina/Condition</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
  </div>

  <!-- Value estimate -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Value Assessment</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">Est. Value</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Metal Weight</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Melt Value</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
  </div>

  <!-- Significance ratings -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Significance &mdash; Rate 1 (Common) to 5 (Rare)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Rarity</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Condition</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>

  <div style="display: flex; align-items: center; gap: 8px; margin-top: 4px; margin-bottom: 4px;">
    <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt;">Personal</span>
    <span class="stars">&#10022; &#10022; &#10022; &#10022; &#10022;</span>
  </div>

  <!-- Photo reference -->
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 6px;">
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Photo Ref. No.</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Kept / Returned / Sold</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
  </div>

  <!-- Notes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 4px; margin-bottom: 3px;">Research &amp; Notes</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Find #%02d &mdash; Care &amp; Notes</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, find_num, find_num, find_num, find_num, page_no[0])


def site_log(page_of, total_pages):
    pg = pn()
    return """<!-- PAGE %d: Site Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Hunting Sites</span>
    <span class="sh-right">Page %d of %d</span>
  </div>

  <div class="page-title">Hunting Sites Directory</div>
  <div class="page-subtitle">Quick-reference for productive locations</div>

  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Site Name</th>
      <th style="width:45px;">Location</th>
      <th style="width:25px;">Visits</th>
      <th style="width:25px;">Finds</th>
      <th style="width:25px;">Rating</th>
      <th>Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">4</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">5</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">6</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">7</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">8</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">9</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">10</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">11</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A6A3A;">12</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Rating: 1=Low yield, 5=Excellent | Visits = number of detecting sessions | Finds = total items recovered</div>

  <div class="page-footer">
    <span>Metal Detecting Logbook</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_of, total_pages, page_no[0])


def gear_inventory():
    pg = pn()
    return """<!-- PAGE %d: Gear -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Gear Inventory</span>
    <span class="sh-right">My Equipment</span>
  </div>

  <div class="page-title">Gear Inventory</div>
  <div class="page-subtitle">Track your detecting equipment</div>

  <div class="gear-card">
    <div class="gear-label">Detectors</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Model</th><th style="width:45px;">Freq.</th><th style="width:25px;">Have?</th><th>Notes</th></tr>
      <tr><td style="font-weight:700;color:#161616;"></td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;"></td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;"></td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Coils</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Coil</th><th style="width:35px;">Size</th><th style="width:25px;">Have?</th><th>Notes</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Stock Coil</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Small Sniper</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Large Search</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Double-D</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Digging &amp; Recovery Tools</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Tool</th><th style="width:45px;">Brand/Type</th><th style="width:25px;">Have?</th><th>Notes</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Digging Tool</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Lesche / Spade</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Sand Scoop</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Pinpointer</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Knee Pads</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Find Pouch</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Headphones</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Metal Detecting Logbook</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def year_in_review():
    pg = pn()
    return """<!-- PAGE %d: Year in Review -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Year in Review</span>
    <span class="sh-right">Best Finds</span>
  </div>

  <div class="page-title">Detecting Year in Review</div>
  <div class="page-subtitle">Reflect on the season and plan ahead</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Total Hunts</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Hours Out</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Total Finds</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Best Finds This Year</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Find</th>
      <th style="width:30px;">Date</th>
      <th style="width:30px;">Rating</th>
      <th>Why It Was Special</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Season Highlights</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Winner</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">Oldest Find</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Most Valuable</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Most Unexpected</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best New Site</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Hunt Day</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Lesson</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">Goals for Next Season</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Metal Detecting Logbook</span>
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
  <div class="page-subtitle">Research, site notes, and observations</div>
  %s
  <div class="page-footer">
    <span>Metal Detecting Logbook</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, lines, page_no[0])


def final_page():
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="cover">
  <div class="glow-bg"></div>
  <div class="title-block">
    <div style="font-size: 18pt; font-weight: 700; color: #ffffff; margin-bottom: 10px;">Every Hole Tells a Story</div>
    <div class="accent-bar"></div>
    <div class="subtitle" style="font-size: 10pt; color: #7AAA8A; font-style: italic;">
      The best find is still<br>waiting underground.
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
    pages.append(metal_identification_reference()) # 4: Metal ID
    pages.append(cleaning_reference())             # 5: Cleaning
    pages.append(legal_reference())                # 6: Legal
    pages.append(detector_settings_reference())    # 7: Detector settings

    # ---- Section 1: Find Logs ----
    pages.append(divider_section(1, "One", "Find Records", "40 detailed find logs &mdash; your personal treasure archive"))
    NUM_FINDS = 40
    for i in range(1, NUM_FINDS + 1):
        pages.append(find_log_left(i))
        pages.append(find_log_right(i))

    # ---- Section 2: Management ----
    pages.append(divider_section(2, "Two", "Site Management", "Locations, gear, and reflections"))
    pages.append(site_log(1, 2))
    pages.append(site_log(2, 2))
    pages.append(gear_inventory())
    pages.append(year_in_review())

    # ---- Section 3: Notes ----
    pages.append(divider_section(3, "Three", "Notes &amp; Research", "Observations and find research"))
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
    print("  Reference (how-to, metal ID, cleaning, legal, settings): 5")
    print("  Section dividers: 3")
    print("  Find logs (%d x 2 pages): %d" % (NUM_FINDS, NUM_FINDS * 2))
    print("  Site directory: 2")
    print("  Gear inventory: 1")
    print("  Year in review: 1")
    print("  Notes pages: 4")
    print("  Final: 1")
    print("  TOTAL: %d" % total_pages)

    assert total_pages % 2 == 0, "Page count %d is odd — KDP requires even" % total_pages


if __name__ == "__main__":
    main()
