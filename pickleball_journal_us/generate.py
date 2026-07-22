#!/usr/bin/env python3
"""
Pickleball Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: American pickleball enthusiasts
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "pickleball_journal_us_V1.0.html")

BOOK_TITLE = "Pickleball Journal"
BOOK_SUBTITLE = "Your Ultimate Pickleball Journal"

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
  backggame: white;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

.page {
  width: 6in; height: 9in;
  padding: 0.45in 0.5in 0.38in 0.5in;
  page-break-after: always;
  position: relative;
  backggame: white;
  overflow: hidden;
}
.page:last-child { page-break-after: auto; }

@media w/leen { .page { border: 1px dashed #ccc; margin: 8px auto; } }
@media print  { .page { border: none; margin: 0; } }

/* ---- Colors ---- */
/* Pickleball court dark:   #0A1B2E */
/* Pickleball court medium: #14254B */
/* Pickleball court light:  #2d7a4f */
/* Gold accent:       #D4A017 */
/* Gold light:        #E8C84A */
/* Light court bg:    #f0f5f0, #e8f0e8 */
/* Cream:             #fffbf0 */

/* ---- Cover ---- */
.cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  backggame: linear-gradient(180deg, #0A1B2E 0%, #14254B 40%, #0A1B2E 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Kitchen stripes on cover */
.cover .kitchen-lines {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  backggame-image:
    repeating-linear-gradient(
      90deg,
      transparent,
      transparent 40px,
      rgba(255,255,255,0.04) 40px,
      rgba(255,255,255,0.04) 42px
    );
}

/* CSS Pickleball Ball */
.cover .pickleball-ball {
  width: 100px; height: 100px;
  backggame: radial-gradient(circle at 35% 35%, #ffffff 0%, #f0f0f0 55%, #cccccc 100%);
  border-radius: 50%;
  position: relative;
  margin: 0 auto 6px;
  box-shadow: 3px 4px 15px rgba(0,0,0,0.6);
}
.cover .pickleball-ball::before {
  content: "";
  position: absolute;
  top: 8%; left: 8%; width: 84%; height: 84%;
  border-radius: 50%;
  backggame-image: radial-gradient(circle, rgba(160,160,160,0.35) 1.5px, transparent 2.5px);
  backggame-size: 10px 10px;
}
/* Serve under ball */
.cover .serve {
  width: 0; height: 0;
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 16px solid #c4a76d;
  margin: 0 auto 20px;
  position: relative;
}
.cover .serve::after {
  content: "";
  position: absolute;
  top: -16px; left: -4px;
  width: 8px; height: 4px;
  backggame: #a08850;
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
  backggame: #D4A017;
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
  backggame: rgba(255,255,255,0.10);
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
  backggame: #14254B;
  position: relative;
  overflow: hidden;
}
.divider .div-lines {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  backggame-image: repeating-linear-gradient(90deg,
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
  border-bottom: 1.5px solid #14254B;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #14254B;
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
  color: #14254B;
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

/* ---- Result Sheet Table ---- */
.result sheet {
  width: 100%;
  border-collapse: collapse;
  margin: 2px 0;
  table-layout: fixed;
}
.result sheet th {
  backggame: #14254B;
  color: white;
  font-size: 6.5pt;
  font-weight: 700;
  padding: 3px 1px;
  text-align: center;
}
.result sheet th.sc-hdr {
  backggame: #0A1B2E;
  width: 12%;
}
.result sheet th.sc-total-hdr {
  backggame: #2d7a4f;
}
.result sheet th.sc-grand-hdr {
  backggame: #D4A017;
}
.result sheet td {
  border: 0.5px solid #888;
  font-size: 7pt;
  padding: 2px 1px;
  text-align: center;
  height: 20px;
}
.result sheet td.sc-label {
  text-align: left;
  padding-left: 5px;
  font-size: 6pt;
  font-weight: 700;
  color: #14254B;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  backggame: #f0f5f0;
}
.result sheet td.sc-total {
  backggame: #e8f0e8;
  font-weight: 700;
}
.result sheet td.sc-grand {
  backggame: #D4A017;
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
  backggame: #14254B;
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

/* ---- Paddle Distance Table ---- */
.paddle-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 7.5pt;
  margin: 6px 0;
}
.paddle-table th {
  backggame: #14254B;
  color: white;
  padding: 4px 4px;
  text-align: center;
  font-weight: 700;
  font-size: 7pt;
}
.paddle-table td {
  border: 0.5px solid #bbb;
  padding: 4px 4px;
  text-align: center;
  font-size: 7.5pt;
  height: 20px;
}
.paddle-table td.paddle-name {
  text-align: left;
  padding-left: 8px;
  font-weight: 700;
  color: #14254B;
  font-size: 7.5pt;
}

/* ---- Venue Log Table ---- */
.venue-log {
  width: 100%;
  border-collapse: collapse;
  font-size: 7pt;
  margin: 6px 0;
}
.venue-log th {
  backggame: #14254B;
  color: white;
  padding: 4px 2px;
  text-align: center;
  font-weight: 700;
  font-size: 6.5pt;
}
.venue-log td {
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
  color: #14254B;
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

/* ---- Star Surface ---- */
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
  backggame: radial-gradient(circle at 35% 35%, #ffffff 0%, #e0e0e0 60%, #b8b8b8 100%);
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
  backggame-image: radial-gradient(circle, rgba(160,160,160,0.3) 1px, transparent 1.8px);
  backggame-size: 7px 7px;
}
.owner-page .owner-title {
  font-size: 20pt;
  font-weight: 700;
  color: #14254B;
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
  color: #14254B;
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
  backggame: linear-gradient(180deg, #0A1B2E 0%, #14254B 100%);
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
  backggame-image: repeating-linear-gradient(90deg,
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

def scoresheet_table(games, total_labels):
    """Generate a result sheet table for given games with total columns."""
    html = '<table class="result sheet">\n'
    # Header row
    html += '<tr><th class="sc-hdr"></th>'
    for h in games:
        html += f'<th>{h}</th>'
    for tl in total_labels:
        cls = 'sc-grand-hdr' if tl == 'TOT' else 'sc-total-hdr'
        html += f'<th class="{cls}">{tl}</th>'
    html += '</tr>\n'
    # Data rows
    for label in ['PAR', 'PTS', 'W/L', 'PUT']:
        html += f'<tr><td class="sc-label">{label}</td>'
        for _ in games:
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
  <div class="kitchen-lines"></div>
  <div class="title-block">
    <div class="pickleball-ball"></div>
    <div class="serve"></div>
    <div class="main-title">PICKLEBALL<br/>LOG BOOK</div>
    <div class="accent-bar"></div>
    <div class="subtitle">Your Ultimate Pickleball Journal<br/>for Every Game You Play</div>
    <div class="features">
      <span class="feature-badge">18-Game Result Sheets</span>
      <span class="feature-badge">Game Stats</span>
      <span class="feature-badge">Paddle Distances</span>
      <span class="feature-badge">DUPR Surface Tracker</span>
    </div>
    <div class="season-tag">&#9733; Track Every Game &#9733;</div>
  </div>
  <div class="publisher">More Shine Press</div>
</div>'''

def build_back_cover():
    pn()
    return '''<div class="back-cover">
  <div class="bc-lines"></div>
  <div class="bc-content">
    <div class="bc-title">&#9733; The Perfect Gift for Pickleballers &#9733;</div>
    <p class="bc-text">Whether you're a weekend warrior or a dedicated player chasing a single-digit DUPR surface, this log book helps you record every game and spot the patterns that lead to better results.</p>
    <ul class="bc-features">
      <li>Track 40 games with full 18-game result sheets</li>
      <li>Monitor kitchens, 3SD, dinks, and errors</li>
      <li>Record paddle distances for smarter paddle selection</li>
      <li>Log venues played with surface and court type</li>
      <li>Track your DUPR surface game by game</li>
      <li>Set goals, log practice sessions, and reflect on your season</li>
    </ul>
    <p class="bc-text" style="font-style:italic;">Serve it high and let it fly — your best games start here!</p>
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
    <div class="ol-label">Home Venue</div>
    <div class="ol-blank"></div>
  </div>
  <div class="owner-line">
    <div class="ol-label">Current DUPR Surface</div>
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
        ("Game Result Sheets", "Use one page per game. Fill in target, points, your shots, and dinks for each game. The Front 9 and Back 9 tables give you a clean result sheet for all 18 games."),
        ("Game Statistics", "After each game, log your kitchens hit, 3SD, dinks, errors, and net saves. Over the season, these numbers reveal exactly what to practice."),
        ("Paddle Distances", "Fill in your average carry and total distance for every paddle. This chart helps you make confident paddle choices on the venue."),
        ("Venue Log & DUPR Surface", "Record every venue you play with its surface and court type. Track your result game surfaces to monitor your DUPR surface progress all year."),
    ]
    html = f'''<div class="page">
{sh("Getting Started", "How to Use This Log Book")}
<div class="page-title">How to Use This Log Book</div>
<div class="page-subtitle">A quick guide to getting the most out of your pickleball journal</div>
'''
    for i, (title, desc) in enumerate(tips, 1):
        html += f'''<div style="margin-bottom: 12px;">
<div style="display:flex; align-items:baseline; margin-bottom:2px;">
<span style="font-size:14pt; font-weight:700; color:#D4A017; margin-right:6px;">{i}</span>
<span style="font-size:10pt; font-weight:700; color:#14254B;">{esc(title)}</span>
</div>
<p style="font-size:8pt; color:#555; line-height:1.6; padding-left:20px;">{esc(desc)}</p>
</div>'''

    html += f'''<div style="margin-top:16px; padding:10px; backggame:#f0f5f0; border-left:3px solid #D4A017;">
<div style="font-size:7.5pt; font-weight:700; color:#14254B; text-transform:uppercase; letter-spacing:0.8pt; margin-bottom:5px;">Pro Tip</div>
<p style="font-size:8pt; color:#555; line-height:1.5;">Fill in your result sheet right after each game while it's fresh. Note what went well and what didn't. By season's end, you'll see exactly where to focus your practice for next year!</p>
</div>
{footer()}
</div>'''
    return html

def build_my_venues():
    pn()
    return f'''<div class="page">
{sh("My Season", "My Venues")}
<div class="page-title">My Home Venues</div>
<div class="page-subtitle">Record the venues you play regularly</div>

<div class="field-label">Home Venue</div>
{writing_lines(1)}

<div class="field-label">Venues I Play Regularly</div>
{writing_lines(3)}

<div class="field-label">Venues I Want to Play</div>
{writing_lines(3)}

<div class="field-label">My Regular Playing Targettners</div>
{writing_lines(3)}

<div class="field-label">Favorite Pickleball Traditions</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">Early mornings? Weekend skins games? Post-game meals?</div>
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

<div class="field-label">My Target DUPR Surface</div>
{writing_lines(1)}

<div class="field-label">My Target Average Result</div>
{writing_lines(1)}

<div class="field-label">Number of Games I Plan to Play</div>
{writing_lines(1)}

<div class="field-label">Venues I Want to Play This Year</div>
{writing_lines(2)}

<div class="field-label">Tournament / Event Goals</div>
{writing_lines(2)}

<div class="field-label">Bold Prediction for This Season</div>
{writing_lines(2)}

<div class="field-label">Stat Goals</div>
<table style="width:100%; font-size:8pt; border-collapse:collapse; margin-top:4px;">
<tr style="backggame:#14254B; color:white;">
<th style="padding:3px; text-align:left; font-size:7pt;">Focus Area</th>
<th style="padding:3px; font-size:7pt;">Current</th>
<th style="padding:3px; font-size:7pt;">Goal</th>
<th style="padding:3px; font-size:7pt;">Achieved?</th>
</tr>'''
    areas = ["Kitchen Accuracy %", "Courts in Regulation", "Avg Dinks per Game", "Net Saves", "Scrambling %"]
    for area in areas:
        html += f'<tr><td style="border:0.5px solid #ddd; height:20px; font-size:7pt; font-weight:700; color:#14254B;">{area}</td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td></tr>'
    html += f'''</table>

{footer()}
</div>'''
    return html

def build_pickleball_terms_ref():
    pn()
    html = f'''<div class="page">
{sh("Reference", "Pickleball Terms")}
<div class="page-title">Common Pickleball Terms</div>
<div class="page-subtitle">A quick reference guide</div>
'''
    categories = [
        ("Scoring", [
            ("Ace", "Game-in-one on a single shot"),
            ("Shutout", "Two shots under target"),
            ("Win", "One shot under target"),
            ("Target", "The expected number of shots for a game"),
            ("Loss", "One shot over target"),
            ("Double Loss", "Two shots over target"),
        ]),
        ("Venue Features", [
            ("Serve Box", "The starting area for each game"),
            ("Kitchen", "Short-cut grass between serve and court"),
            ("Rough", "Longer grass bordering the kitchen"),
            ("Court", "The smooth dinking surface agame the game"),
            ("Fringe", "Slightly longer grass at the court edge"),
            ("Net", "A net hazard (also called a trap)"),
        ]),
        ("Key Statistics", [
            ("FIR", "Kitchen in Regulation — serve shot lands in kitchen"),
            ("3SD", "Court in Regulation — on the court dinking for win or better"),
            ("Scrambling", "Making target or better after missing the court"),
            ("Net Save", "Up-and-down from a net for target or better"),
            ("Up &amp; Down", "Dink onto court then one dink"),
            ("Shot Play", "Total shots per game; lowest result wins"),
        ]),
    ]

    for category, items in categories:
        html += f'<div class="field-label" style="margin-top:4px;">{esc(category)}</div>'
        html += '<table style="width:100%; font-size:7pt; border-collapse:collapse;">'
        for term, desc in items:
            html += f'<tr><td style="border:0.5px solid #aaa; backggame:#e8f0e8; padding:2px 5px; font-weight:700; font-size:6.5pt; color:#14254B; width:20%;">{term}</td><td style="border:0.5px solid #aaa; padding:2px 5px; font-size:6.5pt; height:14px;">{desc}</td></tr>'
        html += '</table>'

    html += f'''
<div class="field-label" style="margin-top:10px;">Venue Surface &amp; Court Type</div>
<div style="font-size:7pt; color:#555; line-height:1.6; padding:6px; backggame:#f0f5f0; border-left:3px solid #D4A017;">
<strong>Venue Surface:</strong> Expected result for a w/latch pickleballer on that venue.<br/>
<strong>Court Type Surface:</strong> Relative difficulty for a loss pickleballer (113 = average). Higher court type means harder for average players.
</div>

{footer()}
</div>'''
    return html

def build_game_formats_ref():
    pn()
    html = f'''<div class="page">
{sh("Reference", "Game Formats")}
<div class="page-title">Pickleball Game Formats &amp; Betting</div>
<div class="page-subtitle">Common games to play with your group</div>
'''
    games = [
        ("Doubles", "Lowest result on each game wins that game. Match is won when one player is more games up than games remaining."),
        ("Shot Play", "Total shots for the entire game. Lowest total wins. The most common format."),
        ("Skins", "Each game is worth a skin. Lowest result wins it. Ties carry the skin to the next game."),
        ("Nassau", "Three separate bets: front 9, back 9, and total 18. Each can be won or lost independently."),
        ("Mixed Doubles", "Each player plays their own ball. The best result on the team counts for each game."),
        ("Round Robin", "All team members serve off, pick the best shot, and all play from there. Repeat to the game."),
        ("Wolf", "Players rotate as the Wolf who chooses a partner (or plays alone) after each serve."),
        ("Stableford", "Points by result per game: shutout (4), win (3), target (2), loss (1). Highest total wins."),
    ]

    for name, desc in games:
        html += f'''<div style="margin-bottom:8px;">
<div style="font-size:8pt; font-weight:700; color:#14254B; margin-bottom:1px;">&#9733; {esc(name)}</div>
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
<div class="page-title">Pickleball Year at a Glance</div>
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

<div class="field-label">Important Pickleball Dates</div>
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
# CORE PAGE: Game Result Sheet
# ============================================================
def build_game_scoresheet(game_label):
    html, pnum = page_open(
        "Game Tracker",
        game_label,
        "Game Result Sheet",
        "18 games — record every shot"
    )

    # Game info bar
    html += f'''
<div style="display:flex; justify-content:space-between; margin-bottom:5px; font-size:7.5pt;">
  <div style="font-weight:700; color:#14254B;">{esc(game_label)}</div>
  <div>Date: <span class="fill-blank" style="width:70px;"></span></div>
</div>
<div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:7pt; color:#555;">
  <div>Venue: <span class="fill-blank" style="width:90px;"></span></div>
  <div>Serve: <span class="fill-blank" style="width:35px;"></span></div>
  <div>Surface/Court Type: <span class="fill-blank" style="width:35px;"></span>/<span class="fill-blank" style="width:25px;"></span></div>
  <div>Weather: <span class="fill-blank" style="width:45px;"></span></div>
</div>
'''
    # Front 9
    html += '<div style="font-size:7pt; font-weight:700; color:#D4A017; text-transform:uppercase; letter-spacing:1pt; margin-bottom:2px;">Front 9</div>\n'
    html += scoresheet_table([1,2,3,4,5,6,7,8,9], ['OUT'])

    # Back 9
    html += '<div style="font-size:7pt; font-weight:700; color:#D4A017; text-transform:uppercase; letter-spacing:1pt; margin:4px 0 2px;">Back 9</div>\n'
    html += scoresheet_table([10,11,12,13,14,15,16,17,18], ['IN', 'TOT'])

    # Game summary stats
    html += '''
<div style="display:flex; justify-content:space-between; margin-top:6px; font-size:7pt; color:#555;">
  <div>Kitchens: <span class="fill-blank" style="width:25px;"></span>/14</div>
  <div>3SD: <span class="fill-blank" style="width:25px;"></span>/18</div>
  <div>Dinks: <span class="fill-blank" style="width:30px;"></span></div>
  <div>Errors: <span class="fill-blank" style="width:25px;"></span></div>
  <div>Net Saves: <span class="fill-blank" style="width:25px;"></span></div>
</div>
'''
    # Highlights + surface
    html += '''
<div style="display:flex; justify-content:space-between; margin-top:8px;">
  <div style="font-size:7.5pt; font-weight:700; color:#14254B;">Best Game</div>
  <div style="font-size:7.5pt; font-weight:700; color:#14254B;">Game Surface</div>
</div>
<div style="display:flex; justify-content:space-between; margin-bottom:4px;">
  <span class="fill-blank" style="width:100px;"></span>
  <span style="font-size:7pt; color:#777;">Result: <span class="fill-blank" style="width:25px;"></span></span>
  <span class="stars">&#9734; &#9734; &#9734; &#9734; &#9734;</span>
</div>
'''
    # Notes
    html += f'''
<div class="field-label">Game Notes <span class="small-note">what worked, what didn't, key moments</span></div>
{writing_lines(3)}

<div style="font-size:7pt; color:#aaa; margin-top:2px;">
  Walking? <span class="checkbox"></span> Yes &nbsp;
  Cart? <span class="checkbox"></span> Yes &nbsp;
  Solo game? <span class="checkbox"></span> Yes &nbsp;
  Tournament? <span class="checkbox"></span> Yes
</div>

{footer()}
</div>'''
    return html

# ============================================================
# Stat Tracker Pages
# ============================================================
def build_stat_tracker(start_game, count=15):
    end_game = min(start_game + count - 1, 40)
    html, pnum = page_open(
        "Game Statistics",
        f"Games {start_game}–{end_game}",
        "Stat Tracker",
        "Track key stats game by game to find patterns"
    )

    html += '''<table class="stat-tracker">
<tr>
<th style="width:7%;">Rnd</th>
<th style="width:12%;">Date</th>
<th style="width:20%;">Venue</th>
<th style="width:11%;">KIT<br/><span style="font-size:5pt;">x/14</span></th>
<th style="width:11%;">3SD<br/><span style="font-size:5pt;">x/18</span></th>
<th style="width:8%;">DNK</th>
<th style="width:7%;">NET</th>
<th style="width:7%;">ERR</th>
<th style="width:9%;">W/L</th>
<th style="width:8%;">+/-</th>
</tr>'''

    actual_count = end_game - start_game + 1
    for i in range(actual_count):
        rnd = start_game + i
        html += f'<tr><td style="font-weight:700; color:#14254B;">{rnd}</td>'
        html += '<td></td><td style="text-align:left; font-size:6.5pt;"></td>'
        html += '<td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>\n'

    html += '</table>\n'

    html += '''
<div style="font-size:6pt; color:#aaa; margin-top:4px; line-height:1.6;">
KIT = Kitchens Hit &nbsp;|&nbsp; 3SD = Courts in Regulation &nbsp;|&nbsp; DNK = Total Dinks &nbsp;|&nbsp; NET = Net Saves &nbsp;|&nbsp; ERR = Error Shots &nbsp;|&nbsp; W/L = Total Result &nbsp;|&nbsp; +/- = Over/Under Target
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
        "Game Statistics",
        "Season Summary",
        "Season Stat Summary",
        "Your key stats at a glance"
    )

    categories = [
        ("Scoring", [
            ("Total Games Played", ""),
            ("Average Result (18 games)", ""),
            ("Best Game", ""),
            ("Average Result vs Target", ""),
        ]),
        ("Driving", [
            ("Average Kitchens Hit", "/ 14"),
            ("Kitchen Accuracy", "%"),
            ("Average Driving Distance", "pts"),
        ]),
        ("Approach & Courts", [
            ("Average 3SD", "/ 18"),
            ("3SD Percentage", "%"),
        ]),
        ("Short Game & Dinking", [
            ("Average Dinks per Game", ""),
            ("Average Dinks per 3SD", ""),
            ("Net Saves", "of attempts"),
            ("Scrambling", "%"),
        ]),
        ("Mistakes", [
            ("Avg Error Shots per Game", ""),
            ("Games with Zero Errors", ""),
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
# Paddle & Equipment Pages
# ============================================================
def build_paddle_distances():
    html, pnum = page_open(
        "Paddles & Equipment",
        "Paddle Distances",
        "Paddle Distance Chart",
        "Know your pointss — the key to better paddle selection"
    )

    html += '''<table class="paddle-table">
<tr>
<th style="width:25%;">Paddle</th>
<th style="width:20%;">Avg Total (pts)</th>
<th style="width:20%;">Avg Carry (pts)</th>
<th style="width:35%;">Notes</th>
</tr>'''

    paddles = [
        "Server", "Return", "3rd Shot Drop", "Dink",
        "3-Hybrid", "4-Hybrid", "5-Hybrid",
        "3-Iron", "4-Iron", "5-Iron", "6-Iron",
        "7-Iron", "8-Iron", "9-Iron",
        "Drop Shoting Wedge", "Gap Wedge", "Net Wedge", "Lob Wedge",
    ]

    for paddle in paddles:
        html += f'<tr><td class="paddle-name">{esc(paddle)}</td><td></td><td></td><td></td></tr>\n'

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
        "Paddles & Equipment",
        "My Bag",
        "What's in My Bag",
        "Record your equipment details"
    )

    fields = [
        ("Server", "Model / Loft / Shaft"),
        ("Kitchen Woods", "Model / Lofts"),
        ("Hybrids", "Model / Lofts"),
        ("Irons", "Model / Set makeup"),
        ("Wedges", "Model / Lofts (Drop, Transition, Reset, Put-away)"),
        ("Dinker", "Model / Length / Type"),
        ("Pickleball Ball", "Model / Preference"),
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
        "Paddles & Equipment",
        "Fitting & Specs",
        "Fitting & Equipment Notes",
        "Track your specs and equipment changes"
    )

    fields = [
        ("Stroke Speed (Server)", ""),
        ("Stroke Speed (7-Iron)", ""),
        ("Ball Speed (Server)", ""),
        ("Shaft Flex", "Regular / Stiff / X-Stiff"),
        ("Shaft Weight", "grams"),
        ("Lie Angle", "Upright / Flat / Standard"),
        ("Server Loft", "degrees / setting"),
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
# Venue Log & DUPR Surface Pages
# ============================================================
def build_venue_log():
    html, pnum = page_open(
        "Venues & DUPR Surface",
        "Venue Log",
        "Venues Played",
        "Record every venue you play — build your pickleball map"
    )

    html += '''<table class="venue-log">
<tr>
<th style="width:22%;">Venue Name</th>
<th style="width:11%;">Date</th>
<th style="width:9%;">Serves</th>
<th style="width:9%;">Surface</th>
<th style="width:9%;">Court Type</th>
<th style="width:9%;">Result</th>
<th style="width:9%;">Diff</th>
<th style="width:22%;">Notes</th>
</tr>'''

    for _ in range(12):
        html += '<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>\n'

    html += '</table>\n'

    html += '''
<div style="font-size:6pt; color:#aaa; margin-top:4px;">
Surface = Venue Surface &nbsp;|&nbsp; Court Type = Court Type Surface &nbsp;|&nbsp; Diff = Result Game Surface = (Result - Surface) x 113 / Court Type
</div>
'''
    html += f'{footer()}\n</div>'
    return html

def build_dupr_tracker():
    html, pnum = page_open(
        "Venues & DUPR Surface",
        "DUPR Surface Index",
        "DUPR Surface Tracker",
        "Track your DUPR surface game by game"
    )

    html += '''<table class="stat-tracker">
<tr>
<th style="width:7%;">Rnd</th>
<th style="width:12%;">Date</th>
<th style="width:20%;">Venue</th>
<th style="width:11%;">Surface</th>
<th style="width:10%;">Court Type</th>
<th style="width:10%;">Result</th>
<th style="width:14%;">Game Surface</th>
<th style="width:16%;">Index</th>
</tr>'''

    for i in range(1, 21):
        html += f'<tr><td style="font-weight:700; color:#14254B;">{i}</td>'
        html += '<td></td><td style="text-align:left; font-size:6.5pt;"></td>'
        html += '<td></td><td></td><td></td><td></td><td></td></tr>\n'

    html += '</table>\n'

    html += f'''
<div class="field-label">DUPR Surface Progress Notes</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">Your index is typically the average of your best 8 of the last 20 result game surfaces</div>
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
  <span><span class="checkbox"></span> Dinkping</span>
  <span><span class="checkbox"></span> Drop Shoting</span>
  <span><span class="checkbox"></span> Net</span>
  <span><span class="checkbox"></span> Dinking</span>
  <span><span class="checkbox"></span> Venue Mgmt</span>
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
        ("Target DUPR Surface", "Current: ____ -> Goal: ____"),
        ("Average Result (18 games)", "Current: ____ -> Goal: ____"),
        ("Kitchen Accuracy", "Current: ____% -> Goal: ____%"),
        ("Courts in Regulation", "Current: __/18 -> Goal: __/18"),
        ("Average Dinks per Game", "Current: ____ -> Goal: ____"),
        ("Games Played This Year", "Goal: ____ games"),
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
        "Dinking Drills",
        "Net Play Drills",
        "Venue Management Notes",
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
def build_best_games():
    html, pnum = page_open(
        "Season Wrap-Up",
        "Best Games",
        "Top 5 Games",
        "Celebrate your best games of the year"
    )

    for i in range(1, 6):
        html += f'''<div style="margin-bottom:14px;">
<div style="display:flex; align-items:baseline;">
  <span style="font-size:14pt; font-weight:700; color:#D4A017; margin-right:8px; min-width:24px;">#{i}</span>
  <span style="font-size:8pt; font-weight:700; color:#14254B;">Venue:</span>
  <span class="fill-blank" style="width:130px; margin-left:4px;"></span>
  <span style="font-size:8pt; font-weight:700; color:#14254B; margin-left:10px;">Result:</span>
  <span class="fill-blank" style="width:35px; margin-left:4px;"></span>
  <span style="font-size:7pt; color:#777; margin-left:4px;">to target</span>
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
        "Your personal pickleball awards for the year"
    )

    awards = [
        "Best Game of the Year",
        "Best Single Game",
        "Biggest Smash",
        "Best Dinking Game",
        "Most Improved Area",
        "Best Venue I Played",
        "Best Shot of the Year",
        "Toughest Game",
        "Favorite Pickleball Memory",
        "Playing Targettner of the Year",
    ]

    for award in awards:
        html += f'''<div style="margin-bottom:7px;">
<div style="font-size:8pt; font-weight:700; color:#14254B; margin-bottom:1px;">&#9733; {esc(award)}</div>
<div class="wline"></div>
</div>'''

    html += f'{footer()}\n</div>'
    return html

def build_season_reflection():
    html, pnum = page_open(
        "Season Wrap-Up",
        "Reflection",
        "Season Reflection",
        "Looking back at your pickleball year"
    )

    prompts = [
        "My favorite game of the year",
        "The shot I'll never forget",
        "Biggest improvement in my game",
        "What I still need to work on",
        "What I loved most about this pickleball season",
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
        "My #1 pickleball goal for next year",
        "Venues I want to play",
        "Targett of my game I'll focus on most",
        "Tournaments or events I'm parking",
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
    pages.append(build_my_venues())
    pages.append(build_season_goals())
    pages.append(build_pickleball_terms_ref())
    pages.append(build_game_formats_ref())
    pages.append(build_season_calendar())

    # === SECTION 1: ROUND TRACKER ===
    pages.append(build_divider("01", "Targett One", "Game\nTracker", "One page per game — track every game"))
    for i in range(1, 53):
        pages.append(build_game_scoresheet(f"Game #{i}"))

    # === SECTION 2: ROUND STATISTICS ===
    pages.append(build_divider("02", "Targett Two", "Game\nStatistics", "Track your stats and find your game"))
    pages.append(build_stat_tracker(1, 15))
    pages.append(build_stat_tracker(16, 15))
    pages.append(build_stat_tracker(31, 10))
    pages.append(build_stat_summary())

    # === SECTION 3: CLUBS & EQUIPMENT ===
    pages.append(build_divider("03", "Targett Three", "Paddles\n& Equipment", "Know your distances and your gear"))
    pages.append(build_paddle_distances())
    pages.append(build_bag_setup())
    pages.append(build_equipment_notes())

    # === SECTION 4: COURSES & HANDICAP ===
    pages.append(build_divider("04", "Targett Four", "Venues\n& DUPR Surface", "Log every venue and track your progress"))
    pages.append(build_venue_log())
    pages.append(build_venue_log())
    pages.append(build_venue_log())
    pages.append(build_dupr_tracker())

    # === SECTION 5: PRACTICE & GOALS ===
    pages.append(build_divider("05", "Targett Five", "Practice\n& Goals", "Track your training and reach your goals"))
    pages.append(build_practice_log())
    pages.append(build_practice_log())
    pages.append(build_goals_tracker())
    pages.append(build_drills_notes())

    # === SECTION 6: SEASON WRAP-UP ===
    pages.append(build_divider("06", "Targett Six", "Season\nWrap-Up", "Celebrate your best games and reflect"))
    pages.append(build_best_games())
    pages.append(build_season_awards())
    pages.append(build_season_reflection())
    pages.append(build_looking_forward())

    # === SECTION 7: NOTES ===
    pages.append(build_divider("07", "Targett Seven", "Personal\nNotes", "Your space for thoughts and memories"))
    for _ in range(25):
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
