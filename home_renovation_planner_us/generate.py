#!/usr/bin/env python3
"""
Home Renovation Planner -- KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Homeowners, DIYers, home improvement enthusiasts
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "home_renovation_planner_us_V1.0.html")

BOOK_TITLE = "Home Renovation Planner"
BOOK_SUBTITLE = "Plan Every Project, Every Budget, Every Detail"

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
  background: linear-gradient(165deg, #1A1410 0%, #2E2218 30%, #1A1410 65%, #0F0A06 100%);
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #B85C2E, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #B85C2E, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #B85C2E, transparent);
}

.cover .title-main {
  font-size: 30pt;
  font-weight: 700;
  color: #FAF6F0;
  line-height: 1.2;
  letter-spacing: 0.5pt;
  position: relative;
  z-index: 2;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 100px; height: 2px;
  background: #B85C2E;
  margin: 20px auto;
  position: relative;
  z-index: 2;
}

.cover .subtitle {
  font-size: 12pt;
  color: #D4B896;
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
  color: #B85C2E;
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
  color: #1A1410;
  letter-spacing: 0.5pt;
  text-transform: uppercase;
}

.section-line {
  flex: 1;
  height: 1px;
  background: #B85C2E;
  margin: 0 12px;
  opacity: 0.4;
}

/* ================ HOW TO USE ================ */
.howto-text { font-size: 10pt; line-height: 1.7; }
.howto-text p { margin-bottom: 8px; }
.howto-text .ht-title {
  font-size: 11pt; font-weight: 700; color: #1A1410;
  margin-bottom: 4px; margin-top: 6px;
}
.howto-text .ht-icon { color: #B85C2E; font-weight: 700; margin-right: 4px; }

/* ================ INFO FIELDS ================ */
.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
  margin-bottom: 8px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #B85C2E;
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

/* ================ PROJECT BANNER ================ */
.project-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1.5px solid #B85C2E;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.project-banner .pb-num {
  display: inline-block;
  border: 1.5px solid #B85C2E;
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 8pt;
  color: #B85C2E;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.project-banner .pb-label {
  font-size: 8pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.project-banner .pb-line {
  flex: 1;
  height: 12px;
  border-bottom: 1px dotted #ccc;
}

/* ================ TYPE CHECKBOXES ================ */
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
  border: 1.5px solid #B85C2E;
  border-radius: 2px;
}

/* ================ MATERIAL TABLE ================ */
.material-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
}

.material-table th {
  font-size: 6.5pt;
  color: #B85C2E;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 5px 3px;
  border-bottom: 1.5px solid #B85C2E;
  text-align: center;
}

.material-table th:first-child { text-align: left; }

.material-table td {
  padding: 4px 3px;
  border-bottom: 1px solid #eee;
  height: 24px;
  font-size: 9pt;
}

/* ================ WRITE BOX ================ */
.write-box {
  border: 1px solid #C4A04A;
  border-radius: 3px;
  padding: 6px 8px;
  margin-bottom: 8px;
}

.write-box .wb-label {
  font-size: 7pt;
  color: #B85C2E;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 3px;
}

.write-box .wb-area {
  height: 28px;
}

/* ================ BUDGET TABLE ================ */
.budget-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 8px;
}

.budget-table th {
  font-size: 6.5pt;
  color: #B85C2E;
  text-transform: uppercase;
  padding: 4px 3px;
  border-bottom: 1.5px solid #B85C2E;
  text-align: center;
}

.budget-table th:first-child { text-align: left; }

.budget-table td {
  padding: 4px 3px;
  border-bottom: 1px solid #eee;
  height: 22px;
  font-size: 9pt;
}

.budget-total {
  font-weight: 700;
  border-top: 1.5px solid #B85C2E;
}

/* ================ NOTES ================ */
.notes-line { border-bottom: 1px solid #ddd; height: 22px; }

/* ================ FINAL PAGE ================ */
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
  width: 60px; height: 1.5px; background: #B85C2E;
  margin: 12px auto; opacity: 0.5;
}
"""


def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- House icon -->
      <g transform="translate(50,50)">
        <!-- Roof -->
        <path d="M -30 -5 L 0 -30 L 30 -5" stroke="#B85C2E" stroke-width="2.5" fill="none" stroke-linejoin="round"/>
        <!-- Walls -->
        <path d="M -24 -5 L -24 25 L 24 25 L 24 -5" stroke="#B85C2E" stroke-width="2" fill="none"/>
        <!-- Door -->
        <rect x="-6" y="8" width="12" height="17" stroke="#B85C2E" stroke-width="1.5" fill="none"/>
        <!-- Windows -->
        <rect x="-18" y="0" width="8" height="8" stroke="#B85C2E" stroke-width="1.2" fill="none"/>
        <rect x="10" y="0" width="8" height="8" stroke="#B85C2E" stroke-width="1.2" fill="none"/>
        <!-- Chimney -->
        <rect x="12" y="-22" width="5" height="10" stroke="#B85C2E" stroke-width="1.2" fill="none"/>
      </g>
    </svg>
  </div>

  <div class="title-main">Home<br>Renovation<br>Planner</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Plan Every Project, Every Budget, Every Detail</div>

  <div class="pub">More Shine Press</div>
</div>""" % pn()


def how_to_use_page():
    pg = pn()
    return """<!-- PAGE %d: How to Use -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">How to Use This Planner</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Renovation Companion</div>
    <p>This planner helps you organize home improvement projects from concept
    to completion. Track materials, budgets, contractors, and timelines all
    in one place. Whether you are remodeling a kitchen or painting a room,
    this journal keeps every detail organized.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Project Pages</div>
    <p>Each project uses a <strong>two-page spread</strong>. The left page
    captures project scope, room details, materials needed, and measurements.
    The right page tracks budget, contractor info, timeline, and progress
    notes.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips</div>
    <p>&#9679; <strong>Always add 15-20 percent contingency.</strong> Surprises happen
    once walls come open.</p>
    <p>&#9679; <strong>Get three quotes.</strong> Compare contractor bids on
    the same scope of work.</p>
    <p>&#9679; <strong>Order materials early.</strong> Lead times can derail
    your schedule.</p>
    <p>&#9679; <strong>Document with photos.</strong> Before, during, and after
    -- for insurance and satisfaction.</p>
  </div>
</div>""" % (pg, pg)


def home_overview_page():
    pg = pn()
    return """<!-- PAGE %d: Home Overview -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Home Overview</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">My Home</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Property Address</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Year Built</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Square Footage</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Lot Size</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Bedrooms / Bathrooms</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Style / Type</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Purchase Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Purchase Price</span><div class="if-write"></div></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Rooms / Spaces to Renovate (Priority List)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #B85C2E;">
    <div class="wb-label">Overall Renovation Budget</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Key Contractors / Contacts</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #B85C2E;">
    <div class="wb-label">Permits / HOA Info</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def project_left(entry_num):
    pg = pn()
    project_types = ["Kitchen", "Bathroom", "Bedroom", "Living Room", "Exterior",
                     "Flooring", "Painting", "Electrical", "Plumbing", "Roofing", "Other"]
    type_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % t
        for t in project_types
    )
    return """<!-- PAGE %d: Project Left #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Project Plan</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="project-banner">
    <span class="pb-num">Project #%03d</span>
    <span class="pb-label">Room:</span>
    <div class="pb-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Project Start Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Target Completion</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">DIY or Contractor</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Estimated Budget</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #B85C2E; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Project Type</div>
  <div class="type-row">%s</div>

  <div class="write-box">
    <div class="wb-label">Scope of Work (What Needs to Be Done)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #B85C2E;">
    <div class="wb-label">Measurements (Room Dimensions, Ceiling Height)</div>
    <div class="wb-area"></div>
  </div>

  <table class="material-table">
    <thead>
      <tr>
        <th>Material / Item</th>
        <th>Qty</th>
        <th>Store / Source</th>
        <th>Est. Cost</th>
      </tr>
    </thead>
    <tbody>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>
</div>""" % (pg, entry_num, pg, entry_num, type_html)


def project_right():
    pg = pn()
    return """<!-- PAGE %d: Project Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Budget &amp; Progress</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="budget-table">
    <thead>
      <tr>
        <th>Expense Category</th>
        <th>Budgeted</th>
        <th>Actual</th>
        <th>Difference</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Materials</td><td></td><td></td><td></td></tr>
      <tr><td>Labor / Contractor</td><td></td><td></td><td></td></tr>
      <tr><td>Permits / Fees</td><td></td><td></td><td></td></tr>
      <tr><td>Tools / Equipment</td><td></td><td></td><td></td></tr>
      <tr><td>Disposal / Cleanup</td><td></td><td></td><td></td></tr>
      <tr><td>Miscellaneous</td><td></td><td></td><td></td></tr>
      <tr class="budget-total"><td>TOTAL</td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="info-row" style="margin-top: 6px;">
    <div class="info-field"><span class="if-label">Contractor Name</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Phone / Email</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">License Number</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Insurance / Bond</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B85C2E;">
    <div class="wb-label">Progress Log (What Was Done, Date)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Issues / Changes / Lessons Learned</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #B85C2E;">
    <div class="wb-label">Final Result &amp; Satisfaction (1-5)</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def contractor_directory_page():
    pg = pn()
    return """<!-- PAGE %d: Contractor Directory -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Contractor Directory</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="material-table">
    <thead>
      <tr>
        <th>Trade / Service</th>
        <th>Company / Name</th>
        <th>Phone</th>
        <th>Rating</th>
      </tr>
    </thead>
    <tbody>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>
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
      Every project improves your home.<br>
      Every detail matters.<br>
      Plan well. Build with confidence.
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
    pages.append(home_overview_page())

    # 25 project spreads (50 pages)
    for entry in range(1, 26):
        pages.append(project_left(entry))
        pages.append(project_right())

    # Contractor directory (2 pages)
    for _ in range(2):
        pages.append(contractor_directory_page())

    # Notes (4 pages)
    for _ in range(4):
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
