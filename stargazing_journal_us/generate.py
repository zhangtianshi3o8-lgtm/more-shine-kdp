#!/usr/bin/env python3
"""
Stargazing Journal - KDP Interior Generator
Zero-dependency (Python stdlib only).

Generates a complete 80-page journal interior as standalone HTML
with print-ready CSS. Open in browser, Print -> Save as PDF.

Trim: 5" x 8" (12.7 x 20.32 cm)
Binding: Perfect binding (KDP standard)
Pages: 80 (4 front matter + 70 stargazing spreads + 6 back matter)
Publisher: More Shine Press

Usage:
  python3 generate.py
  open stargazing_journal_us_V1.0.html
  # Then Cmd+P -> Save as PDF
"""

import os

OUTPUT_FILE = "stargazing_journal_us_V1.0.html"
NUM_SESSIONS = 35

# ============================================================
# THEME — deep night sky navy + burnished gold
# ============================================================
THEME_COLOR     = "#0A0E1A"   # deep navy (main)
THEME_DARK      = "#06080F"   # near-black navy
THEME_LIGHT     = "#E8E2D4"   # warm cream tint for labels
THEME_ACCENT    = "#C4A04A"   # gold accent
THEME_ACCENT_DK = "#8a7430"   # dark gold
LINE_COLOR      = "#d0d0d0"
GRID_COLOR      = "#e0e0e0"
FONT_FAMILY     = "'Georgia', 'Times New Roman', serif"
FONT_SANS       = "'Helvetica Neue', 'Arial', sans-serif"
JOURNAL_TITLE   = "Stargazing Journal"

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
  .session-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 2px solid #0A0E1A;
    padding-bottom: 4px;
    margin-bottom: 8px;
  }
  .session-header .title {
    font-size: 12.5pt;
    font-weight: bold;
    color: #0A0E1A;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  .session-header .number {
    font-size: 18pt;
    font-weight: bold;
    color: #C4A04A;
  }

  .page-title {
    font-size: 13pt;
    font-weight: bold;
    color: #0A0E1A;
    text-align: center;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding-bottom: 4px;
    border-bottom: 2px solid #0A0E1A;
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
    background: #E8E2D4;
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
    background: #0A0E1A;
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

  /* --- EYEPIECE SKETCH AREA (dotted grid circle) --- */
  .fov-circle {
    border: 1.5px solid #C4A04A;
    border-radius: 50%;
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
  .title-page .star-icon {
    font-size: 48pt;
    margin-bottom: 20px;
    opacity: 0.8;
  }
  .title-page h1 {
    font-size: 24pt;
    color: #0A0E1A;
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
    background: #0A0E1A;
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

  /* --- EQUIPMENT CARD --- */
  .equip-card {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 8px;
    margin-bottom: 10px;
  }
  .equip-card-title {
    font-size: 9pt;
    font-weight: bold;
    color: #0A0E1A;
    margin-bottom: 5px;
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  /* --- REFERENCE LIST (Constellation Guide) --- */
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
    color: #06080F;
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
    color: #0A0E1A;
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
    color: #0A0E1A;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .essential-card .ec-desc {
    font-size: 6.5pt;
    color: #888;
    margin-top: 2px;
    line-height: 1.3;
  }

  /* --- TARGETS CHECKLIST --- */
  .target-category {
    margin-bottom: 8px;
  }
  .target-cat-title {
    font-size: 7.5pt;
    font-weight: bold;
    color: #0A0E1A;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 1px solid #d0d0d0;
    padding-bottom: 2px;
    margin-bottom: 4px;
  }
  .target-items {
    display: flex;
    flex-wrap: wrap;
    gap: 3px 12px;
  }
  .target-item {
    font-size: 7pt;
    color: #555;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
    display: flex;
    align-items: center;
    gap: 3px;
  }

  /* --- OBJECTS LOG TABLE --- */
  .log-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7pt;
  }
  .log-table th {
    background: #0A0E1A;
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
    <div class="star-icon">&#9733;</div>
    <h1>Stargazing<br>Journal</h1>
    <div class="divider"></div>
    <div class="subtitle">Track Every Constellation, Every Planet, Every Meteor Shower</div>
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
      <tr><td class="label">Home Location</td><td class="fill"></td></tr>
      <tr><td class="label">Latitude</td><td class="fill"></td></tr>
      <tr><td class="label">Local Bortle Scale</td><td class="fill"></td></tr>
      <tr><td class="label">Telescope / Mount</td><td class="fill"></td></tr>
      <tr><td class="label">Equipment Summary</td><td class="fill"></td></tr>
    </table>
  </div>
  <div style="margin-top: 16px; font-size: 7.5pt; color: #888; font-style: italic; text-align: center; line-height: 1.5;">
    Bring this journal to every stargazing session.<br>
    Your observation notes will build a personal record of the night sky.
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_how_to_use():
    items = [
        "Record each stargazing session as soon as possible while the details are fresh. Fill in the fields on the left page, then note your observations on the right.",
        "Use the sketch circle to draw what you see through your eyepiece &mdash; star patterns, brightness, and positions of objects.",
        "Rate sky conditions by seeing and transparency. Over time you will learn which nights are worth setting up your gear.",
        "Log details about your equipment on the next page so you can track which setups work best for different objects.",
        "Use the summary pages at the back to tally your sessions, hours under the stars, and objects observed.",
        "This journal fits 35 observation sessions. Bring it along on every night out under the sky.",
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
  <div style="margin-top: 14px; padding: 8px 10px; background: #E8E2D4; border-radius: 4px; border-left: 3px solid #C4A04A;">
    <div style="font-size: 7pt; color: #888; text-transform: uppercase; letter-spacing: 1px; font-family: 'Helvetica Neue', 'Arial', sans-serif; margin-bottom: 3px;">Pro Tip</div>
    <div style="font-size: 7.5pt; color: #555; line-height: 1.4; font-style: italic;">
      Use a red light flashlight to protect your night vision when filling out this journal.
      It takes about 30 minutes for your eyes to fully dark-adapt.
    </div>
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_equipment_log():
    def equip_card(n, fields):
        rows = ""
        for fname in fields:
            rows += f'<tr><td class="label" style="width:40%">{fname}</td><td class="fill"></td></tr>'
        return f"""
    <div class="equip-card">
      <div class="equip-card-title">{n}</div>
      <table class="kv-table">{rows}</table>
    </div>"""

    card1 = equip_card("Telescope", ["Type", "Aperture", "Focal Length", "Focal Ratio"])
    card2 = equip_card("Mount", ["Type", "Tracking", "Go-To System"])

    card3_html = """
    <div class="equip-card">
      <div class="equip-card-title">Optics &amp; Accessories</div>
      <table class="kv-table">
        <tr>
          <td class="label" style="width:35%">Binoculars</td><td class="fill"></td>
          <td class="label" style="width:35%">Eyepieces</td><td class="fill"></td>
        </tr>
        <tr>
          <td class="label" style="width:35%">Filters</td><td class="fill"></td>
          <td class="label" style="width:35%">Barlow / Reducer</td><td class="fill"></td>
        </tr>
      </table>
    </div>"""

    card4_html = """
    <div class="equip-card">
      <div class="equip-card-title">Astrophotography</div>
      <table class="kv-table">
        <tr>
          <td class="label" style="width:35%">Camera</td><td class="fill"></td>
          <td class="label" style="width:35%">Sensor</td><td class="fill"></td>
        </tr>
        <tr>
          <td class="label" style="width:35%">Software</td><td class="fill" colspan="3"></td>
        </tr>
      </table>
    </div>"""

    return f"""
<div class="page verso">
  <div class="page-title">Equipment Log</div>
  <div class="page-subtitle">Record your stargazing gear</div>
  {card1}
  {card2}
  {card3_html}
  {card4_html}
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_session_left(session_num):
    return f"""
<div class="page recto">
  <div class="session-header">
    <span class="title">Observation Session</span>
    <span class="number">#{session_num:02d}</span>
  </div>

  <table class="kv-table">
    <tr>
      <td class="label">Date</td><td class="fill"></td>
      <td class="label">Day</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Location</td><td class="fill" colspan="3"></td>
    </tr>
    <tr>
      <td class="label">Coordinates / Lat</td><td class="fill"></td>
      <td class="label">Bortle Scale</td><td class="fill"></td>
    </tr>
  </table>

  <div class="section-bar">Sky Conditions</div>
  <div class="check-row">
    <span class="check-item"><span class="check-box"></span>Clear</span>
    <span class="check-item"><span class="check-box"></span>Partly Cloudy</span>
    <span class="check-item"><span class="check-box"></span>Overcast</span>
    <span class="check-item"><span class="check-box"></span>Hazy</span>
    <span class="check-item"><span class="check-box"></span>Transparent</span>
  </div>
  <table class="kv-table">
    <tr>
      <td class="label">Wind</td><td class="fill"></td>
      <td class="label">Temp</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Humidity</td><td class="fill"></td>
      <td class="label">Dew</td><td class="fill"></td>
    </tr>
  </table>

  <div class="section-bar">Moon</div>
  <div class="field-label" style="margin-bottom: 2px;">Phase</div>
  <div class="check-row">
    <span class="check-item"><span class="check-box"></span>New</span>
    <span class="check-item"><span class="check-box"></span>Waxing Cres.</span>
    <span class="check-item"><span class="check-box"></span>First Quarter</span>
    <span class="check-item"><span class="check-box"></span>Waxing Gibbous</span>
    <span class="check-item"><span class="check-box"></span>Full</span>
    <span class="check-item"><span class="check-box"></span>Waning Gibbous</span>
    <span class="check-item"><span class="check-box"></span>Last Quarter</span>
    <span class="check-item"><span class="check-box"></span>Waning Cres.</span>
  </div>
  <table class="kv-table">
    <tr>
      <td class="label">Moon Illumination %</td><td class="fill"></td>
      <td class="label">Moon Altitude</td><td class="fill"></td>
    </tr>
  </table>

  <div class="section-bar">Sky Quality</div>
  <div class="rating-row">
    <div class="rating-group">
      <span class="rating-label">Seeing</span>
      <span class="star">&#9734;&#9734;&#9734;&#9734;&#9734;</span>
    </div>
    <div class="rating-group">
      <span class="rating-label">Transparency</span>
      <span class="star">&#9734;&#9734;&#9734;&#9734;&#9734;</span>
    </div>
  </div>
  <table class="kv-table">
    <tr>
      <td class="label">Bortle Scale (1-9)</td><td class="fill"></td>
      <td class="label">NELM (mag)</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Time Started</td><td class="fill"></td>
      <td class="label">Time Ended</td><td class="fill"></td>
    </tr>
  </table>

  <div class="page-footer">Session #{session_num:02d}</div>
</div>"""


def page_session_right(session_num):
    # Objects observed table: 8 rows
    obj_rows = "".join([f'<tr><td>{n}</td><td></td><td></td><td></td><td></td><td></td></tr>' for n in range(1, 9)])

    return f"""
<div class="page verso">
  <div class="session-header">
    <span class="title">Field Notes</span>
    <span class="number">#{session_num:02d}</span>
  </div>

  <div class="field-label" style="margin-bottom: 3px;">Objects Observed</div>
  <table class="log-table">
    <tr><th>#</th><th>Object Name</th><th>Type</th><th>Constellation</th><th>Mag</th><th>Notes</th></tr>
    {obj_rows}
  </table>

  <div class="section-bar">Eyepiece Sketch</div>
  <div style="display: flex; justify-content: center; margin: 4px 0 6px 0;">
    <div class="fov-circle" style="width: 1.7in; height: 1.7in;"></div>
  </div>

  <div class="section-bar">Highlights &amp; Discoveries</div>
  <div class="write-line"></div>
  <div class="write-line"></div>
  <div class="write-line"></div>

  <div class="section-bar">Challenges &amp; Lessons</div>
  <div class="write-line"></div>
  <div class="write-line"></div>

  <div class="check-row" style="margin-top: 6px;">
    <span class="check-item"><span class="check-box"></span>New Objects Found</span>
    <span class="check-item"><span class="check-box"></span>Photos Taken</span>
  </div>
  <div class="field-label" style="margin-top: 4px;">Would revisit this site?</div>
  <div class="check-row" style="margin-top: 2px;">
    <span class="check-item"><span class="check-box"></span>Absolutely</span>
    <span class="check-item"><span class="check-box"></span>Maybe</span>
    <span class="check-item"><span class="check-box"></span>No</span>
  </div>

  <div class="page-footer">Session #{session_num:02d}</div>
</div>"""


def page_stargazing_summary():
    return """
<div class="page recto">
  <div class="page-title">Stargazing Summary</div>
  <div class="page-subtitle">Tally your season under the stars</div>

  <table class="kv-table">
    <tr>
      <td class="label" style="width:50%">Total Sessions</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Total Hours Under Stars</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Total Objects Observed</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">New Objects Found</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Most Observed Constellation</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Best Session</td><td class="fill"></td>
    </tr>
  </table>

  <div class="section-bar">Top 5 Observation Sessions</div>
  <table class="kv-table">
    <tr><td class="label" style="width:12%">#</td><td class="label" style="width:30%">Date</td><td class="label" style="width:58%">Highlights / Why</td></tr>
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


def page_constellation_guide():
    constellations = [
        ("Ursa Major", "The Great Bear. Home to the Big Dipper asterism; the pointer stars point to Polaris. Visible year-round in the northern sky."),
        ("Ursa Minor", "The Little Bear. Contains Polaris, the North Star, around which the northern sky appears to rotate. Circumpolar for most northern observers."),
        ("Cassiopeia", "The Queen. Distinctive W or M shape. Circumpolar in the north. Rich in star clusters and lies in the Milky Way band."),
        ("Cepheus", "The King. Resembles a house or pointed hat. Circumpolar for northern latitudes. Home to the Garnet Star and variable star Delta Cephei."),
        ("Draco", "The Dragon. Long winding constellation winding between the Big and Little Dippers. Contains Thuban, a former pole star."),
        ("Orion", "The Hunter. Most recognizable constellation, visible in winter. Belt of three stars; sword holds the famous Orion Nebula."),
        ("Canis Major", "The Greater Dog. Contains Sirius, the brightest star in the night sky. Best seen in winter months below Orion."),
        ("Taurus", "The Bull. Contains the Pleiades (Seven Sisters) star cluster and the Hyades. The red star Aldebaran marks the bull's eye."),
        ("Gemini", "The Twins. Marked by bright stars Castor and Pollux. Site of a major meteor shower in December."),
        ("Leo", "The Lion. Distinctive backwards-question-mark (the Sickle) marks the lion's mane. Bright star Regulus anchors the constellation."),
        ("Scorpius", "The Scorpion. Striking summer constellation with the red star Antares. Curved tail resembles a scorpion's stinger."),
        ("Lyra", "The Lyre. Small but bright, led by Vega. Contains the Ring Nebula, a classic planetary nebula for telescopes."),
    ]
    items_html = ""
    for i, (title, desc) in enumerate(constellations):
        items_html += (
            f'<div class="lnt-item">'
            f'<div class="lnt-num">{i+1}</div>'
            f'<div class="lnt-text"><strong>{title}</strong><br>{desc}</div>'
            f'</div>'
        )

    return f"""
<div class="page verso">
  <div class="page-title">Constellation Guide</div>
  <div class="page-subtitle">Twelve major constellations to find</div>
  <div style="margin-top: 4px;">
    {items_html}
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_stargazing_essentials():
    essentials = [
        ("Red Light Flashlight", "Protects night vision for reading charts"),
        ("Star Chart / Planisphere", "Locate stars and constellations quickly"),
        ("Warm Clothing", "Nights get cold &mdash; dress in layers"),
        ("Blanket / Chair", "Comfort for long periods of looking up"),
        ("Binoculars", "Wide-field views of clusters and the Milky Way"),
        ("Snacks / Hot Drinks", "Stay warm and energized through the night"),
        ("Insect Repellent", "Essential for warm-season observations"),
        ("Notepad / Pencil", "Quick sketches and notes in the field"),
        ("Phone / App", "Astronomy apps help locate objects fast"),
        ("Patience", "Let your eyes adapt and the sky will reward you"),
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
  <div class="page-title">Stargazing Essentials</div>
  <div class="page-subtitle">Bring these on every night out</div>
  <div class="essentials-grid">
    {cards_html}
  </div>
  <div style="margin-top: 14px; padding: 8px 10px; background: #E8E2D4; border-radius: 4px; border-left: 3px solid #C4A04A;">
    <div style="font-size: 7pt; color: #888; text-transform: uppercase; letter-spacing: 1px; font-family: 'Helvetica Neue', 'Arial', sans-serif; margin-bottom: 3px;">Night Vision</div>
    <div style="font-size: 7.5pt; color: #555; line-height: 1.4; font-style: italic;">
      Give your eyes at least 20-30 minutes to dark-adapt. Avoid white light at all costs &mdash;
      use only red light to preserve your night vision throughout the session.
    </div>
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_observation_targets():
    categories = [
        ("Solar System", ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]),
        ("Deep Sky", ["Milky Way", "Andromeda Galaxy", "Orion Nebula", "Pleiades", "Double Cluster", "Ring Nebula", "Great Cluster (M13)", "Whirlpool Galaxy"]),
    ]

    cats_html = ""
    for cat_name, items in categories:
        items_html = "".join([
            f'<span class="target-item"><span class="check-box"></span>{item}</span>'
            for item in items
        ])
        cats_html += (
            f'<div class="target-category">'
            f'<div class="target-cat-title">{cat_name}</div>'
            f'<div class="target-items">{items_html}</div>'
            f'</div>'
        )

    return f"""
<div class="page verso">
  <div class="page-title">Observation Targets Checklist</div>
  <div class="page-subtitle">Lifetime list of night-sky objects</div>
  <div style="margin-top: 4px;">
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
    pages_html.append(("equipment", page_equipment_log()))

    # Stargazing spreads (pages 5-74)
    for i in range(1, NUM_SESSIONS + 1):
        pages_html.append((f"session_left_{i}", page_session_left(i)))
        pages_html.append((f"session_right_{i}", page_session_right(i)))

    # Back matter (pages 75-80)
    pages_html.append(("summary", page_stargazing_summary()))
    pages_html.append(("constellations", page_constellation_guide()))
    pages_html.append(("essentials", page_stargazing_essentials()))
    pages_html.append(("targets", page_observation_targets()))
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
    print(f"     Sessions: {NUM_SESSIONS}")
    print(f"     Publisher: More Shine Press")
    print(f"")
    print(f"     Next: open {abs_path} in browser")
    print(f"           Then Cmd+P -> Save as PDF (Margins: None, Scale: 100%)")
