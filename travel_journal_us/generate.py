#!/usr/bin/env python3
"""
Travel Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Travelers, backpackers, vacationers, digital nomads
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "travel_journal_us_V1.0.html")

BOOK_TITLE = "Travel Journal"
BOOK_SUBTITLE = "Capture Every Journey, Every Memory, Every Adventure"

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

/* TITLE PAGE */
.cover {
  width: 6in; height: 9in; padding: 0;
  page-break-after: always;
  position: relative; overflow: hidden;
  background: linear-gradient(165deg, #0A1620 0%, #102838 30%, #0A1620 65%, #050D14 100%);
  display: flex; flex-direction: column;
  justify-content: center; align-items: center; text-align: center;
}
.cover .glow-bg {
  position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.06;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #2E86AB, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #2E86AB, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #2E86AB, transparent);
}
.cover .title-main { font-size: 32pt; font-weight: 700; color: #FAF6F0; line-height: 1.2; letter-spacing: 1pt; position: relative; z-index: 2; text-shadow: 2px 2px 8px rgba(0,0,0,0.5); }
.cover .accent-bar { width: 100px; height: 2px; background: #2E86AB; margin: 20px auto; position: relative; z-index: 2; }
.cover .subtitle { font-size: 12pt; color: #8FBDD3; font-style: italic; line-height: 1.5; position: relative; z-index: 2; }
.cover .pub { position: absolute; bottom: 0.6in; left: 0; right: 0; text-align: center; font-size: 9pt; color: #C4A04A; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; }

/* PAGE HEADER */
.page-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; padding-bottom: 4px; border-bottom: 0.5px solid #eee; }
.page-header .ph-left { font-size: 8pt; color: #2E86AB; text-transform: uppercase; letter-spacing: 1pt; font-weight: 700; }
.page-header .ph-right { font-size: 8pt; color: #999; }

/* SECTION */
.section-header { display: flex; align-items: center; justify-content: center; margin-bottom: 14px; }
.section-title { font-size: 14pt; font-weight: 700; color: #0A1620; letter-spacing: 0.5pt; text-transform: uppercase; }
.section-line { flex: 1; height: 1px; background: #2E86AB; margin: 0 12px; opacity: 0.4; }

/* TRIP BANNER */
.trip-banner { display: flex; align-items: center; gap: 8px; border-bottom: 1.5px solid #2E86AB; padding-bottom: 5px; margin-bottom: 10px; }
.trip-banner .tb-num { display: inline-block; border: 1.5px solid #2E86AB; border-radius: 4px; padding: 3px 10px; font-size: 8pt; color: #2E86AB; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt; }
.trip-banner .tb-label { font-size: 8pt; color: #999; text-transform: uppercase; letter-spacing: 0.5pt; }
.trip-banner .tb-line { flex: 1; height: 12px; border-bottom: 1px dotted #ccc; }

/* INFO FIELDS */
.info-row { display: grid; grid-template-columns: 1fr 1fr; gap: 6px 12px; margin-bottom: 8px; }
.info-field .if-label { font-size: 6.5pt; color: #2E86AB; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; display: block; margin-bottom: 1px; }
.info-field .if-write { height: 16px; border-bottom: 1px dotted #ccc; }

/* WRITE BOX */
.write-box { border: 1px solid #2E86AB; border-radius: 3px; padding: 6px 8px; margin-bottom: 8px; }
.write-box .wb-label { font-size: 7pt; color: #2E86AB; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; margin-bottom: 3px; }
.write-box .wb-area { height: 24px; }

/* RATING CIRCLES */
.rating-row { display: flex; align-items: center; gap: 4px; margin-bottom: 5px; }
.rating-row .rr-label { font-size: 8pt; width: 70px; flex-shrink: 0; }
.rating-circle { width: 12px; height: 12px; border: 1.5px solid #2E86AB; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 5pt; color: #2E86AB; margin-right: 1px; }

/* CHECKBOX LISTS */
.check-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2px 12px; margin-bottom: 8px; }
.check-item { display: flex; align-items: center; gap: 4px; height: 18px; }
.check-box { width: 9px; height: 9px; border: 1px solid #2E86AB; border-radius: 2px; flex-shrink: 0; }
.check-item span { font-size: 8pt; color: #2A2A2A; }

/* ITINERARY TABLE */
.itin-table { width: 100%; border-collapse: collapse; margin-bottom: 8px; }
.itin-table th { font-size: 6.5pt; color: #2E86AB; text-transform: uppercase; letter-spacing: 0.5pt; padding: 4px 3px; border-bottom: 1.5px solid #2E86AB; text-align: left; }
.itin-table td { padding: 4px 3px; border-bottom: 1px solid #eee; height: 24px; }

/* EXPENSE TABLE */
.expense-table { width: 100%; border-collapse: collapse; }
.expense-table th { font-size: 6.5pt; color: #2E86AB; text-transform: uppercase; padding: 4px 3px; border-bottom: 1.5px solid #2E86AB; text-align: left; }
.expense-table td { padding: 4px 3px; border-bottom: 1px solid #eee; height: 20px; font-size: 8pt; }
.expense-total { font-weight: 700; border-top: 1.5px solid #2E86AB !important; }

/* NOTES */
.notes-line { border-bottom: 1px solid #ddd; height: 22px; }

/* FINAL */
.final-page { display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; height: 100%; }
.final-page .fp-text { font-size: 12pt; color: #999; font-style: italic; line-height: 1.8; margin-bottom: 20px; }
.final-page .fp-logo { font-size: 11pt; color: #C4A04A; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; }
.final-page .fp-line { width: 60px; height: 1.5px; background: #2E86AB; margin: 12px auto; opacity: 0.5; }

/* HOW-TO */
.howto-text { font-size: 10pt; line-height: 1.7; }
.howto-text p { margin-bottom: 8px; }
.howto-text .ht-title { font-size: 11pt; font-weight: 700; color: #0A1620; margin-bottom: 4px; margin-top: 6px; }
.howto-text .ht-icon { color: #2E86AB; font-weight: 700; margin-right: 4px; }
"""


def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- Compass -->
      <circle cx="50" cy="50" r="40" stroke="#2E86AB" stroke-width="1.5" fill="none"/>
      <circle cx="50" cy="50" r="32" stroke="#2E86AB" stroke-width="1" fill="none" opacity="0.4"/>
      <!-- Compass needle -->
      <polygon points="50,20 45,50 50,45 55,50" fill="#2E86AB" opacity="0.6"/>
      <polygon points="50,80 45,50 50,55 55,50" fill="#C4A04A" opacity="0.6"/>
      <!-- Cardinal points -->
      <text x="46" y="16" font-family="Georgia" font-size="8" fill="#2E86AB" font-weight="bold">N</text>
      <text x="46" y="92" font-family="Georgia" font-size="8" fill="#C4A04A">S</text>
      <text x="80" y="54" font-family="Georgia" font-size="8" fill="#C4A04A">E</text>
      <text x="13" y="54" font-family="Georgia" font-size="8" fill="#C4A04A">W</text>
      <circle cx="50" cy="50" r="3" fill="#2E86AB"/>
    </svg>
  </div>

  <div class="title-main">Travel Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Capture Every Journey, Every Memory, Every Adventure</div>

  <div class="pub">More Shine Press</div>
</div>""" % pn()


def how_to_use_page():
    pg = pn()
    return """<!-- PAGE %d: How to Use -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">How to Use This Journal</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Travel Companion</div>
    <p>The world is full of incredible places waiting to be discovered.
    This journal helps you plan your trips, record your experiences, and
    preserve your travel memories for years to come.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Trip Log</div>
    <p>Each trip uses a <strong>three-page spread</strong>. Page one captures the
    essentials: destination, dates, companions, transportation, and accommodation.
    Page two is your daily itinerary planner. Page three holds your memories,
    highlights, food discoveries, expenses, and reflections.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips</div>
    <p>&#9679; <strong>Write daily.</strong> Even a few lines keep memories vivid.</p>
    <p>&#9679; <strong>Note the food.</strong> Meals are often the best memories.</p>
    <p>&#9679; <strong>Sketch or paste.</strong> Ticket stubs, receipts, leaves — all welcome.</p>
    <p>&#9679; <strong>Track spending.</strong> The expense log helps you budget future trips.</p>
  </div>
</div>""" % (pg, pg)


def bucket_list_page():
    pg = pn()
    destinations = [
        "Northern Lights (Aurora)", "Safari in Africa", "Great Wall of China",
        "Machu Picchu", "Pyramids of Giza", "Tokyo, Japan",
        "Paris, France", "Grand Canyon", "Great Barrier Reef",
        "Northern Italy", "Iceland Ring Road", "Patagonia",
        "Santorini, Greece", "New York City", "Petra, Jordan",
        "Angkor Wat, Cambodia", "Amalfi Coast", "Norwegian Fjords",
        "Galapagos Islands", "Route 66 Road Trip", "Bali, Indonesia",
        "Maldives", "Swiss Alps", "Amazon Rainforest",
    ]
    items_html = "\n".join(
        '<div class="check-item"><div class="check-box"></div><span>%s</span></div>'
        % H.escape(d)
        for d in destinations
    )
    return """<!-- PAGE %d: Bucket List -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Travel Bucket List</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Dreams &amp; Destinations</div>
    <div class="section-line"></div>
  </div>

  <div class="check-grid">%s</div>

  <div class="write-box" style="margin-top: 6px; border-color: #C4A04A;">
    <div class="wb-label" style="color: #C4A04A;">Add Your Own Destinations</div>
    <div class="wb-area" style="height: 50px;"></div>
  </div>
</div>""" % (pg, pg, items_html)


def trip_page_1(trip_num):
    pg = pn()
    transport = ["Plane", "Train", "Car", "Bus", "Boat", "Bike", "Walking", "Other"]
    transport_html = " ".join(
        '<span class="check-item" style="margin-right: 4px;"><span class="check-box"></span><span style="font-size: 7.5pt;">%s</span></span>'
        % t for t in transport
    )
    return """<!-- PAGE %d: Trip #%d Essentials -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Trip Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="trip-banner">
    <span class="tb-num">Trip #%03d</span>
    <span class="tb-label">Destination:</span>
    <div class="tb-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Country / Region</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">City / Town</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Date Departure</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Date Return</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Duration (Days)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Trip Type</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #2E86AB; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Transportation</div>
  <div style="margin-bottom: 8px;">%s</div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Travel Companions</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Weather / Season</span><div class="if-write"></div></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Accommodation Details (Name, Address, Cost)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #C4A04A;">
    <div class="wb-label" style="color: #C4A04A;">Pre-Trip Notes &amp; Reservations</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>
</div>""" % (pg, trip_num, pg, trip_num, transport_html)


def trip_page_2():
    pg = pn()
    rows = ""
    days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    for day in days:
        rows += '<tr><td style="font-weight:700; color:#2E86AB;">%s</td><td></td><td></td><td></td></tr>\n' % day
    return """<!-- PAGE %d: Itinerary -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Daily Itinerary</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Plan Each Day</div>
    <div class="section-line"></div>
  </div>

  <table class="itin-table">
    <thead>
      <tr>
        <th style="width: 45px;">Day</th>
        <th>Morning Plan</th>
        <th>Afternoon Plan</th>
        <th>Evening Plan</th>
      </tr>
    </thead>
    <tbody>%s</tbody>
  </table>

  <div class="write-box" style="margin-top: 6px;">
    <div class="wb-label">Must-See Places / Bookings / Tickets</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>
</div>""" % (pg, pg, rows)


def trip_page_3():
    pg = pn()
    exp_rows = ""
    categories = ["Flights", "Lodging", "Food & Drink", "Transport (local)", "Activities/Tickets", "Shopping", "Other"]
    for cat in categories:
        exp_rows += '<tr><td>%s</td><td></td><td></td></tr>\n' % cat
    return """<!-- PAGE %d: Memories & Expenses -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Memories &amp; Expenses</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="write-box">
    <div class="wb-label">Best Moments &amp; Highlights</div>
    <div class="wb-area" style="height: 44px;"></div>
  </div>

  <div class="write-box" style="border-color: #C4A04A;">
    <div class="wb-label" style="color: #C4A04A;">Food &amp; Drink Discoveries</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="rating-row" style="margin-top: 4px;">
    <span class="rr-label">Overall Trip</span>
    <span class="rating-circle">1</span><span class="rating-circle">2</span>
    <span class="rating-circle">3</span><span class="rating-circle">4</span>
    <span class="rating-circle">5</span>
  </div>

  <table class="expense-table" style="margin-top: 6px;">
    <thead>
      <tr>
        <th>Expense Category</th>
        <th style="width: 60px;">Budget</th>
        <th style="width: 60px;">Actual</th>
      </tr>
    </thead>
    <tbody>
      %s
      <tr class="expense-total"><td>Total</td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="write-box" style="border-color: #2E86AB;">
    <div class="wb-label">What I Learned / Would Do Differently</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg, exp_rows)


def country_tracker_page():
    pg = pn()
    rows = ""
    for _ in range(20):
        rows += '<tr><td style="text-align:center; width:30px;"><span class="check-box" style="display:inline-block;"></span></td><td></td><td></td><td></td></tr>\n'
    return """<!-- PAGE %d: Countries Visited -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Countries &amp; Places Visited</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">My Travel Map</div>
    <div class="section-line"></div>
  </div>

  <table class="itin-table">
    <thead>
      <tr>
        <th>Visited</th>
        <th>Country / Place</th>
        <th style="width: 80px;">Year</th>
        <th style="width: 80px;">Highlights</th>
      </tr>
    </thead>
    <tbody>%s</tbody>
  </table>
</div>""" % (pg, pg, rows)


def notes_page():
    pg = pn()
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes &amp; Memories</span>
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
      Not all those who wander<br>
      are lost.<br>
      Travel far, travel often,<br>
      and write it all down.
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
    pages.append(bucket_list_page())

    # 15 trips x 3 pages each = 45 pages
    for trip in range(1, 16):
        pages.append(trip_page_1(trip))
        pages.append(trip_page_2())
        pages.append(trip_page_3())

    # Country tracker
    pages.append(country_tracker_page())
    pages.append(country_tracker_page())

    # Notes
    for _ in range(2):
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
