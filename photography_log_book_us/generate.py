#!/usr/bin/env python3
"""
Photography Log Book -- KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Photographers of all levels
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "photography_log_book_us_V1.0.html")

BOOK_TITLE = "Photography Log Book"
BOOK_SUBTITLE = "Capture Every Shot, Every Setting, Every Story"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

def nl(n):
    return "\n".join('<div class="notes-line"></div>' for _ in range(n))

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
@media print { .page { border: none; margin: 0; } }

/* ================ INTERIOR TITLE PAGE ================ */
.cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(165deg, #0D1117 0%, #1A2332 30%, #0D1117 65%, #060A0F 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.cover .glow-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #5B8DB8, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #5B8DB8, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #5B8DB8, transparent);
}

.cover .title-main {
  font-size: 30pt;
  font-weight: 700;
  color: #FAF6F0;
  line-height: 1.2;
  letter-spacing: 0.5pt;
  position: relative;
  z-index: 2;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 100px; height: 2px;
  background: #5B8DB8;
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
  color: #5B8DB8;
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
  color: #0D1117;
  letter-spacing: 0.5pt;
  text-transform: uppercase;
}

.section-line {
  flex: 1;
  height: 1px;
  background: #5B8DB8;
  margin: 0 12px;
  opacity: 0.4;
}

/* ================ HOW TO USE ================ */
.howto-text { font-size: 10pt; line-height: 1.7; }
.howto-text p { margin-bottom: 8px; }
.howto-text .ht-title {
  font-size: 11pt; font-weight: 700; color: #0D1117;
  margin-bottom: 4px; margin-top: 6px;
}
.howto-text .ht-icon { color: #5B8DB8; font-weight: 700; margin-right: 4px; }

/* ================ INFO FIELDS ================ */
.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
  margin-bottom: 8px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #5B8DB8;
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

/* ================ SHOT BANNER ================ */
.shot-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1.5px solid #5B8DB8;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.shot-banner .tb-num {
  display: inline-block;
  border: 1.5px solid #5B8DB8;
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 8pt;
  color: #5B8DB8;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.shot-banner .tb-label {
  font-size: 8pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.shot-banner .tb-line {
  flex: 1;
  height: 12px;
  border-bottom: 1px dotted #ccc;
}

/* ================ TYPE CHECKBOXES ================ */
.type-row {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-bottom: 8px;
}

.type-check {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 7.5pt;
  color: #555;
}

.type-box {
  width: 10px; height: 10px;
  border: 1.5px solid #5B8DB8;
  border-radius: 2px;
}

/* ================ DATA TABLE ================ */
.data-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
}

.data-table th {
  font-size: 6.5pt;
  color: #5B8DB8;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 5px 3px;
  border-bottom: 1.5px solid #5B8DB8;
  text-align: center;
}

.data-table th:first-child { text-align: left; }

.data-table td {
  padding: 4px 3px;
  border-bottom: 1px solid #eee;
  height: 24px;
  font-size: 9pt;
}

/* ================ WRITE BOX ================ */
.write-box {
  border: 1px solid #C4A04A;
  border-radius: 3px;
  padding: 6px 8px;
  margin-bottom: 8px;
}

.write-box .wb-label {
  font-size: 7pt;
  color: #5B8DB8;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 3px;
}

.write-box .wb-area {
  height: 28px;
}

/* ================ METRIC ROWS ================ */
.metric-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 6px 10px;
  margin-bottom: 8px;
}

.metric-field .mf-label {
  font-size: 6.5pt;
  color: #5B8DB8;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  display: block;
  margin-bottom: 1px;
}

.metric-field .mf-write {
  height: 18px;
  border-bottom: 1px dotted #ccc;
}

/* ================ SCORE DOTS ================ */
.score-dots {
  display: flex;
  gap: 4px;
  margin-top: 2px;
}

.score-dot {
  width: 12px; height: 12px;
  border: 1.5px solid #5B8DB8;
  border-radius: 50%;
}

/* ================ NOTES ================ */
.notes-line { border-bottom: 1px solid #ddd; height: 22px; }

/* ================ FINAL PAGE ================ */
.final-page {
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  text-align: center; height: 100%;
}
.final-page .fp-text {
  font-size: 12pt; color: #999; font-style: italic;
  line-height: 1.8; margin-bottom: 20px;
}
.final-page .fp-logo {
  font-size: 11pt; color: #C4A04A;
  letter-spacing: 2.5pt; text-transform: uppercase;
  font-weight: 700;
}
.final-page .fp-line {
  width: 60px; height: 1.5px; background: #5B8DB8;
  margin: 12px auto; opacity: 0.5;
}
"""


def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(50,50)">
        <!-- Camera body -->
        <rect x="-32" y="-16" width="64" height="38" rx="5" fill="none" stroke="#5B8DB8" stroke-width="2"/>
        <!-- Viewfinder hump -->
        <rect x="-12" y="-26" width="24" height="10" rx="2" fill="none" stroke="#5B8DB8" stroke-width="2"/>
        <!-- Lens -->
        <circle cx="0" cy="5" r="13" fill="none" stroke="#C4A04A" stroke-width="2"/>
        <circle cx="0" cy="5" r="8" fill="none" stroke="#5B8DB8" stroke-width="1.5"/>
        <circle cx="0" cy="5" r="3" fill="#C4A04A"/>
        <!-- Shutter button -->
        <circle cx="24" cy="-16" r="3" fill="none" stroke="#C4A04A" stroke-width="1.5"/>
      </g>
    </svg>
  </div>

  <div class="title-main">Photography<br>Log Book</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Capture Every Shot, Every Setting,<br>Every Story</div>

  <div class="pub">More Shine Press</div>
</div>""" % pn()


def how_to_use_page():
    pg = pn()
    return """<!-- PAGE %d: How to Use -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">How to Use This Log Book</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Photographic Journey</div>
    <p>This log book is designed to make you a more intentional and
    deliberate photographer. Every great photographer keeps records --
    not because they enjoy paperwork, but because reviewing past
    shoots is the fastest path to mastering light, composition, and
    technique.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Two-Page Shot Spread</div>
    <p>Each shoot uses a <strong>two-page spread</strong>. The left page
    captures the technical details: date, location, camera body, lens,
    focal length, aperture, shutter speed, ISO, white balance, metering
    mode, and shooting mode. The right page is for your creative notes:
    lighting conditions, weather, composition, what worked, what to
    improve, and the story behind the shot.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Weekly Review</div>
    <p>After every 5 shoots, a <strong>weekly review page</strong> helps
    you identify your best shot of the week, the biggest lesson learned,
    settings to practice, new techniques tried, and your total output.
    This is where skill is built.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips for Best Results</div>
    <p>&#9679; <strong>Log each shoot immediately</strong>, while details
    are still fresh in your mind.</p>
    <p>&#9679; <strong>Be specific with settings.</strong> Exact aperture,
    shutter, and ISO values are how you learn what works.</p>
    <p>&#9679; <strong>Review weekly.</strong> Patterns in light and
    composition emerge over many shoots.</p>
    <p>&#9679; <strong>Note what failed.</strong> Mistakes are the best
    teachers when you write them down.</p>
  </div>
</div>""" % (pg, pg)


def gear_inventory_page():
    pg = pn()
    return """<!-- PAGE %d: Gear Inventory -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Gear Inventory</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Gear Inventory</div>
    <div class="section-line"></div>
  </div>

  <div class="write-box" style="border-color: #5B8DB8;">
    <div class="wb-label">Camera Body / Bodies</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Lenses (Focal Lengths)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Filters</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Tripod</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Flash / Speedlight</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Remote Shutter</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Memory Cards</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Batteries</span><div class="if-write"></div></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Other Accessories (Bag, Strap, Cleaning, etc.)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>
</div>""" % (pg, pg)


def shot_left(entry_num):
    pg = pn()
    modes = ["Manual", "Aperture Priority", "Shutter Priority", "Program", "Auto"]
    mode_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % m
        for m in modes
    )
    metering = ["Matrix", "Center-Weighted", "Spot"]
    meter_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % m
        for m in metering
    )
    return """<!-- PAGE %d: Shot Left #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Shot Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="shot-banner">
    <span class="tb-num">Shot #%03d</span>
    <span class="tb-label">Subject:</span>
    <div class="tb-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Location</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Camera Body</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Lens</span><div class="if-write"></div></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Focal Length (mm)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Aperture (f/)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Shutter Speed</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">ISO</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">White Balance</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Exposure Comp</span><div class="mf-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #5B8DB8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Metering Mode</div>
  <div class="type-row">%s</div>

  <div style="font-size: 7pt; font-weight: 700; color: #5B8DB8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Shooting Mode</div>
  <div class="type-row">%s</div>

  <div class="write-box" style="border-color: #5B8DB8;">
    <div class="wb-label">Additional Settings (Drive Mode, Focus Mode, etc.)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>
</div>""" % (pg, entry_num, pg, entry_num, meter_html, mode_html)


def shot_right():
    pg = pn()
    lighting = ["Natural", "Flash", "Studio", "Mixed"]
    light_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % l
        for l in lighting
    )
    return """<!-- PAGE %d: Shot Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Shot Analysis</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Weather</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Time of Day</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Photo No.</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Subject / Story</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #5B8DB8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Lighting Condition</div>
  <div class="type-row">%s</div>

  <div class="write-box">
    <div class="wb-label">Composition Notes (Framing, Angle, Depth of Field)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #5B8DB8;">
    <div class="wb-label">What Worked Well</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #C0392B;">
    <div class="wb-label">What to Improve</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #C4A04A;">
    <div class="wb-label">The Story Behind This Shot</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 6px;">
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #5B8DB8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Keepers / Total Shots</div>
      <div style="border-bottom: 1px dotted #ccc; height: 18px;"></div>
    </div>
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #5B8DB8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Shot Satisfaction</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Poor &#160; 5 = Excellent</div>
    </div>
  </div>
</div>""" % (pg, pg, light_html)


def weekly_review_page(review_num):
    pg = pn()
    return """<!-- PAGE %d: Weekly Review #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Weekly Review</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="shot-banner">
    <span class="tb-num">Review #%02d</span>
    <span class="tb-label">Week of:</span>
    <div class="tb-line"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Total Shoots</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Total Shots Taken</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Keepers</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Favorite Focal Length</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Most Used Aperture</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Most Used ISO</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #5B8DB8;">
    <div class="wb-label">Best Shot of the Week (What Made It Work)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #C0392B;">
    <div class="wb-label">Biggest Lesson This Week</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Settings to Practice</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #5B8DB8;">
    <div class="wb-label">New Techniques Tried</div>
    <div class="wb-area"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-top: 4px;">
    <div>
      <div style="font-size: 6.5pt; font-weight: 700; color: #5B8DB8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Lighting Skills</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
    </div>
    <div>
      <div style="font-size: 6.5pt; font-weight: 700; color: #5B8DB8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Composition Skills</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
    </div>
    <div>
      <div style="font-size: 6.5pt; font-weight: 700; color: #5B8DB8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Technical Control</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
    </div>
  </div>
</div>""" % (pg, review_num, pg, review_num)


def location_directory_page():
    pg = pn()
    return """<!-- PAGE %d: Location Directory -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Location Directory</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Location Name</th>
        <th>Best Time to Shoot</th>
        <th>Access Notes</th>
        <th>Shots Taken</th>
      </tr>
    </thead>
    <tbody>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>
</div>""" % (pg, pg)


def monthly_summary_page():
    pg = pn()
    return """<!-- PAGE %d: Monthly Summary -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Monthly Summary</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Month / Year</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Total Shoots</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Total Shots Taken</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Keepers</span><div class="if-write"></div></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Top Focal Length</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Top Aperture</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Gear Used Most</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Best Lighting Used</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Locations Visited</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">New Techniques</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #5B8DB8;">
    <div class="wb-label">Favorite Shots This Month (What Made Them Stand Out)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box" style="border-color: #C0392B;">
    <div class="wb-label">Techniques That Need Work</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #5B8DB8;">
    <div class="wb-label">Goals for Next Month</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Notes / Observations</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>
</div>""" % (pg, pg)


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
      Great photographs are made, not taken.<br>
      Every shoot is a lesson.<br>
      Observe. Experiment. Create.
    </div>
    <div class="fp-line"></div>
    <div class="fp-logo">More Shine Press</div>
    <div class="fp-line"></div>
  </div>
</div>""" % pg


def generate(output_path=HTML_FILE):
    pages = []
    pages.append(interior_title_page())       # 1
    pages.append(how_to_use_page())           # 2
    pages.append(gear_inventory_page())       # 3

    # 25 shot logs (50 pages), with a weekly review every 5 shoots
    shot_count = 0
    review_count = 0
    for entry in range(1, 26):
        pages.append(shot_left(entry))
        pages.append(shot_right())
        shot_count += 1
        # Insert weekly review after every 5th shoot
        if shot_count % 5 == 0:
            review_count += 1
            pages.append(weekly_review_page(review_count))

    # Location Directory (2 pages)
    for _ in range(2):
        pages.append(location_directory_page())

    # Monthly summary (2 pages)
    for _ in range(2):
        pages.append(monthly_summary_page())

    # Notes (3 pages)
    for _ in range(3):
        pages.append(notes_page())

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
