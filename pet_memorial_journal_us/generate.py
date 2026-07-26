#!/usr/bin/env python3
"""
Pet Memorial Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Pet owners grieving the loss of a beloved pet
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "pet_memorial_journal_us_V1.0.html")

BOOK_TITLE = "In Loving Memory of My Pet"
BOOK_SUBTITLE = "A Memorial Journal and Keepsake"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

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

/* ---- Colors ---- */
/* Charcoal-warm: #0F1A18, #16261F */
/* Deep brown-charcoal: #1A2E26 */
/* Gold accent: #8FA8A0 */
/* Warm cream: #F6FAF8, #EAF0EC */
/* Soft mauve: #7A9B8E */
/* Text: #2A2A2A */

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

/* ================ COVER (INTERIOR TITLE PAGE) ================ */
.cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(165deg, #0F1A18 0%, #16261F 30%, #0F1A18 65%, #080C0B 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Gold glow background */
.cover .glow-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #8FA8A0, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #8FA8A0, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #7A9B8E, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #8FA8A0, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #7A9B8E, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #8FA8A0, transparent),
    radial-gradient(ellipse 18px 11px at 90% 40%, #7A9B8E, transparent),
    radial-gradient(ellipse 16px 10px at 40% 90%, #8FA8A0, transparent);
}

/* ===== CSS Pet Silhouette ===== */
.cover .pet-wrap {
  width: 140px; height: 120px;
  position: relative;
  margin: 0 auto 24px;
}

/* Pet head — circle */
.cover .pet-head {
  width: 72px; height: 72px;
  position: absolute;
  top: 30px; left: 34px;
  background: linear-gradient(160deg,
    rgba(250,246,240,0.08) 0%,
    rgba(250,246,240,0.03) 40%,
    rgba(196,160,74,0.04) 80%,
    rgba(15,15,15,0.06) 100%);
  border-radius: 50%;
  border: 1.5px solid rgba(196,160,74,0.35);
}

/* Left ear — triangle */
.cover .pet-ear-l {
  width: 0; height: 0;
  position: absolute;
  top: 18px; left: 36px;
  border-left: 14px solid transparent;
  border-right: 14px solid transparent;
  border-bottom: 24px solid transparent;
  /* Use pseudo approach instead */
}

/* Left ear using clip-path */
.cover .pet-ear-left {
  width: 22px; height: 26px;
  position: absolute;
  top: 14px; left: 32px;
  background: linear-gradient(160deg,
    rgba(250,246,240,0.06) 0%,
    rgba(250,246,240,0.02) 100%);
  border-left: 1.5px solid rgba(196,160,74,0.35);
  clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
}

/* Right ear using clip-path */
.cover .pet-ear-right {
  width: 22px; height: 26px;
  position: absolute;
  top: 14px; left: 86px;
  background: linear-gradient(160deg,
    rgba(250,246,240,0.06) 0%,
    rgba(250,246,240,0.02) 100%);
  border-right: 1.5px solid rgba(196,160,74,0.35);
  clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
}

/* Whisker lines (left) */
.cover .whisker-ll {
  width: 20px; height: 1px;
  position: absolute;
  top: 62px; left: 14px;
  background: rgba(196,160,74,0.3);
}
.cover .whisker-l2 {
  width: 20px; height: 1px;
  position: absolute;
  top: 67px; left: 14px;
  background: rgba(196,160,74,0.25);
}

/* Whisker lines (right) */
.cover .whisker-rl {
  width: 20px; height: 1px;
  position: absolute;
  top: 62px; left: 106px;
  background: rgba(196,160,74,0.3);
}
.cover .whisker-r2 {
  width: 20px; height: 1px;
  position: absolute;
  top: 67px; left: 106px;
  background: rgba(196,160,74,0.25);
}

/* Heart above pet */
.cover .heart {
  width: 16px; height: 15px;
  position: absolute;
  top: 0px; left: 62px;
  background: rgba(196,160,74,0.25);
  transform: rotate(-45deg);
  border-radius: 0 0 50% 50%;
}
.cover .heart::before,
.cover .heart::after {
  content: '';
  width: 16px; height: 16px;
  background: rgba(196,160,74,0.25);
  border-radius: 50%;
  position: absolute;
}
.cover .heart::before {
  top: -8px; left: 0;
}
.cover .heart::after {
  top: 0; left: 8px;
}

/* Star/sparkle above */
.cover .sparkle {
  width: 4px; height: 4px;
  position: absolute;
  top: 10px; left: 30px;
  background: rgba(196,160,74,0.4);
  border-radius: 50%;
  box-shadow: 80px 8px 0 rgba(196,160,74,0.3),
              90px 0px 0 rgba(196,160,74,0.2),
              20px 14px 0 rgba(196,160,74,0.2);
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 26pt;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.2;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 6px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 100px; height: 2px;
  background: #8FA8A0;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 11pt;
  color: #B0C8BE;
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
  color: #8FA8A0;
  font-size: 7pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 9px;
  border-radius: 3px;
  text-transform: uppercase;
}

.cover .tagline {
  font-size: 8.5pt;
  color: #B0C8BE;
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
  color: #8FA8A0;
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
  background: linear-gradient(165deg, #0F1A18 0%, #16261F 50%, #0F1A18 100%);
  position: relative;
  overflow: hidden;
}

.divider .div-glow {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #8FA8A0, transparent),
    radial-gradient(ellipse 25px 15px at 80% 30%, #8FA8A0, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #7A9B8E, transparent),
    radial-gradient(ellipse 18px 11px at 25% 85%, #8FA8A0, transparent);
}

.divider .div-num {
  font-size: 60pt;
  color: rgba(196,160,74,0.10);
  font-weight: 700;
  position: absolute;
  top: 1in;
}

.divider .div-paw {
  font-size: 20pt;
  color: rgba(196,160,74,0.15);
  margin-bottom: 16px;
  position: relative;
}

.divider .div-label {
  font-size: 10pt;
  color: #8FA8A0;
  letter-spacing: 3pt;
  text-transform: uppercase;
  margin-bottom: 10px;
  position: relative;
}

.divider .div-title {
  font-size: 22pt;
  color: #ffffff;
  font-weight: 700;
  line-height: 1.2;
  position: relative;
  padding: 0 0.6in;
}

.divider .div-sub {
  font-size: 11pt;
  color: #B0C8BE;
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
  border-bottom: 1.5px solid #8FA8A0;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #0F1A18;
  text-transform: uppercase;
}
.section-header .sh-right {
  color: #aaa;
}

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
  color: #0F1A18;
  margin-bottom: 3px;
}

.page-subtitle {
  font-size: 8pt;
  color: #888;
  font-style: italic;
  margin-bottom: 12px;
}

/* ---- Writing Lines ---- */
.wline {
  border-bottom: 0.5px solid #ccc;
  height: 24px;
  margin-bottom: 2px;
}
.wline-sm {
  border-bottom: 0.5px solid #ddd;
  height: 20px;
  margin-bottom: 1px;
}
.wline-lg {
  border-bottom: 0.5px solid #ccc;
  height: 30px;
  margin-bottom: 3px;
}

/* ---- Data Tables ---- */
table.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
}
table.data-table th {
  background: #0F1A18;
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
table.data-table tr:nth-child(even) td {
  background: #F6FAF8;
}

/* ---- Field Grid ---- */
.field-row {
  display: flex;
  gap: 8px;
  align-items: baseline;
  margin-bottom: 6px;
}
.field-label {
  font-size: 7.5pt;
  font-weight: 700;
  color: #0F1A18;
  text-transform: uppercase;
  letter-spacing: 0.4pt;
  white-space: nowrap;
  min-width: 70px;
}
.field-line {
  flex: 1;
  border-bottom: 0.5px solid #bbb;
  height: 16px;
}

/* ---- Checkbox Row ---- */
.check-row {
  display: flex;
  flex-wrap: wrap;
  gap: 5px 12px;
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

/* ---- Star Rating ---- */
.stars {
  font-size: 13pt;
  color: #ccc;
  letter-spacing: 2pt;
}

/* ---- Info / Quote Box ---- */
.info-box {
  background: #F6FAF8;
  border-left: 3px solid #8FA8A0;
  padding: 10px 12px;
  margin-bottom: 10px;
  font-size: 8.5pt;
  color: #333;
  line-height: 1.6;
}
.info-box .info-title {
  font-weight: 700;
  color: #0F1A18;
  font-size: 8.5pt;
  margin-bottom: 4px;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
}

/* ---- Prompt Box ---- */
.prompt-box {
  background: #EAF0EC;
  border: 1px solid #D8E0DC;
  border-radius: 4px;
  padding: 10px 12px;
  margin-bottom: 8px;
}
.prompt-box .prompt-label {
  font-size: 7pt;
  font-weight: 700;
  color: #8FA8A0;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  margin-bottom: 4px;
}
.prompt-box .prompt-text {
  font-size: 9pt;
  color: #444;
  font-style: italic;
  margin-bottom: 6px;
  line-height: 1.4;
}

/* ---- Rating Bars (1-5 scale) ---- */
.rating-bar-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 5px;
}
.rating-bar-label {
  font-size: 7pt;
  font-weight: 700;
  color: #0F1A18;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  min-width: 70px;
}
.rating-bar-circles {
  display: flex;
  gap: 4px;
}
.rating-circle {
  width: 14px; height: 14px;
  border: 1.5px solid #8FA8A0;
  border-radius: 50%;
  display: inline-block;
}

/* ---- Stat Card ---- */
.stat-card {
  text-align: center;
  padding: 8px 4px;
  background: #F6FAF8;
  border-radius: 4px;
  border: 1px solid #D0D8D4;
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
  color: #0F1A18;
}

/* ---- Photo Frame ---- */
.photo-frame {
  border: 2px solid #8FA8A0;
  border-radius: 4px;
  width: 100%;
  height: 2.6in;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #ccc;
  font-size: 8pt;
  font-style: italic;
  background: #F6FAF8;
}

.photo-frame-sq {
  border: 2px solid #8FA8A0;
  border-radius: 4px;
  width: 2in; height: 2in;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #ccc;
  font-size: 8pt;
  font-style: italic;
  background: #F6FAF8;
  margin: 0 auto;
}

.photo-frame-sm {
  border: 1.5px solid #8FA8A0;
  border-radius: 3px;
  width: 100%;
  height: 1.8in;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #ccc;
  font-size: 7pt;
  font-style: italic;
  background: #F6FAF8;
}

/* ---- Dot Grid ---- */
.dot-grid {
  background-image: radial-gradient(circle, #ddd 1px, transparent 1px);
  background-size: 16px 16px;
}

/* ---- Paw Print Accent ---- */
.paw-accent {
  text-align: center;
  color: #8FA8A0;
  font-size: 14pt;
  opacity: 0.3;
  letter-spacing: 12pt;
  margin: 10px 0;
}
"""


# ============================================================
# PAGE FUNCTIONS
# ============================================================

def cover():
    """Interior title page (page 1)"""
    return f'''
<!-- Page {pn()}: Cover -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="margin: 0 auto 30px; z-index: 5; position: relative;">
    <svg viewBox="0 0 120 130" width="90" height="97" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="25" cy="38" rx="10" ry="14" transform="rotate(-15 25 38)" fill="rgba(143,168,160,0.15)"/>
      <ellipse cx="48" cy="25" rx="10" ry="15" fill="rgba(143,168,160,0.18)"/>
      <ellipse cx="72" cy="25" rx="10" ry="15" fill="rgba(143,168,160,0.18)"/>
      <ellipse cx="95" cy="38" rx="10" ry="14" transform="rotate(15 95 38)" fill="rgba(143,168,160,0.15)"/>
      <path d="M 60 50 Q 30 55 25 75 Q 22 95 35 105 Q 50 112 60 112 Q 70 112 85 105 Q 98 95 95 75 Q 90 55 60 50 Z" fill="rgba(143,168,160,0.20)" stroke="rgba(143,168,160,0.50)" stroke-width="1.5"/>
    </svg>
  </div>

  <div class="title-block">
    <div class="main-title">In Loving Memory<br>of My Pet</div>
    <div class="accent-bar"></div>
    <div class="subtitle">A Memorial Journal and Keepsake</div>

    <div class="features">
      <span class="feature-badge">Photo Pages</span>
      <span class="feature-badge">Memory Prompts</span>
      <span class="feature-badge">Tribute Letters</span>
    </div>

    <div class="tagline">Cherish Every Memory &middot; Honor Every Moment</div>
  </div>

  <div class="publisher">More Shine Press</div>
</div>
'''


def owner_page():
    """This book belongs to / dedicated to page"""
    return f'''
<!-- Page {pn()}: Owner / Dedication -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">In Loving Memory</span>
    <span class="sh-right">A Keepsake Journal</span>
  </div>

  <div style="text-align: center; margin-top: 1in;">
    <div style="font-size: 10pt; color: #8FA8A0; letter-spacing: 3pt; text-transform: uppercase; margin-bottom: 20px;">This Memorial Journal Belongs To</div>
    <div style="border-bottom: 1.5px solid #8FA8A0; width: 4in; height: 28px; margin: 0 auto 40px;"></div>

    <div style="font-size: 10pt; color: #8FA8A0; letter-spacing: 3pt; text-transform: uppercase; margin-bottom: 20px;">In Memory Of</div>
    <div style="border-bottom: 1.5px solid #8FA8A0; width: 4in; height: 28px; margin: 0 auto 8px;"></div>
    <div style="font-size: 8pt; color: #999; font-style: italic;">My Beloved Pet</div>

    <div style="margin-top: 50px;">
      <div style="font-size: 10pt; color: #8FA8A0; letter-spacing: 3pt; text-transform: uppercase; margin-bottom: 12px;">Years Together</div>
      <div style="display: flex; justify-content: center; gap: 30px; font-size: 8pt; color: #888;">
        <span>From: <span style="display:inline-block; border-bottom:0.5px solid #bbb; width: 80px; height: 16px;"></span></span>
        <span>To: <span style="display:inline-block; border-bottom:0.5px solid #bbb; width: 80px; height: 16px;"></span></span>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def how_to_use():
    """How to use this journal"""
    return f'''
<!-- Page {pn()}: How to Use -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Introduction</span>
    <span class="sh-right">How to Use This Journal</span>
  </div>

  <div class="page-title">How to Use This Journal</div>
  <div class="page-subtitle">There is no right or wrong way to grieve</div>

  <div class="info-box">
    <div class="info-title">A Gentle Reminder</div>
    This journal is your private space to remember, reflect, and heal.
    Write as much or as little as you wish. Skip pages that do not feel
    right and return to them when you are ready. There is no timeline
    for grief &mdash; only the journey of honoring the love you shared.
  </div>

  <div class="prompt-box">
    <div class="prompt-label">Section 1 &mdash; My Pet's Story</div>
    <div class="prompt-text">Record the story of your pet's life: how you met, their
    personality, habits, and the home you shared together.</div>
  </div>

  <div class="prompt-box">
    <div class="prompt-label">Section 2 &mdash; Favorite Memories</div>
    <div class="prompt-text">Capture the moments that made you smile, laugh, and love
    deeply. Each spread gives you space for a photo and a treasured memory.</div>
  </div>

  <div class="prompt-box">
    <div class="prompt-label">Section 3 &mdash; Photo Gallery</div>
    <div class="prompt-text">Frame your favorite photographs alongside captions that
    tell the story behind each image.</div>
  </div>

  <div class="prompt-box">
    <div class="prompt-label">Section 4 &mdash; Letters &amp; Reflections</div>
    <div class="prompt-text">Write letters to your pet and reflect on what they meant
    to you. Let your heart speak freely.</div>
  </div>

  <div class="prompt-box">
    <div class="prompt-label">Section 5 &mdash; The Final Goodbye</div>
    <div class="prompt-text">Honor the farewell, the legacy of love, and the ways your
    pet will always be part of your life.</div>
  </div>

  <div class="prompt-box">
    <div class="prompt-label">Section 6 &mdash; Notes</div>
    <div class="prompt-text">Open space for anything else you wish to write &mdash;
    poems, quotes, drawings, or thoughts.</div>
  </div>

  <div class="paw-accent">✧✧✧</div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def cats_life_left():
    """My Pet's Story — left page (profile / vital stats)"""
    return f'''
<!-- Page {pn()}: Pet's Story — Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">My Pet's Story</span>
    <span class="sh-right">Profile</span>
  </div>

  <div class="page-title">All About My Pet</div>
  <div class="page-subtitle">Who they were, in their own special way</div>

  <div class="field-row">
    <span class="field-label">Name</span>
    <span class="field-line"></span>
  </div>
  <div class="field-row">
    <span class="field-label">Breed / Mix</span>
    <span class="field-line"></span>
  </div>
  <div class="field-row">
    <span class="field-label">Color(s)</span>
    <span class="field-line"></span>
  </div>
  <div class="field-row">
    <span class="field-label">Eye Color</span>
    <span class="field-line"></span>
  </div>
  <div class="field-row">
    <span class="field-label">Sex</span>
    <span class="field-line" style="max-width: 80px;"></span>
    <span class="field-label" style="min-width: 50px;">Weight</span>
    <span class="field-line" style="max-width: 60px;"></span>
    <span class="field-label" style="min-width: 30px;">lbs</span>
  </div>
  <div class="field-row">
    <span class="field-label">Born</span>
    <span class="field-line"></span>
  </div>
  <div class="field-row">
    <span class="field-label">Adopted</span>
    <span class="field-line"></span>
  </div>
  <div class="field-row">
    <span class="field-label">Passed</span>
    <span class="field-line"></span>
  </div>
  <div class="field-row">
    <span class="field-label">Age</span>
    <span class="field-line" style="max-width: 120px;"></span>
    <span class="field-label" style="min-width: 50px;">Years Together</span>
    <span class="field-line" style="max-width: 100px;"></span>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Personality in Three Words</div>
  <div style="display: flex; gap: 12px; justify-content: center; margin-bottom: 14px;">
    <span style="border-bottom: 1px solid #8FA8A0; width: 90px; height: 22px; text-align: center;"></span>
    <span style="border-bottom: 1px solid #8FA8A0; width: 90px; height: 22px; text-align: center;"></span>
    <span style="border-bottom: 1px solid #8FA8A0; width: 90px; height: 22px; text-align: center;"></span>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 6px;">Nicknames</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def cats_life_right():
    """My Pet's Story — right page (portrait + how we met)"""
    return f'''
<!-- Page {pn()}: Pet's Story — Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">My Pet's Story</span>
    <span class="sh-right">Portrait</span>
  </div>

  <div style="display: flex; gap: 14px;">
    <div style="flex: 0 0 2in;">
      <div class="photo-frame-sq">Photo</div>
    </div>
    <div style="flex: 1;">
      <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">How We Met</div>
      <div class="wline-sm"></div>
      <div class="wline-sm"></div>
      <div class="wline-sm"></div>
      <div class="wline-sm"></div>
      <div class="wline-sm"></div>
      <div class="wline-sm"></div>

      <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">First Impression</div>
      <div class="wline-sm"></div>
      <div class="wline-sm"></div>
      <div class="wline-sm"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 16px; margin-bottom: 6px;">A Day in Their Life</div>
  <div class="info-box" style="font-size: 7.5pt;">
    Morning ritual, favorite napping spot, mealtime habits, evening routine &mdash;
    describe a typical day with your pet.
  </div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 6px;">Favorite Things</div>
  <div class="field-row">
    <span class="field-label" style="min-width: 80px;">Food / Treat</span>
    <span class="field-line"></span>
  </div>
  <div class="field-row">
    <span class="field-label" style="min-width: 80px;">Toy</span>
    <span class="field-line"></span>
  </div>
  <div class="field-row">
    <span class="field-label" style="min-width: 80px;">Napping Spot</span>
    <span class="field-line"></span>
  </div>
  <div class="field-row">
    <span class="field-label" style="min-width: 80px;">Activity</span>
    <span class="field-line"></span>
  </div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def personality_traits():
    """Personality traits rating page"""
    traits = [
        "Affectionate", "Independent", "Playful", "Curious",
        "Talkative", "Quiet", "Brave", "Cautious",
        "Social", "Shy", "Energetic", "Mellow",
    ]
    rows = ""
    for t in traits:
        circles = '<div class="rating-bar-circles">'
        for _ in range(5):
            circles += '<span class="rating-circle"></span>'
        circles += '</div>'
        rows += f'''
    <div class="rating-bar-row">
      <span class="rating-bar-label">{t}</span>
      {circles}
    </div>'''

    return f'''
<!-- Page {pn()}: Personality Traits -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">My Pet's Story</span>
    <span class="sh-right">Personality</span>
  </div>

  <div class="page-title">Personality Traits</div>
  <div class="page-subtitle">Fill in the circle that best describes your pet</div>

  <div style="font-size: 7pt; color: #888; margin-bottom: 12px; display: flex; justify-content: flex-end; gap: 22px; padding-right: 8px;">
    <span>Rarely</span>
    <span>Sometimes</span>
    <span>Always</span>
  </div>

  {rows}

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 16px; margin-bottom: 6px;">Quirks &amp; Habits</div>
  <div class="info-box" style="font-size: 7.5pt;">
    What made your pet truly one of a kind? The little oddities, the funny
    behaviors, the things only you understood.
  </div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def habits_page():
    """Sounds, routines, funny moments"""
    return f'''
<!-- Page {pn()}: Habits & Moments -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">My Pet's Story</span>
    <span class="sh-right">Habits &amp; Moments</span>
  </div>

  <div class="page-title">Little Habits &amp; Big Moments</div>
  <div class="page-subtitle">The small things that made them who they were</div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">The Sound of Their Voice</div>
  <div class="prompt-box">
    <div class="prompt-text">Chirps, purrs, barks, songs, and sounds &mdash;
    what did your pet sound like? When did they get vocal?</div>
  </div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 12px; margin-bottom: 6px;">Funniest Thing They Did</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 12px; margin-bottom: 6px;">Naughtiest Moment</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 12px; margin-bottom: 6px;">Smartest Thing They Did</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 12px; margin-bottom: 6px;">The Look They Gave Me</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def memory_spread(num):
    """Favorite memory two-page spread — left page"""
    return f'''
<!-- Page {pn()}: Memory {num} — Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Favorite Memories</span>
    <span class="sh-right">Memory #{num}</span>
  </div>

  <div class="page-title">A Treasured Memory</div>
  <div class="page-subtitle">A moment I never want to forget</div>

  <div class="photo-frame">Favorite Photo</div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 12px; margin-bottom: 4px;">Caption</div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 6px;">What Happened</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 6px;">How It Made Me Feel</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def memory_right(num):
    """Favorite memory — right page (more space)"""
    return f'''
<!-- Page {pn()}: Memory {num} — Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Favorite Memories</span>
    <span class="sh-right">Memory #{num}</span>
  </div>

  <div class="page-title">More About This Memory</div>
  <div class="page-subtitle">The details, the feelings, the story behind it</div>

  <div class="photo-frame-sm">Another Photo (optional)</div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 6px;">The Full Story</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def photo_gallery(num_pages):
    """Photo gallery pages — 2 photos per page"""
    pages = []
    for i in range(num_pages):
        pages.append(f'''
<!-- Page {pn()}: Photo Gallery {i+1} -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Photo Gallery</span>
    <span class="sh-right">Page {i+1}</span>
  </div>

  <div class="page-title">Photo Gallery</div>
  <div class="page-subtitle">Capture every side of their personality</div>

  <div style="display: flex; gap: 12px; margin-bottom: 10px;">
    <div style="flex: 1;">
      <div class="photo-frame-sm">Photo</div>
      <div class="wline-sm" style="margin-top: 4px;"></div>
    </div>
    <div style="flex: 1;">
      <div class="photo-frame-sm">Photo</div>
      <div class="wline-sm" style="margin-top: 4px;"></div>
    </div>
  </div>
  <div style="display: flex; gap: 12px; margin-bottom: 10px;">
    <div style="flex: 1;">
      <div class="photo-frame-sm">Photo</div>
      <div class="wline-sm" style="margin-top: 4px;"></div>
    </div>
    <div style="flex: 1;">
      <div class="photo-frame-sm">Photo</div>
      <div class="wline-sm" style="margin-top: 4px;"></div>
    </div>
  </div>

  <div style="display: flex; gap: 12px;">
    <div style="flex: 1;">
      <div class="photo-frame-sm">Photo</div>
      <div class="wline-sm" style="margin-top: 4px;"></div>
    </div>
    <div style="flex: 1;">
      <div class="photo-frame-sm">Photo</div>
      <div class="wline-sm" style="margin-top: 4px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
''')
    return "".join(pages)


def letter_to_pet():
    """Letter to my pet — lined page with prompt"""
    return f'''
<!-- Page {pn()}: Letter to My Pet -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Letters &amp; Reflections</span>
    <span class="sh-right">Letter</span>
  </div>

  <div class="page-title">Dear...</div>
  <div class="page-subtitle">Write a letter to your pet</div>

  <div class="info-box" style="font-size: 8pt;">
    Speak from the heart. Tell them what you miss, what you wish you
    had said more often, and how much they meant to you. This is your
    private conversation &mdash; say everything.
  </div>

  <div class="wline"></div>
  <div class="wline"></div>
  <div class="wline"></div>
  <div class="wline"></div>
  <div class="wline"></div>
  <div class="wline"></div>
  <div class="wline"></div>
  <div class="wline"></div>
  <div class="wline"></div>
  <div class="wline"></div>
  <div class="wline"></div>
  <div class="wline"></div>
  <div class="wline"></div>
  <div class="wline"></div>
  <div class="wline"></div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def what_they_taught_me():
    """Reflection: what my pet taught me"""
    prompts = [
        ("What My Pet Taught Me About Love", "How did loving your pet change you?"),
        ("What My Pet Taught Me About Patience", "When did they test you, and what did you learn?"),
        ("What My Pet Taught Me About Joy", "What small moments brought you the most happiness?"),
    ]

    content = ""
    for title, prompt in prompts:
        content += f'''
  <div style="font-size: 8.5pt; font-weight: 700; color: #0F1A18; margin-top: 10px; margin-bottom: 4px;">{title}</div>
  <div style="font-size: 7.5pt; color: #999; font-style: italic; margin-bottom: 4px;">{prompt}</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
'''

    return f'''
<!-- Page {pn()}: What They Taught Me -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Letters &amp; Reflections</span>
    <span class="sh-right">What They Taught Me</span>
  </div>

  <div class="page-title">Lessons From My Pet</div>
  <div class="page-subtitle">The wisdom they shared without saying a word</div>

  {content}

  <div style="font-size: 8.5pt; font-weight: 700; color: #0F1A18; margin-top: 14px; margin-bottom: 4px;">How My Life Is Better Because of Them</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def the_final_goodbye_left():
    """Final goodbye — left page"""
    return f'''
<!-- Page {pn()}: Final Goodbye — Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">The Final Goodbye</span>
    <span class="sh-right">Farewell</span>
  </div>

  <div class="page-title">The Final Goodbye</div>
  <div class="page-subtitle">Honoring the farewell with love</div>

  <div class="field-row">
    <span class="field-label">Date</span>
    <span class="field-line"></span>
  </div>
  <div class="field-row">
    <span class="field-label">Location</span>
    <span class="field-line"></span>
  </div>
  <div class="field-row">
    <span class="field-label">Who Was There</span>
    <span class="field-line"></span>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">My Last Moments Together</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 12px; margin-bottom: 6px;">What I Want to Remember About That Day</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 12px; margin-bottom: 6px;">How I Knew It Was Time</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def the_final_goodbye_right():
    """Final goodbye — right page"""
    return f'''
<!-- Page {pn()}: Final Goodbye — Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">The Final Goodbye</span>
    <span class="sh-right">Reflection</span>
  </div>

  <div class="page-title">Saying Goodbye</div>
  <div class="page-subtitle">The hardest act of love</div>

  <div class="prompt-box">
    <div class="prompt-label">A Promise to My Pet</div>
    <div class="prompt-text">What do you promise to carry with you? How will you
    honor their memory in the days and years ahead?</div>
  </div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 12px; margin-bottom: 6px;">Resting Place / Memorial</div>
  <div class="field-row">
    <span class="field-label" style="min-width: 60px;">Type</span>
    <span class="field-line"></span>
  </div>
  <div class="field-row">
    <span class="field-label" style="min-width: 60px;">Location</span>
    <span class="field-line"></span>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Ways I Honor Their Memory</div>
  <div class="info-box" style="font-size: 7.5pt;">
    A special ornament at the holidays, a framed photo on the desk,
    a donation in their name, a garden stone, a keepsake box &mdash;
    the ways we remember are as unique as the cats we loved.
  </div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="paw-accent" style="margin-top: 16px;">✧</div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def paw_print_memorial():
    """Paw print keepsake page"""
    return f'''
<!-- Page {pn()}: Paw Print Memorial -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">The Final Goodbye</span>
    <span class="sh-right">Paw Print Keepsake</span>
  </div>

  <div class="page-title">Paw Print Keepsake</div>
  <div class="page-subtitle">A lasting impression of their little paw</div>

  <div style="display: flex; justify-content: center; align-items: center; height: 4.5in; margin-top: 10px;">
    <div style="width: 3.5in; height: 4in; border: 2px dashed #8FA8A0; border-radius: 12px; display: flex; justify-content: center; align-items: center; text-align: center; background: #F6FAF8;">
      <div>
        <div style="font-size: 9pt; color: #8FA8A0; letter-spacing: 2pt; text-transform: uppercase; margin-bottom: 8px;">Place Paw Print Here</div>
        <div style="font-size: 7.5pt; color: #aaa; font-style: italic; padding: 0 0.4in; line-height: 1.5;">
          Ink your pet's paw and press gently in this space.<br>
          A treasured keepsake for years to come.
        </div>
      </div>
    </div>
  </div>

  <div style="text-align: center; margin-top: 16px;">
    <div class="field-row" style="justify-content: center;">
      <span class="field-label" style="min-width: 40px;">Date</span>
      <span class="field-line" style="max-width: 150px;"></span>
    </div>
  </div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def legacy_page():
    """Legacy / how they changed my life"""
    return f'''
<!-- Page {pn()}: Legacy -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">The Final Goodbye</span>
    <span class="sh-right">Legacy</span>
  </div>

  <div class="page-title">Their Legacy</div>
  <div class="page-subtitle">How my pet changed my life forever</div>

  <div class="prompt-box">
    <div class="prompt-label">How They Changed Me</div>
    <div class="prompt-text">In what ways are you different because of your pet?
    What did they bring to your life that no one else could?</div>
  </div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="prompt-box">
    <div class="prompt-label">What I Will Never Forget</div>
    <div class="prompt-text">If you could only keep one memory, what would it be?</div>
  </div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="prompt-box">
    <div class="prompt-label">What I Want Others to Know About My Pet</div>
    <div class="prompt-text">If someone asked you to describe your pet, what would
    you want them to know?</div>
  </div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">If My Pet Could See Me Now, I Would Want Them to Know...</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def favorite_quotes():
    """Comforting quotes page"""
    return f'''
<!-- Page {pn()}: Quotes -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Letters &amp; Reflections</span>
    <span class="sh-right">Words of Comfort</span>
  </div>

  <div class="page-title">Words of Comfort</div>
  <div class="page-subtitle">Quotes and poems that bring peace</div>

  <div class="info-box" style="margin-top: 8px;">
    <div style="font-size: 9pt; font-style: italic; color: #444; line-height: 1.6;">
      "Until one has loved an animal, a part of one's soul remains unawakened."
    </div>
    <div style="font-size: 7pt; color: #8FA8A0; margin-top: 4px; text-align: right; letter-spacing: 1pt;">&mdash; ANATOLE FRANCE</div>
  </div>

  <div class="info-box">
    <div style="font-size: 9pt; font-style: italic; color: #444; line-height: 1.6;">
      "Animals are such agreeable friends &mdash; they ask no questions, they pass no criticisms."
    </div>
    <div style="font-size: 7pt; color: #8FA8A0; margin-top: 4px; text-align: right; letter-spacing: 1pt;">&mdash; GEORGE ELIOT</div>
  </div>

  <div class="info-box">
    <div style="font-size: 9pt; font-style: italic; color: #444; line-height: 1.6;">
      "The love for all living creatures is the most noble attribute of man."
    </div>
    <div style="font-size: 7pt; color: #8FA8A0; margin-top: 4px; text-align: right; letter-spacing: 1pt;">&mdash; CHARLES DARWIN</div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #0F1A18; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 16px; margin-bottom: 6px;">My Favorite Quotes &amp; Poems</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def notes_page():
    """Blank lined notes page"""
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

  <div class="page-title">Notes</div>
  <div class="page-subtitle">Thoughts, poems, and reflections</div>

  {lines}

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def sketch_page():
    """Dot grid page for sketches / paw tracings"""
    return f'''
<!-- Page {pn()}: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Notes</span>
    <span class="sh-right">Sketches &amp; Drawings</span>
  </div>

  <div class="page-title">Sketch Pad</div>
  <div class="page-subtitle">Draw your pet, trace their paw, or doodle freely</div>

  <div class="dot-grid" style="width: 100%; height: 6.5in; border-radius: 4px;"></div>

  <div class="page-footer">
    <span>In Loving Memory of My Pet</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def divider_section(num, num_word, title, subtitle):
    """Section divider page"""
    return f'''
<!-- Page {pn()}: Divider — Section {num} -->
<div class="divider">
  <div class="div-glow"></div>
  <div class="div-num">{num}</div>
  <div class="div-paw">✧</div>
  <div class="div-label">Section {num_word}</div>
  <div class="div-title">{title}</div>
  <div class="div-sub">{subtitle}</div>
</div>
'''


# ============================================================
# MAIN — ASSEMBLE BOOK
# ============================================================

def main():
    pages = []

    # ---- Front Matter ----
    pages.append(cover())                          # 1: Cover
    pages.append(owner_page())                     # 2: Owner / dedication

    # ---- How to use ----
    pages.append(how_to_use())                     # 3: How to use

    # ---- Section 1: My Pet's Story ----
    pages.append(divider_section(1, "One", "My Pet's Story", "Who they were, in every detail"))
    pages.append(cats_life_left())                 # Profile / vital stats
    pages.append(cats_life_right())                # Portrait + how we met
    pages.append(personality_traits())             # Personality rating
    pages.append(habits_page())                    # Habits & moments

    # ---- Section 2: Favorite Memories ----
    pages.append(divider_section(2, "Two", "Favorite Memories", "The moments that stay forever"))
    NUM_MEMORIES = 8
    for i in range(1, NUM_MEMORIES + 1):
        pages.append(memory_spread(i))             # Left page
        pages.append(memory_right(i))              # Right page

    # ---- Section 3: Photo Gallery ----
    pages.append(divider_section(3, "Three", "Photo Gallery", "Every picture tells their story"))
    pages.append(photo_gallery(6))                 # 6 pages, 6 photos each

    # ---- Section 4: Letters & Reflections ----
    pages.append(divider_section(4, "Four", "Letters &amp; Reflections", "Words from the heart"))
    pages.append(letter_to_pet())                  # Letter to my pet
    pages.append(letter_to_pet())                  # Second letter page
    pages.append(what_they_taught_me())            # What they taught me
    pages.append(favorite_quotes())                # Quotes

    # ---- Section 5: The Final Goodbye ----
    pages.append(divider_section(5, "Five", "The Final Goodbye", "Honoring the farewell"))
    pages.append(the_final_goodbye_left())         # Final goodbye details
    pages.append(the_final_goodbye_right())        # Reflection / promises
    pages.append(paw_print_memorial())             # Paw print keepsake
    pages.append(legacy_page())                    # Legacy

    # ---- Section 6: Notes ----
    pages.append(divider_section(6, "Six", "Notes", "Open space for thoughts and memories"))
    pages.append(sketch_page())                    # Dot grid
    for _ in range(16):
        pages.append(notes_page())                 # 16 lined notes pages

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

    # Print breakdown
    print(f"\nPage breakdown:")
    print(f"  Cover: 1")
    print(f"  Owner / dedication: 1")
    print(f"  How to use: 1")
    print(f"  Section dividers: 6")
    print(f"  Pet's story (profile, portrait, personality, habits): 4")
    print(f"  Memory spreads ({NUM_MEMORIES} x 2 pages): {NUM_MEMORIES * 2}")
    print(f"  Photo gallery: 4")
    print(f"  Letters & reflections (2 letters, lessons, quotes): 4")
    print(f"  Final goodbye (details, reflection, paw print, legacy): 4")
    print(f"  Sketch page: 1")
    print(f"  Notes pages: 8")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
