#!/usr/bin/env python3
"""
Golf Log Book — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: American golf enthusiasts
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "golf_log_book_us_V1.0.html")

BOOK_TITLE = "Golf Log Book"
BOOK_SUBTITLE = "Your Ultimate Golf Journal"

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
  color: #1A1A1A;
  background: white;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

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

/* ---- Colors ---- */
/* Golf green dark:   #0D3B20 */
/* Golf green medium: #1A5C38 */
/* Golf green light:  #2d7a4f */
/* Gold accent:       #D4A017 */
/* Gold light:        #E8C84A */
/* Light green bg:    #f0f5f0, #e8f0e8 */
/* Cream:             #fffbf0 */

/* ---- Cover ---- */
.cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(180deg, #0D3B20 0%, #1A5C38 40%, #0D3B20 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Fairway stripes on cover */
.cover .fairway-lines {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image:
    repeating-linear-gradient(
      90deg,
      transparent,
      transparent 40px,
      rgba(255,255,255,0.04) 40px,
      rgba(255,255,255,0.04) 42px
    );
}

/* CSS Golf Ball */
.cover .golf-ball {
  width: 100px; height: 100px;
  background: radial-gradient(circle at 35% 35%, #ffffff 0%, #f0f0f0 55%, #cccccc 100%);
  border-radius: 50%;
  position: relative;
  margin: 0 auto 6px;
  box-shadow: 3px 4px 15px rgba(0,0,0,0.6);
}
.cover .golf-ball::before {
  content: "";
  position: absolute;
  top: 8%; left: 8%; width: 84%; height: 84%;
  border-radius: 50%;
  background-image: radial-gradient(circle, rgba(160,160,160,0.35) 1.5px, transparent 2.5px);
  background-size: 10px 10px;
}
/* Tee under ball */
.cover .tee {
  width: 0; height: 0;
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 16px solid #c4a76d;
  margin: 0 auto 20px;
  position: relative;
}
.cover .tee::after {
  content: "";
  position: absolute;
  top: -16px; left: -4px;
  width: 8px; height: 4px;
  background: #a08850;
  border-radius: 2px 2px 0 0;
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
  line-height: 1.1;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
}

.cover .accent-bar {
  width: 120px; height: 3px;
  background: #D4A017;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 12pt;
  color: #aacbb0;
  font-style: italic;
  line-height: 1.5;
  margin-bottom: 24px;
}

.cover .features {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.cover .feature-badge {
  background: rgba(255,255,255,0.10);
  border: 1px solid rgba(212,160,23,0.5);
  color: #D4A017;
  font-size: 7.5pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 10px;
  border-radius: 3px;
  text-transform: uppercase;
}

.cover .season-tag {
  font-size: 9pt;
  color: #8fbf9f;
  letter-spacing: 2pt;
  text-transform: uppercase;
  margin-top: 10px;
}

.cover .publisher {
  position: absolute;
  bottom: 0.4in;
  left: 0; right: 0;
  text-align: center;
  font-size: 9pt;
  color: #D4A017;
  letter-spacing: 2pt;
  text-transform: uppercase;
  font-weight: 700;
}

/* ---- Section Divider ---- */
.divider {
  width: 6in; height: 9in;
  page-break-after: always;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  background: #1A5C38;
  position: relative;
  overflow: hidden;
}
.divider .div-lines {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: repeating-linear-gradient(90deg,
    transparent, transparent 40px,
    rgba(255,255,255,0.04) 40px, rgba(255,255,255,0.04) 42px);
}
.divider .div-num {
  font-size: 60pt;
  color: rgba(212,160,23,0.12);
  font-weight: 700;
  position: absolute;
  top: 1in;
}
.divider .div-label {
  font-size: 10pt;
  color: #D4A017;
  letter-spacing: 3pt;
  text-transform: uppercase;
  margin-bottom: 10px;
  position: relative;
}
.divider .div-title {
  font-size: 26pt;
  color: #ffffff;
  font-weight: 700;
  line-height: 1.2;
  position: relative;
  padding: 0 0.6in;
}
.divider .div-sub {
  font-size: 11pt;
  color: #8fbf9f;
  font-style: italic;
  margin-top: 14px;
  position: relative;
}

/* ---- Content Pages ---- */
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 7.5pt;
  color: #999;
  padding-bottom: 4px;
  border-bottom: 1.5px solid #1A5C38;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #1A5C38;
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
  color: #1A5C38;
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
  border-bottom: 0.5px solid #c8c8c8;
  height: 22px;
}
.wline-wide {
  border-bottom: 0.5px solid #c8c8c8;
  height: 26px;
}

/* ---- Scorecard Table ---- */
.scorecard {
  width: 100%;
  border-collapse: collapse;
  margin: 2px 0;
  table-layout: fixed;
}
.scorecard th {
  background: #1A5C38;
  color: white;
  font-size: 6.5pt;
  font-weight: 700;
  padding: 3px 1px;
  text-align: center;
}
.scorecard th.sc-hdr {
  background: #0D3B20;
  width: 12%;
}
.scorecard th.sc-total-hdr {
  background: #2d7a4f;
}
.scorecard th.sc-grand-hdr {
  background: #D4A017;
}
.scorecard td {
  border: 0.5px solid #888;
  font-size: 7pt;
  padding: 2px 1px;
  text-align: center;
  height: 20px;
}
.scorecard td.sc-label {
  text-align: left;
  padding-left: 5px;
  font-size: 6pt;
  font-weight: 700;
  color: #1A5C38;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  background: #f0f5f0;
}
.scorecard td.sc-total {
  background: #e8f0e8;
  font-weight: 700;
}
.scorecard td.sc-grand {
  background: #D4A017;
  color: white;
  font-weight: 700;
  font-size: 8pt;
}

/* ---- Stat Tracker Table ---- */
.stat-tracker {
  width: 100%;
  border-collapse: collapse;
  font-size: 7pt;
  margin: 6px 0;
}
.stat-tracker th {
  background: #1A5C38;
  color: white;
  padding: 4px 1px;
  text-align: center;
  font-weight: 700;
  font-size: 6.5pt;
  line-height: 1.2;
}
.stat-tracker td {
  border: 0.5px solid #bbb;
  padding: 3px 2px;
  text-align: center;
  font-size: 7pt;
  height: 20px;
}

/* ---- Club Distance Table ---- */
.club-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 7.5pt;
  margin: 6px 0;
}
.club-table th {
  background: #1A5C38;
  color: white;
  padding: 4px 4px;
  text-align: center;
  font-weight: 700;
  font-size: 7pt;
}
.club-table td {
  border: 0.5px solid #bbb;
  padding: 4px 4px;
  text-align: center;
  font-size: 7.5pt;
  height: 20px;
}
.club-table td.club-name {
  text-align: left;
  padding-left: 8px;
  font-weight: 700;
  color: #1A5C38;
  font-size: 7.5pt;
}

/* ---- Course Log Table ---- */
.course-log {
  width: 100%;
  border-collapse: collapse;
  font-size: 7pt;
  margin: 6px 0;
}
.course-log th {
  background: #1A5C38;
  color: white;
  padding: 4px 2px;
  text-align: center;
  font-weight: 700;
  font-size: 6.5pt;
}
.course-log td {
  border: 0.5px solid #bbb;
  padding: 3px 2px;
  text-align: center;
  font-size: 7pt;
  height: 22px;
}

/* ---- Field Labels ---- */
.field-label {
  font-size: 7.5pt;
  font-weight: 700;
  color: #1A5C38;
  text-transform: uppercase;
  letter-spacing: 0.8pt;
  margin-bottom: 3px;
  margin-top: 8px;
}
.field-label .small-note {
  font-weight: 400;
  text-transform: none;
  letter-spacing: 0;
  color: #aaa;
  font-style: italic;
  font-size: 6.5pt;
  float: right;
}

.fill-blank {
  border-bottom: 0.5px solid #999;
  height: 16px;
  display: inline-block;
}

/* ---- Checkbox ---- */
.checkbox {
  display: inline-block;
  width: 10px; height: 10px;
  border: 1px solid #555;
  border-radius: 2px;
  margin-right: 4px;
  vertical-align: middle;
}
.checkbox-row {
  font-size: 8pt;
  color: #555;
  margin: 4px 0;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.checkbox-row span {
  display: flex;
  align-items: center;
  white-space: nowrap;
}

/* ---- Star Rating ---- */
.stars {
  font-size: 14pt;
  color: #ccc;
  letter-spacing: 3pt;
}

/* ---- Owner Page ---- */
.owner-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100%;
}
.owner-page .owner-icon {
  width: 50px; height: 50px;
  background: radial-gradient(circle at 35% 35%, #ffffff 0%, #e0e0e0 60%, #b8b8b8 100%);
  border-radius: 50%;
  margin: 0 auto 20px;
  position: relative;
  box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
}
.owner-page .owner-icon::before {
  content: "";
  position: absolute;
  top: 10%; left: 10%; width: 80%; height: 80%;
  border-radius: 50%;
  background-image: radial-gradient(circle, rgba(160,160,160,0.3) 1px, transparent 1.8px);
  background-size: 7px 7px;
}
.owner-page .owner-title {
  font-size: 20pt;
  font-weight: 700;
  color: #1A5C38;
  margin-bottom: 6px;
}
.owner-page .owner-sub {
  font-size: 9pt;
  color: #888;
  font-style: italic;
  margin-bottom: 30px;
}
.owner-line {
  width: 4in;
  margin: 10px auto;
  text-align: left;
}
.owner-line .ol-label {
  font-size: 8pt;
  font-weight: 700;
  color: #1A5C38;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  margin-bottom: 2px;
}
.owner-line .ol-blank {
  border-bottom: 1px solid #999;
  height: 20px;
}

/* ---- Back Cover ---- */
.back-cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: auto;
  background: linear-gradient(180deg, #0D3B20 0%, #1A5C38 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.back-cover .bc-lines {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: repeating-linear-gradient(90deg,
    transparent, transparent 40px,
    rgba(255,255,255,0.04) 40px, rgba(255,255,255,0.04) 42px);
}
.back-cover .bc-content {
  position: relative;
  z-index: 2;
  padding: 0 0.6in;
}
.back-cover .bc-title {
  font-size: 16pt;
  color: #D4A017;
  font-weight: 700;
  margin-bottom: 12px;
  letter-spacing: 1pt;
}
.back-cover .bc-text {
  font-size: 9pt;
  color: #aacbb0;
  line-height: 1.8;
  margin-bottom: 20px;
}
.back-cover .bc-features {
  text-align: left;
  margin: 0 auto 24px;
  max-width: 3.5in;
}
.back-cover .bc-features li {
  list-style: none;
  font-size: 8pt;
  color: #e0e0e0;
  margin: 5px 0;
}
.back-cover .bc-features li::before {
  content: "\25B8 ";
  color: #D4A017;
}
.back-cover .bc-publisher {
  font-size: 9pt;
  color: #D4A017;
  letter-spacing: 2pt;
  text-transform: uppercase;
  font-weight: 700;
}
"""

# ============================================================
# HELPER FUNCTIONS
# ============================================================
def esc(s):
    return H.escape(str(s))

def footer(text=BOOK_TITLE):
    return f'<div class="page-footer"><span></span><span>{esc(text)}</span></div>'

def sh(left, right=""):
    return f'<div class="section-header"><span class="sh-left">{esc(left)}</span><span class="sh-right">{esc(right)}</span></div>'

def writing_lines(n, wide=False):
    cls = "wline-wide" if wide else "wline"
    return "\n".join(f'<div class="{cls}"></div>' for _ in range(n))

def page_open(sec_left, sec_right, title=None, subtitle=None):
    pnum = pn()
    html = f'<div class="page">{sh(sec_left, sec_right)}'
    if title:
        html += f'<div class="page-title">{esc(title)}</div>'
    if subtitle:
        html += f'<div class="page-subtitle">{esc(subtitle)}</div>'
    return html, pnum

def scorecard_table(holes, total_labels):
    """Generate a scorecard table for given holes with total columns."""
    html = '<table class="scorecard">\n'
    # Header row
    html += '<tr><th class="sc-hdr"></th>'
    for h in holes:
        html += f'<th>{h}</th>'
    for tl in total_labels:
        cls = 'sc-grand-hdr' if tl == 'TOT' else 'sc-total-hdr'
        html += f'<th class="{cls}">{tl}</th>'
    html += '</tr>\n'
    # Data rows
    for label in ['PAR', 'YDS', 'SCR', 'PUT']:
        html += f'<tr><td class="sc-label">{label}</td>'
        for _ in holes:
            html += '<td></td>'
        for tl in total_labels:
            cls = 'sc-grand' if tl == 'TOT' else 'sc-total'
            html += f'<td class="{cls}"></td>'
        html += '</tr>\n'
    html += '</table>\n'
    return html

# ============================================================
# PAGE BUILDERS
# ============================================================

def build_cover():
    pn()
    return '''<div class="cover">
  <div class="fairway-lines"></div>
  <div class="title-block">
    <div class="golf-ball"></div>
    <div class="tee"></div>
    <div class="main-title">GOLF<br/>LOG BOOK</div>
    <div class="accent-bar"></div>
    <div class="subtitle">Your Ultimate Golf Journal<br/>for Every Round You Play</div>
    <div class="features">
      <span class="feature-badge">18-Hole Scorecards</span>
      <span class="feature-badge">Round Stats</span>
      <span class="feature-badge">Club Distances</span>
      <span class="feature-badge">Handicap Tracker</span>
    </div>
    <div class="season-tag">&#9733; Track Every Round &#9733;</div>
  </div>
  <div class="publisher">More Shine Press</div>
</div>'''

def build_back_cover():
    pn()
    return '''<div class="back-cover">
  <div class="bc-lines"></div>
  <div class="bc-content">
    <div class="bc-title">&#9733; The Perfect Gift for Golfers &#9733;</div>
    <p class="bc-text">Whether you're a weekend warrior or a dedicated player chasing a single-digit handicap, this log book helps you record every round and spot the patterns that lead to better scores.</p>
    <ul class="bc-features">
      <li>Track 40 rounds with full 18-hole scorecards</li>
      <li>Monitor fairways, GIR, putts, and penalties</li>
      <li>Record club distances for smarter club selection</li>
      <li>Log courses played with rating and slope</li>
      <li>Track your handicap round by round</li>
      <li>Set goals, log practice sessions, and reflect on your season</li>
    </ul>
    <p class="bc-text" style="font-style:italic;">Tee it high and let it fly — your best rounds start here!</p>
  </div>
  <div class="bc-publisher">More Shine Press</div>
</div>'''

def build_owner_page():
    pn()
    return f'''<div class="page">
<div class="owner-page">
  <div class="owner-icon"></div>
  <div class="owner-title">This Log Book Belongs To</div>
  <div class="owner-sub">Fill in your details below</div>
  <div class="owner-line">
    <div class="ol-label">Name</div>
    <div class="ol-blank"></div>
  </div>
  <div class="owner-line">
    <div class="ol-label">Home Course</div>
    <div class="ol-blank"></div>
  </div>
  <div class="owner-line">
    <div class="ol-label">Current Handicap</div>
    <div class="ol-blank"></div>
  </div>
  <div class="owner-line">
    <div class="ol-label">Season / Year</div>
    <div class="ol-blank"></div>
  </div>
</div>
</div>'''

def build_how_to_use():
    pn()
    tips = [
        ("Round Scorecards", "Use one page per round. Fill in par, yardage, your strokes, and putts for each hole. The Front 9 and Back 9 tables give you a clean scorecard for all 18 holes."),
        ("Round Statistics", "After each round, log your fairways hit, GIR, putts, penalties, and sand saves. Over the season, these numbers reveal exactly what to practice."),
        ("Club Distances", "Fill in your average carry and total distance for every club. This chart helps you make confident club choices on the course."),
        ("Course Log & Handicap", "Record every course you play with its rating and slope. Track your score differentials to monitor your handicap progress all year."),
    ]
    html = f'''<div class="page">
{sh("Getting Started", "How to Use This Log Book")}
<div class="page-title">How to Use This Log Book</div>
<div class="page-subtitle">A quick guide to getting the most out of your golf journal</div>
'''
    for i, (title, desc) in enumerate(tips, 1):
        html += f'''<div style="margin-bottom: 12px;">
<div style="display:flex; align-items:baseline; margin-bottom:2px;">
<span style="font-size:14pt; font-weight:700; color:#D4A017; margin-right:6px;">{i}</span>
<span style="font-size:10pt; font-weight:700; color:#1A5C38;">{esc(title)}</span>
</div>
<p style="font-size:8pt; color:#555; line-height:1.6; padding-left:20px;">{esc(desc)}</p>
</div>'''

    html += f'''<div style="margin-top:16px; padding:10px; background:#f0f5f0; border-left:3px solid #D4A017;">
<div style="font-size:7.5pt; font-weight:700; color:#1A5C38; text-transform:uppercase; letter-spacing:0.8pt; margin-bottom:5px;">Pro Tip</div>
<p style="font-size:8pt; color:#555; line-height:1.5;">Fill in your scorecard right after each hole while it's fresh. Note what went well and what didn't. By season's end, you'll see exactly where to focus your practice for next year!</p>
</div>
{footer()}
</div>'''
    return html

def build_my_courses():
    pn()
    return f'''<div class="page">
{sh("My Season", "My Courses")}
<div class="page-title">My Home Courses</div>
<div class="page-subtitle">Record the courses you play regularly</div>

<div class="field-label">Home Course</div>
{writing_lines(1)}

<div class="field-label">Courses I Play Regularly</div>
{writing_lines(3)}

<div class="field-label">Courses I Want to Play</div>
{writing_lines(3)}

<div class="field-label">My Regular Playing Partners</div>
{writing_lines(3)}

<div class="field-label">Favorite Golf Traditions</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">Early mornings? Weekend skins games? Post-round meals?</div>
{writing_lines(3)}

<div class="field-label">This Season, I'm Most Excited About...</div>
{writing_lines(3)}

{footer()}
</div>'''

def build_season_goals():
    pn()
    html = f'''<div class="page">
{sh("My Season", "Goals & Predictions")}
<div class="page-title">Season Goals &amp; Predictions</div>
<div class="page-subtitle">Set your targets before the season starts — check back at the end!</div>

<div class="field-label">My Target Handicap</div>
{writing_lines(1)}

<div class="field-label">My Target Average Score</div>
{writing_lines(1)}

<div class="field-label">Number of Rounds I Plan to Play</div>
{writing_lines(1)}

<div class="field-label">Courses I Want to Play This Year</div>
{writing_lines(2)}

<div class="field-label">Tournament / Event Goals</div>
{writing_lines(2)}

<div class="field-label">Bold Prediction for This Season</div>
{writing_lines(2)}

<div class="field-label">Stat Goals</div>
<table style="width:100%; font-size:8pt; border-collapse:collapse; margin-top:4px;">
<tr style="background:#1A5C38; color:white;">
<th style="padding:3px; text-align:left; font-size:7pt;">Focus Area</th>
<th style="padding:3px; font-size:7pt;">Current</th>
<th style="padding:3px; font-size:7pt;">Goal</th>
<th style="padding:3px; font-size:7pt;">Achieved?</th>
</tr>'''
    areas = ["Fairway Accuracy %", "Greens in Regulation", "Avg Putts per Round", "Sand Saves", "Scrambling %"]
    for area in areas:
        html += f'<tr><td style="border:0.5px solid #ddd; height:20px; font-size:7pt; font-weight:700; color:#1A5C38;">{area}</td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td></tr>'
    html += f'''</table>

{footer()}
</div>'''
    return html

def build_golf_terms_ref():
    pn()
    html = f'''<div class="page">
{sh("Reference", "Golf Terms")}
<div class="page-title">Common Golf Terms</div>
<div class="page-subtitle">A quick reference guide</div>
'''
    categories = [
        ("Scoring", [
            ("Ace", "Hole-in-one on a single stroke"),
            ("Eagle", "Two strokes under par"),
            ("Birdie", "One stroke under par"),
            ("Par", "The expected number of strokes for a hole"),
            ("Bogey", "One stroke over par"),
            ("Double Bogey", "Two strokes over par"),
        ]),
        ("Course Features", [
            ("Tee Box", "The starting area for each hole"),
            ("Fairway", "Short-cut grass between tee and green"),
            ("Rough", "Longer grass bordering the fairway"),
            ("Green", "The smooth putting surface around the hole"),
            ("Fringe", "Slightly longer grass at the green edge"),
            ("Bunker", "A sand hazard (also called a trap)"),
        ]),
        ("Key Statistics", [
            ("FIR", "Fairway in Regulation — tee shot lands in fairway"),
            ("GIR", "Green in Regulation — on the green putting for birdie or better"),
            ("Scrambling", "Making par or better after missing the green"),
            ("Sand Save", "Up-and-down from a bunker for par or better"),
            ("Up &amp; Down", "Chip onto green then one putt"),
            ("Stroke Play", "Total strokes per round; lowest score wins"),
        ]),
    ]

    for category, items in categories:
        html += f'<div class="field-label" style="margin-top:4px;">{esc(category)}</div>'
        html += '<table style="width:100%; font-size:7pt; border-collapse:collapse;">'
        for term, desc in items:
            html += f'<tr><td style="border:0.5px solid #aaa; background:#e8f0e8; padding:2px 5px; font-weight:700; font-size:6.5pt; color:#1A5C38; width:20%;">{term}</td><td style="border:0.5px solid #aaa; padding:2px 5px; font-size:6.5pt; height:14px;">{desc}</td></tr>'
        html += '</table>'

    html += f'''
<div class="field-label" style="margin-top:10px;">Course Rating &amp; Slope</div>
<div style="font-size:7pt; color:#555; line-height:1.6; padding:6px; background:#f0f5f0; border-left:3px solid #D4A017;">
<strong>Course Rating:</strong> Expected score for a scratch golfer on that course.<br/>
<strong>Slope Rating:</strong> Relative difficulty for a bogey golfer (113 = average). Higher slope means harder for average players.
</div>

{footer()}
</div>'''
    return html

def build_game_formats_ref():
    pn()
    html = f'''<div class="page">
{sh("Reference", "Game Formats")}
<div class="page-title">Golf Game Formats &amp; Betting</div>
<div class="page-subtitle">Common games to play with your group</div>
'''
    games = [
        ("Match Play", "Lowest score on each hole wins that hole. Match is won when one player is more holes up than holes remaining."),
        ("Stroke Play", "Total strokes for the entire round. Lowest total wins. The most common format."),
        ("Skins", "Each hole is worth a skin. Lowest score wins it. Ties carry the skin to the next hole."),
        ("Nassau", "Three separate bets: front 9, back 9, and total 18. Each can be won or lost independently."),
        ("Best Ball", "Each player plays their own ball. The best score on the team counts for each hole."),
        ("Scramble", "All team members tee off, pick the best shot, and all play from there. Repeat to the hole."),
        ("Wolf", "Players rotate as the Wolf who chooses a partner (or plays alone) after each drive."),
        ("Stableford", "Points by score per hole: eagle (4), birdie (3), par (2), bogey (1). Highest total wins."),
    ]

    for name, desc in games:
        html += f'''<div style="margin-bottom:8px;">
<div style="font-size:8pt; font-weight:700; color:#1A5C38; margin-bottom:1px;">&#9733; {esc(name)}</div>
<div style="font-size:7pt; color:#555; line-height:1.5; padding-left:14px;">{esc(desc)}</div>
</div>'''

    html += f'''
<div class="field-label" style="margin-top:8px;">My Group's Favorite Games</div>
{writing_lines(2)}

<div class="field-label">Weekly Bet / Press Notes</div>
{writing_lines(2)}

{footer()}
</div>'''
    return html

def build_season_calendar():
    pn()
    html = f'''<div class="page">
{sh("Reference", "Season Calendar")}
<div class="page-title">Golf Year at a Glance</div>
<div class="page-subtitle">Mark key dates, tournaments, and events throughout the year</div>
'''
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    for month in months:
        html += f'<div class="field-label" style="margin-top:2px;">{month}</div>'
        html += writing_lines(2)

    html += f'''
<div class="field-label" style="margin-top:8px;">Tournaments &amp; Events to Watch</div>
{writing_lines(2)}

<div class="field-label">Important Golf Dates</div>
{writing_lines(2)}

{footer()}
</div>'''
    return html

def build_divider(part_num, label, title, subtitle):
    pn()
    return f'''<div class="divider">
  <div class="div-lines"></div>
  <div class="div-num">{part_num}</div>
  <div style="position:relative; text-align:center;">
    <div class="div-label">{esc(label)}</div>
    <div class="div-title">{esc(title)}</div>
    <div class="div-sub">{esc(subtitle)}</div>
  </div>
</div>'''

# ============================================================
# CORE PAGE: Round Scorecard
# ============================================================
def build_round_scorecard(round_label):
    html, pnum = page_open(
        "Round Tracker",
        round_label,
        "Round Scorecard",
        "18 holes — record every stroke"
    )

    # Round info bar
    html += f'''
<div style="display:flex; justify-content:space-between; margin-bottom:5px; font-size:7.5pt;">
  <div style="font-weight:700; color:#1A5C38;">{esc(round_label)}</div>
  <div>Date: <span class="fill-blank" style="width:70px;"></span></div>
</div>
<div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:7pt; color:#555;">
  <div>Course: <span class="fill-blank" style="width:90px;"></span></div>
  <div>Tee: <span class="fill-blank" style="width:35px;"></span></div>
  <div>Rating/Slope: <span class="fill-blank" style="width:35px;"></span>/<span class="fill-blank" style="width:25px;"></span></div>
  <div>Weather: <span class="fill-blank" style="width:45px;"></span></div>
</div>
'''
    # Front 9
    html += '<div style="font-size:7pt; font-weight:700; color:#D4A017; text-transform:uppercase; letter-spacing:1pt; margin-bottom:2px;">Front 9</div>\n'
    html += scorecard_table([1,2,3,4,5,6,7,8,9], ['OUT'])

    # Back 9
    html += '<div style="font-size:7pt; font-weight:700; color:#D4A017; text-transform:uppercase; letter-spacing:1pt; margin:4px 0 2px;">Back 9</div>\n'
    html += scorecard_table([10,11,12,13,14,15,16,17,18], ['IN', 'TOT'])

    # Round summary stats
    html += '''
<div style="display:flex; justify-content:space-between; margin-top:6px; font-size:7pt; color:#555;">
  <div>Fairways: <span class="fill-blank" style="width:25px;"></span>/14</div>
  <div>GIR: <span class="fill-blank" style="width:25px;"></span>/18</div>
  <div>Putts: <span class="fill-blank" style="width:30px;"></span></div>
  <div>Penalties: <span class="fill-blank" style="width:25px;"></span></div>
  <div>Sand Saves: <span class="fill-blank" style="width:25px;"></span></div>
</div>
'''
    # Highlights + rating
    html += '''
<div style="display:flex; justify-content:space-between; margin-top:8px;">
  <div style="font-size:7.5pt; font-weight:700; color:#1A5C38;">Best Hole</div>
  <div style="font-size:7.5pt; font-weight:700; color:#1A5C38;">Round Rating</div>
</div>
<div style="display:flex; justify-content:space-between; margin-bottom:4px;">
  <span class="fill-blank" style="width:100px;"></span>
  <span style="font-size:7pt; color:#777;">Score: <span class="fill-blank" style="width:25px;"></span></span>
  <span class="stars">&#9734; &#9734; &#9734; &#9734; &#9734;</span>
</div>
'''
    # Notes
    html += f'''
<div class="field-label">Round Notes <span class="small-note">what worked, what didn't, key moments</span></div>
{writing_lines(3)}

<div style="font-size:7pt; color:#aaa; margin-top:2px;">
  Walking? <span class="checkbox"></span> Yes &nbsp;
  Cart? <span class="checkbox"></span> Yes &nbsp;
  Solo round? <span class="checkbox"></span> Yes &nbsp;
  Tournament? <span class="checkbox"></span> Yes
</div>

{footer()}
</div>'''
    return html

# ============================================================
# Stat Tracker Pages
# ============================================================
def build_stat_tracker(start_round, count=15):
    end_round = min(start_round + count - 1, 40)
    html, pnum = page_open(
        "Round Statistics",
        f"Rounds {start_round}–{end_round}",
        "Stat Tracker",
        "Track key stats round by round to find patterns"
    )

    html += '''<table class="stat-tracker">
<tr>
<th style="width:7%;">Rnd</th>
<th style="width:12%;">Date</th>
<th style="width:20%;">Course</th>
<th style="width:11%;">FWY<br/><span style="font-size:5pt;">x/14</span></th>
<th style="width:11%;">GIR<br/><span style="font-size:5pt;">x/18</span></th>
<th style="width:8%;">PUTT</th>
<th style="width:7%;">SND</th>
<th style="width:7%;">PEN</th>
<th style="width:9%;">SCR</th>
<th style="width:8%;">+/-</th>
</tr>'''

    actual_count = end_round - start_round + 1
    for i in range(actual_count):
        rnd = start_round + i
        html += f'<tr><td style="font-weight:700; color:#1A5C38;">{rnd}</td>'
        html += '<td></td><td style="text-align:left; font-size:6.5pt;"></td>'
        html += '<td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>\n'

    html += '</table>\n'

    html += '''
<div style="font-size:6pt; color:#aaa; margin-top:4px; line-height:1.6;">
FWY = Fairways Hit &nbsp;|&nbsp; GIR = Greens in Regulation &nbsp;|&nbsp; PUTT = Total Putts &nbsp;|&nbsp; SND = Sand Saves &nbsp;|&nbsp; PEN = Penalty Strokes &nbsp;|&nbsp; SCR = Total Score &nbsp;|&nbsp; +/- = Over/Under Par
</div>
'''
    html += f'''
<div class="field-label">Notes &amp; Trends</div>
{writing_lines(3)}

{footer()}
</div>'''
    return html

def build_stat_summary():
    html, pnum = page_open(
        "Round Statistics",
        "Season Summary",
        "Season Stat Summary",
        "Your key stats at a glance"
    )

    categories = [
        ("Scoring", [
            ("Total Rounds Played", ""),
            ("Average Score (18 holes)", ""),
            ("Best Round", ""),
            ("Average Score vs Par", ""),
        ]),
        ("Driving", [
            ("Average Fairways Hit", "/ 14"),
            ("Fairway Accuracy", "%"),
            ("Average Driving Distance", "yds"),
        ]),
        ("Approach & Greens", [
            ("Average GIR", "/ 18"),
            ("GIR Percentage", "%"),
        ]),
        ("Short Game & Putting", [
            ("Average Putts per Round", ""),
            ("Average Putts per GIR", ""),
            ("Sand Saves", "of attempts"),
            ("Scrambling", "%"),
        ]),
        ("Mistakes", [
            ("Avg Penalty Strokes per Round", ""),
            ("Rounds with Zero Penalties", ""),
            ("Most Common Trouble", ""),
        ]),
    ]

    for cat_name, items in categories:
        html += f'<div class="field-label" style="margin-top:6px;">{esc(cat_name)}</div>'
        html += '<table style="width:100%; font-size:7.5pt; border-collapse:collapse;">'
        for stat, unit in items:
            html += f'<tr><td style="border:0.5px solid #ddd; padding:3px 5px; font-size:7pt; width:60%;">{esc(stat)}</td><td style="border:0.5px solid #ddd; height:18px; width:25%;"></td><td style="border:0.5px solid #ddd; font-size:6.5pt; color:#aaa; width:15%;">{esc(unit)}</td></tr>'
        html += '</table>'

    html += f'''
<div class="field-label" style="margin-top:8px;">Biggest Strength This Season</div>
{writing_lines(2)}

<div class="field-label">Area to Improve Next Season</div>
{writing_lines(2)}

{footer()}
</div>'''
    return html

# ============================================================
# Club & Equipment Pages
# ============================================================
def build_club_distances():
    html, pnum = page_open(
        "Clubs & Equipment",
        "Club Distances",
        "Club Distance Chart",
        "Know your yardages — the key to better club selection"
    )

    html += '''<table class="club-table">
<tr>
<th style="width:25%;">Club</th>
<th style="width:20%;">Avg Total (yds)</th>
<th style="width:20%;">Avg Carry (yds)</th>
<th style="width:35%;">Notes</th>
</tr>'''

    clubs = [
        "Driver", "3-Wood", "5-Wood", "7-Wood",
        "3-Hybrid", "4-Hybrid", "5-Hybrid",
        "3-Iron", "4-Iron", "5-Iron", "6-Iron",
        "7-Iron", "8-Iron", "9-Iron",
        "Pitching Wedge", "Gap Wedge", "Sand Wedge", "Lob Wedge",
    ]

    for club in clubs:
        html += f'<tr><td class="club-name">{esc(club)}</td><td></td><td></td><td></td></tr>\n'

    html += '</table>\n'

    html += f'''
<div class="field-label">Distance Gap Notes</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">Where are your gaps too large or too small?</div>
{writing_lines(3)}

{footer()}
</div>'''
    return html

def build_bag_setup():
    html, pnum = page_open(
        "Clubs & Equipment",
        "My Bag",
        "What's in My Bag",
        "Record your equipment details"
    )

    fields = [
        ("Driver", "Model / Loft / Shaft"),
        ("Fairway Woods", "Model / Lofts"),
        ("Hybrids", "Model / Lofts"),
        ("Irons", "Model / Set makeup"),
        ("Wedges", "Model / Lofts (PW, GW, SW, LW)"),
        ("Putter", "Model / Length / Type"),
        ("Golf Ball", "Model / Preference"),
        ("Glove", "Model / Size"),
    ]

    for label, hint in fields:
        html += f'<div class="field-label">{esc(label)} <span class="small-note">{esc(hint)}</span></div>'
        html += writing_lines(1)

    html += f'''
<div class="field-label">Bag &amp; Accessories</div>
{writing_lines(2)}

<div class="field-label">Equipment Changes &amp; Notes</div>
{writing_lines(3)}

{footer()}
</div>'''
    return html

def build_equipment_notes():
    html, pnum = page_open(
        "Clubs & Equipment",
        "Fitting & Specs",
        "Fitting & Equipment Notes",
        "Track your specs and equipment changes"
    )

    fields = [
        ("Swing Speed (Driver)", ""),
        ("Swing Speed (7-Iron)", ""),
        ("Ball Speed (Driver)", ""),
        ("Shaft Flex", "Regular / Stiff / X-Stiff"),
        ("Shaft Weight", "grams"),
        ("Lie Angle", "Upright / Flat / Standard"),
        ("Driver Loft", "degrees / setting"),
        ("Grip Size", "Standard / Midsize / Oversize"),
    ]

    for label, hint in fields:
        hint_html = f' <span class="small-note">{esc(hint)}</span>' if hint else ''
        html += f'<div class="field-label">{esc(label)}{hint_html}</div>'
        html += writing_lines(1)

    html += f'''
<div class="field-label">Fitting Session Notes</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">Key findings from your last fitting</div>
{writing_lines(3)}

<div class="field-label">Equipment Wishlist</div>
{writing_lines(2)}

{footer()}
</div>'''
    return html

# ============================================================
# Course Log & Handicap Pages
# ============================================================
def build_course_log():
    html, pnum = page_open(
        "Courses & Handicap",
        "Course Log",
        "Courses Played",
        "Record every course you play — build your golf map"
    )

    html += '''<table class="course-log">
<tr>
<th style="width:22%;">Course Name</th>
<th style="width:11%;">Date</th>
<th style="width:9%;">Tees</th>
<th style="width:9%;">Rating</th>
<th style="width:9%;">Slope</th>
<th style="width:9%;">Score</th>
<th style="width:9%;">Diff</th>
<th style="width:22%;">Notes</th>
</tr>'''

    for _ in range(12):
        html += '<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>\n'

    html += '</table>\n'

    html += '''
<div style="font-size:6pt; color:#aaa; margin-top:4px;">
Rating = Course Rating &nbsp;|&nbsp; Slope = Slope Rating &nbsp;|&nbsp; Diff = Score Differential = (Score - Rating) x 113 / Slope
</div>
'''
    html += f'{footer()}\n</div>'
    return html

def build_handicap_tracker():
    html, pnum = page_open(
        "Courses & Handicap",
        "Handicap Index",
        "Handicap Tracker",
        "Track your handicap round by round"
    )

    html += '''<table class="stat-tracker">
<tr>
<th style="width:7%;">Rnd</th>
<th style="width:12%;">Date</th>
<th style="width:20%;">Course</th>
<th style="width:11%;">Rating</th>
<th style="width:10%;">Slope</th>
<th style="width:10%;">Score</th>
<th style="width:14%;">Differential</th>
<th style="width:16%;">Index</th>
</tr>'''

    for i in range(1, 21):
        html += f'<tr><td style="font-weight:700; color:#1A5C38;">{i}</td>'
        html += '<td></td><td style="text-align:left; font-size:6.5pt;"></td>'
        html += '<td></td><td></td><td></td><td></td><td></td></tr>\n'

    html += '</table>\n'

    html += f'''
<div class="field-label">Handicap Progress Notes</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">Your index is typically the average of your best 8 of the last 20 score differentials</div>
{writing_lines(3)}

{footer()}
</div>'''
    return html

# ============================================================
# Practice & Goals Pages
# ============================================================
def build_practice_log():
    html, pnum = page_open(
        "Practice & Goals",
        "Practice Log",
        "Practice Session Log",
        "Track your training and see your improvement"
    )

    html += '''<table class="stat-tracker">
<tr>
<th style="width:12%;">Date</th>
<th style="width:10%;">Time</th>
<th style="width:12%;">Duration</th>
<th style="width:16%;">Focus Area</th>
<th style="width:25%;">Drills / Activities</th>
<th style="width:25%;">Notes</th>
</tr>'''

    for _ in range(14):
        html += '<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>\n'

    html += '</table>\n'

    html += f'''
<div class="field-label">Practice Focus This Period</div>
<div class="checkbox-row">
  <span><span class="checkbox"></span> Driving</span>
  <span><span class="checkbox"></span> Irons</span>
  <span><span class="checkbox"></span> Chipping</span>
  <span><span class="checkbox"></span> Pitching</span>
  <span><span class="checkbox"></span> Bunker</span>
  <span><span class="checkbox"></span> Putting</span>
  <span><span class="checkbox"></span> Course Mgmt</span>
  <span><span class="checkbox"></span> Mental Game</span>
</div>
{footer()}
</div>'''
    return html

def build_goals_tracker():
    html, pnum = page_open(
        "Practice & Goals",
        "Season Goals",
        "Goals Tracker",
        "Set targets and measure your progress"
    )

    goals = [
        ("Target Handicap", "Current: ____ -> Goal: ____"),
        ("Average Score (18 holes)", "Current: ____ -> Goal: ____"),
        ("Fairway Accuracy", "Current: ____% -> Goal: ____%"),
        ("Greens in Regulation", "Current: __/18 -> Goal: __/18"),
        ("Average Putts per Round", "Current: ____ -> Goal: ____"),
        ("Rounds Played This Year", "Goal: ____ rounds"),
    ]

    for label, hint in goals:
        html += f'<div class="field-label">{esc(label)}</div>'
        html += f'<div style="font-size:7pt; color:#aaa; font-style:italic; margin-bottom:2px;">{esc(hint)}</div>'
        html += '<div class="wline"></div>'

    html += f'''
<div class="field-label" style="margin-top:12px;">Mid-Season Check-In</div>
{writing_lines(3)}

<div class="field-label">End-of-Season Review</div>
{writing_lines(3)}

{footer()}
</div>'''
    return html

def build_drills_notes():
    html, pnum = page_open(
        "Practice & Goals",
        "Drills & Training",
        "Drills & Training Notes",
        "Record drills that work and track your progress"
    )

    areas = [
        "Driving Drills",
        "Iron Play Drills",
        "Short Game Drills",
        "Putting Drills",
        "Bunker Play Drills",
        "Course Management Notes",
    ]

    for area in areas:
        html += f'<div class="field-label">{esc(area)}</div>'
        html += writing_lines(2)

    html += f'''
<div class="field-label">Lesson Notes</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">Key takeaways from coaching sessions</div>
{writing_lines(3)}

{footer()}
</div>'''
    return html

# ============================================================
# Season Wrap-Up Pages
# ============================================================
def build_best_rounds():
    html, pnum = page_open(
        "Season Wrap-Up",
        "Best Rounds",
        "Top 5 Rounds",
        "Celebrate your best rounds of the year"
    )

    for i in range(1, 6):
        html += f'''<div style="margin-bottom:14px;">
<div style="display:flex; align-items:baseline;">
  <span style="font-size:14pt; font-weight:700; color:#D4A017; margin-right:8px; min-width:24px;">#{i}</span>
  <span style="font-size:8pt; font-weight:700; color:#1A5C38;">Course:</span>
  <span class="fill-blank" style="width:130px; margin-left:4px;"></span>
  <span style="font-size:8pt; font-weight:700; color:#1A5C38; margin-left:10px;">Score:</span>
  <span class="fill-blank" style="width:35px; margin-left:4px;"></span>
  <span style="font-size:7pt; color:#777; margin-left:4px;">to par</span>
  <span class="fill-blank" style="width:25px; margin-left:4px;"></span>
</div>
<div style="padding-left:32px; font-size:7pt; color:#777; font-style:italic;">What made it great:</div>
<div style="padding-left:32px;"><div class="wline"></div><div class="wline"></div></div>
</div>'''

    html += f'''
<div class="field-label">Best Shot of the Year</div>
{writing_lines(3)}

{footer()}
</div>'''
    return html

def build_season_awards():
    html, pnum = page_open(
        "Season Wrap-Up",
        "My Awards",
        "Season Awards — My Picks",
        "Your personal golf awards for the year"
    )

    awards = [
        "Best Round of the Year",
        "Best Single Hole",
        "Longest Drive",
        "Best Putting Round",
        "Most Improved Area",
        "Best Course I Played",
        "Best Shot of the Year",
        "Toughest Round",
        "Favorite Golf Memory",
        "Playing Partner of the Year",
    ]

    for award in awards:
        html += f'''<div style="margin-bottom:7px;">
<div style="font-size:8pt; font-weight:700; color:#1A5C38; margin-bottom:1px;">&#9733; {esc(award)}</div>
<div class="wline"></div>
</div>'''

    html += f'{footer()}\n</div>'
    return html

def build_season_reflection():
    html, pnum = page_open(
        "Season Wrap-Up",
        "Reflection",
        "Season Reflection",
        "Looking back at your golf year"
    )

    prompts = [
        "My favorite round of the year",
        "The shot I'll never forget",
        "Biggest improvement in my game",
        "What I still need to work on",
        "What I loved most about this golf season",
    ]

    for prompt in prompts:
        html += f'<div class="field-label">{esc(prompt)}</div>\n'
        html += writing_lines(3)

    html += f'{footer()}\n</div>'
    return html

def build_looking_forward():
    html, pnum = page_open(
        "Season Wrap-Up",
        "Looking Ahead",
        "Looking Forward to Next Season",
        "What's on your radar for next year"
    )

    prompts = [
        "My #1 golf goal for next year",
        "Courses I want to play",
        "Part of my game I'll focus on most",
        "Tournaments or events I'm targeting",
        "Something new I want to try in my game",
    ]

    for prompt in prompts:
        html += f'<div class="field-label">{esc(prompt)}</div>\n'
        html += writing_lines(3)

    html += f'{footer()}\n</div>'
    return html

def build_notes_page(title="Notes", subtitle=None):
    html, pnum = page_open("Notes", "", title, subtitle)
    html += writing_lines(26)
    html += f'{footer()}\n</div>'
    return html

# ============================================================
# MAIN
# ============================================================
def main():
    pages = []

    # === FRONT MATTER ===
    pages.append(build_cover())
    pages.append(build_owner_page())
    pages.append(build_how_to_use())
    pages.append(build_my_courses())
    pages.append(build_season_goals())
    pages.append(build_golf_terms_ref())
    pages.append(build_game_formats_ref())
    pages.append(build_season_calendar())

    # === SECTION 1: ROUND TRACKER ===
    pages.append(build_divider("01", "Part One", "Round\nTracker", "One page per round — track every hole"))
    for i in range(1, 41):
        pages.append(build_round_scorecard(f"Round #{i}"))

    # === SECTION 2: ROUND STATISTICS ===
    pages.append(build_divider("02", "Part Two", "Round\nStatistics", "Track your stats and find your game"))
    pages.append(build_stat_tracker(1, 15))
    pages.append(build_stat_tracker(16, 15))
    pages.append(build_stat_tracker(31, 10))
    pages.append(build_stat_summary())

    # === SECTION 3: CLUBS & EQUIPMENT ===
    pages.append(build_divider("03", "Part Three", "Clubs\n& Equipment", "Know your distances and your gear"))
    pages.append(build_club_distances())
    pages.append(build_bag_setup())
    pages.append(build_equipment_notes())

    # === SECTION 4: COURSES & HANDICAP ===
    pages.append(build_divider("04", "Part Four", "Courses\n& Handicap", "Log every course and track your progress"))
    pages.append(build_course_log())
    pages.append(build_course_log())
    pages.append(build_course_log())
    pages.append(build_handicap_tracker())

    # === SECTION 5: PRACTICE & GOALS ===
    pages.append(build_divider("05", "Part Five", "Practice\n& Goals", "Track your training and reach your goals"))
    pages.append(build_practice_log())
    pages.append(build_practice_log())
    pages.append(build_goals_tracker())
    pages.append(build_drills_notes())

    # === SECTION 6: SEASON WRAP-UP ===
    pages.append(build_divider("06", "Part Six", "Season\nWrap-Up", "Celebrate your best rounds and reflect"))
    pages.append(build_best_rounds())
    pages.append(build_season_awards())
    pages.append(build_season_reflection())
    pages.append(build_looking_forward())

    # === SECTION 7: NOTES ===
    pages.append(build_divider("07", "Part Seven", "Personal\nNotes", "Your space for thoughts and memories"))
    for _ in range(26):
        pages.append(build_notes_page())

    # === BACK COVER ===
    pages.append(build_back_cover())

    # === Assemble ===
    body_content = "\n".join(pages)
    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(BOOK_TITLE)} — {esc(BOOK_SUBTITLE)}</title>
<style>{CSS}</style>
</head>
<body>
{body_content}
</body>
</html>'''

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)

    total_pages = page_no[0]
    print(f"Generated: {HTML_FILE}")
    print(f"Total pages: {total_pages}")
    print(f"File size: {os.path.getsize(HTML_FILE):,} bytes")

if __name__ == "__main__":
    main()
