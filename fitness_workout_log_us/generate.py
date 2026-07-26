#!/usr/bin/env python3
"""
Fitness & Workout Log — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Gym-goers, weightlifters, runners, fitness enthusiasts
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "fitness_workout_log_us_V1.0.html")

BOOK_TITLE = "Fitness & Workout Log"
BOOK_SUBTITLE = "Track Your Training and Crush Every Goal"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

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
  padding: 0.45in 0.5in 0.38in 0.5in;
  page-break-after: always;
  position: relative;
  background: white;
  overflow: hidden;
}
.page:last-child { page-break-after: auto; }

@media screen { .page { border: 1px dashed #ccc; margin: 8px auto; } }
@media print  { .page { border: none; margin: 0; } }

/* ================ COVER ================ */
.cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(165deg, #161616 0%, #1E1E1E 30%, #161616 65%, #0D0D0D 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.cover .glow-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #C4A04A, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #C4A04A, transparent);
}

.cover .icon-wrap {
  width: 120px; height: 120px;
  position: relative;
  margin: 0 auto 16px;
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 28pt;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.15;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 6px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 110px; height: 2.5px;
  background: #C4A04A;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 11pt;
  color: #D4B896;
  font-style: italic;
  line-height: 1.5;
  margin-bottom: 20px;
}

.cover .features {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.cover .feature-badge {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(196,160,74,0.4);
  color: #C4A04A;
  font-size: 7pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 9px;
  border-radius: 3px;
  text-transform: uppercase;
}

.cover .tagline {
  font-size: 8.5pt;
  color: #D4B896;
  letter-spacing: 2pt;
  text-transform: uppercase;
  margin-top: 8px;
}

.cover .publisher {
  position: absolute;
  bottom: 0.4in;
  left: 0; right: 0;
  text-align: center;
  font-size: 9pt;
  color: #C4A04A;
  letter-spacing: 2pt;
  text-transform: uppercase;
  font-weight: 700;
}

/* ================ SECTION DIVIDER ================ */
.divider {
  width: 6in; height: 9in;
  page-break-after: always;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  background: linear-gradient(165deg, #161616 0%, #1E1E1E 50%, #161616 100%);
  position: relative;
  overflow: hidden;
}

.divider .div-glow {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 25px 15px at 80% 30%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 25% 85%, #C4A04A, transparent);
}

.divider .div-num {
  font-size: 60pt;
  color: rgba(196,160,74,0.12);
  font-weight: 700;
  position: absolute;
  top: 1in;
}

.divider .div-label {
  font-size: 10pt;
  color: #C4A04A;
  letter-spacing: 3pt;
  text-transform: uppercase;
  margin-bottom: 10px;
  position: relative;
}

.divider .div-title {
  font-size: 24pt;
  color: #ffffff;
  font-weight: 700;
  line-height: 1.2;
  position: relative;
  padding: 0 0.6in;
}

.divider .div-sub {
  font-size: 11pt;
  color: #D4B896;
  font-style: italic;
  margin-top: 14px;
  position: relative;
}

/* ================ CONTENT PAGES ================ */
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 7.5pt;
  color: #999;
  padding-bottom: 4px;
  border-bottom: 1.5px solid #C4A04A;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #161616;
  text-transform: uppercase;
}
.section-header .sh-right { color: #aaa; }

.page-footer {
  position: absolute;
  bottom: 0.22in;
  left: 0.5in; right: 0.5in;
  font-size: 6.5pt;
  color: #bbb;
  display: flex;
  justify-content: space-between;
  border-top: 0.5px solid #eee;
  padding-top: 3px;
}

.page-title {
  font-size: 14pt;
  font-weight: 700;
  color: #161616;
  margin-bottom: 3px;
}

.page-subtitle {
  font-size: 8pt;
  color: #888;
  font-style: italic;
  margin-bottom: 12px;
}

.wline {
  border-bottom: 0.5px solid #ccc;
  height: 22px;
  margin-bottom: 2px;
}
.wline-sm {
  border-bottom: 0.5px solid #ddd;
  height: 18px;
  margin-bottom: 1px;
}

table.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
}
table.data-table th {
  background: #C4A04A;
  color: white;
  font-weight: 700;
  text-align: left;
  padding: 4px 5px;
  font-size: 7pt;
  letter-spacing: 0.3pt;
  text-transform: uppercase;
}
table.data-table td {
  padding: 4px 5px;
  border-bottom: 0.5px solid #ddd;
  vertical-align: top;
}
table.data-table tr:nth-child(even) td { background: #FAF6F0; }

.check-row {
  display: flex;
  flex-wrap: wrap;
  gap: 5px 10px;
  font-size: 8pt;
  color: #555;
  align-items: center;
}
.check-row .check-item {
  display: inline-flex;
  align-items: center;
  gap: 3px;
}
.check-box {
  width: 10px; height: 10px;
  border: 1px solid #888;
  border-radius: 2px;
  display: inline-block;
}

.info-box {
  background: #FAF6F0;
  border-left: 3px solid #C4A04A;
  padding: 8px 10px;
  margin-bottom: 10px;
  font-size: 8pt;
  color: #333;
  line-height: 1.5;
}
.info-box .info-title {
  font-weight: 700;
  color: #161616;
  font-size: 8.5pt;
  margin-bottom: 4px;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
}

.stat-card {
  text-align: center;
  padding: 6px 4px;
  background: #FAF6F0;
  border-radius: 4px;
  border: 1px solid #E8DCC8;
}
.stat-card .stat-label {
  font-size: 6.5pt;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 2px;
}
.stat-card .stat-value {
  font-size: 11pt;
  font-weight: 700;
  color: #161616;
}
"""

# ============================================================
# PAGE BUILDERS
# ============================================================

def cover_page():
    return f'''
<!-- Page {pn()}: Cover -->
<div class="cover">
  <div class="glow-bg"></div>
  <div class="icon-wrap">
    <svg viewBox="0 0 120 120" width="120" height="120" xmlns="http://www.w3.org/2000/svg">
      <!-- Dumbbell -->
      <!-- Left plates -->
      <rect x="14" y="40" width="10" height="42" rx="2" stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.1)"/>
      <rect x="8" y="44" width="8" height="34" rx="2" stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.15)"/>
      <!-- Right plates -->
      <rect x="96" y="40" width="10" height="42" rx="2" stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.1)"/>
      <rect x="104" y="44" width="8" height="34" rx="2" stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.15)"/>
      <!-- Bar -->
      <rect x="24" y="57" width="72" height="8" rx="2" stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.2)"/>
      <!-- Grip lines -->
      <line x1="40" y1="57" x2="40" y2="65" stroke="#C4A04A" stroke-width="0.6" opacity="0.4"/>
      <line x1="48" y1="57" x2="48" y2="65" stroke="#C4A04A" stroke-width="0.6" opacity="0.4"/>
      <line x1="56" y1="57" x2="56" y2="65" stroke="#C4A04A" stroke-width="0.6" opacity="0.4"/>
      <line x1="64" y1="57" x2="64" y2="65" stroke="#C4A04A" stroke-width="0.6" opacity="0.4"/>
      <line x1="72" y1="57" x2="72" y2="65" stroke="#C4A04A" stroke-width="0.6" opacity="0.4"/>
      <line x1="80" y1="57" x2="80" y2="65" stroke="#C4A04A" stroke-width="0.6" opacity="0.4"/>
      <!-- Energy arc -->
      <path d="M 30 25 Q 60 15 90 25" stroke="#C4A04A" stroke-width="1" fill="none" opacity="0.2" stroke-dasharray="3,3"/>
      <path d="M 35 95 Q 60 105 85 95" stroke="#C4A04A" stroke-width="0.8" fill="none" opacity="0.15" stroke-dasharray="3,3"/>
    </svg>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">100 Workouts</span>
      <span class="feature-badge">Body Tracker</span>
      <span class="feature-badge">Goal Setter</span>
      <span class="feature-badge">PR Tracker</span>
    </div>
    <div class="tagline">Train &middot; Track &middot; Transform</div>
  </div>
  <div class="publisher">More Shine Press</div>
</div>
'''


def owner_page():
    return f'''
<!-- Page {pn()}: Owner -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">This Book Belongs To</span>
    <span class="sh-right"></span>
  </div>

  <div style="height: 2.5in;"></div>

  <div style="text-align: center; margin-bottom: 30px;">
    <div style="font-size: 16pt; font-weight: 700; color: #161616; margin-bottom: 6px;">This Journal Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #161616; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Start Date</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Primary Goal</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Target Date</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Why I Train</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Fitness &amp; Workout Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def how_to_use():
    return f'''
<!-- Page {pn()}: How to Use -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Getting Started</span>
    <span class="sh-right">More Shine Press</span>
  </div>

  <div class="page-title">How to Use This Journal</div>
  <div class="page-subtitle">What gets measured gets improved</div>

  <div class="info-box">
    <div class="info-title">Why Track Your Workouts?</div>
    Research consistently shows that people who track their workouts make faster progress, stay motivated longer, and are more likely to reach their fitness goals. A workout log lets you see what works, identify plateaus, ensure progressive overload, and celebrate milestones along the way.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Keys to Progress</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Progressive overload.</strong> Each week, aim to lift slightly more weight, do one more rep, or complete one more set than last time. Small improvements compound into big results.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Track everything.</strong> Weight, reps, sets, rest times, and how you felt. The more data you have, the better you can optimize.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Review weekly.</strong> Look back at your last 4-8 workouts. Are you progressing? If not, change a variable &mdash; weight, reps, rest, or exercise selection.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Track body metrics.</strong> Weight, measurements, and photos tell the story the mirror can't. Check monthly for an honest assessment.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Set process goals.</strong> Focus on showing up and executing, not just outcomes. "Train 4 times this week" beats "lose 10 pounds."
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Pro Tip:</strong> Take progress photos in the same lighting, same pose, same time of day. Consistency in measurement is everything.
  </div>

  <div class="page-footer">
    <span>Fitness &amp; Workout Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def goal_setting():
    """Goal setting and planning page"""
    return f'''
<!-- Page {pn()}: Goals -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Goal Setting</span>
    <span class="sh-right">Plan Your Success</span>
  </div>

  <div class="page-title">Fitness Goals</div>
  <div class="page-subtitle">Define what success looks like for you</div>

  <!-- Goal categories -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Primary Goals (pick 1-3)</div>
  <div class="check-row" style="margin-bottom: 12px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Build Muscle</span>
    <span class="check-item"><span class="check-box"></span> Lose Fat</span>
    <span class="check-item"><span class="check-box"></span> Get Stronger</span>
    <span class="check-item"><span class="check-box"></span> Improve Endurance</span>
    <span class="check-item"><span class="check-box"></span> Increase Flexibility</span>
    <span class="check-item"><span class="check-box"></span> Run Faster/Farther</span>
    <span class="check-item"><span class="check-box"></span> General Health</span>
    <span class="check-item"><span class="check-box"></span> Sports Performance</span>
  </div>

  <!-- Specific goals -->
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Goal</th>
      <th style="width:50px;">Current</th>
      <th style="width:50px;">Target</th>
      <th style="width:50px;">Deadline</th>
      <th style="width:22px;">&#10003;</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">Body Weight</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Bench Press</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Squat</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Deadlift</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Run Distance</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Run Time</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Other</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <!-- Workout schedule -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 12px; margin-bottom: 4px;">Weekly Schedule Plan</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr><th>Day</th><th style="width:1.6in;">Focus</th><th>Notes</th></tr>
    <tr><td style="font-weight:700;color:#161616;">Monday</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Tuesday</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Wednesday</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Thursday</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Friday</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Saturday</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Sunday</td><td></td><td></td></tr>
  </table>

  <div class="page-footer">
    <span>Fitness &amp; Workout Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def body_tracker():
    """Body measurements tracker"""
    return f'''
<!-- Page {pn()}: Body Tracker -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Body Tracker</span>
    <span class="sh-right">Measurements</span>
  </div>

  <div class="page-title">Body Measurement Tracker</div>
  <div class="page-subtitle">Record monthly for honest progress</div>

  <!-- Starting stats -->
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-bottom:12px;">
    <div class="stat-card" style="padding:8px;"><div class="stat-label">Start Weight</div><div class="stat-value" style="font-size:14pt;"></div></div>
    <div class="stat-card" style="padding:8px;"><div class="stat-label">Goal Weight</div><div class="stat-value" style="font-size:14pt;"></div></div>
    <div class="stat-card" style="padding:8px;"><div class="stat-label">Height</div><div class="stat-value" style="font-size:14pt;"></div></div>
  </div>

  <!-- Measurement table -->
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th>Date</th>
      <th style="width:38px;">Weight</th>
      <th style="width:34px;">Chest</th>
      <th style="width:34px;">Waist</th>
      <th style="width:34px;">Hips</th>
      <th style="width:34px;">Arm</th>
      <th style="width:34px;">Thigh</th>
      <th style="width:30px;">BF%</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Month 1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Month 2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Month 3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Month 4</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Month 5</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Month 6</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Month 7</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Month 8</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Month 9</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Month 10</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Month 11</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Month 12</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">All measurements in lbs/inches or kg/cm. BF% = body fat percentage.</div>

  <div class="page-footer">
    <span>Fitness &amp; Workout Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def divider_section(num, title, subtitle):
    labels = ["One", "Two", "Three", "Four", "Five", "Six", "Seven"]
    label_text = labels[num-1] if num <= 7 else ""
    return f'''
<!-- Page {pn()}: Divider -->
<div class="divider">
  <div class="div-glow"></div>
  <div class="div-num">{num:02d}</div>
  <div class="div-label">Part {label_text}</div>
  <div class="div-title">{title}</div>
  <div class="div-sub">{subtitle}</div>
</div>
'''


def workout_page(entry_num):
    """Single-page workout log"""
    return f'''
<!-- Page {pn()}: Workout {entry_num} -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Workout #{entry_num:03d}</span>
    <span class="sh-right">Training Log</span>
  </div>

  <!-- Workout header -->
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:4px;margin-bottom:8px;">
    <div style="display:flex;align-items:baseline;gap:3px;">
      <span style="font-size:6.5pt;font-weight:700;color:#161616;text-transform:uppercase;">Date</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:3px;">
      <span style="font-size:6.5pt;font-weight:700;color:#161616;text-transform:uppercase;">Day</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:3px;">
      <span style="font-size:6.5pt;font-weight:700;color:#161616;text-transform:uppercase;">Focus</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:3px;">
      <span style="font-size:6.5pt;font-weight:700;color:#161616;text-transform:uppercase;">Duration</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
  </div>

  <!-- Focus type checkboxes -->
  <div class="check-row" style="margin-bottom: 8px; font-size: 7pt;">
    <span class="check-item"><span class="check-box"></span> Push</span>
    <span class="check-item"><span class="check-box"></span> Pull</span>
    <span class="check-item"><span class="check-box"></span> Legs</span>
    <span class="check-item"><span class="check-box"></span> Upper</span>
    <span class="check-item"><span class="check-box"></span> Lower</span>
    <span class="check-item"><span class="check-box"></span> Full Body</span>
    <span class="check-item"><span class="check-box"></span> Cardio</span>
    <span class="check-item"><span class="check-box"></span> Core</span>
  </div>

  <!-- Exercise table -->
  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:14px;">#</th>
      <th>Exercise</th>
      <th style="width:32px;">Set 1</th>
      <th style="width:32px;">Set 2</th>
      <th style="width:32px;">Set 3</th>
      <th style="width:32px;">Set 4</th>
      <th style="width:32px;">Set 5</th>
      <th style="width:30px;">Rest</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;text-align:center;">1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;text-align:center;">2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;text-align:center;">3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;text-align:center;">4</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;text-align:center;">5</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;text-align:center;">6</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;text-align:center;">7</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;text-align:center;">8</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>
  <div style="font-size: 5.5pt; color: #aaa; margin-top: 2px;">Format: weight x reps (e.g., 135x8, 145x6, 155x5)</div>

  <!-- Cardio -->
  <div style="font-size: 6.5pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.3pt; margin-top: 8px; margin-bottom: 3px;">Cardio / Warm-up / Cool-down</div>
  <table class="data-table" style="font-size: 7pt;">
    <tr><th>Type</th><th style="width:40px;">Duration</th><th style="width:35px;">Distance</th><th style="width:35px;">Intensity</th></tr>
    <tr><td></td><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td><td></td></tr>
  </table>

  <!-- Notes -->
  <div style="font-size: 6.5pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.3pt; margin-top: 8px; margin-bottom: 3px;">Notes / PRs / How I Felt</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Energy/Rating -->
  <div style="display:flex;justify-content:space-between;align-items:center;margin-top:6px;font-size:7pt;">
    <div>
      <span style="font-weight:700;color:#161616;text-transform:uppercase;font-size:6.5pt;">Energy:</span>
      <span style="margin-left:4px;">
        <span class="check-box" style="margin-right:1px;"></span> Low
        <span class="check-box" style="margin-left:4px;margin-right:1px;"></span> Medium
        <span class="check-box" style="margin-left:4px;margin-right:1px;"></span> High
      </span>
    </div>
    <div>
      <span style="font-weight:700;color:#161616;text-transform:uppercase;font-size:6.5pt;">Rating:</span>
      <span style="color:#ccc;letter-spacing:1pt;margin-left:4px;">&starf;&starf;&starf;&starf;&starf;</span>
    </div>
  </div>

  <div class="page-footer">
    <span>Workout #{entry_num:03d}</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def pr_tracker():
    """Personal records tracker"""
    lifts = [
        ("Bench Press", ""),
        ("Squat (Back)", ""),
        ("Deadlift", ""),
        ("Overhead Press", ""),
        ("Barbell Row", ""),
        ("Front Squat", ""),
        ("Romanian Deadlift", ""),
        ("Pull-up (Max Reps)", ""),
        ("Dip (Max Reps)", ""),
        ("Power Clean", ""),
        ("Push-up (Max Reps)", ""),
        ("Plank (Max Time)", ""),
    ]

    rows = ""
    for lift, _ in lifts:
        rows += f'''
      <tr><td style="font-weight:700;color:#161616;">{lift}</td><td></td><td></td><td></td><td></td></tr>'''

    return f'''
<!-- Page {pn()}: PR Tracker -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Personal Records</span>
    <span class="sh-right">Lift Your Best</span>
  </div>

  <div class="page-title">Personal Records (PRs)</div>
  <div class="page-subtitle">Celebrate every milestone</div>

  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Lift / Exercise</th>
      <th style="width:42px;">1RM</th>
      <th style="width:42px;">3RM</th>
      <th style="width:42px;">5RM</th>
      <th style="width:50px;">Date</th>
    </tr>
    {rows}
  </table>

  <div style="margin-top: 12px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">PR Highlights &amp; Milestones</div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
  </div>

  <div class="page-footer">
    <span>Fitness &amp; Workout Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def weekly_review():
    """Weekly progress review"""
    return f'''
<!-- Page {pn()}: Weekly Review -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Weekly Review</span>
    <span class="sh-right">Reflect &amp; Adjust</span>
  </div>

  <div class="page-title">Weekly Progress Review</div>
  <div class="page-subtitle">What worked, what didn't, what's next</div>

  <!-- Weekly stats -->
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:6px;margin-bottom:12px;">
    <div class="stat-card" style="padding:8px 4px;"><div class="stat-label">Workouts</div><div class="stat-value" style="font-size:14pt;"></div></div>
    <div class="stat-card" style="padding:8px 4px;"><div class="stat-label">Total Time</div><div class="stat-value" style="font-size:14pt;"></div></div>
    <div class="stat-card" style="padding:8px 4px;"><div class="stat-label">Weight Lifted</div><div class="stat-value" style="font-size:14pt;"></div></div>
    <div class="stat-card" style="padding:8px 4px;"><div class="stat-label">Avg Energy</div><div class="stat-value" style="font-size:14pt;"></div></div>
  </div>

  <!-- Review questions -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Week Starting</div>
  <div class="wline-sm" style="margin-bottom:10px;"></div>

  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th style="width:50px;">Day</th>
      <th>Trained?</th>
      <th>Focus</th>
      <th style="width:28px;">Rating</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Mon</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Tue</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Wed</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Thu</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Fri</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Sat</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">Sun</td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 4px;">What Went Well</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">What to Improve Next Week</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Goal for Next Week</div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Fitness &amp; Workout Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def notes_page(page_num):
    lines = ""
    for _ in range(18):
        lines += '<div class="wline"></div>\n'

    return f'''
<!-- Page {pn()}: Notes -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Notes</span>
    <span class="sh-right"></span>
  </div>

  <div class="page-title">Training Notes</div>
  <div class="page-subtitle">Programs, exercises, and ideas</div>

  {lines}

  <div class="page-footer">
    <span>Fitness &amp; Workout Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


# ============================================================
# MAIN
# ============================================================
def main():
    pages = []

    # ---- Front Matter ----
    pages.append(cover_page())                          # 1
    pages.append(owner_page())                           # 2
    pages.append(how_to_use())                           # 3
    pages.append(goal_setting())                         # 4
    pages.append(body_tracker())                         # 5

    # ---- Section 1: Workout Logs ----
    pages.append(divider_section(1, "Workout Logs", "100 workouts &mdash; every rep, every set"))
    NUM_WORKOUTS = 100
    for i in range(1, NUM_WORKOUTS + 1):
        pages.append(workout_page(i))

    # ---- Section 2: Personal Records ----
    pages.append(divider_section(2, "Personal Records", "Track your best lifts and celebrate milestones"))
    pages.append(pr_tracker())

    # ---- Section 3: Weekly Reviews ----
    pages.append(divider_section(3, "Weekly Reviews", "Reflect, adjust, and stay on track"))
    for i in range(4):
        pages.append(weekly_review())

    # ---- Section 4: Notes ----
    pages.append(divider_section(4, "Notes", "Programs, exercises, and ideas"))
    for i in range(4):
        pages.append(notes_page(i + 1))

    # Assemble HTML
    body_content = "\n".join(pages)
    total_pages = page_no[0]

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{BOOK_TITLE} &mdash; More Shine Press</title>
<style>{CSS}</style>
</head>
<body>
{body_content}
</body>
</html>'''

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Generated: {HTML_FILE}")
    print(f"Total pages: {total_pages}")

    print(f"\nPage breakdown:")
    print(f"  Cover: 1")
    print(f"  Owner page: 1")
    print(f"  How to use: 1")
    print(f"  Goal setting: 1")
    print(f"  Body tracker: 1")
    print(f"  Section dividers: 4")
    print(f"  Workout logs ({NUM_WORKOUTS}): {NUM_WORKOUTS}")
    print(f"  PR tracker: 1")
    print(f"  Weekly reviews: 4")
    print(f"  Notes pages: 4")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
