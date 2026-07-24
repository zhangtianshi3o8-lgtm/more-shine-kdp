#!/usr/bin/env python3
"""
Yoga and Meditation Journal -- KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Yoga and meditation practitioners
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "yoga_meditation_journal_us_V1.0.html")

BOOK_TITLE = "Yoga and Meditation Journal"
BOOK_SUBTITLE = "Track Your Practice, Nurture Your Inner Peace"

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
  background: linear-gradient(165deg, #161616 0%, #232323 30%, #161616 65%, #0E0E0E 100%);
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #7A9A7E, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #7A9A7E, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #7A9A7E, transparent);
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
  background: #7A9A7E;
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
  color: #7A9A7E;
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
  background: #7A9A7E;
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
.howto-text .ht-icon { color: #7A9A7E; font-weight: 700; margin-right: 4px; }

/* ================ INFO FIELDS ================ */
.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
  margin-bottom: 8px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #7A9A7E;
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
  border-bottom: 1.5px solid #7A9A7E;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.session-banner .sb-num {
  display: inline-block;
  border: 1.5px solid #7A9A7E;
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 8pt;
  color: #7A9A7E;
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
  border: 1.5px solid #7A9A7E;
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
  color: #7A9A7E;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 5px 3px;
  border-bottom: 1.5px solid #7A9A7E;
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
  color: #7A9A7E;
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
  color: #7A9A7E;
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
  border: 1.5px solid #7A9A7E;
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
  width: 60px; height: 1.5px; background: #7A9A7E;
  margin: 12px auto; opacity: 0.5;
}
"""


def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- Lotus flower outline -->
      <g transform="translate(50,52)" stroke="#7A9A7E" stroke-width="1.8" fill="none" stroke-linejoin="round">
        <!-- Center petal -->
        <path d="M0,-32 C-6,-18 -6,-6 0,0 C6,-6 6,-18 0,-32 Z"/>
        <!-- Inner side petals -->
        <path d="M-18,-24 C-16,-12 -10,-4 0,0 C-4,-10 -8,-20 -18,-24 Z"/>
        <path d="M18,-24 C16,-12 10,-4 0,0 C4,-10 8,-20 18,-24 Z"/>
        <!-- Outer side petals -->
        <path d="M-30,-14 C-22,-6 -14,-2 0,0 C-8,-8 -16,-14 -30,-14 Z"/>
        <path d="M30,-14 C22,-6 14,-2 0,0 C8,-8 16,-14 30,-14 Z"/>
        <!-- Base line -->
        <line x1="-24" y1="6" x2="24" y2="6" stroke="#C4A04A" stroke-width="1" opacity="0.5"/>
      </g>
    </svg>
  </div>

  <div class="title-main">Yoga &amp;<br>Meditation<br>Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Track Your Practice,<br>Nurture Your Inner Peace</div>

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
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Practice Companion</div>
    <p>This journal is designed to help you build a consistent,
    mindful yoga and meditation practice. Every dedicated
    practitioner keeps records -- not because it is a chore, but
    because reflecting on your practice is the surest path to
    inner growth and lasting peace.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Two-Page Practice Spread</div>
    <p>Each session uses a <strong>two-page spread</strong>. The left
    page captures the essentials: date, day, practice type, duration,
    location, time of day, and your teacher or source. The right page
    is for your inner experience: poses practiced, breathwork,
    meditation length, how you felt before and after, energy and
    mind-chatter levels, emotions, insights, and gratitude.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Weekly Reflection</div>
    <p>After every 5 sessions, a <strong>weekly reflection page</strong>
    helps you spot patterns: total practice time, breakthrough moments,
    challenging poses, the week's theme, and what to focus on next.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Guidelines to Follow</div>
    <p>&#9679; <strong>Fill it in right after practice</strong>, while
    the experience is still fresh in body and mind.</p>
    <p>&#9679; <strong>Be honest.</strong> Record how you truly felt,
    not how you wish you had felt.</p>
    <p>&#9679; <strong>Reflect weekly.</strong> Patterns emerge over
    many sessions.</p>
    <p>&#9679; <strong>Set intentions monthly.</strong> Clarity of
    purpose deepens every practice.</p>
  </div>
</div>""" % (pg, pg)


def intention_setting_page():
    pg = pn()
    focus_areas = ["Flexibility", "Strength", "Mindfulness", "Stress Relief", "Spiritual Growth"]
    focus_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % a
        for a in focus_areas
    )
    return """<!-- PAGE %d: Intention Setting -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Intention Setting</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Monthly Intentions</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Month / Year</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Sessions Goal</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Meditation Goal (min/day)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Days Per Week</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #7A9A7E; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Areas to Focus</div>
  <div class="type-row">%s</div>

  <div class="write-box" style="border-color: #7A9A7E;">
    <div class="wb-label">My Intention for This Month</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Poses I Want to Master</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #7A9A7E;">
    <div class="wb-label">Habits I Want to Build</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">What Does Inner Peace Mean to Me Right Now?</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>
</div>""" % (pg, pg, focus_html)


def practice_left(entry_num):
    pg = pn()
    practice_types = [
        "Hatha", "Vinyasa", "Ashtanga", "Yin", "Restorative",
        "Kundalini", "Meditation", "Pranayama", "Bikram",
    ]
    type_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % t
        for t in practice_types
    )
    locations = ["Home", "Studio", "Outdoors"]
    loc_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % loc
        for loc in locations
    )
    times = ["Morning", "Afternoon", "Evening"]
    time_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % tm
        for tm in times
    )
    return """<!-- PAGE %d: Practice Left #%d -->
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
    <div class="info-field"><span class="if-label">Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Day of Week</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Duration (min)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Teacher / Source</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #7A9A7E; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Practice Type</div>
  <div class="type-row">%s</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 12px; margin-bottom: 8px;">
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #7A9A7E; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Location</div>
      <div class="type-row" style="margin-bottom: 0;">%s</div>
    </div>
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #7A9A7E; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Time of Day</div>
      <div class="type-row" style="margin-bottom: 0;">%s</div>
    </div>
  </div>

  <div class="write-box" style="border-color: #7A9A7E;">
    <div class="wb-label">How I Felt Before Practice</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Setting the Scene (Music, Candle, Props, Mood)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>
</div>""" % (pg, entry_num, pg, entry_num, type_html, loc_html, time_html)


def practice_right():
    pg = pn()
    return """<!-- PAGE %d: Practice Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Practice Reflection</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="write-box">
    <div class="wb-label">Poses Practiced (Sequence / Flow)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="info-row" style="margin-bottom: 8px;">
    <div class="info-field"><span class="if-label">Breathwork / Pranayama Done</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Meditation Duration (min)</span><div class="if-write"></div></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px 12px; margin-top: 4px; margin-bottom: 8px;">
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #7A9A7E; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Felt Before (1-5)</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Restless &#160; 5 = Centered</div>
    </div>
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #7A9A7E; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Felt After (1-5)</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Drained &#160; 5 = Renewed</div>
    </div>
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #7A9A7E; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Energy Level (1-5)</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Sluggish &#160; 5 = Vibrant</div>
    </div>
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #7A9A7E; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Mind Chatter (1-5)</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Busy &#160; 5 = Still</div>
    </div>
  </div>

  <div class="write-box" style="border-color: #7A9A7E;">
    <div class="wb-label">What Arose Emotionally</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Insights / Intuitive Messages</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box" style="border-color: #C4A04A;">
    <div class="wb-label">Gratitude from Today's Practice</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def weekly_reflection_page(review_num):
    pg = pn()
    return """<!-- PAGE %d: Weekly Reflection #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Weekly Reflection</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="session-banner">
    <span class="sb-num">Reflection #%02d</span>
    <span class="sb-label">Week of:</span>
    <div class="sb-line"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Total Sessions</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Total Practice Time (min)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Total Meditation (min)</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #7A9A7E;">
    <div class="wb-label">Most Impactful Session (What Made It So)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Breakthrough Moments</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #7A9A7E;">
    <div class="wb-label">Challenging Poses or Moments</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Theme of the Week</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #7A9A7E;">
    <div class="wb-label">What to Focus on Next Week</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, review_num, pg, review_num)


def pose_tracker_page(page_part):
    pg = pn()
    return """<!-- PAGE %d: Pose Progress Tracker -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Pose Progress Tracker</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Pose Name</th>
        <th>Date First Attempted</th>
        <th>Alignment Notes</th>
        <th>Progress (1-5)</th>
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


def monthly_reflection_page(page_part):
    pg = pn()
    return """<!-- PAGE %d: Monthly Reflection -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Monthly Reflection</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Monthly Reflection</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Month / Year</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Total Sessions</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Total Minutes</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Meditation Total (min)</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #7A9A7E;">
    <div class="wb-label">New Poses Learned</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Biggest Breakthrough</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #7A9A7E;">
    <div class="wb-label">Areas of Growth (Body, Mind, Spirit)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Goals for Next Month</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>
</div>""" % (pg, pg)


def notes_page():
    pg = pn()
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes &amp; Reflections</span>
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
      The body benefits from movement.<br>
      The mind benefits from stillness.<br>
      Breathe. Flow. Return to center.
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
    pages.append(intention_setting_page())

    # 25 practice spreads (50 pages), with a weekly reflection every 5 sessions
    practice_count = 0
    review_count = 0
    for entry in range(1, 26):
        pages.append(practice_left(entry))
        pages.append(practice_right())
        practice_count += 1
        # Insert weekly reflection after every 5th session
        if practice_count % 5 == 0:
            review_count += 1
            pages.append(weekly_reflection_page(review_count))

    # Pose progress tracker (2 pages)
    pages.append(pose_tracker_page(1))
    pages.append(pose_tracker_page(2))

    # Monthly reflection (2 pages)
    pages.append(monthly_reflection_page(1))
    pages.append(monthly_reflection_page(2))

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
