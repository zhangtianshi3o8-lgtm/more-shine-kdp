#!/usr/bin/env python3
"""
Dream Journal -- KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Dreamers, lucid dreamers, anyone interested in their subconscious
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "dream_journal_us_V1.0.html")

BOOK_TITLE = "Dream Journal"
BOOK_SUBTITLE = "Capture the Journey of Your Subconscious Mind"

# Accent color: deep lavender
ACCENT = "#8B7D9B"
ACCENT_D = "#6B5D7B"
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
  background: linear-gradient(165deg, #161616 0%, #2A2530 30%, #161616 65%, #0F0A12 100%);
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #8B7D9B, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #8B7D9B, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #8B7D9B, transparent);
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
  background: #8B7D9B;
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
  color: #8B7D9B;
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
  background: #8B7D9B;
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
.howto-text .ht-icon { color: #8B7D9B; font-weight: 700; margin-right: 4px; }

/* ================ INFO FIELDS ================ */
.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
  margin-bottom: 8px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #8B7D9B;
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

/* ================ DREAM BANNER ================ */
.dream-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1.5px solid #8B7D9B;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.dream-banner .db-num {
  display: inline-block;
  border: 1.5px solid #8B7D9B;
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 8pt;
  color: #8B7D9B;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.dream-banner .db-label {
  font-size: 8pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.dream-banner .db-line {
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
  border: 1.5px solid #8B7D9B;
  border-radius: 2px;
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
  color: #8B7D9B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 3px;
}

.write-box .wb-area {
  height: 28px;
}

/* ================ EMOTION SCALE ================ */
.emotion-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  padding: 6px 8px;
  border: 1px solid #ddd;
  border-radius: 3px;
}

.emotion-label {
  font-size: 7pt;
  color: #8B7D9B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
}

.emotion-dots {
  display: flex;
  gap: 8px;
}

.emotion-dot {
  width: 16px; height: 16px;
  border: 1.5px solid #8B7D9B;
  border-radius: 50%;
  position: relative;
}

.emotion-dot::after {
  content: attr(data-num);
  position: absolute;
  top: -14px; left: 50%;
  transform: translateX(-50%);
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
  width: 60px; height: 1.5px; background: #8B7D9B;
  margin: 12px auto; opacity: 0.5;
}
"""


def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- Crescent moon + star (minimal line art) -->
      <g transform="translate(50,50)">
        <!-- Crescent moon -->
        <path d="M -5,-30 A 30,30 0 1,0 -5,30 A 22,22 0 1,1 -5,-30 Z"
              fill="none" stroke="#8B7D9B" stroke-width="2" stroke-linejoin="round"/>
        <!-- Small star -->
        <path d="M 20,-15 L 22,-10 L 27,-9 L 23,-5 L 24,0 L 20,-2 L 16,0 L 17,-5 L 13,-9 L 18,-10 Z"
              fill="none" stroke="#C4A04A" stroke-width="1.2" stroke-linejoin="round"/>
        <!-- Tiny stars -->
        <circle cx="28" cy="12" r="1.2" fill="#C4A04A" opacity="0.7"/>
        <circle cx="-22" cy="-18" r="1" fill="#8B7D9B" opacity="0.5"/>
        <circle cx="15" cy="22" r="0.8" fill="#8B7D9B" opacity="0.4"/>
      </g>
    </svg>
  </div>

  <div class="title-main">Dream<br>Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Capture the Journey of<br>Your Subconscious Mind</div>

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
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Why Record Your Dreams</div>
    <p>Dreams are windows into the subconscious. By writing them down
    consistently, you begin to notice patterns, symbols, and themes that
    reveal your inner world. Over time, you may even improve your dream
    recall and experience lucid dreams.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Two-Page Dream Spread</div>
    <p>Each dream uses a <strong>two-page spread</strong>. The left page
    captures the essentials: date, dream title, mood, lucidity level, and
    type. The right page is for the full narrative -- write everything you
    remember, in any order. Do not worry about grammar or logic.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips for Better Recall</div>
    <p>&#9679; <strong>Write immediately.</strong> Keep this journal by your
    bed. The moment you wake, write -- dreams fade within minutes.</p>
    <p>&#9679; <strong>Stay still.</strong> Do not move or check your phone
    first. Lie still and let the dream come back to you.</p>
    <p>&#9679; <strong>Note emotions.</strong> Feelings are the strongest
    anchor for dream memory. Record them first if details are fuzzy.</p>
    <p>&#9679; <strong>Look for symbols.</strong> Recurring people, places,
    and objects often carry personal meaning.</p>
  </div>
</div>""" % (pg, pg)


def dream_symbols_page():
    pg = pn()
    return """<!-- PAGE %d: Dream Symbols Guide -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Common Dream Symbols</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Symbol Reference</div>
    <div class="section-line"></div>
  </div>

  <div class="howto-text" style="font-size: 9pt; line-height: 1.6;">
    <p style="margin-bottom: 6px;"><strong>Flying</strong> -- Freedom,
    ambition, or a desire to escape limitations.</p>
    <p style="margin-bottom: 6px;"><strong>Falling</strong> -- Loss of
    control, anxiety, or fear of failure.</p>
    <p style="margin-bottom: 6px;"><strong>Water</strong> -- Emotions and
    the subconscious. Still water reflects peace; rough water reflects
    turmoil.</p>
    <p style="margin-bottom: 6px;"><strong>Being chased</strong> -- Avoiding
    a fear or confronting an unresolved issue.</p>
    <p style="margin-bottom: 6px;"><strong>Teeth falling out</strong> --
    Anxiety about appearance, communication, or major life changes.</p>
    <p style="margin-bottom: 6px;"><strong>House</strong> -- The self.
    Different rooms represent different aspects of your mind.</p>
    <p style="margin-bottom: 6px;"><strong>Animals</strong> -- Instincts
    and primal emotions. The type of animal matters.</p>
    <p style="margin-bottom: 6px;"><strong>Death</strong> -- Transformation
    and endings, rarely literal. Often signals a new beginning.</p>
    <p style="margin-bottom: 6px;"><strong>Babies</strong> -- New ideas,
    projects, or a fresh start in life.</p>
    <p style="margin-bottom: 6px;"><strong>Mirror</strong> --
    Self-reflection and how you see yourself.</p>
    <p style="margin-bottom: 6px;"><strong>Fire</strong> -- Passion,
    destruction, or purification. Context is everything.</p>
    <p style="margin-bottom: 6px;"><strong>Door</strong> -- New
    opportunities or transitions. An open door invites; a closed one
    blocks.</p>
  </div>

  <div class="write-box" style="border-color: #8B7D9B; margin-top: 10px;">
    <div class="wb-label">Your Personal Symbols (recurring themes in your dreams)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>
</div>""" % (pg, pg)


def dream_left(entry_num):
    pg = pn()
    dream_types = ["Vivid", "Lucid", "Recurring", "Nightmare", "Prophetic",
                   "Fragment", "Epic", "Healing"]
    type_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % t
        for t in dream_types
    )
    return """<!-- PAGE %d: Dream Left #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Dream Record</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="dream-banner">
    <span class="db-num">Dream #%03d</span>
    <span class="db-label">Title:</span>
    <div class="db-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Day of Week</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Wake Time</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Hours Slept</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #8B7D9B; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Dream Type</div>
  <div class="type-row">%s</div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Mood Upon Waking</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Lucidity Level (0-5)</span><div class="if-write"></div></div>
  </div>

  <div class="emotion-row">
    <span class="emotion-label">Clarity</span>
    <div class="emotion-dots">
      <span class="emotion-dot" data-num="1"></span>
      <span class="emotion-dot" data-num="2"></span>
      <span class="emotion-dot" data-num="3"></span>
      <span class="emotion-dot" data-num="4"></span>
      <span class="emotion-dot" data-num="5"></span>
    </div>
  </div>

  <div class="emotion-row">
    <span class="emotion-label">Emotion Intensity</span>
    <div class="emotion-dots">
      <span class="emotion-dot" data-num="1"></span>
      <span class="emotion-dot" data-num="2"></span>
      <span class="emotion-dot" data-num="3"></span>
      <span class="emotion-dot" data-num="4"></span>
      <span class="emotion-dot" data-num="5"></span>
    </div>
  </div>

  <div class="write-box">
    <div class="wb-label">Key Symbols / People / Places</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #8B7D9B;">
    <div class="wb-label">Emotions Felt in Dream</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, entry_num, pg, entry_num, type_html)


def dream_right():
    pg = pn()
    return """<!-- PAGE %d: Dream Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Dream Narrative</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="write-box" style="border-color: #8B7D9B; height: 430px; overflow: hidden;">
    <div class="wb-label">Write Everything You Remember</div>
    <div style="margin-top: 4px;">%s</div>
  </div>

  <div class="write-box">
    <div class="wb-label">Possible Meaning / Interpretation</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #8B7D9B;">
    <div class="wb-label">Connection to Waking Life</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg, nl(14))


def weekly_review_page(review_num):
    pg = pn()
    return """<!-- PAGE %d: Weekly Review #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Weekly Review</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Review #%d</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Week Of</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Dreams Recorded</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Lucid Dreams</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Recurring Themes</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #8B7D9B;">
    <div class="wb-label">Most Vivid Dream This Week</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Recurring Symbols or People</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #8B7D9B;">
    <div class="wb-label">Emotional Themes (What dominated your dream world?)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Connection to Waking Life Events</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #8B7D9B;">
    <div class="wb-label">Patterns Emerging / Insights</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>
</div>""" % (pg, review_num, pg, review_num)


def lucid_progress_page():
    pg = pn()
    return """<!-- PAGE %d: Lucid Dreaming Progress -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Lucid Dreaming Progress</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Reality Checks</div>
    <div class="section-line"></div>
  </div>

  <div class="howto-text" style="font-size: 9pt; line-height: 1.6;">
    <p style="margin-bottom: 6px;"><strong>Reality checks</strong> are habits
    you practice while awake that eventually carry into dreams. When the
    check fails in a dream, you realize you are dreaming.</p>
    <p style="margin-bottom: 4px;">&#9679; <strong>Nose pinch:</strong> Pinch
    your nose shut and try to breathe. In a dream, you will still breathe.</p>
    <p style="margin-bottom: 4px;">&#9679; <strong>Hand check:</strong> Look at
    your hands. In dreams, fingers often appear distorted or extra.</p>
    <p style="margin-bottom: 4px;">&#9679; <strong>Text test:</strong> Read
    text, look away, read again. In dreams, text changes.</p>
    <p style="margin-bottom: 4px;">&#9679; <strong>Light switch:</strong>
    Flip a switch. In dreams, lights often do not respond.</p>
  </div>

  <div class="write-box" style="border-color: #8B7D9B; margin-top: 8px;">
    <div class="wb-label">Reality Check Log (mark each day you practiced)</div>
    <div style="margin-top: 4px;">
      <table style="width: 100%%; font-size: 7.5pt; border-collapse: collapse;">
        <tr style="border-bottom: 1px solid #ddd;">
          <td style="padding: 4px; font-weight: 700; color: #8B7D9B;">Week</td>
          <td style="padding: 4px; text-align: center;">M</td>
          <td style="padding: 4px; text-align: center;">T</td>
          <td style="padding: 4px; text-align: center;">W</td>
          <td style="padding: 4px; text-align: center;">T</td>
          <td style="padding: 4px; text-align: center;">F</td>
          <td style="padding: 4px; text-align: center;">S</td>
          <td style="padding: 4px; text-align: center;">S</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee; height: 20px;">
          <td style="padding: 4px; font-size: 7pt; color: #999;">1</td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td>
        </tr>
        <tr style="border-bottom: 1px solid #eee; height: 20px;">
          <td style="padding: 4px; font-size: 7pt; color: #999;">2</td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td>
        </tr>
        <tr style="border-bottom: 1px solid #eee; height: 20px;">
          <td style="padding: 4px; font-size: 7pt; color: #999;">3</td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td>
        </tr>
        <tr style="border-bottom: 1px solid #eee; height: 20px;">
          <td style="padding: 4px; font-size: 7pt; color: #999;">4</td>
          <td></td><td></td><td></td><td></td><td></td><td></td><td></td>
        </tr>
      </table>
    </div>
  </div>

  <div class="write-box">
    <div class="wb-label">Lucid Dream Triggers (what made you realize you were dreaming?)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #8B7D9B;">
    <div class="wb-label">Techniques Tried (WBTB, MILD, WILD, DILD, etc.)</div>
    <div class="wb-area"></div>
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

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Month in Review</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Month</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Total Dreams Recorded</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Lucid Dreams</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Nightmares</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Recurring Dreams</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Most Common Emotion</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #8B7D9B;">
    <div class="wb-label">Top 3 Most Memorable Dreams</div>
    <div class="wb-area" style="height: 44px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Recurring Symbols This Month</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #8B7D9B;">
    <div class="wb-label">Patterns or Themes Noticed</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Dream Recall Improvement (easier than last month?)</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #8B7D9B;">
    <div class="wb-label">Goal for Next Month</div>
    <div class="wb-area"></div>
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
      Every dream is a message from within.<br>
      Listen to them.<br>
      Write them down.
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
    pages.append(dream_symbols_page())

    # 25 dream spreads (50 pages), with a weekly review every 5 dreams
    dream_count = 0
    review_count = 0
    for entry in range(1, 26):
        pages.append(dream_left(entry))
        pages.append(dream_right())
        dream_count += 1
        if dream_count % 5 == 0:
            review_count += 1
            pages.append(weekly_review_page(review_count))

    # Lucid dreaming progress (2 pages)
    pages.append(lucid_progress_page())
    pages.append(lucid_progress_page())

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
