#!/usr/bin/env python3
"""
Seed Saving & Garden Genetics Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Homesteaders, permaculturists, heirloom gardeners, seed savers
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "seed_saving_garden_genetics_journal_us_V1.0.html")

BOOK_TITLE = "Seed Saving & Garden Genetics Journal"
BOOK_SUBTITLE = "Preserving Heritage, One Seed at a Time"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

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

/* Colors:
   Charcoal: #161616, #1E1E1E
   Harvest gold: #C4A04A, #D4B896
   Sage green: #5A7A4A, #7A9A6A, #9ABA8A
   Wheat: #D4B896
   Rust: #A05A30
*/

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
    radial-gradient(ellipse 26px 16px at 80% 15%, #7A9A6A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #7A9A6A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #D4B896, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #A05A30, transparent);
}

/* ===== Seed Envelope SVG ===== */
.cover .seed-wrap {
  width: 110px; height: 170px;
  position: relative;
  margin: 0 auto 18px;
}

/* Envelope */
.cover .env-body {
  width: 80px; height: 100px;
  position: absolute;
  top: 30px; left: 15px;
  background: linear-gradient(180deg,
    rgba(212,184,150,0.15) 0%,
    rgba(196,160,74,0.10) 100%);
  border: 1px solid rgba(196,160,74,0.30);
  border-radius: 2px 2px 4px 4px;
}

/* Envelope flap */
.cover .env-flap {
  width: 0; height: 0;
  position: absolute;
  top: 30px; left: 15px;
  border-left: 40px solid transparent;
  border-right: 40px solid transparent;
  border-top: 25px solid rgba(180,150,110,0.12);
}

/* Envelope label */
.cover .env-label {
  width: 40px; height: 20px;
  position: absolute;
  top: 55px; left: 35px;
  border: 1px solid rgba(196,160,74,0.20);
  border-radius: 1px;
  background: rgba(250,248,244,0.05);
}

/* Seeds spilling out */
.cover .seed1 {
  width: 6px; height: 8px;
  position: absolute;
  top: 18px; left: 52px;
  background: rgba(196,160,74,0.30);
  border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
  transform: rotate(-20deg);
}
.cover .seed2 {
  width: 5px; height: 7px;
  position: absolute;
  top: 12px; left: 44px;
  background: rgba(160,90,48,0.25);
  border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
  transform: rotate(15deg);
}
.cover .seed3 {
  width: 5px; height: 7px;
  position: absolute;
  top: 22px; left: 60px;
  background: rgba(122,154,106,0.25);
  border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
  transform: rotate(-35deg);
}
.cover .seed4 {
  width: 4px; height: 5px;
  position: absolute;
  top: 8px; left: 56px;
  background: rgba(196,160,74,0.20);
  border-radius: 50%;
}

/* Leaf accent */
.cover .leaf-1 {
  width: 18px; height: 10px;
  position: absolute;
  top: 65px; left: 2px;
  background: rgba(122,154,106,0.15);
  border-radius: 0 100% 0 100%;
  border: 1px solid rgba(122,154,106,0.20);
  transform: rotate(-30deg);
}
.cover .leaf-2 {
  width: 16px; height: 9px;
  position: absolute;
  top: 80px; right: 0px;
  background: rgba(122,154,106,0.12);
  border-radius: 0 100% 0 100%;
  border: 1px solid rgba(122,154,106,0.18);
  transform: rotate(20deg);
}

/* Sprout */
.cover .sprout {
  width: 2px; height: 15px;
  position: absolute;
  top: 15px; left: 54px;
  background: rgba(122,154,106,0.25);
}

.cover .sparkle1 {
  width: 4px; height: 4px;
  background: rgba(196,160,74,0.4);
  border-radius: 50%;
  position: absolute;
  top: 45px; left: 0px;
  box-shadow: 0 0 4px rgba(196,160,74,0.3);
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 21pt;
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
  color: #D4B896;
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
  border: 1px solid rgba(196,160,74,0.40);
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
  color: #7A9A6A;
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
    radial-gradient(ellipse 25px 15px at 80% 30%, #7A9A6A, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #D4B896, transparent),
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
  font-size: 22pt;
  color: #ffffff;
  font-weight: 700;
  line-height: 1.2;
  position: relative;
  padding: 0 0.6in;
}

.divider .div-sub {
  font-size: 11pt;
  color: #D4B896;
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
  border-bottom: 1.5px solid #C4A04A;
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

table.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
}
table.data-table th {
  background: #C4A04A;
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

.stars {
  font-size: 13pt;
  color: #ccc;
  letter-spacing: 2pt;
}

.info-box {
  background: #FAF8F4;
  border-left: 3px solid #C4A04A;
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
  border: 1.5px solid #C4A04A;
  border-radius: 50%;
  display: inline-block;
}

.prop-card {
  border: 1px solid #D8D0C0;
  border-radius: 4px;
  padding: 6px 8px;
  margin-bottom: 5px;
  background: #FCFAF7;
}
.prop-card-label {
  font-size: 7pt;
  font-weight: 700;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 3px;
}
.prop-card-value {
  font-size: 7.5pt;
  color: #888;
  line-height: 1.5;
}

.stat-card {
  text-align: center;
  padding: 6px 4px;
  background: #FAF8F4;
  border-radius: 4px;
  border: 1px solid #D8D0C0;
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
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 4px;
}

.dot-grid {
  background-image: radial-gradient(circle, #d0d0d0 1px, transparent 1px);
  background-size: 0.20in 0.20in;
  background-position: 0.10in 0.10in;
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
  <div class="seed-wrap">
    <div class="sparkle1"></div>
    <div class="leaf-1"></div>
    <div class="leaf-2"></div>
    <div class="sprout"></div>
    <div class="env-flap"></div>
    <div class="env-body"></div>
    <div class="env-label"></div>
    <div class="seed1"></div>
    <div class="seed2"></div>
    <div class="seed3"></div>
    <div class="seed4"></div>
  </div>
  <div class="title-block">
    <div class="main-title">%s</div>
    <div class="accent-bar"></div>
    <div class="subtitle">%s</div>
    <div class="features">
      <span class="feature-badge">40 Variety Logs</span>
      <span class="feature-badge">Pollination Guide</span>
      <span class="feature-badge">Germination Tests</span>
      <span class="feature-badge">Seed Library</span>
    </div>
    <div class="tagline">For Homesteaders &amp; Heritage Gardeners</div>
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
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Garden Zone</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Years Seed Saving</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Number of Varieties</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Crop</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Seed Saving Journal</span>
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
  <div class="page-subtitle">Build your personal seed bank, season by season</div>

  <div class="info-box">
    <div class="info-title">Why Save Seeds?</div>
    Every seed saved is a small act of preservation. By selecting the best plants from your garden and saving their seeds, you develop varieties adapted to your climate, preserve irreplaceable heritage genetics, and gain true food independence. A journal turns scattered experience into reliable knowledge.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Guidelines for Better Seed Saving</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Know your plant's pollination.</strong> Before saving seed, understand whether a variety is self-pollinating or cross-pollinating. This determines how many plants you need and whether isolation is required. The reference pages cover the most common garden crops.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Save from the best.</strong> Always select seeds from your healthiest, most productive plants. Mark these plants early and let them fully mature. The traits you select become the traits you cultivate.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Label everything.</strong> Unlabeled seeds are lost knowledge. Record variety name, date saved, source, and growing location on every envelope. Photograph the mother plant.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Dry thoroughly.</strong> Moisture is the enemy of seed storage. Dry seeds at room temperature in a well-ventilated space for 1-2 weeks before packaging. A simple bend test (seed snaps rather than bends) confirms dryness.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Test germination.</strong> Before relying on saved seed, test a small batch between damp paper towels. Record the germination rate in this journal so you know which batches to trust.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>6. Store cool, dark, and dry.</strong> Glass jars with silica gel packets in a cool basement or refrigerator dramatically extend seed viability. Record storage location in this journal.
    </div>
  </div>

  <div class="page-footer">
    <span>Seed Saving Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def pollination_reference():
    pg = pn()
    return """<!-- PAGE %d: Pollination Reference -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Pollination &amp; Isolation</span>
  </div>

  <div class="page-title">Pollination Guide</div>
  <div class="page-subtitle">How common crops pollinate &mdash; the key to pure seed</div>

  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th>Crop</th>
      <th style="width:32px;">Pollinated</th>
      <th style="width:28px;">Min. Plants</th>
      <th style="width:35px;">Isolation</th>
      <th>Notes</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Tomato</td>
      <td>Self</td>
      <td style="text-align:center;">1-5</td>
      <td style="text-align:center;">10 ft</td>
      <td>Mostly self-pollinating. Save from 1 plant OK for home use, 5+ for genetic diversity.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Pepper</td>
      <td>Self/Cross</td>
      <td style="text-align:center;">5+</td>
      <td style="text-align:center;">500 ft</td>
      <td>Can cross-pollinate. Isolate varieties or use blossom bags.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Bean (Common)</td>
      <td>Self</td>
      <td style="text-align:center;">10+</td>
      <td style="text-align:center;">20 ft</td>
      <td>Mostly self-pollinating. Rarely crosses. Easy for beginners.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Pea</td>
      <td>Self</td>
      <td style="text-align:center;">10+</td>
      <td style="text-align:center;">20 ft</td>
      <td>Self-pollinating. Very reliable. Great first seed-saving crop.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Lettuce</td>
      <td>Self</td>
      <td style="text-align:center;">5+</td>
      <td style="text-align:center;">20 ft</td>
      <td>Self-pollinating but can cross with wild lettuce.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Squash / Pumpkin</td>
      <td>Cross (Insect)</td>
      <td style="text-align:center;">5+</td>
      <td style="text-align:center;">1/2 mile</td>
      <td>Crosses within same species. Hand-pollinate for purity.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Corn</td>
      <td>Cross (Wind)</td>
      <td style="text-align:center;">200+</td>
      <td style="text-align:center;">1/2 mile</td>
      <td>Needs large population to avoid inbreeding depression.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Cucumber</td>
      <td>Cross (Bee)</td>
      <td style="text-align:center;">5+</td>
      <td style="text-align:center;">1/2 mile</td>
      <td>Crosses within same species. Hand-pollinate or isolate.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Melon</td>
      <td>Cross (Bee)</td>
      <td style="text-align:center;">5+</td>
      <td style="text-align:center;">1/2 mile</td>
      <td>Crosses with other melons, not watermelons.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Brassicas</td>
      <td>Cross (Insect)</td>
      <td style="text-align:center;">20+</td>
      <td style="text-align:center;">1/2 mile</td>
      <td>Broccoli, kale, cabbage, Brussels sprouts all intercross.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Carrot</td>
      <td>Cross (Insect)</td>
      <td style="text-align:center;">20+</td>
      <td style="text-align:center;">1/2 mile</td>
      <td>Biennial &mdash; needs 2 seasons. Crosses with wild Queen Anne's lace.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Onion</td>
      <td>Cross (Insect)</td>
      <td style="text-align:center;">20+</td>
      <td style="text-align:center;">1 mile</td>
      <td>Biennial. Produces seed in second year.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Spinach</td>
      <td>Cross (Wind)</td>
      <td style="text-align:center;">10+</td>
      <td style="text-align:center;">1/2 mile</td>
      <td>Dioecious (separate male/female plants). Wind pollinated.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Radish</td>
      <td>Cross (Insect)</td>
      <td style="text-align:center;">10+</td>
      <td style="text-align:center;">1/2 mile</td>
      <td>Crosses with wild radishes. Can be biennial in cold climates.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Sunflower</td>
      <td>Cross (Bee)</td>
      <td style="text-align:center;">5+</td>
      <td style="text-align:center;">1/2 mile</td>
      <td>Bees carry pollen far. Bag heads for purity.</td>
    </tr>
  </table>

  <div style="margin-top: 6px; padding: 5px 8px; background: #FFF8E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 6.5pt; color: #777; font-style: italic;">
    <strong style="color: #8B6914;">Key:</strong> Self = self-pollinating (easy to save). Cross = requires isolation or hand-pollination. Min. Plants = minimum for genetic health. Isolation = safe distance from other varieties of the same species. For home gardens under 1/2 mile isolation, use blossom bags or cages with hand pollination.
  </div>

  <div class="page-footer">
    <span>Seed Saving Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def processing_reference():
    pg = pn()
    return """<!-- PAGE %d: Processing Reference -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Seed Processing Methods</span>
  </div>

  <div class="page-title">Seed Processing Methods</div>
  <div class="page-subtitle">Dry vs wet processing &mdash; the right technique for each crop</div>

  <div style="font-size: 8pt; line-height: 1.6; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Dry Processing</div>
    <div style="margin-bottom: 4px;"><strong>For:</strong> Beans, peas, lettuce, brassicas, radish, corn, grains, herbs</div>
    <div style="margin-bottom: 4px;"><strong>1. Harvest:</strong> Leave pods/seed heads on the plant until fully dry and brown. Harvest before rain.</div>
    <div style="margin-bottom: 4px;"><strong>2. Thresh:</strong> Rub seed pods between hands or gently flail to release seeds from chaff.</div>
    <div style="margin-bottom: 4px;"><strong>3. Winnow:</strong> Pour seeds between two bowls in a light breeze or before a fan. Chaff blows away, clean seeds remain.</div>
    <div style="margin-bottom: 10px;"><strong>4. Screen:</strong> Use screens or sieves with appropriate mesh sizes to separate by size.</div>

    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Wet Processing</div>
    <div style="margin-bottom: 4px;"><strong>For:</strong> Tomatoes, cucumbers, melons, squash, peppers</div>
    <div style="margin-bottom: 4px;"><strong>1. Harvest:</strong> Pick fully ripe (often overripe) fruit. Cut open and scoop out seeds with surrounding pulp.</div>
    <div style="margin-bottom: 4px;"><strong>2. Ferment:</strong> Place seed/pulp mixture in a jar with a little water. Let ferment 2-4 days at room temperature. A mold layer forms on top &mdash; this breaks down germination inhibitors and disease.</div>
    <div style="margin-bottom: 4px;"><strong>3. Wash:</strong> After fermentation, add water. Viable seeds sink to the bottom; debris and non-viable seeds float. Pour off the floaters. Repeat until water runs clear.</div>
    <div style="margin-bottom: 4px;"><strong>4. Dry:</strong> Spread clean seeds on a glass plate, coffee filter, or screen. Dry at room temperature for 1-2 weeks. Do not dry in direct sun or in an oven.</div>
    <div style="margin-bottom: 10px;"><strong>5. Package:</strong> Store in labeled envelopes or jars once completely dry.</div>

    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Special Cases</div>
    <div style="margin-bottom: 4px;"><strong>Peppers:</strong> Do not need fermentation. Rinse seeds from flesh and dry directly.</div>
    <div style="margin-bottom: 4px;"><strong>Squash/Pumpkin:</strong> Rinse seeds in a strainer under running water, rubbing gently. No fermentation needed.</div>
    <div><strong>Biennials (carrot, onion, beet, cabbage):</strong> Need a cold period (vernalization) before flowering. Dig roots, store over winter, replant in spring for second-year seed.</div>
  </div>

  <div class="page-footer">
    <span>Seed Saving Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def germination_reference():
    pg = pn()
    return """<!-- PAGE %d: Germination Reference -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Germination Testing</span>
  </div>

  <div class="page-title">Germination Testing</div>
  <div class="page-subtitle">Test your seed viability before planting season</div>

  <div class="info-box">
    <div class="info-title">Why Test?</div>
    Seeds lose viability over time. A quick germination test tells you what percentage of your saved seeds will actually sprout, so you can plant thickly if the rate is low or confidently thin if it is high. This prevents wasted garden space and disappointment.
  </div>

  <div style="font-size: 8pt; line-height: 1.6; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Paper Towel Method</div>
    <div style="margin-bottom: 4px;"><strong>1.</strong> Count out exactly 10 or 100 seeds (makes percentage easy).</div>
    <div style="margin-bottom: 4px;"><strong>2.</strong> Dampen a paper towel (not dripping) and place seeds on one half.</div>
    <div style="margin-bottom: 4px;"><strong>3.</strong> Fold the towel over and place in a sealed plastic bag. Label with variety, date, and seed count.</div>
    <div style="margin-bottom: 4px;"><strong>4.</strong> Keep in a warm spot (65-75&deg;F). Check daily.</div>
    <div style="margin-bottom: 8px;"><strong>5.</strong> Count sprouted seeds after 7-14 days (varies by crop). Calculate: (sprouted &divide; total) &times; 100 = germination rate %%.</div>

    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Interpreting Results</div>
  </div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th>Rate</th>
      <th>Assessment</th>
      <th>Action</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#4A8B4A;text-align:center;">80-100%%</td>
      <td>Excellent &mdash; fresh, well-saved seed</td>
      <td>Plant at normal density</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#C4A04A;text-align:center;">60-79%%</td>
      <td>Good &mdash; viable but aging</td>
      <td>Plant slightly thicker than normal</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#D4AC0D;text-align:center;">40-59%%</td>
      <td>Fair &mdash; plant heavily</td>
      <td>Double seeding rate. Use soon.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#A05A30;text-align:center;">Below 40%%</td>
      <td>Poor &mdash; seed is old or was damaged</td>
      <td>Save remaining for difficult conditions, or compost</td>
    </tr>
  </table>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Expected Viability by Crop Type</div>
    <table class="data-table" style="font-size: 7.5pt;">
      <tr>
        <th>Crop</th>
        <th style="width:50px;">Years (good storage)</th>
      </tr>
      <tr><td style="font-weight:700;color:#161616;">Onion, Leek, Parsnip</td><td style="text-align:center;">1-2 years</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Corn, Spinach, Lettuce</td><td style="text-align:center;">2-3 years</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Bean, Pea, Carrot, Pepper</td><td style="text-align:center;">3-4 years</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Tomato, Cucumber, Squash</td><td style="text-align:center;">4-6 years</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Cabbage family, Radish</td><td style="text-align:center;">4-5 years</td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Seed Saving Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def storage_reference():
    pg = pn()
    return """<!-- PAGE %d: Storage Reference -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Storage &amp; Longevity</span>
  </div>

  <div class="page-title">Seed Storage Guide</div>
  <div class="page-subtitle">The three rules: cool, dark, dry</div>

  <div class="info-box">
    <div class="info-title">The Enemies of Seed Viability</div>
    Heat, moisture, and light degrade seeds over time. Every 10&deg;F decrease in storage temperature roughly doubles seed life. Every 1 percent decrease in seed moisture also doubles life. Ideal storage: below 50&deg;F and below 50%% humidity.
  </div>

  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th style="width:70px;">Method</th>
      <th>Setup</th>
      <th>Best For</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Room Temp</td>
      <td>Paper envelopes in a drawer or box. Cool, dark closet.</td>
      <td>1-3 year storage. Easy access. Most home seed savers.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Airtight Jar</td>
      <td>Glass jar with tight lid + silica gel packet. Cool basement.</td>
      <td>3-5 year storage. Protects from humidity.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Refrigerator</td>
      <td>Sealed jar/container (must be airtight to prevent condensation). With silica gel.</td>
      <td>5-10 year storage. Excellent for valuable seeds.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Freezer</td>
      <td>Completely dry seeds in airtight jar. No condensation allowed. Only open when at room temp.</td>
      <td>10+ year storage. For long-term backup of irreplaceable varieties.</td>
    </tr>
  </table>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Storage Tips</div>
    <div style="font-size: 8pt; line-height: 1.6; color: #444;">
      <div style="margin-bottom: 3px;">&bull; Use silica gel packets in jars to absorb moisture. Recharge them by baking at 200&deg;F for 2 hours.</div>
      <div style="margin-bottom: 3px;">&bull; Never store seeds in a hot shed, greenhouse, or car. Heat is the fastest killer.</div>
      <div style="margin-bottom: 3px;">&bull; Label every container with variety, date saved, and any notes. A seed library is useless if unlabeled.</div>
      <div style="margin-bottom: 3px;">&bull; Rotate your stock. Plant and refresh older seeds rather than letting them sit unused.</div>
      <div style="margin-bottom: 3px;">&bull; Keep a backup. If a variety is irreplaceable, store two samples in different locations.</div>
    </div>
  </div>

  <div style="margin-top: 10px; padding: 6px 10px; background: #F5F8F0; border: 1px solid #C8D8B8; border-radius: 3px; font-size: 7.5pt; color: #666; font-style: italic;">
    <strong style="color: #4A6B3E;">Moisture Check:</strong> Properly dried seeds should snap cleanly when bent, not flex. For large seeds like beans and peas, hit with a hammer &mdash; they should shatter, not mash. If seeds are still flexible, they need more drying time before storage.
  </div>

  <div class="page-footer">
    <span>Seed Saving Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def families_reference():
    pg = pn()
    return """<!-- PAGE %d: Plant Families -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Plant Families &amp; Crossing Rules</span>
  </div>

  <div class="page-title">Garden Plant Families</div>
  <div class="page-subtitle">What crosses with what &mdash; the essential reference</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px;">
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Solanaceae (Nightshade)</div>
      <div class="prop-card-value">Tomato, pepper, eggplant, potato. Mostly self-pollinating (tomato) or bee-pollinated (pepper/eggplant). Crosses within species only. Tomato varieties cross rarely; peppers and eggplants need isolation.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Fabaceae (Legume)</div>
      <div class="prop-card-value">Bean, pea, fava, soybean, peanut. Mostly self-pollinating. Very easy to save. Rarely crosses. The best crops for beginning seed savers.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Cucurbitaceae (Gourd)</div>
      <div class="prop-card-value">Squash, pumpkin, cucumber, melon, watermelon. Bee-pollinated. Crosses within species. Four squash species (maxima, moschata, pepo, argyrosperma) don't cross each other.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Brassicaceae (Mustard)</div>
      <div class="prop-card-value">Broccoli, kale, cabbage, Brussels sprouts, cauliflower, radish, arugula, turnip. Insect-pollinated. Most brassicas cross freely with each other. Needs isolation or caging.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Apiaceae (Umbel)</div>
      <div class="prop-card-value">Carrot, celery, parsley, parsnip, dill, fennel, cilantro. Insect-pollinated biennials. Carrot crosses with wild Queen Anne's lace. Most need 2 seasons to produce seed.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Alliaceae (Onion)</div>
      <div class="prop-card-value">Onion, leek, garlic, shallot, chive. Insect-pollinated biennials. Chives and garlic are propagated by division, not seed.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Amaranthaceae</div>
      <div class="prop-card-value">Spinach, beet, chard, amaranth. Wind-pollinated. Spinach is dioecious. Beets and chard cross with each other (same species).</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Asteraceae (Composite)</div>
      <div class="prop-card-value">Lettuce, sunflower, endive, chicory, artichoke. Mostly self-pollinating (lettuce) or insect-pollinated (sunflower). Lettuce is easy; sunflower needs isolation.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Poaceae (Grass)</div>
      <div class="prop-card-value">Corn, wheat, oats, barley, rice, rye. Wind-pollinated. Corn is especially challenging &mdash; needs 200+ plants and 1/2 mile isolation.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Lamiaceae (Mint)</div>
      <div class="prop-card-value">Basil, mint, oregano, thyme, sage, rosemary, lavender. Insect-pollinated. Many cross freely. Some are propagated by cuttings, not seed.</div>
    </div>
  </div>

  <div style="margin-top: 6px; padding: 5px 10px; background: #FFF8E8; border-radius: 3px; font-size: 7pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Rule of thumb:</strong> Plants only cross-pollinate within the same species, not just the same family. For example, Acorn squash and Zucchini are both Cucurbita pepo and will cross, but Butternut (C. moschata) will not cross with either.
  </div>

  <div class="page-footer">
    <span>Seed Saving Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def divider_section(num, label, title, subtitle):
    labels = ["One", "Two", "Three", "Four", "Five"]
    label_text = labels[num-1] if num <= 5 else label
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


def variety_log_left(variety_num):
    """Left page: variety identity and growout record"""
    pg = pn()
    return """<!-- PAGE %d: Variety %d Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Variety #%02d</span>
    <span class="sh-right">Identity &amp; Growout</span>
  </div>

  <div class="page-title">Variety #%02d &mdash; Identity</div>
  <div class="page-subtitle">Catalog this variety and its origin</div>

  <!-- Basic Info -->
  <div style="background: #FAF8F4; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Seed ID</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Variety Name</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Crop / Family</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Source / Origin</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Growout details -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Growout Record</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-bottom: 8px;">
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Pollination Type</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label"># Plants Grown</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Isolation Method</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Location / Bed</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
  </div>

  <!-- Selection criteria -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Selection Criteria &mdash; What Traits Did You Select For?</div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Flavor</span>
    <span class="check-item"><span class="check-box"></span> Yield</span>
    <span class="check-item"><span class="check-box"></span> Disease Resist.</span>
    <span class="check-item"><span class="check-box"></span> Early Maturity</span>
    <span class="check-item"><span class="check-box"></span> Size</span>
    <span class="check-item"><span class="check-box"></span> Color</span>
  </div>
  <div class="check-row" style="margin-bottom: 6px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Drought Tol.</span>
    <span class="check-item"><span class="check-box"></span> Cold Tol.</span>
    <span class="check-item"><span class="check-box"></span> Storage Life</span>
    <span class="check-item"><span class="check-box"></span> Pest Resist.</span>
    <span class="check-item"><span class="check-box"></span> Vigor</span>
    <span class="check-item"><span class="check-box"></span> Heirloom Purity</span>
  </div>

  <!-- Plant description -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Mother Plant Description</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Variety #%02d &mdash; Identity</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, variety_num, variety_num, variety_num, variety_num, page_no[0])


def variety_log_right(variety_num):
    """Right page: seed harvest, processing, storage, notes"""
    pg = pn()
    return """<!-- PAGE %d: Variety %d Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Variety #%02d</span>
    <span class="sh-right">Harvest &amp; Storage</span>
  </div>

  <div class="page-title">Variety #%02d &mdash; Seed Record</div>
  <div class="page-subtitle">Harvest, processing, viability, and storage</div>

  <!-- Harvest details -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Harvest Details</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">Harvest Date</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Processing Method</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Quantity Saved</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
  </div>

  <!-- Processing method -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Processing Method Used</div>
  <div class="check-row" style="margin-bottom: 6px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Dry (thresh/winnow)</span>
    <span class="check-item"><span class="check-box"></span> Wet (ferment/wash)</span>
    <span class="check-item"><span class="check-box"></span> Rinse Only</span>
    <span class="check-item"><span class="check-box"></span> Screen Separation</span>
  </div>

  <!-- Quality ratings -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Seed Quality &mdash; Rate 1 (Poor) to 5 (Excellent)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Purity</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Plumpness</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Cleanliness</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>

  <!-- Germination test -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Germination Test Results</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">Test Date</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label"># Tested</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">%% Sprouted</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
  </div>

  <!-- Storage -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Storage Location</div>
  <div class="check-row" style="margin-bottom: 6px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Room Temp</span>
    <span class="check-item"><span class="check-box"></span> Airtight Jar</span>
    <span class="check-item"><span class="check-box"></span> Refrigerator</span>
    <span class="check-item"><span class="check-box"></span> Freezer</span>
    <span class="check-item"><span class="check-box"></span> With Silica Gel</span>
  </div>

  <!-- Notes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Notes &amp; Observations</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Variety #%02d &mdash; Seed Record</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, variety_num, variety_num, variety_num, variety_num, page_no[0])


def seed_library_overview(page_of, total_pages):
    pg = pn()
    return """<!-- PAGE %d: Seed Library -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Seed Library</span>
    <span class="sh-right">Page %d of %d</span>
  </div>

  <div class="page-title">Seed Library Overview</div>
  <div class="page-subtitle">Complete inventory of saved seeds</div>

  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Variety</th>
      <th style="width:40px;">Crop</th>
      <th style="width:28px;">Year</th>
      <th style="width:28px;">Qty</th>
      <th style="width:25px;">Germ %%</th>
      <th style="width:30px;">Store</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Year: year saved | Qty: approx quantity (T/tablespoon, g/gram, oz) | Germ %%: germination test result | Store: R=Room, J=Jar, F=Fridge, Z=Freezer</div>

  <div class="page-footer">
    <span>Seed Saving Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_of, total_pages, page_no[0])


def trade_exchange_log():
    """Seed swap and exchange records"""
    pg = pn()
    return """<!-- PAGE %d: Trade Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Seed Swaps</span>
    <span class="sh-right">Trades &amp; Exchanges</span>
  </div>

  <div class="page-title">Seed Swap &amp; Exchange Log</div>
  <div class="page-subtitle">Track trades, gifts, and acquisitions</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th style="width:30px;">Date</th>
      <th>Variety</th>
      <th style="width:30px;">In/Out</th>
      <th>Trading Partner / Source</th>
      <th>Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Seed Swap Groups &amp; Communities</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Group / Event</th><th style="width:50px;">Frequency</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Seed Saving Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def wishlist():
    """Seed wishlist and acquisition plans"""
    pg = pn()
    return """<!-- PAGE %d: Wishlist -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Wishlist</span>
    <span class="sh-right">Seeds to Acquire</span>
  </div>

  <div class="page-title">Seed Wishlist</div>
  <div class="page-subtitle">Varieties to find, acquire, or breed</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Variety</th>
      <th style="width:40px;">Type</th>
      <th>Why I Want It</th>
      <th style="width:30px;">Priority</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Breeding / Adaptation Projects</div>
    <table class="data-table" style="font-size: 7.5pt;">
      <tr>
        <th style="width:18px;">#</th>
        <th>Project Name</th>
        <th>Goal (trait to develop)</th>
        <th style="width:40px;">Started</th>
      </tr>
      <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Seed Saving Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def favorites_summary():
    pg = pn()
    return """<!-- PAGE %d: Favorites -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Year in Review</span>
    <span class="sh-right">Reflections &amp; Favorites</span>
  </div>

  <div class="page-title">Seed Saving Year in Review</div>
  <div class="page-subtitle">Reflect on the season and plan the next</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Varieties Saved</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">New This Year</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Families Covered</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Best Varieties This Year</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Variety</th>
      <th style="width:30px;">Crop</th>
      <th>Why It Stands Out</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Lessons &amp; Discoveries</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Winner</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">Easiest to Save</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Germination</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Garden Performer</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Surprise</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Failure</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">Goals for Next Year</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Seed Saving Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def notes_page():
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
  <div class="page-subtitle">Observations, references, and reminders</div>
  %s
  <div class="page-footer">
    <span>Seed Saving Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, lines, page_no[0])


def sketch_page():
    pg = pn()
    return """<!-- PAGE %d: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Garden Layout</span>
    <span class="sh-right">Plot Planning</span>
  </div>
  <div class="page-title">Garden Layout &amp; Plot Plan</div>
  <div class="page-subtitle">Sketch garden beds, isolation distances, and planting locations</div>
  <div class="dot-grid" style="width: 100%%; height: 6.5in; border-radius: 4px;"></div>
  <div class="page-footer">
    <span>Seed Saving Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def final_page():
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="cover">
  <div class="glow-bg"></div>
  <div class="title-block">
    <div style="font-size: 18pt; font-weight: 700; color: #ffffff; margin-bottom: 10px;">Every Seed Is a Promise</div>
    <div class="accent-bar"></div>
    <div class="subtitle" style="font-size: 10pt; color: #D4B896; font-style: italic;">
      To the next harvest, the next gardener,<br>and the living chain of seed savers before us.
    </div>
    <div style="margin-top: 30px;">
      <div class="tagline">More Shine Press</div>
    </div>
  </div>
</div>
""" % pg


# ============================================================
# MAIN
# ============================================================

def main():
    pages = []

    # ---- Front Matter ----
    pages.append(cover())                          # 1: Cover
    pages.append(owner_page())                     # 2: Owner

    # ---- Reference Section ----
    pages.append(how_to_use())                     # 3: How to use
    pages.append(pollination_reference())          # 4: Pollination guide
    pages.append(processing_reference())           # 5: Processing methods
    pages.append(germination_reference())          # 6: Germination testing
    pages.append(storage_reference())              # 7: Storage & longevity
    pages.append(families_reference())             # 8: Plant families

    # ---- Section 1: Variety Logs ----
    pages.append(divider_section(1, "One", "Variety Records", "40 detailed variety logs &mdash; your personal seed database"))
    NUM_VARIETIES = 40
    for i in range(1, NUM_VARIETIES + 1):
        pages.append(variety_log_left(i))
        pages.append(variety_log_right(i))

    # ---- Section 2: Seed Library Management ----
    pages.append(divider_section(2, "Two", "Seed Library", "Inventory, swaps, and acquisition planning"))
    pages.append(seed_library_overview(1, 4))
    pages.append(seed_library_overview(2, 4))
    pages.append(seed_library_overview(3, 4))
    pages.append(seed_library_overview(4, 4))
    pages.append(trade_exchange_log())
    pages.append(trade_exchange_log())
    pages.append(wishlist())

    # ---- Section 3: Reflection & Notes ----
    pages.append(divider_section(3, "Three", "Reflection &amp; Notes", "Year in review and garden planning"))
    pages.append(favorites_summary())
    pages.append(sketch_page())
    for _ in range(5):
        pages.append(notes_page())

    # ---- Final ----
    pages.append(final_page())

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

    print("\nPage breakdown:")
    print("  Cover: 1")
    print("  Owner: 1")
    print("  Reference (how-to, pollination, processing, germination, storage, families): 6")
    print("  Section dividers: 3")
    print("  Variety logs (%d x 2 pages): %d" % (NUM_VARIETIES, NUM_VARIETIES * 2))
    print("  Seed library overview: 4")
    print("  Trade/exchange log: 2")
    print("  Wishlist: 1")
    print("  Year in review: 1")
    print("  Garden layout sketch: 1")
    print("  Notes pages: 5")
    print("  Final: 1")
    print("  TOTAL: %d" % total_pages)

    assert total_pages % 2 == 0, "Page count %d is odd — KDP requires even" % total_pages


if __name__ == "__main__":
    main()
