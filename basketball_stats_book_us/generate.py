#!/usr/bin/env python3
"""
Basketball Stats Book — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: American basketball fans (NBA + NCAA)
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "basketball_stats_book_us_V1.0.html")

BOOK_TITLE = "Basketball Stats Book"
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
/* Court wood: #C97A3D, #B5642A */
/* Basketball orange: #E8731C, #D45F0F */
/* Accent navy: #1A2B50 */
/* Light: #f5f5f5 */

/* ---- Cover ---- */
.cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(180deg, #14213D 0%, #1A2B50 40%, #14213D 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Court lines on cover */
.cover .court-lines {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image:
    repeating-linear-gradient(
      90deg,
      transparent,
      transparent 40px,
      rgba(255,255,255,0.06) 40px,
      rgba(255,255,255,0.06) 42px
    );
}

/* CSS Basketball */
.cover .basketball {
  width: 110px; height: 110px;
  background: radial-gradient(circle at 35% 35%, #f08c30, #D45F0F 70%, #a84500);
  border-radius: 50%;
  position: relative;
  margin: 0 auto 20px;
  box-shadow: 3px 3px 12px rgba(0,0,0,0.5);
}
.cover .basketball::before {
  content: "";
  position: absolute;
  top: 0; left: 50%;
  width: 1.5px; height: 100%;
  background: #1a1a1a;
  transform: translateX(-50%);
}
.cover .basketball::after {
  content: "";
  position: absolute;
  top: 50%; left: 0;
  width: 100%; height: 1.5px;
  background: #1a1a1a;
  transform: translateY(-50%);
}
.cover .basketball-curves {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  border-radius: 50%;
  overflow: hidden;
}
.cover .basketball-curves::before {
  content: "";
  position: absolute;
  top: 0; left: 0;
  width: 60%; height: 100%;
  border-right: 1.5px solid #1a1a1a;
  border-radius: 50% / 100%;
}
.cover .basketball-curves::after {
  content: "";
  position: absolute;
  top: 0; right: 0;
  width: 60%; height: 100%;
  border-left: 1.5px solid #1a1a1a;
  border-radius: 50% / 100%;
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
  background: #E8731C;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 12pt;
  color: #aab8d8;
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
  border: 1px solid rgba(232,115,28,0.5);
  color: #E8731C;
  font-size: 7.5pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 10px;
  border-radius: 3px;
  text-transform: uppercase;
}

.cover .season-tag {
  font-size: 9pt;
  color: #8ba3d8;
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
  color: #E8731C;
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
  background: #1A2B50;
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
  color: rgba(232,115,28,0.12);
  font-weight: 700;
  position: absolute;
  top: 1in;
}
.divider .div-label {
  font-size: 10pt;
  color: #E8731C;
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
  color: #8ba3d8;
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
  border-bottom: 1.5px solid #1A2B50;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #1A2B50;
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
  color: #1A2B50;
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
  background: #1A2B50;
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
  color: #1A2B50;
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

/* ---- Bracket ---- */
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
  color: #1A2B50;
  margin-bottom: 10px;
  border-bottom: 2px solid #E8731C;
  padding-bottom: 5px;
}

/* ---- Standings ---- */
.standings-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 7.5pt;
  margin-bottom: 10px;
}
.standings-table th {
  background: #1A2B50;
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
  width: 45px; height: 45px;
  background: radial-gradient(circle at 35% 35%, #f08c30, #D45F0F);
  border-radius: 50%;
  margin: 0 auto 20px;
  position: relative;
}
.owner-page .owner-icon::before {
  content: "";
  position: absolute;
  top: 0; left: 50%;
  width: 1px; height: 100%;
  background: #1a1a1a;
  transform: translateX(-50%);
}
.owner-page .owner-icon::after {
  content: "";
  position: absolute;
  top: 50%; left: 0;
  width: 100%; height: 1px;
  background: #1a1a1a;
  transform: translateY(-50%);
}
.owner-page .owner-title {
  font-size: 20pt;
  font-weight: 700;
  color: #1A2B50;
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
  color: #1A2B50;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  margin-bottom: 2px;
}
.owner-line .ol-blank {
  border-bottom: 1px solid #999;
  height: 20px;
}

/* ---- Series Tracker ---- */
.series-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 7.5pt;
  margin-bottom: 8px;
}
.series-table th {
  background: #1A2B50;
  color: white;
  padding: 3px 4px;
  font-size: 7pt;
  font-weight: 700;
  text-align: center;
}
.series-table td {
  border: 0.5px solid #999;
  padding: 4px;
  font-size: 7.5pt;
  height: 22px;
}
.series-table td.game-col {
  text-align: center;
  font-weight: 700;
  color: #1A2B50;
  width: 10%;
}

/* ---- Back Cover ---- */
.back-cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: auto;
  background: linear-gradient(180deg, #14213D 0%, #1A2B50 100%);
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
  color: #E8731C;
  font-weight: 700;
  margin-bottom: 12px;
  letter-spacing: 1pt;
}
.back-cover .bc-text {
  font-size: 9pt;
  color: #aab8d8;
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
  color: #E8731C;
}
.back-cover .bc-publisher {
  font-size: 9pt;
  color: #E8731C;
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

# ============================================================
# PAGE BUILDERS
# ============================================================

def build_cover():
    pn()
    return '''<div class="cover">
  <div class="court-lines"></div>
  <div class="title-block">
    <div class="basketball">
      <div class="basketball-curves"></div>
    </div>
    <div class="main-title">BASKETBALL<br/>STATS BOOK</div>
    <div class="accent-bar"></div>
    <div class="subtitle">Your Ultimate Season Journal<br/>for Pro &amp; College Basketball</div>
    <div class="features">
      <span class="feature-badge">Box Scores</span>
      <span class="feature-badge">Playoff Brackets</span>
      <span class="feature-badge">Team Stats</span>
      <span class="feature-badge">Season Notes</span>
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
    <div class="bc-title">&#9733; A Perfect Gift for Basketball Fans &#9733;</div>
    <p class="bc-text">Whether you're a die-hard fan or a casual viewer, this book helps you capture every thrilling moment of the basketball season.</p>
    <ul class="bc-features">
      <li>Track box scores for pro &amp; college games</li>
      <li>Fill in playoff brackets and championship results</li>
      <li>Monitor team standings all season long</li>
      <li>Record your predictions, picks, and reflections</li>
      <li>Track player stats and standout performances</li>
      <li>Plenty of space for personal notes and memories</li>
    </ul>
    <p class="bc-text" style="font-style:italic;">Tip off your season and never forget a game!</p>
  </div>
  <div class="bc-publisher">More Shine Press</div>
</div>'''

def build_owner_page():
    pn()
    return f'''<div class="page">
<div class="owner-page">
  <div class="owner-icon"></div>
  <div class="owner-title">This Book Belongs To</div>
  <div class="owner-sub">Fill in your details below</div>
  <div class="owner-line">
    <div class="ol-label">Name</div>
    <div class="ol-blank"></div>
  </div>
  <div class="owner-line">
    <div class="ol-label">Favorite Pro Team</div>
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
        ("Game Tracker", "Use one page per game. Fill in the teams, scores by quarter (or half for college), and jot down the key plays that made the difference."),
        ("Playoff Brackets", "Fill in the teams as they advance through the playoffs. For pro leagues, track each best-of-seven series game by game."),
        ("Standings & Stats", "Update team records regularly. Track your weekly picks and see how you perform against the experts."),
        ("Tournament Bracket", "Use the bracket to fill in all 64 teams and track every upset and Cinderella story."),
    ]
    html = f'''<div class="page">
{sh("Getting Started", "How to Use This Book")}
<div class="page-title">How to Use This Book</div>
<div class="page-subtitle">A quick guide to getting the most out of your season journal</div>
'''
    for i, (title, desc) in enumerate(tips, 1):
        html += f'''<div style="margin-bottom: 12px;">
<div style="display:flex; align-items:baseline; margin-bottom:2px;">
<span style="font-size:14pt; font-weight:700; color:#E8731C; margin-right:6px;">{i}</span>
<span style="font-size:10pt; font-weight:700; color:#1A2B50;">{esc(title)}</span>
</div>
<p style="font-size:8pt; color:#555; line-height:1.6; padding-left:20px;">{esc(desc)}</p>
</div>'''

    html += f'''<div style="margin-top:20px; padding:10px; background:#f5f5f5; border-left:3px solid #E8731C;">
<div style="font-size:7.5pt; font-weight:700; color:#1A2B50; text-transform:uppercase; letter-spacing:0.8pt; margin-bottom:5px;">Pro Tip</div>
<p style="font-size:8pt; color:#555; line-height:1.5;">Keep this book handy while watching games. Fill in the scores as they happen, then add your notes after the final buzzer. By season's end, you'll have a complete record of your basketball year!</p>
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
<div class="page-subtitle">Make your picks before the season tips off — check back at the end!</div>

<div class="field-label">Pro League Champion Prediction</div>
{writing_lines(1)}

<div class="field-label">College National Champion Prediction</div>
{writing_lines(1)}

<div class="field-label">MVP Pick</div>
{writing_lines(1)}

<div class="field-label">Player of the Year Pick</div>
{writing_lines(1)}

<div class="field-label">Breakout Team of the Year</div>
{writing_lines(1)}

<div class="field-label">Surprise / Upset Team</div>
{writing_lines(1)}

<div class="field-label">Scoring Leader Prediction</div>
{writing_lines(1)}

<div class="field-label">Record Predictions for My Teams</div>
<table style="width:100%; font-size:8pt; border-collapse:collapse; margin-top:4px;">
<tr style="background:#1A2B50; color:white;">
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
    pn()
    divisions = [
        ("Pro League — Eastern Conference", [
            ("Atlantic Division", 5), ("Central Division", 5), ("Southeast Division", 5)
        ]),
        ("Pro League — Western Conference", [
            ("Northwest Division", 5), ("Pacific Division", 5), ("Southwest Division", 5)
        ]),
    ]

    html = f'''<div class="page">
{sh("Reference", "Team Divisions")}
<div class="page-title">Pro League Divisions</div>
<div class="page-subtitle">Reference guide — fill in teams as you track your season</div>
'''
    for league, divs in divisions:
        html += f'<div class="field-label" style="margin-top:4px;">{esc(league)}</div>'
        html += '<table style="width:100%; font-size:7pt; border-collapse:collapse;">'
        for div_name, count in divs:
            html += f'<tr><td style="border:0.5px solid #aaa; background:#e8ecf5; padding:2px 5px; font-weight:700; font-size:6.5pt; color:#1A2B50; width:40%;">{esc(div_name)}</td>'
            html += '<td style="border:0.5px solid #aaa; height:14px;"></td></tr>'
            for _ in range(count - 1):
                html += '<tr><td style="border:0.5px solid #aaa;"></td><td style="border:0.5px solid #aaa; height:14px;"></td></tr>'
        html += '</table>'

    html += f'''<div class="field-label" style="margin-top:10px;">Play-In Tournament Notes</div>
{writing_lines(2)}
{footer()}
</div>'''
    return html

def build_conference_ref():
    pn()
    html = f'''<div class="page">
{sh("Reference", "College Conferences")}
<div class="page-title">College Basketball Conferences</div>
<div class="page-subtitle">Reference guide — fill in key teams as you track your season</div>
'''
    conferences = [
        ("ACC", 4), ("Big Ten", 4), ("Big 12", 4),
        ("SEC", 4), ("Pac-12", 3), ("Big East", 3),
        ("American", 2), ("Mid-Major / Others", 3),
    ]

    html += '<table style="width:100%; font-size:7pt; border-collapse:collapse;">'
    for conf, count in conferences:
        html += f'<tr><td style="border:0.5px solid #aaa; background:#e8ecf5; padding:2px 5px; font-weight:700; font-size:6.5pt; color:#1A2B50; width:40%;">{esc(conf)}</td>'
        html += '<td style="border:0.5px solid #aaa; height:14px;"></td></tr>'
        for _ in range(count - 1):
            html += '<tr><td style="border:0.5px solid #aaa;"></td><td style="border:0.5px solid #aaa; height:14px;"></td></tr>'
    html += '</table>'

    html += f'''
<div class="field-label" style="margin-top:12px;">Conference Tournament Notes</div>
{writing_lines(2)}

<div class="field-label">Rivalry Games to Watch</div>
{writing_lines(3)}

<div class="field-label">Tournament Notes</div>
{writing_lines(3)}

{footer()}
</div>'''
    return html

def build_season_calendar():
    pn()
    months = ["October", "November", "December", "January", "February", "March", "April", "May", "June"]
    html = f'''<div class="page">
{sh("Reference", "Season Calendar")}
<div class="page-title">Season at a Glance</div>
<div class="page-subtitle">Mark key dates, big games, and events throughout the season</div>
'''
    for month in months:
        html += f'<div class="field-label" style="margin-top:3px;">{month}</div>'
        html += writing_lines(2)

    html += f'''<div class="field-label" style="margin-top:8px;">Important Dates &amp; Events</div>
{writing_lines(2)}
{footer()}
</div>'''
    return html

def build_game_tracker(week_label, league_tag="PRO"):
    """One game tracking page — basketball scoring by quarter/half."""
    html, pnum = page_open(
        f"Game Tracker — {league_tag}",
        week_label,
        "Game Tracker",
        "Record every detail of the game"
    )

    if league_tag == "NCAA":
        q_labels = ["1st Half", "2nd Half", "OT", ""]
    else:
        q_labels = ["Q1", "Q2", "Q3", "Q4"]

    html += f'''
<div style="display:flex; justify-content:space-between; margin-bottom:8px;">
  <div style="font-size:8pt; font-weight:700; color:#1A2B50;">{esc(week_label)}</div>
  <div style="font-size:8pt; color:#777;">Date: <span class="fill-blank" style="width:60px;"></span></div>
</div>

<table class="score-table">
<tr>
<th style="width:32%;">Team</th>'''

    for ql in q_labels:
        if ql:
            html += f'<th>{esc(ql)}</th>'

    html += '<th style="background:#E8731C;">FINAL</th>\n</tr>\n'

    for role in ["HOME", "AWAY"]:
        html += f'''<tr>
<td class="team-cell">
  <span style="font-size:6pt; color:#aaa;">{role}:</span><br/>
  <span style="border-bottom:0.5px solid #999; display:inline-block; width:85%; height:14px;"></span>
</td>'''
        for ql in q_labels:
            if ql:
                html += '<td class="score-input"></td>'
        html += '<td class="score-input final-cell"></td>\n</tr>\n'

    html += '</table>'

    html += '''
<div style="font-size:7pt; color:#aaa; margin-bottom:4px;">Venue: <span class="fill-blank" style="width:100px;"></span> &nbsp; Attendance: <span class="fill-blank" style="width:60px;"></span> &nbsp; TV: <span class="fill-blank" style="width:50px;"></span></div>

<div class="field-label">Key Plays &amp; Highlights <span class="small-note">big shots, runs, turnovers, clutch moments</span></div>
'''
    html += writing_lines(4)

    html += '''
<div style="display:flex; justify-content:space-between; margin-top:6px;">
  <div style="font-size:7.5pt; font-weight:700; color:#1A2B50;">Star Player of the Game</div>
  <div style="font-size:7.5pt; font-weight:700; color:#1A2B50;">Game Rating</div>
</div>
<div style="display:flex; justify-content:space-between; margin-bottom:4px;">
  <span class="fill-blank" style="width:120px;"></span>
  <span style="font-size:7pt; color:#777;">Points: <span class="fill-blank" style="width:30px;"></span></span>
  <span class="stars">&#9734; &#9734; &#9734; &#9734; &#9734;</span>
</div>

<div class="field-label">Team Stats Comparison</div>
<table style="width:100%; font-size:7pt; border-collapse:collapse;">
<tr style="background:#f5f5f5;">
<th style="padding:2px; text-align:left; font-size:6.5pt; width:24%;"></th>
<th style="padding:2px; font-size:6.5pt; width:19%;">FG%</th>
<th style="padding:2px; font-size:6.5pt; width:19%;">3PT%</th>
<th style="padding:2px; font-size:6.5pt; width:19%;">FT%</th>
<th style="padding:2px; font-size:6.5pt; width:19%;">REB</th>
</tr>
<tr><td style="border:0.5px solid #ddd; font-size:6.5pt; color:#aaa;">Home</td><td style="border:0.5px solid #ddd; height:14px;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td></tr>
<tr><td style="border:0.5px solid #ddd; font-size:6.5pt; color:#aaa;">Away</td><td style="border:0.5px solid #ddd; height:14px;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td><td style="border:0.5px solid #ddd;"></td></tr>
</table>

<div class="field-label">My Thoughts &amp; Notes</div>
'''
    html += writing_lines(3)

    html += f'''
<div style="font-size:7pt; color:#aaa; margin-top:2px;">Pick correct? <span class="checkbox"></span> Yes &nbsp; Overtime? <span class="checkbox"></span> Yes &nbsp; Watched live? <span class="checkbox"></span> Yes &nbsp; Buzzer beater? <span class="checkbox"></span> Yes</div>

{footer()}
</div>'''
    return html

def build_playoff_series():
    """Pro playoff series tracker — best-of-7 format."""
    html, pnum = page_open(
        "Playoff Tracker",
        "Pro League Series",
        "Playoff Series Tracker",
        "Track each best-of-seven series game by game"
    )

    for series_num in range(1, 3):
        html += f'''
<div style="border:1px solid #1A2B50; padding:8px; margin-bottom:8px; border-radius:3px;">
<div style="font-size:8pt; font-weight:700; color:#1A2B50; text-transform:uppercase; letter-spacing:0.5pt; margin-bottom:4px;">Series {series_num}</div>
<div style="display:flex; justify-content:space-between; margin-bottom:4px;">
  <span class="fill-blank" style="width:120px; height:14px;"></span>
  <span style="font-size:8pt; color:#aaa;">vs</span>
  <span class="fill-blank" style="width:120px; height:14px;"></span>
</div>
<table class="series-table">
<tr><th>Game</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th></tr>
<tr><td class="game-col">Away Score</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td class="game-col">Home Score</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td class="game-col">Series Lead</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
</table>
<div style="font-size:6.5pt; color:#aaa; font-style:italic;">Series Result: <span class="fill-blank" style="width:150px;"></span> wins <span class="fill-blank" style="width:20px;"></span>-<span class="fill-blank" style="width:20px;"></span></div>
</div>'''

    html += f'''<div class="field-label">Playoff Notes</div>
{writing_lines(3)}
{footer()}
</div>'''
    return html

def build_finals_page():
    """Championship finals page."""
    html, pnum = page_open(
        "Playoff Tracker",
        "The Finals",
        "The Championship Finals",
        "The biggest stage — track every game of the finals"
    )

    html += '''
<div style="border:2px solid #E8731C; padding:12px; margin-bottom:8px; background:#fffbf5; border-radius:4px;">
<div style="text-align:center; font-size:10pt; font-weight:700; color:#E8731C; text-transform:uppercase; letter-spacing:1pt; margin-bottom:8px;">&#9733; Championship Series &#9733;</div>
<div style="display:flex; justify-content:space-between; margin-bottom:6px;">
  <span class="fill-blank" style="width:130px; height:16px;"></span>
  <span style="font-size:10pt; font-weight:700; color:#E8731C;">VS</span>
  <span class="fill-blank" style="width:130px; height:16px;"></span>
</div>
</div>

<table class="series-table">
<tr><th>Game</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th></tr>
<tr><td class="game-col">Away</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td class="game-col">Home</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td class="game-col">Winner</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
</table>

<div style="font-size:8pt; color:#555; margin-top:8px;">
<div>Series Result: <span class="fill-blank" style="width:140px;"></span> win <span class="fill-blank" style="width:20px;"></span>-<span class="fill-blank" style="width:20px;"></span></div>
<div style="margin-top:4px;">Finals MVP: <span class="fill-blank" style="width:140px;"></span></div>
</div>

<div class="field-label">My Finals Experience</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">Where did you watch? Who were you with? What was the best moment?</div>
'''
    html += writing_lines(4)
    html += f'{footer()}\n</div>'
    return html

def build_march_madness():
    """Tournament bracket — 2 pages."""
    pages = []
    for part in [1, 2]:
        html, pnum = page_open(
            "Tournament Tracker",
            f"Tournament Bracket — Round {part}" if part == 1 else "Tournament Bracket — Final Rounds",
            "Tournament Bracket" if part == 1 else "Tournament Bracket (cont.)",
            "Fill in teams as the tournament advances"
        )
        if part == 1:
            html += '<div class="field-label">First Round &amp; Second Round</div>'
            html += '<div style="display:grid; grid-template-columns:1fr 1fr; gap:4px;">'
            for i in range(16):
                html += f'''<div class="bracket-slot" style="min-height:22px;">
<div class="slot-team"></div><div class="slot-team"></div>
<div style="font-size:5.5pt; color:#ccc;">Score: ______</div>
</div>'''
            html += '</div>'
            html += '<div class="field-label" style="margin-top:4px;">Regional Semifinals</div>'
            html += '<div style="display:grid; grid-template-columns:1fr 1fr; gap:6px;">'
            for i in range(8):
                html += f'''<div class="bracket-slot" style="min-height:22px;">
<div class="slot-team"></div><div class="slot-team"></div>
<div style="font-size:5.5pt; color:#ccc;">Score: ______</div>
</div>'''
            html += '</div>'
        else:
            html += '<div class="field-label">Regional Finals</div>'
            html += '<div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">'
            for i in range(4):
                html += f'''<div class="bracket-slot" style="min-height:30px;">
<div class="slot-label">Regional Final</div>
<div class="slot-team"></div><div class="slot-team"></div>
<div style="font-size:5.5pt; color:#ccc;">Score: ______</div>
</div>'''
            html += '</div>'

            html += '<div class="field-label" style="margin-top:8px;">Semifinals</div>'
            html += '<div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">'
            for label in ["Semifinal 1", "Semifinal 2"]:
                html += f'''<div class="bracket-slot" style="min-height:36px;">
<div class="slot-label">{label}</div>
<div class="slot-team"></div><div class="slot-team"></div>
<div style="font-size:5.5pt; color:#ccc;">Score: ______</div>
</div>'''
            html += '</div>'

            html += '''
<div class="field-label" style="margin-top:10px; text-align:center; font-size:10pt;">&#9733; NATIONAL CHAMPIONSHIP &#9733;</div>
<div style="border:2px solid #E8731C; padding:10px; margin-top:4px; text-align:center; background:#fffbf5;">
<div style="display:flex; justify-content:center; gap:16px; margin-bottom:6px;">
  <span class="fill-blank" style="width:110px;"></span>
  <span style="font-size:10pt; font-weight:700; color:#E8731C;">VS</span>
  <span class="fill-blank" style="width:110px;"></span>
</div>
<div style="font-size:7.5pt; color:#555;">Final Score: <span class="fill-blank" style="width:50px;"></span> — <span class="fill-blank" style="width:50px;"></span></div>
<div style="font-size:7.5pt; color:#555;">National Champion: <span class="fill-blank" style="width:120px;"></span></div>
<div style="font-size:7.5pt; color:#555;">MOP (Most Outstanding Player): <span class="fill-blank" style="width:120px;"></span></div>
</div>

<div class="field-label">Biggest Upset of the Tournament</div>
<div class="wline"></div>
'''
        html += f'{footer()}\n</div>'
        pages.append(html)
    return pages

def build_standings(section_title, league_tag):
    html, pnum = page_open(
        "Standings Tracker",
        league_tag,
        section_title,
        "Update each team's record regularly"
    )

    for conf in ["Conference A", "Conference B"]:
        html += f'<div class="field-label">{conf}</div>'
        html += '''<table class="standings-table">
<tr>
<th>Team</th><th>W</th><th>L</th><th>PCT</th><th>GB</th><th>HOME</th><th>AWAY</th><th>STRK</th>
</tr>'''
        for _ in range(5):
            html += '<tr><td class="team-col"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>'
        html += '</table>'

    html += f'''
<div class="field-label">Playoff Picture</div>
<div class="checkbox-row">
  <span><span class="checkbox"></span> Top 6 Seed</span>
  <span><span class="checkbox"></span> Play-In Spot</span>
  <span><span class="checkbox"></span> Eliminated</span>
</div>
{writing_lines(2)}
{footer()}
</div>'''
    return html

def build_player_tracker():
    html, pnum = page_open(
        "Stats Tracker",
        "Players",
        "Player Performance Tracker",
        "Follow standout players throughout the season"
    )

    html += '''<div class="field-label">Scoring Leaders</div>
<table class="standings-table">
<tr><th>Player</th><th>Team</th><th>PPG</th><th>RPG</th><th>APG</th><th>FG%</th></tr>'''
    for _ in range(5):
        html += '<tr><td class="team-col"></td><td></td><td></td><td></td><td></td><td></td></tr>'
    html += '</table>'

    html += '''<div class="field-label">All-Around Players</div>
<table class="standings-table">
<tr><th>Player</th><th>Team</th><th>SPG</th><th>BPG</th><th>3PT%</th><th>FT%</th></tr>'''
    for _ in range(4):
        html += '<tr><td class="team-col"></td><td></td><td></td><td></td><td></td><td></td></tr>'
    html += '</table>'

    html += '''<div class="field-label">Rookies to Watch</div>
<table class="standings-table">
<tr><th>Player</th><th>Team</th><th>PPG</th><th>RPG</th><th>APG</th><th>Notes</th></tr>'''
    for _ in range(3):
        html += '<tr><td class="team-col"></td><td></td><td></td><td></td><td></td><td></td></tr>'
    html += '</table>'

    html += f'''
<div class="field-label">My Player Notes</div>
{writing_lines(2)}
{footer()}
</div>'''
    return html

def build_picks_results():
    html, pnum = page_open(
        "My Picks",
        "Weekly Results",
        "My Weekly Picks Results",
        "Track how your predictions stack up all season"
    )

    html += '''<table class="standings-table">
<tr>
<th style="width:12%;">Week</th>
<th style="width:13%;">Games Picked</th>
<th style="width:11%;">Correct</th>
<th style="width:12%;">Accuracy</th>
<th>Best Pick</th>
<th>Worst Pick</th>
</tr>'''
    for week in range(1, 27):
        html += f'<tr><td style="font-weight:700; color:#1A2B50;">{week}</td><td></td><td></td><td></td><td class="team-col"></td><td class="team-col"></td></tr>'
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
    html, pnum = page_open(
        "Season Wrap-Up",
        "Top Games",
        "Top 10 Games I Watched",
        "Rank the most memorable games of the season"
    )

    for i in range(1, 11):
        html += f'''<div style="margin-bottom:10px;">
<div style="display:flex; align-items:baseline;">
  <span style="font-size:14pt; font-weight:700; color:#E8731C; margin-right:8px; min-width:24px;">#{i}</span>
  <span style="font-size:8pt; font-weight:700; color:#1A2B50;">Teams:</span>
  <span class="fill-blank" style="width:140px; margin-left:4px;"></span>
  <span style="font-size:8pt; font-weight:700; color:#1A2B50; margin-left:10px;">Score:</span>
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
        "Best Defensive Performance",
        "Most Memorable Moment",
        "Breakout Star",
        "Biggest Disappointment",
        "Coach of the Year (My Pick)",
        "Fan of the Year (Me or a Friend)",
    ]

    for award in awards:
        html += f'''<div style="margin-bottom:7px;">
<div style="font-size:8pt; font-weight:700; color:#1A2B50; margin-bottom:1px;">&#9733; {esc(award)}</div>
<div class="wline"></div>
</div>'''

    html += f'{footer()}\n</div>'
    return html

def build_season_reflection():
    html, pnum = page_open(
        "Season Wrap-Up",
        "Reflection",
        "Season Reflection",
        "Looking back at the year in basketball"
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
  <div class="div-lines"></div>
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

    # === SECTION 1: PRO GAME TRACKER ===
    pages.append(build_divider("01", "Part One", "Pro League\nGame Tracker", "One page per game — track every matchup"))

    # Regular season games
    for i in range(1, 27):
        pages.append(build_game_tracker(f"Game #{i}", "PRO"))
    # Bonus pages
    for i in range(1, 9):
        pages.append(build_game_tracker(f"Bonus Game #{i}", "PRO"))

    # === SECTION 2: COLLEGE GAME TRACKER ===
    pages.append(build_divider("02", "Part Two", "College\nGame Tracker", "Track every college game you watch"))

    for i in range(1, 21):
        pages.append(build_game_tracker(f"College Game #{i}", "NCAA"))

    # === SECTION 3: PLAYOFFS ===
    pages.append(build_divider("03", "Part Three", "Playoffs\n& Championships", "Track every series and crown your champion"))

    # Pro playoff series (4 pages, 2 series each)
    for _ in range(4):
        pages.append(build_playoff_series())
    # Finals
    pages.append(build_finals_page())
    # Tournament bracket (2 pages)
    mm_pages = build_march_madness()
    pages.extend(mm_pages)
    # Playoff notes
    pages.append(build_notes_page("Playoff Notes", "Strategic thoughts, predictions, and results"))

    # === SECTION 4: STATS & STANDINGS ===
    pages.append(build_divider("04", "Part Four", "Standings\n& Statistics", "Track team records and player stats"))

    pages.append(build_standings("Pro League Standings", "Pro League"))
    pages.append(build_standings("Pro League Standings (cont.)", "Pro League"))
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

    for _ in range(26):
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
