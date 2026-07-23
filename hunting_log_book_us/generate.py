#!/usr/bin/env python3
"""
Hunting Log Book — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Hunters (deer, elk, waterfowl, small game)
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "hunting_log_book_us_V1.0.html")

BOOK_TITLE = "Hunting Log Book"
BOOK_SUBTITLE = "Track Every Hunt, Every Season, Every Memory"

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
  background: linear-gradient(165deg, #0D1B0A 0%, #1A2E12 30%, #0D1B0A 65%, #060F05 100%);
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #4A7C2E, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #6B5D3D, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #4A7C2E, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #6B5D3D, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #4A7C2E, transparent);
}

.cover .title-main {
  font-size: 32pt;
  font-weight: 700;
  color: #FAF6F0;
  line-height: 1.2;
  letter-spacing: 1pt;
  position: relative;
  z-index: 2;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 100px; height: 2px;
  background: #4A7C2E;
  margin: 20px auto;
  position: relative;
  z-index: 2;
}

.cover .subtitle {
  font-size: 12pt;
  color: #8F9D6E;
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
  color: #4A7C2E;
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
  color: #0D1B0A;
  letter-spacing: 0.5pt;
  text-transform: uppercase;
}

.section-line {
  flex: 1;
  height: 1px;
  background: #4A7C2E;
  margin: 0 12px;
  opacity: 0.4;
}

/* ================ HUNT LOG LEFT ================ */
.hunt-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1.5px solid #4A7C2E;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.hunt-banner .hb-num {
  display: inline-block;
  border: 1.5px solid #4A7C2E;
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 8pt;
  color: #4A7C2E;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.hunt-banner .hb-label {
  font-size: 8pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.hunt-banner .hb-line {
  flex: 1;
  height: 12px;
  border-bottom: 1px dotted #ccc;
}

.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
  margin-bottom: 8px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #4A7C2E;
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
  border: 1.5px solid #4A7C2E;
  border-radius: 2px;
}

/* Weather */
.weather-box {
  border: 1px solid #4A7C2E;
  border-radius: 4px;
  padding: 6px 8px;
  margin-bottom: 8px;
  background: #F5F2EC;
}

.weather-box .wb-label {
  font-size: 7pt;
  color: #4A7C2E;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 3px;
}

.weather-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 6px;
}

.weather-field .wf-label {
  font-size: 6pt;
  color: #aaa;
  text-transform: uppercase;
  display: block;
}

.weather-field .wf-write {
  height: 14px;
  border-bottom: 1px dotted #ccc;
}

/* Game details table */
.game-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 6px;
}

.game-table th {
  font-size: 6.5pt;
  color: #4A7C2E;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 4px 3px;
  border-bottom: 1.5px solid #4A7C2E;
  text-align: center;
}

.game-table th:first-child { text-align: left; }

.game-table td {
  padding: 4px 3px;
  border-bottom: 1px solid #eee;
  height: 24px;
}

/* Shot log */
.shot-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
  font-size: 8pt;
}

.shot-num {
  width: 16px; height: 16px;
  border: 1.5px solid #4A7C2E;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 6pt;
  color: #4A7C2E;
  flex-shrink: 0;
}

.shot-line {
  flex: 1;
  height: 14px;
  border-bottom: 1px dotted #ccc;
}

/* Gear */
.gear-box {
  border-left: 3px solid #6B5D3D;
  padding: 6px 10px;
  margin-bottom: 8px;
  background: #F5F2EC;
}

.gear-box .gb-label {
  font-size: 7pt;
  color: #6B5D3D;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 3px;
}

.gear-box .gb-line {
  height: 14px;
  border-bottom: 1px dotted #ccc;
  margin-bottom: 3px;
}

/* Notes */
.write-box {
  border: 1px solid #C4A04A;
  border-radius: 3px;
  padding: 6px 8px;
  margin-bottom: 8px;
}

.write-box .wb-label {
  font-size: 7pt;
  color: #4A7C2E;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 3px;
}

.write-box .wb-area {
  height: 28px;
}

/* Rating */
.rating-row {
  display: flex;
  align-items: center;
  gap: 4px;
  margin-bottom: 5px;
}

.rating-row .rr-label {
  font-size: 8pt;
  width: 80px;
  flex-shrink: 0;
}

.rating-circle {
  width: 12px; height: 12px;
  border: 1.5px solid #4A7C2E;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 5pt;
  color: #4A7C2E;
  margin-right: 1px;
}

/* How-to */
.howto-text { font-size: 10pt; line-height: 1.7; }
.howto-text p { margin-bottom: 8px; }
.howto-text .ht-title {
  font-size: 11pt; font-weight: 700; color: #0D1B0A;
  margin-bottom: 4px; margin-top: 6px;
}
.howto-text .ht-icon { color: #4A7C2E; font-weight: 700; margin-right: 4px; }

/* Season summary */
.summary-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
}

.summary-table th {
  font-size: 7pt;
  color: #4A7C2E;
  text-transform: uppercase;
  padding: 5px 4px;
  border-bottom: 1.5px solid #4A7C2E;
  text-align: center;
}

.summary-table th:first-child { text-align: left; }

.summary-table td {
  padding: 5px 4px;
  border-bottom: 1px solid #eee;
  height: 22px;
}

/* Notes */
.notes-line { border-bottom: 1px solid #ddd; height: 22px; }

/* Final */
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
  width: 60px; height: 1.5px; background: #4A7C2E;
  margin: 12px auto; opacity: 0.5;
}
"""

def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- Crosshair / target -->
      <circle cx="50" cy="50" r="38" stroke="#4A7C2E" stroke-width="1.5" fill="none" opacity="0.4"/>
      <circle cx="50" cy="50" r="28" stroke="#4A7C2E" stroke-width="1.5" fill="none"/>
      <circle cx="50" cy="50" r="18" stroke="#4A7C2E" stroke-width="1" fill="none" opacity="0.6"/>
      <circle cx="50" cy="50" r="4" fill="#4A7C2E" opacity="0.6"/>
      <!-- Crosshair lines -->
      <line x1="50" y1="2" x2="50" y2="20" stroke="#4A7C2E" stroke-width="1.5"/>
      <line x1="50" y1="80" x2="50" y2="98" stroke="#4A7C2E" stroke-width="1.5"/>
      <line x1="2" y1="50" x2="20" y2="50" stroke="#4A7C2E" stroke-width="1.5"/>
      <line x1="80" y1="50" x2="98" y2="50" stroke="#4A7C2E" stroke-width="1.5"/>
      <!-- Antler silhouette at top -->
      <path d="M 35 20 L 30 12 L 32 16 L 26 14 L 30 18 L 24 18 M 65 20 L 70 12 L 68 16 L 74 14 L 70 18 L 76 18"
            stroke="#6B5D3D" stroke-width="1.2" fill="none" stroke-linejoin="round"/>
    </svg>
  </div>

  <div class="title-main">Hunting<br>Log Book</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Track Every Hunt, Every Season, Every Memory</div>

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
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Hunting Journal</div>
    <p>This log book is designed to be your faithful companion in the field.
    Record every hunt &mdash; the conditions, the game, the shots, the gear,
    and most importantly, the memories. Over time, your logs become an
    invaluable record of your hunting seasons.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Hunt Log</div>
    <p>Each hunt uses a <strong>two-page spread</strong>. The left page captures
    date, location, game species, weather, and sighting details. The right
    page records shot placement, harvest details, gear used, and your
    field notes and observations.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips</div>
    <p>&#9679; <strong>Log it same day.</strong> Details fade quickly after a long hunt.</p>
    <p>&#9679; <strong>Note the wind.</strong> Wind direction matters more than almost anything.</p>
    <p>&#9679; <strong>Track patterns.</strong> Over seasons, you will see animal movement patterns.</p>
    <p>&#9679; <strong>Record misses too.</strong> They teach as much as successes.</p>
  </div>
</div>""" % (pg, pg)


def season_goals_page():
    pg = pn()
    return """<!-- PAGE %d: Season Goals -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Season Goals &amp; Licenses</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">My Season Plan</div>
    <div class="section-line"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Species I Plan to Hunt This Season</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Locations / Public Land / Leases</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">License &amp; Tag Numbers</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Gear to Buy / Upgrade</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box" style="border-color: #4A7C2E;">
    <div class="wb-label">Personal Goals for This Season</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>
</div>""" % (pg, pg)


def hunt_log_left(session_num):
    pg = pn()
    game_types = ["Deer", "Elk", "Bear", "Turkey", "Waterfowl", "Upland", "Predator", "Small Game"]
    type_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % t
        for t in game_types
    )
    return """<!-- PAGE %d: Hunt Left #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Hunt Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="hunt-banner">
    <span class="hb-num">Hunt #%03d</span>
    <span class="hb-label">Date:</span>
    <div class="hb-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Location / Property</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">State / Zone</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Hunt Type</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Time (In / Out)</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #4A7C2E; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Game Species</div>
  <div class="type-row">%s</div>

  <div class="weather-box">
    <div class="wb-label">Weather Conditions</div>
    <div class="weather-row">
      <div class="weather-field"><span class="wf-label">Temp</span><div class="wf-write"></div></div>
      <div class="weather-field"><span class="wf-label">Wind Dir / Speed</span><div class="wf-write"></div></div>
      <div class="weather-field"><span class="wf-label">Conditions</span><div class="wf-write"></div></div>
      <div class="weather-field"><span class="wf-label">Barometric</span><div class="wf-write"></div></div>
      <div class="weather-field"><span class="wf-label">Moon Phase</span><div class="wf-write"></div></div>
      <div class="weather-field"><span class="wf-label">Visibility</span><div class="wf-write"></div></div>
    </div>
  </div>

  <div class="write-box" style="border-color: #4A7C2E;">
    <div class="wb-label">Game Sighted (Species, Count, Behavior, Distance)</div>
    <div class="wb-area" style="height: 50px;"></div>
  </div>

  <div class="rating-row">
    <span class="rr-label">Animal Activity</span>
    <span class="rating-circle">1</span><span class="rating-circle">2</span>
    <span class="rating-circle">3</span><span class="rating-circle">4</span>
    <span class="rating-circle">5</span>
  </div>
</div>""" % (pg, session_num, pg, session_num, type_html)


def hunt_log_right():
    pg = pn()
    return """<!-- PAGE %d: Hunt Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Harvest &amp; Field Notes</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #4A7C2E; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">
    Shot Record
  </div>

  <div class="shot-row">
    <div class="shot-num">1</div>
    <span style="font-size: 7pt; color: #999; width: 50px;">Distance:</span>
    <div class="shot-line"></div>
    <span style="font-size: 7pt; color: #999; width: 55px;">Shot Place:</span>
    <div class="shot-line"></div>
  </div>
  <div class="shot-row">
    <div class="shot-num">2</div>
    <span style="font-size: 7pt; color: #999; width: 50px;">Distance:</span>
    <div class="shot-line"></div>
    <span style="font-size: 7pt; color: #999; width: 55px;">Shot Place:</span>
    <div class="shot-line"></div>
  </div>

  <div class="info-row" style="margin-top: 8px;">
    <div class="info-field"><span class="if-label">Harvested? (Y/N)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Species / Sex</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Estimated Weight</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Points / Antlers</span><div class="if-write"></div></div>
  </div>

  <div class="gear-box">
    <div class="gb-label">Weapon &amp; Gear Used</div>
    <div class="gb-line"></div>
    <div class="gb-line"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Field Notes &amp; Observations</div>
    <div class="wb-area" style="height: 50px;"></div>
  </div>

  <div class="write-box" style="border-color: #6B5D3D;">
    <div class="wb-label" style="color: #6B5D3D;">Lessons Learned / Next Time</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>
</div>""" % (pg, pg)


def season_summary_page():
    pg = pn()
    return """<!-- PAGE %d: Season Summary -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Season Summary</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Season: __________</div>
    <div class="section-line"></div>
  </div>

  <table class="summary-table">
    <thead>
      <tr>
        <th>Species</th>
        <th>Days Hunted</th>
        <th>Sightings</th>
        <th>Harvested</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="write-box">
    <div class="wb-label">Best Day of the Season</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #6B5D3D;">
    <div class="wb-label" style="color: #6B5D3D;">Toughest Challenge</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #4A7C2E;">
    <div class="wb-label">Goals for Next Season</div>
    <div class="wb-area"></div>
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
      Every hunt is a story.<br>
      Every season is a chapter.<br>
      Write them well.
    </div>
    <div class="fp-line"></div>
    <div class="fp-logo">More Shine Press</div>
    <div class="fp-line"></div>
  </div>
</div>""" % pg


def generate(output_path=HTML_FILE):
    pages = []
    pages.append(interior_title_page())
    pages.append(how_to_use_page())
    pages.append(season_goals_page())

    # 35 hunt log spreads (70 pages)
    for session in range(1, 36):
        pages.append(hunt_log_left(session))
        pages.append(hunt_log_right())
        if session % 7 == 0:
            pages.append(season_summary_page())

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
