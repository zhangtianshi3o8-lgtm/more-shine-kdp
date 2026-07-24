#!/usr/bin/env python3
"""
Running Training Log -- KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Runners of all levels
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "running_training_log_us_V1.0.html")

BOOK_TITLE = "Running Training Log"
BOOK_SUBTITLE = "Track Every Run, Every Mile, Every Goal"

# Accent color: electric orange
ACCENT = "#E85D2A"
ACCENT_D = "#C04A1F"
GOLD = "#C4A04A"
GOLD_L = "#D4B896"

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
  background: linear-gradient(165deg, #161616 0%, #2A2A2A 30%, #161616 65%, #0E0E0E 100%);
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
    radial-gradient(ellipse 30px 18px at 15%% 20%%, #E85D2A, transparent),
    radial-gradient(ellipse 26px 16px at 80%% 15%%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70%% 70%%, #E85D2A, transparent),
    radial-gradient(ellipse 22px 14px at 25%% 80%%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50%% 45%%, #E85D2A, transparent);
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
  background: #E85D2A;
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
  color: #E85D2A;
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
  background: #E85D2A;
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
.howto-text .ht-icon { color: #E85D2A; font-weight: 700; margin-right: 4px; }

/* ================ INFO FIELDS ================ */
.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
  margin-bottom: 8px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #E85D2A;
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

/* ================ RUN BANNER ================ */
.run-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1.5px solid #E85D2A;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.run-banner .rb-num {
  display: inline-block;
  border: 1.5px solid #E85D2A;
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 8pt;
  color: #E85D2A;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.run-banner .rb-label {
  font-size: 8pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.run-banner .rb-line {
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
  border: 1.5px solid #E85D2A;
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
  color: #E85D2A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 5px 3px;
  border-bottom: 1.5px solid #E85D2A;
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
  color: #E85D2A;
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
  color: #E85D2A;
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

/* ================ SCORE DOTS ================ */
.score-dots {
  display: flex;
  gap: 4px;
  margin-top: 2px;
}

.score-dot {
  width: 12px; height: 12px;
  border: 1.5px solid #E85D2A;
  border-radius: 50%;
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
  width: 60px; height: 1.5px; background: #E85D2A;
  margin: 12px auto; opacity: 0.5;
}
"""


def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- Running shoe silhouette (minimal line art) -->
      <g transform="translate(50,52)">
        <!-- Sole -->
        <path d="M -35,18 Q -36,22 -30,22 L 28,22 Q 34,22 34,17 L 34,13 L -34,13 Z"
              fill="none" stroke="#E85D2A" stroke-width="2" stroke-linejoin="round"/>
        <!-- Upper shoe body -->
        <path d="M -32,13 L -32,2 Q -30,-4 -22,-6 L -8,-10 Q 2,-12 10,-8 Q 20,-3 28,3 L 32,8 L 32,13"
              fill="none" stroke="#E85D2A" stroke-width="2" stroke-linejoin="round"/>
        <!-- Laces detail -->
        <line x1="-14" y1="-4" x2="-4" y2="-2" stroke="#E85D2A" stroke-width="1" opacity="0.6"/>
        <line x1="-12" y1="1" x2="-2" y2="3" stroke="#E85D2A" stroke-width="1" opacity="0.6"/>
        <line x1="-10" y1="6" x2="0" y2="7" stroke="#E85D2A" stroke-width="1" opacity="0.6"/>
        <!-- Heel curve -->
        <path d="M -32,2 Q -34,8 -32,13" fill="none" stroke="#E85D2A" stroke-width="2"/>
        <!-- Accent dot -->
        <circle cx="20" cy="0" r="2" fill="#C4A04A"/>
      </g>
    </svg>
  </div>

  <div class="title-main">Running<br>Training<br>Log</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Track Every Run, Every Mile,<br>Every Goal</div>

  <div class="pub">More Shine Press</div>
</div>""" % pn()


def how_to_use_page():
    pg = pn()
    return """<!-- PAGE %d: How to Use -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">How to Use This Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Training Partner</div>
    <p>This log is designed to make you a stronger, smarter runner.
    Every serious runner keeps records -- not because they enjoy
    paperwork, but because reviewing past training is the fastest
    path to consistent improvement and fewer injuries.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Two-Page Run Spread</div>
    <p>Each run uses a <strong>two-page spread</strong>. The left page
    captures the essentials: date, distance, duration, pace, route,
    weather, effort, heart rate, and calories. The right page is for
    your reflections: how it felt, what went well, what to improve,
    shoes worn, route notes, and workout type.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Weekly Summary</div>
    <p>After every 5 runs, a <strong>weekly summary page</strong> helps
    you track total mileage, average pace, longest and shortest runs,
    elevation gain, rest days, and notes on how the week went.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips for Success</div>
    <p>&#9679; <strong>Log it right away.</strong> Fill in each run while
    the details are fresh in your mind.</p>
    <p>&#9679; <strong>Be honest about effort.</strong> Record how hard
    the run truly felt, not just the numbers.</p>
    <p>&#9679; <strong>Watch your shoes.</strong> Track mileage on each
    pair so you know when to replace them.</p>
    <p>&#9679; <strong>Review regularly.</strong> Patterns and progress
    emerge over weeks, not single runs.</p>
  </div>
</div>""" % (pg, pg)


def season_goals_page():
    pg = pn()
    return """<!-- PAGE %d: Season Goals -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Season Goals</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Season Goals</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Season / Year</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Season Start Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Current Weekly Mileage</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Target Weekly Mileage</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #E85D2A; text-transform: uppercase; letter-spacing: 0.5pt; margin: 10px 0 6px;">Goal Races</div>
  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Race 1 Name</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Date</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Distance</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Race 2 Name</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Date</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Distance</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Race 3 Name</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Date</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Distance</span><div class="mf-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #E85D2A; text-transform: uppercase; letter-spacing: 0.5pt; margin: 10px 0 6px;">Target Times</div>
  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">5K Target</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">10K Target</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Half Marathon Target</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Marathon Target</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Custom Distance</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Custom Target</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #E85D2A;">
    <div class="wb-label">Personal Goals for This Season</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Key Workouts to Focus On</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>
</div>""" % (pg, pg)


def run_left(entry_num):
    pg = pn()
    weather_opts = ["Sunny", "Cloudy", "Rain", "Wind", "Snow", "Hot", "Cold"]
    weather_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % w
        for w in weather_opts
    )
    return """<!-- PAGE %d: Run Left #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Run Record</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="run-banner">
    <span class="rb-num">Run #%03d</span>
    <span class="rb-label">Date:</span>
    <div class="rb-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Day of Week</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Route / Location</span><div class="if-write"></div></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Distance (mi)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Duration</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Pace (min/mi)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Effort (1-10)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Avg Heart Rate</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Max Heart Rate</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Calories</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Elevation (ft)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Temp (&#176;F)</span><div class="mf-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #E85D2A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Weather Conditions</div>
  <div class="type-row">%s</div>

  <div class="write-box" style="border-color: #E85D2A;">
    <div class="wb-label">Warmup / Cooldown Notes</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Splits (Mile 1 / 2 / 3 / 4 / 5 / 6+)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>
</div>""" % (pg, entry_num, pg, entry_num, weather_html)


def run_right():
    pg = pn()
    workout_types = ["Easy", "Tempo", "Intervals", "Long", "Recovery", "Race"]
    wt_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % w
        for w in workout_types
    )
    return """<!-- PAGE %d: Run Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Run Reflection</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 8px;">
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #E85D2A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">How Did It Feel? (1-10)</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Terrible &#160; 10 = Amazing</div>
    </div>
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #E85D2A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Energy Level</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Drained &#160; 5 = Full</div>
    </div>
  </div>

  <div class="write-box" style="border-color: #E85D2A;">
    <div class="wb-label">What Went Well</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #C0392B;">
    <div class="wb-label">What to Improve</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #E85D2A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Workout Type</div>
  <div class="type-row">%s</div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Shoes Worn</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Time of Day</span><div class="if-write"></div></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Route Notes / Terrain Details</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #C4A04A;">
    <div class="wb-label">General Notes</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>
</div>""" % (pg, pg, wt_html)


def weekly_summary_page(review_num):
    pg = pn()
    return """<!-- PAGE %d: Weekly Summary #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Weekly Summary</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="run-banner">
    <span class="rb-num">Week #%02d</span>
    <span class="rb-label">Week of:</span>
    <div class="rb-line"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Total Distance (mi)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Total Time</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Avg Pace (min/mi)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Longest Run (mi)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Shortest Run (mi)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Total Runs</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Elevation (ft)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Rest Days</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Avg Heart Rate</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #E85D2A;">
    <div class="wb-label">Best Run This Week (What Made It Great)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #C0392B;">
    <div class="wb-label">Toughest Run This Week (What Was Hard)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Body / Health Notes (Aches, Soreness, Sleep)</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #E85D2A;">
    <div class="wb-label">Focus for Next Week</div>
    <div class="wb-area"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-top: 4px;">
    <div>
      <div style="font-size: 6.5pt; font-weight: 700; color: #E85D2A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Overall Fitness</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
    </div>
    <div>
      <div style="font-size: 6.5pt; font-weight: 700; color: #E85D2A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Motivation</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
    </div>
    <div>
      <div style="font-size: 6.5pt; font-weight: 700; color: #E85D2A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Recovery</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
    </div>
  </div>
</div>""" % (pg, review_num, pg, review_num)


def shoe_tracking_page():
    pg = pn()
    return """<!-- PAGE %d: Shoe Tracking -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Shoe Tracking</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Shoe Name / Model</th>
        <th>Brand</th>
        <th>Date Started</th>
        <th>Miles Logged</th>
        <th>Retire At (mi)</th>
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
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="write-box" style="margin-top: 8px; border-color: #E85D2A;">
    <div class="wb-label">Shoe Rotation Notes</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>
</div>""" % (pg, pg)


def race_results_page():
    pg = pn()
    return """<!-- PAGE %d: Race Results -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Race Results</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Race Name</th>
        <th>Date</th>
        <th>Distance</th>
        <th>Time</th>
        <th>Pace</th>
        <th>Place</th>
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
    </tbody>
  </table>

  <div class="write-box" style="margin-top: 8px; border-color: #E85D2A;">
    <div class="wb-label">PR (Personal Record) Highlights</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>
</div>""" % (pg, pg)


def monthly_summary_page():
    pg = pn()
    return """<!-- PAGE %d: Monthly Summary -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Monthly Summary</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Month / Year</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Races Run</span><div class="if-write"></div></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Total Miles</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Total Runs</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Avg Distance (mi)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Longest Run (mi)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Avg Pace (min/mi)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Total Elevation (ft)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Rest Days</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Injuries / Issues</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Goals Met</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #E85D2A;">
    <div class="wb-label">Biggest Win This Month</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #C0392B;">
    <div class="wb-label">Biggest Challenge / Setback</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #E85D2A;">
    <div class="wb-label">Goal for Next Month</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Notes / Observations</div>
    <div class="wb-area" style="height: 32px;"></div>
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
      Every mile counts.<br>
      Every run builds the next.<br>
      Keep showing up.
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
    pages.append(season_goals_page())

    # 25 run spreads (50 pages), with a weekly summary every 5 runs
    run_count = 0
    review_count = 0
    for entry in range(1, 26):
        pages.append(run_left(entry))
        pages.append(run_right())
        run_count += 1
        # Insert weekly summary after every 5th run
        if run_count % 5 == 0:
            review_count += 1
            pages.append(weekly_summary_page(review_count))

    # Shoe Tracking (2 pages)
    for _ in range(2):
        pages.append(shoe_tracking_page())

    # Race Results (2 pages)
    for _ in range(2):
        pages.append(race_results_page())

    # Monthly Summary (2 pages)
    for _ in range(2):
        pages.append(monthly_summary_page())

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
