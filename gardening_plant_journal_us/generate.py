#!/usr/bin/env python3
"""
Gardening & Plant Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Home gardeners, plant enthusiasts, vegetable growers
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "gardening_plant_journal_us_V1.0.html")

BOOK_TITLE = "Gardening & Plant Journal"
BOOK_SUBTITLE = "Grow, Track, and Nurture Your Garden Through Every Season"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

# ============================================================
# CSS — Moleskine luxury: charcoal #161616 + gold #C4A04A
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
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #C4A04A, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 90% 40%, #C4A04A, transparent),
    radial-gradient(ellipse 16px 10px at 40% 90%, #C4A04A, transparent);
}

/* Leaf icon */
.cover .icon-wrap {
  width: 130px; height: 130px;
  position: relative;
  margin: 0 auto 16px;
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 28pt;
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
  color: #D4B896;
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
    radial-gradient(ellipse 25px 15px at 80% 30%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #C4A04A, transparent),
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
.section-header .sh-right { color: #aaa; }

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
table.data-table tr:nth-child(even) td { background: #FAF6F0; }

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

.info-box {
  background: #FAF6F0;
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
.rating-bar-circles { display: flex; gap: 4px; }
.rating-circle {
  width: 14px; height: 14px;
  border: 1.5px solid #C4A04A;
  border-radius: 50%;
  display: inline-block;
}

.info-card {
  border: 1px solid #E8DCC8;
  border-radius: 4px;
  padding: 8px 10px;
  margin-bottom: 6px;
  background: #FCFAF7;
}
.info-card .ic-label {
  font-size: 7pt;
  font-weight: 700;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 3px;
}
.info-card .ic-text {
  font-size: 7.5pt;
  color: #888;
  line-height: 1.5;
}

.stat-card {
  text-align: center;
  padding: 6px 4px;
  background: #FAF6F0;
  border-radius: 4px;
  border: 1px solid #E8DCC8;
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

.field-row {
  display: flex;
  gap: 8px;
  align-items: baseline;
}
.field-label {
  font-size: 7pt;
  font-weight: 700;
  color: #161616;
  text-transform: uppercase;
  letter-spacing: 0.4pt;
  white-space: nowrap;
  min-width: 54px;
}
.field-line {
  flex: 1;
  border-bottom: 0.5px solid #bbb;
  height: 14px;
}

.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4px 10px;
}
"""

# ============================================================
# PAGE BUILDERS
# ============================================================

def cover_page():
    return f'''
<!-- Page {pn()}: Cover -->
<div class="cover">
  <div class="glow-bg"></div>
  <div class="icon-wrap">
    <svg viewBox="0 0 130 130" width="130" height="130" xmlns="http://www.w3.org/2000/svg">
      <!-- Stem -->
      <path d="M 65 110 Q 65 80 65 50" stroke="#C4A04A" stroke-width="2" fill="none" opacity="0.5"/>
      <!-- Left leaf -->
      <path d="M 65 65 Q 30 55 25 30 Q 50 35 65 60 Z" stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.08)"/>
      <!-- Right leaf -->
      <path d="M 65 55 Q 100 45 105 20 Q 80 25 65 50 Z" stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.08)"/>
      <!-- Left leaf vein -->
      <path d="M 65 65 Q 50 50 35 35" stroke="#C4A04A" stroke-width="0.8" fill="none" opacity="0.4"/>
      <!-- Right leaf vein -->
      <path d="M 65 55 Q 80 42 95 28" stroke="#C4A04A" stroke-width="0.8" fill="none" opacity="0.4"/>
      <!-- Small bud at top -->
      <circle cx="65" cy="45" r="6" stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.1)"/>
      <!-- Soil mound -->
      <path d="M 40 110 Q 65 100 90 110" stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.06)"/>
    </svg>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">Plant Inventory</span>
      <span class="feature-badge">Seasonal Planner</span>
      <span class="feature-badge">Harvest Log</span>
      <span class="feature-badge">Pest Tracker</span>
    </div>
    <div class="tagline">For Home Gardeners &amp; Plant Lovers</div>
  </div>
  <div class="publisher">More Shine Press</div>
</div>
'''


def owner_page():
    return f'''
<!-- Page {pn()}: Owner -->
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
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Garden Name / Location</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">USDA Hardiness Zone</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Garden Type</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Years Gardening</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Gardening &amp; Plant Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def how_to_use():
    return f'''
<!-- Page {pn()}: How to Use -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Getting Started</span>
    <span class="sh-right">More Shine Press</span>
  </div>

  <div class="page-title">How to Use This Journal</div>
  <div class="page-subtitle">Your garden's story, told season by season</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Garden Journal?</div>
    A garden journal is the secret weapon of every great gardener. It captures what you planted, when, where, and how it performed &mdash; the details that fade from memory but make all the difference next year. Your journal becomes a personal gardening manual written by experience.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Tips for Better Gardening</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Know your zone.</strong> Your USDA Hardiness Zone determines what will thrive in your climate. Find it at planthardiness.ars.usda.gov, then choose plants suited to your zone for effortless success.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Track your seasons.</strong> First and last frost dates, planting times, and bloom periods vary every year. Write them down so you can plan earlier and smarter each season.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Record what works.</strong> Note which varieties thrived and which struggled. Next year's seed orders will be faster, cheaper, and more productive because you remembered.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Watch the weather.</strong> Temperature, rainfall, and sunlight shape your garden. Your weather notes reveal patterns and help you protect plants before problems hit.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Sketch your layout.</strong> A simple garden map helps you rotate crops, avoid crowding, and plan succession planting. You will catch mistakes on paper that cost money in soil.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Companion Planting:</strong> Some plants grow better together. Basil repels tomato pests, marigolds deter nematodes, and the Three Sisters (corn, beans, squash) support each other beautifully.
  </div>

  <div class="page-footer">
    <span>Gardening &amp; Plant Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def hardiness_zones():
    zones = [
        ("Zone 3", "&minus;40 to &minus;35&deg;F", "Very short season. Cool-weather crops: kale, spinach, peas, radishes. Start seeds indoors."),
        ("Zone 4", "&minus;35 to &minus;25&deg;F", "Short season. Apples, potatoes, carrots, brassicas. Mulch heavily for winter protection."),
        ("Zone 5", "&minus;25 to &minus;20&deg;F", "Moderate season. Tomatoes, peppers, squash, herbs. Last frost ~mid-May."),
        ("Zone 6", "&minus;10 to &minus;5&deg;F", "Longer season. Most vegetables thrive. Last frost ~late April. Great for perennials."),
        ("Zone 7", "0 to 5&deg;F", "Long growing season. Figs, pecan, many perennials. Last frost ~mid-April."),
        ("Zone 8", "10 to 15&deg;F", "Mild winters. Citrus (outdoor), avocado, olive. Nearly year-round gardening possible."),
        ("Zone 9", "20 to 25&deg;F", "Subtropical. Citrus, bananas, avocados. Very long season. Protect from rare frost."),
        ("Zone 10", "30 to 35&deg;F", "Tropical. Mangoes, papaya, coffee. No freezing temperatures. Year-round growing."),
    ]

    rows = ""
    for zone, temp, desc in zones:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 50px; font-size: 8pt; font-weight: 700; color: #161616;">{zone}</div>
        <div style="min-width: 75px; font-size: 7pt; color: #C4A04A; font-weight: 700;">{temp}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Hardiness Zones -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">USDA Hardiness Zones</span>
  </div>

  <div class="page-title">USDA Hardiness Zone Guide</div>
  <div class="page-subtitle">Know your zone, grow with confidence</div>

  {rows}

  <div style="margin-top: 8px; padding: 6px 8px; background: #FAF6F0; border-radius: 3px; font-size: 7pt; color: #888; font-style: italic;">
    Find your zone at planthardiness.ars.usda.gov. Choose plants rated for your zone or colder for best results.
  </div>

  <div class="page-footer">
    <span>Gardening &amp; Plant Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def planting_calendar():
    seasons = [
        ("Spring Tasks (Mar&ndash;May)",
         "Prepare beds &bull; Start seeds indoors &bull; Plant cool-season crops (peas, lettuce, spinach) &bull; Transplant seedlings after last frost &bull; Prune fruit trees &bull; Apply mulch &bull; Set up trellises &bull; Divide perennials"),
        ("Summer Tasks (Jun&ndash;Aug)",
         "Water deeply &amp; consistently &bull; Harvest vegetables &bull; Deadhead flowers &bull; Monitor for pests &bull; Stake tall plants &bull; Succession plant &bull; Fertilize heavy feeders &bull; Weed regularly"),
        ("Fall Tasks (Sep&ndash;Nov)",
         "Plant garlic &amp; bulbs &bull; Harvest remaining crops &bull; Clean up garden beds &bull; Compost leaves &bull; Plant cover crops &bull; Protect tender plants &bull; Clean and oil tools &bull; Plan next year's garden"),
        ("Winter Tasks (Dec&ndash;Feb)",
         "Order seeds &bull; Start seeds indoors (late winter) &bull; Plan garden layout &bull; Sharpen and repair tools &bull; Prune dormant trees &bull; Review journal notes &bull; Build new beds &bull; Dream big"),
    ]

    rows = ""
    for season, tasks in seasons:
        rows += f'''
      <div class="info-card">
        <div class="ic-label">{season}</div>
        <div class="ic-text">{tasks}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Planting Calendar -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Seasonal Calendar</span>
  </div>

  <div class="page-title">Seasonal Planting Calendar</div>
  <div class="page-subtitle">What to do in each season</div>

  {rows}

  <div class="page-footer">
    <span>Gardening &amp; Plant Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def companion_planting():
    companions = [
        ("Tomatoes", "Basil, marigold, carrots, onions, parsley", "Fennel, cabbage, broccoli, corn"),
        ("Peppers", "Basil, onions, carrots, okra, petunias", "Beans, cabbage, Brussels sprouts"),
        ("Cucumbers", "Radishes, beans, corn, sunflowers, dill", "Sage, potatoes, aromatic herbs"),
        ("Lettuce", "Carrots, radishes, strawberries, chervil", "Cabbage family, broccoli"),
        ("Beans", "Corn, squash, carrots, cucumbers, strawberries", "Onions, garlic, peppers"),
        ("Squash", "Corn, beans, radishes, nasturtiums, marigolds", "Potatoes"),
        ("Carrots", "Tomatoes, lettuce, onions, rosemary, sage", "Dill, parsnips"),
        ("Herbs", "Most vegetables (especially roses with garlic)", "Fennel (inhibits most plants)"),
    ]

    rows = ""
    for crop, good, bad in companions:
        rows += f'''
      <div style="display: grid; grid-template-columns: 80px 1fr 1fr; gap: 6px; margin-bottom: 4px; padding: 5px 8px; border-left: 2px solid #C4A04A; background: #FCFAF7; border-radius: 0 3px 3px 0;">
        <div style="font-size: 8pt; font-weight: 700; color: #161616;">{crop}</div>
        <div style="font-size: 7pt; color: #2A7A2A; line-height: 1.4;">&#10003; {good}</div>
        <div style="font-size: 7pt; color: #B04040; line-height: 1.4;">&#10007; {bad}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Companion Planting -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Companion Planting</span>
  </div>

  <div class="page-title">Companion Planting Guide</div>
  <div class="page-subtitle">Plant friends together, keep enemies apart</div>

  <div style="display: grid; grid-template-columns: 80px 1fr 1fr; gap: 6px; margin-bottom: 6px; font-size: 7pt; font-weight: 700; text-transform: uppercase; color: #999; padding: 0 8px;">
    <div>Crop</div>
    <div style="color: #2A7A2A;">Good Companions</div>
    <div style="color: #B04040;">Avoid Planting With</div>
  </div>

  {rows}

  <div class="page-footer">
    <span>Gardening &amp; Plant Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def divider_section(num, label, title, subtitle):
    labels = ["One", "Two", "Three", "Four", "Five", "Six", "Seven"]
    label_text = labels[num-1] if num <= 7 else label
    return f'''
<!-- Page {pn()}: Divider -->
<div class="divider">
  <div class="div-glow"></div>
  <div class="div-num">{num:02d}</div>
  <div class="div-label">Part {label_text}</div>
  <div class="div-title">{title}</div>
  <div class="div-sub">{subtitle}</div>
</div>
'''


def plant_inventory_left(entry_num):
    """Left page: plant details"""
    return f'''
<!-- Page {pn()}: Plant {entry_num} Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Plant #{entry_num:02d}</span>
    <span class="sh-right">Gardening &amp; Plant Journal</span>
  </div>

  <div class="page-title">Plant #{entry_num:02d}</div>
  <div class="page-subtitle">Plant Details &amp; Growing Conditions</div>

  <!-- Plant Info -->
  <div style="background: #FAF6F0; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Plant Name</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Variety</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Type</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Source</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Price</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Date Planted</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Location</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Plant Type -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Plant Type</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Vegetable</span>
    <span class="check-item"><span class="check-box"></span> Fruit</span>
    <span class="check-item"><span class="check-box"></span> Herb</span>
    <span class="check-item"><span class="check-box"></span> Flower</span>
    <span class="check-item"><span class="check-box"></span> Shrub</span>
    <span class="check-item"><span class="check-box"></span> Tree</span>
    <span class="check-item"><span class="check-box"></span> Indoor</span>
    <span class="check-item"><span class="check-box"></span> Succulent</span>
  </div>

  <!-- Sun / Water -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Sunlight Needs</div>
  <div class="check-row" style="margin-bottom: 10px;">
    <span class="check-item"><span class="check-box"></span> Full Sun (6+ hr)</span>
    <span class="check-item"><span class="check-box"></span> Partial Sun (3&ndash;6 hr)</span>
    <span class="check-item"><span class="check-box"></span> Shade (&lt;3 hr)</span>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Water Needs</div>
  <div class="check-row" style="margin-bottom: 10px;">
    <span class="check-item"><span class="check-box"></span> Heavy (daily)</span>
    <span class="check-item"><span class="check-box"></span> Moderate (2&ndash;3x/week)</span>
    <span class="check-item"><span class="check-box"></span> Light (weekly)</span>
    <span class="check-item"><span class="check-box"></span> Drought-tolerant</span>
  </div>

  <!-- Growing conditions -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Soil &amp; Spacing</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px 10px;">
    <div class="field-row"><span class="field-label">Soil Type</span><div class="field-line"></div></div>
    <div class="field-row"><span class="field-label">pH</span><div class="field-line"></div></div>
    <div class="field-row"><span class="field-label">Spacing</span><div class="field-line"></div></div>
    <div class="field-row"><span class="field-label">Depth</span><div class="field-line"></div></div>
  </div>

  <div class="page-footer">
    <span>Plant #{entry_num:02d} &mdash; Details</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def plant_inventory_right(entry_num):
    """Right page: care log, harvest, notes"""
    return f'''
<!-- Page {pn()}: Plant {entry_num} Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Plant #{entry_num:02d}</span>
    <span class="sh-right">Care Log &amp; Notes</span>
  </div>

  <div class="page-title">Plant #{entry_num:02d}</div>
  <div class="page-subtitle">Care, growth, and observations</div>

  <!-- Growth Timeline -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Key Milestones</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px 10px; margin-bottom: 10px;">
    <div class="field-row"><span class="field-label">Seedling</span><div class="field-line"></div></div>
    <div class="field-row"><span class="field-label">Transplant</span><div class="field-line"></div></div>
    <div class="field-row"><span class="field-label">First Bloom</span><div class="field-line"></div></div>
    <div class="field-row"><span class="field-label">First Harvest</span><div class="field-line"></div></div>
  </div>

  <!-- Care Log -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Watering &amp; Feeding Schedule</div>
  <table class="data-table" style="font-size: 7pt; margin-bottom: 10px;">
    <tr><th style="width:62px;">Date</th><th>Action (Water/Fertilize/Prune)</th><th style="width:48px;">Amount</th></tr>
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
  </table>

  <!-- Pests / Problems -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Pests &amp; Problems</div>
  <table class="data-table" style="font-size: 7pt; margin-bottom: 10px;">
    <tr><th style="width:62px;">Date</th><th>Problem / Pest</th><th>Treatment &amp; Result</th></tr>
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
  </table>

  <!-- Harvest Record -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Harvest Record</div>
  <table class="data-table" style="font-size: 7pt; margin-bottom: 8px;">
    <tr><th style="width:62px;">Date</th><th>Quantity / Yield</th><th style="width:50px;">Quality</th></tr>
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
  </table>

  <!-- Notes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Notes &amp; Observations</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Plant #{entry_num:02d} &mdash; Care Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def garden_layout():
    """Grid-based garden layout sketch page"""
    return f'''
<!-- Page {pn()}: Garden Layout -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Garden Layout</span>
    <span class="sh-right">Map Your Beds</span>
  </div>

  <div class="page-title">Garden Layout Map</div>
  <div class="page-subtitle">Sketch your beds, rows, and plant locations</div>

  <!-- Grid background -->
  <div style="width: 100%; height: 6.0in; background: #FCFAF7; border: 1px solid #C4A04A; border-radius: 4px; position: relative;
    background-image:
      linear-gradient(0deg, transparent 48%, rgba(196,160,74,0.12) 50%, transparent 52%),
      linear-gradient(90deg, transparent 48%, rgba(196,160,74,0.12) 50%, transparent 52%);
    background-size: 0.35in 0.35in;">
  </div>

  <div style="margin-top: 8px; display: grid; grid-template-columns: 1fr 1fr; gap: 4px 10px;">
    <div class="field-row"><span class="field-label">Season</span><div class="field-line"></div></div>
    <div class="field-row"><span class="field-label">Year</span><div class="field-line"></div></div>
  </div>

  <div style="margin-top: 6px; font-size: 6.5pt; color: #aaa; font-style: italic;">
    Use N/S/E/W to orient your map. Mark permanent features (fences, paths, trees) and rotate crop locations each season.
  </div>

  <div class="page-footer">
    <span>Gardening &amp; Plant Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def monthly_tasks(month_name):
    """Monthly task planner — by season"""
    return f'''
<!-- Page {pn()}: Monthly Tasks {month_name} -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">{month_name}</span>
    <span class="sh-right">Monthly Garden Tasks</span>
  </div>

  <div class="page-title">{month_name} Tasks</div>
  <div class="page-subtitle">Plan, plant, and maintain this month</div>

  <!-- Weather -->
  <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Weather Notes</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4px 10px; margin-bottom: 10px;">
    <div class="field-row"><span class="field-label">Temp</span><div class="field-line"></div></div>
    <div class="field-row"><span class="field-label">Rain</span><div class="field-line"></div></div>
    <div class="field-row"><span class="field-label">Sun</span><div class="field-line"></div></div>
  </div>

  <!-- Task Table -->
  <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">This Month's Tasks</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:22px;">#</th>
      <th>Task</th>
      <th style="width:50px;">Target Date</th>
      <th style="width:22px;">Done</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
  </table>

  <!-- Observations -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Observations</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>{month_name} &mdash; Garden Tasks</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def harvest_log(page_of, total_pages):
    """Harvest log — what you picked and how much"""
    return f'''
<!-- Page {pn()}: Harvest Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Harvest Log</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Harvest Log</div>
  <div class="page-subtitle">Record what you grew, picked, and preserved</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Crop</th>
      <th style="width:50px;">Date</th>
      <th style="width:48px;">Quantity</th>
      <th style="width:36px;">Unit</th>
      <th>Notes / Quality</th>
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

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Unit: lb / oz / count / bunch / basket</div>

  <div class="page-footer">
    <span>Gardening &amp; Plant Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def seed_order_log():
    """Seed and supply order tracker"""
    return f'''
<!-- Page {pn()}: Seed Order Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Seed &amp; Supply Orders</span>
    <span class="sh-right">Order Tracker</span>
  </div>

  <div class="page-title">Seed &amp; Supply Orders</div>
  <div class="page-subtitle">Track your seed purchases and sources</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Seed / Supply</th>
      <th style="width:50px;">Variety</th>
      <th style="width:50px;">Source</th>
      <th style="width:36px;">Qty</th>
      <th style="width:40px;">Price</th>
      <th style="width:24px;">&#10003;</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">13</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">14</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">15</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div class="page-footer">
    <span>Gardening &amp; Plant Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def pest_disease_log():
    """Pest and disease tracker"""
    return f'''
<!-- Page {pn()}: Pest & Disease Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Pest &amp; Disease Tracker</span>
    <span class="sh-right">Problem Log</span>
  </div>

  <div class="page-title">Pest &amp; Disease Tracker</div>
  <div class="page-subtitle">Identify problems early and track treatments</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Date</th>
      <th>Plant Affected</th>
      <th>Problem (Pest/Disease)</th>
      <th>Treatment</th>
      <th style="width:30px;">Resolved?</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div class="page-footer">
    <span>Gardening &amp; Plant Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def garden_expenses():
    """Garden expenses and budget tracker"""
    return f'''
<!-- Page {pn()}: Garden Expenses -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Garden Expenses</span>
    <span class="sh-right">Budget Tracker</span>
  </div>

  <div class="page-title">Garden Expense Tracker</div>
  <div class="page-subtitle">Track spending on your garden</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Date</th>
      <th>Item</th>
      <th style="width:52px;">Category</th>
      <th style="width:40px;">Amount</th>
      <th>Source / Notes</th>
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

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Category: Seeds/Plants &bull; Soil/Compost &bull; Tools &bull; Fertilizer &bull; Pots &bull; Pest Control &bull; Other</div>

  <div class="page-footer">
    <span>Gardening &amp; Plant Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def year_review():
    """Year-end garden review"""
    return f'''
<!-- Page {pn()}: Year Review -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Year-End Review</span>
    <span class="sh-right">Reflect &amp; Plan Ahead</span>
  </div>

  <div class="page-title">Garden Year in Review</div>
  <div class="page-subtitle">Celebrate your successes and learn for next year</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="text-align:center;padding:10px 6px;">
      <div class="stat-label">Plants Grown</div>
      <div class="stat-value" style="font-size: 16pt;"></div>
    </div>
    <div class="stat-card" style="text-align:center;padding:10px 6px;">
      <div class="stat-label">Total Harvest</div>
      <div class="stat-value" style="font-size: 16pt;"></div>
    </div>
    <div class="stat-card" style="text-align:center;padding:10px 6px;">
      <div class="stat-label">Money Spent</div>
      <div class="stat-value" style="font-size: 16pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Biggest Success This Year</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 6px;">Biggest Challenge / Failure</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 6px;">Top 5 Varieties to Grow Again</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 6px;">What to Try Next Year</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Gardening &amp; Plant Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def notes_page(page_num):
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

  <div class="page-title">Garden Notes</div>
  <div class="page-subtitle">Observations, ideas, and reminders</div>

  {lines}

  <div class="page-footer">
    <span>Gardening &amp; Plant Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


# ============================================================
# MAIN
# ============================================================
def main():
    pages = []

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    # ---- Front Matter ----
    pages.append(cover_page())                          # 1: Cover
    pages.append(owner_page())                           # 2: Owner page

    # ---- Reference Section ----
    pages.append(how_to_use())                           # 3: How to use
    pages.append(hardiness_zones())                      # 4: Hardiness zones
    pages.append(planting_calendar())                    # 5: Seasonal calendar
    pages.append(companion_planting())                   # 6: Companion planting

    # ---- Section 1: Plant Inventory ----
    pages.append(divider_section(1, "One", "Plant Inventory", "30 plants &mdash; detailed records"))
    NUM_PLANTS = 30
    for i in range(1, NUM_PLANTS + 1):
        pages.append(plant_inventory_left(i))
        pages.append(plant_inventory_right(i))

    # ---- Section 2: Garden Layout ----
    pages.append(divider_section(2, "Two", "Garden Layout", "Map your beds and rows"))
    pages.append(garden_layout())                        # Spring layout
    pages.append(garden_layout())                        # Summer/Fall layout

    # ---- Section 3: Monthly Tasks ----
    pages.append(divider_section(3, "Three", "Monthly Tasks", "Plan each month with intention"))
    for month in months:
        pages.append(monthly_tasks(month))

    # ---- Section 4: Harvest & Expenses ----
    pages.append(divider_section(4, "Four", "Harvest &amp; Expenses", "Track yield and spending"))
    pages.append(harvest_log(1, 3))
    pages.append(harvest_log(2, 3))
    pages.append(harvest_log(3, 3))
    pages.append(garden_expenses())

    # ---- Section 5: Seeds, Pests & Review ----
    pages.append(divider_section(5, "Five", "Seeds, Pests &amp; Review", "Plan ahead and reflect"))
    pages.append(seed_order_log())
    pages.append(pest_disease_log())
    pages.append(year_review())

    # ---- Section 6: Notes ----
    pages.append(divider_section(6, "Six", "Notes", "Observations, ideas, and reminders"))
    for i in range(6):
        pages.append(notes_page(i + 1))

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

    print(f"\nPage breakdown:")
    print(f"  Cover: 1")
    print(f"  Owner page: 1")
    print(f"  Reference (how-to, zones, calendar, companion): 4")
    print(f"  Section dividers: 6")
    print(f"  Plant inventory ({NUM_PLANTS} x 2): {NUM_PLANTS * 2}")
    print(f"  Garden layouts: 2")
    print(f"  Monthly tasks: 12")
    print(f"  Harvest log: 3")
    print(f"  Garden expenses: 1")
    print(f"  Seed order log: 1")
    print(f"  Pest/disease log: 1")
    print(f"  Year review: 1")
    print(f"  Notes pages: 6")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
