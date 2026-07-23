#!/usr/bin/env python3
"""
Camping Journal - KDP Interior Generator
Zero-dependency (Python stdlib only).

Generates a complete 80-page journal interior as standalone HTML
with print-ready CSS. Open in browser, Print -> Save as PDF.

Trim: 5" x 8" (12.7 x 20.32 cm)
Binding: Perfect binding (KDP standard)
Pages: 80 (4 front matter + 70 camping spreads + 6 back matter)
Publisher: More Shine Press

Usage:
  python3 generate.py
  open camping_journal_us_V1.0.html
  # Then Cmd+P -> Save as PDF
"""

import os

OUTPUT_FILE = "camping_journal_us_V1.0.html"
NUM_CAMPS = 35

# ============================================================
# THEME — forest green charcoal-gold
# ============================================================
THEME_COLOR     = "#1a2418"   # forest green charcoal (main)
THEME_DARK      = "#121612"   # near-black
THEME_LIGHT     = "#e8e2d4"   # warm cream tint for labels
THEME_ACCENT    = "#C4A04A"   # gold accent
THEME_ACCENT_DK = "#8a7430"   # dark gold
LINE_COLOR      = "#d0d0d0"
GRID_COLOR      = "#e0e0e0"
FONT_FAMILY     = "'Georgia', 'Times New Roman', serif"
FONT_SANS       = "'Helvetica Neue', 'Arial', sans-serif"
JOURNAL_TITLE   = "Camping Journal"

# ============================================================
# CSS
# ============================================================
CSS = r"""
<style>
  @page { size: 5in 8in; margin: 0; }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Georgia', 'Times New Roman', serif;
    color: #2c2c2c;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  /* --- PAGE BASE --- */
  .page {
    width: 5in; height: 8in;
    page-break-after: always;
    position: relative;
    overflow: hidden;
  }
  .page:last-child { page-break-after: auto; }

  /* Alternating gutter margins for facing pages */
  .page.recto {   /* odd page, right side - gutter on left */
    padding: 0.45in 0.38in 0.4in 0.65in;
  }
  .page.verso {   /* even page, left side - gutter on right */
    padding: 0.45in 0.65in 0.4in 0.38in;
  }

  /* --- HEADERS --- */
  .hike-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 2px solid #1a2418;
    padding-bottom: 4px;
    margin-bottom: 8px;
  }
  .hike-header .title {
    font-size: 12.5pt;
    font-weight: bold;
    color: #1a2418;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  .hike-header .number {
    font-size: 18pt;
    font-weight: bold;
    color: #C4A04A;
  }

  .page-title {
    font-size: 13pt;
    font-weight: bold;
    color: #1a2418;
    text-align: center;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding-bottom: 4px;
    border-bottom: 2px solid #1a2418;
    margin-bottom: 10px;
  }
  .page-subtitle {
    font-size: 8pt;
    text-align: center;
    color: #999;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
  }

  /* --- FORM FIELDS --- */
  .field-row {
    display: flex;
    gap: 6px;
    margin-bottom: 7px;
  }
  .field {
    flex: 1;
  }
  .field-label {
    font-size: 6.5pt;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 2px;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
  }
  .field-line {
    border-bottom: 1px solid #d0d0d0;
    height: 16px;
  }

  /* --- KEY-VALUE TABLE --- */
  .kv-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 8pt;
  }
  .kv-table td {
    border: 1px solid #ccc;
    padding: 4px 5px;
    height: 22px;
  }
  .kv-table td.label {
    background: #e8e2d4;
    font-weight: bold;
    color: #555;
    font-size: 7pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
    width: 30%;
    white-space: nowrap;
  }
  .kv-table td.fill { }

  /* --- CHECKBOXES --- */
  .check-row {
    display: flex;
    flex-wrap: wrap;
    gap: 5px 10px;
    margin-bottom: 7px;
  }
  .check-item {
    font-size: 7.5pt;
    color: #555;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
    display: flex;
    align-items: center;
    gap: 3px;
  }
  .check-box {
    display: inline-block;
    width: 9px;
    height: 9px;
    border: 1.2px solid #999;
    border-radius: 2px;
  }

  /* --- STAR RATING --- */
  .rating-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 7px;
  }
  .rating-group {
    display: flex;
    align-items: center;
    gap: 3px;
  }
  .rating-label {
    font-size: 7pt;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
    margin-right: 4px;
  }
  .star {
    font-size: 12pt;
    color: #ddd;
    letter-spacing: 1px;
  }

  /* --- SECTION DIVIDER --- */
  .section-bar {
    background: #1a2418;
    color: white;
    font-size: 7.5pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    padding: 3px 8px;
    margin: 8px 0 6px 0;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
    border-radius: 2px;
  }

  /* --- TRAIL SKETCH AREA (dotted grid) --- */
  .trail-map {
    border: 1px solid #bbb;
    border-radius: 3px;
    background-image: radial-gradient(circle, #e0e0e0 1px, transparent 1px);
    background-size: 0.16in 0.16in;
    background-position: 0.08in 0.08in;
  }

  /* --- LINED NOTES --- */
  .write-line {
    border-bottom: 1px solid #d0d0d0;
    height: 18px;
  }

  /* --- FOOTER --- */
  .page-footer {
    position: absolute;
    bottom: 0.22in;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 6.5pt;
    color: #bbb;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
    letter-spacing: 0.5px;
  }

  /* --- TITLE PAGE --- */
  .title-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 8in;
    padding: 1in;
    text-align: center;
  }
  .title-page .boot-icon {
    font-size: 48pt;
    margin-bottom: 20px;
    opacity: 0.8;
  }
  .title-page h1 {
    font-size: 24pt;
    color: #1a2418;
    letter-spacing: 2px;
    margin-bottom: 8px;
    line-height: 1.2;
  }
  .title-page .subtitle {
    font-size: 11pt;
    color: #777;
    font-style: italic;
    margin-bottom: 30px;
  }
  .title-page .divider {
    width: 2in;
    height: 2px;
    background: #C4A04A;
    margin: 15px 0;
  }
  .title-page .publisher {
    font-size: 9pt;
    color: #999;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 40px;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
  }

  /* --- HOW TO USE --- */
  .htu-item {
    display: flex;
    gap: 8px;
    margin-bottom: 9px;
    font-size: 8pt;
    line-height: 1.4;
  }
  .htu-num {
    flex-shrink: 0;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #1a2418;
    color: white;
    font-size: 8pt;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
  }
  .htu-text {
    color: #444;
    padding-top: 1px;
  }

  /* --- TRAIL INFO CARD --- */
  .trail-card {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 8px;
    margin-bottom: 10px;
  }
  .trail-card-title {
    font-size: 9pt;
    font-weight: bold;
    color: #1a2418;
    margin-bottom: 5px;
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  /* --- REFERENCE LIST (Leave No Trace, Ten Essentials) --- */
  .lnt-item {
    display: flex;
    gap: 8px;
    margin-bottom: 8px;
    font-size: 7.5pt;
    line-height: 1.4;
  }
  .lnt-num {
    flex-shrink: 0;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #C4A04A;
    color: #121612;
    font-size: 8pt;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
  }
  .lnt-text {
    color: #444;
    padding-top: 1px;
  }
  .lnt-text strong {
    color: #1a2418;
    font-size: 8pt;
  }

  /* --- ESSENTIALS GRID --- */
  .essentials-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 4px;
  }
  .essential-card {
    border: 1px solid #8a7430;
    border-radius: 4px;
    padding: 6px 8px;
    width: calc(50% - 3px);
    font-size: 7.5pt;
  }
  .essential-card .ec-num {
    font-size: 7pt;
    font-weight: bold;
    color: #C4A04A;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
  }
  .essential-card .ec-name {
    font-size: 8pt;
    font-weight: bold;
    color: #1a2418;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .essential-card .ec-desc {
    font-size: 6.5pt;
    color: #888;
    margin-top: 2px;
    line-height: 1.3;
  }

  /* --- PACKING CHECKLIST --- */
  .pack-category {
    margin-bottom: 8px;
  }
  .pack-cat-title {
    font-size: 7.5pt;
    font-weight: bold;
    color: #1a2418;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 1px solid #d0d0d0;
    padding-bottom: 2px;
    margin-bottom: 4px;
  }
  .pack-items {
    display: flex;
    flex-wrap: wrap;
    gap: 3px 12px;
  }
  .pack-item {
    font-size: 7pt;
    color: #555;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
    display: flex;
    align-items: center;
    gap: 3px;
  }

  /* --- TRAIL LOG TABLE --- */
  .log-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7pt;
  }
  .log-table th {
    background: #1a2418;
    color: white;
    font-size: 6.5pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 4px 3px;
    text-align: left;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
  }
  .log-table td {
    border: 1px solid #ccc;
    padding: 3px;
    height: 20px;
  }

  /* Screen preview border */
  .page {
    border: 1px dashed #e0e0e0;
  }
  @media print {
    .page { border: none; }
  }
</style>
"""


# ============================================================
# PAGE BUILDERS
# ============================================================

def page_side(idx):
    """Return 'recto' for odd pages (right side), 'verso' for even (left side)."""
    return "recto" if idx % 2 == 1 else "verso"


def page_title_page():
    return """
<div class="page recto" style="padding:0;">
  <div class="title-page">
    <div class="boot-icon">&#9978;</div>
    <h1>Camping<br>Journal</h1>
    <div class="divider"></div>
    <div class="subtitle">Capture Every Campfire, Every Starry Night, Every Adventure</div>
    <div class="publisher">More Shine Press</div>
  </div>
</div>"""


def page_belongs_to():
    return """
<div class="page verso">
  <div class="page-title">This Journal Belongs To</div>
  <div style="margin-top: 20px;">
    <table class="kv-table">
      <tr><td class="label">Name</td><td class="fill"></td></tr>
      <tr><td class="label">Email</td><td class="fill"></td></tr>
      <tr><td class="label">Phone</td><td class="fill"></td></tr>
      <tr><td class="label">Home Base</td><td class="fill"></td></tr>
      <tr><td class="label">Emergency Contact</td><td class="fill"></td></tr>
      <tr><td class="label">Emergency Phone</td><td class="fill"></td></tr>
      <tr><td class="label">Blood Type</td><td class="fill"></td></tr>
      <tr><td class="label">Allergies / Medical</td><td class="fill"></td></tr>
    </table>
  </div>
  <div style="margin-top: 16px; font-size: 7.5pt; color: #888; font-style: italic; text-align: center; line-height: 1.5;">
    Take this journal on every camping trip.<br>
    In case of emergency, the information above could help first responders.
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_how_to_use():
    items = [
        "Record each camping trip as soon as you arrive or right after setup while details are fresh. Fill in the fields on the left page, then write your story on the right.",
        "Use the campsite sketch area to draw your site layout, mark nearby trails, or note where you pitched your shelter.",
        "Rate your trips by difficulty and overall enjoyment. Over time you will discover your favorite campsites and conditions.",
        "Log details about your favorite campsites on the next page so you can track which spots suit different seasons and setups.",
        "Use the summary pages at the back to tally your nights, miles, and memorable moments at season's end.",
        "This journal fits 35 camping trips. Keep it in your gear bin or pack pocket.",
    ]
    items_html = ""
    for i, text in enumerate(items):
        items_html += f'<div class="htu-item"><div class="htu-num">{i+1}</div><div class="htu-text">{text}</div></div>'

    return f"""
<div class="page recto">
  <div class="page-title">How to Use This Journal</div>
  <div style="margin-top: 6px;">
    {items_html}
  </div>
  <div style="margin-top: 14px; padding: 8px 10px; background: {THEME_LIGHT}; border-radius: 4px; border-left: 3px solid {THEME_ACCENT};">
    <div style="font-size: 7pt; color: #888; text-transform: uppercase; letter-spacing: 1px; font-family: {FONT_SANS}; margin-bottom: 3px;">Pro Tip</div>
    <div style="font-size: 7.5pt; color: #555; line-height: 1.4; font-style: italic;">
      Take a moment after each trip to jot down not just the numbers, but how the campsite made you feel.
      Years from now, those notes will be the most valuable part of this journal.
    </div>
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_favorite_campsites():
    def campsite_card(n):
        return f"""
    <div class="trail-card">
      <div class="trail-card-title">Favorite Campsite {n}</div>
      <table class="kv-table">
        <tr>
          <td class="label" style="width:35%">Campsite Name</td><td class="fill"></td>
          <td class="label" style="width:35%">Location</td><td class="fill"></td>
        </tr>
        <tr>
          <td class="label" style="width:35%">Type</td><td class="fill"></td>
          <td class="label" style="width:35%">Best Season</td><td class="fill"></td>
        </tr>
        <tr>
          <td class="label" style="width:35%">Notes</td><td class="fill" colspan="3"></td>
        </tr>
      </table>
    </div>"""
    cards = "".join([campsite_card(i) for i in range(1, 3)])
    return f"""
<div class="page verso">
  <div class="page-title">Favorite Campsites</div>
  <div class="page-subtitle">Record your go-to campsites and conditions</div>
  {cards}
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_camp_left(camp_num):
    return f"""
<div class="page recto">
  <div class="hike-header">
    <span class="title">Camp Log</span>
    <span class="number">#{camp_num:02d}</span>
  </div>

  <table class="kv-table">
    <tr>
      <td class="label">Date</td><td class="fill"></td>
      <td class="label">Day</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Campsite Name</td><td class="fill"></td>
      <td class="label">Location</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Site Number</td><td class="fill" colspan="3"></td>
    </tr>
  </table>

  <div class="section-bar">Weather</div>
  <div class="check-row">
    <span class="check-item"><span class="check-box"></span>Sunny</span>
    <span class="check-item"><span class="check-box"></span>Cloudy</span>
    <span class="check-item"><span class="check-box"></span>Rain</span>
    <span class="check-item"><span class="check-box"></span>Wind</span>
    <span class="check-item"><span class="check-box"></span>Fog</span>
    <span class="check-item"><span class="check-box"></span>Snow</span>
  </div>
  <table class="kv-table">
    <tr>
      <td class="label">Temp</td><td class="fill"></td>
      <td class="label">Wind</td><td class="fill"></td>
    </tr>
  </table>

  <div class="section-bar">Camp Type</div>
  <div class="check-row">
    <span class="check-item"><span class="check-box"></span>Tent</span>
    <span class="check-item"><span class="check-box"></span>RV</span>
    <span class="check-item"><span class="check-box"></span>Cabin</span>
    <span class="check-item"><span class="check-box"></span>Hammock</span>
    <span class="check-item"><span class="check-box"></span>Backpack</span>
  </div>

  <div class="section-bar">Campground Type</div>
  <div class="check-row">
    <span class="check-item"><span class="check-box"></span>National Park</span>
    <span class="check-item"><span class="check-box"></span>State Park</span>
    <span class="check-item"><span class="check-box"></span>Private</span>
    <span class="check-item"><span class="check-box"></span>Dispersed</span>
    <span class="check-item"><span class="check-box"></span>Public Land</span>
  </div>

  <div class="section-bar">Stats</div>
  <table class="kv-table">
    <tr>
      <td class="label">Nights</td><td class="fill"></td>
      <td class="label">Campers</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Distance from Home</td><td class="fill"></td>
      <td class="label">Drive Time</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Setup Time</td><td class="fill"></td>
      <td class="label">Campmates</td><td class="fill"></td>
    </tr>
  </table>

  <div class="rating-row" style="margin-top: 8px;">
    <div class="rating-group">
      <span class="rating-label">Difficulty</span>
      <span class="star">&#9734;&#9734;&#9734;&#9734;&#9734;</span>
    </div>
    <div class="rating-group">
      <span class="rating-label">Overall</span>
      <span class="star">&#9734;&#9734;&#9734;&#9734;&#9734;</span>
    </div>
  </div>

  <div class="page-footer">Camp #{camp_num:02d}</div>
</div>"""


def page_camp_right(camp_num):
    return f"""
<div class="page verso">
  <div class="hike-header">
    <span class="title">Camp Notes</span>
    <span class="number">#{camp_num:02d}</span>
  </div>

  <div class="field-label" style="margin-bottom: 3px;">Campsite Sketch &amp; Map</div>
  <div class="trail-map" style="width: 100%; height: 2.1in;"></div>

  <div class="section-bar">Camp Highlights</div>
  <div class="write-line"></div>
  <div class="write-line"></div>
  <div class="write-line"></div>

  <table class="kv-table" style="margin-top: 4px;">
    <tr><td class="label">Wildlife Spotted</td><td class="fill"></td></tr>
    <tr><td class="label">Camp Conditions</td><td class="fill"></td></tr>
  </table>

  <div class="section-bar">Challenges &amp; Lessons</div>
  <div class="write-line"></div>
  <div class="write-line"></div>
  <div class="write-line"></div>

  <div class="check-row" style="margin-top: 6px;">
    <span class="check-item"><span class="check-box"></span>Campfire?</span>
  </div>
  <div class="field-label" style="margin-top: 4px;">Would return to this campsite?</div>
  <div class="check-row" style="margin-top: 2px;">
    <span class="check-item"><span class="check-box"></span>Absolutely</span>
    <span class="check-item"><span class="check-box"></span>Maybe</span>
    <span class="check-item"><span class="check-box"></span>No</span>
  </div>

  <div class="page-footer">Camp #{camp_num:02d}</div>
</div>"""


def page_camp_summary():
    return """
<div class="page recto">
  <div class="page-title">Camping Summary</div>
  <div class="page-subtitle">Tally your season at a glance</div>

  <table class="kv-table">
    <tr>
      <td class="label" style="width:50%">Total Trips</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Total Nights</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Total Campers</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Longest Trip</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Favorite Campsite</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Most Adventurous</td><td class="fill"></td>
    </tr>
  </table>

  <div class="section-bar">Top 5 Camping Trips</div>
  <table class="kv-table">
    <tr><td class="label" style="width:12%">#</td><td class="label" style="width:30%">Date</td><td class="label" style="width:58%">Campsite / Why</td></tr>
    <tr><td>1</td><td></td><td></td></tr>
    <tr><td>2</td><td></td><td></td></tr>
    <tr><td>3</td><td></td><td></td></tr>
    <tr><td>4</td><td></td><td></td></tr>
    <tr><td>5</td><td></td><td></td></tr>
  </table>

  <div class="section-bar">Goals for Next Season</div>
  <div class="write-line"></div>
  <div class="write-line"></div>
  <div class="write-line"></div>

  <div class="page-footer">More Shine Press</div>
</div>"""


def page_leave_no_trace():
    principles = [
        ("Plan Ahead and Prepare", "Know the regulations and prepare for extreme weather, hazards, and emergencies. Schedule your trip to avoid times of high use."),
        ("Travel and Camp on Durable Surfaces", "Use established trails and campsites. Walk single file in the middle of the trail. Keep campsites small and at least 200 feet from water."),
        ("Dispose of Waste Properly", "Pack it in, pack it out. Inspect your campsite for trash or spilled foods. Deposit solid human waste in catholes 6-8 inches deep, 200 feet from water."),
        ("Leave What You Find", "Preserve the past: examine but do not touch cultural or historic structures and artifacts. Leave rocks, plants, and other natural objects as you find them."),
        ("Minimize Campfire Impacts", "Use a lightweight stove for cooking and a candle lantern for light. Where fires are permitted, use established fire rings, fire pans, or mound fires."),
        ("Respect Wildlife", "Observe wildlife from a distance. Never feed animals. Store food securely and keep wildlife wild. Control pets at all times."),
        ("Be Considerate of Other Visitors", "Respect other visitors and protect the quality of their experience. Yield to other users on the trail. Let nature's sounds prevail."),
    ]
    items_html = ""
    for i, (title, desc) in enumerate(principles):
        items_html += (
            f'<div class="lnt-item">'
            f'<div class="lnt-num">{i+1}</div>'
            f'<div class="lnt-text"><strong>{title}</strong><br>{desc}</div>'
            f'</div>'
        )

    return f"""
<div class="page verso">
  <div class="page-title">Leave No Trace</div>
  <div class="page-subtitle">Seven Principles for Outdoor Ethics</div>
  <div style="margin-top: 4px;">
    {items_html}
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_camping_essentials():
    essentials = [
        ("Shelter", "Tent, tarp, or hammock setup"),
        ("Sleep System", "Sleeping bag, pad, pillow"),
        ("Kitchen", "Stove, fuel, cookware, utensils"),
        ("Water", "Bottles, filter, or purification tablets"),
        ("Fire", "Matches, lighter, fire starter, kindling"),
        ("Lighting", "Headlamp, lantern, extra batteries"),
        ("First-Aid", "Bandages, antiseptic, medications"),
        ("Navigation", "Map, compass, GPS device"),
        ("Clothing", "Layers, rain gear, extra socks"),
        ("Tools", "Knife, multi-tool, cordage, repair tape"),
    ]
    cards_html = ""
    for i, (name, desc) in enumerate(essentials):
        cards_html += (
            f'<div class="essential-card">'
            f'<span class="ec-num">{i+1:02d}</span> '
            f'<span class="ec-name">{name}</span>'
            f'<div class="ec-desc">{desc}</div>'
            f'</div>'
        )

    return f"""
<div class="page recto">
  <div class="page-title">Camping Essentials</div>
  <div class="page-subtitle">Ten categories every camper should pack</div>
  <div class="essentials-grid">
    {cards_html}
  </div>
  <div style="margin-top: 14px; padding: 8px 10px; background: {THEME_LIGHT}; border-radius: 4px; border-left: 3px solid {THEME_ACCENT};">
    <div style="font-size: 7pt; color: #888; text-transform: uppercase; letter-spacing: 1px; font-family: {FONT_SANS}; margin-bottom: 3px;">Safety First</div>
    <div style="font-size: 7.5pt; color: #555; line-height: 1.4; font-style: italic;">
      These ten categories form the foundation of every camping trip.
      Customize your gear for the terrain, weather, and length of your stay.
    </div>
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_packing_checklist():
    categories = [
        ("Shelter", ["Tent", "Tarp / footprint", "Stakes", "Guy lines", "Mallet"]),
        ("Sleep", ["Sleeping bag", "Sleeping pad", "Pillow", "Extra blanket", "Ear plugs"]),
        ("Kitchen / Cooking", ["Stove", "Fuel", "Cookware", "Utensils", "Plates / cups", "Coffee press", "Trash bags"]),
        ("Water", ["Water bottles", "Hydration bladder", "Water filter", "Purification tablets"]),
        ("Fire", ["Matches (waterproof)", "Lighter", "Fire starter", "Kindling", "Axe / saw"]),
        ("Lighting", ["Headlamp", "Lantern", "Extra batteries", "Glow sticks"]),
        ("First-Aid", ["Bandages", "Antiseptic wipes", "Blister kit", "Pain reliever", "Tweezers", "Medical tape"]),
        ("Navigation", ["Map", "Compass", "GPS device", "Trail guide", "Pencil / pen"]),
        ("Clothing", ["Base layer", "Insulating jacket", "Rain shell", "Warm hat", "Gloves", "Extra socks", "Sturdy shoes"]),
        ("Personal", ["Journal & pen", "Camera", "Phone", "Insect repellent", "Sunscreen", "Toiletries", "Towel"]),
        ("Tools / Misc", ["Multi-tool / knife", "Duct tape", "Cordage / paracord", "Whistle", "Cooler", "Camp chairs"]),
    ]

    cats_html = ""
    for cat_name, items in categories:
        items_html = "".join([
            f'<span class="pack-item"><span class="check-box"></span>{item}</span>'
            for item in items
        ])
        cats_html += (
            f'<div class="pack-category">'
            f'<div class="pack-cat-title">{cat_name}</div>'
            f'<div class="pack-items">{items_html}</div>'
            f'</div>'
        )

    return f"""
<div class="page verso">
  <div class="page-title">Packing Checklist</div>
  <div class="page-subtitle">Gear up before you head to camp</div>
  <div style="margin-top: 2px;">
    {cats_html}
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_notes(num_lines=18):
    lines = "".join([f'<div class="write-line"></div>' for _ in range(num_lines)])
    return f"""
<div class="page recto">
  <div class="page-title">Notes</div>
  <div style="margin-top: 6px;">{lines}</div>
  <div class="page-footer">More Shine Press</div>
</div>"""


# ============================================================
# MAIN ASSEMBLY
# ============================================================

def generate(output_path=OUTPUT_FILE):
    pages_html = []

    # Front matter (pages 1-4)
    pages_html.append(("title", page_title_page()))
    pages_html.append(("belongs", page_belongs_to()))
    pages_html.append(("howto", page_how_to_use()))
    pages_html.append(("campsites", page_favorite_campsites()))

    # Camping spreads (pages 5-74)
    for i in range(1, NUM_CAMPS + 1):
        pages_html.append((f"camp_left_{i}", page_camp_left(i)))
        pages_html.append((f"camp_right_{i}", page_camp_right(i)))

    # Back matter (pages 75-80)
    pages_html.append(("summary", page_camp_summary()))
    pages_html.append(("lnt", page_leave_no_trace()))
    pages_html.append(("essentials", page_camping_essentials()))
    pages_html.append(("packing", page_packing_checklist()))
    pages_html.append(("notes", page_notes()))
    pages_html.append(("notes", page_notes()))

    # Count pages
    total_pages = len(pages_html)

    body = "\n".join([html for _, html in pages_html])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{JOURNAL_TITLE} - Interior</title>
  {CSS}
</head>
<body>
{body}
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path, total_pages


if __name__ == "__main__":
    path, count = generate()
    abs_path = os.path.abspath(path)
    print(f"[OK] Interior generated: {abs_path}")
    print(f"     Total pages: {count}")
    print(f"     Trim size: 5in x 8in")
    print(f"     Camps: {NUM_CAMPS}")
    print(f"     Publisher: More Shine Press")
    print(f"")
    print(f"     Next: open {abs_path} in browser")
    print(f"           Then Cmd+P -> Save as PDF (Margins: None, Scale: 100%)")
