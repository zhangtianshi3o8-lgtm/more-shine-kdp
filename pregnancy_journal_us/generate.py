#!/usr/bin/env python3
"""
Pregnancy Journal -- KDP Interior Generator
Trim: 8 x 10 in | Language: English
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "pregnancy_journal_us_V1.0.html")

BOOK_TITLE = "Pregnancy Journal"
BOOK_SUBTITLE = "A 40-Week Guided Journal for Moms to Be"

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
  font-size: 34pt;
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

/* ================ TRIMESTER DIVIDER ================ */
.tri-divider {
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  text-align: center; height: 100%;
}
.tri-divider .td-num {
  font-size: 60pt; color: #B8860B; font-weight: 700;
  opacity: 0.15; line-height: 1;
}
.tri-divider .td-title {
  font-size: 22pt; color: #161616; font-weight: 700;
  letter-spacing: 1pt; text-transform: uppercase;
  margin-top: 10px;
}
.tri-divider .td-weeks {
  font-size: 11pt; color: #B8860B; font-style: italic;
  margin-top: 6px;
}
.tri-divider .td-line {
  width: 80px; height: 2px; background: #B8860B;
  margin: 16px auto; opacity: 0.5;
}

/* ================ WEEKLY PAGE ================ */
.week-banner {
  display: flex;
  align-items: center;
  gap: 10px;
  border-bottom: 1.5px solid #B8860B;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.week-banner .wb-week {
  display: inline-block;
  border: 1.5px solid #B8860B;
  border-radius: 4px;
  padding: 3px 12px;
  font-size: 9pt;
  color: #B8860B;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.week-banner .wb-sub {
  font-size: 8pt;
  color: #999;
}

/* ================ SYMPTOM CHECKBOXES ================ */
.symptom-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 4px 10px;
  margin-bottom: 8px;
}

.symptom-check {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 7.5pt;
  color: #555;
}

.symptom-box {
  width: 10px; height: 10px;
  border: 1.5px solid #B8860B;
  border-radius: 2px;
  flex-shrink: 0;
}

/* ================ MOOD DOTS ================ */
.mood-row {
  display: flex;
  gap: 8px;
  align-items: center;
  margin-bottom: 8px;
}

.mood-label {
  font-size: 7pt;
  color: #B8860B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  width: 0.6in;
  flex-shrink: 0;
}

.mood-dots {
  display: flex;
  gap: 4px;
}

.mood-dot {
  width: 12px; height: 12px;
  border: 1.5px solid #B8860B;
  border-radius: 50%;
}

/* ================ BUMP FRAME ================ */
.bump-frame {
  border: 1.5px solid #C4A04A;
  border-radius: 4px;
  width: 2in; height: 2.4in;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

.bump-frame .bf-text {
  font-size: 7pt;
  color: #ccc;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
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

.data-table td {
  padding: 4px 3px;
  border-bottom: 1px solid #eee;
  height: 24px;
  font-size: 9pt;
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
      <!-- Mother and baby bump silhouette -->
      <g transform="translate(50,50)">
        <!-- Heart outline -->
        <path d="M 0,20 C -20,5 -28,-5 -28,-14 C -28,-24 -20,-28 -12,-24 C -6,-21 -2,-16 0,-12 C 2,-16 6,-21 12,-24 C 20,-28 28,-24 28,-14 C 28,-5 20,5 0,20 Z"
              stroke="#B8860B" stroke-width="2" fill="none"/>
        <!-- Inner heart highlight -->
        <path d="M -16,-18 C -18,-14 -14,-10 -10,-10" stroke="#C4A04A" stroke-width="1" fill="none"/>
        <path d="M 16,-18 C 18,-14 14,-10 10,-10" stroke="#C4A04A" stroke-width="1" fill="none"/>
        <!-- Small dot sparkle -->
        <circle cx="0" cy="-8" r="1.5" fill="#D4B896"/>
      </g>
    </svg>
  </div>

  <div class="title-main">Pregnancy<br>Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">A 40-Week Guided Journal<br>for Moms to Be</div>

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
    <div class="ht-title"><span class="ht-icon">&#10058;</span> Your Pregnancy Companion</div>
    <p>This journal is designed to be your companion through one of
    life's most extraordinary journeys. From the first positive test
    to the first cry in the delivery room, every week brings new
    changes, new emotions, and new memories worth preserving.</p>

    <div class="ht-title"><span class="ht-icon">&#10058;</span> The Weekly Pages</div>
    <p>Each week from week 4 to week 40 has its own <strong>tracking
    page</strong>. Record your symptoms, mood, cravings, weight,
    appointments, and thoughts. There is space for a bump photo
    reference and notes about how you are feeling. Weeks are grouped
    into three trimesters, each with its own divider and reflection
    page.</p>

    <div class="ht-title"><span class="ht-icon">&#10058;</span> Milestone Pages</div>
    <p>Beyond the weekly tracking, you will find dedicated pages for:</p>
    <p>&#9679; <strong>Pregnancy Overview</strong> -- due date, doctor,
    hospital, support team.</p>
    <p>&#9679; <strong>Prenatal Appointments</strong> -- log every visit,
    question, and result.</p>
    <p>&#9679; <strong>Ultrasound Gallery</strong> -- preserve each
    sonogram with date and notes.</p>
    <p>&#9679; <strong>Baby Names</strong> -- brainstorm and narrow down
    your favorites.</p>
    <p>&#9679; <strong>Nursery Planning</strong> -- plan the perfect
    space for your little one.</p>
    <p>&#9679; <strong>Hospital Bag Checklist</strong> -- everything you
    need for the big day.</p>
    <p>&#9679; <strong>Birth Plan &amp; Birth Day</strong> -- your
    preferences and the first details.</p>
  </div>
</div>""" % (pg, pg)


def overview_page():
    pg = pn()
    return """<!-- PAGE %d: Pregnancy Overview -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Our Pregnancy Journey</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">The Beginning</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Mother's Name</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Partner's Name</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Due Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Conception Date</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Positive Test Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">First Appointment</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">OB / Midwife</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Hospital / Birth Center</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Support Person</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Doula</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">How I Felt When I Found Out</div>
    <div class="wb-area" style="height: 50px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Our Announcement Plan</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Starting Weight</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Pre-Pregnancy BMI</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Target Gain (lbs)</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Hopes &amp; Dreams for This Baby</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>
</div>""" % (pg, pg)


def trimester_divider(tri_num, weeks_label):
    pg = pn()
    return """<!-- PAGE %d: Trimester %d Divider -->
<div class="page">
  <div class="tri-divider">
    <div class="td-num">%d</div>
    <div class="td-title">Trimester</div>
    <div class="td-weeks">%s</div>
    <div class="td-line"></div>
  </div>
</div>""" % (pg, tri_num, tri_num, weeks_label)


def weekly_page(week_num):
    pg = pn()
    symptoms = [
        "Nausea", "Fatigue", "Headache", "Backache",
        "Cramping", "Dizziness", "Heartburn", "Cravings",
        "Mood swings", "Breast tenderness", "Frequent urination", "Sleep trouble",
        "Round ligament", "Swelling", "Shortness of breath", "Constipation",
    ]
    syms_html = "\n".join(
        '        <span class="symptom-check"><span class="symptom-box"></span>%s</span>' % s
        for s in symptoms
    )
    return """<!-- PAGE %d: Week %d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Pregnancy Week %d</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="week-banner">
    <span class="wb-week">Week %d</span>
    <span class="wb-sub">Trimester %d &nbsp;|&nbsp; Days pregnant: ~%d</span>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Date</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Weight</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Bump (cm)</span><div class="mf-write"></div></div>
  </div>

  <div style="font-size: 7pt; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; margin-bottom: 4px;">Symptoms Today</div>
  <div class="symptom-grid">
%s
  </div>

  <div class="mood-row">
    <span class="mood-label">Mood</span>
    <div class="mood-dots">
      <div class="mood-dot"></div>
      <div class="mood-dot"></div>
      <div class="mood-dot"></div>
      <div class="mood-dot"></div>
      <div class="mood-dot"></div>
    </div>
    <span style="font-size: 6.5pt; color: #aaa;">(1 = low &nbsp; 5 = great)</span>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Cravings</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Aversions</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Appointments This Week</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Vitamins / Meds Taken</span><div class="if-write"></div></div>
  </div>

  <div style="display: flex; gap: 12px; margin-bottom: 8px;">
    <div class="bump-frame">
      <div class="bf-text">Bump Photo</div>
    </div>
    <div style="flex: 1;">
      <div class="write-box" style="border-color: #B8860B;">
        <div class="wb-label">Baby This Week (Size, Milestones)</div>
        <div class="wb-area" style="height: 32px;"></div>
      </div>
      <div class="write-box">
        <div class="wb-label">How I'm Feeling (Notes, Memories)</div>
        <div class="wb-area" style="height: 32px;"></div>
      </div>
    </div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Partner's Notes</div>
    <div class="wb-area" style="height: 24px;"></div>
  </div>
</div>""" % (pg, week_num, week_num, pg, week_num, 
            (week_num - 1) // 13 + 1 if week_num <= 13 else (2 if week_num <= 27 else 3),
            (week_num - 1) * 7,
            syms_html)


def trimester_reflection(tri_num):
    pg = pn()
    return """<!-- PAGE %d: Trimester %d Reflection -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Trimester %d Reflection</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Looking Back</div>
    <div class="section-line"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Hardest Part of This Trimester</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Best Moment of This Trimester</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Biggest Surprise</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Weight Gain</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Total Appointments</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Weeks Completed</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">What I'm Most Excited About Next</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Advice to My Past Self</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, tri_num, tri_num, pg)


def appointment_log_page():
    pg = pn()
    return """<!-- PAGE %d: Prenatal Appointments -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Prenatal Appointment Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Doctor Visits</div>
    <div class="section-line"></div>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Date</th>
        <th>Week</th>
        <th>Doctor</th>
        <th>Weight</th>
        <th>BP</th>
        <th>Heartbeat</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Questions for Next Visit</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>
</div>""" % (pg, pg)


def ultrasound_page():
    pg = pn()
    return """<!-- PAGE %d: Ultrasound Gallery -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Ultrasound Gallery</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">First Glimpses</div>
    <div class="section-line"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 10px;">
    <div style="border: 1.5px solid #C4A04A; border-radius: 4px; height: 3in; display: flex; align-items: center; justify-content: center;">
      <span style="font-size: 8pt; color: #ccc; text-transform: uppercase; letter-spacing: 0.5pt;">Ultrasound Photo</span>
    </div>
    <div style="border: 1.5px solid #C4A04A; border-radius: 4px; height: 3in; display: flex; align-items: center; justify-content: center;">
      <span style="font-size: 8pt; color: #ccc; text-transform: uppercase; letter-spacing: 0.5pt;">Ultrasound Photo</span>
    </div>
  </div>

  <div class="info-row" style="margin-top: 12px;">
    <div class="info-field"><span class="if-label">Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Week</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">What We Saw (Measurements, Heartbeat, Position)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">How We Felt Seeing Baby</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Doctor's Notes</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def baby_names_page():
    pg = pn()
    return """<!-- PAGE %d: Baby Names -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Baby Names</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Name Brainstorm</div>
    <div class="section-line"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Girl Names We Love</div>
    <div class="wb-area" style="height: 50px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Boy Names We Love</div>
    <div class="wb-area" style="height: 50px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Gender Neutral Options</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Middle Name Ideas</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Names That Are Meaningful to Us (Family, Heritage, Stories)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Our Top 3 Picks</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def nursery_page():
    pg = pn()
    return """<!-- PAGE %d: Nursery Planning -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Nursery Planning</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Baby's Room</div>
    <div class="section-line"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Color Scheme &amp; Theme</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Furniture Needed (Crib, Dresser, Glider, Changing Table...)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Decor Ideas (Wall Art, Lighting, Rug, Curtains...)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div style="font-size: 7pt; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; margin-bottom: 4px;">Registry Checklist</div>
  <div class="symptom-grid">
    <span class="symptom-check"><span class="symptom-box"></span>Crib &amp; Mattress</span>
    <span class="symptom-check"><span class="symptom-box"></span>Bedding Sets</span>
    <span class="symptom-check"><span class="symptom-box"></span>Glider / Rocker</span>
    <span class="symptom-check"><span class="symptom-box"></span>Dresser</span>
    <span class="symptom-check"><span class="symptom-box"></span>Changing Pad</span>
    <span class="symptom-check"><span class="symptom-box"></span>Diaper Pail</span>
    <span class="symptom-check"><span class="symptom-box"></span>Monitor</span>
    <span class="symptom-check"><span class="symptom-box"></span>Nightlight</span>
    <span class="symptom-check"><span class="symptom-box"></span>Swaddle Blankets</span>
    <span class="symptom-check"><span class="symptom-box"></span>Blackout Curtains</span>
    <span class="symptom-check"><span class="symptom-box"></span>Bookshelf</span>
    <span class="symptom-check"><span class="symptom-box"></span>Storage Bins</span>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Budget &amp; Notes</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def hospital_bag_page():
    pg = pn()
    return """<!-- PAGE %d: Hospital Bag Checklist -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Hospital Bag Checklist</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Pack &amp; Ready</div>
    <div class="section-line"></div>
  </div>

  <div style="font-size: 7pt; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; margin-bottom: 4px;">For Mom</div>
  <div class="symptom-grid">
    <span class="symptom-check"><span class="symptom-box"></span>ID &amp; Insurance</span>
    <span class="symptom-check"><span class="symptom-box"></span>Birth Plan</span>
    <span class="symptom-check"><span class="symptom-box"></span>Labor Gown</span>
    <span class="symptom-check"><span class="symptom-box"></span>Slippers / Socks</span>
    <span class="symptom-check"><span class="symptom-box"></span>Nursing Bras</span>
    <span class="symptom-check"><span class="symptom-box"></span>Going-Home Outfit</span>
    <span class="symptom-check"><span class="symptom-box"></span>Toiletries</span>
    <span class="symptom-check"><span class="symptom-box"></span>Hair Ties</span>
    <span class="symptom-check"><span class="symptom-box"></span>Lip Balm</span>
    <span class="symptom-check"><span class="symptom-box"></span>Phone Charger</span>
    <span class="symptom-check"><span class="symptom-box"></span>Snacks &amp; Drinks</span>
    <span class="symptom-check"><span class="symptom-box"></span>Pillow from Home</span>
  </div>

  <div style="font-size: 7pt; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; margin-bottom: 4px; margin-top: 8px;">For Partner / Support</div>
  <div class="symptom-grid">
    <span class="symptom-check"><span class="symptom-box"></span>Change of Clothes</span>
    <span class="symptom-check"><span class="symptom-box"></span>Toiletries</span>
    <span class="symptom-check"><span class="symptom-box"></span>Phone Charger</span>
    <span class="symptom-check"><span class="symptom-box"></span>Snacks</span>
    <span class="symptom-check"><span class="symptom-box"></span>Cash / Coins</span>
    <span class="symptom-check"><span class="symptom-box"></span>Camera / Batteries</span>
  </div>

  <div style="font-size: 7pt; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; margin-bottom: 4px; margin-top: 8px;">For Baby</div>
  <div class="symptom-grid">
    <span class="symptom-check"><span class="symptom-box"></span>Going-Home Outfit</span>
    <span class="symptom-check"><span class="symptom-box"></span>2-3 Onesies</span>
    <span class="symptom-check"><span class="symptom-box"></span>Hats &amp; Mittens</span>
    <span class="symptom-check"><span class="symptom-box"></span>Swaddle Blankets</span>
    <span class="symptom-check"><span class="symptom-box"></span>Car Seat</span>
    <span class="symptom-check"><span class="symptom-box"></span>Socks / Booties</span>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Other Items &amp; Notes</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def birth_plan_page():
    pg = pn()
    return """<!-- PAGE %d: Birth Plan -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Birth Plan</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Our Preferences</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Hospital / Center</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">OB / Midwife</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Labor Environment (Lighting, Music, Who Is Present)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Pain Management Preferences</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Positions &amp; Movement During Labor</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div style="font-size: 7pt; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; margin-bottom: 4px;">Preferences</div>
  <div class="symptom-grid">
    <span class="symptom-check"><span class="symptom-box"></span>Skin-to-skin right after</span>
    <span class="symptom-check"><span class="symptom-box"></span>Delay cord clamping</span>
    <span class="symptom-check"><span class="symptom-box"></span>Breastfeed first hour</span>
    <span class="symptom-check"><span class="symptom-box"></span>No formula unless needed</span>
    <span class="symptom-check"><span class="symptom-box"></span>Partner cuts cord</span>
    <span class="symptom-check"><span class="symptom-box"></span>Photos / Video in delivery</span>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">In Case of C-Section (Preferences)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Other Wishes &amp; Notes</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def baby_shower_page():
    pg = pn()
    return """<!-- PAGE %d: Baby Shower -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Baby Shower Planning</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Celebrating Baby</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Host</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Venue</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Theme</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Guest Count</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Registry Link</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Food &amp; Drink Plan</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Games &amp; Activities</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Decor &amp; Favors</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Gifts Received (Thank You Notes Tracker)</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def birth_day_page():
    pg = pn()
    return """<!-- PAGE %d: Birth Day -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Birth Day</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Welcome, Baby</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Baby's Full Name</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Date of Birth</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Time of Birth</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Day of Week</span><div class="if-write"></div></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Weight</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Length</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Head Circ.</span><div class="mf-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Delivered By</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Hospital</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Labor &amp; Delivery Story</div>
    <div class="wb-area" style="height: 50px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">First Thoughts When We Met Baby</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Who Was There &amp; First Visitors</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">First Photo Description / Memory</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def notes_page():
    pg = pn()
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes &amp; Memories</span>
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
      You are stronger than you know.<br>
      You are more loved than you imagine.<br>
      You are already the perfect mother<br>
      for this little one.
    </div>
    <div class="fp-line"></div>
    <div class="fp-logo">More Shine Press</div>
    <div class="fp-line"></div>
  </div>
</div>""" % pg


def generate(output_path=HTML_FILE):
    pages = []
    # Front matter
    pages.append(interior_title_page())
    pages.append(how_to_use_page())
    pages.append(overview_page())

    # Trimester 1: weeks 4-13
    pages.append(trimester_divider(1, "Weeks 4 - 13"))
    for w in range(4, 14):
        pages.append(weekly_page(w))
    pages.append(trimester_reflection(1))

    # Trimester 2: weeks 14-27
    pages.append(trimester_divider(2, "Weeks 14 - 27"))
    for w in range(14, 28):
        pages.append(weekly_page(w))
    pages.append(trimester_reflection(2))

    # Trimester 3: weeks 28-40
    pages.append(trimester_divider(3, "Weeks 28 - 40"))
    for w in range(28, 41):
        pages.append(weekly_page(w))
    pages.append(trimester_reflection(3))

    # Milestone pages
    for _ in range(4):
        pages.append(appointment_log_page())
    for _ in range(2):
        pages.append(ultrasound_page())
    for _ in range(2):
        pages.append(baby_names_page())
    pages.append(nursery_page())
    pages.append(hospital_bag_page())
    for _ in range(2):
        pages.append(birth_plan_page())
    pages.append(baby_shower_page())
    for _ in range(2):
        pages.append(birth_day_page())

    # Notes
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
