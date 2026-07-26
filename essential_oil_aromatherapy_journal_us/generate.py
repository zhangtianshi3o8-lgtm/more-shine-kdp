#!/usr/bin/env python3
"""
Essential Oil & Aromatherapy Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Essential oil enthusiasts, wellness practitioners, DIY blenders
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "essential_oil_aromatherapy_journal_us_V1.0.html")

BOOK_TITLE = "Essential Oil & Aromatherapy Journal"
BOOK_SUBTITLE = "Track Every Blend, Every Oil, Every Benefit"

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
/* Deep charcoal: #161616, #1E1E1E */
/* Sage green: #7A8B6F, #8B9B7E, #A8B89C */
/* Gold accent: #C4A04A */
/* Warm cream: #FAF8F4, #F5F0E8 */
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
  background: linear-gradient(165deg, #161616 0%, #1E1E1E 30%, #161616 65%, #100F0F 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Sage/gold glow background */
.cover .glow-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #8B9B7E, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #8B9B7E, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 90% 40%, #8B9B7E, transparent),
    radial-gradient(ellipse 16px 10px at 40% 90%, #C4A04A, transparent);
}

/* ===== CSS Dropper Bottle Illustration ===== */
.cover .bottle-wrap {
  width: 100px; height: 170px;
  position: relative;
  margin: 0 auto 20px;
}

/* Bottle body */
.cover .bottle-body {
  width: 56px; height: 100px;
  position: absolute;
  top: 40px; left: 22px;
  background: linear-gradient(160deg,
    rgba(138,155,126,0.15) 0%,
    rgba(138,155,126,0.06) 40%,
    rgba(196,160,74,0.08) 80%,
    rgba(122,139,111,0.10) 100%);
  border: 1px solid rgba(196,160,74,0.35);
  border-radius: 6px 6px 4px 4px;
}

/* Bottle liquid inside (sage green) */
.cover .bottle-liquid {
  width: 50px; height: 60px;
  position: absolute;
  top: 76px; left: 25px;
  background: linear-gradient(180deg,
    rgba(138,155,126,0.25) 0%,
    rgba(122,139,111,0.35) 50%,
    rgba(100,117,92,0.30) 100%);
  border-radius: 3px 3px 4px 4px;
}

/* Bottle shine highlight */
.cover .bottle-shine {
  width: 5px; height: 60px;
  position: absolute;
  top: 50px; left: 30px;
  background: linear-gradient(180deg, rgba(250,248,244,0.4), rgba(250,248,244,0.05));
  border-radius: 50%;
}

/* Bottle neck */
.cover .bottle-neck {
  width: 22px; height: 18px;
  position: absolute;
  top: 26px; left: 39px;
  background: linear-gradient(160deg,
    rgba(138,155,126,0.12),
    rgba(138,155,126,0.04));
  border: 1px solid rgba(196,160,74,0.30);
  border-bottom: none;
}

/* Bottle cap (gold) */
.cover .bottle-cap {
  width: 26px; height: 16px;
  position: absolute;
  top: 12px; left: 37px;
  background: linear-gradient(180deg, #C4A04A, #A08438);
  border-radius: 3px 3px 1px 1px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.3);
}

/* Cap highlight */
.cover .bottle-cap-shine {
  width: 3px; height: 10px;
  position: absolute;
  top: 15px; left: 42px;
  background: rgba(250,248,244,0.4);
  border-radius: 50%;
}

/* Dropper bulb */
.cover .dropper-bulb {
  width: 20px; height: 14px;
  position: absolute;
  top: 0px; left: 40px;
  background: linear-gradient(180deg,
    rgba(196,160,74,0.3),
    rgba(196,160,74,0.12));
  border: 1px solid rgba(196,160,74,0.4);
  border-radius: 50% 50% 30% 30%;
}

/* Vapor/aroma lines rising from bottle */
.cover .vapor1 {
  width: 2px; height: 22px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.35), transparent);
  position: absolute;
  top: -12px; left: 42px;
  border-radius: 50%;
  transform: rotate(-8deg);
}
.cover .vapor2 {
  width: 2px; height: 28px;
  background: linear-gradient(180deg, transparent, rgba(138,155,126,0.30), transparent);
  position: absolute;
  top: -18px; left: 55px;
  border-radius: 50%;
  transform: rotate(6deg);
}
.cover .vapor3 {
  width: 2px; height: 20px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.20), transparent);
  position: absolute;
  top: -10px; left: 30px;
  border-radius: 50%;
  transform: rotate(-3deg);
}

/* Leaf decoration */
.cover .leaf-deco {
  position: absolute;
  width: 40px; height: 20px;
  opacity: 0.08;
}
.cover .leaf-deco.left {
  top: 140px; left: -15px;
  transform: rotate(-30deg);
}
.cover .leaf-deco.right {
  top: 140px; right: -15px;
  transform: rotate(30deg) scaleX(-1);
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
  color: #A8B89C;
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
    radial-gradient(ellipse 25px 15px at 80% 30%, #8B9B7E, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 25% 85%, #8B9B7E, transparent);
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
  border-bottom: 1.5px solid #7A8B6F;
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
  background: #7A8B6F;
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

/* ---- Field Grid ---- */
.field-grid {
  display: grid;
  gap: 6px;
  margin-bottom: 8px;
}
.field-row {
  display: flex;
  gap: 8px;
  align-items: baseline;
}
.field-label {
  font-size: 7.5pt;
  font-weight: 700;
  color: #161616;
  text-transform: uppercase;
  letter-spacing: 0.4pt;
  white-space: nowrap;
  min-width: 60px;
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
  border-left: 3px solid #7A8B6F;
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
  border: 1.5px solid #7A8B6F;
  border-radius: 50%;
  display: inline-block;
}

/* ---- Category Card ---- */
.flavor-cat {
  border: 1px solid #D8E0D2;
  border-radius: 4px;
  padding: 6px 8px;
  margin-bottom: 5px;
  background: #FCFAF7;
}
.flavor-cat-label {
  font-size: 7pt;
  font-weight: 700;
  color: #7A8B6F;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 3px;
}
.flavor-cat-notes {
  font-size: 7.5pt;
  color: #888;
  line-height: 1.5;
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
  color: #7A8B6F;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 4px;
}
.gear-card .gear-line {
  border-bottom: 0.5px solid #ddd;
  height: 16px;
  margin-bottom: 2px;
}

/* ---- Dot Grid ---- */
.dot-grid {
  background-image: radial-gradient(circle, #d0d0d0 1px, transparent 1px);
  background-size: 0.20in 0.20in;
  background-position: 0.10in 0.10in;
}

/* ---- Blend Recipe Card ---- */
.recipe-oil-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 3px;
}
.recipe-oil-num {
  width: 16px; height: 16px;
  border: 1px solid #7A8B6F;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 6.5pt;
  font-weight: 700;
  color: #7A8B6F;
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
  <div class="bottle-wrap">
    <div class="vapor1"></div>
    <div class="vapor2"></div>
    <div class="vapor3"></div>
    <div class="dropper-bulb"></div>
    <div class="bottle-cap"></div>
    <div class="bottle-cap-shine"></div>
    <div class="bottle-neck"></div>
    <div class="bottle-body"></div>
    <div class="bottle-liquid"></div>
    <div class="bottle-shine"></div>
  </div>
  <div class="title-block">
    <div class="main-title">%s</div>
    <div class="accent-bar"></div>
    <div class="subtitle">%s</div>
    <div class="features">
      <span class="feature-badge">40 Blend Recipes</span>
      <span class="feature-badge">Oil Inventory</span>
      <span class="feature-badge">Wellness Tracker</span>
      <span class="feature-badge">Dilution Guide</span>
    </div>
    <div class="tagline">For Wellness Seekers &amp; Essential Oil Enthusiasts</div>
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
      <div style="font-size: 8pt; font-weight: 700; color: #7A8B6F; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Oil</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #7A8B6F; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Preferred Diffuser</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #7A8B6F; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Collection Size</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #7A8B6F; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Carrier Oil of Choice</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
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
  <div class="page-subtitle">Make every drop count</div>

  <div class="info-box">
    <div class="info-title">Why Keep an Oil Journal?</div>
    The difference between using essential oils and mastering them is attention. A journal helps you discover which oils work best for you, track your blend recipes so they can be recreated, and build a personal wellness reference over time. Your journal becomes your own aromatherapy apothecary guide.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Tips for Better Blending</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Start with intention.</strong> Before blending, decide your purpose: relaxation, energy, focus, immune support, or something else. A clear intention guides your oil selection and helps you evaluate results.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Know your dilution rates.</strong> Always dilute essential oils in a carrier oil before applying to skin. A 2%% dilution (about 12 drops per ounce of carrier) is standard for adults. See the dilution guide on the next reference page.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Record every drop.</strong> Write down each oil and the exact number of drops as you blend. This is the only way to recreate a blend you love or adjust one that needs improvement.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Label and date everything.</strong> Mark each blend with its name, date created, ingredients, and intended use. Oils change over time &mdash; some blends improve, others lose potency.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Test and observe.</strong> After using a blend, note how you felt before and after. Did it help? How quickly? Any reaction? This feedback loop turns trial and error into genuine expertise.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #F5F0E8; border: 1px solid #D8E0D2; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #5A6B4F;">Safety Note:</strong> Always perform a patch test before using a new blend on skin. Keep oils away from eyes and sensitive areas. Consult a qualified practitioner for use during pregnancy, with children, or with medical conditions.
  </div>

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def dilution_guide():
    pg = pn()
    return """<!-- PAGE %d: Dilution Guide -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Dilution Guide</span>
  </div>

  <div class="page-title">Dilution Guide</div>
  <div class="page-subtitle">Safe ratios for every use</div>

  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Use Case</th>
      <th>Dilution</th>
      <th>Drops per 1 oz Carrier</th>
      <th>Notes</th>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Perfume / Pulse Points</td>
      <td>5%%</td>
      <td style="text-align: center;">~30</td>
      <td>Small area, short contact</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Adult Daily Use</td>
      <td>2%%</td>
      <td style="text-align: center;">~12</td>
      <td>Standard body application</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Adult Intensive / Targeted</td>
      <td>3-5%%</td>
      <td style="text-align: center;">18-30</td>
      <td>Short-term, localized area</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Face / Sensitive Skin</td>
      <td>1%%</td>
      <td style="text-align: center;">~6</td>
      <td>Dilute extra for face</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Children (2+)</td>
      <td>0.5-1%%</td>
      <td style="text-align: center;">3-6</td>
      <td>Use gentle oils only</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Bath</td>
      <td>Dispersed</td>
      <td style="text-align: center;">5-10</td>
      <td>Mix with salt/milk first</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Diffuser</td>
      <td>N/A</td>
      <td style="text-align: center;">3-8</td>
      <td>Per water reservoir</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #161616;">Massage Oil</td>
      <td>2-3%%</td>
      <td style="text-align: center;">12-18</td>
      <td>Large body area</td>
    </tr>
  </table>

  <div style="margin-top: 10px; padding: 8px 10px; background: #FAF8F4; border-left: 3px solid #7A8B6F; border-radius: 0 4px 4px 0; font-size: 8pt; color: #555; line-height: 1.5;">
    <strong style="color: #161616; text-transform: uppercase; font-size: 8pt; letter-spacing: 0.3pt;">Common Carrier Oils:</strong>
    Jojoba (closest to skin's sebum, long shelf life) &bull; Sweet Almond (versatile, lightweight) &bull; Fractionated Coconut (non-staining, stable) &bull; Argan (rich, nourishing) &bull; Rosehip Seed (regenerating, face) &bull; Olive (heavy, traditional)
  </div>

  <div style="margin-top: 8px; padding: 6px 10px; background: #FFF8E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 7.5pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Remember:</strong> Less is more with essential oils. Start with fewer drops and increase gradually. A 2%% dilution is roughly 12 drops per ounce (30 ml) of carrier oil.
  </div>

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def oil_categories_reference():
    pg = pn()
    categories = [
        ("Floral",
         "Lavender &bull; Rose &bull; Jasmine &bull; Geranium &bull; Ylang Ylang &bull; Chamomile (Roman &amp; German) &bull; Neroli &bull; Clary Sage"),
        ("Citrus",
         "Lemon &bull; Sweet Orange &bull; Grapefruit &bull; Bergamot &bull; Lime &bull; Tangerine &bull; Mandarin &bull; Petitgrain"),
        ("Herbaceous",
         "Rosemary &bull; Peppermint &bull; Basil &bull; Thyme &bull; Marjoram &bull; Tea Tree &bull; Oregano &bull; Lemongrass"),
        ("Woody / Earthy",
         "Sandalwood &bull; Cedarwood &bull; Vetiver &bull; Patchouli &bull; Pine &bull; Cypress &bull; Frankincense &bull; Myrrh"),
        ("Spicy",
         "Black Pepper &bull; Cinnamon &bull; Clove &bull; Cardamom &bull; Ginger &bull; Nutmeg &bull; Coriander &bull; Fennel"),
        ("Minty",
         "Peppermint &bull; Spearmint &bull; Eucalyptus &bull; Wintergreen"),
    ]

    rows = ""
    for cat, notes in categories:
        rows += """
      <div class="flavor-cat">
        <div class="flavor-cat-label">%s</div>
        <div class="flavor-cat-notes">%s</div>
      </div>""" % (cat, notes)

    return """<!-- PAGE %d: Oil Categories -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Oil Categories</span>
  </div>

  <div class="page-title">Essential Oil Categories</div>
  <div class="page-subtitle">Know your oil families and their properties</div>

  %s

  <div style="margin-top: 8px; padding: 6px 8px; background: #FAF8F4; border-radius: 3px; font-size: 7pt; color: #888; font-style: italic;">
    Oils within the same category generally blend well together. For complex blends, try combining 2-3 categories (e.g., floral + citrus + woody for a balanced aroma).
  </div>

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, rows, page_no[0])


def blending_notes_reference():
    pg = pn()
    return """<!-- PAGE %d: Blending Notes -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Blending Principles</span>
  </div>

  <div class="page-title">The Art of Blending</div>
  <div class="page-subtitle">Building balanced, harmonious blends</div>

  <div style="font-size: 8.5pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">The Note System</div>
    <div style="margin-bottom: 10px;">
      <strong>Top Notes (first impression):</strong> Citrus and mint oils. Light, fresh, evaporate quickly. Examples: Lemon, Bergamot, Peppermint, Sweet Orange. Use 20-30%% of your blend.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>Middle Notes (the heart):</strong> Floral and herbaceous oils. Form the core character. Examples: Lavender, Geranium, Rosemary, Tea Tree. Use 40-60%% of your blend.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>Base Notes (the anchor):</strong> Woody, earthy, and resin oils. Deep, slow to evaporate, long-lasting. Examples: Sandalwood, Vetiver, Patchouli, Cedarwood. Use 10-25%% of your blend.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #FAF8F4; border-left: 3px solid #C4A04A; border-radius: 0 4px 4px 0; font-size: 8pt; color: #555; line-height: 1.5;">
    <strong style="color: #161616; text-transform: uppercase; font-size: 8pt; letter-spacing: 0.3pt;">Classic Ratio: 30/50/20</strong><br>
    30%% top notes &bull; 50%% middle notes &bull; 20%% base notes. A versatile starting point for any blend. Adjust to taste &mdash; some prefer 25/45/30 for a longer-lasting aroma.
  </div>

  <div style="margin-top: 10px; font-size: 8.5pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Blending Tips</div>
    <div style="margin-bottom: 6px;">
      &bull; Start with 3-5 oils. More than that can create a muddy scent profile.
    </div>
    <div style="margin-bottom: 6px;">
      &bull; Let blends rest 24-48 hours before evaluating. Oils need time to integrate.
    </div>
    <div style="margin-bottom: 6px;">
      &bull; Keep a record of every blend &mdash; even failures. Learning what does not work is valuable.
    </div>
    <div style="margin-bottom: 6px;">
      &bull; Drop size varies by oil viscosity. Thicker oils (like Vetiver) form larger drops. Count drops, not milliliters, for consistency.
    </div>
  </div>

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def safety_reference():
    pg = pn()
    terms = [
        ("Phototoxic Oils", "Citrus oils (especially Bergamot, Lemon, Lime, Bitter Orange) can cause skin sensitivity when exposed to sunlight. Avoid direct sun for 12 hours after application to skin."),
        ("Hot Oils", "Cinnamon, Clove, Oregano, Thyme, and Cassia are &quot;hot&quot; oils that can cause burning or irritation. Always dilute heavily and patch-test before use."),
        ("Pregnancy &amp; Children", "Many oils are not recommended during pregnancy or for young children. Consult a qualified aromatherapist or healthcare provider. Generally avoid: Clary Sage, Rosemary, Sage, Wintergreen."),
        ("Pet Safety", "Tea Tree, Eucalyptus, Pennyroyal, Wintergreen, and Citrus oils can be toxic to pets (especially cats and birds). Research pet-safe oils before diffusing around animals."),
        ("Storage", "Store essential oils in dark glass bottles away from heat and light. Keep bottles tightly capped to prevent oxidation. Most oils last 2-3 years; citrus oils 1-2 years."),
        ("Ingestion", "Never ingest essential oils without professional guidance. Even small amounts can cause serious harm. Internal use requires supervision by a qualified practitioner."),
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
  <div class="page-subtitle">Enjoy essential oils responsibly</div>

  %s

  <div style="margin-top: 8px; padding: 6px 10px; background: #FFF0F0; border: 1px solid #E8C0C0; border-radius: 3px; font-size: 7.5pt; color: #888; font-style: italic;">
    <strong style="color: #8B3333;">Important:</strong> This journal is a personal tracking tool and does not provide medical advice. Always consult a healthcare professional for health concerns. Essential oils are complementary, not a replacement for medical treatment.
  </div>

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
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


def blend_log_left(session_num):
    """Left page of two-page blend spread — recipe details"""
    pg = pn()
    return """<!-- PAGE %d: Blend %d Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Blend #%02d</span>
    <span class="sh-right">Essential Oil Journal</span>
  </div>

  <div class="page-title">Blend Recipe #%02d</div>
  <div class="page-subtitle">Oils, carrier, and purpose</div>

  <!-- Blend Info -->
  <div style="background: #FAF8F4; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Time</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Blend Name</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Purpose</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Purpose checkboxes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Application Method</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Diffuser</span>
    <span class="check-item"><span class="check-box"></span> Topical</span>
    <span class="check-item"><span class="check-box"></span> Massage</span>
    <span class="check-item"><span class="check-box"></span> Bath</span>
    <span class="check-item"><span class="check-box"></span> Inhaler</span>
    <span class="check-item"><span class="check-box"></span> Roll-on</span>
    <span class="check-item"><span class="check-box"></span> Room Spray</span>
    <span class="check-item"><span class="check-box"></span> Other</span>
  </div>

  <!-- Carrier Oil -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Carrier Oil &amp; Amount</div>
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 8px;">
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Essential Oil Recipe -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Essential Oils &mdash; Record Each Oil and Drops</div>

  <div class="recipe-oil-row">
    <div class="recipe-oil-num">1</div>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    <span style="font-size: 7pt; color: #888; min-width: 20px;">drops</span>
    <div style="width: 30px; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div class="recipe-oil-row">
    <div class="recipe-oil-num">2</div>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    <span style="font-size: 7pt; color: #888; min-width: 20px;">drops</span>
    <div style="width: 30px; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div class="recipe-oil-row">
    <div class="recipe-oil-num">3</div>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    <span style="font-size: 7pt; color: #888; min-width: 20px;">drops</span>
    <div style="width: 30px; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div class="recipe-oil-row">
    <div class="recipe-oil-num">4</div>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    <span style="font-size: 7pt; color: #888; min-width: 20px;">drops</span>
    <div style="width: 30px; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div class="recipe-oil-row">
    <div class="recipe-oil-num">5</div>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    <span style="font-size: 7pt; color: #888; min-width: 20px;">drops</span>
    <div style="width: 30px; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div class="recipe-oil-row">
    <div class="recipe-oil-num">6</div>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    <span style="font-size: 7pt; color: #888; min-width: 20px;">drops</span>
    <div style="width: 30px; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Total drops -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-top: 6px; padding: 4px 8px; background: #F5F0E8; border-radius: 3px;">
    <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase;">Total Drops</span>
    <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    <span style="font-size: 7pt; font-weight: 700; color: #7A8B6F; text-transform: uppercase;">Dilution %%</span>
    <div style="width: 30px; border-bottom: 0.5px solid #aaa; height: 16px;"></div>
  </div>

  <div class="page-footer">
    <span>Blend #%02d &mdash; Recipe</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, session_num, session_num, session_num, session_num, page_no[0])


def blend_log_right(session_num):
    """Right page of two-page blend spread — aroma profile, notes, results"""
    pg = pn()
    return """<!-- PAGE %d: Blend %d Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Blend #%02d</span>
    <span class="sh-right">Aroma &amp; Results</span>
  </div>

  <div class="page-title">Blend Notes #%02d</div>
  <div class="page-subtitle">Aroma profile, effectiveness, and observations</div>

  <!-- Aroma Ratings (1-5 scale) -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Aroma Profile &mdash; Fill in circles (1 = weak, 5 = strong)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Top Note</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Middle Note</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Base Note</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Sweetness</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Strength</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Longevity</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>

  <!-- Aroma Character Checklist -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Aroma Character &mdash; Check What Applies</div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Floral</span>
    <span class="check-item"><span class="check-box"></span> Citrus</span>
    <span class="check-item"><span class="check-box"></span> Woody</span>
    <span class="check-item"><span class="check-box"></span> Herbal</span>
    <span class="check-item"><span class="check-box"></span> Minty</span>
    <span class="check-item"><span class="check-box"></span> Spicy</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Earthy</span>
    <span class="check-item"><span class="check-box"></span> Sweet</span>
    <span class="check-item"><span class="check-box"></span> Fresh</span>
    <span class="check-item"><span class="check-box"></span> Warm</span>
    <span class="check-item"><span class="check-box"></span> Calming</span>
    <span class="check-item"><span class="check-box"></span> Energizing</span>
  </div>

  <!-- Scent Description -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Scent Description</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Overall Rating -->
  <div style="display: flex; align-items: center; gap: 8px; margin-top: 8px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt;">Overall Rating</span>
    <span class="stars">&#10022; &#10022; &#10022; &#10022; &#10022;</span>
  </div>

  <!-- Effectiveness -->
  <div class="check-row" style="margin-bottom: 8px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Would Make Again</span>
    <span class="check-item"><span class="check-box"></span> Would Share</span>
    <span class="check-item"><span class="check-box"></span> New Favorite</span>
  </div>

  <!-- Detailed Notes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Results &amp; Observations</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Adjust Next Time -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">What to Adjust Next Time</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Blend #%02d &mdash; Notes</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, session_num, session_num, session_num, session_num, page_no[0])


def oil_inventory(page_of, total_pages):
    """Oil collection inventory page"""
    pg = pn()
    return """<!-- PAGE %d: Oil Inventory -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Oil Collection</span>
    <span class="sh-right">Page %d of %d</span>
  </div>

  <div class="page-title">My Oil Collection</div>
  <div class="page-subtitle">Track what you have, what you need, and what you love</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Oil Name</th>
      <th style="width:55px;">Category</th>
      <th style="width:32px;">Size</th>
      <th style="width:50px;">Brand</th>
      <th style="width:30px;">Rating</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">1</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">2</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">3</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">4</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">5</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">6</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">7</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">8</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">9</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">10</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">11</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">12</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Rating: 1-5 (5 = best) | Category: Floral/Citrus/Herbal/Woody/Spicy/Minty | Size: ml | Brand: Supplier or maker</div>

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_of, total_pages, page_no[0])


def wellness_tracker():
    """Daily wellness and oil usage tracker"""
    pg = pn()
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    rows = ""
    for d in days:
        rows += """
    <tr>
      <td style="font-weight:700;color:#7A8B6F;text-align:center;">%s</td>
      <td></td>
      <td></td>
      <td style="text-align:center;"><span class="check-box" style="vertical-align:middle;"></span></td>
      <td></td>
    </tr>""" % d

    return """<!-- PAGE %d: Wellness Tracker -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Wellness Tracker</span>
    <span class="sh-right">Weekly Log</span>
  </div>

  <div class="page-title">Weekly Wellness Tracker</div>
  <div class="page-subtitle">Track your daily oil use and how you feel</div>

  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 10px;">
    <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase;">Week of</span>
    <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 16px;"></div>
  </div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:30px;">Day</th>
      <th>Oils / Blends Used</th>
      <th style="width:60px;">Purpose</th>
      <th style="width:25px;">Mood</th>
      <th>Notes / How I Felt</th>
    </tr>
    %s
  </table>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Weekly Reflection</div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
  </div>

  <div style="margin-top: 8px; padding: 6px 8px; background: #FAF8F4; border-radius: 3px; font-size: 7pt; color: #888;">
    <strong style="color: #5A6B4F;">Mood Key:</strong> &#9786; Great &nbsp; &#9785; Okay &nbsp; &#9781; Low &nbsp; Or rate 1-5
  </div>

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, rows, page_no[0])


def suppliers_log(page_of, total_pages):
    """Favorite suppliers and shops"""
    pg = pn()
    return """<!-- PAGE %d: Suppliers -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Suppliers &amp; Shops</span>
    <span class="sh-right">Page %d of %d</span>
  </div>

  <div class="page-title">Oil Suppliers &amp; Shops</div>
  <div class="page-subtitle">Where to find quality oils</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Name</th>
      <th style="width:70px;">Specialty</th>
      <th style="width:55px;">Quality</th>
      <th>Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">6</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">7</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">8</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">9</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">10</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">11</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6F;">12</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Go-To Supplier</div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #7A8B6F; text-transform: uppercase; min-width: 38px;">Name</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #7A8B6F; text-transform: uppercase; min-width: 38px;">Why I Trust Them</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #7A8B6F; text-transform: uppercase; min-width: 38px;">Usual Order</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_of, total_pages, page_no[0])


def tools_accessories():
    """Diffusers, droppers, and accessories inventory"""
    pg = pn()
    return """<!-- PAGE %d: Tools -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Tools</span>
    <span class="sh-right">My Aromatherapy Kit</span>
  </div>

  <div class="page-title">Tools &amp; Accessories</div>
  <div class="page-subtitle">Know your kit</div>

  <div class="gear-card">
    <div class="gear-label">Diffusers</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Brand / Model</th><th>Room Size</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Application Tools</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Brand / Model</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Roller Bottles &amp; Containers</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Size</th><th>Quantity</th></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Carrier Oils &amp; Storage</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Item</th><th>Type / Size</th><th>Spare?</th></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def single_oil_profiles():
    """Single oil profile template page"""
    pg = pn()
    return """<!-- PAGE %d: Oil Profile -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Oil Profile</span>
    <span class="sh-right">Detailed Reference</span>
  </div>

  <div class="page-title">Oil Profile</div>
  <div class="page-subtitle">Deep dive into a single oil</div>

  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 10px;">
    <span style="font-size: 8pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 40px;">Oil Name</span>
    <div style="flex:1; border-bottom: 1px solid #161616; height: 20px;"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 10px;">
    <div style="background: #FAF8F4; padding: 6px 8px; border-radius: 4px;">
      <div style="font-size: 7pt; font-weight: 700; color: #7A8B6F; text-transform: uppercase; margin-bottom: 2px;">Botanical Name</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="background: #FAF8F4; padding: 6px 8px; border-radius: 4px;">
      <div style="font-size: 7pt; font-weight: 700; color: #7A8B6F; text-transform: uppercase; margin-bottom: 2px;">Plant Family</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="background: #FAF8F4; padding: 6px 8px; border-radius: 4px;">
      <div style="font-size: 7pt; font-weight: 700; color: #7A8B6F; text-transform: uppercase; margin-bottom: 2px;">Extraction Method</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="background: #FAF8F4; padding: 6px 8px; border-radius: 4px;">
      <div style="font-size: 7pt; font-weight: 700; color: #7A8B6F; text-transform: uppercase; margin-bottom: 2px;">Note (Top/Mid/Base)</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Aroma Description</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Primary Uses</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Blends Well With</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Safety / Precautions</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Personal Experience &amp; Notes</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def favorites_summary():
    """Year-in-review and favorites page"""
    pg = pn()
    return """<!-- PAGE %d: Favorites -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Favorites &amp; Stats</span>
    <span class="sh-right">Your Oil Year in Review</span>
  </div>

  <div class="page-title">Oil Year in Review</div>
  <div class="page-subtitle">Fill in at the end of your blending journey</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Blends Created</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Oils Collected</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Categories Used</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Top 5 Blends</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Blend Name</th>
      <th style="width:55px;">Purpose</th>
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
    <tr><td style="font-weight:700;color:#161616;">Favorite Single Oil</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Favorite Category</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Relaxation Blend</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Energy Blend</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best New Discovery</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">What I Want to Explore Next</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
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
  <div class="page-subtitle">Ideas, recipes, and reminders</div>

  %s

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, lines, page_no[0])


def sketch_page():
    """Dot grid page for sketching blend ideas"""
    pg = pn()
    return """<!-- PAGE %d: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Sketch Pad</span>
    <span class="sh-right">Blend Maps &amp; Ideas</span>
  </div>

  <div class="page-title">Sketch Pad</div>
  <div class="page-subtitle">Draw blend maps, plan oil pairings, sketch labels</div>

  <div class="dot-grid" style="width: 100%%; height: 6.5in; border-radius: 4px;"></div>

  <div class="page-footer">
    <span>Essential Oil &amp; Aromatherapy Journal</span>
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
    <div style="font-size: 20pt; font-weight: 700; color: #ffffff; margin-bottom: 10px;">Your Wellness Journey Continues</div>
    <div class="accent-bar"></div>
    <div class="subtitle" style="font-size: 10pt; color: #A8B89C; font-style: italic;">
      Every blend you create is a step toward<br>a more balanced, fragrant life.
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
    pages.append(dilution_guide())                 # 4: Dilution guide
    pages.append(oil_categories_reference())       # 5: Oil categories
    pages.append(blending_notes_reference())       # 6: Blending principles
    pages.append(safety_reference())               # 7: Safety

    # ---- Section 1: Blend Logs ----
    pages.append(divider_section(1, "One", "Blend Recipes", "40 blends &mdash; your personal apothecary"))
    NUM_BLENDS = 40
    for i in range(1, NUM_BLENDS + 1):
        pages.append(blend_log_left(i))            # Left page: recipe
        pages.append(blend_log_right(i))           # Right page: notes

    # ---- Section 2: Oil Collection ----
    pages.append(divider_section(2, "Two", "Oil Collection", "Your essential oil inventory"))
    pages.append(oil_inventory(1, 3))
    pages.append(oil_inventory(2, 3))
    pages.append(oil_inventory(3, 3))

    # ---- Section 3: Wellness Tracking ----
    pages.append(divider_section(3, "Three", "Wellness Tracker", "Daily use and mood journal"))
    pages.append(wellness_tracker())
    pages.append(wellness_tracker())
    pages.append(wellness_tracker())
    pages.append(wellness_tracker())

    # ---- Section 4: Oil Profiles ----
    pages.append(divider_section(4, "Four", "Oil Profiles", "Deep dive into individual oils"))
    pages.append(single_oil_profiles())
    pages.append(single_oil_profiles())
    pages.append(single_oil_profiles())
    pages.append(single_oil_profiles())

    # ---- Section 5: Suppliers & Tools ----
    pages.append(divider_section(5, "Five", "Suppliers &amp; Tools", "Your aromatherapy kit"))
    pages.append(suppliers_log(1, 2))
    pages.append(suppliers_log(2, 2))
    pages.append(tools_accessories())

    # ---- Section 6: Favorites & Notes ----
    pages.append(divider_section(6, "Six", "Favorites &amp; Notes", "Reflections and ideas"))
    pages.append(favorites_summary())
    pages.append(sketch_page())
    for _ in range(7):
        pages.append(notes_page())

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
    print("  Reference (how-to, dilution, categories, blending, safety): 5")
    print("  Section dividers: 6")
    print("  Blend logs (%d blends x 2 pages): %d" % (NUM_BLENDS, NUM_BLENDS * 2))
    print("  Oil inventory: 3")
    print("  Wellness tracker: 4")
    print("  Oil profiles: 4")
    print("  Suppliers log: 2")
    print("  Tools & accessories: 1")
    print("  Favorites summary: 1")
    print("  Sketch page: 1")
    print("  Notes pages: 7")
    print("  Final page: 1")
    print("  TOTAL: %d" % total_pages)

    # Assert even page count for KDP
    assert total_pages % 2 == 0, "Page count %d is odd — KDP requires even" % total_pages


if __name__ == "__main__":
    main()
