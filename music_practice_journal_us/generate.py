#!/usr/bin/env python3
"""
Music Practice Journal -- KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Music students and performers
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "music_practice_journal_us_V1.0.html")

BOOK_TITLE = "Music Practice Journal"
BOOK_SUBTITLE = "Track Your Progress, Master Your Craft"

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

/* ================ FOCUS CHECKBOXES ================ */
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

/* ================ HABIT TRACKER (weekly review) ================ */
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
      <!-- Treble clef minimal icon -->
      <g transform="translate(50,50)">
        <!-- Vertical stem -->
        <line x1="0" y1="-32" x2="0" y2="30" stroke="#B8860B" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Upper curl -->
        <path d="M 0,-32 C 12,-32 14,-18 4,-12 C -6,-6 -10,4 0,10 C 12,18 16,2 6,-4"
              stroke="#B8860B" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <!-- Lower loop -->
        <ellipse cx="0" cy="20" rx="9" ry="10" stroke="#B8860B" stroke-width="2.5" fill="none"/>
        <!-- Gold dot accent -->
        <circle cx="0" cy="20" r="3" fill="#C4A04A"/>
      </g>
    </svg>
  </div>

  <div class="title-main">Music<br>Practice<br>Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Track Your Progress,<br>Master Your Craft</div>

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
    <div class="ht-title"><span class="ht-icon">&#9835;</span> Your Practice Companion</div>
    <p>This journal is designed to help you become a more focused,
    deliberate, and self-aware musician. Every great musician keeps
    practice records -- not because they enjoy paperwork, but because
    reviewing past sessions is the fastest path to mastery.</p>

    <div class="ht-title"><span class="ht-icon">&#9835;</span> The Two-Page Session Spread</div>
    <p>Each session uses a <strong>two-page spread</strong>. The left page
    captures the essentials: date, instrument, piece, composer, duration,
    focus areas, metronome markings, and key signature. The right page is
    for your reflection: what went well, what needs work, specific
    passages practiced, tempo progress, teacher notes, and goals for
    next time.</p>

    <div class="ht-title"><span class="ht-icon">&#9835;</span> The Weekly Review</div>
    <p>After every 5 sessions, a <strong>weekly review page</strong> helps
    you track total practice time, pieces worked on, breakthroughs,
    areas needing attention, and a 7-day habit tracker. This is where
    progress becomes visible.</p>

    <div class="ht-title"><span class="ht-icon">&#9835;</span> How to Practice Effectively</div>
    <p>&#9679; <strong>Set a goal before each session.</strong> Know what
    you want to improve before you begin.</p>
    <p>&#9679; <strong>Practice slowly.</strong> Use the metronome markings
    to track tempo from start to target.</p>
    <p>&#9679; <strong>Isolate difficult passages.</strong> Note the bar
    numbers so you can return to them.</p>
    <p>&#9679; <strong>Review regularly.</strong> Progress compounds over
    weeks, not single sessions.</p>
  </div>
</div>""" % (pg, pg)


def goals_page():
    pg = pn()
    return """<!-- PAGE %d: Practice Goals -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Practice Goals</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">My Goals</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Term / Semester</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Start Date</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">What I Want to Improve (Technique, Tone, Expression)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Pieces to Learn</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Target Tempo (BPM)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Daily Practice Goal</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Sessions per Week</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Performance / Exam Goals</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Inspiration (Musicians I Admire)</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Motivation -- Why I Play</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>
</div>""" % (pg, pg)


def session_left(entry_num):
    pg = pn()
    focus_areas = ["Scales", "Technique", "Repertoire", "Sight-Reading", "Ear-Training", "Theory", "Ensemble"]
    focus_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % fa
        for fa in focus_areas
    )
    return """<!-- PAGE %d: Session Left #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Practice Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="session-banner">
    <span class="sb-num">Session #%03d</span>
    <span class="sb-label">Date:</span>
    <div class="sb-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Day of Week</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Instrument</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Piece / Title</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Composer</span><div class="if-write"></div></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Practice Duration (min)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Key Signature</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Time Signature</span><div class="mf-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Focus Areas (Check All)</div>
  <div class="type-row">%s</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 6px;">
    <div>
      <div style="font-size: 6.5pt; font-weight: 700; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 1px;">Metronome Start (BPM)</div>
      <div class="mf-write" style="height: 18px; border-bottom: 1px dotted #ccc;"></div>
    </div>
    <div>
      <div style="font-size: 6.5pt; font-weight: 700; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 1px;">Metronome Target (BPM)</div>
      <div class="mf-write" style="height: 18px; border-bottom: 1px dotted #ccc;"></div>
    </div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Specific Passages Practiced (Bar Numbers)</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Warm-Up / Exercises Done</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, entry_num, pg, entry_num, focus_html)


def session_right():
    pg = pn()
    return """<!-- PAGE %d: Session Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Session Reflection</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">What Went Well</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #8B4040;">
    <div class="wb-label">What Needs Work</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Tempo Progress (Start BPM &#8594; Current BPM)</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Teacher Notes</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Goals for Next Session</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 6px;">
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Mood / Energy Level</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Low &#160; 5 = High</div>
    </div>
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Focus Quality</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Distracted &#160; 5 = Locked In</div>
    </div>
  </div>
</div>""" % (pg, pg)


def weekly_review_page(review_num):
    pg = pn()
    days_html = "".join(
        '<div class="habit-day">%s</div>' % d
        for d in ["M", "T", "W", "T", "F", "S", "S"]
    )
    return """<!-- PAGE %d: Weekly Review #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Weekly Review</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="session-banner">
    <span class="sb-num">Review #%02d</span>
    <span class="sb-label">Week of:</span>
    <div class="sb-line"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Total Practice Time</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Sessions This Week</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Avg Session Length</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Pieces Worked On</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Breakthroughs / Highlights</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #8B4040;">
    <div class="wb-label">Areas Needing Attention</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Focus for Next Week</div>
    <div class="wb-area"></div>
  </div>

  <div style="margin-top: 6px;">
    <div style="font-size: 6.5pt; font-weight: 700; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Habit Tracker -- Practiced X/7 Days</div>
    <div class="habit-track">%s</div>
  </div>
</div>""" % (pg, review_num, pg, review_num, days_html)


def repertoire_page():
    pg = pn()
    return """<!-- PAGE %d: Repertoire List -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Repertoire List</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Piece</th>
        <th>Composer</th>
        <th>Date Started</th>
        <th>Memorized</th>
        <th>Ready?</th>
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
    </tbody>
  </table>
</div>""" % (pg, pg)


def performance_log_page():
    pg = pn()
    return """<!-- PAGE %d: Performance Log -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Performance Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="info-row" style="margin-bottom: 10px;">
    <div class="info-field"><span class="if-label">Event / Occasion</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Date</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Venue / Location</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Piece(s) Performed</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">How It Went (Strengths)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #8B4040;">
    <div class="wb-label">What to Improve Next Time</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 6px;">
    <div>
      <div style="font-size: 6.5pt; font-weight: 700; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Preparation Level</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
    </div>
    <div>
      <div style="font-size: 6.5pt; font-weight: 700; color: #B8860B; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Performance Confidence</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
    </div>
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
    <div class="info-field"><span class="if-label">Total Sessions</span><div class="if-write"></div></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Total Practice Hours</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Avg Session Length</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Days Practiced</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">New Pieces Started</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Pieces Completed / Memorized</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Highlights of the Month</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #8B4040;">
    <div class="wb-label">Biggest Challenge</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Goals for Next Month</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def notes_page():
    pg = pn()
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes &amp; Musical Ideas</span>
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
      Practice with patience.<br>
      Every session is progress.<br>
      Listen. Reflect. Improve.
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

    # 25 session spreads (50 pages), with a weekly review every 5 sessions
    session_count = 0
    review_count = 0
    for entry in range(1, 26):
        pages.append(session_left(entry))
        pages.append(session_right())
        session_count += 1
        # Insert weekly review after every 5th session
        if session_count % 5 == 0:
            review_count += 1
            pages.append(weekly_review_page(review_count))

    # Repertoire list (2 pages)
    for _ in range(2):
        pages.append(repertoire_page())

    # Performance log (2 pages)
    for _ in range(2):
        pages.append(performance_log_page())

    # Monthly summary (2 pages)
    for _ in range(2):
        pages.append(monthly_summary_page())

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
