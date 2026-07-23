#!/usr/bin/env python3
"""
Gardening Journal - KDP Interior Generator
Zero-dependency (Python stdlib only).

Generates a complete 80-page journal interior as standalone HTML
with print-ready CSS. Open in browser, Print -> Save as PDF.

Trim: 5" x 8" (12.7 x 20.32 cm)
Binding: Perfect binding (KDP standard)
Pages: 80 (4 front matter + 70 garden spreads + 6 back matter)
Publisher: More Shine Press

Usage:
  python3 generate.py
  open gardening_journal_us_V1.0.html
  # Then Cmd+P -> Save as PDF
"""

import os

OUTPUT_FILE = "gardening_journal_us_V1.0.html"
NUM_ENTRIES = 35

# ============================================================
# THEME — sage/olive earth with gold accent
# ============================================================
THEME_COLOR     = "#2A3320"   # sage-olive (main)
THEME_DARK      = "#12160E"   # near-black olive
THEME_LIGHT     = "#e8e2d4"   # warm cream tint for labels
THEME_ACCENT    = "#C4A04A"   # gold accent
THEME_ACCENT_DK = "#8a7430"   # dark gold
LINE_COLOR      = "#d0d0d0"
GRID_COLOR      = "#e0e0e0"
FONT_FAMILY     = "'Georgia', 'Times New Roman', serif"
FONT_SANS       = "'Helvetica Neue', 'Arial', sans-serif"
JOURNAL_TITLE   = "Gardening Journal"

# ============================================================
# CSS — raw string, NO f-string for CSS
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
  .entry-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 2px solid #2A3320;
    padding-bottom: 4px;
    margin-bottom: 8px;
  }
  .entry-header .title {
    font-size: 12.5pt;
    font-weight: bold;
    color: #2A3320;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  .entry-header .number {
    font-size: 18pt;
    font-weight: bold;
    color: #C4A04A;
  }

  .page-title {
    font-size: 13pt;
    font-weight: bold;
    color: #2A3320;
    text-align: center;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding-bottom: 4px;
    border-bottom: 2px solid #2A3320;
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
    background: #2A3320;
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

  /* --- GARDEN SKETCH AREA (dotted grid) --- */
  .garden-sketch {
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
  .title-page .seedling-icon {
    font-size: 48pt;
    margin-bottom: 20px;
    opacity: 0.8;
  }
  .title-page h1 {
    font-size: 24pt;
    color: #2A3320;
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
    background: #2A3320;
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

  /* --- GARDEN INFO CARD --- */
  .garden-card {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 8px;
    margin-bottom: 10px;
  }
  .garden-card-title {
    font-size: 9pt;
    font-weight: bold;
    color: #2A3320;
    margin-bottom: 5px;
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  /* --- COMPANION PAIR LIST --- */
  .companion-item {
    display: flex;
    gap: 8px;
    margin-bottom: 8px;
    font-size: 7.5pt;
    line-height: 1.4;
  }
  .companion-num {
    flex-shrink: 0;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #C4A04A;
    color: #12160E;
    font-size: 8pt;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
  }
  .companion-text {
    color: #444;
    padding-top: 1px;
  }
  .companion-text strong {
    color: #2A3320;
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
    color: #2A3320;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .essential-card .ec-desc {
    font-size: 6.5pt;
    color: #888;
    margin-top: 2px;
    line-height: 1.3;
  }

  /* --- PLANTING CALENDAR --- */
  .cal-category {
    margin-bottom: 8px;
  }
  .cal-cat-title {
    font-size: 7.5pt;
    font-weight: bold;
    color: #2A3320;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 1px solid #d0d0d0;
    padding-bottom: 2px;
    margin-bottom: 4px;
  }
  .cal-items {
    display: flex;
    flex-wrap: wrap;
    gap: 3px 12px;
  }
  .cal-item {
    font-size: 7pt;
    color: #555;
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
    display: flex;
    align-items: center;
    gap: 3px;
  }

  /* --- PLANT LOG TABLE --- */
  .log-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7pt;
  }
  .log-table th {
    background: #2A3320;
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
    <div class="seedling-icon">&#127793;</div>
    <h1>Gardening<br>Journal</h1>
    <div class="divider"></div>
    <div class="subtitle">Track Every Seed, Every Bloom, Every Harvest</div>
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
      <tr><td class="label">Garden Location</td><td class="fill"></td></tr>
      <tr><td class="label">USDA Hardiness Zone</td><td class="fill"></td></tr>
      <tr><td class="label">Garden Type</td><td class="fill"></td></tr>
      <tr><td class="label">Garden Size</td><td class="fill"></td></tr>
    </table>
  </div>
  <div style="margin-top: 16px; font-size: 7.5pt; color: #888; font-style: italic; text-align: center; line-height: 1.5;">
    Record your garden journey through every season.<br>
    Each entry builds a growing record you will treasure for years.
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_how_to_use():
    items = [
        "Record each garden entry as soon as you finish your session while memories are fresh. Fill in the fields on the left page, then write your observations on the right.",
        "Use the garden sketch area to draw your bed layout, mark where you planted, or plan where new plants will go.",
        "Track your garden through all four seasons. Note the weather, soil moisture, and which tasks you completed each time you visit the garden.",
        "Use the companion planting guide to plan which plants grow best side by side, and the planting calendar to know when to sow each crop.",
        "At season's end, use the summary pages to tally your harvest, count your gardening days, and set goals for next year.",
        "This journal fits 35 garden entries. Keep it with your garden tools so it is always ready for your next visit.",
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
  <div style="margin-top: 14px; padding: 8px 10px; background: #e8e2d4; border-radius: 4px; border-left: 3px solid #C4A04A;">
    <div style="font-size: 7pt; color: #888; text-transform: uppercase; letter-spacing: 1px; font-family: 'Helvetica Neue', 'Arial', sans-serif; margin-bottom: 3px;">Garden Wisdom</div>
    <div style="font-size: 7.5pt; color: #555; line-height: 1.4; font-style: italic;">
      The best fertilizer is the gardener's shadow. Visit your garden often, observe closely,
      and this journal will become a living record of everything you grow.
    </div>
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_garden_overview():
    return """
<div class="page verso">
  <div class="page-title">Garden Overview</div>
  <div class="page-subtitle">Your garden at a glance</div>
  <div style="margin-top: 10px;">
    <table class="kv-table">
      <tr>
        <td class="label">Garden Name</td><td class="fill"></td>
        <td class="label">Location</td><td class="fill"></td>
      </tr>
      <tr>
        <td class="label">Zone</td><td class="fill"></td>
        <td class="label">Size</td><td class="fill"></td>
      </tr>
      <tr>
        <td class="label">Soil Type</td><td class="fill"></td>
        <td class="label">Sun Exposure</td><td class="fill"></td>
      </tr>
      <tr>
        <td class="label">Water Source</td><td class="fill"></td>
        <td class="label">Years Gardening</td><td class="fill"></td>
      </tr>
    </table>
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_entry_left(entry_num):
    return f"""
<div class="page recto">
  <div class="entry-header">
    <span class="title">Garden Entry</span>
    <span class="number">#{entry_num:02d}</span>
  </div>

  <table class="kv-table">
    <tr>
      <td class="label">Date</td><td class="fill"></td>
      <td class="label">Day</td><td class="fill"></td>
    </tr>
  </table>

  <div class="section-bar">Season</div>
  <div class="check-row">
    <span class="check-item"><span class="check-box"></span>Spring</span>
    <span class="check-item"><span class="check-box"></span>Summer</span>
    <span class="check-item"><span class="check-box"></span>Fall</span>
    <span class="check-item"><span class="check-box"></span>Winter</span>
  </div>

  <div class="section-bar">Weather</div>
  <div class="check-row">
    <span class="check-item"><span class="check-box"></span>Sunny</span>
    <span class="check-item"><span class="check-box"></span>Cloudy</span>
    <span class="check-item"><span class="check-box"></span>Rain</span>
    <span class="check-item"><span class="check-box"></span>Overcast</span>
    <span class="check-item"><span class="check-box"></span>Hot</span>
    <span class="check-item"><span class="check-box"></span>Cool</span>
    <span class="check-item"><span class="check-box"></span>Frost</span>
  </div>
  <table class="kv-table">
    <tr>
      <td class="label">Temp</td><td class="fill"></td>
      <td class="label">Soil Moisture</td><td class="fill"></td>
    </tr>
  </table>

  <div class="section-bar">Tasks Done</div>
  <div class="check-row">
    <span class="check-item"><span class="check-box"></span>Planted</span>
    <span class="check-item"><span class="check-box"></span>Watered</span>
    <span class="check-item"><span class="check-box"></span>Weeded</span>
    <span class="check-item"><span class="check-box"></span>Pruned</span>
    <span class="check-item"><span class="check-box"></span>Fertilized</span>
    <span class="check-item"><span class="check-box"></span>Harvested</span>
    <span class="check-item"><span class="check-box"></span>Composted</span>
    <span class="check-item"><span class="check-box"></span>Mulched</span>
  </div>

  <div class="section-bar">Plants Today</div>
  <table class="log-table">
    <tr><th>Plant / Variety</th><th>Action</th><th>Qty</th><th>Location / Bed</th></tr>
    <tr><td></td><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td><td></td></tr>
  </table>

  <table class="kv-table" style="margin-top: 7px;">
    <tr>
      <td class="label">Time Spent</td><td class="fill"></td>
      <td class="label">Helpers</td><td class="fill"></td>
    </tr>
  </table>

  <div class="page-footer">Entry #{entry_num:02d}</div>
</div>"""


def page_entry_right(entry_num):
    return f"""
<div class="page verso">
  <div class="entry-header">
    <span class="title">Garden Notes</span>
    <span class="number">#{entry_num:02d}</span>
  </div>

  <div class="field-label" style="margin-bottom: 3px;">Garden Sketch &amp; Bed Layout</div>
  <div class="garden-sketch" style="width: 100%; height: 1.8in;"></div>

  <div class="section-bar">Observations &amp; Growth Notes</div>
  <div class="write-line"></div>
  <div class="write-line"></div>
  <div class="write-line"></div>

  <div class="section-bar">Pests / Diseases Spotted</div>
  <table class="kv-table">
    <tr><td class="label">Pest</td><td class="fill"></td><td class="label">Affected Plant</td><td class="fill"></td></tr>
    <tr><td class="label">Treatment</td><td class="fill" colspan="3"></td></tr>
  </table>

  <div class="section-bar">Harvest Today</div>
  <table class="kv-table">
    <tr><td class="label">Plant</td><td class="fill"></td><td class="label">Amount</td><td class="fill"></td></tr>
    <tr><td class="label">Quality</td><td class="fill" colspan="3"></td></tr>
  </table>

  <div class="section-bar">Challenges &amp; Lessons</div>
  <div class="write-line"></div>
  <div class="write-line"></div>

  <div class="check-row" style="margin-top: 6px;">
    <span class="check-item"><span class="check-box"></span>Bloom / Fruit Photos Taken</span>
  </div>

  <div class="rating-row" style="margin-top: 6px;">
    <div class="rating-group">
      <span class="rating-label">Enjoyment</span>
      <span class="star">&#9734;&#9734;&#9734;&#9734;&#9734;</span>
    </div>
  </div>

  <div class="page-footer">Entry #{entry_num:02d}</div>
</div>"""


def page_season_summary():
    return """
<div class="page recto">
  <div class="page-title">Season Summary</div>
  <div class="page-subtitle">Tally your garden season at a glance</div>

  <table class="kv-table">
    <tr>
      <td class="label" style="width:50%">Total Gardening Days</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Total Hours</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Plants Started</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Plants Harvested</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Total Harvest Weight</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Most Successful Crop</td><td class="fill"></td>
    </tr>
    <tr>
      <td class="label" style="width:50%">Biggest Challenge</td><td class="fill"></td>
    </tr>
  </table>

  <div class="section-bar">Top 5 Crops</div>
  <table class="kv-table">
    <tr><td class="label" style="width:12%">#</td><td class="label" style="width:30%">Crop</td><td class="label" style="width:58%">Why / Notes</td></tr>
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


def page_companion_planting():
    pairs = [
        ("Tomato + Basil", "Basil repels pests that trouble tomatoes and is said to improve flavor. Plant them as close neighbors."),
        ("Carrot + Onion", "Onions deter carrot flies, and carrots deter onion flies. A classic mutual-protection pairing."),
        ("Bean + Corn", "Beans fix nitrogen in the soil, feeding the tall corn, while corn stalks give beans a natural pole to climb."),
        ("Cucumber + Radish", "Radishes repel cucumber beetles. Sow radishes around cucumbers and let them go to seed as a trap crop."),
        ("Lettuce + Strawberry", "Lettuce grows low and shades strawberry roots, keeping soil cool and moist while deterring weeds."),
        ("Pepper + Okra", "Okra's tall stems provide wind protection for peppers, and peppers help repel some okra pests."),
        ("Marigold + Tomato", "Marigolds repel nematodes in the soil and discourage many common tomato pests with their scent."),
        ("Nasturtium + Cucumber", "Nasturtiums act as a trap crop for aphids and crawling pests, drawing them away from cucumbers."),
    ]
    items_html = ""
    for i, (title, desc) in enumerate(pairs):
        items_html += (
            f'<div class="companion-item">'
            f'<div class="companion-num">{i+1}</div>'
            f'<div class="companion-text"><strong>{title}</strong><br>{desc}</div>'
            f'</div>'
        )

    return f"""
<div class="page verso">
  <div class="page-title">Companion Planting Guide</div>
  <div class="page-subtitle">Plants that grow better together</div>
  <div style="margin-top: 4px;">
    {items_html}
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_garden_essentials():
    essentials = [
        ("Quality Soil / Compost", "Foundation of every healthy garden"),
        ("Hand Trowel", "For digging, transplanting, and potting"),
        ("Pruning Shears", "For trimming, deadheading, and harvesting"),
        ("Watering Can / Hose", "Gentle, consistent watering for young plants"),
        ("Garden Gloves", "Protect your hands from thorns and soil"),
        ("Seeds / Seedlings", "The starts of everything you will grow"),
        ("Plant Markers", "Label what you planted and where"),
        ("Sun Hat", "Shade for long hours in the garden"),
        ("Knee Pad", "Comfort for planting and weeding low"),
        ("Garden Fork", "For turning compost and aerating soil"),
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
  <div class="page-title">Garden Essentials</div>
  <div class="page-subtitle">Tools every gardener should have</div>
  <div class="essentials-grid">
    {cards_html}
  </div>
  <div style="margin-top: 14px; padding: 8px 10px; background: #e8e2d4; border-radius: 4px; border-left: 3px solid #C4A04A;">
    <div style="font-size: 7pt; color: #888; text-transform: uppercase; letter-spacing: 1px; font-family: 'Helvetica Neue', 'Arial', sans-serif; margin-bottom: 3px;">Gardener's Rule</div>
    <div style="font-size: 7.5pt; color: #555; line-height: 1.4; font-style: italic;">
      Take care of your tools and they will take care of your garden.
      Clean, sharpen, and store them properly after every use.
    </div>
  </div>
  <div class="page-footer">More Shine Press</div>
</div>"""


def page_planting_calendar():
    seasons = [
        ("Spring", ["Peas", "Lettuce", "Spinach", "Radish", "Carrot", "Onion"]),
        ("Summer", ["Tomato", "Pepper", "Cucumber", "Bean", "Squash", "Corn"]),
        ("Fall", ["Kale", "Broccoli", "Cabbage", "Garlic", "Beet", "Turnip"]),
    ]

    cats_html = ""
    for season_name, items in seasons:
        items_html = "".join([
            f'<span class="cal-item"><span class="check-box"></span>{item}</span>'
            for item in items
        ])
        cats_html += (
            f'<div class="cal-category">'
            f'<div class="cal-cat-title">{season_name}</div>'
            f'<div class="cal-items">{items_html}</div>'
            f'</div>'
        )

    return f"""
<div class="page verso">
  <div class="page-title">Planting Calendar</div>
  <div class="page-subtitle">When to plant your favorite crops</div>
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
    pages_html.append(("overview", page_garden_overview()))

    # Garden entry spreads (pages 5-74)
    for i in range(1, NUM_ENTRIES + 1):
        pages_html.append((f"entry_left_{i}", page_entry_left(i)))
        pages_html.append((f"entry_right_{i}", page_entry_right(i)))

    # Back matter (pages 75-80)
    pages_html.append(("summary", page_season_summary()))
    pages_html.append(("companion", page_companion_planting()))
    pages_html.append(("essentials", page_garden_essentials()))
    pages_html.append(("calendar", page_planting_calendar()))
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
    print(f"     Garden entries: {NUM_ENTRIES}")
    print(f"     Publisher: More Shine Press")
    print(f"")
    print(f"     Next: open {abs_path} in browser")
    print(f"           Then Cmd+P -> Save as PDF (Margins: None, Scale: 100%)")
