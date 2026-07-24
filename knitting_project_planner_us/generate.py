#!/usr/bin/env python3
"""
Knitting Project Planner -- KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Knitters and crocheters tracking projects
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "knitting_project_planner_us_V1.0.html")

BOOK_TITLE = "Knitting Project Planner"
BOOK_SUBTITLE = "Track Every Stitch, Finish Every Project"

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
  background: #B8860B;
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

/* ================ SESSION BANNER ================ */
.session-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1.5px solid #B8860B;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.session-banner .sb-num {
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

.session-banner .sb-label {
  font-size: 8pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.session-banner .sb-line {
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

/* ================ GAUGE BOX ================ */
.gauge-box {
  border: 1.5px solid #B8860B;
  border-radius: 4px;
  padding: 8px;
  margin-bottom: 8px;
}

.gauge-box .gb-label {
  font-size: 7pt;
  color: #B8860B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 4px;
}

.gauge-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 6px;
}

.gauge-field .gf-label {
  font-size: 6pt;
  color: #999;
  text-transform: uppercase;
  font-weight: 700;
  display: block;
  margin-bottom: 1px;
}

.gauge-field .gf-write {
  height: 16px;
  border-bottom: 1px dotted #ccc;
}

/* ================ SCORE DOTS ================ */
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

/* ================ HABIT TRACKER ================ */
.habit-track {
  display: flex;
  gap: 4px;
  margin-top: 2px;
}

.habit-day {
  width: 22px; height: 22px;
  border: 1px solid #B8860B;
  border-radius: 2px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 6pt;
  color: #999;
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
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- Two crossed knitting needles with a yarn ball -->
      <g transform="translate(50,50)">
        <!-- Needle 1 (diagonal) -->
        <line x1="-32" y1="28" x2="28" y2="-30" stroke="#B8860B" stroke-width="2" stroke-linecap="round"/>
        <!-- Needle 1 tip -->
        <circle cx="28" cy="-30" r="2.5" fill="#C4A04A"/>
        <!-- Needle 2 (diagonal opposite) -->
        <line x1="32" y1="28" x2="-28" y2="-30" stroke="#B8860B" stroke-width="2" stroke-linecap="round"/>
        <!-- Needle 2 tip -->
        <circle cx="-28" cy="-30" r="2.5" fill="#C4A04A"/>
        <!-- Yarn ball (center) -->
        <circle cx="0" cy="0" r="14" stroke="#B8860B" stroke-width="2" fill="none"/>
        <path d="M -10,-6 Q 0,-10 10,-4" stroke="#C4A04A" stroke-width="1.5" fill="none"/>
        <path d="M -8,2 Q 2,8 9,0" stroke="#C4A04A" stroke-width="1.5" fill="none"/>
        <path d="M -5,8 Q 3,4 7,9" stroke="#B8860B" stroke-width="1.2" fill="none"/>
        <!-- Yarn strand trailing -->
        <path d="M 14,0 Q 28,4 36,-8 Q 40,-16 34,-22" stroke="#B8860B" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      </g>
    </svg>
  </div>

  <div class="title-main">Knitting<br>Project<br>Planner</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Track Every Stitch,<br>Finish Every Project</div>

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
    <div class="ht-title"><span class="ht-icon">&#10058;</span> Your Knitting Companion</div>
    <p>This planner is designed to help you stay organized from
    cast-on to bind-off. Whether you knit sweaters, scarves, socks,
    blankets, or amigurumi, keeping detailed project records is the
    key to finishing what you start and repeating what works.</p>

    <div class="ht-title"><span class="ht-icon">&#10058;</span> The Two-Page Project Spread</div>
    <p>Each project uses a <strong>two-page spread</strong>. The left
    page captures the project overview: name, pattern, yarn details,
    needle sizes, gauge swatch, start and end dates, and a project
    checklist. The right page is for your notes: stitch pattern
    details, adjustments made, rows completed per session, problems
    solved, and what you would do differently next time.</p>

    <div class="ht-title"><span class="ht-icon">&#10058;</span> The Progress Review</div>
    <p>After every 5 projects, a <strong>progress review page</strong>
    helps you reflect on your knitting journey: total time invested,
    techniques learned, favorite projects, and goals for the next
    batch.</p>

    <div class="ht-title"><span class="ht-icon">&#10058;</span> Additional Sections</div>
    <p>&#9679; <strong>Needle &amp; Hook Inventory</strong> -- track every
    needle and hook you own.</p>
    <p>&#9679; <strong>Yarn Stash Tracker</strong> -- log your yarn by
    weight, color, fiber, and yardage.</p>
    <p>&#9679; <strong>Pattern Library</strong> -- keep a running list
    of patterns you want to try.</p>
    <p>&#9679; <strong>Gift Log</strong> -- track handknit gifts and
    who received them.</p>
  </div>
</div>""" % (pg, pg)


def goals_page():
    pg = pn()
    return """<!-- PAGE %d: Knitting Goals -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Knitting Goals</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">My Goals</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Year</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Start Date</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Projects I Want to Make</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">New Techniques to Learn</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Projects Goal</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Gifts Planned</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Yarn Budget</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Challenge Project (Something New)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Inspiration (Designers, Patterns, Ideas)</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Why I Knit -- What It Means to Me</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>
</div>""" % (pg, pg)


def project_left(entry_num):
    pg = pn()
    types = ["Sweater", "Scarf", "Hat", "Socks", "Blanket", "Shawl", "Mittens", "Toy"]
    types_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % t
        for t in types
    )
    return """<!-- PAGE %d: Project Left #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Project Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="session-banner">
    <span class="sb-num">Project #%03d</span>
    <span class="sb-label">Project Name:</span>
    <div class="sb-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Pattern Source</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Designer</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">For (Recipient)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Size</span><div class="if-write"></div></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Start Date</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Target Finish</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Actual Finish</span><div class="mf-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Project Type (Check All)</div>
  <div class="type-row">%s</div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Yarn Used</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Yarn Weight</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Total Skeins</span><div class="mf-write"></div></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Yarn Color(s)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Dye Lot</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Fiber Content</span><div class="mf-write"></div></div>
  </div>

  <div class="gauge-box">
    <div class="gb-label">Gauge Swatch</div>
    <div class="gauge-grid">
      <div class="gauge-field"><span class="gf-label">Needle Size</span><div class="gf-write"></div></div>
      <div class="gauge-field"><span class="gf-label">Sts / 4 in</span><div class="gf-write"></div></div>
      <div class="gauge-field"><span class="gf-label">Rows / 4 in</span><div class="gf-write"></div></div>
      <div class="gauge-field"><span class="gf-label">Hook Size</span><div class="gf-write"></div></div>
    </div>
  </div>

  <div class="write-box">
    <div class="wb-label">Total Yardage / Meterage Used</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, entry_num, pg, entry_num, types_html)


def project_right():
    pg = pn()
    return """<!-- PAGE %d: Project Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Project Notes</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Stitch Pattern(s) Used</div>
    <div class="wb-area"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Cast On Sts</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Total Rows</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Total Time (hrs)</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Adjustments &amp; Modifications</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #8B4040;">
    <div class="wb-label">Problems Encountered &amp; Solutions</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Buttons, Zippers, or Notions</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Care Instructions (Wash, Block, Dry)</div>
    <div class="wb-area"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 6px;">
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Difficulty</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Beginner &#160; 5 = Expert</div>
    </div>
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Satisfaction</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Not Happy &#160; 5 = Love It</div>
    </div>
  </div>
</div>""" % (pg, pg)


def progress_review_page(review_num):
    pg = pn()
    days_html = "".join(
        '<div class="habit-day">%s</div>' % d
        for d in ["M", "T", "W", "T", "F", "S", "S"]
    )
    return """<!-- PAGE %d: Progress Review #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Progress Review</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="session-banner">
    <span class="sb-num">Review #%02d</span>
    <span class="sb-label">Period:</span>
    <div class="sb-line"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Projects Finished</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Projects in Progress</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Total Knitting Hours</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Favorite Project &amp; Why</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">New Techniques Learned</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #8B4040;">
    <div class="wb-label">Biggest Challenge &amp; What I Learned</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Goals for Next Period</div>
    <div class="wb-area"></div>
  </div>

  <div style="margin-top: 6px;">
    <div style="font-size: 6.5pt; font-weight: 700; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Habit Tracker -- Knitted X/7 Days</div>
    <div class="habit-track">%s</div>
  </div>
</div>""" % (pg, review_num, pg, review_num, days_html)


def needle_inventory_page():
    pg = pn()
    return """<!-- PAGE %d: Needle & Hook Inventory -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Needle &amp; Hook Inventory</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Size (US)</th>
        <th>Size (mm)</th>
        <th>Type</th>
        <th>Length</th>
        <th>Material</th>
        <th>Qty</th>
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
    </tbody>
  </table>
</div>""" % (pg, pg)


def yarn_stash_page():
    pg = pn()
    return """<!-- PAGE %d: Yarn Stash Tracker -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Yarn Stash Tracker</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Brand / Name</th>
        <th>Weight</th>
        <th>Color</th>
        <th>Fiber</th>
        <th>Skeins</th>
        <th>Yards</th>
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
    </tbody>
  </table>
</div>""" % (pg, pg)


def pattern_library_page():
    pg = pn()
    return """<!-- PAGE %d: Pattern Wishlist -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Pattern Wishlist</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Pattern Name</th>
        <th>Designer</th>
        <th>Type</th>
        <th>Difficulty</th>
        <th>Tried?</th>
      </tr>
    </thead>
    <tbody>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>
</div>""" % (pg, pg)


def gift_log_page():
    pg = pn()
    return """<!-- PAGE %d: Gift Log -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Handknit Gift Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Project</th>
        <th>Recipient</th>
        <th>Occasion</th>
        <th>Date Given</th>
        <th>Reaction</th>
      </tr>
    </thead>
    <tbody>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>
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
</div>""" % (pg, pg, nl(28))


def final_page():
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="page">
  <div class="final-page">
    <div class="fp-text">
      Every stitch tells a story.<br>
      Every project is a journey.<br>
      Cast on. Knit with love. Finish with pride.
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
    pages.append(goals_page())

    # 25 project spreads (50 pages), with a progress review every 5 projects
    project_count = 0
    review_count = 0
    for entry in range(1, 26):
        pages.append(project_left(entry))
        pages.append(project_right())
        project_count += 1
        # Insert progress review after every 5th project
        if project_count % 5 == 0:
            review_count += 1
            pages.append(progress_review_page(review_count))

    # Needle & Hook Inventory (2 pages)
    for _ in range(2):
        pages.append(needle_inventory_page())

    # Yarn Stash Tracker (2 pages)
    for _ in range(2):
        pages.append(yarn_stash_page())

    # Pattern Wishlist (1 page)
    pages.append(pattern_library_page())

    # Gift Log (1 page)
    pages.append(gift_log_page())

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
