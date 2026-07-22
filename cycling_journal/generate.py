#!/usr/bin/env python3
"""
Cycling Adventure Journal - KDP Interior Generator
Zero-dependency (Python stdlib only).

Generates a complete 80-page journal interior as standalone HTML
with print-ready CSS. Open in browser, Print -> Save as PDF.

Trim: 5" x 8" (12.7 x 20.32 cm)
Binding: Perfect binding (KDP standard)
Pages: 80 (4 front matter + 70 ride spreads + 6 back matter)
Publisher: More Shine Press

Usage:
  python3 generate.py
  open cycling_adventure_journal.html
  # Then Cmd+P -> Save as PDF
"""

import os
import json

OUTPUT_FILE = "cycling_adventure_journal.html"
NUM_RIDES = 35

# ============================================================
# THEME
# ============================================================
THEME_COLOR   = "#1a5d3a"   # deep forest green
THEME_DARK    = "#0f3d24"   # darker shade
THEME_LIGHT   = "#eef5ef"   # very light green tint for labels
THEME_ACCENT  = "#c4862a"   # warm amber accent
LINE_COLOR    = "#d0d0d0"
GRID_COLOR    = "#e0e0e0"
FONT_FAMILY   = "'Georgia', 'Times New Roman', serif"
FONT_SANS     = "'Helvetica Neue', 'Arial', sans-serif"
JOURNAL_TITLE = "Cycling Adventure Journal"

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
  .ride-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 2px solid {THEME_COLOR};
    padding-bottom: 4px;
    margin-bottom: 8px;
  }}
  .ride-header .title {{
    font-size: 12.5pt;
    font-weight: bold;
    color: {THEME_COLOR};
    letter-spacing: 1px;
    text-transform: uppercase;
  }}
  .ride-header .number {{
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

  /* --- ROUTE SKETCH AREA (dotted grid) --- */
  .route-map {{
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
  .title-page .bike-icon {{
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

  /* --- BIKE INFO CARD --- */
  .bike-card {{
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 8px;
    margin-bottom: 10px;
  }}
  .bike-card-title {{
    font-size: 9pt;
    font-weight: bold;
    color: {THEME_COLOR};
    margin-bottom: 5px;
    text-transform: uppercase;
    letter-spacing: 1px;
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
    <div class="bike-icon">&#128691;</div>
    <h1>Cycling<br>Adventure<br>Journal</h1>
    <div class="divider"></div>
    <div class="subtitle">A Rider's Log for Roads, Trails &amp; Journeys</div>
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
    Carry this journal on every ride.<br>
    In case of emergency, the information above could help first responders.
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_how_to_use():
    items = [
        ("Record each ride as soon as you finish while memories are fresh. Fill in the fields on the left page, then write your story on the right."),
        ("Use the route sketch area to draw your path, mark checkpoints, or note turn-by-turn directions."),
        ("Rate your rides by difficulty and overall enjoyment. Over time you will discover your favorite routes and conditions."),
        ("Log details about your bikes on the next page so you can track which setup works best for different terrain."),
        ("Use the summary pages at the back to tally your miles, elevation, and memorable moments at season's end."),
        ("This journal fits 35 rides. Carry it in your jersey pocket, handlebar bag, or backpack."),
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
      Take a moment after each ride to jot down not just the numbers, but how the ride made you feel.
      Years from now, those notes will be the most valuable part of this journal.
    </div>
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_my_bikes():
    def bike_card(n):
        return f"""
    <div class="bike-card">
      <div class="bike-card-title">Bike {n}</div>
      <table class="kv-table">
        <tr>
          <td class="label" style="width:35%">Type</td><td class="fill"></td>
          <td class="label" style="width:35%">Brand / Model</td><td class="fill"></td>
        </tr>
        <tr>
          <td class="label" style="width:35%">Frame Size</td><td class="fill"></td>
          <td class="label" style="width:35%">Year</td><td class="fill"></td>
        </tr>
        <tr>
          <td class="label" style="width:35%">Tire Size</td><td class="fill"></td>
          <td class="label" style="width:35%">Groupset</td><td class="fill"></td>
        </tr>
        <tr>
          <td class="label" style="width:35%">Notable Mods</td><td class="fill" colspan="3"></td>
        </tr>
      </table>
    </div>"""
    cards = "".join([bike_card(i) for i in range(1, 3)])
    return f"""
<div class="page verso">
  <div class="page-title">My Bikes</div>
  <div class="page-subtitle">Record your rides and setups</div>
  {cards}
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_ride_left(ride_num):
    return f"""
<div class="page recto">
  <div class="ride-header">
    <span class="title">Ride Log</span>
    <span class="number">#{ride_num:02d}</span>
  </div>

  <table class="kv-table">
    <tr>
      <td class="label">Date</td><td class="fill"></td>
      <td class="label">Day</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Start</td><td class="fill" colspan="3"></td>
    </tr>
    <tr>
      <td class="label">End</td><td class="fill" colspan="3"></td>
    </tr>
  </table>

  <div class="section-bar">Conditions</div>
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

  <div class="section-bar">Stats</div>
  <table class="kv-table">
    <tr>
      <td class="label">Distance</td><td class="fill"></td>
      <td class="label">Ride Time</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Elevation</td><td class="fill"></td>
      <td class="label">Avg Speed</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Max Speed</td><td class="fill"></td>
      <td class="label">Calories</td><td class="fill"></td>
    </tr>
  </table>

  <div class="section-bar">Details</div>
  <table class="kv-table">
    <tr>
      <td class="label">Terrain</td><td class="fill"></td>
      <td class="label">Bike Used</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label">Riding With</td><td class="fill" colspan="3"></td>
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

  <div class="page-footer">Ride #{ride_num:02d}</div>
</div>"""


def page_ride_right(ride_num):
    return f"""
<div class="page verso">
  <div class="ride-header">
    <span class="title">Journey Notes</span>
    <span class="number">#{ride_num:02d}</span>
  </div>

  <div class="field-label" style="margin-bottom: 3px;">Route Sketch &amp; Map</div>
  <div class="route-map" style="width: 100%; height: 2.1in;"></div>

  <div class="section-bar">Highlights &amp; Memories</div>
  <div class="write-line"></div>
  <div class="write-line"></div>
  <div class="write-line"></div>
  <div class="write-line"></div>
  <div class="write-line"></div>

  <div class="section-bar">Challenges &amp; Lessons</div>
  <div class="write-line"></div>
  <div class="write-line"></div>
  <div class="write-line"></div>

  <div class="field-label" style="margin-top: 8px;">Would ride this route again?</div>
  <div class="check-row" style="margin-top: 2px;">
    <span class="check-item"><span class="check-box"></span>Absolutely</span>
    <span class="check-item"><span class="check-box"></span>Maybe</span>
    <span class="check-item"><span class="check-box"></span>No</span>
  </div>

  <div class="page-footer">Ride #{ride_num:02d}</div>
</div>"""


def page_ride_summary():
    return """
<div class="page recto">
  <div class="page-title">Ride Summary</div>
  <div class="page-subtitle">Tally your season at a glance</div>

  <table class="kv-table">
    <tr>
      <td class="label" style="width:50%">Total Rides</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Total Distance</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Total Ride Time</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Total Elevation</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Longest Ride</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Most Challenging</td><td class="fill"></td>
    </tr>
  </table>

  <div class="section-bar">Top 5 Favorite Rides</div>
  <table class="kv-table">
    <tr><td class="label" style="width:12%">#</td><td class="label" style="width:30%">Date</td><td class="label" style="width:58%">Route / Why</td></tr>
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


def page_notes(num_lines=18):
    lines = "".join([f'<div class="write-line"></div>' for _ in range(num_lines)])
    return f"""
<div class="page verso">
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
    pages_html.append(("bikes", page_my_bikes()))

    # Ride spreads (pages 5-74)
    for i in range(1, NUM_RIDES + 1):
        pages_html.append((f"ride_left_{i}", page_ride_left(i)))
        pages_html.append((f"ride_right_{i}", page_ride_right(i)))

    # Back matter (pages 75-80)
    pages_html.append(("summary", page_ride_summary()))
    for _ in range(5):
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
    print(f"     Rides: {NUM_RIDES}")
    print(f"     Publisher: More Shine Press")
    print(f"")
    print(f"     Next: open {abs_path} in browser")
    print(f"           Then Cmd+P -> Save as PDF (Margins: None, Scale: 100%)")
