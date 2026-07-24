#!/usr/bin/env python3
"""
Wedding Planner -- KDP Interior Generator
Trim: 8 x 10 in | Language: English
Target: Brides and couples planning their wedding
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "wedding_planner_us_V1.0.html")

BOOK_TITLE = "Wedding Planner"
BOOK_SUBTITLE = "Your Complete Guide to the Perfect Day"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

def nl(n):
    return "\n".join('<div class="notes-line"></div>' for _ in range(n))

CSS = r"""
@page { size: 8in 10in; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: Georgia, "Iowan Old Style", "Palatino", serif;
  color: #2A2A2A;
  background: white;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

.page {
  width: 8in; height: 10in;
  padding: 0.6in 0.6in 0.5in 0.6in;
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
  width: 8in; height: 10in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(165deg, #0F0E0C 0%, #1A1612 30%, #0F0E0C 65%, #080706 100%);
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #B8860B, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #B8860B, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #B8860B, transparent);
}

.cover .title-main {
  font-size: 36pt;
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
  background: #B8860B;
  margin: 20px auto;
  position: relative;
  z-index: 2;
}

.cover .subtitle {
  font-size: 13pt;
  color: #D4B896;
  font-style: italic;
  line-height: 1.5;
  position: relative;
  z-index: 2;
}

.cover .pub {
  position: absolute;
  bottom: 0.7in;
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
  color: #B8860B;
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
  color: #161616;
  letter-spacing: 0.5pt;
  text-transform: uppercase;
}

.section-line {
  flex: 1;
  height: 1px;
  background: #B8860B;
  margin: 0 12px;
  opacity: 0.4;
}

/* ================ HOW TO USE ================ */
.howto-text { font-size: 10pt; line-height: 1.7; }
.howto-text p { margin-bottom: 8px; }
.howto-text .ht-title {
  font-size: 11pt; font-weight: 700; color: #161616;
  margin-bottom: 4px; margin-top: 6px;
}
.howto-text .ht-icon { color: #B8860B; font-weight: 700; margin-right: 4px; }

/* ================ INFO FIELDS ================ */
.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
  margin-bottom: 8px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #B8860B;
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

/* ================ VENDOR BANNER ================ */
.vendor-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1.5px solid #B8860B;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.vendor-banner .vb-num {
  display: inline-block;
  border: 1.5px solid #B8860B;
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 8pt;
  color: #B8860B;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.vendor-banner .vb-label {
  font-size: 8pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.vendor-banner .vb-line {
  flex: 1;
  height: 12px;
  border-bottom: 1px dotted #ccc;
}

/* ================ CATEGORY CHECKBOXES ================ */
.cat-row {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-bottom: 8px;
}

.cat-check {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 7.5pt;
  color: #555;
}

.cat-box {
  width: 10px; height: 10px;
  border: 1.5px solid #B8860B;
  border-radius: 2px;
}

/* ================ DATA TABLE ================ */
.data-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
}

.data-table th {
  font-size: 6.5pt;
  color: #B8860B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 5px 3px;
  border-bottom: 1.5px solid #B8860B;
  text-align: center;
}

.data-table th:first-child { text-align: left; }

.data-table td {
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
  color: #B8860B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 3px;
}

.write-box .wb-area {
  height: 28px;
}

/* ================ METRIC ROWS ================ */
.metric-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 6px 10px;
  margin-bottom: 8px;
}

.metric-field .mf-label {
  font-size: 6.5pt;
  color: #B8860B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  display: block;
  margin-bottom: 1px;
}

.metric-field .mf-write {
  height: 18px;
  border-bottom: 1px dotted #ccc;
}

/* ================ QUOTE BOX ================ */
.quote-box {
  border: 1.5px solid #B8860B;
  border-radius: 4px;
  padding: 8px;
  margin-bottom: 8px;
}

.quote-box .qb-label {
  font-size: 7pt;
  color: #B8860B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 4px;
}

.quote-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 6px;
}

.quote-field .qf-label {
  font-size: 6pt;
  color: #999;
  text-transform: uppercase;
  font-weight: 700;
  display: block;
  margin-bottom: 1px;
}

.quote-field .qf-write {
  height: 16px;
  border-bottom: 1px dotted #ccc;
}

/* ================ RATING DOTS ================ */
.score-dots {
  display: flex;
  gap: 4px;
  margin-top: 2px;
}

.score-dot {
  width: 12px; height: 12px;
  border: 1.5px solid #B8860B;
  border-radius: 50%;
}

/* ================ COUNTDOWN TRACKER ================ */
.countdown-row {
  display: flex;
  gap: 4px;
  margin-top: 2px;
}

.countdown-week {
  width: 26px; height: 26px;
  border: 1px solid #B8860B;
  border-radius: 2px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 6pt;
  color: #999;
}

/* ================ BUDGET BAR ================ */
.budget-bar-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
}

.budget-bar-cat {
  font-size: 8pt;
  color: #555;
  width: 1.5in;
  flex-shrink: 0;
}

.budget-bar-track {
  flex: 1;
  height: 14px;
  border: 1px solid #C4A04A;
  border-radius: 3px;
  position: relative;
}

.budget-bar-fill {
  width: 0;
  height: 100%;
  background: linear-gradient(90deg, #B8860B, #C4A04A);
  border-radius: 2px;
}

.budget-bar-amt {
  font-size: 7pt;
  color: #999;
  width: 0.8in;
  text-align: right;
  flex-shrink: 0;
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
  width: 60px; height: 1.5px; background: #B8860B;
  margin: 12px auto; opacity: 0.5;
}
"""


def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="110" height="110" xmlns="http://www.w3.org/2000/svg">
      <!-- Two interlocking wedding rings -->
      <g transform="translate(50,52)">
        <!-- Left ring -->
        <circle cx="-12" cy="0" r="18" stroke="#B8860B" stroke-width="2" fill="none"/>
        <!-- Right ring (interlocking) -->
        <circle cx="12" cy="0" r="18" stroke="#C4A04A" stroke-width="2" fill="none"/>
        <!-- Left ring highlight -->
        <path d="M -24,-10 A 18,18 0 0,1 -6,-16" stroke="#D4B896" stroke-width="1" fill="none"/>
        <!-- Right ring highlight -->
        <path d="M 0,-16 A 18,18 0 0,1 18,-10" stroke="#D4B896" stroke-width="1" fill="none"/>
        <!-- Small diamond accent above -->
        <path d="M 0,-28 L 4,-23 L 0,-18 L -4,-23 Z" fill="#C4A04A"/>
        <path d="M 0,-28 L 4,-23 L 0,-18 L -4,-23 Z" stroke="#B8860B" stroke-width="0.5" fill="none"/>
        <!-- Sparkle -->
        <circle cx="0" cy="-23" r="1" fill="#D4B896"/>
      </g>
    </svg>
  </div>

  <div class="title-main">Wedding<br>Planner</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Your Complete Guide<br>to the Perfect Day</div>

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
    <div class="ht-title"><span class="ht-icon">&#10058;</span> Your Wedding Companion</div>
    <p>This planner guides you through every step of your wedding
    journey, from the first vision to the final toast. Whether you
    have a year or three months, staying organized is the key to
    enjoying the process and creating the day you have always
    dreamed of.</p>

    <div class="ht-title"><span class="ht-icon">&#10058;</span> The Two-Page Vendor Spread</div>
    <p>Each vendor or planning category uses a <strong>two-page
    spread</strong>. The left page captures the essentials: vendor
    type, company name, contact details, appointment dates, quote
    amounts, deposit status, and a rating. The right page is for
    your notes: what they offer, questions to ask, comparison
    details, and your overall impression.</p>

    <div class="ht-title"><span class="ht-icon">&#10058;</span> The Milestone Review</div>
    <p>After every 5 vendors, a <strong>milestone review page</strong>
    helps you step back and reflect: what is decided, what still
    needs attention, how the budget is holding up, and how you are
    feeling about the big day.</p>

    <div class="ht-title"><span class="ht-icon">&#10058;</span> Additional Sections</div>
    <p>&#9679; <strong>Wedding Overview</strong> -- your date, venue,
    colors, and theme at a glance.</p>
    <p>&#9679; <strong>Budget Summary</strong> -- track spending across
    every category.</p>
    <p>&#9679; <strong>Guest List Manager</strong> -- manage addresses,
    RSVPs, and dietary needs.</p>
    <p>&#9679; <strong>Seating Arrangement</strong> -- plan table layouts
    and guest placement.</p>
    <p>&#9679; <strong>Day-of Timeline</strong> -- minute-by-minute
    schedule for the wedding day.</p>
  </div>
</div>""" % (pg, pg)


def overview_page():
    pg = pn()
    return """<!-- PAGE %d: Our Wedding Day -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Our Wedding Day</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">The Big Day</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Wedding Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Day of the Week</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Ceremony Time</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Reception Time</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Ceremony Venue</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Reception Venue</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">City &amp; State</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Expected Guests</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Our Color Palette</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Our Theme &amp; Style</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Total Budget</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Engaged On</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Countdown (Days)</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">What This Day Means to Us</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>
</div>""" % (pg, pg)


def vision_page():
    pg = pn()
    return """<!-- PAGE %d: Wedding Vision -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Wedding Vision &amp; Inspiration</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Our Dream Day</div>
    <div class="section-line"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">The Atmosphere We Want (Romantic, Fun, Elegant, Rustic, Modern...)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Season &amp; Setting (Indoor, Outdoor, Garden, Beach, Barn, Ballroom...)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Must-Have Moments (First Dance, Vows, Surprise, Family Traditions...)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Flowers &amp; Decor Ideas</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Food &amp; Drink Vision</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Inspiration (Designers, Blogs, Pinterest Boards, Real Weddings We Love)</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def budget_page():
    pg = pn()
    cats = [
        "Venue", "Catering &amp; Bar", "Photography", "Videography",
        "Florals &amp; Decor", "Attire &amp; Accessories", "Music &amp; Entertainment",
        "Invitations &amp; Stationery", "Cake &amp; Desserts", "Transportation",
        "Hair &amp; Makeup", "Favors &amp; Gifts", "Rental Equipment", "Lighting",
        "Officiant", "Honeymoon", "Other / Misc",
    ]
    cat_rows = "\n".join(
        '<div class="budget-bar-row"><div class="budget-bar-cat">%s</div>'
        '<div class="budget-bar-track"><div class="budget-bar-fill"></div></div>'
        '<div class="budget-bar-amt"></div></div>' % c
        for c in cats
    )
    return """<!-- PAGE %d: Budget Tracker -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Budget Summary</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Budget by Category</div>
    <div class="section-line"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Total Budget</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Spent So Far</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Remaining</span><div class="mf-write"></div></div>
  </div>

  %s

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Payment Schedule &amp; Deposits</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>
</div>""" % (pg, pg, cat_rows)


def vendor_left(entry_num):
    pg = pn()
    categories = [
        "Venue", "Caterer", "Bar &amp; Drinks", "Photographer", "Videographer",
        "Florist", "Officiant", "Music / DJ", "Band", "Cake &amp; Bakery",
        "Wedding Dress", "Bridal Party Attire", "Tuxedo / Suit", "Hair &amp; Makeup",
        "Invitations", "Transportation", "Rentals", "Lighting &amp; Decor",
        "Photo Booth", "Favors",
    ]
    cats_html = " ".join(
        '<span class="cat-check"><span class="cat-box"></span>%s</span>' % c
        for c in categories
    )
    return """<!-- PAGE %d: Vendor Left #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Vendor &amp; Planning Tracker</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="vendor-banner">
    <span class="vb-num">Entry #%03d</span>
    <span class="vb-label">Vendor / Category:</span>
    <div class="vb-line"></div>
  </div>

  <div class="cat-row">%s</div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Company Name</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Contact Person</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Phone</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Email</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Website</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Office Address</span><div class="if-write"></div></div>
  </div>

  <div class="quote-box">
    <div class="qb-label">Quote &amp; Booking</div>
    <div class="quote-grid">
      <div class="quote-field"><span class="qf-label">Quoted Price</span><div class="qf-write"></div></div>
      <div class="quote-field"><span class="qf-label">Deposit Due</span><div class="qf-write"></div></div>
      <div class="quote-field"><span class="qf-label">Balance Due</span><div class="qf-write"></div></div>
    </div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Appointment Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Contract Signed?</span><div class="if-write"></div></div>
  </div>

  <div style="display: flex; gap: 12px; margin-top: 8px;">
    <div>
      <div style="font-size: 7pt; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; margin-bottom: 3px;">Rating</div>
      <div class="score-dots">
        <div class="score-dot"></div>
        <div class="score-dot"></div>
        <div class="score-dot"></div>
        <div class="score-dot"></div>
        <div class="score-dot"></div>
      </div>
    </div>
    <div style="flex: 1;">
      <div style="font-size: 7pt; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; margin-bottom: 3px;">Booked?</div>
      <div style="display: flex; gap: 12px; margin-top: 2px;">
        <span class="cat-check"><span class="cat-box"></span>Yes</span>
        <span class="cat-check"><span class="cat-box"></span>Maybe</span>
        <span class="cat-check"><span class="cat-box"></span>No</span>
      </div>
    </div>
  </div>
</div>""" % (pg, entry_num, pg, entry_num, cats_html)


def vendor_right():
    pg = pn()
    return """<!-- PAGE %d: Vendor Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes &amp; Details</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">What They Offer (Package Details, Inclusions, Services)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Questions to Ask</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Pros &amp; Cons (What We Liked / Did Not Like)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Comparison With Other Options</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Final Notes &amp; Impressions</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Next Steps / Follow-Up</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def milestone_review_page(review_num):
    pg = pn()
    return """<!-- PAGE %d: Milestone Review #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Milestone Review</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Check-in #%d</div>
    <div class="section-line"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Vendors Booked</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Budget Used</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Days to Go</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">What Is Decided So Far</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">What Still Needs Attention</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Surprises &amp; Lessons Learned</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Goals for Next Phase</div>
    <div class="wb-area"></div>
  </div>

  <div style="display: flex; gap: 12px; margin-top: 6px;">
    <div>
      <div style="font-size: 7pt; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; margin-bottom: 3px;">How We Feel</div>
      <div class="score-dots">
        <div class="score-dot"></div>
        <div class="score-dot"></div>
        <div class="score-dot"></div>
        <div class="score-dot"></div>
        <div class="score-dot"></div>
      </div>
    </div>
    <div style="flex: 1; align-self: flex-end;">
      <div style="font-size: 7pt; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700;">Stress Level: Excited / Calm / Managing / Stressed</div>
    </div>
  </div>
</div>""" % (pg, review_num, pg, review_num)


def guest_list_page():
    pg = pn()
    return """<!-- PAGE %d: Guest List -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Guest List Manager</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Guest List</div>
    <div class="section-line"></div>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Guest Name</th>
        <th>Side</th>
        <th>Address</th>
        <th>RSVP</th>
        <th>+1</th>
        <th>Meal</th>
      </tr>
    </thead>
    <tbody>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Invited</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Yes</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">No</span><div class="mf-write"></div></div>
  </div>
</div>""" % (pg, pg)


def seating_page():
    pg = pn()
    return """<!-- PAGE %d: Seating Arrangement -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Seating Arrangement</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Table Layout</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Total Tables</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Guests per Table</span><div class="if-write"></div></div>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Table #</th>
        <th>Table Name / Theme</th>
        <th>Guests Assigned</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>1</td><td></td><td></td><td></td></tr>
      <tr><td>2</td><td></td><td></td><td></td></tr>
      <tr><td>3</td><td></td><td></td><td></td></tr>
      <tr><td>4</td><td></td><td></td><td></td></tr>
      <tr><td>5</td><td></td><td></td><td></td></tr>
      <tr><td>6</td><td></td><td></td><td></td></tr>
      <tr><td>7</td><td></td><td></td><td></td></tr>
      <tr><td>8</td><td></td><td></td><td></td></tr>
      <tr><td>9</td><td></td><td></td><td></td></tr>
      <tr><td>10</td><td></td><td></td><td></td></tr>
      <tr><td>11</td><td></td><td></td><td></td></tr>
      <tr><td>12</td><td></td><td></td><td></td></tr>
      <tr><td>13</td><td></td><td></td><td></td></tr>
      <tr><td>14</td><td></td><td></td><td></td></tr>
      <tr><td>15</td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Seating Notes (Family Dynamics, VIPs, Special Requests)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>
</div>""" % (pg, pg)


def day_of_timeline_page():
    pg = pn()
    return """<!-- PAGE %d: Day-of Timeline -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Day-of Timeline</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Wedding Day Schedule</div>
    <div class="section-line"></div>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 0.8in;">Time</th>
        <th>Event / Activity</th>
        <th>Location</th>
        <th>Who</th>
      </tr>
    </thead>
    <tbody>
      <tr><td></td><td>Hair &amp; Makeup Start</td><td></td><td></td></tr>
      <tr><td></td><td>Bridal Party Arrives</td><td></td><td></td></tr>
      <tr><td></td><td>Photographer Arrives</td><td></td><td></td></tr>
      <tr><td></td><td>Getting Ready Photos</td><td></td><td></td></tr>
      <tr><td></td><td>First Look</td><td></td><td></td></tr>
      <tr><td></td><td>Bridal Party Photos</td><td></td><td></td></tr>
      <tr><td></td><td>Family Photos</td><td></td><td></td></tr>
      <tr><td></td><td>Guests Arrive</td><td></td><td></td></tr>
      <tr><td></td><td>Ceremony Begins</td><td></td><td></td></tr>
      <tr><td></td><td>Ceremony Ends</td><td></td><td></td></tr>
      <tr><td></td><td>Cocktail Hour</td><td></td><td></td></tr>
      <tr><td></td><td>Reception Opens</td><td></td><td></td></tr>
      <tr><td></td><td>First Dance</td><td></td><td></td></tr>
      <tr><td></td><td>Dinner Service</td><td></td><td></td></tr>
      <tr><td></td><td>Toasts &amp; Speeches</td><td></td><td></td></tr>
      <tr><td></td><td>Parent Dances</td><td></td><td></td></tr>
      <tr><td></td><td>Cake Cutting</td><td></td><td></td></tr>
      <tr><td></td><td>Bouquet Toss</td><td></td><td></td></tr>
      <tr><td></td><td>Open Dance Floor</td><td></td><td></td></tr>
      <tr><td></td><td>Grand Exit / Send-Off</td><td></td><td></td></tr>
    </tbody>
  </table>
</div>""" % (pg, pg)


def wedding_party_page():
    pg = pn()
    return """<!-- PAGE %d: Wedding Party -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Wedding Party &amp; Roles</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Our Wedding Party</div>
    <div class="section-line"></div>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Role</th>
        <th>Name</th>
        <th>Phone</th>
        <th>Attire Fitted?</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Maid of Honor</td><td></td><td></td><td></td></tr>
      <tr><td>Matron of Honor</td><td></td><td></td><td></td></tr>
      <tr><td>Bridesmaid</td><td></td><td></td><td></td></tr>
      <tr><td>Bridesmaid</td><td></td><td></td><td></td></tr>
      <tr><td>Bridesmaid</td><td></td><td></td><td></td></tr>
      <tr><td>Bridesmaid</td><td></td><td></td><td></td></tr>
      <tr><td>Flower Girl</td><td></td><td></td><td></td></tr>
      <tr><td>Best Man</td><td></td><td></td><td></td></tr>
      <tr><td>Groomsman</td><td></td><td></td><td></td></tr>
      <tr><td>Groomsman</td><td></td><td></td><td></td></tr>
      <tr><td>Groomsman</td><td></td><td></td><td></td></tr>
      <tr><td>Groomsman</td><td></td><td></td><td></td></tr>
      <tr><td>Ring Bearer</td><td></td><td></td><td></td></tr>
      <tr><td>Usher</td><td></td><td></td><td></td></tr>
      <tr><td>Officiant</td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Special Roles (Readers, Musicians, Program Distributors)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>
</div>""" % (pg, pg)


def checklist_page():
    pg = pn()
    return """<!-- PAGE %d: Final Checklist -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Final Countdown Checklist</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Last Weeks</div>
    <div class="section-line"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">2 Weeks Before</div>
    <div style="font-size: 8pt; color: #555; line-height: 1.8;">
      &#9744; Final headcount to caterer &nbsp;&#9744; Confirm all vendors<br>
      &#9744; Seating chart finalized &nbsp;&#9744; Wedding rings picked up<br>
      &#9744; Marriage license obtained &nbsp;&#9744; Final dress fitting<br>
      &#9744; Confirm honeymoon travel &nbsp;&#9744; Break in wedding shoes<br>
      &#9744; Create vendor tip envelopes &nbsp;&#9744; Assign day-of point person
    </div>
  </div>

  <div class="write-box">
    <div class="wb-label">1 Week Before</div>
    <div style="font-size: 8pt; color: #555; line-height: 1.8;">
      &#9744; Give final guest count to venue &nbsp;&#9744; Confirm seating chart<br>
      &#9744; Pack overnight bag &nbsp;&#9744; Pick up wedding attire<br>
      &#9744; Confirm transportation &nbsp;&#9744; Review timeline with vendors<br>
      &#9744; Practice vows &nbsp;&#9744; Get a manicure<br>
      &#9744; Confirm DJ / band playlist &nbsp;&#9744; Sleep and hydrate
    </div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Day Before</div>
    <div style="font-size: 8pt; color: #555; line-height: 1.8;">
      &#9744; Confirm setup times &nbsp;&#9744; Charge devices<br>
      &#9744; Prepare wedding rings &nbsp;&#9744; Iron / steam attire<br>
      &#9744; Get plenty of rest &nbsp;&#9744; Stay hydrated<br>
      &#9744; Decor items ready &nbsp;&#9744; Rehearsal &amp; rehearsal dinner
    </div>
  </div>

  <div class="write-box">
    <div class="wb-label">Morning of the Wedding</div>
    <div style="font-size: 8pt; color: #555; line-height: 1.8;">
      &#9744; Eat a good breakfast &nbsp;&#9744; Hair &amp; makeup<br>
      &#9744; Put on dress last &nbsp;&#9744; Something borrowed / blue / old / new<br>
      &#9744; Trust your planning &nbsp;&#9744; Breathe and enjoy every moment
    </div>
  </div>
</div>""" % (pg, pg)


def notes_page():
    pg = pn()
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes &amp; Ideas</span>
    <span class="ph-right">Page %d</span>
  </div>
  <div>%s</div>
</div>""" % (pg, pg, nl(34))


def final_page():
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="page">
  <div class="final-page">
    <div class="fp-text">
      Every love story is beautiful,<br>
      but yours is our favorite.<br>
      Plan with love. Celebrate with joy.<br>
      Cherish every moment.
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
    pages.append(overview_page())
    pages.append(vision_page())
    pages.append(budget_page())

    # 25 vendor spreads (50 pages), with a milestone review every 5
    entry_count = 0
    review_count = 0
    for entry in range(1, 26):
        pages.append(vendor_left(entry))
        pages.append(vendor_right())
        entry_count += 1
        if entry_count % 5 == 0:
            review_count += 1
            pages.append(milestone_review_page(review_count))

    # Guest List (4 pages)
    for _ in range(4):
        pages.append(guest_list_page())

    # Seating Arrangement (2 pages)
    for _ in range(2):
        pages.append(seating_page())

    # Day-of Timeline (2 pages)
    for _ in range(2):
        pages.append(day_of_timeline_page())

    # Wedding Party & Roles (2 pages)
    for _ in range(2):
        pages.append(wedding_party_page())

    # Final Checklist (2 pages)
    for _ in range(2):
        pages.append(checklist_page())

    # Notes (5 pages)
    for _ in range(5):
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
