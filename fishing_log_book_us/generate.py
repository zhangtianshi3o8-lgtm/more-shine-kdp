#!/usr/bin/env python3
"""
Fishing Log Book — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: American anglers (all levels, freshwater & saltwater)
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "fishing_log_book_us_V1.0.html")

BOOK_TITLE = "Fishing Log Book"
BOOK_SUBTITLE = "Track Every Catch, Every Trip, Every Story"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

# ============================================================
# CSS
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
/* Deep Water: #0D3B4C, #164E63, #1B6B8C */
/* Steel Blue: #2A6F97 */
/* Sand: #E8D5A0, #DBC78E */
/* Gold/Amber: #D4A017, #C8A041 */
/* Foam: #F0F5F7 */
/* Dark: #1A1A1A */

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

/* ================ COVER ================ */
.cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(165deg, #062430 0%, #0D3B4C 25%, #164E63 55%, #0D3B4C 85%, #062430 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Water ripple texture */
.cover .water-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 30px 8px at 15% 25%, #ffffff, transparent),
    radial-gradient(ellipse 24px 6px at 80% 15%, #ffffff, transparent),
    radial-gradient(ellipse 28px 7px at 70% 70%, #ffffff, transparent),
    radial-gradient(ellipse 20px 6px at 25% 80%, #ffffff, transparent),
    radial-gradient(ellipse 18px 5px at 50% 50%, #ffffff, transparent),
    radial-gradient(ellipse 22px 6px at 10% 60%, #ffffff, transparent),
    radial-gradient(ellipse 16px 5px at 90% 45%, #ffffff, transparent),
    radial-gradient(ellipse 14px 4px at 40% 90%, #ffffff, transparent);
}

/* CSS Fish illustration */
.cover .fish-wrap {
  width: 140px; height: 70px;
  position: relative;
  margin: 0 auto 20px;
}

/* Fish body - elongated ellipse */
.cover .fish-body {
  width: 100px; height: 42px;
  background: #D4A017;
  border-radius: 50%;
  position: absolute;
  top: 14px; left: 15px;
  box-shadow: 2px 2px 8px rgba(0,0,0,0.4),
              inset -6px -3px 8px rgba(0,0,0,0.15),
              inset 6px 3px 8px rgba(255,255,255,0.08);
}

/* Fish belly highlight */
.cover .fish-belly {
  width: 80px; height: 14px;
  background: #F0CE6A;
  border-radius: 50%;
  position: absolute;
  top: 36px; left: 25px;
  opacity: 0.6;
}

/* Fish head shading */
.cover .fish-head {
  width: 42px; height: 38px;
  background: #C89010;
  border-radius: 50%;
  position: absolute;
  top: 16px; left: 65px;
  opacity: 0.5;
}

/* Fish tail */
.cover .fish-tail {
  width: 0; height: 0;
  border-right: 28px solid #D4A017;
  border-top: 20px solid transparent;
  border-bottom: 20px solid transparent;
  position: absolute;
  top: 15px; left: -10px;
  filter: drop-shadow(-2px 1px 4px rgba(0,0,0,0.3));
}

/* Fish dorsal fin */
.cover .fish-dorsal {
  width: 0; height: 0;
  border-bottom: 16px solid #B8860B;
  border-left: 8px solid transparent;
  border-right: 18px solid transparent;
  position: absolute;
  top: 4px; left: 50px;
}

/* Fish pectoral fin */
.cover .fish-pectoral {
  width: 20px; height: 10px;
  background: #B8860B;
  border-radius: 50% 50% 50% 0;
  position: absolute;
  top: 38px; left: 60px;
  transform: rotate(15deg);
  opacity: 0.8;
}

/* Fish eye */
.cover .fish-eye {
  width: 6px; height: 6px;
  background: #1A1A1A;
  border-radius: 50%;
  position: absolute;
  top: 26px; left: 92px;
}
.cover .fish-eye::after {
  content: "";
  width: 2px; height: 2px;
  background: white;
  border-radius: 50%;
  position: absolute;
  top: 1px; left: 3px;
}

/* Fish gill line */
.cover .fish-gill {
  width: 2px; height: 30px;
  background: #B8860B;
  position: absolute;
  top: 20px; left: 68px;
  border-radius: 1px;
  transform: rotate(5deg);
  opacity: 0.4;
}

/* Hook decoration */
.cover .hook {
  width: 30px; height: 45px;
  position: absolute;
  top: 110px; left: 50%;
  transform: translateX(-50%);
  opacity: 0.15;
}
.cover .hook::before {
  content: "";
  width: 2px; height: 25px;
  background: #D4A017;
  position: absolute;
  top: 0; left: 14px;
  border-radius: 1px;
}
.cover .hook::after {
  content: "";
  width: 18px; height: 18px;
  border: 2px solid #D4A017;
  border-top: none;
  border-left: none;
  border-radius: 0 0 50% 0;
  position: absolute;
  top: 22px; left: 14px;
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 30pt;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.15;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 6px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 110px; height: 2.5px;
  background: #D4A017;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 11pt;
  color: #A8C8D8;
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
  border: 1px solid rgba(212,160,23,0.4);
  color: #D4A017;
  font-size: 7pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 9px;
  border-radius: 3px;
  text-transform: uppercase;
}

.cover .tagline {
  font-size: 8.5pt;
  color: #A8C8D8;
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
  color: #D4A017;
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
  background: linear-gradient(165deg, #062430 0%, #0D3B4C 50%, #062430 100%);
  position: relative;
  overflow: hidden;
}
.divider .div-ripple {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 30px 8px at 15% 20%, #ffffff, transparent),
    radial-gradient(ellipse 25px 7px at 80% 30%, #ffffff, transparent),
    radial-gradient(ellipse 22px 6px at 70% 75%, #ffffff, transparent),
    radial-gradient(ellipse 18px 5px at 25% 85%, #ffffff, transparent);
}
.divider .div-num {
  font-size: 60pt;
  color: rgba(212,160,23,0.12);
  font-weight: 700;
  position: absolute;
  top: 1in;
}
.divider .div-label {
  font-size: 10pt;
  color: #D4A017;
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
  color: #A8C8D8;
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
  border-bottom: 1.5px solid #2A6F97;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #0D3B4C;
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
  color: #0D3B4C;
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
  background: #164E63;
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
  background: #F0F5F7;
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
  color: #0D3B4C;
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
  background: #F0F5F7;
  border-left: 3px solid #2A6F97;
  padding: 8px 10px;
  margin-bottom: 10px;
  font-size: 8pt;
  color: #333;
  line-height: 1.5;
}
.info-box .info-title {
  font-weight: 700;
  color: #0D3B4C;
  font-size: 8.5pt;
  margin-bottom: 4px;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
}

/* ---- Dot Grid ---- */
.dot-grid {
  background-image: radial-gradient(circle, #d0d0d0 1px, transparent 1px);
  background-size: 0.20in 0.20in;
  background-position: 0.10in 0.10in;
}

/* ---- Stat Card ---- */
.stat-card {
  text-align: center;
  padding: 6px 4px;
  background: #F0F5F7;
  border-radius: 4px;
  border: 1px solid #D0E0E8;
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
  color: #0D3B4C;
}

/* ---- Species Life List ---- */
table.life-list th {
  background: #2A6F97;
}
table.life-list td:first-child {
  width: 22px;
  text-align: center;
  font-weight: 700;
  color: #2A6F97;
}
table.life-list td:last-child {
  width: 28px;
  text-align: center;
}

/* ---- Tackle/Gear Card ---- */
.gear-card {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 8px;
  margin-bottom: 6px;
  background: #FAFCFC;
}
.gear-card .gear-label {
  font-size: 7pt;
  font-weight: 700;
  color: #2A6F97;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 4px;
}
.gear-card .gear-line {
  border-bottom: 0.5px solid #ddd;
  height: 16px;
  margin-bottom: 2px;
}
"""

# ============================================================
# PAGE BUILDERS
# ============================================================

def cover():
    return f'''
<!-- Page {pn()}: Cover -->
<div class="cover">
  <div class="water-bg"></div>
  <div class="fish-wrap">
    <div class="fish-tail"></div>
    <div class="fish-body"></div>
    <div class="fish-belly"></div>
    <div class="fish-head"></div>
    <div class="fish-dorsal"></div>
    <div class="fish-pectoral"></div>
    <div class="fish-gill"></div>
    <div class="fish-eye"></div>
  </div>
  <div class="hook"></div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">52 Trip Logs</span>
      <span class="feature-badge">Species Tracker</span>
      <span class="feature-badge">Tackle Inventory</span>
      <span class="feature-badge">Favorite Spots</span>
    </div>
    <div class="tagline">For Freshwater &amp; Saltwater Anglers</div>
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
    <div style="font-size: 16pt; font-weight: 700; color: #0D3B4C; margin-bottom: 6px;">This Log Book Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #0D3B4C; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #2A6F97; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Home Lake / River</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #2A6F97; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Species</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #2A6F97; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Fishing License #</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #2A6F97; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Emergency Contact</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Fishing Log Book</span>
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

  <div class="page-title">How to Use This Log Book</div>
  <div class="page-subtitle">Make every fishing trip count</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Fishing Log?</div>
    The difference between catching fish once and catching them consistently is data. A log helps you spot patterns — which baits work at certain temperatures, which spots produce at dawn vs. dusk, how weather and moon phase affect the bite. Over time, your log becomes your personal fishing intelligence.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #0D3B4C; font-size: 10pt; margin-bottom: 6px;">Tips for Effective Logging</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Log right after each trip.</strong> Memory fades fast. Record the details while they are fresh — the more you write now, the better your future trips will be.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Note the conditions.</strong> Weather, water temperature, wind, and barometric pressure are just as important as what you caught. These are the clues that reveal patterns.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Record the misses too.</strong> Fish that followed, bumped, or short-struck your bait are valuable data. Next time, you will know to adjust your retrieve or bait size.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Track your tackle.</strong> Knowing what is in your box saves money and prevents over-buying. The tackle inventory section helps you stay organized.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Use the species checklist.</strong> Mark off new species as you catch them. Building a life list is one of the great joys of fishing.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Pro Tip:</strong> Take a quick photo of each log page with your phone before heading home. If you ever lose the book, your data is safe.
  </div>

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def knot_reference():
    knots = [
        ("Improved Clinch Knot", "The most popular fishing knot. Reliable for tying line to hooks, lures, and swivels. Works best with monofilament and fluorocarbon up to 20 lb test.", "Best for: Live bait rigs, spinners, small lures"),
        ("Palomar Knot", "Incredibly strong and simple. One of the strongest knots for braided line. Nearly 100% line strength when tied correctly.", "Best for: Braided line, drop-shot rigs, jig heads"),
        ("Uni Knot (Duncan Loop)", "Versatile knot that works for tying to hooks, joining lines, or securing line to a reel spool. Can be used with all line types.", "Best for: General purpose, line-to-line connections"),
        ("Blood Knot", "The standard knot for joining two pieces of similar-diameter line. Essential for building leaders and tapered rigs.", "Best for: Fly fishing leaders, connecting tippet"),
        ("Snell Knot", "Aligns the hook point with the line pull for maximum hook-setting power. Preferred by catfish and saltwater anglers.", "Best for: Circle hooks, live bait fishing"),
        ("Loop Knot", "Creates a flexible connection that lets lures and flies move more naturally. Crucial for fly fishing and jigging.", "Best for: Flies, jigs, swimbaits"),
    ]

    rows = ""
    for name, desc, best in knots:
        rows += f'''
      <div style="border: 1px solid #e0e0e0; border-radius: 3px; padding: 7px 9px; margin-bottom: 6px; background: #FAFCFC;">
        <div style="font-size: 9.5pt; font-weight: 700; color: #0D3B4C; margin-bottom: 3px;">{name}</div>
        <div style="font-size: 8pt; color: #555; line-height: 1.5; margin-bottom: 4px;">{desc}</div>
        <div style="font-size: 7.5pt; color: #2A6F97; font-weight: 700;">{best}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Knot Reference -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Essential Knots</span>
    <span class="sh-right">Quick Reference</span>
  </div>

  <div class="page-title">Essential Fishing Knots</div>
  <div class="page-subtitle">The six knots every angler should know</div>

  {rows}

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def fish_species_reference():
    """Two-page fish species common to North America"""
    species_freshwater = [
        ("Largemouth Bass", "Most popular game fish in North America. Found in lakes, ponds, and slow rivers. Aggressive striker, strong fighter."),
        ("Smallmouth Bass", "Prefers cooler, clearer water with rocky or gravel bottoms. Known for acrobatic fights and power."),
        ("Walleye", "Prime table fish. Active at dusk and dawn. Found in deep lakes and rivers with moderate current."),
        ("Northern Pike", "Aggressive predator with sharp teeth. Found in weedy lakes and slow rivers. Use wire leaders."),
        ("Rainbow Trout", "Popular in streams, rivers, and lakes. Takes flies, spinners, and bait. Acrobatic fighter."),
        ("Brown Trout", "Wary and challenging. Prefers clear, cool streams. More active at night and in low light."),
        ("Brook Trout", "Beautiful native trout of cold, clean mountain streams. Sensitive to water temperature."),
        ("Crappie (Black & White)", "Schooling panfish. Spring spawners. Jigs and minnows are go-to baits. Excellent eating."),
        ("Bluegill / Sunfish", "Common panfish found in nearly every freshwater body. Great for beginners and kids."),
        ("Channel Catfish", "Bottom feeder with excellent sense of smell. Active at night. Use stink baits and cut bait."),
        ("Striped Bass", "Anadromous powerhouse. Caught in coastal waters, estuaries, and large reservoirs."),
        ("Muskellunge (Musky)", "The fish of ten thousand casts. Apex predator. Requires heavy tackle and endless patience."),
    ]

    rows = ""
    for name, desc in species_freshwater:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 6px; padding: 5px 8px; border-left: 2.5px solid #2A6F97; background: #F0F5F7; border-radius: 0 3px 3px 0;">
        <div style="min-width: 105px; font-size: 8.5pt; font-weight: 700; color: #0D3B4C;">{name}</div>
        <div style="font-size: 7.5pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Species Reference -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Species Guide</span>
    <span class="sh-right">Common North American Fish</span>
  </div>

  <div class="page-title">Freshwater Species Guide</div>
  <div class="page-subtitle">Know your target — habitat and habits</div>

  {rows}

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def saltwater_species_reference():
    species_salt = [
        ("Redfish (Red Drum)", "Shallow-water powerhouse of the Gulf and Atlantic coasts. Sight-fishing gold. Gold spoons and soft plastics."),
        ("Speckled Trout (Spotted Sea Trout)", "Popular inshore target from Maryland to Texas. Active at dawn and dusk. Soft plastics and topwater."),
        ("Snook", "Tropical and subtropical game fish. Found around docks, bridges, and inlets. Strong runs and jumps."),
        ("Tarpon", "The silver king. Massive, acrobatic fighter. Catch and release only in most areas. Needs heavy gear."),
        ("Flounder", "Bottom-dwelling flatfish. Ambush predator. Mud minnows and jigs bounced on the bottom."),
        ("Striped Bass (Saltwater)", "Migratory coastal fish. Surf, boat, and pier fishing. Eels, plugs, and bucktails."),
        ("Mahi-Mahi (Dolphinfish)", "Offshore speedster. Brilliant colors. Found near floating structure. Trolling ballyhoo."),
        ("Red Snapper", "Reef fish prized for both sport and table. Found over structure. Cut bait and vertical jigs."),
        ("King Mackerel (Kingfish)", "Fast, toothy offshore predator. Trolled live bait or frozen cigar minnows. Wire leader essential."),
        ("Sea Bass (Black Sea Bass)", "Reef and wreck dweller. Aggressive striker on squid and clams. Great eating."),
        ("Cobia", "Roving predator often sighted near the surface or following rays. Live eels and jigs."),
        ("Yellowfin Tuna", "Deep-water powerhouse. High-speed trolling and chunking. Requires heavy stand-up gear."),
    ]

    rows = ""
    for name, desc in species_salt:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 6px; padding: 5px 8px; border-left: 2.5px solid #1B6B8C; background: #E8F0F5; border-radius: 0 3px 3px 0;">
        <div style="min-width: 105px; font-size: 8.5pt; font-weight: 700; color: #0D3B4C;">{name}</div>
        <div style="font-size: 7.5pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Saltwater Species -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Species Guide</span>
    <span class="sh-right">Common Saltwater Fish</span>
  </div>

  <div class="page-title">Saltwater Species Guide</div>
  <div class="page-subtitle">Inshore and offshore favorites</div>

  {rows}

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def seasonal_reference():
    months = [
        ("January", "Cold water slows fish metabolism. Focus on deep holes and slow presentations. Ice fishing season in the north."),
        ("February", "Pre-spawn staging begins in southern waters. Fish move toward shallows on warm afternoons. Slow retrieves still key."),
        ("March", "Spring awakening. Bass and crappie move shallow as water warms. Trout become more active. Great month for jigs."),
        ("April", "Spawn season for bass and crappie in many regions. Sight fishing opportunities. Walleye run in rivers."),
        ("May", "Peak spawn for many species. Bluegill on beds. Trout fishing excellent. Topwater bites beginning."),
        ("June", "Post-spawn feeding frenzy. Fish are hungry and aggressive. Excellent month for topwater lures at dawn and dusk."),
        ("July", "Summer patterns. Early morning and late evening are best. Night fishing for catfish and stripers heats up."),
        ("August", "Dog days. Fish deep or fish at night. Thermocline fishing for walleye and trout. Offshore pelagics at peak."),
        ("September", "Fall transition begins. Cooling water triggers feeding. Bass and walleye active. Hunting season overlap begins."),
        ("October", "Prime fall fishing. Fish binge-feed before winter. Crankbaits and swimbaits excel. Trout streams at their best."),
        ("November", "Late fall bite still strong. Stripers and musky peak. Deep-water jigging for walleye. Fewer crowds."),
        ("December", "Winter patterns set in. Ice fishing begins up north. Southern saltwater remains productive. Slow presentations."),
    ]

    rows = ""
    for month, desc in months:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; background: #FAFCFC; border-radius: 3px; border: 1px solid #eee;">
        <div style="min-width: 58px; font-size: 8pt; font-weight: 700; color: #D4A017; text-transform: uppercase; letter-spacing: 0.3pt;">{month}</div>
        <div style="font-size: 7.5pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Seasonal Reference -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Seasonal Guide</span>
    <span class="sh-right">Month-by-Month</span>
  </div>

  <div class="page-title">Fishing Calendar</div>
  <div class="page-subtitle">What to expect each month of the year</div>

  {rows}

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def divider_section(num, label, title, subtitle):
    labels = ["One", "Two", "Three", "Four", "Five"]
    label_text = labels[num-1] if num <= 5 else label
    return f'''
<!-- Page {pn()}: Divider -->
<div class="divider">
  <div class="div-ripple"></div>
  <div class="div-num">{num:02d}</div>
  <div class="div-label">Part {label_text}</div>
  <div class="div-title">{title}</div>
  <div class="div-sub">{subtitle}</div>
</div>
'''


def trip_log_left(trip_num):
    """Left page of two-page trip spread — structured catch data"""
    return f'''
<!-- Page {pn()}: Trip {trip_num} Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Trip #{trip_num:02d}</span>
    <span class="sh-right">Fishing Log Book</span>
  </div>

  <div class="page-title">Trip Log #{trip_num:02d}</div>
  <div class="page-subtitle">Catch Details &amp; Conditions</div>

  <!-- Trip Info -->
  <div style="background: #F0F5F7; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; min-width: 28px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; min-width: 28px;">Time</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; min-width: 28px;">Loc.</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; min-width: 28px;">GPS</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Water Type & Conditions -->
  <div style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Water Type</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Lake</span>
    <span class="check-item"><span class="check-box"></span> River</span>
    <span class="check-item"><span class="check-box"></span> Pond</span>
    <span class="check-item"><span class="check-box"></span> Stream</span>
    <span class="check-item"><span class="check-box"></span> Ocean</span>
    <span class="check-item"><span class="check-box"></span> Bay/Estuary</span>
    <span class="check-item"><span class="check-box"></span> Reservoir</span>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Conditions</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Sunny</span>
    <span class="check-item"><span class="check-box"></span> Cloudy</span>
    <span class="check-item"><span class="check-box"></span> Overcast</span>
    <span class="check-item"><span class="check-box"></span> Light Rain</span>
    <span class="check-item"><span class="check-box"></span> Stormy</span>
    <span class="check-item"><span class="check-box"></span> Foggy</span>
  </div>

  <!-- Water Data Fields -->
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 8px;">
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #2A6F97; text-transform: uppercase;">Water Temp</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #2A6F97; text-transform: uppercase;">Air Temp</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #2A6F97; text-transform: uppercase;">Wind mph</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #2A6F97; text-transform: uppercase;">Barometer</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #2A6F97; text-transform: uppercase;">Water Clarity</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
    <div><div style="font-size: 6.5pt; font-weight: 700; color: #2A6F97; text-transform: uppercase;">Moon Phase</div><div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div></div>
  </div>

  <!-- Catch Table -->
  <div style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Catch Record</div>
  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:14px;">#</th>
      <th>Species</th>
      <th style="width:32px;">Len</th>
      <th style="width:30px;">Wt</th>
      <th>Bait / Lure / Fly</th>
      <th style="width:24px;">Rel</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A6F97;">1</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A6F97;">2</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A6F97;">3</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A6F97;">4</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A6F97;">5</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A6F97;">6</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A6F97;">7</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#2A6F97;">8</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Len = inches | Wt = lbs/oz | Rel = check if released</div>

  <div class="page-footer">
    <span>Trip #{trip_num:02d} — Catch Details</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def trip_log_right(trip_num):
    """Right page of two-page trip spread — notes, techniques, summary"""
    return f'''
<!-- Page {pn()}: Trip {trip_num} Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Trip #{trip_num:02d}</span>
    <span class="sh-right">Notes &amp; Reflection</span>
  </div>

  <div class="page-title">Trip Notes #{trip_num:02d}</div>
  <div class="page-subtitle">Tactics, observations, and the story of the day</div>

  <!-- Techniques Used -->
  <div style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Techniques Used</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Casting</span>
    <span class="check-item"><span class="check-box"></span> Trolling</span>
    <span class="check-item"><span class="check-box"></span> Jigging</span>
    <span class="check-item"><span class="check-box"></span> Fly Fishing</span>
    <span class="check-item"><span class="check-box"></span> Bottom Fishing</span>
    <span class="check-item"><span class="check-box"></span> Drift Fishing</span>
    <span class="check-item"><span class="check-box"></span> Still Fishing</span>
    <span class="check-item"><span class="check-box"></span> Surf Fishing</span>
  </div>

  <!-- Trip Stats -->
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 5px; margin-bottom: 10px;">
    <div class="stat-card"><div class="stat-label">Hours</div><div class="stat-value"></div></div>
    <div class="stat-card"><div class="stat-label">Total Caught</div><div class="stat-value"></div></div>
    <div class="stat-card"><div class="stat-label">Biggest (lb)</div><div class="stat-value"></div></div>
    <div class="stat-card"><div class="stat-label">Best Bait</div><div class="stat-value" style="font-size:7pt;"></div></div>
  </div>

  <!-- Trip Rating -->
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
    <span style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; letter-spacing: 0.4pt;">Overall Rating</span>
    <span class="stars">☆ ☆ ☆ ☆ ☆</span>
  </div>

  <!-- Notes Area -->
  <div style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Trip Highlights &amp; Notes</div>
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

  <!-- Companions -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-top: 8px; margin-bottom: 6px;">
    <span style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; min-width: 72px;">Fished With</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Lessons -->
  <div style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">What Worked / What to Try Next Time</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Trip #{trip_num:02d} — Notes</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def species_life_list(title_text, subtitle_text, species_list, color_hex):
    """Species life list checklist page"""
    rows = ""
    for i, sp in enumerate(species_list, 1):
        rows += f'''
    <tr>
      <td>{i}</td>
      <td>{sp}</td>
      <td></td>
      <td></td>
      <td><span class="check-box" style="vertical-align: middle;"></span></td>
    </tr>'''

    return f'''
<!-- Page {pn()}: Life List -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Species Checklist</span>
    <span class="sh-right">Life List</span>
  </div>

  <div class="page-title">{title_text}</div>
  <div class="page-subtitle">{subtitle_text}</div>

  <table class="data-table life-list" style="font-size: 7.5pt;">
    <tr>
      <th style="width:22px;">#</th>
      <th>Species</th>
      <th style="width:70px;">First Caught</th>
      <th style="width:70px;">Location</th>
      <th style="width:28px;">✓</th>
    </tr>
    {rows}
  </table>

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def catch_summary():
    """Season summary statistics page"""
    return f'''
<!-- Page {pn()}: Catch Summary -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Season Summary</span>
    <span class="sh-right">Your Best Year Yet</span>
  </div>

  <div class="page-title">Season Catch Summary</div>
  <div class="page-subtitle">Fill in at the end of each season</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Total Trips</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Total Fish Caught</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Species Count</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Personal Bests</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Species</th>
      <th>Size / Weight</th>
      <th>Date &amp; Location</th>
    </tr>
    <tr><td style="font-weight:700;color:#0D3B4C;">Biggest Fish</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#0D3B4C;">Most Fish in a Trip</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#0D3B4C;">First New Species</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#0D3B4C;">Longest Fight</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#0D3B4C;">Best Day Ever</td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Top 5 Trips</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Date</th>
      <th>Location</th>
      <th>Species</th>
      <th>Catch Count</th>
      <th>Memorable Moment</th>
    </tr>
    <tr><td style="font-weight:700;color:#D4A017;">1</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#D4A017;">2</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#D4A017;">3</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#D4A017;">4</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#D4A017;">5</td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def tackle_inventory():
    """Tackle and gear inventory page"""
    return f'''
<!-- Page {pn()}: Tackle Inventory -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Tackle &amp; Gear</span>
    <span class="sh-right">Inventory</span>
  </div>

  <div class="page-title">Tackle Inventory</div>
  <div class="page-subtitle">Know what is in your box</div>

  <div class="gear-card">
    <div class="gear-label">Rods</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Length</th><th>Power / Action</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Reels</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Line Capacity</th><th>Gear Ratio</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Line &amp; Leaders</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Test (lb)</th><th>Brand / Notes</th><th>Spare?</th></tr>
      <tr><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def lure_inventory():
    """Lures and baits inventory page"""
    return f'''
<!-- Page {pn()}: Lure Inventory -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Lure Box</span>
    <span class="sh-right">Inventory</span>
  </div>

  <div class="page-title">Lure &amp; Bait Inventory</div>
  <div class="page-subtitle">Keep track of what produces</div>

  <div class="gear-card">
    <div class="gear-label">Hard Baits — Crankbaits, Jerkbaits, Topwater</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Color</th><th>Size</th><th>Diving Depth</th><th>Best For</th></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Soft Plastics — Worms, Grubs, Swimbaits</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Color</th><th>Size</th><th>Qty</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Jigs, Spoons &amp; Spinners</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Weight</th><th>Color</th><th>Qty</th><th>Best For</th></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def favorite_spots(page_of, total_pages):
    """Favorite fishing spots log"""
    rows = ""
    spots = list(range(1, 11))
    for i in spots:
        rows += f'''
    <tr>
      <td style="font-weight:700;color:#2A6F97;text-align:center;">{i}</td>
      <td></td>
      <td></td>
      <td></td>
      <td style="text-align:center;"></td>
    </tr>'''

    return f'''
<!-- Page {pn()}: Favorite Spots -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Favorite Spots</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Favorite Fishing Spots</div>
  <div class="page-subtitle">Your go-to locations</div>

  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th style="width:20px;">#</th>
      <th>Location Name</th>
      <th style="width:80px;">Water Type</th>
      <th style="width:75px;">Best Season</th>
      <th style="width:55px;">Rating</th>
    </tr>
    {rows}
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Rating: ☆☆☆☆☆ (circle or fill in your stars)</div>

  <div style="margin-top: 12px;">
    <div style="font-size: 7pt; font-weight: 700; color: #0D3B4C; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Spot Notes</div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px;">
      <div>
        <div style="font-size: 6.5pt; color: #2A6F97; font-weight: 700; margin-bottom: 2px;">Spot Name</div>
        <div style="border-bottom: 0.5px solid #ccc; height: 16px; margin-bottom: 4px;"></div>
        <div style="font-size: 6.5pt; color: #2A6F97; font-weight: 700; margin-bottom: 2px;">GPS / Directions</div>
        <div style="border-bottom: 0.5px solid #ccc; height: 16px; margin-bottom: 4px;"></div>
        <div style="font-size: 6.5pt; color: #2A6F97; font-weight: 700; margin-bottom: 2px;">Best Techniques</div>
        <div style="border-bottom: 0.5px solid #ccc; height: 16px; margin-bottom: 4px;"></div>
        <div style="font-size: 6.5pt; color: #2A6F97; font-weight: 700; margin-bottom: 2px;">Access / Parking</div>
        <div style="border-bottom: 0.5px solid #ccc; height: 16px;"></div>
      </div>
      <div>
        <div style="font-size: 6.5pt; color: #2A6F97; font-weight: 700; margin-bottom: 2px;">Spot Name</div>
        <div style="border-bottom: 0.5px solid #ccc; height: 16px; margin-bottom: 4px;"></div>
        <div style="font-size: 6.5pt; color: #2A6F97; font-weight: 700; margin-bottom: 2px;">GPS / Directions</div>
        <div style="border-bottom: 0.5px solid #ccc; height: 16px; margin-bottom: 4px;"></div>
        <div style="font-size: 6.5pt; color: #2A6F97; font-weight: 700; margin-bottom: 2px;">Best Techniques</div>
        <div style="border-bottom: 0.5px solid #ccc; height: 16px; margin-bottom: 4px;"></div>
        <div style="font-size: 6.5pt; color: #2A6F97; font-weight: 700; margin-bottom: 2px;">Access / Parking</div>
        <div style="border-bottom: 0.5px solid #ccc; height: 16px;"></div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def notes_page(page_num):
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

  <div class="page-title">Fishing Notes</div>
  <div class="page-subtitle">Ideas, observations, and reminders</div>

  {lines}

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def sketch_page():
    """Dot grid page for sketching maps and rigging diagrams"""
    return f'''
<!-- Page {pn()}: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Sketch Pad</span>
    <span class="sh-right">Maps &amp; Rigging Diagrams</span>
  </div>

  <div class="page-title">Sketch Pad</div>
  <div class="page-subtitle">Draw spot maps, rigging setups, and fish markings</div>

  <div class="dot-grid" style="width: 100%; height: 6.5in; border-radius: 4px;"></div>

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


# ============================================================
# MAIN — ASSEMBLE BOOK
# ============================================================

def main():
    pages = []

    # ---- Front Matter ----
    pages.append(cover())                    # 1: Cover
    pages.append(owner_page())               # 2: Owner page

    # ---- Educational Reference ----
    pages.append(how_to_use())               # 3: How to use
    pages.append(knot_reference())           # 4: Knots
    pages.append(fish_species_reference())   # 5: Freshwater species
    pages.append(saltwater_species_reference())  # 6: Saltwater species
    pages.append(seasonal_reference())       # 7: Seasonal guide

    # ---- Section 1: Trip Logs ----
    pages.append(divider_section(1, "One", "Trip Logs", "52 trips — your fishing story"))
    NUM_TRIPS = 52
    for i in range(1, NUM_TRIPS + 1):
        pages.append(trip_log_left(i))       # Left page: catch data
        pages.append(trip_log_right(i))      # Right page: notes

    # ---- Section 2: Species Life List ----
    pages.append(divider_section(2, "Two", "Species Checklist", "Your fishing life list"))

    # Freshwater life list (2 pages, 40 species)
    fw_species_1 = [
        "Largemouth Bass", "Smallmouth Bass", "Spotted Bass", "Striped Bass",
        "White Bass", "Yellow Bass", "Walleye", "Sauger",
        "Northern Pike", "Muskellunge", "Chain Pickerel", "Tiger Musky",
        "Rainbow Trout", "Brown Trout", "Brook Trout", "Lake Trout",
        "Cutthroat Trout", "Steelhead", " Chinook Salmon", "Coho Salmon",
    ]
    fw_species_2 = [
        "Channel Catfish", "Blue Catfish", "Flathead Catfish", "White Catfish",
        "Black Crappie", "White Crappie", "Bluegill", "Redear Sunfish",
        "Green Sunfish", "Pumpkinseed", "Longear Sunfish", "Warmouth",
        "Yellow Perch", "White Perch", "Sauger", "Bowfin",
        "Gar (Longnose)", "Carp (Common)", "Northern Pike", "Sturgeon",
    ]
    pages.append(species_life_list("Freshwater Life List (1-20)", "Check off each species as you catch it", fw_species_1, "#2A6F97"))
    pages.append(species_life_list("Freshwater Life List (21-40)", "Keep building your list", fw_species_2, "#2A6F97"))

    # Saltwater life list (1 page, 20 species)
    sw_species = [
        "Redfish (Red Drum)", "Speckled Trout", "Snook", "Tarpon",
        "Flounder (Southern)", "Striped Bass (Salt)", "Bluefish", "Weakfish",
        "Mahi-Mahi", "Red Snapper", "King Mackerel", "Spanish Mackerel",
        "Black Sea Bass", "Cobia", "Amberjack", "Yellowfin Tuna",
        "Wahoo", "Grouper (Gag)", "Sheepshead", "Pompano",
    ]
    pages.append(species_life_list("Saltwater Life List", "Inshore and offshore species", sw_species, "#1B6B8C"))

    # ---- Section 3: Season Summary ----
    pages.append(divider_section(3, "Three", "Season Summary", "Your best catches, trips, and memories"))
    pages.append(catch_summary())
    pages.append(catch_summary())  # Two summary pages (mid-year + year-end)

    # ---- Section 4: Tackle Inventory ----
    pages.append(divider_section(4, "Four", "Tackle Inventory", "Your rods, reels, and lures"))
    pages.append(tackle_inventory())
    pages.append(lure_inventory())

    # ---- Section 5: Favorite Spots & Notes ----
    pages.append(divider_section(5, "Five", "Spots & Notes", "Your map to great fishing"))
    pages.append(favorite_spots(1, 2))
    pages.append(favorite_spots(2, 2))
    pages.append(sketch_page())
    pages.append(sketch_page())

    # Notes pages to fill out
    for i in range(6):
        pages.append(notes_page(i + 1))

    # Assemble HTML
    body_content = "\n".join(pages)
    total_pages = page_no[0]

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{BOOK_TITLE} — More Shine Press</title>
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
    print(f"  Owner page: 1")
    print(f"  Reference (how-to, knots, species, seasonal): 5")
    print(f"  Section dividers: 5")
    print(f"  Trip logs (52 trips x 2 pages): 104")
    print(f"  Species life lists: 3")
    print(f"  Season summaries: 2")
    print(f"  Tackle/lure inventory: 2")
    print(f"  Favorite spots: 2")
    print(f"  Sketch pages: 2")
    print(f"  Notes pages: 6")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
