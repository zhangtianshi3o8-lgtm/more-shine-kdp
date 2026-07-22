#!/usr/bin/env python3
"""
Hiking Adventure Journal - KDP Interior Generator
Zero-dependency (Python stdlib only).

Generates a complete 80-page journal interior as standalone HTML
with print-ready CSS. Open in browser, Print -> Save as PDF.

Trim: 5" x 8" (12.7 x 20.32 cm)
Binding: Perfect binding (KDP standard)
Pages: 80 (4 front matter + 70 hike spreads + 6 back matter)
Publisher: More Shine Press

Usage:
  python3 generate.py
  open hiking_journal_us_V1.0.html
  # Then Cmd+P -> Save as PDF
"""

import os

OUTPUT_FILE = "hiking_journal_us_V1.0.html"
NUM_HIKES = 35

# ============================================================
# THEME — understated luxury charcoal-gold
# ============================================================
THEME_COLOR     = "#2a2a2e"   # charcoal (main)
THEME_DARK      = "#161616"   # near-black
THEME_LIGHT     = "#e8e2d4"   # warm cream tint for labels
THEME_ACCENT    = "#C4A04A"   # gold accent
THEME_ACCENT_DK = "#8a7430"   # dark gold
LINE_COLOR      = "#d0d0d0"
GRID_COLOR      = "#e0e0e0"
FONT_FAMILY     = "'Georgia', 'Times New Roman', serif"
FONT_SANS       = "'Helvetica Neue', 'Arial', sans-serif"
JOURNAL_TITLE   = "Hiking Adventure Journal"

# ============================================================
# CSS
# ============================================================
CSS = f"""
<style>
  @page {{ size: 5in 8in; margin: 0; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: {FONT_FAMILY};
    color: #2c2c2c;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  /* --- PAGE BASE --- */
  .page {{
    width: 5in; height: 8in;
    page-break-after: always;
    position: relative;
    overflow: hidden;
  }}
  .page:last-child {{ page-break-after: auto; }}

  /* Alternating gutter margins for facing pages */
  .page.recto {{   /* odd page, right side - gutter on left */
    padding: 0.45in 0.38in 0.4in 0.65in;
  }}
  .page.verso {{   /* even page, left side - gutter on right */
    padding: 0.45in 0.65in 0.4in 0.38in;
  }}

  /* --- HEADERS --- */
  .hike-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 2px solid {THEME_COLOR};
    padding-bottom: 4px;
    margin-bottom: 8px;
  }}
  .hike-header .title {{
    font-size: 12.5pt;
    font-weight: bold;
    color: {THEME_COLOR};
    letter-spacing: 1px;
    text-transform: uppercase;
  }}
  .hike-header .number {{
    font-size: 18pt;
    font-weight: bold;
    color: {THEME_ACCENT};
  }}

  .page-title {{
    font-size: 13pt;
    font-weight: bold;
    color: {THEME_COLOR};
    text-align: center;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding-bottom: 4px;
    border-bottom: 2px solid {THEME_COLOR};
    margin-bottom: 10px;
  }}
  .page-subtitle {{
    font-size: 8pt;
    text-align: center;
    color: #999;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
  }}

  /* --- FORM FIELDS --- */
  .field-row {{
    display: flex;
    gap: 6px;
    margin-bottom: 7px;
  }}
  .field {{
    flex: 1;
  }}
  .field-label {{
    font-size: 6.5pt;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 2px;
    font-family: {FONT_SANS};
  }}
  .field-line {{
    border-bottom: 1px solid {LINE_COLOR};
    height: 16px;
  }}

  /* --- KEY-VALUE TABLE --- */
  .kv-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 8pt;
  }}
  .kv-table td {{
    border: 1px solid #ccc;
    padding: 4px 5px;
    height: 22px;
  }}
  .kv-table td.label {{
    background: {THEME_LIGHT};
    font-weight: bold;
    color: #555;
    font-size: 7pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-family: {FONT_SANS};
    width: 30%;
    white-space: nowrap;
  }}
  .kv-table td.fill {{ }}

  /* --- CHECKBOXES --- */
  .check-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 5px 10px;
    margin-bottom: 7px;
  }}
  .check-item {{
    font-size: 7.5pt;
    color: #555;
    font-family: {FONT_SANS};
    display: flex;
    align-items: center;
    gap: 3px;
  }}
  .check-box {{
    display: inline-block;
    width: 9px;
    height: 9px;
    border: 1.2px solid #999;
    border-radius: 2px;
  }}

  /* --- STAR RATING --- */
  .rating-row {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 7px;
  }}
  .rating-group {{
    display: flex;
    align-items: center;
    gap: 3px;
  }}
  .rating-label {{
    font-size: 7pt;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-family: {FONT_SANS};
    margin-right: 4px;
  }}
  .star {{
    font-size: 12pt;
    color: #ddd;
    letter-spacing: 1px;
  }}

  /* --- SECTION DIVIDER --- */
  .section-bar {{
    background: {THEME_COLOR};
    color: white;
    font-size: 7.5pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    padding: 3px 8px;
    margin: 8px 0 6px 0;
    font-family: {FONT_SANS};
    border-radius: 2px;
  }}

  /* --- TRAIL SKETCH AREA (dotted grid) --- */
  .trail-map {{
    border: 1px solid #bbb;
    border-radius: 3px;
    background-image: radial-gradient(circle, {GRID_COLOR} 1px, transparent 1px);
    background-size: 0.16in 0.16in;
    background-position: 0.08in 0.08in;
  }}

  /* --- LINED NOTES --- */
  .write-line {{
    border-bottom: 1px solid {LINE_COLOR};
    height: 18px;
  }}

  /* --- FOOTER --- */
  .page-footer {{
    position: absolute;
    bottom: 0.22in;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 6.5pt;
    color: #bbb;
    font-family: {FONT_SANS};
    letter-spacing: 0.5px;
  }}

  /* --- TITLE PAGE --- */
  .title-page {{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 8in;
    padding: 1in;
    text-align: center;
  }}
  .title-page .boot-icon {{
    font-size: 48pt;
    margin-bottom: 20px;
    opacity: 0.8;
  }}
  .title-page h1 {{
    font-size: 24pt;
    color: {THEME_COLOR};
    letter-spacing: 2px;
    margin-bottom: 8px;
    line-height: 1.2;
  }}
  .title-page .subtitle {{
    font-size: 11pt;
    color: #777;
    font-style: italic;
    margin-bottom: 30px;
  }}
  .title-page .divider {{
    width: 2in;
    height: 2px;
    background: {THEME_ACCENT};
    margin: 15px 0;
  }}
  .title-page .publisher {{
    font-size: 9pt;
    color: #999;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 40px;
    font-family: {FONT_SANS};
  }}

  /* --- HOW TO USE --- */
  .htu-item {{
    display: flex;
    gap: 8px;
    margin-bottom: 9px;
    font-size: 8pt;
    line-height: 1.4;
  }}
  .htu-num {{
    flex-shrink: 0;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: {THEME_COLOR};
    color: white;
    font-size: 8pt;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: {FONT_SANS};
  }}
  .htu-text {{
    color: #444;
    padding-top: 1px;
  }}

  /* --- TRAIL INFO CARD --- */
  .trail-card {{
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 8px;
    margin-bottom: 10px;
  }}
  .trail-card-title {{
    font-size: 9pt;
    font-weight: bold;
    color: {THEME_COLOR};
    margin-bottom: 5px;
    text-transform: uppercase;
    letter-spacing: 1px;
  }}

  /* --- REFERENCE LIST (Leave No Trace, Ten Essentials) --- */
  .lnt-item {{
    display: flex;
    gap: 8px;
    margin-bottom: 8px;
    font-size: 7.5pt;
    line-height: 1.4;
  }}
  .lnt-num {{
    flex-shrink: 0;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: {THEME_ACCENT};
    color: {THEME_DARK};
    font-size: 8pt;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: {FONT_SANS};
  }}
  .lnt-text {{
    color: #444;
    padding-top: 1px;
  }}
  .lnt-text strong {{
    color: {THEME_COLOR};
    font-size: 8pt;
  }}

  /* --- ESSENTIALS GRID --- */
  .essentials-grid {{
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 4px;
  }}
  .essential-card {{
    border: 1px solid {THEME_ACCENT_DK};
    border-radius: 4px;
    padding: 6px 8px;
    width: calc(50% - 3px);
    font-size: 7.5pt;
  }}
  .essential-card .ec-num {{
    font-size: 7pt;
    font-weight: bold;
    color: {THEME_ACCENT};
    font-family: {FONT_SANS};
  }}
  .essential-card .ec-name {{
    font-size: 8pt;
    font-weight: bold;
    color: {THEME_COLOR};
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .essential-card .ec-desc {{
    font-size: 6.5pt;
    color: #888;
    margin-top: 2px;
    line-height: 1.3;
  }}

  /* --- PACKING CHECKLIST --- */
  .pack-category {{
    margin-bottom: 8px;
  }}
  .pack-cat-title {{
    font-size: 7.5pt;
    font-weight: bold;
    color: {THEME_COLOR};
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 1px solid {LINE_COLOR};
    padding-bottom: 2px;
    margin-bottom: 4px;
  }}
  .pack-items {{
    display: flex;
    flex-wrap: wrap;
    gap: 3px 12px;
  }}
  .pack-item {{
    font-size: 7pt;
    color: #555;
    font-family: {FONT_SANS};
    display: flex;
    align-items: center;
    gap: 3px;
  }}

  /* --- TRAIL LOG TABLE --- */
  .log-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 7pt;
  }}
  .log-table th {{
    background: {THEME_COLOR};
    color: white;
    font-size: 6.5pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 4px 3px;
    text-align: left;
    font-family: {FONT_SANS};
  }}
  .log-table td {{
    border: 1px solid #ccc;
    padding: 3px;
    height: 20px;
  }}

  /* Screen preview border */
  .page {{
    border: 1px dashed #e0e0e0;
  }}
  @media print {{
    .page {{ border: none; }}
  }}
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
    <div class="boot-icon">&#9968;</div>
    <h1>Hiking<br>Adventure<br>Journal</h1>
    <div class="divider"></div>
    <div class="subtitle">A Hiker's Log for Trails, Peaks &amp; Summits</div>
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
    Carry this journal on every hike.<br>
    In case of emergency, the information above could help first responders.
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_how_to_use():
    items = [
        "Record each hike as soon as you finish while memories are fresh. Fill in the fields on the left page, then write your story on the right.",
        "Use the trail sketch area to draw your route, mark waypoints, or note turn-by-turn directions.",
        "Rate your hikes by difficulty and overall enjoyment. Over time you will discover your favorite trails and conditions.",
        "Log details about your favorite trails on the next page so you can track which routes suit different seasons and skill levels.",
        "Use the summary pages at the back to tally your miles, elevation, and memorable moments at season's end.",
        "This journal fits 35 hikes. Carry it in your pack pocket or side pouch.",
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
      Take a moment after each hike to jot down not just the numbers, but how the trail made you feel.
      Years from now, those notes will be the most valuable part of this journal.
    </div>
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_favorite_trails():
    def trail_card(n):
        return f"""
    <div class="trail-card">
      <div class="trail-card-title">Favorite Trail {n}</div>
      <table class="kv-table">
        <tr>
          <td class="label" style="width:35%">Trail Name</td><td class="fill"></td>
          <td class="label" style="width:35%">Location</td><td class="fill"></td>
        </tr>
        <tr>
          <td class="label" style="width:35%">Distance</td><td class="fill"></td>
          <td class="label" style="width:35%">Elevation Gain</td><td class="fill"></td>
        </tr>
        <tr>
          <td class="label" style="width:35%">Difficulty</td><td class="fill"></td>
          <td class="label" style="width:35%">Best Season</td><td class="fill"></td>
        </tr>
        <tr>
          <td class="label" style="width:35%">Notes</td><td class="fill" colspan="3"></td>
        </tr>
      </table>
    </div>"""
    cards = "".join([trail_card(i) for i in range(1, 3)])
    return f"""
<div class="page verso">
  <div class="page-title">Favorite Trails</div>
  <div class="page-subtitle">Record your go-to trails and conditions</div>
  {cards}
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_hike_left(hike_num):
    return f"""
<div class="page recto">
  <div class="hike-header">
    <span class="title">Hike Log</span>
    <span class="number">#{hike_num:02d}</span>
  </div>

  <table class="kv-table">
    <tr>
      <td class="label">Date</td><td class="fill"></td>
      <td class="label">Day</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Trailhead</td><td class="fill" colspan="3"></td>
    </tr>
    <tr>
      <td class="label">Trail Name</td><td class="fill"></td>
      <td class="label">Location</td><td class="fill"></td>
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

  <div class="section-bar">Trail Info</div>
  <div class="field-label" style="margin-bottom: 2px;">Difficulty</div>
  <div class="check-row">
    <span class="check-item"><span class="check-box"></span>Easy</span>
    <span class="check-item"><span class="check-box"></span>Moderate</span>
    <span class="check-item"><span class="check-box"></span>Strenuous</span>
    <span class="check-item"><span class="check-box"></span>Extreme</span>
  </div>
  <div class="field-label" style="margin-bottom: 2px;">Surface</div>
  <div class="check-row">
    <span class="check-item"><span class="check-box"></span>Paved</span>
    <span class="check-item"><span class="check-box"></span>Dirt</span>
    <span class="check-item"><span class="check-box"></span>Rocky</span>
    <span class="check-item"><span class="check-box"></span>Sand</span>
    <span class="check-item"><span class="check-box"></span>Snow</span>
    <span class="check-item"><span class="check-box"></span>Mixed</span>
  </div>

  <div class="section-bar">Stats</div>
  <table class="kv-table">
    <tr>
      <td class="label">Distance</td><td class="fill"></td>
      <td class="label">Moving Time</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Total Time</td><td class="fill"></td>
      <td class="label">Pace (min/mi)</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Elevation Gain</td><td class="fill"></td>
      <td class="label">Max Elevation</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Calories Burned</td><td class="fill"></td>
      <td class="label">Heart Rate (bpm)</td><td class="fill"></td>
    </tr>
  </table>

  <table class="kv-table" style="margin-top: 7px;">
    <tr>
      <td class="label">Hiking With</td><td class="fill" colspan="3"></td>
    </tr>
  </table>

  <div class="rating-row" style="margin-top: 8px;">
    <div class="rating-group">
      <span class="rating-label">Difficulty</span>
      <span class="star">&#9734;&#9734;&#9734;&#9734;&#9734;</span>
    </div>
    <div class="rating-group">
      <span class="rating-label">Enjoyment</span>
      <span class="star">&#9734;&#9734;&#9734;&#9734;&#9734;</span>
    </div>
  </div>

  <div class="page-footer">Hike #{hike_num:02d}</div>
</div>"""


def page_hike_right(hike_num):
    return f"""
<div class="page verso">
  <div class="hike-header">
    <span class="title">Trail Notes</span>
    <span class="number">#{hike_num:02d}</span>
  </div>

  <div class="field-label" style="margin-bottom: 3px;">Trail Sketch &amp; Map</div>
  <div class="trail-map" style="width: 100%; height: 2.1in;"></div>

  <div class="section-bar">Trail Highlights</div>
  <div class="write-line"></div>
  <div class="write-line"></div>
  <div class="write-line"></div>

  <table class="kv-table" style="margin-top: 4px;">
    <tr><td class="label">Wildlife Spotted</td><td class="fill"></td></tr>
    <tr><td class="label">Trail Conditions</td><td class="fill"></td></tr>
  </table>

  <div class="section-bar">Challenges &amp; Lessons</div>
  <div class="write-line"></div>
  <div class="write-line"></div>
  <div class="write-line"></div>

  <div class="check-row" style="margin-top: 6px;">
    <span class="check-item"><span class="check-box"></span>Photos Taken</span>
  </div>
  <div class="field-label" style="margin-top: 4px;">Would hike this trail again?</div>
  <div class="check-row" style="margin-top: 2px;">
    <span class="check-item"><span class="check-box"></span>Absolutely</span>
    <span class="check-item"><span class="check-box"></span>Maybe</span>
    <span class="check-item"><span class="check-box"></span>No</span>
  </div>

  <div class="page-footer">Hike #{hike_num:02d}</div>
</div>"""


def page_hike_summary():
    return """
<div class="page recto">
  <div class="page-title">Hike Summary</div>
  <div class="page-subtitle">Tally your season at a glance</div>

  <table class="kv-table">
    <tr>
      <td class="label" style="width:50%">Total Hikes</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Total Miles Hiked</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Total Time on Trail</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Total Elevation Gained</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Longest Hike</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Highest Elevation</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Most Challenging</td><td class="fill"></td>
    </tr>
  </table>

  <div class="section-bar">Top 5 Favorite Hikes</div>
  <table class="kv-table">
    <tr><td class="label" style="width:12%">#</td><td class="label" style="width:30%">Date</td><td class="label" style="width:58%">Trail / Why</td></tr>
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


def page_ten_essentials():
    essentials = [
        ("Navigation", "Map, compass, GPS"),
        ("Sun Protection", "Sunglasses, sunscreen, hat"),
        ("Insulation", "Extra clothing, jacket"),
        ("Illumination", "Headlamp, extra batteries"),
        ("First-Aid Supplies", "Bandages, antiseptic, meds"),
        ("Fire", "Matches, lighter, fire starter"),
        ("Repair Kit", "Knife, duct tape, cordage"),
        ("Nutrition", "Extra food, energy bars"),
        ("Hydration", "Extra water, filter or tablets"),
        ("Emergency Shelter", "Space blanket, tarp, bivy"),
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
  <div class="page-title">The Ten Essentials</div>
  <div class="page-subtitle">Carry these on every hike, every time</div>
  <div class="essentials-grid">
    {cards_html}
  </div>
  <div style="margin-top: 14px; padding: 8px 10px; background: {THEME_LIGHT}; border-radius: 4px; border-left: 3px solid {THEME_ACCENT};">
    <div style="font-size: 7pt; color: #888; text-transform: uppercase; letter-spacing: 1px; font-family: {FONT_SANS}; margin-bottom: 3px;">Safety First</div>
    <div style="font-size: 7.5pt; color: #555; line-height: 1.4; font-style: italic;">
      The Ten Essentials form the minimum gear every hiker should carry.
      Customize your pack for the terrain, weather, and length of your hike.
    </div>
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_packing_checklist():
    categories = [
        ("Navigation", ["Map", "Compass", "GPS device", "Trail guide", "Pencil/pen"]),
        ("Sun Protection", ["Sunscreen", "Sunglasses", "Hat", "Lip balm (SPF)"]),
        ("Insulation", ["Base layer", "Insulating jacket", "Rain shell", "Warm hat", "Gloves", "Extra socks"]),
        ("Illumination", ["Headlamp", "Extra batteries", "Backup light"]),
        ("First Aid", ["Bandages", "Antiseptic wipes", "Blister kit", "Pain reliever", "Tweezers", "Medical tape"]),
        ("Fire", ["Matches (waterproof)", "Lighter", "Fire starter"]),
        ("Repair Kit", ["Multi-tool / knife", "Duct tape", "Cordage / paracord", "Safety pins"]),
        ("Nutrition", ["Trail snacks", "Energy bars", "Extra food (1 day)", "Electrolytes"]),
        ("Hydration", ["Water bottles", "Hydration bladder", "Water filter", "Purification tablets"]),
        ("Emergency Shelter", ["Space blanket", "Emergency bivy", "Whistle", "Signaling mirror"]),
        ("Personal", ["Journal & pen", "Camera", "Phone", "Trash bag", "Insect repellent", "Trekking poles"]),
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
  <div class="page-subtitle">Gear up before you hit the trail</div>
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
    pages_html.append(("trails", page_favorite_trails()))

    # Hike spreads (pages 5-74)
    for i in range(1, NUM_HIKES + 1):
        pages_html.append((f"hike_left_{i}", page_hike_left(i)))
        pages_html.append((f"hike_right_{i}", page_hike_right(i)))

    # Back matter (pages 75-80)
    pages_html.append(("summary", page_hike_summary()))
    pages_html.append(("lnt", page_leave_no_trace()))
    pages_html.append(("essentials", page_ten_essentials()))
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
    print(f"     Hikes: {NUM_HIKES}")
    print(f"     Publisher: More Shine Press")
    print(f"")
    print(f"     Next: open {abs_path} in browser")
    print(f"           Then Cmd+P -> Save as PDF (Margins: None, Scale: 100%)")
