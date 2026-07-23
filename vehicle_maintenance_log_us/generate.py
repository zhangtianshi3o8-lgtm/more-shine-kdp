#!/usr/bin/env python3
"""
Vehicle Maintenance Log Book -- KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Car/truck owners, DIY mechanics, fleet managers
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "vehicle_maintenance_log_us_V1.0.html")

BOOK_TITLE = "Vehicle Maintenance Log Book"
BOOK_SUBTITLE = "Track Every Service, Every Mile, Every Repair"

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
  background: linear-gradient(165deg, #121826 0%, #1A2332 30%, #121826 65%, #0A0F1A 100%);
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #3D6FA8, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #3D6FA8, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #3D6FA8, transparent);
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
  background: #3D6FA8;
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
  color: #3D6FA8;
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
  color: #121826;
  letter-spacing: 0.5pt;
  text-transform: uppercase;
}

.section-line {
  flex: 1;
  height: 1px;
  background: #3D6FA8;
  margin: 0 12px;
  opacity: 0.4;
}

/* ================ HOW TO USE ================ */
.howto-text { font-size: 10pt; line-height: 1.7; }
.howto-text p { margin-bottom: 8px; }
.howto-text .ht-title {
  font-size: 11pt; font-weight: 700; color: #121826;
  margin-bottom: 4px; margin-top: 6px;
}
.howto-text .ht-icon { color: #3D6FA8; font-weight: 700; margin-right: 4px; }

/* ================ INFO FIELDS ================ */
.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
  margin-bottom: 8px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #3D6FA8;
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

/* ================ SERVICE TABLE ================ */
.service-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
}

.service-table th {
  font-size: 6.5pt;
  color: #3D6FA8;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 5px 3px;
  border-bottom: 1.5px solid #3D6FA8;
  text-align: center;
}

.service-table th:first-child { text-align: left; }

.service-table td {
  padding: 4px 3px;
  border-bottom: 1px solid #eee;
  height: 26px;
  font-size: 9pt;
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
  border: 1.5px solid #3D6FA8;
  border-radius: 2px;
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
  color: #3D6FA8;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 3px;
}

.write-box .wb-area {
  height: 28px;
}

/* ================ SERVICE BANNER ================ */
.service-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1.5px solid #3D6FA8;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.service-banner .sb-num {
  display: inline-block;
  border: 1.5px solid #3D6FA8;
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 8pt;
  color: #3D6FA8;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.service-banner .sb-label {
  font-size: 8pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.service-banner .sb-line {
  flex: 1;
  height: 12px;
  border-bottom: 1px dotted #ccc;
}

/* ================ NOTES ================ */
.notes-line { border-bottom: 1px solid #ddd; height: 22px; }

/* ================ FUEL LOG ================ */
.fuel-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 8px;
}

.fuel-table th {
  font-size: 6pt;
  color: #3D6FA8;
  text-transform: uppercase;
  padding: 4px 2px;
  border-bottom: 1.5px solid #3D6FA8;
  text-align: center;
}

.fuel-table th:first-child { text-align: left; }

.fuel-table td {
  padding: 3px 2px;
  border-bottom: 1px solid #eee;
  height: 20px;
}

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
  width: 60px; height: 1.5px; background: #3D6FA8;
  margin: 12px auto; opacity: 0.5;
}
"""


def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- Wrench icon -->
      <g transform="translate(50,50)">
        <path d="M -28 -10 L -20 -18 A 8 8 0 0 1 -8 -10 L -10 -2 L -2 -10 A 8 8 0 0 1 -10 -22 L -2 -30"
              stroke="#3D6FA8" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <rect x="-4" y="-4" width="28" height="8" rx="2"
              stroke="#3D6FA8" stroke-width="2" fill="none" transform="rotate(45 10 0)"/>
        <circle cx="22" cy="22" r="6" stroke="#3D6FA8" stroke-width="2" fill="none"/>
      </g>
    </svg>
  </div>

  <div class="title-main">Vehicle<br>Maintenance Log</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Track Every Service, Every Mile, Every Repair</div>

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
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Vehicle Journal</div>
    <p>This log book is your vehicle's complete service history. Record every oil
    change, tire rotation, brake job, and repair. Over time, these records
    protect your investment and boost resale value.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Service Log</div>
    <p>Each service entry uses a <strong>two-page spread</strong>. The left page
    captures the date, mileage, service type, shop or DIY details, and parts used.
    The right page tracks costs, labor, fluid checks, tire condition, and notes
    for next time.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips</div>
    <p>&#9679; <strong>Log it immediately.</strong> Write entries the same day as service.</p>
    <p>&#9679; <strong>Keep receipts.</strong> Note where you filed them for warranty claims.</p>
    <p>&#9679; <strong>Track mileage.</strong> Knowing your mileage patterns helps predict
    when services are due.</p>
    <p>&#9679; <strong>Note recalls.</strong> Record any recall work performed by dealerships.</p>
  </div>
</div>""" % (pg, pg)


def vehicle_info_page():
    pg = pn()
    return """<!-- PAGE %d: Vehicle Info -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Vehicle Information</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">My Vehicle</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Year / Make / Model</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Trim / Submodel</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">VIN</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">License Plate</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Color</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Purchase Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Purchase Mileage</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Purchase Price</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Engine / Displacement</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Transmission</span><div class="if-write"></div></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Insurance Company / Policy Number</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #3D6FA8;">
    <div class="wb-label">Preferred Mechanic / Dealership / Contact</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Tire Size / Pressure (PSI)</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #3D6FA8;">
    <div class="wb-label">Oil Type / Viscosity / Filter Part Number</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def service_log_left(entry_num):
    pg = pn()
    service_types = ["Oil Change", "Tire Rotation", "Brakes", "Fluid Check", "Filter", "Battery",
                     "Alignment", "Inspection", "Repair", "Recall", "Other"]
    type_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % t
        for t in service_types
    )
    return """<!-- PAGE %d: Service Left #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Service Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="service-banner">
    <span class="sb-num">Service #%03d</span>
    <span class="sb-label">Date:</span>
    <div class="sb-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Mileage</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Next Service Due</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Performed By</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Shop / Location</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #3D6FA8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Service Type</div>
  <div class="type-row">%s</div>

  <table class="service-table">
    <thead>
      <tr>
        <th>Work Performed / Part Replaced</th>
        <th>Part Number</th>
        <th>Qty</th>
        <th>Cost</th>
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

  <div class="write-box">
    <div class="wb-label">Fluid Levels Checked (Oil / Coolant / Brake / Transmission / Washer)</div>
    <div class="wb-area" style="height: 22px;"></div>
  </div>
</div>""" % (pg, entry_num, pg, entry_num, type_html)


def service_log_right():
    pg = pn()
    return """<!-- PAGE %d: Service Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Costs &amp; Notes</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Parts Total</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Labor Total</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Tax / Fees</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Grand Total</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #3D6FA8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">
    Tire Condition (LF / RF / LR / RR)
  </div>
  <table class="service-table">
    <thead>
      <tr>
        <th>Position</th>
        <th>Tread Depth</th>
        <th>Pressure (PSI)</th>
        <th>Brand / Model</th>
        <th>Replace?</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Left Front</td><td></td><td></td><td></td><td></td></tr>
      <tr><td>Right Front</td><td></td><td></td><td></td><td></td></tr>
      <tr><td>Left Rear</td><td></td><td></td><td></td><td></td></tr>
      <tr><td>Right Rear</td><td></td><td></td><td></td><td></td></tr>
      <tr><td>Spare</td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="write-box" style="border-color: #3D6FA8;">
    <div class="wb-label">Notes &amp; Observations</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Reminder for Next Service</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def fuel_log_page():
    pg = pn()
    rows = "\n".join(
        "<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>" for _ in range(14)
    )
    return """<!-- PAGE %d: Fuel Log -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Fuel &amp; Mileage Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="fuel-table">
    <thead>
      <tr>
        <th>Date</th>
        <th>Mileage</th>
        <th>Gallons</th>
        <th>Price/Gal</th>
        <th>Total</th>
        <th>MPG</th>
      </tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>

  <div class="write-box" style="margin-top: 10px;">
    <div class="wb-label">Notes (Best / Worst MPG, Fuel Brand, Driving Conditions)</div>
    <div class="wb-area" style="height: 60px;"></div>
  </div>
</div>""" % (pg, pg, rows)


def annual_summary_page():
    pg = pn()
    return """<!-- PAGE %d: Annual Summary -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Annual Summary</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Year: __________</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Start Mileage</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">End Mileage</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Total Miles Driven</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Average MPG</span><div class="if-write"></div></div>
  </div>

  <table class="service-table">
    <thead>
      <tr>
        <th>Service Category</th>
        <th>Times Done</th>
        <th>Total Cost</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Oil Changes</td><td></td><td></td><td></td></tr>
      <tr><td>Tire Service / Replacement</td><td></td><td></td><td></td></tr>
      <tr><td>Brake Service</td><td></td><td></td><td></td></tr>
      <tr><td>Fluids / Filters</td><td></td><td></td><td></td></tr>
      <tr><td>Repairs</td><td></td><td></td><td></td></tr>
      <tr><td>Inspections / Registration</td><td></td><td></td><td></td></tr>
      <tr style="font-weight: 700;"><td>Annual Total</td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="write-box" style="border-color: #3D6FA8;">
    <div class="wb-label">Biggest Repair This Year</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Plans for Next Year</div>
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
      A well-maintained vehicle<br>
      is a reliable vehicle.<br>
      Keep this log. Drive with confidence.
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
    pages.append(vehicle_info_page())

    # 30 service log spreads (60 pages)
    for entry in range(1, 31):
        pages.append(service_log_left(entry))
        pages.append(service_log_right())
        if entry % 10 == 0:
            pages.append(annual_summary_page())

    # Fuel logs (6 pages)
    for _ in range(6):
        pages.append(fuel_log_page())

    # Notes (3 pages)
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
