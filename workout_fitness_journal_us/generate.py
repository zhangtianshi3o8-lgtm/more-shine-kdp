#!/usr/bin/env python3
"""
Workout & Fitness Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Gym-goers, fitness enthusiasts, weightlifters
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "workout_fitness_journal_us_V1.0.html")

BOOK_TITLE = "Workout & Fitness Journal"
BOOK_SUBTITLE = "Track Every Rep, Every Set, Every Gain"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

def nl(n):
    return "\n".join('<div class="notes-line"></div>' for _ in range(n))

# ============================================================
# CSS
# ============================================================
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
@media print  { .page { border: none; margin: 0; } }

/* ================ INTERIOR TITLE PAGE ================ */
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
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C0392B, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C0392B, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #C0392B, transparent);
}

.cover .title-main {
  font-size: 28pt;
  font-weight: 700;
  color: #FAF6F0;
  line-height: 1.2;
  letter-spacing: 0.5pt;
  position: relative;
  z-index: 2;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 100px;
  height: 2px;
  background: #C0392B;
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
  color: #C0392B;
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
  background: #C0392B;
  margin: 0 12px;
  opacity: 0.4;
}

/* ================ HOW TO USE ================ */
.howto-text {
  font-size: 10pt;
  line-height: 1.7;
  color: #2A2A2A;
}

.howto-text p {
  margin-bottom: 8px;
}

.howto-text .ht-title {
  font-size: 11pt;
  font-weight: 700;
  color: #161616;
  margin-bottom: 4px;
  margin-top: 6px;
}

.howto-text .ht-icon {
  color: #C0392B;
  font-weight: 700;
  margin-right: 4px;
}

/* ================ GOAL BOXES ================ */
.goal-box {
  border: 1px solid #C0392B;
  border-radius: 4px;
  padding: 10px 12px;
  margin-bottom: 10px;
}

.goal-box .g-label {
  font-size: 8pt;
  color: #C0392B;
  text-transform: uppercase;
  letter-spacing: 1pt;
  font-weight: 700;
  margin-bottom: 4px;
}

.goal-line {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
}

.goal-checkbox {
  width: 12px;
  height: 12px;
  border: 1.5px solid #C0392B;
  border-radius: 2px;
  flex-shrink: 0;
}

.goal-write {
  flex: 1;
  border-bottom: 1px dotted #ccc;
  height: 14px;
}

/* ================ MEASUREMENT TABLE ================ */
.meas-table {
  width: 100%;
  border-collapse: collapse;
}

.meas-table th {
  font-size: 7.5pt;
  color: #C0392B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 5px 4px;
  border-bottom: 1.5px solid #C0392B;
  text-align: center;
}

.meas-table th:first-child {
  text-align: left;
  width: 90px;
}

.meas-table td {
  padding: 5px 4px;
  border-bottom: 1px solid #eee;
  text-align: center;
  height: 22px;
  font-size: 9pt;
}

.meas-table td:first-child {
  text-align: left;
  font-weight: 600;
  font-size: 9pt;
}

/* ================ WORKOUT LOG ================ */
.workout-banner {
  display: flex;
  align-items: center;
  gap: 6px;
  border-bottom: 1.5px solid #C0392B;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.workout-banner .wb-label {
  font-size: 8pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.workout-banner .wb-line {
  flex: 1;
  height: 12px;
  border-bottom: 1px dotted #ccc;
}

.workout-banner .wb-num {
  display: inline-block;
  border: 1.5px solid #C0392B;
  border-radius: 4px;
  padding: 2px 8px;
  font-size: 7.5pt;
  color: #C0392B;
  font-weight: 700;
  text-transform: uppercase;
}

.type-row {
  display: flex;
  gap: 6px;
  margin-bottom: 8px;
  flex-wrap: wrap;
}

.type-check {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 7.5pt;
  color: #555;
}

.type-box {
  width: 10px;
  height: 10px;
  border: 1.5px solid #C0392B;
  border-radius: 2px;
}

/* Exercise table */
.ex-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 4px;
}

.ex-table th {
  font-size: 6.5pt;
  color: #C0392B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 4px 2px;
  border-bottom: 1.5px solid #C0392B;
  text-align: center;
}

.ex-table th:first-child {
  text-align: left;
  width: 1.5in;
}

.ex-table td {
  padding: 4px 2px;
  border-bottom: 1px solid #eee;
  height: 26px;
}

.ex-table td:first-child {
  border-bottom: 1px solid #ddd;
}

.ex-table .ex-name {
  border: none;
  border-bottom: 1px dotted #ddd;
  height: 14px;
  font-size: 9pt;
}

.ex-table .ex-num {
  text-align: center;
  border: none;
  border-bottom: 1px dotted #eee;
  height: 14px;
}

/* Cardio and feeling section */
.cardio-box {
  border: 1px solid #C0392B;
  border-radius: 4px;
  padding: 8px 10px;
  margin-top: 8px;
  background: #FAF6F0;
}

.cardio-box .cb-label {
  font-size: 7pt;
  color: #C0392B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 4px;
}

.cardio-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 8px;
}

.cardio-field .cf-label {
  font-size: 6pt;
  color: #aaa;
  text-transform: uppercase;
  display: block;
  margin-bottom: 1px;
}

.cardio-field .cf-write {
  height: 14px;
  border-bottom: 1px dotted #ccc;
}

.feel-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 5px;
}

.feel-label {
  font-size: 8pt;
  color: #2A2A2A;
  width: 70px;
  flex-shrink: 0;
}

.feel-dots {
  display: flex;
  gap: 4px;
}

.feel-dot {
  width: 12px;
  height: 12px;
  border: 1.5px solid #C0392B;
  border-radius: 50%;
}

.feel-dots .feel-num {
  font-size: 6pt;
  color: #C0392B;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 12px;
}

.pr-box {
  border-left: 3px solid #C0392B;
  padding: 6px 10px;
  margin-top: 8px;
  background: #FAF6F0;
}

.pr-box .pr-label {
  font-size: 7pt;
  color: #C0392B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 2px;
}

.pr-box .pr-write {
  height: 18px;
  border-bottom: 1px dotted #ccc;
  margin-bottom: 4px;
}

/* Weekly summary */
.weekly-lines {
  border-bottom: 1px solid #ddd;
  height: 22px;
}

/* PR Tracker */
.pr-table {
  width: 100%;
  border-collapse: collapse;
}

.pr-table th {
  font-size: 7pt;
  color: #C0392B;
  text-transform: uppercase;
  padding: 5px 4px;
  border-bottom: 1.5px solid #C0392B;
  text-align: center;
}

.pr-table th:first-child {
  text-align: left;
}

.pr-table td {
  padding: 6px 4px;
  border-bottom: 1px solid #eee;
  height: 26px;
}

/* Glossary */
.glossary-item {
  margin-bottom: 6px;
}

.glossary-term {
  font-weight: 700;
  color: #C0392B;
  font-size: 9pt;
}

.glossary-def {
  font-size: 9pt;
  color: #2A2A2A;
  margin-left: 12px;
}

/* Notes */
.notes-line {
  border-bottom: 1px solid #ddd;
  height: 22px;
}

/* Final page */
.final-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100%;
}

.final-page .fp-text {
  font-size: 12pt;
  color: #999;
  font-style: italic;
  line-height: 1.8;
  margin-bottom: 20px;
}

.final-page .fp-logo {
  font-size: 11pt;
  color: #C4A04A;
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  font-weight: 700;
}

.final-page .fp-line {
  width: 60px;
  height: 1.5px;
  background: #C0392B;
  margin: 12px auto;
  opacity: 0.5;
}
"""

# ============================================================
# PAGE GENERATORS
# ============================================================

def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 120 100" width="120" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- Barbell -->
      <!-- Left plate -->
      <rect x="6" y="35" width="12" height="30" rx="2" stroke="#C0392B" stroke-width="1.5" fill="none"/>
      <!-- Left inner plate -->
      <rect x="20" y="40" width="8" height="20" rx="1" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.7"/>
      <!-- Bar -->
      <line x1="6" y1="50" x2="114" y2="50" stroke="#C4A04A" stroke-width="2"/>
      <!-- Right inner plate -->
      <rect x="92" y="40" width="8" height="20" rx="1" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.7"/>
      <!-- Right plate -->
      <rect x="102" y="35" width="12" height="30" rx="2" stroke="#C0392B" stroke-width="1.5" fill="none"/>
      <!-- Collars -->
      <rect x="28" y="46" width="3" height="8" stroke="#C4A04A" stroke-width="1" fill="none"/>
      <rect x="89" y="46" width="3" height="8" stroke="#C4A04A" stroke-width="1" fill="none"/>
    </svg>
  </div>

  <div class="title-main">Workout &amp; Fitness<br>Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Track Every Rep, Every Set, Every Gain</div>

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
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Training Log</div>
    <p>This journal is your training partner. Every workout matters &mdash;
    whether you are chasing a new personal record or just staying active.
    Write it down, track your progress, and watch yourself get stronger.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Workout Log</div>
    <p>Each workout uses a <strong>two-page spread</strong>. The left page captures
    your workout type, exercises, sets, reps, weights, and RPE (how hard
    each set felt on a 1-10 scale). The right page tracks cardio, how you
    felt, personal records, and your focus for next time.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Progress Tracking</div>
    <p>Use the <strong>body measurement tracker</strong> and <strong>one-rep max log</strong>
    at the front to record your starting point. Every few weeks, retake
    measurements to see your progress. The <strong>weekly summaries</strong> help
    you spot trends in your training and recovery.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips</div>
    <p>&#9679; Record your workouts immediately after finishing &mdash; do not rely on memory.</p>
    <p>&#9679; Use RPE honestly. A 10 means you could not have done another rep.</p>
    <p>&#9679; Track accessories too, not just main lifts. It all adds up.</p>
    <p>&#9679; When you hit a PR, circle it and celebrate.</p>
  </div>
</div>""" % (pg, pg)


def goal_setting_page():
    pg = pn()
    goals = [
        ("Short-Term Goals (1-3 months)", 4),
        ("Long-Term Goals (6-12 months)", 3),
        ("Target Body Weight", 1),
        ("Target Bench / Squat / Deadlift", 2),
    ]
    boxes = ""
    for label, count in goals:
        lines = "\n".join(
            '<div class="goal-line"><div class="goal-checkbox"></div>'
            '<div class="goal-write"></div></div>'
            for _ in range(count)
        )
        boxes += """<div class="goal-box">
    <div class="g-label">%s</div>
    %s
  </div>
""" % (H.escape(label), lines)

    return """<!-- PAGE %d: Goal Setting -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">My Fitness Goals</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Goal Setting</div>
    <div class="section-line"></div>
  </div>

  %s
</div>""" % (pg, pg, boxes)


def body_measurement_page():
    pg = pn()
    measurements = [
        "Body Weight", "Body Fat %", "Chest", "Waist", "Hips",
        "Right Arm", "Left Arm", "Right Thigh", "Left Thigh", "Right Calf", "Left Calf",
    ]
    rows = ""
    for m in measurements:
        rows += """<tr>
    <td>%s</td>
    <td></td><td></td><td></td><td></td>
  </tr>
""" % H.escape(m)

    return """<!-- PAGE %d: Body Measurements -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Body Measurements</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Measurement Tracker</div>
    <div class="section-line"></div>
  </div>

  <table class="meas-table">
    <thead>
      <tr>
        <th>Measurement</th>
        <th>Start</th>
        <th>Month 1</th>
        <th>Month 2</th>
        <th>Month 3</th>
      </tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>

  <div class="pr-box" style="margin-top: 14px;">
    <div class="pr-label">Progress Photo Dates</div>
    <div class="pr-write"></div>
    <div class="pr-write"></div>
  </div>
</div>""" % (pg, pg, rows)


def one_rep_max_page():
    pg = pn()
    lifts = ["Bench Press", "Squat", "Deadlift", "Overhead Press", "Barbell Row", "Power Clean"]
    rows = ""
    for lift in lifts:
        rows += """<tr>
    <td>%s</td>
    <td></td><td></td><td></td><td></td>
  </tr>
""" % H.escape(lift)

    return """<!-- PAGE %d: One Rep Max Tracker -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">One Rep Max Tracker</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">1RM Progress</div>
    <div class="section-line"></div>
  </div>

  <table class="meas-table">
    <thead>
      <tr>
        <th>Lift</th>
        <th>Start</th>
        <th>Current</th>
        <th>Goal</th>
        <th>Date</th>
      </tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>

  <div class="pr-box" style="margin-top: 14px;">
    <div class="pr-label">Notes on Form &amp; Technique</div>
    <div class="pr-write"></div>
    <div class="pr-write"></div>
    <div class="pr-write"></div>
  </div>
</div>""" % (pg, pg, rows)


def workout_log_left(session_num):
    """Left page of a workout log spread."""
    pg = pn()
    types = ["Push", "Pull", "Legs", "Upper", "Lower", "Full Body", "Cardio", "Sports"]
    type_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % t
        for t in types
    )
    # 6 exercise rows
    ex_rows = ""
    for _ in range(6):
        ex_rows += """<tr>
    <td><input class="ex-name" disabled></td>
    <td><input class="ex-num" disabled></td>
    <td><input class="ex-num" disabled></td>
    <td><input class="ex-num" disabled></td>
    <td><input class="ex-num" disabled></td>
    <td><input class="ex-num" disabled></td>
  </tr>
"""

    return """<!-- PAGE %d: Workout Left -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Workout Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="workout-banner">
    <span class="wb-num">Session #%03d</span>
    <span class="wb-label">Date:</span>
    <div class="wb-line"></div>
    <span class="wb-label">Duration:</span>
    <div class="wb-line" style="max-width: 0.8in;"></div>
  </div>

  <div class="type-row">%s</div>

  <table class="ex-table">
    <thead>
      <tr>
        <th>Exercise</th>
        <th>Set 1</th>
        <th>Set 2</th>
        <th>Set 3</th>
        <th>Set 4</th>
        <th>RPE</th>
      </tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>

  <div style="font-size: 7pt; color: #aaa; margin-top: 4px; font-style: italic;">
    Record weight (lbs) x reps in each set box. RPE: 1-10 scale (10 = could not do another rep).
  </div>

  <div class="pr-box" style="margin-top: 8px;">
    <div class="pr-label">Warm-Up Notes</div>
    <div class="pr-write"></div>
  </div>
</div>""" % (pg, pg, session_num, type_html, ex_rows)


def workout_log_right():
    """Right page of a workout log spread."""
    pg = pn()
    return """<!-- PAGE %d: Workout Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Cardio &amp; Recovery</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="cardio-box">
    <div class="cb-label">Cardio / Conditioning</div>
    <div class="cardio-row">
      <div class="cardio-field"><span class="cf-label">Type</span><div class="cf-write"></div></div>
      <div class="cardio-field"><span class="cf-label">Duration</span><div class="cf-write"></div></div>
      <div class="cardio-field"><span class="cf-label">Distance</span><div class="cf-write"></div></div>
      <div class="cardio-field"><span class="cf-label">Avg HR</span><div class="cf-write"></div></div>
    </div>
  </div>

  <div class="cardio-box" style="border-color: #C4A04A; margin-top: 8px;">
    <div class="cb-label" style="color: #C4A04A;">How Did You Feel?</div>
    <div class="feel-row">
      <div class="feel-label">Energy</div>
      <div class="feel-dots">
        <span class="feel-num">1</span><div class="feel-dot"></div>
        <span class="feel-num">2</span><div class="feel-dot"></div>
        <span class="feel-num">3</span><div class="feel-dot"></div>
        <span class="feel-num">4</span><div class="feel-dot"></div>
        <span class="feel-num">5</span><div class="feel-dot"></div>
        <span class="feel-num">6</span><div class="feel-dot"></div>
        <span class="feel-num">7</span><div class="feel-dot"></div>
        <span class="feel-num">8</span><div class="feel-dot"></div>
        <span class="feel-num">9</span><div class="feel-dot"></div>
        <span class="feel-num">10</span><div class="feel-dot"></div>
      </div>
    </div>
    <div class="feel-row">
      <div class="feel-label">Strength</div>
      <div class="feel-dots">
        <span class="feel-num">1</span><div class="feel-dot"></div>
        <span class="feel-num">2</span><div class="feel-dot"></div>
        <span class="feel-num">3</span><div class="feel-dot"></div>
        <span class="feel-num">4</span><div class="feel-dot"></div>
        <span class="feel-num">5</span><div class="feel-dot"></div>
        <span class="feel-num">6</span><div class="feel-dot"></div>
        <span class="feel-num">7</span><div class="feel-dot"></div>
        <span class="feel-num">8</span><div class="feel-dot"></div>
        <span class="feel-num">9</span><div class="feel-dot"></div>
        <span class="feel-num">10</span><div class="feel-dot"></div>
      </div>
    </div>
    <div class="feel-row">
      <div class="feel-label">Motivation</div>
      <div class="feel-dots">
        <span class="feel-num">1</span><div class="feel-dot"></div>
        <span class="feel-num">2</span><div class="feel-dot"></div>
        <span class="feel-num">3</span><div class="feel-dot"></div>
        <span class="feel-num">4</span><div class="feel-dot"></div>
        <span class="feel-num">5</span><div class="feel-dot"></div>
        <span class="feel-num">6</span><div class="feel-dot"></div>
        <span class="feel-num">7</span><div class="feel-dot"></div>
        <span class="feel-num">8</span><div class="feel-dot"></div>
        <span class="feel-num">9</span><div class="feel-dot"></div>
        <span class="feel-num">10</span><div class="feel-dot"></div>
      </div>
    </div>
  </div>

  <div class="pr-box" style="margin-top: 8px;">
    <div class="pr-label">Personal Records Today</div>
    <div class="pr-write"></div>
    <div class="pr-write"></div>
  </div>

  <div class="pr-box" style="border-color: #7A8B6F; margin-top: 8px;">
    <div class="pr-label" style="color: #7A8B6F;">Next Session Focus</div>
    <div class="pr-write"></div>
    <div class="pr-write"></div>
  </div>
</div>""" % (pg, pg)


def weekly_summary_page(week_num):
    pg = pn()
    return """<!-- PAGE %d: Weekly Summary -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Weekly Progress Summary</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Week %d Review</div>
    <div class="section-line"></div>
  </div>

  <table class="meas-table">
    <thead>
      <tr>
        <th>Metric</th>
        <th>Start of Week</th>
        <th>End of Week</th>
        <th>Change</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Body Weight</td><td></td><td></td><td></td></tr>
      <tr><td>Body Fat %%</td><td></td><td></td><td></td></tr>
      <tr><td>Waist</td><td></td><td></td><td></td></tr>
      <tr><td>Workouts Done</td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="pr-box" style="margin-top: 10px;">
    <div class="pr-label">Biggest Win This Week</div>
    <div class="pr-write"></div>
    <div class="pr-write"></div>
  </div>

  <div class="pr-box" style="border-color: #7A8B6F; margin-top: 8px;">
    <div class="pr-label" style="color: #7A8B6F;">Challenges &amp; Lessons</div>
    <div class="pr-write"></div>
    <div class="pr-write"></div>
  </div>

  <div class="pr-box" style="border-color: #C4A04A; margin-top: 8px;">
    <div class="pr-label" style="color: #C4A04A;">Goal for Next Week</div>
    <div class="pr-write"></div>
    <div class="pr-write"></div>
  </div>
</div>""" % (pg, pg, week_num)


def pr_tracker_page():
    pg = pn()
    rows = ""
    for _ in range(14):
        rows += """<tr>
    <td></td><td></td><td></td><td></td><td></td>
  </tr>
"""
    return """<!-- PAGE %d: PR Tracker -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Personal Records Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">PR History</div>
    <div class="section-line"></div>
  </div>

  <table class="pr-table">
    <thead>
      <tr>
        <th>Date</th>
        <th>Lift / Exercise</th>
        <th>Weight</th>
        <th>Reps</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>
</div>""" % (pg, pg, rows)


def exercise_reference_page():
    pg = pn()
    groups = [
        ("Chest", ["Bench Press", "Incline Press", "Dumbbell Press", "Push-ups", "Chest Fly", "Cable Crossover"]),
        ("Back", ["Deadlift", "Pull-ups", "Barbell Row", "Lat Pulldown", "Seated Cable Row", "Face Pull"]),
        ("Shoulders", ["Overhead Press", "Lateral Raise", "Front Raise", "Rear Delt Fly", "Arnold Press", "Shrug"]),
        ("Legs", ["Squat", "Front Squat", "Leg Press", "Lunge", "Leg Curl", "Calf Raise"]),
        ("Arms", ["Barbell Curl", "Hammer Curl", "Tricep Pushdown", "Skull Crusher", "Preacher Curl", "Dip"]),
        ("Core", ["Plank", "Hanging Leg Raise", "Cable Crunch", "Russian Twist", "Dead Bug", "Pallof Press"]),
    ]
    left = ""
    right = ""
    for i, (group, exercises) in enumerate(groups):
        ex_html = ", ".join(H.escape(e) for e in exercises)
        section = """<div class="goal-box">
  <div class="g-label">%s</div>
  <div style="font-size: 9pt; color: #2A2A2A; line-height: 1.6;">%s</div>
</div>
""" % (H.escape(group), ex_html)
        if i < 3:
            left += section
        else:
            right += section

    return """<!-- PAGE %d: Exercise Reference -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Exercise Reference</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Common Exercises by Muscle Group</div>
    <div class="section-line"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    %s
    %s
  </div>
</div>""" % (pg, pg, left, right)


def glossary_page():
    pg = pn()
    terms = [
        ("RPE", "Rate of Perceived Exertion. A 1-10 scale of how hard a set felt. RPE 10 means you could not complete another rep."),
        ("1RM", "One Rep Max. The maximum weight you can lift for a single repetition with proper form."),
        ("AMRAP", "As Many Reps As Possible. Do as many repetitions as you can in a given time or until form breaks."),
        ("DOMS", "Delayed Onset Muscle Soreness. Muscle soreness that appears 24-72 hours after intense exercise."),
        ("Hypertrophy", "Muscle growth. Training for size typically uses moderate weight and 8-15 rep ranges."),
        ("Compound Lift", "An exercise that works multiple muscle groups and joints at once (squat, deadlift, bench press)."),
        ("Isolation Lift", "An exercise that targets a single muscle group (bicep curl, tricep extension)."),
        ("Superset", "Two exercises performed back-to-back with no rest between them."),
        ("Drop Set", "Continuing an exercise with lighter weight immediately after reaching failure at a heavier weight."),
        ("Progressive Overload", "Gradually increasing weight, reps, or intensity over time to keep making gains."),
        ("Deload", "A planned period of reduced training volume or intensity to allow recovery."),
        ("Volume", "Total amount of work done, calculated as sets x reps x weight."),
    ]
    items = ""
    for term, definition in terms:
        items += """<div class="glossary-item">
    <span class="glossary-term">%s</span>
    <span class="glossary-def">%s</span>
  </div>
""" % (H.escape(term), H.escape(definition))

    return """<!-- PAGE %d: Glossary -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Fitness Glossary</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Key Terms</div>
    <div class="section-line"></div>
  </div>

  %s
</div>""" % (pg, pg, items)


def year_review_page():
    pg = pn()
    return """<!-- PAGE %d: Year in Review -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Year in Review</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">My Fitness Year</div>
    <div class="section-line"></div>
  </div>

  <table class="meas-table">
    <thead>
      <tr>
        <th>Metric</th>
        <th>Start of Year</th>
        <th>End of Year</th>
        <th>Change</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Body Weight</td><td></td><td></td><td></td></tr>
      <tr><td>Body Fat %%</td><td></td><td></td><td></td></tr>
      <tr><td>Bench Press 1RM</td><td></td><td></td><td></td></tr>
      <tr><td>Squat 1RM</td><td></td><td></td><td></td></tr>
      <tr><td>Deadlift 1RM</td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="pr-box" style="margin-top: 10px;">
    <div class="pr-label">Total Workouts This Year</div>
    <div class="pr-write"></div>
  </div>

  <div class="pr-box" style="border-color: #C4A04A; margin-top: 8px;">
    <div class="pr-label" style="color: #C4A04A;">Biggest Achievement</div>
    <div class="pr-write"></div>
    <div class="pr-write"></div>
  </div>

  <div class="pr-box" style="border-color: #7A8B6F; margin-top: 8px;">
    <div class="pr-label" style="color: #7A8B6F;">Goals for Next Year</div>
    <div class="pr-write"></div>
    <div class="pr-write"></div>
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
      Strength is built one<br>
      workout at a time.<br>
      Keep showing up.
    </div>
    <div class="fp-line"></div>
    <div class="fp-logo">More Shine Press</div>
    <div class="fp-line"></div>
  </div>
</div>""" % pg


# ============================================================
# MAIN
# ============================================================
def generate(output_path=HTML_FILE):
    pages = []

    # 1. Title
    pages.append(interior_title_page())

    # 2. How to use
    pages.append(how_to_use_page())

    # 3. Goals
    pages.append(goal_setting_page())

    # 4. Body measurements
    pages.append(body_measurement_page())

    # 5. 1RM tracker
    pages.append(one_rep_max_page())

    # 6-85. 40 workout log spreads (2 pages each = 80 pages)
    session = 1
    for i in range(40):
        pages.append(workout_log_left(session))
        pages.append(workout_log_right())
        session += 1

        # Every 4th workout, insert a weekly summary
        if (i + 1) % 4 == 0:
            week_num = (i + 1) // 4
            pages.append(weekly_summary_page(week_num))

    # 86-87. PR tracker (2 pages)
    pages.append(pr_tracker_page())
    pages.append(pr_tracker_page())

    # 88. Exercise reference
    pages.append(exercise_reference_page())

    # 89. Glossary
    pages.append(glossary_page())

    # 90. Year in review
    pages.append(year_review_page())

    # 91-93. Notes (3 pages)
    for _ in range(3):
        pages.append(notes_page())

    # 94. Final
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
