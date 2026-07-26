#!/usr/bin/env python3
"""
Astronomy Observation Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Amateur astronomers, backyard stargazers, astrophotographers
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "astronomy_observation_journal_us_V1.0.html")

BOOK_TITLE = "Astronomy Observation Journal"
BOOK_SUBTITLE = "Under the Same Stars, Always Wondering"

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
   Midnight blue: #3A4A7A, #5A6A9A, #2A3A6A
   Gold: #C4A04A, #D4B896
   Nebula cyan: #4A7A8A, #6A9AAA, #3A6A7A
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #3A4A7A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #4A7A8A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #3A4A7A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #6A9AAA, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #2A3A6A, transparent);
}

/* CSS Star Field Illustration */
.cover .star-wrap {
  width: 120px; height: 170px;
  position: relative;
  margin: 0 auto 18px;
}

/* Telescope tube */
.cover .scope-base {
  width: 36px; height: 70px;
  position: absolute;
  top: 75px; left: 42px;
  background: linear-gradient(180deg,
    rgba(58,74,122,0.15) 0%,
    rgba(74,122,138,0.10) 100%);
  border: 1px solid rgba(58,74,122,0.30);
  border-radius: 4px;
  transform: rotate(-15deg);
}

/* Telescope aperture (top circle) */
.cover .scope-aperture {
  width: 38px; height: 12px;
  position: absolute;
  top: 73px; left: 41px;
  background: rgba(22,22,22,0.15);
  border: 1px solid rgba(58,74,122,0.25);
  border-radius: 50%;
  transform: rotate(-15deg);
}

/* Telescope mount/tripod */
.cover .tripod1 {
  width: 2px; height: 30px;
  position: absolute;
  top: 135px; left: 50px;
  background: rgba(90,90,90,0.15);
  transform: rotate(-15deg);
}
.cover .tripod2 {
  width: 2px; height: 30px;
  position: absolute;
  top: 135px; left: 58px;
  background: rgba(90,90,90,0.15);
  transform: rotate(10deg);
}
.cover .tripod3 {
  width: 2px; height: 28px;
  position: absolute;
  top: 135px; left: 65px;
  background: rgba(90,90,90,0.12);
  transform: rotate(20deg);
}

/* Stars */
.cover .star1 {
  width: 5px; height: 5px;
  position: absolute;
  top: 15px; left: 20px;
  background: rgba(196,160,74,0.5);
  border-radius: 50%;
  box-shadow: 0 0 6px rgba(196,160,74,0.4);
}
.cover .star2 {
  width: 4px; height: 4px;
  position: absolute;
  top: 25px; left: 80px;
  background: rgba(250,248,244,0.4);
  border-radius: 50%;
  box-shadow: 0 0 5px rgba(250,248,244,0.3);
}
.cover .star3 {
  width: 3px; height: 3px;
  position: absolute;
  top: 40px; left: 50px;
  background: rgba(196,160,74,0.4);
  border-radius: 50%;
  box-shadow: 0 0 4px rgba(196,160,74,0.3);
}
.cover .star4 {
  width: 3px; height: 3px;
  position: absolute;
  top: 50px; left: 95px;
  background: rgba(250,248,244,0.3);
  border-radius: 50%;
}
.cover .star5 {
  width: 2px; height: 2px;
  position: absolute;
  top: 60px; left: 15px;
  background: rgba(250,248,244,0.25);
  border-radius: 50%;
}
.cover .star6 {
  width: 2px; height: 2px;
  position: absolute;
  top: 10px; left: 55px;
  background: rgba(196,160,74,0.3);
  border-radius: 50%;
}
.cover .star7 {
  width: 2px; height: 2px;
  position: absolute;
  top: 35px; left: 100px;
  background: rgba(250,248,244,0.2);
  border-radius: 50%;
}

/* Constellation lines (faint) */
.cover .constline1 {
  width: 35px; height: 1px;
  position: absolute;
  top: 20px; left: 22px;
  background: rgba(196,160,74,0.10);
  transform: rotate(15deg);
}
.cover .constline2 {
  width: 30px; height: 1px;
  position: absolute;
  top: 28px; left: 50px;
  background: rgba(196,160,74,0.08);
  transform: rotate(-10deg);
}

/* Crescent moon */
.cover .moon {
  width: 16px; height: 16px;
  position: absolute;
  top: 18px; left: 88px;
  border-radius: 50%;
  background: rgba(196,160,74,0.08);
  border: 1px solid rgba(196,160,74,0.15);
  box-shadow: inset 5px 0 0 rgba(22,22,22,0.3);
}

/* Ground line */
.cover .ground {
  width: 90px; height: 1px;
  position: absolute;
  top: 160px; left: 15px;
  background: rgba(58,74,122,0.10);
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 22pt;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.15;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 6px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 110px; height: 2.5px;
  background: #3A4A7A;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 11pt;
  color: #6A9AAA;
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
  border: 1px solid rgba(58,74,122,0.40);
  color: #5A6A9A;
  font-size: 7pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 9px;
  border-radius: 3px;
  text-transform: uppercase;
}

.cover .tagline {
  font-size: 8.5pt;
  color: #6A9AAA;
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #3A4A7A, transparent),
    radial-gradient(ellipse 25px 15px at 80% 30%, #4A7A8A, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 25% 85%, #3A4A7A, transparent);
}

.divider .div-num {
  font-size: 60pt;
  color: rgba(58,74,122,0.12);
  font-weight: 700;
  position: absolute;
  top: 1in;
}

.divider .div-label {
  font-size: 10pt;
  color: #3A4A7A;
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
  color: #6A9AAA;
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
  border-bottom: 1.5px solid #3A4A7A;
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
  background: #3A4A7A;
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
  border-left: 3px solid #3A4A7A;
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
  border: 1.5px solid #3A4A7A;
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
  color: #3A4A7A;
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
  color: #3A4A7A;
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
  <div class="star-wrap">
    <div class="constline1"></div>
    <div class="constline2"></div>
    <div class="moon"></div>
    <div class="star1"></div>
    <div class="star2"></div>
    <div class="star3"></div>
    <div class="star4"></div>
    <div class="star5"></div>
    <div class="star6"></div>
    <div class="star7"></div>
    <div class="scope-base"></div>
    <div class="scope-aperture"></div>
    <div class="tripod1"></div>
    <div class="tripod2"></div>
    <div class="tripod3"></div>
    <div class="ground"></div>
  </div>
  <div class="title-block">
    <div class="main-title">%s</div>
    <div class="accent-bar"></div>
    <div class="subtitle">%s</div>
    <div class="features">
      <span class="feature-badge">40 Sessions</span>
      <span class="feature-badge">Object Log</span>
      <span class="feature-badge">Star Charts</span>
      <span class="feature-badge">Gear Ref</span>
    </div>
    <div class="tagline">For Amateur Astronomers &amp; Stargazers</div>
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
      <div style="font-size: 8pt; font-weight: 700; color: #3A4A7A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Experience Level</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #3A4A7A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Primary Telescope</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #3A4A7A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Target Type</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #3A4A7A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Home Observing Site</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Astronomy Observation Journal</span>
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
  <div class="page-subtitle">Every night under the stars is worth remembering</div>

  <div class="info-box">
    <div class="info-title">Why Keep an Observing Log?</div>
    An observing journal transforms casual stargazing into systematic discovery. Conditions change, objects reveal different details on different nights, and your skills grow with each session. Without records, you forget what you have seen and cannot track your progress as an observer. This journal is your personal astronomical archive.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Tips for Better Observing Notes</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Record conditions precisely.</strong> Note temperature, humidity, wind, and especially seeing and transparency. The same object looks dramatically different under different skies. Rate each on a 1-5 scale.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Dark adapt your eyes.</strong> Allow 20-30 minutes for full dark adaptation. Use only red light when reading or writing notes. White light resets your night vision completely.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Sketch what you see.</strong> Drawing forces you to look carefully. Even rough sketches capture details you would otherwise miss. Use the dot-grid sketch areas for your drawings.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Note magnification and eyepieces.</strong> Different objects need different powers. Record what eyepiece and magnification you used. This helps you choose the right setup next time.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Describe what you actually see.</strong> Not what the book says you should see. Note brightness, size, shape, color hints, and any detail visible. Honesty builds observing skill.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>6. Track the Moon phase.</strong> Moonlight washes out faint objects. Record the phase and Moon rise/set times. Plan deep-sky sessions around new Moon windows.
    </div>
  </div>

  <div class="page-footer">
    <span>Astronomy Observation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def magnitude_reference():
    pg = pn()
    return """<!-- PAGE %d: Magnitude -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Stellar Magnitude</span>
  </div>

  <div class="page-title">Understanding Magnitude</div>
  <div class="page-subtitle">The brightness scale of the sky</div>

  <div class="info-box">
    <div class="info-title">How Magnitude Works</div>
    The magnitude scale is backwards: lower numbers are brighter. Each magnitude step represents a brightness difference of about 2.5 times. A magnitude 1 star is 100 times brighter than a magnitude 6 star. Under dark skies, the naked eye limit is about magnitude 6.
  </div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:40px;">Mag</th>
      <th style="width:70px;">Example Star</th>
      <th>Visibility</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">-26.7</td><td>Sun</td><td>Do not observe directly &mdash; permanent eye damage.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">-12.6</td><td>Full Moon</td><td>Extremely bright. Washes out most deep-sky objects.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">-4.6</td><td>Venus (max)</td><td>Brilliant. Casts shadows. Brightest planet.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">-2.9</td><td>Jupiter (max)</td><td>Very bright. Always brighter than any star.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">-1.5</td><td>Sirius</td><td>Brightest night-time star. Blazes in winter sky.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">0.0</td><td>Vega</td><td>Reference star. Zero point of the magnitude scale.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">0.5</td><td>Arcturus</td><td>Bright spring star. Easy naked-eye target.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">1.0</td><td>Antares</td><td>Bright red supergiant. Easy to spot.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">2.0</td><td>Polaris</td><td>North Star. Moderate brightness. Useful navigation.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">3.0</td><td> Megrez</td><td>Faintest Big Dipper star. Still easy from suburbs.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">4.0</td><td>&mdash;</td><td>Faint from light-polluted skies. Easy under dark sky.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">5.0</td><td>Uranus</td><td>Barely visible naked-eye under dark skies.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">6.0</td><td>&mdash;</td><td>Naked-eye limit under ideal dark conditions.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">7+</td><td>&mdash;</td><td>Binocular or telescope required.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">9+</td><td>Neptune</td><td>Telescope required. Star-like blue point.</td></tr>
    <tr><td style="font-weight:700;color:#161616;text-align:center;">13+</td><td>Pluto</td><td>Large telescope required. Very challenging.</td></tr>
  </table>

  <div style="margin-top: 6px; padding: 5px 8px; background: #FAF8F4; border-radius: 3px; font-size: 6.5pt; color: #777; font-style: italic;">
    Magnitudes listed are apparent magnitude (brightness as seen from Earth). Absolute magnitude measures intrinsic brightness at a standard 10 parsecs distance. Planets vary because their distance from Earth changes.
  </div>

  <div class="page-footer">
    <span>Astronomy Observation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def messier_reference():
    pg = pn()
    return """<!-- PAGE %d: Messier Objects -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Best Messier Objects</span>
  </div>

  <div class="page-title">Top Messier Objects</div>
  <div class="page-subtitle">The finest deep-sky targets for amateur telescopes</div>

  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:25px;">M#</th>
      <th>Name</th>
      <th style="width:45px;">Type</th>
      <th style="width:40px;">Const.</th>
      <th style="width:22px;">Mag</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M31</td><td>Andromeda Galaxy</td><td>Galaxy</td><td>Andromeda</td><td style="text-align:center;">3.4</td><td>Largest galaxy in Local Group. Naked-eye visible.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M42</td><td>Orion Nebula</td><td>Nebula</td><td>Orion</td><td style="text-align:center;">4.0</td><td>Brightest nebula. Stunning in any telescope.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M45</td><td>Pleiades</td><td>Open Cluster</td><td>Taurus</td><td style="text-align:center;">1.6</td><td>Seven Sisters. Best in binoculars or wide-field.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M13</td><td>Great Cluster</td><td>Globular</td><td>Hercules</td><td style="text-align:center;">5.8</td><td>Finest globular in northern sky.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M57</td><td>Ring Nebula</td><td>Planetary</td><td>Lyra</td><td style="text-align:center;">8.8</td><td>Classic planetary nebula. Looks like a smoke ring.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M27</td><td>Dumbbell Nebula</td><td>Planetary</td><td>Vulpecula</td><td style="text-align:center;">7.5</td><td>Brightest planetary nebula. Visible in small scopes.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M51</td><td>Whirlpool Galaxy</td><td>Galaxy</td><td>Canes Venatici</td><td style="text-align:center;">8.4</td><td>Spiral arms visible in larger telescopes.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M81</td><td>Bode's Galaxy</td><td>Galaxy</td><td>Ursa Major</td><td style="text-align:center;">6.9</td><td>Bright spiral galaxy near M82.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M82</td><td>Cigar Galaxy</td><td>Galaxy</td><td>Ursa Major</td><td style="text-align:center;">8.4</td><td>Starburst galaxy. Elongated edge-on.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M44</td><td>Beehive Cluster</td><td>Open Cluster</td><td>Cancer</td><td style="text-align:center;">3.7</td><td>Large naked-eye cluster. Best in binoculars.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M1</td><td>Crab Nebula</td><td>Supernova</td><td>Taurus</td><td style="text-align:center;">8.4</td><td>Supernova remnant from 1054 AD.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M22</td><td>Sagittarius Cluster</td><td>Globular</td><td>Sagittarius</td><td style="text-align:center;">5.1</td><td>Brightest globular in northern hemisphere.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M104</td><td>Sombrero Galaxy</td><td>Galaxy</td><td>Virgo</td><td style="text-align:center;">8.0</td><td>Edge-on galaxy with dark dust lane.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M8</td><td>Lagoon Nebula</td><td>Nebula</td><td>Sagittarius</td><td style="text-align:center;">6.0</td><td>Bright emission nebula. Summer Milky Way.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M20</td><td>Trifid Nebula</td><td>Nebula</td><td>Sagittarius</td><td style="text-align:center;">6.3</td><td>Three-lobed nebula near M8.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M101</td><td>Pinwheel Galaxy</td><td>Galaxy</td><td>Ursa Major</td><td style="text-align:center;">7.9</td><td>Face-on spiral. Large but low surface brightness.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M11</td><td>Wild Duck Cluster</td><td>Open Cluster</td><td>Scutum</td><td style="text-align:center;">6.3</td><td>Rich, compact open cluster.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M15</td><td>Great Pegasus Cluster</td><td>Globular</td><td>Pegasus</td><td style="text-align:center;">6.2</td><td>Dense, compact globular cluster.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M16</td><td>Eagle Nebula</td><td>Nebula</td><td>Serpens</td><td style="text-align:center;">6.0</td><td>"Pillars of Creation" nebula.</td></tr>
    <tr><td style="font-weight:700;color:#3A4A7A;">M17</td><td>Swan/Omega Nebula</td><td>Nebula</td><td>Sagittarius</td><td style="text-align:center;">6.0</td><td>Bright nebula shaped like a swan.</td></tr>
  </table>

  <div style="margin-top: 6px; padding: 5px 8px; background: #FAF8F4; border-radius: 3px; font-size: 6.5pt; color: #777; font-style: italic;">
    The Messier catalog contains 110 objects. Charles Messier compiled it to help comet hunters avoid confusing these "fuzzy" objects with comets. Today it is a checklist of the sky's finest deep-sky targets. "M" numbers followed by the catalog entry.
  </div>

  <div class="page-footer">
    <span>Astronomy Observation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def telescope_reference():
    pg = pn()
    return """<!-- PAGE %d: Telescopes -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Telescope Types</span>
  </div>

  <div class="page-title">Telescope Types Comparison</div>
  <div class="page-subtitle">Understanding your instrument</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:65px;">Type</th>
      <th style="width:30px;">Cost</th>
      <th style="width:30px;">Maint.</th>
      <th>Strengths &amp; Weaknesses</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Refractor</td>
      <td style="text-align:center;">$$$</td>
      <td style="text-align:center;">Low</td>
      <td>Crisp high-contrast images. Great for Moon and planets. Low maintenance. Large apertures expensive. Chromatic aberration in cheap models.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Reflector (Newtonian)</td>
      <td style="text-align:center;">$</td>
      <td style="text-align:center;">Med</td>
      <td>Most aperture per dollar. Great deep-sky performance. No chromatic aberration. Requires collimation. Open tube gathers dust.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Dobsonian</td>
      <td style="text-align:center;">$</td>
      <td style="text-align:center;">Med</td>
      <td>Newtonian on simple alt-az mount. Best value for aperture. Large sizes manageable. Not for astrophotography. Manual pointing.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Schmidt-Cassegrain (SCT)</td>
      <td style="text-align:center;">$$$$</td>
      <td style="text-align:center;">Med</td>
      <td>Compact tube. Versatile for visual and photography. Long focal length for planets. Requires cooldown. Higher f-ratio.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Maksutov-Cassegrain</td>
      <td style="text-align:center;">$$$</td>
      <td style="text-align:center;">Low</td>
      <td>Compact and rugged. Excellent for planets and Moon. Slow cooldown. Narrow field of view. Heavier than equivalent SCT.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Binoculars</td>
      <td style="text-align:center;">$</td>
      <td style="text-align:center;">Low</td>
      <td>Wide field. Portable. Best first instrument. Great for large clusters and Milky Way. Limited magnification. Cannot do planetary detail.</td>
    </tr>
  </table>

  <div style="margin-top: 12px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Eyepiece Magnification Guide</div>
    <table class="data-table" style="font-size: 8pt;">
      <tr><th>Formula</th><th>Magnification = Telescope Focal Length / Eyepiece Focal Length</th></tr>
    </table>
    <table class="data-table" style="font-size: 7.5pt; margin-top: 4px;">
      <tr><th style="width:60px;">Scope FL</th><th style="width:35px;">Eyepiece</th><th style="width:35px;">Mag</th><th style="width:60px;">Use</th></tr>
      <tr><td style="font-weight:700;color:#161616;">1000mm</td><td style="text-align:center;">25mm</td><td style="text-align:center;">40x</td><td>Wide field, clusters, nebulae</td></tr>
      <tr><td style="font-weight:700;color:#161616;">1000mm</td><td style="text-align:center;">10mm</td><td style="text-align:center;">100x</td><td>General viewing, galaxies</td></tr>
      <tr><td style="font-weight:700;color:#161616;">1000mm</td><td style="text-align:center;">6mm</td><td style="text-align:center;">167x</td><td>Planets, Moon, globulars</td></tr>
      <tr><td style="font-weight:700;color:#161616;">2000mm</td><td style="text-align:center;">25mm</td><td style="text-align:center;">80x</td><td>Wide field for SCT</td></tr>
      <tr><td style="font-weight:700;color:#161616;">2000mm</td><td style="text-align:center;">10mm</td><td style="text-align:center;">200x</td><td>Planets and Moon detail</td></tr>
    </table>
  </div>

  <div style="margin-top: 8px; padding: 6px 10px; background: #FAF8F4; border-radius: 3px; font-size: 7pt; color: #777; font-style: italic;">
    <strong style="color: #3A4A7A;">Practical Limit:</strong> Maximum useful magnification is about 50x per inch of aperture. Beyond this, images become dim and blurry. Most nights, atmospheric seeing limits useful magnification to 200-300x regardless of telescope size.
  </div>

  <div class="page-footer">
    <span>Astronomy Observation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def bortle_reference():
    pg = pn()
    return """<!-- PAGE %d: Bortle Scale -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Bortle Dark Sky Scale</span>
  </div>

  <div class="page-title">Bortle Dark Sky Scale</div>
  <div class="page-subtitle">Rate your sky quality</div>

  <div class="info-box">
    <div class="info-title">What Is the Bortle Scale?</div>
    The Bortle Scale rates sky darkness from Class 1 (darkest) to Class 9 (inner city). It combines limiting magnitude, sky brightness, and visual observations into a single rating. Knowing your Bortle class helps predict what you can see and plan your observing sessions.
  </div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:25px;">Class</th>
      <th style="width:65px;">Sky Description</th>
      <th style="width:35px;">Lim. Mag</th>
      <th>What You Can See</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">1</td>
      <td>Excellent dark sky</td>
      <td style="text-align:center;">7.6-8.0</td>
      <td>Milky Way casts shadows. M33 naked-eye. Zodiacal light obvious. Rare.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">2</td>
      <td>Truly dark</td>
      <td style="text-align:center;">7.1-7.5</td>
      <td>Milky Way shows structure. M33 easily visible. Ground is dark.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">3</td>
      <td>Rural sky</td>
      <td style="text-align:center;">6.6-7.0</td>
      <td>Milky Way complex. Some light domes on horizon. Good observing.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">4</td>
      <td>Rural/Suburban</td>
      <td style="text-align:center;">6.1-6.5</td>
      <td>Milky Way visible overhead. Light domes obvious. Most clusters visible.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">5</td>
      <td>Suburban</td>
      <td style="text-align:center;">5.6-6.0</td>
      <td>Milky Way faint. Only overhead. Bright clusters and nebulae visible.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">6</td>
      <td>Bright Suburban</td>
      <td style="text-align:center;">5.1-5.5</td>
      <td>Milky Way only hints. Bright constellations easy. Need filters.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">7</td>
      <td>Suburban/Urban</td>
      <td style="text-align:center;">4.6-5.0</td>
      <td>No Milky Way. Bright stars only. Deep-sky limited to brightest.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">8</td>
      <td>City sky</td>
      <td style="text-align:center;">4.1-4.5</td>
      <td>Only major constellations visible. Moon and planets mainly.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">9</td>
      <td>Inner city</td>
      <td style="text-align:center;">4.0</td>
      <td>Only brightest stars. Moon, planets, and brightest clusters.</td>
    </tr>
  </table>

  <div style="margin-top: 12px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Moon Phase Impact on Observing</div>
    <table class="data-table" style="font-size: 8pt;">
      <tr><th style="width:65px;">Phase</th><th>Effect on Observing</th></tr>
      <tr><td style="font-weight:700;color:#161616;">New Moon</td><td>Best for deep-sky. Darkest skies. Plan galaxy and nebula sessions.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Crescent</td><td>Good early evening. Moon sets early. Decent deep-sky after Moon set.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">First/Last Quarter</td><td>Good for Moon itself. Deep-sky in Moon-free half of night.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Gibbous</td><td>Bright Moon most of night. Best for planets, double stars, Moon.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Full Moon</td><td>Worst for deep-sky. Excellent for Moon photography and planets.</td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Astronomy Observation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def seeing_reference():
    pg = pn()
    return """<!-- PAGE %d: Seeing &amp; Transparency -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Seeing &amp; Transparency</span>
  </div>

  <div class="page-title">Seeing and Transparency Scale</div>
  <div class="page-subtitle">Rate the two most important sky conditions</div>

  <div class="info-box">
    <div class="info-title">Seeing vs Transparency</div>
    Seeing is atmospheric steadiness &mdash; how much stars twinkle and images shimmer. Transparency is sky clarity &mdash; how dark the background sky is. Good seeing means sharp planetary views. Good transparency means faint deep-sky objects are visible. They are independent: a crystal-clear winter night often has poor seeing.
  </div>

  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th style="width:20px;">Rating</th>
      <th style="width:65px;">Seeing</th>
      <th style="width:65px;">Transparency</th>
      <th>What to Observe</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">5</td>
      <td>Excellent &mdash; rock-steady</td>
      <td>Excellent &mdash; jet black</td>
      <td>Everything. Push magnification on planets. Faint fuzzies at limit.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">4</td>
      <td>Good &mdash; minor shimmer</td>
      <td>Good &mdash; slight haze</td>
      <td>Planetary detail sharp. Most deep-sky objects easy.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">3</td>
      <td>Average &mdash; moderate</td>
      <td>Average &mdash; some haze</td>
      <td>Moon and bright planets fine. Bright clusters and nebulae.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">2</td>
      <td>Poor &mdash; lots of boil</td>
      <td>Poor &mdash; murky</td>
      <td>Only Moon, bright planets, and bright double stars.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#3A4A7A;text-align:center;">1</td>
      <td>Very poor &mdash; unsteady</td>
      <td>Very poor &mdash; overcast</td>
      <td>Almost nothing. Moon only. Pack up or observe from indoors.</td>
    </tr>
  </table>

  <div style="margin-top: 12px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Quick Seeing Test</div>
    <table class="data-table" style="font-size: 8pt;">
      <tr><th style="width:65px;">Observation</th><th>Seeing Rating</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Stars barely twinkle</td><td>5 (Excellent)</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Stars twinkle slightly</td><td>4 (Good)</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Stars twinkle moderately</td><td>3 (Average)</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Stars twinkle a lot, colors flash</td><td>2 (Poor)</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Stars dance wildly</td><td>1 (Very poor)</td></tr>
    </table>
  </div>

  <div style="margin-top: 12px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Polar Alignment Quick Reference</div>
    <table class="data-table" style="font-size: 8pt;">
      <tr><th style="width:65px;">Step</th><th>Action</th></tr>
      <tr><td style="font-weight:700;color:#161616;">1. Level</td><td>Level the mount. Approximate is fine for visual use.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">2. Set latitude</td><td>Adjust mount tilt to match your observing latitude.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">3. Find Polaris</td><td>Locate Polaris using the Big Dipper pointer stars.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">4. Center</td><td>Center Polaris in the polar scope or use the mount's polar axis.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">5. Refine</td><td>For photography: drift align. For visual: good enough.</td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Astronomy Observation Journal</span>
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


def observation_log_left(obs_num):
    """Left page: date, location, conditions, target"""
    pg = pn()
    return """<!-- PAGE %d: Observation %d Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Session #%02d</span>
    <span class="sh-right">Conditions</span>
  </div>

  <div class="page-title">Session #%02d &mdash; Conditions</div>
  <div class="page-subtitle">Date, location, weather, and target data</div>

  <!-- Session Info -->
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
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Observing Site</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 42px;">Latitude</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 42px;">Longitude</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Weather -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Weather Conditions</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 5px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">Temp</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Humidity</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Wind</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Cloud</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
  </div>

  <!-- Sky Quality Ratings -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Sky Quality &mdash; Rate 1 (Poor) to 5 (Excellent)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Seeing</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Transp.</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">Bortle Class</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Moon Phase</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Lim. Mag</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
  </div>

  <!-- Target -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Primary Target</div>
  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Object Name</th>
      <th style="width:40px;">Catalog</th>
      <th style="width:35px;">Type</th>
      <th style="width:30px;">Const.</th>
      <th style="width:25px;">Mag</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">1</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">2</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">3</td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div class="page-footer">
    <span>Session #%02d &mdash; Conditions</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, obs_num, obs_num, obs_num, obs_num, page_no[0])


def observation_log_right(obs_num):
    """Right page: equipment, observations, sketch"""
    pg = pn()
    return """<!-- PAGE %d: Observation %d Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Session #%02d</span>
    <span class="sh-right">Observations</span>
  </div>

  <div class="page-title">Session #%02d &mdash; Observations</div>
  <div class="page-subtitle">Equipment, viewing notes, and sketches</div>

  <!-- Equipment -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Equipment Used</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-bottom: 8px;">
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Telescope</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Aperture / FL</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Eyepiece(s)</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Magnification</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Filters Used</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Mount / Tracking</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
  </div>

  <!-- Viewing Notes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Viewing Notes &mdash; Describe What You Actually Saw</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Quality ratings -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Session Rating &mdash; Rate 1 (Poor) to 5 (Excellent)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Conditions</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Satisfaction</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>

  <!-- Sketch -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Field Sketch</div>
  <div class="dot-grid" style="width: 100%%; height: 1.7in; border-radius: 4px;"></div>

  <div class="page-footer">
    <span>Session #%02d &mdash; Observations</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, obs_num, obs_num, obs_num, obs_num, page_no[0])


def target_wishlist(page_of, total_pages):
    pg = pn()
    return """<!-- PAGE %d: Wishlist -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Observing Wishlist</span>
    <span class="sh-right">Page %d of %d</span>
  </div>

  <div class="page-title">Observing Wishlist</div>
  <div class="page-subtitle">Objects you want to observe</div>

  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Object Name</th>
      <th style="width:35px;">Catalog</th>
      <th style="width:30px;">Type</th>
      <th style="width:30px;">Const.</th>
      <th style="width:25px;">Best Season</th>
      <th style="width:25px;">Seen?</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">2</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">3</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">4</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">5</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">6</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">7</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">8</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">9</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">10</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">11</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#3A4A7A;">12</td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Type: Gxy=Galaxy, Neb=Nebula, OC=Open Cluster, GC=Globular, DN=Double Star, Pl=Planet | Seen: Y/N</div>

  <div class="page-footer">
    <span>Astronomy Observation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_of, total_pages, page_no[0])


def gear_inventory():
    pg = pn()
    return """<!-- PAGE %d: Gear -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Equipment Inventory</span>
    <span class="sh-right">My Observatory</span>
  </div>

  <div class="page-title">Equipment Inventory</div>
  <div class="page-subtitle">Track your astronomy gear</div>

  <div class="gear-card">
    <div class="gear-label">Telescopes</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Model</th><th style="width:35px;">Aperture</th><th style="width:35px;">Focal L.</th><th style="width:25px;">Have?</th><th>Notes</th></tr>
      <tr><td style="font-weight:700;color:#161616;"></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;"></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;"></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Eyepieces</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Model</th><th style="width:30px;">FL (mm)</th><th style="width:30px;">AFOV</th><th style="width:25px;">Have?</th><th>Notes</th></tr>
      <tr><td style="font-weight:700;color:#161616;"></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;"></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;"></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;"></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Barlow</td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Accessories</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Item</th><th style="width:45px;">Type/Brand</th><th style="width:25px;">Have?</th><th>Notes</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Filters</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Finderscope</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Red Flashlight</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Star Atlas/App</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Binoculars</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Camera</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Astronomy Observation Journal</span>
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
    <span class="sh-right">Best Sessions</span>
  </div>

  <div class="page-title">Observing Year in Review</div>
  <div class="page-subtitle">Reflect on your year under the stars</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Sessions Logged</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Objects Seen</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">New Messiers</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Best Sessions This Year</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Date</th>
      <th style="width:45px;">Highlights</th>
      <th style="width:30px;">Rating</th>
      <th>Why It Was Memorable</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Year Highlights</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Answer</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">Best New Object</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Most Challenging</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Dark Sky Site</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">New Skill/Technique</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Most Surprising Find</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Lesson</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">Goals for Next Year</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Astronomy Observation Journal</span>
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
  <div class="page-subtitle">Star charts, sketches, and observing notes</div>
  %s
  <div class="page-footer">
    <span>Astronomy Observation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, lines, page_no[0])


def sketch_page():
    pg = pn()
    return """<!-- PAGE %d: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Deep Sky Sketch Pad</span>
    <span class="sh-right">Field Drawings</span>
  </div>
  <div class="page-title">Deep Sky Sketch Pad</div>
  <div class="page-subtitle">Draw what you see at the eyepiece</div>
  <div class="dot-grid" style="width: 100%%; height: 6.5in; border-radius: 4px;"></div>
  <div class="page-footer">
    <span>Astronomy Observation Journal</span>
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
    <div style="font-size: 18pt; font-weight: 700; color: #ffffff; margin-bottom: 10px;">The Sky Is Always There</div>
    <div class="accent-bar"></div>
    <div class="subtitle" style="font-size: 10pt; color: #6A9AAA; font-style: italic;">
      Every clear night is a gift.<br>Look up. Wonder. Record.
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
    pages.append(magnitude_reference())            # 4: Magnitude
    pages.append(messier_reference())              # 5: Messier objects
    pages.append(telescope_reference())            # 6: Telescopes
    pages.append(bortle_reference())               # 7: Bortle scale
    pages.append(seeing_reference())               # 8: Seeing & transparency

    # ---- Section 1: Observation Logs ----
    pages.append(divider_section(1, "One", "Observation Logs", "40 detailed session logs &mdash; your personal night-sky archive"))
    NUM_OBS = 40
    for i in range(1, NUM_OBS + 1):
        pages.append(observation_log_left(i))
        pages.append(observation_log_right(i))

    # ---- Section 2: Management ----
    pages.append(divider_section(2, "Two", "Planning &amp; Gear", "Wishlist, equipment, and reflection"))
    pages.append(target_wishlist(1, 2))
    pages.append(target_wishlist(2, 2))
    pages.append(gear_inventory())
    pages.append(year_in_review())

    # ---- Section 3: Sketches & Notes ----
    pages.append(divider_section(3, "Three", "Sketches &amp; Notes", "Field drawings and observations"))
    pages.append(sketch_page())
    pages.append(sketch_page())
    for _ in range(4):
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
    print("  Reference (how-to, magnitude, Messier, telescopes, Bortle, seeing): 6")
    print("  Section dividers: 3")
    print("  Observation logs (%d x 2 pages): %d" % (NUM_OBS, NUM_OBS * 2))
    print("  Wishlist: 2")
    print("  Gear inventory: 1")
    print("  Year in review: 1")
    print("  Sketch pages: 2")
    print("  Notes pages: 4")
    print("  Final: 1")
    print("  TOTAL: %d" % total_pages)

    assert total_pages % 2 == 0, "Page count %d is odd — KDP requires even" % total_pages


if __name__ == "__main__":
    main()
