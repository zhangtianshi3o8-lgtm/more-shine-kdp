#!/usr/bin/env python3
"""
Gratitude Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "gratitude_journal_us_V1.0.html")

BOOK_TITLE = "Gratitude Journal"
BOOK_SUBTITLE = "Find Joy in Every Day"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

def goal_lines(n):
    return "\n".join(
        '<div class="goal-line"><div class="goal-checkbox"></div>'
        '<div class="goal-write"></div></div>'
        for _ in range(n)
    )

def wl(n):
    """n weekly-lines divs."""
    return "\n".join('<div class="weekly-lines"></div>' for _ in range(n))

def nl(n):
    """n notes-line divs."""
    return "\n".join('<div class="notes-line"></div>' for _ in range(n))

# ============================================================
# CSS  (raw string — never f-string, to avoid backslash issues)
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #C4A04A, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 90% 40%, #C4A04A, transparent);
}

.cover .title-main {
  font-size: 32pt;
  font-weight: 700;
  color: #FAF6F0;
  line-height: 1.2;
  letter-spacing: 1pt;
  position: relative;
  z-index: 2;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 100px;
  height: 2px;
  background: #C4A04A;
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
  bottom: 0.6in;
  left: 0; right: 0;
  text-align: center;
  font-size: 9pt;
  color: #C4A04A;
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  font-weight: 700;
}

/* ================ SECTION HEADERS ================ */
.section-header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
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
  background: #C4A04A;
  margin: 0 12px;
  opacity: 0.5;
}

/* ================ DAILY ENTRY ================ */
.daily-date {
  display: flex;
  align-items: baseline;
  gap: 8px;
  border-bottom: 1.5px solid #C4A04A;
  padding-bottom: 6px;
  margin-bottom: 14px;
}

.daily-date .date-label {
  font-size: 9pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 1pt;
}

.daily-date .date-line {
  flex: 1;
  height: 14px;
  border-bottom: 1px dotted #ccc;
}

.daily-date .mood-label {
  font-size: 9pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 1pt;
}

.daily-date .mood-circles {
  display: flex;
  gap: 4px;
}

.mood-circle {
  width: 16px;
  height: 16px;
  border: 1.5px solid #C4A04A;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 6pt;
  color: #C4A04A;
}

.gratitude-prompt {
  font-size: 9pt;
  color: #7A8B6F;
  font-style: italic;
  margin-bottom: 4px;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.gratitude-line {
  height: 26px;
  border-bottom: 1px solid #ddd;
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.gratitude-num {
  width: 18px;
  height: 18px;
  border: 1.5px solid #C4A04A;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 7pt;
  color: #C4A04A;
  margin-right: 10px;
  flex-shrink: 0;
}

.gratitude-write {
  flex: 1;
  height: 18px;
}

.reflection-box {
  border: 1px solid #C4A04A;
  border-radius: 4px;
  padding: 10px 12px;
  margin-top: 12px;
  background: #FAF6F0;
}

.reflection-box .r-label {
  font-size: 8pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 1pt;
  font-weight: 700;
  margin-bottom: 4px;
}

.reflection-lines {
  height: 40px;
}

.highlight-box {
  border-left: 3px solid #C4A04A;
  padding: 8px 12px;
  margin-top: 12px;
  background: #FAF6F0;
}

.highlight-box .h-label {
  font-size: 8pt;
  color: #7A8B6F;
  text-transform: uppercase;
  letter-spacing: 1pt;
  font-weight: 700;
  margin-bottom: 4px;
}

.highlight-lines {
  height: 30px;
}

/* ================ WEEKLY REVIEW ================ */
.weekly-header {
  text-align: center;
  margin-bottom: 16px;
}

.weekly-week-num {
  display: inline-block;
  border: 1.5px solid #C4A04A;
  border-radius: 4px;
  padding: 4px 12px;
  font-size: 9pt;
  color: #C4A04A;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1pt;
  margin-bottom: 12px;
}

.weekly-section {
  margin-bottom: 14px;
}

.weekly-prompt {
  font-size: 9.5pt;
  color: #7A8B6F;
  font-style: italic;
  margin-bottom: 4px;
  font-weight: 600;
}

.weekly-lines {
  border-bottom: 1px solid #ddd;
  height: 24px;
}

.rating-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 8px;
}

.rating-label {
  font-size: 9pt;
  color: #2A2A2A;
  width: 140px;
  flex-shrink: 0;
}

.rating-dots {
  display: flex;
  gap: 6px;
}

.rating-dot {
  width: 14px;
  height: 14px;
  border: 1.5px solid #C4A04A;
  border-radius: 50%;
}

.rating-dots .rating-num {
  font-size: 7pt;
  color: #C4A04A;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 14px;
}

/* ================ MONTHLY REVIEW ================ */
.monthly-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 14px;
}

.monthly-card {
  border: 1px solid #C4A04A;
  border-radius: 4px;
  padding: 10px;
  background: #FAF6F0;
}

.monthly-card .mc-label {
  font-size: 8pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 1pt;
  font-weight: 700;
  margin-bottom: 6px;
}

.monthly-card .mc-lines {
  height: 40px;
  border-bottom: 1px dotted #ccc;
}

/* ================ GOAL SETTING ================ */
.goal-box {
  border: 1px solid #C4A04A;
  border-radius: 4px;
  padding: 12px;
  margin-bottom: 10px;
}

.goal-box .g-label {
  font-size: 9pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 1pt;
  font-weight: 700;
  margin-bottom: 6px;
}

.goal-line {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.goal-checkbox {
  width: 14px;
  height: 14px;
  border: 1.5px solid #C4A04A;
  border-radius: 2px;
  flex-shrink: 0;
}

.goal-write {
  flex: 1;
  border-bottom: 1px dotted #ccc;
  height: 16px;
}

/* ================ HOW TO USE ================ */
.howto-text {
  font-size: 10pt;
  line-height: 1.7;
  color: #2A2A2A;
}

.howto-text p {
  margin-bottom: 10px;
}

.howto-text .ht-title {
  font-size: 11pt;
  font-weight: 700;
  color: #161616;
  margin-bottom: 4px;
  margin-top: 6px;
}

.howto-text .ht-icon {
  color: #C4A04A;
  font-weight: 700;
  margin-right: 4px;
}

/* ================ QUOTE PAGE ================ */
.quote-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100%;
  padding: 0 0.75in;
}

.quote-mark {
  font-size: 48pt;
  color: #C4A04A;
  opacity: 0.3;
  font-family: Georgia, serif;
  line-height: 1;
  margin-bottom: -10px;
}

.quote-text {
  font-size: 16pt;
  font-style: italic;
  color: #2A2A2A;
  line-height: 1.6;
}

.quote-author {
  font-size: 10pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 2pt;
  margin-top: 16px;
  font-weight: 700;
}

/* ================ HABIT TRACKER ================ */
.habit-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 8px;
}

.habit-table th {
  font-size: 7.5pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 6px 4px;
  border-bottom: 1.5px solid #C4A04A;
  text-align: center;
}

.habit-table th:first-child {
  text-align: left;
  width: 130px;
}

.habit-table td {
  padding: 6px 4px;
  border-bottom: 1px solid #eee;
  text-align: center;
  height: 24px;
}

.habit-table td:first-child {
  text-align: left;
  font-size: 9pt;
  color: #2A2A2A;
}

.habit-check {
  width: 12px;
  height: 12px;
  border: 1px solid #C4A04A;
  border-radius: 50%;
  display: inline-block;
}

/* ================ PAGE HEADER ================ */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
  padding-bottom: 4px;
  border-bottom: 0.5px solid #eee;
}

.page-header .ph-left {
  font-size: 8pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 1pt;
  font-weight: 700;
}

.page-header .ph-right {
  font-size: 8pt;
  color: #999;
}

/* ================ NOTES PAGE ================ */
.notes-lines {
  width: 100%;
}

.notes-line {
  border-bottom: 1px solid #ddd;
  height: 24px;
}

/* ================ FINAL PAGE ================ */
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
  background: #C4A04A;
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
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="8" stroke="#C4A04A" stroke-width="1.5" fill="none"/>
      <ellipse cx="50" cy="28" rx="8" ry="18" stroke="#C4A04A" stroke-width="1.5" fill="none" opacity="0.7"/>
      <ellipse cx="50" cy="72" rx="8" ry="18" stroke="#C4A04A" stroke-width="1.5" fill="none" opacity="0.7"/>
      <ellipse cx="28" cy="50" rx="18" ry="8" stroke="#C4A04A" stroke-width="1.5" fill="none" opacity="0.7"/>
      <ellipse cx="72" cy="50" rx="18" ry="8" stroke="#C4A04A" stroke-width="1.5" fill="none" opacity="0.7"/>
      <ellipse cx="35" cy="35" rx="8" ry="14" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.5"
               transform="rotate(-45 35 35)"/>
      <ellipse cx="65" cy="35" rx="8" ry="14" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.5"
               transform="rotate(45 65 35)"/>
      <ellipse cx="35" cy="65" rx="8" ry="14" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.5"
               transform="rotate(45 35 65)"/>
      <ellipse cx="65" cy="65" rx="8" ry="14" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.5"
               transform="rotate(-45 65 65)"/>
    </svg>
  </div>

  <div class="title-main">Gratitude<br>Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Find Joy in Every Day</div>

  <div class="pub">More Shine Press</div>
</div>""" % pn()


def how_to_use_page_1():
    pg = pn()
    return """<!-- PAGE %d: How to Use 1 -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">How to Use This Journal</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Welcome to Your Gratitude Practice</div>
    <p>Gratitude is more than saying "thank you." It is a daily practice of
    noticing the good in your life &mdash; the big moments and the small ones.
    Research shows that people who regularly write down what they are grateful
    for report higher levels of happiness, better sleep, and stronger
    relationships.</p>

    <p>This journal is designed to make gratitude a simple, meaningful part
    of your everyday routine. You do not need to write a lot. Just a few
    minutes a day is enough to shift your perspective.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Daily Practice</div>
    <p>Each day, you will find space to write <strong>three things</strong> you are
    grateful for. They can be as simple as a warm cup of coffee or as
    meaningful as a conversation with a loved one. There are no wrong answers.</p>

    <p>You will also find a <strong>daily highlight</strong> section for capturing
    one special moment, and a <strong>reflection</strong> space for deeper
    thoughts. End each day by rating your overall mood.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Weekly and Monthly Reviews</div>
    <p>Every seven days, take a few extra minutes for a <strong>weekly review</strong>
    &mdash; look back on themes, big moments, and lessons learned. At the end
    of each month, you will find a <strong>monthly reflection</strong> page to
    zoom out and see the bigger picture of your growth.</p>
  </div>
</div>""" % (pg, pg)


def how_to_use_page_2():
    pg = pn()
    habits = [
        "Wrote 3 gratitudes",
        "Meditated or prayed",
        "Exercised",
        "Read for 20 minutes",
        "Drank 8 glasses of water",
        "Slept 7+ hours",
        "Reached out to someone",
        "Spent time outdoors",
    ]
    days = ["M", "T", "W", "T", "F", "S", "S"]
    habit_rows = ""
    for h in habits:
        cells = "".join('<td><span class="habit-check"></span></td>' for _ in days)
        habit_rows += "<tr><td>%s</td>%s</tr>\n" % (H.escape(h), cells)

    return """<!-- PAGE %d: How to Use 2 — Habit Tracker -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Weekly Habit Tracker</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Build Your Gratitude Habit</div>
    <p>Consistency matters more than perfection. Use the tracker below to
    build your daily gratitude practice. Check off each day you complete
    a habit. Do not worry about perfect streaks &mdash; just come back tomorrow.</p>
  </div>

  <table class="habit-table">
    <thead>
      <tr>
        <th>Habit</th>
        <th>M</th><th>T</th><th>W</th><th>T</th><th>F</th><th>S</th><th>S</th>
      </tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>

  <div class="howto-text" style="margin-top: 16px;">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips for Success</div>
    <p>&#9679; <strong>Same time, same place.</strong> Morning or bedtime works best.</p>
    <p>&#9679; <strong>Be specific.</strong> "My daughter's laugh" beats "my family."</p>
    <p>&#9679; <strong>Feel it.</strong> Do not just list &mdash; take a moment to feel the gratitude.</p>
    <p>&#9679; <strong>No judgment.</strong> If you miss a day, just start again.</p>
  </div>
</div>""" % (pg, pg, habit_rows)


def goal_setting_page():
    pg = pn()
    return """<!-- PAGE %d: Goal Setting -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">My Intentions</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Setting My Intentions</div>
    <div class="section-line"></div>
  </div>

  <div class="goal-box">
    <div class="g-label">My Gratitude Goals for This Journal</div>
    %s
  </div>

  <div class="goal-box">
    <div class="g-label">Three Things I Want to Appreciate More</div>
    %s
  </div>

  <div class="goal-box">
    <div class="g-label">People I Want to Thank in Person</div>
    %s
  </div>

  <div class="goal-box">
    <div class="g-label">Positive Changes I Want to Make</div>
    %s
  </div>

  <div class="reflection-box">
    <div class="r-label">My Personal Mantra</div>
    <div class="reflection-lines"></div>
  </div>
</div>""" % (pg, pg, goal_lines(4), goal_lines(3), goal_lines(3), goal_lines(3))


def quote_page(quote, author):
    pg = pn()
    return """<!-- PAGE %d: Quote -->
<div class="page">
  <div class="quote-page">
    <div class="quote-mark">&ldquo;</div>
    <div class="quote-text">%s</div>
    <div class="quote-author">&mdash; %s</div>
  </div>
</div>""" % (pg, H.escape(quote), H.escape(author))


def daily_entry_page():
    pg = pn()
    return """<!-- PAGE %d: Daily Entry -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Today I Am Grateful For</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="daily-date">
    <span class="date-label">Date:</span>
    <div class="date-line" style="width: 1.8in;"></div>
    <span class="mood-label">Mood:</span>
    <div class="mood-circles">
      <div class="mood-circle">1</div>
      <div class="mood-circle">2</div>
      <div class="mood-circle">3</div>
      <div class="mood-circle">4</div>
      <div class="mood-circle">5</div>
    </div>
  </div>

  <div class="gratitude-prompt">Three things I am grateful for today:</div>

  <div class="gratitude-line">
    <div class="gratitude-num">1</div>
    <div class="gratitude-write"></div>
  </div>
  <div class="gratitude-line">
    <div class="gratitude-num">2</div>
    <div class="gratitude-write"></div>
  </div>
  <div class="gratitude-line">
    <div class="gratitude-num">3</div>
    <div class="gratitude-write"></div>
  </div>

  <div class="gratitude-prompt" style="margin-top: 6px;">Someone who made my day better:</div>
  <div class="gratitude-line">
    <div class="gratitude-num" style="border-color: #7A8B6F; color: #7A8B6F;">&#9829;</div>
    <div class="gratitude-write"></div>
  </div>

  <div class="gratitude-prompt" style="margin-top: 6px;">Something about myself I appreciate today:</div>
  <div class="gratitude-line">
    <div class="gratitude-num" style="border-color: #B85C7A; color: #B85C7A;">&#9733;</div>
    <div class="gratitude-write"></div>
  </div>

  <div class="highlight-box">
    <div class="h-label">Today's Highlight</div>
    <div class="highlight-lines"></div>
  </div>

  <div class="reflection-box">
    <div class="r-label">A Thought I Want to Remember</div>
    <div class="reflection-lines"></div>
  </div>
</div>""" % (pg, pg)


def weekly_review_page():
    pg = pn()
    return """<!-- PAGE %d: Weekly Review -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Weekly Reflection</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="weekly-header">
    <div class="weekly-week-num">Week of: ________________</div>
  </div>

  <div class="weekly-section">
    <div class="weekly-prompt">The best thing that happened this week:</div>
    %s
  </div>

  <div class="weekly-section">
    <div class="weekly-prompt">Something new I discovered or learned:</div>
    %s
  </div>

  <div class="weekly-section">
    <div class="weekly-prompt">Someone I am especially grateful for this week:</div>
    <div class="weekly-lines"></div>
  </div>

  <div class="weekly-section">
    <div class="weekly-prompt">A challenge I faced and what it taught me:</div>
    %s
  </div>

  <div class="weekly-section">
    <div class="weekly-prompt">Three words that describe this week:</div>
    <div class="weekly-lines"></div>
  </div>

  <div style="margin-top: 8px;">
    <div class="weekly-prompt" style="margin-bottom: 6px;">How was your week overall?</div>
    <div class="rating-row">
      <div class="rating-label">Overall satisfaction</div>
      <div class="rating-dots">
        <span class="rating-num">1</span><div class="rating-dot"></div>
        <span class="rating-num">2</span><div class="rating-dot"></div>
        <span class="rating-num">3</span><div class="rating-dot"></div>
        <span class="rating-num">4</span><div class="rating-dot"></div>
        <span class="rating-num">5</span><div class="rating-dot"></div>
      </div>
    </div>
    <div class="rating-row">
      <div class="rating-label">How connected I felt to others</div>
      <div class="rating-dots">
        <span class="rating-num">1</span><div class="rating-dot"></div>
        <span class="rating-num">2</span><div class="rating-dot"></div>
        <span class="rating-num">3</span><div class="rating-dot"></div>
        <span class="rating-num">4</span><div class="rating-dot"></div>
        <span class="rating-num">5</span><div class="rating-dot"></div>
      </div>
    </div>
  </div>

  <div class="reflection-box">
    <div class="r-label">My Intention for Next Week</div>
    <div class="reflection-lines"></div>
  </div>
</div>""" % (pg, pg, wl(2), wl(2), wl(2))


def monthly_review_page():
    pg = pn()
    return """<!-- PAGE %d: Monthly Review -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Monthly Reflection</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="weekly-header">
    <div class="weekly-week-num">Month: ________________</div>
  </div>

  <div class="monthly-grid">
    <div class="monthly-card">
      <div class="mc-label">Biggest Highlight</div>
      <div class="mc-lines"></div>
    </div>
    <div class="monthly-card">
      <div class="mc-label">Hardest Moment</div>
      <div class="mc-lines"></div>
    </div>
    <div class="monthly-card">
      <div class="mc-label">Most Grateful For</div>
      <div class="mc-lines"></div>
    </div>
    <div class="monthly-card">
      <div class="mc-label">Biggest Lesson</div>
      <div class="mc-lines"></div>
    </div>
  </div>

  <div class="weekly-section">
    <div class="weekly-prompt">Top 5 moments from this month:</div>
    %s
  </div>

  <div class="weekly-section">
    <div class="weekly-prompt">People who made this month special:</div>
    %s
  </div>

  <div class="weekly-section">
    <div class="weekly-prompt">How have I grown this month?</div>
    %s
  </div>

  <div class="reflection-box">
    <div class="r-label">One Word to Describe This Month</div>
    <div style="text-align: center; padding-top: 8px;">
      <span style="font-size: 14pt; color: #C4A04A; letter-spacing: 2pt;">________________</span>
    </div>
  </div>
</div>""" % (pg, pg, wl(5), wl(2), wl(2))


def notes_page():
    pg = pn()
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes</span>
    <span class="ph-right">Page %d</span>
  </div>
  <div class="notes-lines">
    %s
  </div>
</div>""" % (pg, pg, nl(26))


def final_page():
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="page">
  <div class="final-page">
    <div class="fp-text">
      May you always find<br>
      something to be grateful for.
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

    # 1. Interior title page
    pages.append(interior_title_page())

    # 2-3. How to use
    pages.append(how_to_use_page_1())
    pages.append(how_to_use_page_2())

    # 4. Goal setting
    pages.append(goal_setting_page())

    # 5. Quote page
    pages.append(quote_page(
        "Gratitude turns what we have into enough.",
        "Aesop"
    ))

    quotes = [
        ("Gratitude is not only the greatest of virtues, but the parent of all others.", "Cicero"),
        ("The roots of all goodness lie in the soil of appreciation for goodness.", "Dalai Lama"),
        ("Enjoy the little things, for one day you may look back and realize they were the big things.", "Robert Brault"),
        ("Gratitude is the fairest blossom which springs from the soul.", "Henry Ward Beecher"),
        ("When we give cheerfully and accept gratefully, everyone is blessed.", "Maya Angelou"),
        ("Gratitude makes sense of our past, brings peace for today, and creates a vision for tomorrow.", "Melody Beattie"),
        ("Acknowledging the good that you already have in your life is the foundation for all abundance.", "Eckhart Tolle"),
        ("The more grateful I am, the more beauty I see.", "Mary Davis"),
        ("Gratitude is riches. Complaint is poverty.", "Doris Day"),
        ("When I started counting my blessings, my whole life turned around.", "Willie Nelson"),
        ("Gratitude is the memory of the heart.", "French Proverb"),
        ("Be thankful for what you have; you will end up having more.", "Oprah Winfrey"),
    ]

    quote_idx = 0

    # 12 weeks: 7 daily + 1 weekly = 96 pages + quotes + monthly reviews
    for week in range(12):
        for _day in range(7):
            pages.append(daily_entry_page())

        pages.append(weekly_review_page())

        if week in [2, 5, 8]:
            q = quotes[quote_idx % len(quotes)]
            pages.append(quote_page(q[0], q[1]))
            quote_idx += 1

        if week in [3, 7, 11]:
            pages.append(monthly_review_page())

    # Notes pages
    for _ in range(3):
        pages.append(notes_page())

    # Final page
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
