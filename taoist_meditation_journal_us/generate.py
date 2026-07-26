#!/usr/bin/env python3
"""
The Taoist Meditation Journal -- KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Meditation practitioners drawn to Taoist philosophy
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "taoist_meditation_journal_us_V1.0.html")

BOOK_TITLE = "The Taoist Meditation Journal"
BOOK_SUBTITLE = "Cultivate Stillness, Follow the Way"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

def nl(n):
    return "\n".join('<div class="notes-line"></div>' for _ in range(n))

from tao_quotes import TAO_QUOTES  # Shared 30-quote list (chapter, english, chinese)

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
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #C4A04A, transparent);
}

.cover .taiji {
  position: relative; z-index: 2;
  margin-bottom: 20px;
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
  width: 100px; height: 2px;
  background: #C4A04A;
  margin: 20px auto;
  position: relative;
  z-index: 2;
}

.cover .subtitle {
  font-size: 12pt;
  color: #D4B896;
  line-height: 1.5;
  position: relative;
  z-index: 2;
}

.cover .pub {
  font-size: 8.5pt;
  color: #888;
  letter-spacing: 2pt;
  text-transform: uppercase;
  margin-top: 50px;
  position: relative;
  z-index: 2;
}

/* ================ PAGE HEADER ================ */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  border-bottom: 1.5px solid #C4A04A;
  padding-bottom: 5px;
  margin-bottom: 12px;
}

.ph-left {
  font-size: 10pt;
  font-weight: 700;
  color: #333;
  letter-spacing: 0.3pt;
}

.ph-right {
  font-size: 7.5pt;
  color: #999;
}

/* ================ HOW TO USE ================ */
.howto-text {
  font-size: 9pt;
  line-height: 1.7;
  color: #444;
}

.howto-text .ht-title {
  font-size: 12pt;
  font-weight: 700;
  color: #333;
  margin-bottom: 8px;
}

.howto-text p { margin-bottom: 8px; }

.howto-text .ht-section {
  margin-bottom: 12px;
}

.howto-text .ht-heading {
  font-size: 9.5pt;
  font-weight: 700;
  color: #C4A04A;
  margin-bottom: 4px;
}

/* ================ QUOTE BOX ================ */
.quote-box {
  border: 1px solid #C4A04A;
  border-radius: 4px;
  padding: 10px 14px;
  margin-bottom: 10px;
  background: #FFFCF5;
  text-align: center;
}

.quote-box .qb-text {
  font-size: 9pt;
  font-style: italic;
  color: #555;
  line-height: 1.5;
}

.quote-box .qb-source {
  font-size: 7pt;
  color: #999;
  margin-top: 4px;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

/* ================ SESSION BANNER ================ */
.session-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
}

.session-banner .sb-num {
  font-size: 13pt;
  font-weight: 700;
  color: #C4A04A;
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

/* ================ INFO ROW ================ */
.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 6px 10px;
  margin-bottom: 10px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  display: block;
  margin-bottom: 1px;
}

.info-field .if-write {
  height: 18px;
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
  border: 1.5px solid #C4A04A;
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
  color: #C4A04A;
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
  color: #C4A04A;
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
  border: 1.5px solid #C4A04A;
  border-radius: 50%;
}

/* ================ NOTES ================ */
.notes-line { border-bottom: 1px solid #ddd; height: 22px; }

/* ================ TWO-COLUMN ================ */
.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px 14px;
}

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
  width: 60px; height: 1.5px; background: #C4A04A;
  margin: 12px auto; opacity: 0.5;
}

/* ================ REFERENCE PAGE ================ */
.ref-section {
  margin-bottom: 14px;
}

.ref-title {
  font-size: 11pt;
  font-weight: 700;
  color: #333;
  border-bottom: 1px solid #C4A04A;
  padding-bottom: 3px;
  margin-bottom: 6px;
}

.ref-text {
  font-size: 8.5pt;
  line-height: 1.6;
  color: #555;
}

.ref-text strong { color: #333; }

/* ================ WEEKLY REFLECTION ================ */
.weekly-banner {
  font-size: 11pt;
  font-weight: 700;
  color: #C4A04A;
  border-bottom: 1px solid #ddd;
  padding-bottom: 4px;
  margin-bottom: 10px;
}

/* ================ MEDITATION TYPES REFERENCE ================ */
.med-type {
  margin-bottom: 6px;
}

.med-type .mt-name {
  font-size: 8.5pt;
  font-weight: 700;
  color: #333;
}

.med-type .mt-desc {
  font-size: 7.5pt;
  color: #777;
  line-height: 1.4;
}
"""


# ============================================================
# PAGE GENERATORS
# ============================================================

def taiji_svg(size=90):
    """Taiji (yin-yang) symbol outline in gold."""
    return f'''<svg viewBox="0 0 100 100" width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="tjclip">
      <circle cx="50" cy="50" r="48"/>
    </clipPath>
  </defs>
  <g clip-path="url(#tjclip)">
    <circle cx="50" cy="50" r="48" fill="none" stroke="#C4A04A" stroke-width="1.5"/>
    <path d="M50,2 A24,24 0 0,1 50,50 A24,24 0 0,0 50,98 A48,48 0 0,1 50,2 Z" fill="#C4A04A" opacity="0.12"/>
    <path d="M50,2 A48,48 0 0,1 50,98 A24,24 0 0,1 50,50 A24,24 0 0,0 50,2 Z" fill="none" stroke="#C4A04A" stroke-width="1.2"/>
    <circle cx="50" cy="26" r="6.5" fill="none" stroke="#C4A04A" stroke-width="1"/>
    <circle cx="50" cy="74" r="6.5" fill="none" stroke="#C4A04A" stroke-width="1"/>
    <circle cx="50" cy="26" r="2" fill="#C4A04A" opacity="0.4"/>
    <circle cx="50" cy="74" r="2" fill="#C4A04A"/>
  </g>
</svg>'''


def interior_title_page():
    return f'''
<!-- PAGE 1: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div class="taiji">{taiji_svg(95)}</div>

  <div class="title-main">The Taoist<br>Meditation<br>Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Cultivate Stillness,<br>Follow the Way</div>

  <div class="pub">More Shine Press</div>
</div>'''


def how_to_use_page():
    return f'''
<!-- PAGE 2: How to Use -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">How to Use This Journal</span>
    <span class="ph-right">Page {pn()}</span>
  </div>

  <div class="howto-text">
    <div class="ht-title">&#9758; Cultivating the Way</div>

    <p>For over two thousand years, Taoist meditation has offered a
    path to inner stillness, harmony with nature, and a deeper
    understanding of the self. This journal is your companion on
    that path -- a place to record, reflect, and grow.</p>

    <div class="ht-section">
      <div class="ht-heading">The Two-Page Practice Spread</div>
      <p>Each session uses a clean two-page spread. The left page
      captures the essentials: date, practice type, duration,
      posture, and setting. The right page holds your inner
      experience: breath observations, sensations, emotions,
      insights, and a Tao wisdom passage to contemplate.</p>
    </div>

    <div class="ht-section">
      <div class="ht-heading">Practice Types</div>
      <p>This journal supports several core Taoist meditation
      practices: Zuowang (sitting in forgetfulness), Guan (inner
      observation), Zuochan (sitting meditation), Breathing
      practice, Inner smile, and Moving meditation. A reference
      guide on the next pages explains each one.</p>
    </div>

    <div class="ht-section">
      <div class="ht-heading">Five-Session Rhythm</div>
      <p>After every five sessions, a reflection page helps you
      review your progress, notice patterns, and deepen your
      practice. Use these moments to celebrate growth and adjust
      your approach.</p>
    </div>

    <p style="margin-top: 14px; font-style: italic; color: #888;
    text-align: center; border-top: 1px solid #eee; padding-top: 8px;">
    The Tao that can be told is not the eternal Tao.<br>
    The name that can be named is not the eternal name.</p>
  </div>
</div>'''


def meditation_types_ref():
    """Two reference pages on Taoist meditation types."""
    types = [
        ("Zuowang &#8212; Sitting in Forgetfulness",
         "The signature Taoist practice of 'sitting and forgetting.' Sit comfortably, close your eyes, and let go of all concepts, identities, and thoughts. Do not resist them -- simply let them pass like clouds. Rest in open awareness."),
        ("Guan &#8212; Inner Observation",
         "A practice of inward seeing. Turn your attention gently inward to observe the body, breath, and mind without judgment. Notice what is present. Cultivate the quality of a mirror: reflecting without holding."),
        ("Zuochan &#8212; Still Sitting",
         "The foundational sitting practice. Sit with spine upright, shoulders relaxed, eyes half-closed. Place hands in your lap. Focus on the natural rhythm of breath. When the mind wanders, return."),
        ("Breathing Practice &#8212; Tu Na",
         "The ancient art of expelling the old and drawing in the new. Breathe slowly and deeply from the abdomen. On each exhale, release tension. On each inhale, gather fresh energy. Let the breath be soft, long, and deep."),
        ("Inner Smile",
         "A practice of cultivating inner warmth and kindness. Smile inwardly to each part of your body, beginning with the face, then moving down to the organs. This practice dissolves tension and gathers energy."),
        ("Moving Meditation",
         "Tai Chi, Qigong, and mindful walking. Movement becomes meditation when done with full awareness, soft breath, and a settled mind. Practice slow, circular motions that follow the natural flow of energy."),
    ]

    html = '<!-- PAGE 3: Meditation Types Reference -->\n'
    html += f'''<div class="page">
  <div class="page-header">
    <span class="ph-left">Taoist Meditation Practices</span>
    <span class="ph-right">Page {pn()}</span>
  </div>'''
    for name, desc in types[:3]:
        html += f'''
  <div class="med-type">
    <div class="mt-name">{name}</div>
    <div class="mt-desc">{desc}</div>
  </div>'''
    html += '\n</div>'

    html += '\n<!-- PAGE 4: Meditation Types Reference (cont.) -->\n'
    html += f'''<div class="page">
  <div class="page-header">
    <span class="ph-left">Taoist Meditation Practices (cont.)</span>
    <span class="ph-right">Page {pn()}</span>
  </div>'''
    for name, desc in types[3:]:
        html += f'''
  <div class="med-type">
    <div class="mt-name">{name}</div>
    <div class="mt-desc">{desc}</div>
  </div>'''

    html += f'''
  <div class="quote-box" style="margin-top: 10px;">
    <div class="qb-text">Empty your mind of all thoughts.<br>Let your heart be at peace.<br>Watch the turmoil of beings, but contemplate their return.</div>
    <div class="qb-source">Tao Te Ching, Chapter 16</div>
  </div>
</div>'''
    return html


def intention_page():
    return f'''
<!-- PAGE 5: Intention Setting -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Setting Your Intention</span>
    <span class="ph-right">Page {pn()}</span>
  </div>

  <div class="howto-text" style="margin-bottom: 12px;">
    <div class="ht-heading" style="color: #333; font-size: 10pt;">Begin with the End in Mind</div>
    <p style="font-size: 8.5pt; color: #777;">Before you start, take a moment to define
    what draws you to this practice. What do you hope to cultivate?
    What does "the Way" mean to you right now?</p>
  </div>

  <div class="write-box" style="height: auto;">
    <div class="wb-label">My Primary Intention for This Practice</div>
    <div class="wb-area" style="height: 50px;"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field">
      <span class="mf-label">Sessions per Week</span>
      <div class="mf-write"></div>
    </div>
    <div class="metric-field">
      <span class="mf-label">Target Duration</span>
      <div class="mf-write"></div>
    </div>
    <div class="metric-field">
      <span class="mf-label">Preferred Time</span>
      <div class="mf-write"></div>
    </div>
  </div>

  <div class="write-box">
    <div class="wb-label">Areas I Wish to Cultivate</div>
    <div class="type-row">
      <span class="type-check"><span class="type-box"></span>Stillness</span>
      <span class="type-check"><span class="type-box"></span>Presence</span>
      <span class="type-check"><span class="type-box"></span>Letting Go</span>
      <span class="type-check"><span class="type-box"></span>Energy Flow</span>
      <span class="type-check"><span class="type-box"></span>Emotional Balance</span>
      <span class="type-check"><span class="type-box"></span>Self-Knowledge</span>
      <span class="type-check"><span class="type-box"></span>Simplicity</span>
      <span class="type-check"><span class="type-box"></span>Compassion</span>
      <span class="type-check"><span class="type-box"></span>Nature Connection</span>
      <span class="type-check"><span class="type-box"></span>Inner Harmony</span>
    </div>
  </div>

  <div class="write-box" style="height: auto;">
    <div class="wb-label">What I Want to Release</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box" style="height: auto; border-color: #C4A04A;">
    <div class="wb-label">A Tao Wisdom to Guide Me</div>
    <div class="quote-box" style="border: none; padding: 6px 0; margin: 0; background: none; text-align: left;">
      <div class="qb-text" style="font-size: 9pt;">"A journey of a thousand miles begins beneath your feet."</div>
      <div class="qb-source" style="text-align: left;">Tao Te Ching, Chapter 64</div>
    </div>
  </div>
</div>'''


def practice_log_left(session_num, quote_text, quote_ch):
    """Left page of the two-page practice spread."""
    return f'''
<!-- Practice Log Left -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Practice Log</span>
    <span class="ph-right">Page {pn()}</span>
  </div>

  <div class="session-banner">
    <span class="sb-num">Session #{session_num:03d}</span>
    <span class="sb-label">Date:</span>
    <div class="sb-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Day of Week</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Duration (min)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Time of Day</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Practice Type</div>
  <div class="type-row">
    <span class="type-check"><span class="type-box"></span>Zuowang</span>
    <span class="type-check"><span class="type-box"></span>Guan</span>
    <span class="type-check"><span class="type-box"></span>Zuochan</span>
    <span class="type-check"><span class="type-box"></span>Breathing</span>
    <span class="type-check"><span class="type-box"></span>Inner Smile</span>
    <span class="type-check"><span class="type-box"></span>Moving Meditation</span>
    <span class="type-check"><span class="type-box"></span>Other</span>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 12px; margin-bottom: 8px;">
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Posture</div>
      <div class="type-row" style="margin-bottom: 0;">
        <span class="type-check"><span class="type-box"></span>Sitting</span>
        <span class="type-check"><span class="type-box"></span>Standing</span>
        <span class="type-check"><span class="type-box"></span>Lying</span>
        <span class="type-check"><span class="type-box"></span>Moving</span>
      </div>
    </div>
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Setting</div>
      <div class="type-row" style="margin-bottom: 0;">
        <span class="type-check"><span class="type-box"></span>Indoors</span>
        <span class="type-check"><span class="type-box"></span>Outdoors</span>
        <span class="type-check"><span class="type-box"></span>Altar Space</span>
      </div>
    </div>
  </div>

  <div class="write-box" style="border-color: #C4A04A;">
    <div class="wb-label">How I Felt Before Practice</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Setting the Scene (Candle, Incense, Music, Position)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Breath Observation (Rhythm, Depth, Quality)</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>
</div>'''


def practice_reflection_right(session_num, quote_text, quote_ch):
    """Right page of the two-page practice spread."""
    src = f"Tao Te Ching, Chapter {quote_ch}" if isinstance(quote_ch, int) else "Tao Wisdom"
    return f'''
<!-- Practice Reflection Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Practice Reflection</span>
    <span class="ph-right">Page {pn()}</span>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px 12px; margin-top: 4px; margin-bottom: 8px;">
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Stillness (1-5)</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Restless &#160; 5 = Deep Stillness</div>
    </div>
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Energy (1-5)</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Depleted &#160; 5 = Vibrant Qi</div>
    </div>
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Mental Clarity (1-5)</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Foggy &#160; 5 = Crystal Clear</div>
    </div>
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Body Relaxation (1-5)</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Tense &#160; 5 = Fully Relaxed</div>
    </div>
  </div>

  <div class="write-box">
    <div class="wb-label">Sensations &amp; Body Observations</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Emotions That Arose</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Insights &amp; Intuitive Knowing</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #C4A04A;">
    <div class="wb-label">How I Felt After Practice</div>
    <div class="wb-area"></div>
  </div>

  <div class="quote-box">
    <div class="qb-text">"{quote_text}"</div>
    <div class="qb-source">{src}</div>
  </div>
</div>'''


def weekly_reflection(week_num):
    return f'''
<!-- Weekly Reflection -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Weekly Reflection</span>
    <span class="ph-right">Page {pn()}</span>
  </div>

  <div class="weekly-banner">Week {week_num} &#8212; Looking Back, Looking Forward</div>

  <div class="metric-row">
    <div class="metric-field">
      <span class="mf-label">Sessions Completed</span>
      <div class="mf-write"></div>
    </div>
    <div class="metric-field">
      <span class="mf-label">Total Time (min)</span>
      <div class="mf-write"></div>
    </div>
    <div class="metric-field">
      <span class="mf-label">Avg. Stillness (1-5)</span>
      <div class="mf-write"></div>
    </div>
  </div>

  <div class="write-box" style="height: auto;">
    <div class="wb-label">What Worked Well This Week</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="height: auto;">
    <div class="wb-label">Challenges or Resistance</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="height: auto;">
    <div class="wb-label">Most Significant Moment or Insight</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box" style="height: auto;">
    <div class="wb-label">What I Want to Cultivate Next Week</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="quote-box">
    <div class="qb-text">"Do you have the patience to wait until your mud settles and the water is clear?"</div>
    <div class="qb-source">Tao Te Ching, Chapter 15</div>
  </div>
</div>'''


def tao_wisdom_ref_pages():
    """Two pages of curated Tao Te Ching wisdom for contemplation."""
    passages = [
        (1, "The Tao that can be told is not the eternal Tao. The name that can be named is not the eternal name. The nameless is the beginning of heaven and earth. The named is the mother of ten thousand things."),
        (8, "The highest good is like water. Water gives life to the ten thousand things and does not strive. It flows in places people reject and so is like the Tao."),
        (11, "Thirty spokes share the center of a wheel. Use the emptiness inside to make it useful. A cup is shaped from clay. Use the emptiness inside to make it useful. A house is built with walls. Use the emptiness inside to make it useful."),
        (16, "Empty yourself of everything. Let the mind rest at peace. The ten thousand things rise and fall while the Self watches their return."),
        (22, "Yield and overcome. Bend and be straight. Empty and be full. Wear out and be new. Have little and gain. Have much and be confused."),
        (33, "Knowing others is intelligence. Knowing yourself is true wisdom. Mastering others is strength. Mastering yourself is true power."),
        (40, "Returning is the motion of the Tao. Yielding is the way of the Tao. The ten thousand things are born of being. Being is born of non-being."),
        (47, "Without going outside your door, you can know the ways of the world. Without peeping through your window, you can see the Tao of heaven."),
        (63, "Act without doing. Work without effort. Think of the small as large and the few as many. Confront the difficult while it is easy."),
        (76, "When people are born they are soft and weak. When they die they are stiff and hard. All things, including the grass and trees, are soft and pliable in life and dry and brittle in death."),
    ]

    html = '<!-- Tao Wisdom Reference Page 1 -->\n'
    html += f'''<div class="page">
  <div class="page-header">
    <span class="ph-left">Tao Wisdom for Contemplation</span>
    <span class="ph-right">Page {pn()}</span>
  </div>'''
    for ch, text in passages[:5]:
        html += f'''
  <div class="quote-box" style="text-align: left; margin-bottom: 8px;">
    <div class="qb-text" style="text-align: left;">{text}</div>
    <div class="qb-source" style="text-align: left;">Tao Te Ching, Chapter {ch}</div>
  </div>'''
    html += '\n</div>'

    html += '\n<!-- Tao Wisdom Reference Page 2 -->\n'
    html += f'''<div class="page">
  <div class="page-header">
    <span class="ph-left">Tao Wisdom for Contemplation (cont.)</span>
    <span class="ph-right">Page {pn()}</span>
  </div>'''
    for ch, text in passages[5:]:
        html += f'''
  <div class="quote-box" style="text-align: left; margin-bottom: 8px;">
    <div class="qb-text" style="text-align: left;">{text}</div>
    <div class="qb-source" style="text-align: left;">Tao Te Ching, Chapter {ch}</div>
  </div>'''
    html += '\n</div>'
    return html


def final_page():
    return f'''
<!-- FINAL PAGE -->
<div class="page">
  <div class="final-page">
    <div class="fp-text">The Tao does nothing,<br>yet nothing is left undone.</div>
    <div class="fp-line"></div>
    <div class="fp-logo">More Shine Press</div>
  </div>
</div>'''


# ============================================================
# BUILD THE BOOK
# ============================================================

def build():
    pages = []
    pages.append('<!DOCTYPE html>')
    pages.append('<html lang="en"><head>')
    pages.append('<meta charset="UTF-8">')
    pages.append(f'<title>{BOOK_TITLE}</title>')
    pages.append(f'<style>{CSS}</style>')
    pages.append('</head><body>')

    # Page 1: Interior title
    pages.append(interior_title_page())

    # Page 2: How to Use
    pages.append(how_to_use_page())

    # Pages 3-4: Meditation types reference
    pages.append(meditation_types_ref())

    # Page 5: Intention setting
    pages.append(intention_page())

    # 30 two-page practice spreads (60 pages) with weekly reflections every 5
    session = 0
    week = 0
    quote_idx = 0
    for i in range(30):
        session += 1
        q_ch, q_text = TAO_QUOTES[quote_idx % len(TAO_QUOTES)][0], TAO_QUOTES[quote_idx % len(TAO_QUOTES)][1]
        quote_idx += 1
        pages.append(practice_log_left(session, q_text, q_ch))
        pages.append(practice_reflection_right(session, q_text, q_ch))

        # Weekly reflection after every 5 sessions
        if session % 5 == 0 and session < 30:
            week += 1
            pages.append(weekly_reflection(week))

    # Tao wisdom reference pages
    pages.append(tao_wisdom_ref_pages())

    # Final page
    pages.append(final_page())

    pages.append('</body></html>')

    html_content = "\n".join(pages)
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)

    total_pages = page_no[0] + 2  # +1 interior title (no pn), +1 final page (no pn)
    print(f"Generated: {HTML_FILE}")
    print(f"Total pages: {total_pages}")
    print(f"  Interior title: 1")
    print(f"  How to Use: 1")
    print(f"  Meditation types ref: 2")
    print(f"  Intention setting: 1")
    print(f"  Practice spreads: 30 x 2 = 60")
    print(f"  Weekly reflections: 5")
    print(f"  Tao wisdom ref: 2")
    print(f"  Final page: 1")


if __name__ == "__main__":
    build()
