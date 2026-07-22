#!/usr/bin/env python3
"""
Football Journal Notebook — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: American football fans (NFL + NCAA)
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "football_journal_us_V1.0.html")

BOOK_TITLE = "Football Journal"
BOOK_SUBTITLE = "Your Ultimate Season Journal"

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
/* Field green: #0B4D2E, #1a6b3f */
/* Football brown: #6B3410, #8B4513 */
/* Accent gold: #D4A017 */
/* Light gray: #f5f5f5 */

/* ---- Cover ---- */
.cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(180deg, #0a3d24 0%, #0B4D2E 40%, #0a3d24 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Yard lines on cover */
.cover .yard-lines {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image:
    repeating-linear-gradient(
      0deg,
      transparent,
      transparent 38px,
      rgba(255,255,255,0.07) 38px,
      rgba(255,255,255,0.07) 40px
    );
}

/* CSS Football */
.cover .football {
  width: 130px; height: 80px;
  background: #7a3e0f;
  border-radius: 50%;
  position: relative;
  margin: 0 auto 20px;
  transform: rotate(-20deg);
  box-shadow: 3px 3px 12px rgba(0,0,0,0.5),
              inset -8px -4px 12px rgba(0,0,0,0.3),
              inset 8px 4px 12px rgba(255,255,255,0.05);
}
.cover .football::before {
  content: "";
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 40px; height: 2px;
  background: #fff;
  border-radius: 1px;
}
.cover .football::after {
  content: "";
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 30px; height: 1px;
  border-top: 0;
  background: transparent;
  box-shadow:
    0 -5px 0 #fff,
    0 5px 0 #fff;
}

.cover .football-laces {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
}
.cover .football-laces span {
  display: block;
  width: 14px; height: 2px;
  background: #fff;
  margin: 3px auto;
  border-radius: 1px;
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 32pt;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.1;
  letter-spacing: 1pt;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
}

.cover .accent-bar {
  width: 120px; height: 3px;
  background: #D4A017;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 13pt;
  color: #c8e6c9;
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
  background: rgba(255,255,255,0.12);
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
  color: #a5d6a7;
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
  background: #0B4D2E;
  position: relative;
  overflow: hidden;
}
.divider .div-yard {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: repeating-linear-gradient(0deg,
    transparent, transparent 40px,
    rgba(255,255,255,0.05) 40px, rgba(255,255,255,0.05) 42px);
}
.divider .div-num {
  font-size: 60pt;
  color: rgba(212,160,23,0.15);
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
  color: #a5d6a7;
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
  border-bottom: 1.5px solid #0B4D2E;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #0B4D2E;
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
  color: #0B4D2E;
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

/* ---- Score Table ---- */
.score-table {
  width: 100%;
  border-collapse: collapse;
  margin: 8px 0;
}
.score-table th {
  background: #0B4D2E;
  color: white;
  font-size: 7.5pt;
  font-weight: 700;
  padding: 4px 2px;
  text-align: center;
  letter-spacing: 0.5pt;
}
.score-table td {
  border: 0.5px solid #999;
  font-size: 9pt;
  padding: 6px 4px;
  text-align: center;
}
.score-table td.team-cell {
  text-align: left;
  padding-left: 6px;
  font-size: 8pt;
}
.score-table td.score-input {
  height: 26px;
  background: #fafafa;
}
.score-table td.final-cell {
  background: #f0f0f0;
  font-weight: 700;
}

/* ---- Field Labels ---- */
.field-label {
  font-size: 7.5pt;
  font-weight: 700;
  color: #0B4D2E;
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

.inline-field {
  display: inline-block;
  border-bottom: 0.5px solid #999;
  min-width: 100px;
  height: 16px;
  margin-left: 4px;
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

/* ---- Bracket ---- */
.bracket-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 8px;
  font-size: 7pt;
}
.bracket-slot {
  border: 0.5px solid #888;
  padding: 3px 5px;
  margin-bottom: 6px;
  font-size: 7pt;
  color: #666;
  min-height: 28px;
}
.bracket-slot .slot-label {
  font-size: 6pt;
  color: #aaa;
  text-transform: uppercase;
}
.bracket-slot .slot-team {
  border-bottom: 0.5px solid #ccc;
  height: 12px;
  margin-top: 2px;
}

/* ---- Notes Page ---- */
.notes-page-title {
  font-size: 12pt;
  font-weight: 700;
  color: #0B4D2E;
  margin-bottom: 10px;
  border-bottom: 2px solid #D4A017;
  padding-bottom: 5px;
}

.gridiron-lines {
  background-image: repeating-linear-gradient(
    transparent,
    transparent 21px,
    #c8c8c8 21px,
    #c8c8c8 21.5px
  );
}

/* ---- Table-like standings ---- */
.standings-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 7.5pt;
  margin-bottom: 10px;
}
.standings-table th {
  background: #0B4D2E;
  color: white;
  padding: 3px 4px;
  text-align: center;
  font-weight: 700;
  font-size: 7pt;
}
.standings-table td {
  border: 0.5px solid #ddd;
  padding: 4px 4px;
  text-align: center;
  height: 20px;
}
.standings-table td.team-col {
  text-align: left;
  width: 40%;
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
  width: 50px; height: 30px;
  background: #7a3e0f;
  border-radius: 50%;
  margin: 0 auto 20px;
  transform: rotate(-20deg);
  position: relative;
}
.owner-page .owner-icon::after {
  content: "";
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%,-50%);
  width: 20px; height: 1.5px;
  background: #fff;
}
.owner-page .owner-title {
  font-size: 20pt;
  font-weight: 700;
  color: #0B4D2E;
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
  color: #0B4D2E;
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
  background: linear-gradient(180deg, #0a3d24 0%, #0B4D2E 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.back-cover .bc-yard {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: repeating-linear-gradient(0deg,
    transparent, transparent 38px,
    rgba(255,255,255,0.05) 38px, rgba(255,255,255,0.05) 40px);
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
  color: #c8e6c9;
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
  content: "▸ ";
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

def page_open(sec_left, sec_right, title=None, subtitle=None, footer_text=BOOK_TITLE):
    pnum = pn()
    html = f'<div class="page">{sh(sec_left, sec_right)}'
    if title:
        html += f'<div class="page-title">{esc(title)}</div>'
    if subtitle:
        html += f'<div class="page-subtitle">{esc(subtitle)}</div>'
    return html, pnum

def page_close(footer_text=BOOK_TITLE):
    return f'{footer(footer_text)}</div>'

# ============================================================
# PAGE BUILDERS
# ============================================================

def build_cover():
    pn()
    return '''<div class="cover">
  <div class="yard-lines"></div>
  <div class="title-block">
    <div class="football">
      <div class="football-laces"><span></span><span></span><span></span><span></span></div>
    </div>
    <div class="main-title">FOOTBALL<br/>JOURNAL</div>
    <div class="accent-bar"></div>
    <div class="subtitle">Your Ultimate Season Journal<br/>for NFL &amp; College Football</div>
    <div class="features">
      <span class="feature-badge">Game Scores</span>
      <span class="feature-badge">Playoff Brackets</span>
      <span class="feature-badge">Team Stats</span>
      <span class="feature-badge">Season Notes</span>
    </div>
    <div class="season-tag">★ Track Every Game ★</div>
  </div>
  <div class="publisher">More Shine Press</div>
</div>'''

def build_back_cover():
    pn()
    return '''<div class="back-cover">
  <div class="bc-yard"></div>
  <div class="bc-content">
    <div class="bc-title">★ A Perfect Gift for Football Fans ★</div>
    <p class="bc-text">Whether you're a die-hard fan or a casual viewer, this journal helps you capture every thrilling moment of the football season.</p>
    <ul class="bc-features">
      <li>Track scores for NFL &amp; College games</li>
      <li>Fill in playoff brackets and championship results</li>
      <li>Monitor team standings all season long</li>
      <li>Record your predictions, picks, and reflections</li>
      <li>Plenty of space for personal notes and memories</li>
    </ul>
    <p class="bc-text" style="font-style:italic;">Kick off your season and never forget a game!</p>
  </div>
  <div class="bc-publisher">More Shine Press</div>
</div>'''

def build_owner_page():
    pn()
    return f'''<div class="page">
<div class="owner-page">
  <div class="owner-icon"></div>
  <div class="owner-title">This Journal Belongs To</div>
  <div class="owner-sub">Fill in your details below</div>
  <div class="owner-line">
    <div class="ol-label">Name</div>
    <div class="ol-blank"></div>
  </div>
  <div class="owner-line">
    <div class="ol-label">Favorite NFL Team</div>
    <div class="ol-blank"></div>
  </div>
  <div class="owner-line">
    <div class="ol-label">Favorite College Team</div>
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
        ("Game Tracker", "Use one page per game. Fill in the teams, scores by quarter, and jot down the key plays that made the difference."),
        ("Playoff Brackets", "Fill in the teams as they advance through the playoffs. Track every matchup from Wild Card to the Championship."),
        ("Standings & Stats", "Update team records each week. Track your weekly picks and see how you perform against the experts."),
        ("Notes & Reflections", "Use the note pages to record your thoughts, memorable moments, and season highlights throughout the year."),
    ]
    html = f'''<div class="page">
{sh("Getting Started", "How to Use This Journal")}
<div class="page-title">How to Use This Journal</div>
<div class="page-subtitle">A quick guide to getting the most out of your season journal</div>
'''
    for i, (title, desc) in enumerate(tips, 1):
        html += f'''<div style="margin-bottom: 12px;">
<div style="display:flex; align-items:baseline; margin-bottom:2px;">
<span style="font-size:14pt; font-weight:700; color:#D4A017; margin-right:6px;">{i}</span>
<span style="font-size:10pt; font-weight:700; color:#0B4D2E;">{esc(title)}</span>
</div>
<p style="font-size:8pt; color:#555; line-height:1.6; padding-left:20px;">{esc(desc)}</p>
</div>'''

    html += f'''<div style="margin-top:20px; padding:10px; background:#f5f5f5; border-left:3px solid #D4A017;">
<div style="font-size:7.5pt; font-weight:700; color:#0B4D2E; text-transform:uppercase; letter-spacing:0.8pt; margin-bottom:5px;">Pro Tip</div>
<p style="font-size:8pt; color:#555; line-height:1.5;">Keep this journal handy while watching games. Fill in the scores as they happen, then add your notes and reflections after the game ends. By season's end, you'll have a complete record of your football year!</p>
</div>
{footer()}
</div>'''
    return html

def build_my_teams():
    pn()
    return f'''<div class="page">
{sh("My Season", "My Teams")}
<div class="page-title">My Teams</div>
<div class="page-subtitle">Record the teams you'll be following this season</div>

<div class="field-label">Pro League Teams I Follow</div>
{writing_lines(1)}
{writing_lines(1)}
{writing_lines(1)}
{writing_lines(1)}

<div class="field-label">College Teams I Follow</div>
{writing_lines(1)}
{writing_lines(1)}
{writing_lines(1)}
{writing_lines(1)}

<div class="field-label">Rivalries I Care About Most</div>
{writing_lines(3)}

<div class="field-label">Game-Watching Traditions</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">Where do you watch? Who do you watch with? Any game-day rituals?</div>
{writing_lines(4)}

<div class="field-label">This Season, I'm Most Excited About...</div>
{writing_lines(4)}

{footer()}
</div>'''

def build_predictions():
    pn()
    return f'''<div class="page">
{sh("My Season", "Predictions")}
<div class="page-title">Season Predictions</div>
<div class="page-subtitle">Make your picks before the season kicks off — check back at the end!</div>

<div class="field-label">Pro League Champion Prediction</div>
{writing_lines(1)}

<div class="field-label">College National Champion Prediction</div>
{writing_lines(1)}

<div class="field-label">MVP Pick</div>
{writing_lines(1)}

<div class="field-label">Top College Player Pick</div>
{writing_lines(1)}

<div class="field-label">Breakout Team of the Year</div>
{writing_lines(1)}

<div class="field-label">Surprise / Upset Team</div>
{writing_lines(1)}

<div class="field-label">Record Predictions for My Teams</div>
<table style="width:100%; font-size:8pt; border-collapse:collapse; margin-top:4px;">
<tr style="background:#0B4D2E; color:white;">
<th style="padding:3px; text-align:left; font-size:7pt;">Team</th>
<th style="padding:3px; font-size:7pt;">Wins</th>
<th style="padding:3px; font-size:7pt;">Losses</th>
<th style="padding:3px; font-size:7pt;">Playoffs?</th>
</tr>
<tr><td style="border:0.5px solid #ddd; height:20px;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td></tr>
<tr><td style="border:0.5px solid #ddd; height:20px;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td></tr>
<tr><td style="border:0.5px solid #ddd; height:20px;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td></tr>
<tr><td style="border:0.5px solid #ddd; height:20px;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td></tr>
</table>

<div class="field-label">Bold Prediction for This Season</div>
{writing_lines(3)}

{footer()}
</div>'''

def build_division_ref():
    """NFL division reference - blank team slots for user to fill in."""
    pn()
    divisions = [
        ("Pro League — AFC", [
            ("AFC East", 4), ("AFC North", 4), ("AFC South", 4), ("AFC West", 4)
        ]),
        ("Pro League — NFC", [
            ("NFC East", 4), ("NFC North", 4), ("NFC South", 4), ("NFC West", 4)
        ]),
    ]

    html = f'''<div class="page">
{sh("Reference", "Team Divisions")}
<div class="page-title">Pro League Divisions</div>
<div class="page-subtitle">Reference guide — fill in teams as you track your season</div>
'''
    for league, divs in divisions:
        html += f'<div class="field-label" style="margin-top:6px;">{esc(league)}</div>'
        html += '<table style="width:100%; font-size:7.5pt; border-collapse:collapse;">'
        for div_name, count in divs:
            html += f'<tr><td style="border:0.5px solid #aaa; background:#e8f0e8; padding:3px 5px; font-weight:700; font-size:7pt; color:#0B4D2E; width:35%;">{esc(div_name)}</td>'
            html += '<td style="border:0.5px solid #aaa; height:16px;"></td></tr>'
            for _ in range(count - 1):
                html += '<tr><td style="border:0.5px solid #aaa;"></td><td style="border:0.5px solid #aaa; height:16px;"></td></tr>'
        html += '</table>'

    html += f'''<div class="field-label" style="margin-top:10px;">Wildcard &amp; Playoff Notes</div>
{writing_lines(2)}
{footer()}
</div>'''
    return html

def build_conference_ref():
    pn()
    html = f'''<div class="page">
{sh("Reference", "College Conferences")}
<div class="page-title">College Football Conferences</div>
<div class="page-subtitle">Reference guide — fill in key teams as you track your season</div>
'''
    conferences = [
        ("SEC", 4), ("Big Ten", 4), ("Big 12", 4),
        ("ACC", 4), ("Pac-12", 3), ("Independent / Others", 3),
    ]

    html += '<table style="width:100%; font-size:7.5pt; border-collapse:collapse;">'
    for conf, count in conferences:
        html += f'<tr><td style="border:0.5px solid #aaa; background:#e8f0e8; padding:3px 5px; font-weight:700; font-size:7pt; color:#0B4D2E; width:35%;">{esc(conf)}</td>'
        html += '<td style="border:0.5px solid #aaa; height:16px;"></td></tr>'
        for _ in range(count - 1):
            html += '<tr><td style="border:0.5px solid #aaa;"></td><td style="border:0.5px solid #aaa; height:16px;"></td></tr>'
    html += '</table>'

    html += f'''
<div class="field-label" style="margin-top:12px;">Rivalry Games to Watch</div>
{writing_lines(3)}

<div class="field-label">Bowl Games I Want to Watch</div>
{writing_lines(4)}

<div class="field-label">College Playoff Notes</div>
{writing_lines(3)}

{footer()}
</div>'''
    return html

def build_season_calendar():
    pn()
    months = ["August", "September", "October", "November", "December", "January", "February"]
    html = f'''<div class="page">
{sh("Reference", "Season Calendar")}
<div class="page-title">Season at a Glance</div>
<div class="page-subtitle">Mark key dates, big games, and events throughout the season</div>
'''
    for month in months:
        html += f'<div class="field-label" style="margin-top:4px;">{month}</div>'
        html += writing_lines(2)

    html += f'''<div class="field-label" style="margin-top:8px;">Important Dates &amp; Events</div>
{writing_lines(3)}
{footer()}
</div>'''
    return html

def build_game_tracker(week_label, league_tag="PRO"):
    """One game tracking page."""
    html, pnum = page_open(
        f"Game Tracker — {league_tag}",
        week_label,
        "Game Tracker",
        f"Week of the season — record every detail"
    )

    html += f'''
<div style="display:flex; justify-content:space-between; margin-bottom:8px;">
  <div style="font-size:8pt; font-weight:700; color:#0B4D2E;">{esc(week_label)}</div>
  <div style="font-size:8pt; color:#777;">Date: <span class="fill-blank" style="width:60px;"></span></div>
</div>

<table class="score-table">
<tr>
<th style="width:32%;">Team</th>
<th>Q1</th><th>Q2</th><th>Q3</th><th>Q4</th>
<th style="background:#D4A017;">FINAL</th>
</tr>
<tr>
<td class="team-cell">
  <span style="font-size:6pt; color:#aaa;">HOME:</span><br/>
  <span style="border-bottom:0.5px solid #999; display:inline-block; width:85%; height:14px;"></span>
</td>
<td class="score-input"></td><td class="score-input"></td><td class="score-input"></td><td class="score-input"></td>
<td class="score-input final-cell"></td>
</tr>
<tr>
<td class="team-cell">
  <span style="font-size:6pt; color:#aaa;">AWAY:</span><br/>
  <span style="border-bottom:0.5px solid #999; display:inline-block; width:85%; height:14px;"></span>
</td>
<td class="score-input"></td><td class="score-input"></td><td class="score-input"></td><td class="score-input"></td>
<td class="score-input final-cell"></td>
</tr>
</table>

<div style="font-size:7pt; color:#aaa; margin-bottom:4px;">OT: <span class="fill-blank" style="width:30px;"></span> &nbsp; Venue: <span class="fill-blank" style="width:120px;"></span> &nbsp; TV: <span class="fill-blank" style="width:60px;"></span></div>

<div class="field-label">Key Plays &amp; Highlights <span class="small-note">big moments, turnovers, scoring drives</span></div>
{writing_lines(4)}

<div style="display:flex; justify-content:space-between; margin-top:6px;">
  <div style="font-size:7.5pt; font-weight:700; color:#0B4D2E;">Star Player of the Game</div>
  <div style="font-size:7.5pt; font-weight:700; color:#0B4D2E;">Game Rating</div>
</div>
<div style="display:flex; justify-content:space-between; margin-bottom:4px;">
  <span class="fill-blank" style="width:160px;"></span>
  <span class="stars">☆ ☆ ☆ ☆ ☆</span>
</div>

<div class="field-label">My Thoughts &amp; Notes</div>
{writing_lines(4)}

<div style="font-size:7pt; color:#aaa; margin-top:2px;">Pick correct? <span class="checkbox"></span> Yes &nbsp; Surprising result? <span class="checkbox"></span> Yes &nbsp; Watched live? <span class="checkbox"></span> Yes &nbsp; Recorded? <span class="checkbox"></span> Yes</div>

{footer()}
</div>'''
    return html

def build_playoff_bracket():
    """NFL-style playoff bracket — 2 pages."""
    pages = []
    for part in [1, 2]:
        html, pnum = page_open(
            "Playoff Tracker",
            f"Pro League Bracket — Part {part}" if part == 1 else "Pro League Bracket — Part 2",
            "Pro League Playoff Bracket" if part == 1 else "Pro League Playoff Bracket (cont.)",
            "Fill in teams as the playoffs advance"
        )
        if part == 1:
            html += '''
<div class="field-label">Wild Card Round</div>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:6px;">
'''
            for i in range(6):
                html += f'''<div class="bracket-slot">
<div class="slot-label">Game {i+1}</div>
<div class="slot-team"></div><div class="slot-team"></div>
<div style="font-size:6pt; color:#ccc; text-align:center;">Score: ______</div>
</div>'''
            html += '</div>'

            html += '''
<div class="field-label" style="margin-top:6px;">Divisional Round</div>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:6px;">
'''
            for i in range(4):
                html += f'''<div class="bracket-slot">
<div class="slot-label">Game {i+1}</div>
<div class="slot-team"></div><div class="slot-team"></div>
<div style="font-size:6pt; color:#ccc; text-align:center;">Score: ______</div>
</div>'''
            html += '</div>'
        else:
            html += '''
<div class="field-label">Conference Championships</div>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
'''
            for label in ["AFC Championship", "NFC Championship"]:
                html += f'''<div class="bracket-slot" style="min-height:50px;">
<div class="slot-label">{label}</div>
<div class="slot-team"></div><div class="slot-team"></div>
<div style="font-size:6pt; color:#ccc; text-align:center;">Score: ______</div>
</div>'''
            html += '</div>'

            html += '''
<div class="field-label" style="margin-top:12px; text-align:center; font-size:10pt;">★ THE BIG GAME ★</div>
<div style="border:2px solid #D4A017; padding:12px; margin-top:6px; text-align:center; background:#fffbf0;">
<div style="font-size:8pt; color:#aaa; margin-bottom:6px;">Championship Game</div>
<div style="display:flex; justify-content:center; gap:20px; margin-bottom:8px;">
  <span class="fill-blank" style="width:120px; display:inline-block;"></span>
  <span style="font-size:10pt; font-weight:700; color:#D4A017;">VS</span>
  <span class="fill-blank" style="width:120px; display:inline-block;"></span>
</div>
<div style="font-size:8pt; color:#555;">Date: <span class="fill-blank" style="width:80px;"></span></div>
<div style="font-size:8pt; color:#555;">Location: <span class="fill-blank" style="width:140px;"></span></div>
<div style="font-size:8pt; color:#555;">Final Score: <span class="fill-blank" style="width:60px;"></span> — <span class="fill-blank" style="width:60px;"></span></div>
<div style="font-size:8pt; color:#555;">Champion: <span class="fill-blank" style="width:140px;"></span></div>
<div style="font-size:8pt; color:#555;">MVP: <span class="fill-blank" style="width:140px;"></span></div>
</div>

<div class="field-label">My Big Game Experience</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">Where did you watch? Who were you with? What was the best moment?</div>
'''
            html += writing_lines(4)

        html += f'{footer()}\n</div>'
        pages.append(html)
    return pages

def build_cfp_bracket():
    """College Football Playoff bracket."""
    html, pnum = page_open(
        "Playoff Tracker",
        "College Playoff Bracket",
        "College Football Playoff Bracket",
        "Fill in teams as the playoffs advance"
    )

    html += '''
<div class="field-label">First Round</div>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:6px;">
'''
    for i in range(4):
        html += f'''<div class="bracket-slot">
<div class="slot-label">Game {i+1}</div>
<div class="slot-team"></div><div class="slot-team"></div>
<div style="font-size:6pt; color:#ccc; text-align:center;">Score: ______</div>
</div>'''
    html += '</div>'

    html += '''
<div class="field-label" style="margin-top:6px;">Semifinals</div>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
'''
    for i in range(2):
        html += f'''<div class="bracket-slot" style="min-height:45px;">
<div class="slot-label">Semifinal {i+1}</div>
<div class="slot-team"></div><div class="slot-team"></div>
<div style="font-size:6pt; color:#ccc; text-align:center;">Score: ______</div>
</div>'''
    html += '</div>'

    html += '''
<div class="field-label" style="margin-top:10px; text-align:center; font-size:10pt;">★ NATIONAL CHAMPIONSHIP ★</div>
<div style="border:2px solid #D4A017; padding:10px; margin-top:4px; text-align:center; background:#fffbf0;">
<div style="display:flex; justify-content:center; gap:16px; margin-bottom:6px;">
  <span class="fill-blank" style="width:120px;"></span>
  <span style="font-size:10pt; font-weight:700; color:#D4A017;">VS</span>
  <span class="fill-blank" style="width:120px;"></span>
</div>
<div style="font-size:7.5pt; color:#555;">Date: <span class="fill-blank" style="width:80px;"></span></div>
<div style="font-size:7.5pt; color:#555;">Final Score: <span class="fill-blank" style="width:50px;"></span> — <span class="fill-blank" style="width:50px;"></span></div>
<div style="font-size:7.5pt; color:#555;">National Champion: <span class="fill-blank" style="width:120px;"></span></div>
</div>

<div class="field-label">Bowl Games Watched</div>
'''

    html += '''<table style="width:100%; font-size:7pt; border-collapse:collapse; margin-top:4px;">
<tr style="background:#0B4D2E; color:white;">
<th style="padding:2px; text-align:left; font-size:6.5pt;">Bowl Name</th>
<th style="padding:2px; text-align:left; font-size:6.5pt;">Teams</th>
<th style="padding:2px; font-size:6.5pt;">Score</th>
</tr>'''
    for _ in range(5):
        html += '<tr><td style="border:0.5px solid #ddd; height:16px;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td></tr>'
    html += '</table>'

    html += f'{footer()}\n</div>'
    return html

def build_standings(section_title, league_tag, num_teams=16):
    """Team standings tracker page."""
    html, pnum = page_open(
        "Standings Tracker",
        league_tag,
        section_title,
        "Update each team's record every week"
    )

    for div_name in ["Division 1", "Division 2"]:
        html += f'<div class="field-label">{div_name}</div>'
        html += '''<table class="standings-table">
<tr>
<th>Team</th><th>W</th><th>L</th><th>T</th><th>PCT</th><th>PF</th><th>PA</th><th>Streak</th>
</tr>'''
        for _ in range(4):
            html += '<tr><td class="team-col"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>'
        html += '</table>'

    html += f'''
<div class="field-label">Playoff Picture</div>
<div class="checkbox-row">
  <span><span class="checkbox"></span> Division Leader</span>
  <span><span class="checkbox"></span> Wild Card</span>
  <span><span class="checkbox"></span> Eliminated</span>
</div>
{writing_lines(2)}
{footer()}
</div>'''
    return html

def build_rankings(section_title, num=12):
    """College rankings tracker."""
    html, pnum = page_open(
        "Rankings Tracker",
        "College Rankings",
        section_title,
        "Track the top teams each week"
    )

    html += '''<table class="standings-table">
<tr>
<th style="width:8%;">Rank</th>
<th>Team</th>
<th style="width:10%;">W-L</th>
<th style="width:12%;">Last Game</th>
<th style="width:12%;">Next Game</th>
</tr>'''
    for i in range(1, num + 1):
        html += f'<tr><td style="font-weight:700; color:#0B4D2E;">{i}</td><td class="team-col"></td><td></td><td></td><td></td></tr>'
    html += '</table>'

    html += f'''
<div class="field-label">Notes &amp; Observations</div>
{writing_lines(2)}
{footer()}
</div>'''
    return html

def build_player_tracker():
    """Player performance tracker."""
    html, pnum = page_open(
        "Stats Tracker",
        "Players",
        "Player Performance Tracker",
        "Follow standout players throughout the season"
    )

    html += '''<div class="field-label">Quarterbacks</div>
<table class="standings-table">
<tr><th>Player</th><th>Team</th><th>YDS</th><th>TD</th><th>INT</th><th>Rating</th></tr>'''
    for _ in range(4):
        html += '<tr><td class="team-col"></td><td></td><td></td><td></td><td></td><td></td></tr>'
    html += '</table>'

    html += '''<div class="field-label">Running Backs</div>
<table class="standings-table">
<tr><th>Player</th><th>Team</th><th>RUSH YDS</th><th>TD</th><th>REC</th><th>YDS</th></tr>'''
    for _ in range(3):
        html += '<tr><td class="team-col"></td><td></td><td></td><td></td><td></td><td></td></tr>'
    html += '</table>'

    html += '''<div class="field-label">Wide Receivers / Tight Ends</div>
<table class="standings-table">
<tr><th>Player</th><th>Team</th><th>REC</th><th>YDS</th><th>TD</th><th>Avg</th></tr>'''
    for _ in range(3):
        html += '<tr><td class="team-col"></td><td></td><td></td><td></td><td></td><td></td></tr>'
    html += '</table>'

    html += f'''
<div class="field-label">Defensive Standouts</div>
{writing_lines(2)}
{footer()}
</div>'''
    return html

def build_picks_results():
    """Weekly picks results tracker."""
    html, pnum = page_open(
        "My Picks",
        "Weekly Results",
        "My Weekly Picks Results",
        "Track how your predictions stack up all season"
    )

    html += '''<table class="standings-table">
<tr>
<th style="width:10%;">Week</th>
<th style="width:12%;">Games Picked</th>
<th style="width:12%;">Correct</th>
<th style="width:12%;">Accuracy</th>
<th>Best Pick</th>
<th>Worst Pick</th>
</tr>'''
    for week in range(1, 19):
        html += f'<tr><td style="font-weight:700; color:#0B4D2E;">{week}</td><td></td><td></td><td></td><td class="team-col"></td><td class="team-col"></td></tr>'
    html += '</table>'

    html += f'''
<div class="field-label">Season Total</div>
<div style="font-size:8pt; color:#555;">
Total Picks: <span class="fill-blank" style="width:40px;"></span> &nbsp;
Correct: <span class="fill-blank" style="width:40px;"></span> &nbsp;
Accuracy: <span class="fill-blank" style="width:50px;"></span>%
</div>
{footer()}
</div>'''
    return html

def build_top_games():
    """Top 10 games of the season."""
    html, pnum = page_open(
        "Season Wrap-Up",
        "Top Games",
        "Top 10 Games I Watched",
        "Rank the most memorable games of the season"
    )

    for i in range(1, 11):
        html += f'''<div style="margin-bottom:10px;">
<div style="display:flex; align-items:baseline;">
  <span style="font-size:14pt; font-weight:700; color:#D4A017; margin-right:8px; min-width:24px;">#{i}</span>
  <span style="font-size:8pt; font-weight:700; color:#0B4D2E;">Teams:</span>
  <span class="fill-blank" style="width:140px; margin-left:4px;"></span>
  <span style="font-size:8pt; font-weight:700; color:#0B4D2E; margin-left:10px;">Score:</span>
  <span class="fill-blank" style="width:50px; margin-left:4px;"></span>
</div>
<div style="padding-left:32px; font-size:7pt; color:#777; font-style:italic;">Why it was memorable:</div>
<div style="padding-left:32px;"><div class="wline"></div></div>
</div>'''

    html += f'{footer()}\n</div>'
    return html

def build_season_awards():
    html, pnum = page_open(
        "Season Wrap-Up",
        "My Awards",
        "Season Awards — My Picks",
        "Your personal awards for the season"
    )

    awards = [
        "Best Game of the Season",
        "Biggest Upset",
        "Most Exciting Finish",
        "Best Individual Performance",
        "Best Defensive Play",
        "Most Memorable Moment",
        "Breakout Star",
        "Biggest Disappointment",
        "Coach of the Year (My Pick)",
        "Fan of the Year (Me or a Friend)",
    ]

    for award in awards:
        html += f'''<div style="margin-bottom:7px;">
<div style="font-size:8pt; font-weight:700; color:#0B4D2E; margin-bottom:1px;">★ {esc(award)}</div>
<div class="wline"></div>
</div>'''

    html += f'{footer()}\n</div>'
    return html

def build_season_reflection():
    html, pnum = page_open(
        "Season Wrap-Up",
        "Reflection",
        "Season Reflection",
        "Looking back at the year in football"
    )

    prompts = [
        "My favorite memory from this season",
        "The game I'll never forget",
        "Most surprising thing that happened",
        "How my teams performed vs. expectations",
        "What I loved most about this season",
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
        "My bold prediction for next season",
        "Teams I'll be watching closely",
        "Players I'm excited to see develop",
        "Games already circled on my calendar",
        "What I want to do differently as a fan",
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

def build_divider(part_num, label, title, subtitle):
    pn()
    return f'''<div class="divider">
  <div class="div-yard"></div>
  <div class="div-num">{part_num}</div>
  <div style="position:relative; text-align:center;">
    <div class="div-label">{esc(label)}</div>
    <div class="div-title">{esc(title)}</div>
    <div class="div-sub">{esc(subtitle)}</div>
  </div>
</div>'''

# ============================================================
# MAIN
# ============================================================
def main():
    pages = []

    # === FRONT MATTER ===
    pages.append(build_cover())
    pages.append(build_owner_page())
    pages.append(build_how_to_use())
    pages.append(build_my_teams())
    pages.append(build_predictions())
    pages.append(build_division_ref())
    pages.append(build_conference_ref())
    pages.append(build_season_calendar())

    # === SECTION 1: NFL GAME TRACKER ===
    pages.append(build_divider("01", "Part One", "Pro League\nGame Tracker", "One page per game — track every matchup"))

    # Weeks 1-18
    for week in range(1, 19):
        pages.append(build_game_tracker(f"Week {week}", "PRO"))
    # Bonus game pages (for multiple games per week)
    for i in range(1, 11):
        pages.append(build_game_tracker(f"Bonus Game #{i}", "PRO"))

    # === SECTION 2: NCAA GAME TRACKER ===
    pages.append(build_divider("02", "Part Two", "College\nGame Tracker", "Track every college game you watch"))

    for i in range(1, 17):
        pages.append(build_game_tracker(f"College Game #{i}", "NCAA"))

    # === SECTION 3: PLAYOFFS ===
    pages.append(build_divider("03", "Part Three", "Playoffs\n& Championships", "Fill in the brackets and crown your champion"))

    # Pro league bracket (2 pages)
    bracket_pages = build_playoff_bracket()
    pages.extend(bracket_pages)
    # College playoff bracket
    pages.append(build_cfp_bracket())
    # Playoff notes
    pages.append(build_notes_page("Playoff Notes", "Strategic thoughts, predictions, and results"))

    # === SECTION 4: STATS & STANDINGS ===
    pages.append(build_divider("04", "Part Four", "Standings\n& Statistics", "Track team records and player stats"))

    # Pro standings (2 pages)
    pages.append(build_standings("Pro League Standings", "Pro League"))
    pages.append(build_standings("Pro League Standings (cont.)", "Pro League"))
    # College rankings (2 pages)
    pages.append(build_rankings("College Rankings — Top 12"))
    pages.append(build_rankings("College Rankings — Next 12", num=12))
    # Player tracker (2 pages)
    pages.append(build_player_tracker())
    pages.append(build_player_tracker())

    # === SECTION 5: PICKS & WRAP-UP ===
    pages.append(build_divider("05", "Part Five", "My Picks\n& Season Wrap-Up", "Track your predictions and reflect on the year"))

    pages.append(build_picks_results())
    pages.append(build_top_games())
    pages.append(build_season_awards())
    pages.append(build_season_reflection())
    pages.append(build_looking_forward())

    # === SECTION 6: NOTES ===
    pages.append(build_divider("06", "Part Six", "Personal\nNotes", "Your space for thoughts, ideas, and memories"))

    for _ in range(46):
        pages.append(build_notes_page())

    # === BACK COVER ===
    pages.append(build_back_cover())

    # === Assemble ===
    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(BOOK_TITLE)} — {esc(BOOK_SUBTITLE)}</title>
<style>{CSS}</style>
</head>
<body>
{"".join(pages)}
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
