#!/usr/bin/env python3
"""
Fermentation Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Home fermentation enthusiasts (kombucha, kimchi, sauerkraut, sourdough, kefir, etc.)
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "fermentation_journal_us_V1.0.html")

BOOK_TITLE = "Fermentation Journal"
BOOK_SUBTITLE = "Track Every Batch, Every Culture, Every Flavor"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

# ============================================================
# CSS  (raw string — never f-string)
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
/* Deep charcoal: #161616, #1E1E1E */
/* Copper/amber: #B87333, #C4A04A, #6B4423 */
/* Olive green: #6B7A4F, #8B9B6E, #A8B89C */
/* Warm cream: #FAF8F4, #F5F0E8 */

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
  background: linear-gradient(165deg, #161616 0%, #1E1E1E 30%, #161616 65%, #100F0F 100%);
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
    radial-gradient(ellipse 26px 16px at 80% 15%, #B87333, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #8B9B6E, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #B87333, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #8B9B6E, transparent),
    radial-gradient(ellipse 18px 11px at 90% 40%, #C4A04A, transparent),
    radial-gradient(ellipse 16px 10px at 40% 90%, #B87333, transparent);
}

/* ===== CSS Mason Jar Illustration ===== */
.cover .jar-wrap {
  width: 110px; height: 160px;
  position: relative;
  margin: 0 auto 20px;
}

/* Jar lid (copper/bronze) */
.cover .jar-lid {
  width: 70px; height: 14px;
  position: absolute;
  top: 4px; left: 20px;
  background: linear-gradient(180deg, #B87333, #8B6914);
  border-radius: 4px 4px 2px 2px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.3);
}
.cover .jar-lid-band {
  width: 74px; height: 6px;
  position: absolute;
  top: 16px; left: 18px;
  background: linear-gradient(180deg, #A06330, #6B4914);
  border-radius: 1px 1px 0 0;
}

/* Jar lid texture lines */
.cover .jar-lid::before {
  content: '';
  position: absolute;
  top: 2px; left: 8px; right: 8px; bottom: 2px;
  background-image: repeating-linear-gradient(
    90deg,
    transparent 0,
    transparent 2px,
    rgba(0,0,0,0.12) 2px,
    rgba(0,0,0,0.12) 3px
  );
  border-radius: 3px;
}

/* Jar body */
.cover .jar-body {
  width: 68px; height: 120px;
  position: absolute;
  top: 22px; left: 21px;
  background: linear-gradient(160deg,
    rgba(196,160,74,0.06) 0%,
    rgba(184,115,51,0.04) 40%,
    rgba(138,155,110,0.06) 80%,
    rgba(196,160,74,0.04) 100%);
  border: 1px solid rgba(196,160,74,0.30);
  border-radius: 8px 8px 6px 6px;
}

/* Ferment liquid/content inside (amber/olive) */
.cover .jar-content {
  width: 62px; height: 70px;
  position: absolute;
  top: 66px; left: 24px;
  background: linear-gradient(180deg,
    rgba(184,115,51,0.18) 0%,
    rgba(139,107,20,0.25) 30%,
    rgba(107,122,79,0.20) 70%,
    rgba(84,99,61,0.25) 100%);
  border-radius: 2px 2px 6px 6px;
}

/* Bubbles inside jar */
.cover .jar-bubble1 {
  width: 4px; height: 4px;
  background: rgba(250,248,244,0.25);
  border-radius: 50%;
  position: absolute;
  top: 72px; left: 40px;
}
.cover .jar-bubble2 {
  width: 3px; height: 3px;
  background: rgba(250,248,244,0.20);
  border-radius: 50%;
  position: absolute;
  top: 82px; left: 56px;
}
.cover .jar-bubble3 {
  width: 5px; height: 5px;
  background: rgba(250,248,244,0.15);
  border-radius: 50%;
  position: absolute;
  top: 92px; left: 34px;
}
.cover .jar-bubble4 {
  width: 3px; height: 3px;
  background: rgba(250,248,244,0.18);
  border-radius: 50%;
  position: absolute;
  top: 100px; left: 60px;
}

/* Jar shine highlight */
.cover .jar-shine {
  width: 5px; height: 80px;
  position: absolute;
  top: 35px; left: 28px;
  background: linear-gradient(180deg, rgba(250,248,244,0.25), rgba(250,248,244,0.03));
  border-radius: 50%;
}

/* Vapor/aroma lines */
.cover .vapor1 {
  width: 2px; height: 24px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.30), transparent);
  position: absolute;
  top: -18px; left: 48px;
  border-radius: 50%;
  transform: rotate(-6deg);
}
.cover .vapor2 {
  width: 2px; height: 30px;
  background: linear-gradient(180deg, transparent, rgba(184,115,51,0.22), transparent);
  position: absolute;
  top: -24px; left: 62px;
  border-radius: 50%;
  transform: rotate(8deg);
}

/* Label on jar */
.cover .jar-label {
  width: 40px; height: 18px;
  position: absolute;
  top: 105px; left: 35px;
  border: 1px solid rgba(196,160,74,0.25);
  border-radius: 1px;
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
  color: #C4A04A;
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
  color: #A8B89C;
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
    radial-gradient(ellipse 25px 15px at 80% 30%, #B87333, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #8B9B6E, transparent),
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
  color: #A8B89C;
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
  border-bottom: 1.5px solid #B87333;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #161616;
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
  color: #161616;
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
  height: 22px;
  margin-bottom: 2px;
}
.wline-sm {
  border-bottom: 0.5px solid #ddd;
  height: 18px;
  margin-bottom: 1px;
}

/* ---- Data Tables ---- */
table.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
}
table.data-table th {
  background: #B87333;
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
  background: #FAF8F4;
}

/* ---- Checkbox Row ---- */
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

/* ---- Star Rating ---- */
.stars {
  font-size: 13pt;
  color: #ccc;
  letter-spacing: 2pt;
}

/* ---- Info Box ---- */
.info-box {
  background: #FAF8F4;
  border-left: 3px solid #B87333;
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
  color: #161616;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  min-width: 68px;
}
.rating-bar-circles {
  display: flex;
  gap: 4px;
}
.rating-circle {
  width: 14px; height: 14px;
  border: 1.5px solid #B87333;
  border-radius: 50%;
  display: inline-block;
}

/* ---- Stat Card ---- */
.stat-card {
  text-align: center;
  padding: 6px 4px;
  background: #FAF8F4;
  border-radius: 4px;
  border: 1px solid #D8E0D2;
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

/* ---- Gear Card ---- */
.gear-card {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 8px;
  margin-bottom: 6px;
  background: #FCFAF7;
}
.gear-card .gear-label {
  font-size: 7pt;
  font-weight: 700;
  color: #B87333;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 4px;
}

/* ---- Dot Grid ---- */
.dot-grid {
  background-image: radial-gradient(circle, #d0d0d0 1px, transparent 1px);
  background-size: 0.20in 0.20in;
  background-position: 0.10in 0.10in;
}

/* ---- Recipe Row ---- */
.recipe-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 3px;
}
.recipe-num {
  width: 16px; height: 16px;
  border: 1px solid #B87333;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 6.5pt;
  font-weight: 700;
  color: #B87333;
  flex-shrink: 0;
}
"""

# ============================================================
# PAGE BUILDERS
# ============================================================

def cover():
    pg = pn()
    return """<!-- PAGE %d: Cover -->
<div class="cover">
  <div class="glow-bg"></div>
  <div class="jar-wrap">
    <div class="vapor1"></div>
    <div class="vapor2"></div>
    <div class="jar-lid"></div>
    <div class="jar-lid-band"></div>
    <div class="jar-body"></div>
    <div class="jar-content"></div>
    <div class="jar-bubble1"></div>
    <div class="jar-bubble2"></div>
    <div class="jar-bubble3"></div>
    <div class="jar-bubble4"></div>
    <div class="jar-shine"></div>
    <div class="jar-label"></div>
  </div>
  <div class="title-block">
    <div class="main-title">%s</div>
    <div class="accent-bar"></div>
    <div class="subtitle">%s</div>
    <div class="features">
      <span class="feature-badge">40 Batch Logs</span>
      <span class="feature-badge">Culture Registry</span>
      <span class="feature-badge">Salt Brine Guide</span>
      <span class="feature-badge">Tasting Notes</span>
    </div>
    <div class="tagline">For Home Fermenters &amp; Gut Health Enthusiasts</div>
  </div>
  <div class="publisher">More Shine Press</div>
</div>
""" % (pg, BOOK_TITLE, BOOK_SUBTITLE)


def owner_page():
    pg = pn()
    return """<!-- PAGE %d: Owner -->
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
      <div style="font-size: 8pt; font-weight: 700; color: #B87333; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Ferment</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #B87333; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Active Cultures</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #B87333; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Experience Level</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #B87333; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Preferred Salt</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def how_to_use():
    pg = pn()
    return """<!-- PAGE %d: How to Use -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Getting Started</span>
    <span class="sh-right">More Shine Press</span>
  </div>

  <div class="page-title">How to Use This Journal</div>
  <div class="page-subtitle">Document your fermentation journey, batch by batch</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Fermentation Journal?</div>
    Fermentation is both art and science. A journal turns experiments into reproducible recipes. By recording ingredients, temperatures, timing, and outcomes, you build a personal reference that transforms trial and error into expertise. Your journal becomes your own fermentation cookbook.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Tips for Better Fermentation</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Weigh everything.</strong> Fermentation lives or dies by ratios. Use a kitchen scale, not measuring cups. Record weights in grams for precision and reproducibility. Salt percentage is the single most important variable.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Temperature matters.</strong> Most ferments thrive between 65-75&deg;F (18-24&deg;C). Too cold and fermentation stalls; too warm and it races, producing off-flavors. Note your ambient temperature daily.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Record observations daily.</strong> In the first week, check every day. Note bubbles, color changes, smell, texture, and any mold. Patterns emerge over multiple batches that you cannot see from memory.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Label every jar.</strong> Write the ferment name, start date, and batch number on each vessel. When you have five jars going at once, memory is not enough. Use glass-safe markers or masking tape labels.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Trust your senses.</strong> A healthy ferment smells sour, tangy, and pleasant. If something smells putrid, rotten, or looks fuzzy (mold with green/black/white growth), discard it. When in doubt, throw it out.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #F5F0E8; border: 1px solid #D8E0D2; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Safety Note:</strong> While fermentation is one of the oldest and safest food preservation methods, proper hygiene is essential. Use clean equipment, filtered water (chlorine inhibits fermentation), and non-iodized salt. If you have health concerns, consult a healthcare professional before consuming fermented foods.
  </div>

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def salt_brine_guide():
    pg = pn()
    return """<!-- PAGE %d: Salt Brine Guide -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Salt &amp; Brine Guide</span>
  </div>

  <div class="page-title">Salt &amp; Brine Guide</div>
  <div class="page-subtitle">The most critical ratio in fermentation</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th>Ferment Type</th>
      <th>Salt %%</th>
      <th>Salt per 1kg Veg</th>
      <th>Salt per 1L Water</th>
      <th>Notes</th>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Sauerkraut</td>
      <td>2.0%%</td>
      <td style="text-align: center;">20g</td>
      <td style="text-align: center;">N/A (massaged)</td>
      <td>Salt massaged into cabbage</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Kimchi</td>
      <td>2.5-3.0%%</td>
      <td style="text-align: center;">25-30g</td>
      <td style="text-align: center;">N/A (soaked)</td>
      <td>Brine soak then paste</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Pickles (cucumber)</td>
      <td>3.5-5.0%%</td>
      <td style="text-align: center;">N/A</td>
      <td style="text-align: center;">35-50g</td>
      <td>Brine pour-over method</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Hot Sauce / Pepper</td>
      <td>3.0-5.0%%</td>
      <td style="text-align: center;">30-50g</td>
      <td style="text-align: center;">30-50g</td>
      <td>Brine or mash method</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Carrots / Radish</td>
      <td>2.5-3.5%%</td>
      <td style="text-align: center;">N/A</td>
      <td style="text-align: center;">25-35g</td>
      <td>Brine pour-over</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Kombucha</td>
      <td>N/A (sugar)</td>
      <td style="text-align: center;">N/A</td>
      <td style="text-align: center;">50-100g sugar</td>
      <td>Sugar feeds SCOBY, not salt</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Sourdough</td>
      <td>1.5-2.5%%</td>
      <td style="text-align: center;">Baker's pct</td>
      <td style="text-align: center;">N/A</td>
      <td>%% of flour weight</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Miso / Bean Paste</td>
      <td>8-12%%</td>
      <td style="text-align: center;">80-120g</td>
      <td style="text-align: center;">N/A</td>
      <td>High salt, long ferment</td>
    </tr>
  </table>

  <div style="margin-top: 10px; padding: 8px 10px; background: #FAF8F4; border-left: 3px solid #B87333; border-radius: 0 4px 4px 0; font-size: 8pt; color: #555; line-height: 1.5;">
    <strong style="color: #161616; text-transform: uppercase; font-size: 8pt; letter-spacing: 0.3pt;">How to Calculate Brine:</strong><br>
    Brine %% = (salt weight &divide; water weight) &times; 100. For a 3.5%% brine: 35g salt per 1000g (1L) water. Always use weight, not volume. A tablespoon of coarse salt weighs very different from a tablespoon of fine salt.
  </div>

  <div style="margin-top: 8px; padding: 6px 10px; background: #FFF8E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 7.5pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Salt choice:</strong> Use non-iodized salt (sea salt, kosher, pickling salt). Iodine inhibits the bacteria that make fermentation work. Avoid salt with anti-caking agents when possible.
  </div>

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def fermentation_types_reference():
    pg = pn()
    categories = [
        ("Lacto-Fermentation (Vegetables)",
         "Sauerkraut &bull; Kimchi &bull; Pickles &bull; Salsa &bull; Hot Sauce &bull; Fermented Carrots &bull; Chutney &bull; Curtido &bull; Giardiniera"),
        ("Kombucha &amp; Fermented Tea",
         "Kombucha (SCOBY) &bull; Jun Tea (SCOBY + honey) &bull; Kvass (beet) &bull; Water Kefir (tibicos)"),
        ("Milk Kefir &amp; Yogurt",
         "Milk Kefir (grains) &bull; Yogurt (thermophilic) &bull; Viili &bull; Filmj&ouml;lk &bull; Caspian Sea Yogurt"),
        ("Sourdough &amp; Grain Ferments",
         "Sourdough Bread &bull; Sourdough Pancakes &bull; Injera &bull; Dosa &bull; Lactobacillus Rice Water"),
        ("Miso, Natto &amp; Tempeh",
         "Miso (soybean/barley) &bull; Natto &bull; Tempeh &bull; Doenjang &bull; Douchi"),
        ("Vinegar &amp; Alcohol",
         "Apple Cider Vinegar &bull; Wine Vinegar &bull; Malt Vinegar &bull; Mead &bull; Country Wine"),
    ]

    rows = ""
    for cat, notes in categories:
        rows += """
      <div style="border: 1px solid #D8E0D2; border-radius: 4px; padding: 6px 8px; margin-bottom: 5px; background: #FCFAF7;">
        <div style="font-size: 7pt; font-weight: 700; color: #B87333; text-transform: uppercase; letter-spacing: 0.3pt; margin-bottom: 3px;">%s</div>
        <div style="font-size: 7.5pt; color: #888; line-height: 1.5;">%s</div>
      </div>""" % (cat, notes)

    return """<!-- PAGE %d: Fermentation Types -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Fermentation Types</span>
  </div>

  <div class="page-title">Types of Fermentation</div>
  <div class="page-subtitle">From vegetables to vinegars &mdash; know your ferments</div>

  %s

  <div style="margin-top: 8px; padding: 6px 8px; background: #FAF8F4; border-radius: 3px; font-size: 7pt; color: #888; font-style: italic;">
    Most vegetable ferments use Lactobacillus bacteria (lacto-fermentation), which convert sugars to lactic acid. This acid preserves the food and creates the characteristic tangy flavor. Kombucha and vinegar use a different process involving yeast and acetic acid bacteria.
  </div>

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, rows, page_no[0])


def ph_timeline_reference():
    pg = pn()
    return """<!-- PAGE %d: pH Timeline -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">pH &amp; Timeline Guide</span>
  </div>

  <div class="page-title">pH &amp; Fermentation Timeline</div>
  <div class="page-subtitle">Know when your ferment is ready</div>

  <div style="font-size: 8.5pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">The pH Scale for Fermentation</div>
    <div style="margin-bottom: 8px;">
      <strong>Below pH 4.0:</strong> Safe zone. Lactic acid bacteria dominate, harmful organisms cannot survive. Most vegetable ferments are ready at pH 3.3-3.8.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>pH 4.0-4.6:</strong> Transition zone. Ferment is progressing but not yet at full preservation. Continue fermenting.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>Above pH 4.6:</strong> Caution. Not acidic enough for safe room-temperature storage. Do not can or seal at this stage.
    </div>
  </div>

  <table class="data-table" style="font-size: 7.5pt; margin-top: 10px;">
    <tr>
      <th>Ferment Type</th>
      <th>Target pH</th>
      <th>Typical Duration</th>
      <th>Temperature</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">Sauerkraut</td><td>3.3-3.8</td><td style="text-align:center;">2-4 weeks</td><td>65-72&deg;F</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Kimchi</td><td>3.5-4.0</td><td style="text-align:center;">3-7 days</td><td>65-72&deg;F</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Cucumber Pickles</td><td>3.0-3.5</td><td style="text-align:center;">1-2 weeks</td><td>68-75&deg;F</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Kombucha (1F)</td><td>2.5-3.5</td><td style="text-align:center;">7-14 days</td><td>72-80&deg;F</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Kombucha (2F)</td><td>2.5-3.0</td><td style="text-align:center;">2-5 days</td><td>72-80&deg;F</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Milk Kefir</td><td>4.2-4.5</td><td style="text-align:center;">12-24 hrs</td><td>68-78&deg;F</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Sourdough (starter)</td><td>3.8-4.2</td><td style="text-align:center;">5-7 days establish</td><td>70-78&deg;F</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Hot Sauce</td><td>3.0-3.8</td><td style="text-align:center;">1-3 weeks</td><td>65-75&deg;F</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Miso</td><td>4.0-5.0</td><td style="text-align:center;">3-12 months</td><td>55-85&deg;F</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Apple Cider Vinegar</td><td>2.5-3.0</td><td style="text-align:center;">4-8 weeks</td><td: 68-80&deg;F</td></tr>
  </table>

  <div style="margin-top: 10px; padding: 6px 10px; background: #FFF8E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 7.5pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">When is it ready?</strong> Taste is your best guide. pH strips confirm safety. When the tanginess is to your liking and pH is below 4.0, move to cold storage (refrigerator) to slow fermentation. It will continue to develop flavor slowly in the fridge.
  </div>

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def safety_reference():
    pg = pn()
    terms = [
        ("Mold vs. Kahm Yeast",
         "White film on the surface is often kahm yeast (harmless). Fuzzy patches that are green, blue, black, or pink are mold &mdash; discard the batch. If unsure, smell: kahm yeast is mild and yeasty; mold smells musty."),
        ("Botulism Risk",
         "Lacto-fermentation is inherently safe because the acidic environment prevents Clostridium botulinum. The danger is primarily in oil-packed or low-acid ferments. Always confirm pH is below 4.0 before long-term storage."),
        ("Temperature Control",
         "Too warm (above 80&deg;F/27&deg;C) can cause rapid, off-flavor fermentation or allow unwanted bacteria to dominate. Too cold (below 60&deg;F/16&deg;C) slows fermentation to a crawl. Aim for 65-75&deg;F for most vegetable ferments."),
        ("Equipment Hygiene",
         "Wash jars, lids, weights, and tools with hot soapy water. No need to sterilize for fermentation (unlike canning), but everything must be visibly clean. Avoid scratched or chipped jars that harbor bacteria."),
        ("Water Quality",
         "Chlorinated tap water can inhibit or kill fermentation bacteria. Use filtered, spring, or dechlorinated water (leave tap water uncovered for 24 hours to let chlorine dissipate)."),
        ("Allergen Awareness",
         "Fermented foods contain histamine and biogenic amines. People with histamine intolerance should introduce fermented foods gradually. Those with compromised immune systems, pregnant women, and young children should consult a healthcare provider."),
    ]

    rows = ""
    for term, desc in terms:
        rows += """
      <div style="border: 1px solid #D8E0D2; border-radius: 3px; padding: 7px 9px; margin-bottom: 6px; background: #FCFAF7;">
        <div style="font-size: 9.5pt; font-weight: 700; color: #161616; margin-bottom: 3px;">%s</div>
        <div style="font-size: 8pt; color: #555; line-height: 1.5;">%s</div>
      </div>""" % (term, desc)

    return """<!-- PAGE %d: Safety -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Safety First</span>
  </div>

  <div class="page-title">Safety Guidelines</div>
  <div class="page-subtitle">Ferment confidently and safely</div>

  %s

  <div style="margin-top: 8px; padding: 6px 10px; background: #FFF0F0; border: 1px solid #E8C0C0; border-radius: 3px; font-size: 7.5pt; color: #888; font-style: italic;">
    <strong style="color: #8B3333;">Important:</strong> This journal is a personal tracking tool and does not provide medical or food safety advice. Always use trusted recipes when starting out. If a ferment looks, smells, or tastes wrong, discard it.
  </div>

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, rows, page_no[0])


def divider_section(num, label, title, subtitle):
    labels = ["One", "Two", "Three", "Four", "Five", "Six"]
    label_text = labels[num-1] if num <= 6 else label
    pg = pn()
    return """<!-- PAGE %d: Divider -->
<div class="divider">
  <div class="div-glow"></div>
  <div class="div-num">%02d</div>
  <div class="div-label">Part %s</div>
  <div class="div-title">%s</div>
  <div class="div-sub">%s</div>
</div>
""" % (pg, num, label_text, title, subtitle)


def batch_log_left(batch_num):
    """Left page of two-page batch spread — recipe & setup"""
    pg = pn()
    return """<!-- PAGE %d: Batch %d Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Batch #%02d</span>
    <span class="sh-right">Fermentation Journal</span>
  </div>

  <div class="page-title">Batch #%02d &mdash; Setup</div>
  <div class="page-subtitle">Ingredients, culture, and parameters</div>

  <!-- Batch Info -->
  <div style="background: #FAF8F4; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Temp</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Batch Name</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Ferment Type</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Ferment Type checkboxes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Fermentation Method</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Lacto-Vegetable</span>
    <span class="check-item"><span class="check-box"></span> Kombucha</span>
    <span class="check-item"><span class="check-box"></span> Kefir (Milk)</span>
    <span class="check-item"><span class="check-box"></span> Kefir (Water)</span>
    <span class="check-item"><span class="check-box"></span> Sourdough</span>
    <span class="check-item"><span class="check-box"></span> Vinegar</span>
    <span class="check-item"><span class="check-box"></span> Miso/Tempeh</span>
    <span class="check-item"><span class="check-box"></span> Other</span>
  </div>

  <!-- Culture / Starter -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Culture / Starter</div>
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 8px;">
    <span style="font-size: 7pt; color: #888; min-width: 20px;">Type:</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 8px;">
    <span style="font-size: 7pt; color: #888; min-width: 20px;">Source:</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Ingredients -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Ingredients &mdash; Record Each Item and Weight</div>

  <div class="recipe-row">
    <div class="recipe-num">1</div>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    <span style="font-size: 7pt; color: #888; min-width: 20px;">grams</span>
    <div style="width: 32px; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div class="recipe-row">
    <div class="recipe-num">2</div>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    <span style="font-size: 7pt; color: #888; min-width: 20px;">grams</span>
    <div style="width: 32px; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div class="recipe-row">
    <div class="recipe-num">3</div>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    <span style="font-size: 7pt; color: #888; min-width: 20px;">grams</span>
    <div style="width: 32px; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div class="recipe-row">
    <div class="recipe-num">4</div>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    <span style="font-size: 7pt; color: #888; min-width: 20px;">grams</span>
    <div style="width: 32px; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div class="recipe-row">
    <div class="recipe-num">5</div>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    <span style="font-size: 7pt; color: #888; min-width: 20px;">grams</span>
    <div style="width: 32px; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div class="recipe-row">
    <div class="recipe-num">6</div>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    <span style="font-size: 7pt; color: #888; min-width: 20px;">grams</span>
    <div style="width: 32px; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div class="recipe-row">
    <div class="recipe-num">7</div>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    <span style="font-size: 7pt; color: #888; min-width: 20px;">grams</span>
    <div style="width: 32px; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Salt & Brine stats -->
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-top: 6px;">
    <div style="background: #F5F0E8; padding: 4px 6px; border-radius: 3px;">
      <div style="font-size: 6.5pt; color: #888; text-transform: uppercase;">Salt %%</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div style="background: #F5F0E8; padding: 4px 6px; border-radius: 3px;">
      <div style="font-size: 6.5pt; color: #888; text-transform: uppercase;">Brine Ratio</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div style="background: #F5F0E8; padding: 4px 6px; border-radius: 3px;">
      <div style="font-size: 6.5pt; color: #888; text-transform: uppercase;">Vessel Size</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Batch #%02d &mdash; Setup</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, batch_num, batch_num, batch_num, batch_num, page_no[0])


def batch_log_right(batch_num):
    """Right page of two-page batch spread — timeline & tasting"""
    pg = pn()
    return """<!-- PAGE %d: Batch %d Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Batch #%02d</span>
    <span class="sh-right">Timeline &amp; Tasting</span>
  </div>

  <div class="page-title">Batch #%02d &mdash; Progress</div>
  <div class="page-subtitle">Fermentation timeline, tasting notes, and results</div>

  <!-- Fermentation Timeline -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Fermentation Timeline &mdash; Log Observations Daily</div>
  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:32px;">Day</th>
      <th style="width:28px;">Temp</th>
      <th style="width:28px;">pH</th>
      <th>Observations (bubbles, color, smell, texture)</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">1</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">2</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">3</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">4</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">5</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">7</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">10</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">14</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">21</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">30+</td><td></td><td></td><td></td></tr>
  </table>

  <!-- Sensory Ratings -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Sensory Ratings &mdash; Fill in Circles (1 = Weak, 5 = Strong)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Sourness</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Saltiness</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Crunch/Texture</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Complexity</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>

  <!-- Overall Rating & Outcome -->
  <div style="display: flex; align-items: center; gap: 8px; margin-top: 6px; margin-bottom: 6px;">
    <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt;">Overall</span>
    <span class="stars">&#10022; &#10022; &#10022; &#10022; &#10022;</span>
  </div>

  <div class="check-row" style="margin-bottom: 6px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Would Make Again</span>
    <span class="check-item"><span class="check-box"></span> New Favorite</span>
    <span class="check-item"><span class="check-box"></span> Needs Tweaking</span>
    <span class="check-item"><span class="check-box"></span> Failed (Discarded)</span>
  </div>

  <!-- Tasting & Results Notes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Tasting Notes &amp; Observations</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">What to Adjust Next Time</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Batch #%02d &mdash; Progress</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, batch_num, batch_num, batch_num, batch_num, page_no[0])


def culture_registry(page_of, total_pages):
    """Starter culture registry"""
    pg = pn()
    return """<!-- PAGE %d: Culture Registry -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Culture Registry</span>
    <span class="sh-right">Page %d of %d</span>
  </div>

  <div class="page-title">Starter Culture Registry</div>
  <div class="page-subtitle">Track your SCOBYs, grains, and starters</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Culture Name</th>
      <th style="width:55px;">Type</th>
      <th style="width:40px;">Source</th>
      <th style="width:35px;">Date</th>
      <th>Notes / Health</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">1</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">2</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">3</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">4</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">5</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">6</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">7</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">8</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">9</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">10</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">11</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">12</td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Type: SCOBY/Kefir Grain/Sourdough Starter/Koji/Other | Source: friend, online, self-cultured | Health: active, dormant, struggling, dead</div>

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_of, total_pages, page_no[0])


def recipe_development():
    """Recipe development worksheet"""
    pg = pn()
    return """<!-- PAGE %d: Recipe Development -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Recipe Lab</span>
    <span class="sh-right">Develop Your Own</span>
  </div>

  <div class="page-title">Recipe Development</div>
  <div class="page-subtitle">Design and refine your signature ferment</div>

  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 10px;">
    <span style="font-size: 8pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 42px;">Recipe</span>
    <div style="flex:1; border-bottom: 1px solid #161616; height: 20px;"></div>
  </div>

  <!-- Inspiration -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Inspiration / Goal</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Ingredients Table -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Ingredients</div>
  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Ingredient</th>
      <th style="width:40px;">Amount (g)</th>
      <th style="width:40px;">%% of Total</th>
      <th>Role / Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">6</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <!-- Parameters -->
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-top: 8px;">
    <div class="stat-card">
      <div class="stat-label">Target Salt %%</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Target pH</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Target Days</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
  </div>

  <!-- Method -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Method / Process Steps</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Iterations -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Iteration Log</div>
  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:18px;">Ver</th>
      <th style="width:35px;">Date</th>
      <th>What Changed</th>
      <th style="width:55px;">Result</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">v1</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">v2</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">v3</td><td></td><td></td><td></td></tr>
  </table>

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def equipment_inventory():
    """Equipment and gear inventory"""
    pg = pn()
    return """<!-- PAGE %d: Equipment -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Equipment</span>
    <span class="sh-right">My Fermentation Kit</span>
  </div>

  <div class="page-title">Equipment &amp; Gear</div>
  <div class="page-subtitle">Know your kit</div>

  <div class="gear-card">
    <div class="gear-label">Jars &amp; Vessels</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Size / Volume</th><th>Quantity</th></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Airlocks, Weights &amp; Lids</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Size / Brand</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Tools &amp; Instruments</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Tool</th><th>Brand / Type</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Supplies (Salt, Water, Sugar)</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Item</th><th>Type / Brand</th><th>Spare?</th></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def tasting_journal():
    """Finished product tasting journal"""
    pg = pn()
    return """<!-- PAGE %d: Tasting Journal -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Tasting Journal</span>
    <span class="sh-right">Evaluate Finished Ferments</span>
  </div>

  <div class="page-title">Tasting Journal</div>
  <div class="page-subtitle">Record tasting notes for finished ferments</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Ferment / Batch</th>
      <th style="width:40px;">Date</th>
      <th style="width:30px;">Age</th>
      <th style="width:55px;">Aroma</th>
      <th>Flavor / Texture Notes</th>
      <th style="width:30px;">Rating</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">1</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">2</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">3</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">4</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">5</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">6</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">7</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">8</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Age: days/weeks/months since start | Aroma: sour/earthy/fruity/pungent/funky | Rating: 1-5 stars</div>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Pairing Ideas &amp; Uses</div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
  </div>

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def suppliers_log(page_of, total_pages):
    """Suppliers and ingredient sources"""
    pg = pn()
    return """<!-- PAGE %d: Suppliers -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Suppliers &amp; Sources</span>
    <span class="sh-right">Page %d of %d</span>
  </div>

  <div class="page-title">Suppliers &amp; Ingredient Sources</div>
  <div class="page-subtitle">Where to find the best supplies and cultures</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Name</th>
      <th style="width:60px;">Specialty</th>
      <th style="width:45px;">Quality</th>
      <th>Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">6</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">7</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">8</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">9</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">10</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">11</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B87333;">12</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Go-To Source</div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #B87333; text-transform: uppercase; min-width: 38px;">Name</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #B87333; text-transform: uppercase; min-width: 38px;">Why I Trust Them</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #B87333; text-transform: uppercase; min-width: 38px;">Usual Order</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_of, total_pages, page_no[0])


def favorites_summary():
    """Year-in-review and favorites page"""
    pg = pn()
    return """<!-- PAGE %d: Favorites -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Favorites &amp; Stats</span>
    <span class="sh-right">Your Fermentation Year in Review</span>
  </div>

  <div class="page-title">Fermentation Year in Review</div>
  <div class="page-subtitle">Fill in at the end of your fermentation journey</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Batches Made</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Cultures Active</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Success Rate</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Top 5 Ferments</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Ferment Name</th>
      <th style="width:55px;">Type</th>
      <th style="width:35px;">Rating</th>
      <th>Why It Stood Out</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Personal Discoveries</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Winner</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">Best Vegetable Ferment</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Kombucha Flavor</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Surprise / Happy Accident</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Most Improved Over Time</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Lesson Learned</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">What I Want to Try Next</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def notes_page():
    """Blank lined notes page"""
    pg = pn()
    lines = ""
    for _ in range(18):
        lines += '<div class="wline"></div>\n'

    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Notes</span>
    <span class="sh-right"></span>
  </div>

  <div class="page-title">Notes</div>
  <div class="page-subtitle">Recipes, ideas, and reminders</div>

  %s

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, lines, page_no[0])


def sketch_page():
    """Dot grid page for sketching recipe ideas"""
    pg = pn()
    return """<!-- PAGE %d: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Sketch Pad</span>
    <span class="sh-right">Recipes &amp; Process Maps</span>
  </div>

  <div class="page-title">Sketch Pad</div>
  <div class="page-subtitle">Draw recipe ratios, process flows, label designs</div>

  <div class="dot-grid" style="width: 100%%; height: 6.5in; border-radius: 4px;"></div>

  <div class="page-footer">
    <span>Fermentation Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def final_page():
    """Closing page"""
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="cover">
  <div class="glow-bg"></div>
  <div class="title-block">
    <div style="font-size: 20pt; font-weight: 700; color: #ffffff; margin-bottom: 10px;">Keep Fermenting</div>
    <div class="accent-bar"></div>
    <div class="subtitle" style="font-size: 10pt; color: #C4A04A; font-style: italic;">
      Every batch teaches you something new.<br>Trust your senses, trust the process,<br>and let time do its work.
    </div>
    <div style="margin-top: 30px;">
      <div class="tagline">More Shine Press</div>
    </div>
  </div>
</div>
""" % pg


# ============================================================
# MAIN — ASSEMBLE BOOK
# ============================================================

def main():
    pages = []

    # ---- Front Matter ----
    pages.append(cover())                          # 1: Cover
    pages.append(owner_page())                     # 2: Owner page

    # ---- Educational Reference ----
    pages.append(how_to_use())                     # 3: How to use
    pages.append(salt_brine_guide())               # 4: Salt & brine guide
    pages.append(fermentation_types_reference())   # 5: Types of fermentation
    pages.append(ph_timeline_reference())          # 6: pH & timeline guide
    pages.append(safety_reference())               # 7: Safety guidelines

    # ---- Section 1: Batch Logs ----
    pages.append(divider_section(1, "One", "Batch Logs", "40 fermentation batches &mdash; your personal records"))
    NUM_BATCHES = 40
    for i in range(1, NUM_BATCHES + 1):
        pages.append(batch_log_left(i))            # Left page: setup
        pages.append(batch_log_right(i))           # Right page: timeline & tasting

    # ---- Section 2: Cultures & Recipes ----
    pages.append(divider_section(2, "Two", "Cultures &amp; Recipes", "Track your starters and develop recipes"))
    pages.append(culture_registry(1, 3))
    pages.append(culture_registry(2, 3))
    pages.append(culture_registry(3, 3))
    pages.append(recipe_development())
    pages.append(recipe_development())

    # ---- Section 3: Equipment & Suppliers ----
    pages.append(divider_section(3, "Three", "Equipment &amp; Sources", "Your fermentation kit and suppliers"))
    pages.append(equipment_inventory())
    pages.append(suppliers_log(1, 2))
    pages.append(suppliers_log(2, 2))

    # ---- Section 4: Tasting & Favorites ----
    pages.append(divider_section(4, "Four", "Tasting &amp; Favorites", "Evaluate and celebrate your ferments"))
    pages.append(tasting_journal())
    pages.append(tasting_journal())
    pages.append(favorites_summary())

    # ---- Notes ----
    pages.append(sketch_page())
    for _ in range(6):
        pages.append(notes_page())

    # ---- Final ----
    pages.append(final_page())

    # Assemble HTML
    body_content = "\n".join(pages)
    total_pages = page_no[0]

    full_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>%s &mdash; More Shine Press</title>
<style>%s</style>
</head>
<body>
%s
</body>
</html>""" % (BOOK_TITLE, CSS, body_content)

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)

    print("Generated: %s" % HTML_FILE)
    print("Total pages: %d" % total_pages)

    # Print breakdown
    print("\nPage breakdown:")
    print("  Cover: 1")
    print("  Owner page: 1")
    print("  Reference (how-to, salt/brine, types, pH, safety): 5")
    print("  Section dividers: 4")
    print("  Batch logs (%d batches x 2 pages): %d" % (NUM_BATCHES, NUM_BATCHES * 2))
    print("  Culture registry: 3")
    print("  Recipe development: 2")
    print("  Equipment inventory: 1")
    print("  Suppliers log: 2")
    print("  Tasting journal: 2")
    print("  Favorites summary: 1")
    print("  Sketch page: 1")
    print("  Notes pages: 6")
    print("  Final page: 1")
    print("  TOTAL: %d" % total_pages)

    # Assert even page count for KDP
    assert total_pages % 2 == 0, "Page count %d is odd — KDP requires even" % total_pages


if __name__ == "__main__":
    main()
