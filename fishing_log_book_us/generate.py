#!/usr/bin/env python3
"""
Fishing Log Book — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Anglers, sport fishermen, fly fishers, bass fishermen
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "fishing_log_book_us_V1.0.html")

BOOK_TITLE = "Fishing Log Book"
BOOK_SUBTITLE = "Track Every Catch and Become a Better Angler"

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
    radial-gradient(ellipse 18px 11px at 90% 40%, #C4A04A, transparent);
}

.cover .icon-wrap {
  width: 120px; height: 120px;
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
  font-size: 30pt;
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
    <svg viewBox="0 0 120 120" width="120" height="120" xmlns="http://www.w3.org/2000/svg">
      <!-- Hook outline -->
      <path d="M 60 12 L 60 60 Q 60 80 48 82 Q 35 82 35 70 Q 35 62 42 62"
        stroke="#C4A04A" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- Barb -->
      <path d="M 42 62 L 38 58 L 45 58 Z" stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.2)"/>
      <!-- Eye/loop at top -->
      <circle cx="60" cy="12" r="5" stroke="#C4A04A" stroke-width="2" fill="none"/>
      <!-- Fish silhouette -->
      <path d="M 55 92 Q 50 88 58 85 Q 70 83 82 86 Q 90 88 96 92 Q 90 96 82 98 Q 70 101 58 99 Q 50 96 55 92 Z"
        stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.1)"/>
      <!-- Fish tail -->
      <path d="M 96 92 L 106 86 L 104 92 L 106 98 Z"
        stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.08)"/>
      <!-- Fish eye -->
      <circle cx="62" cy="91" r="2" fill="#C4A04A" opacity="0.5"/>
      <!-- Water ripples -->
      <path d="M 30 100 Q 40 98 50 100 Q 60 102 70 100 Q 80 98 90 100"
        stroke="#C4A04A" stroke-width="0.8" fill="none" opacity="0.3"/>
      <path d="M 35 105 Q 45 103 55 105 Q 65 107 75 105 Q 85 103 95 105"
        stroke="#C4A04A" stroke-width="0.6" fill="none" opacity="0.2"/>
    </svg>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">50 Catch Logs</span>
      <span class="feature-badge">Gear Tracker</span>
      <span class="feature-badge">Best Spots</span>
      <span class="feature-badge">Trip Planner</span>
    </div>
    <div class="tagline">Cast &middot; Catch &middot; Remember</div>
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
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Fishing License #</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Fish Species</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Home Waters</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Personal Best</div>
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

  <div class="page-title">How to Use This Journal</div>
  <div class="page-subtitle">Catch more by learning from every trip</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Fishing Log?</div>
    Successful anglers don't just remember their catches &mdash; they study them. A fishing log helps you identify patterns in weather, water, bait, and location that lead to success. Over time, your journal becomes your personal fishing intelligence, turning good days into repeatable strategies.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">What to Record Every Trip</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Conditions matter.</strong> Record the date, time, weather, water temperature, and tide or current. The same spot can produce very differently depending on conditions.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Track your bait and tackle.</strong> Note the exact lure, bait, hook size, line weight, and rig. What worked today might be the key to tomorrow.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Measure and record.</strong> Species, length, and weight for every catch. Over time, this data reveals which spots produce the biggest fish.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Mark your spots.</strong> Record GPS coordinates or landmark descriptions. Your best fishing holes are worth remembering.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Note techniques.</strong> Casting, trolling, jigging, fly presentation &mdash; the how matters as much as the where and what.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Pro Tip:</strong> Take a quick photo of each catch with your phone before releasing. The photo's metadata captures the time and GPS location automatically.
  </div>

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def fish_species_guide():
    """Common fish species reference page"""
    species = [
        ("Largemouth Bass", "Most popular freshwater game fish in North America. Loves structure &mdash; weed beds, fallen logs, docks. Best lures: plastic worms, crankbaits, jigs."),
        ("Smallmouth Bass", "Found in clear, rocky lakes and rivers. More aggressive fight than largemouth. Try tube baits, spinnerbaits, and topwater lures."),
        ("Rainbow Trout", "Cool-water fish in streams, rivers, and lakes. Fly fishing favorite. Effective: spinners, salmon eggs, and nymph patterns."),
        ("Walleye", "Prime eating fish, active at dawn/dusk and low light. Jigs with minnows, crankbaits trolled along drop-offs."),
        ("Northern Pike", "Aggressive predators in weedy shallows. Large spoons, spinnerbaits, and swimbaits. Use steel leaders."),
        ("Catfish", "Bottom feeders, best at night. Chicken liver, cut bait, stink bait on the river bottom."),
        ("Crappie", "Panfish that school around structure. Small jigs and minnows fished slowly around brush piles."),
        ("Bluegill &amp; Sunfish", "Perfect for beginners and kids. Worms and small jigs near shallow structure and docks."),
        ("Striped Bass", "Anadromous game fish, surf and boat. Live eels, bucktails, and topwater poppers."),
        ("Salmon", "Chinook, Coho, Atlantic. Trolling with spoons, herring, or fly fishing in rivers during runs."),
    ]

    rows = ""
    for name, desc in species:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 95px; font-size: 8pt; font-weight: 700; color: #161616;">{name}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Species Guide -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Species Guide</span>
  </div>

  <div class="page-title">Common Fish Species</div>
  <div class="page-subtitle">Know your target before you cast</div>

  {rows}

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def knots_reference():
    """Essential fishing knots reference"""
    knots = [
        ("Improved Clinch Knot", "For tying line to hook, lure, or swivel. Pass line through eye, wrap 5-7 times, thread through loop near eye, then through big loop. Lubricate and tighten."),
        ("Palomar Knot", "One of the strongest knots for braided line. Double the line, pass loop through eye, tie simple overhand, pass lure/loop through the loop, tighten."),
        ("Uni Knot", "Versatile for line-to-hook and line-to-swatch. Pass line through eye, form loop, wrap tag end 5-7 times through loop, moisten and pull tight."),
        ("Blood Knot", "For joining two lines of similar diameter. Overlap ends, wrap each around the other 5-6 times in opposite directions, thread through center, tighten."),
        ("Surgeon's Loop", "For creating a loop at the end of line. Form a loop, tie an overhand knot passing the loop through once more, pull both strands tight."),
        ("Snell Knot", "For attaching hook to leader. Pass line through eye from front, wrap tag end around shank 5-7 times toward the eye, thread through eye, tighten."),
    ]

    rows = ""
    for name, desc in knots:
        rows += f'''
      <div style="margin-bottom: 6px; padding: 5px 8px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="font-size: 8pt; font-weight: 700; color: #161616; margin-bottom: 2px;">{name}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Knots -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Essential Knots</span>
  </div>

  <div class="page-title">Essential Fishing Knots</div>
  <div class="page-subtitle">The right knot makes all the difference</div>

  {rows}

  <div style="margin-top: 8px; padding: 6px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 7.5pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Knot Tip:</strong> Always moisten the line before tightening. Dry friction weakens monofilament and braided line significantly.
  </div>

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def tackle_inventory():
    """Tackle box inventory tracker"""
    categories = [
        ("Hooks", ["Drop-shot", "Circle", "Octopus", "Aberdeen", "Treble", "Worm"]),
        ("Lures &amp; Baits", ["Crankbait", "Spinnerbait", "Jig", "Soft plastic", "Topwater", "Spoon"]),
        ("Lines &amp; Leaders", ["Monofilament", "Braided", "Fluorocarbon", "Steel leader", "Fly line"]),
    ]

    sections = ""
    for cat_name, items in categories:
        item_rows = ""
        for item in items:
            item_rows += f'''
          <tr><td style="font-size:7.5pt;">{item}</td><td></td><td></td><td style="text-align:center;"></td></tr>'''
        sections += f'''
      <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">{cat_name}</div>
      <table class="data-table" style="font-size: 7.5pt;">
        <tr><th>Item</th><th style="width:50px;">Size/Type</th><th style="width:50px;">Qty</th><th style="width:22px;">Low?</th></tr>
        {item_rows}
      </table>'''

    return f'''
<!-- Page {pn()}: Tackle Inventory -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Tackle Inventory</span>
    <span class="sh-right">Gear Tracker</span>
  </div>

  <div class="page-title">Tackle Box Inventory</div>
  <div class="page-subtitle">Know what you have and what you need</div>

  {sections}

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def divider_section(num, title, subtitle):
    labels = ["One", "Two", "Three", "Four", "Five", "Six", "Seven"]
    label_text = labels[num-1] if num <= 7 else ""
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


def catch_log_left(entry_num):
    """Left page: catch details"""
    return f'''
<!-- Page {pn()}: Catch {entry_num} Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Catch #{entry_num:02d}</span>
    <span class="sh-right">Details</span>
  </div>

  <div class="page-title">Catch #{entry_num:02d}</div>
  <div class="page-subtitle">The full story of every catch</div>

  <!-- Trip Info -->
  <div style="background: #FAF6F0; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display:flex;align-items:baseline;gap:4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Date</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
      <div style="display:flex;align-items:baseline;gap:4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Time</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
      <div style="display:flex;align-items:baseline;gap:4px;grid-column:span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Location</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
      <div style="display:flex;align-items:baseline;gap:4px;grid-column:span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">GPS / Landmarks</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
      <div style="display:flex;align-items:baseline;gap:4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Water Type</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
      <div style="display:flex;align-items:baseline;gap:4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Water Temp</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
      <div style="display:flex;align-items:baseline;gap:4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Depth</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
      <div style="display:flex;align-items:baseline;gap:4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Bottom</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
    </div>
  </div>

  <!-- Weather -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Weather Conditions</div>
  <div class="check-row" style="margin-bottom: 8px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Sunny</span>
    <span class="check-item"><span class="check-box"></span> Cloudy</span>
    <span class="check-item"><span class="check-box"></span> Overcast</span>
    <span class="check-item"><span class="check-box"></span> Rain</span>
    <span class="check-item"><span class="check-box"></span> Fog</span>
    <span class="check-item"><span class="check-box"></span> Wind</span>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-bottom:10px;">
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;">Air</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;">Wind</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;">Pressure</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
  </div>

  <!-- Catch details -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">The Catch</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr><th>Species</th><th style="width:45px;">Length</th><th style="width:45px;">Weight</th></tr>
    <tr><td></td><td></td><td></td></tr>
  </table>
  <div class="check-row" style="margin-top: 6px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Kept</span>
    <span class="check-item"><span class="check-box"></span> Released</span>
    <span class="check-item"><span class="check-box"></span> Personal Best</span>
    <span class="check-item"><span class="check-box"></span> New Record</span>
  </div>

  <div class="page-footer">
    <span>Catch #{entry_num:02d} &mdash; Details</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def catch_log_right(entry_num):
    """Right page: technique, bait, notes"""
    return f'''
<!-- Page {pn()}: Catch {entry_num} Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Catch #{entry_num:02d}</span>
    <span class="sh-right">Technique &amp; Notes</span>
  </div>

  <div class="page-title">Catch #{entry_num:02d}</div>
  <div class="page-subtitle">Bait, technique, and what worked</div>

  <!-- Method -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Fishing Method</div>
  <div class="check-row" style="margin-bottom: 10px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Shore</span>
    <span class="check-item"><span class="check-box"></span> Boat</span>
    <span class="check-item"><span class="check-box"></span> Kayak</span>
    <span class="check-item"><span class="check-box"></span> Wading</span>
    <span class="check-item"><span class="check-box"></span> Pier/Bridge</span>
    <span class="check-item"><span class="check-box"></span> Ice</span>
  </div>

  <!-- Bait & Tackle -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Bait &amp; Tackle</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px 10px; margin-bottom: 10px;">
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;min-width:42px;">Bait</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;min-width:42px;">Lure</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;min-width:42px;">Hook</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;min-width:42px;">Line</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;min-width:42px;">Rod</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;min-width:42px;">Rig</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
  </div>

  <!-- Technique -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Technique</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- What worked / Lessons -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 4px;">What Worked / Lessons Learned</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Companions -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 4px;">Fishing With</div>
  <div class="wline-sm"></div>

  <!-- Overall trip -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 4px;">Total Catch Today</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;">
    <div class="stat-card" style="padding:6px;"><div class="stat-label">Fish</div><div class="stat-value" style="font-size:11pt;"></div></div>
    <div class="stat-card" style="padding:6px;"><div class="stat-label">Species</div><div class="stat-value" style="font-size:11pt;"></div></div>
    <div class="stat-card" style="padding:6px;"><div class="stat-label">Biggest</div><div class="stat-value" style="font-size:11pt;"></div></div>
  </div>

  <div class="page-footer">
    <span>Catch #{entry_num:02d} &mdash; Technique</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def best_spots():
    """Best fishing spots tracker"""
    return f'''
<!-- Page {pn()}: Best Spots -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Best Spots</span>
    <span class="sh-right">Secret Holes</span>
  </div>

  <div class="page-title">Best Fishing Spots</div>
  <div class="page-subtitle">Your personal map of honey holes</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Location / Lake / River</th>
      <th style="width:45px;">GPS / Landmark</th>
      <th style="width:45px;">Best Season</th>
      <th style="width:45px;">Species</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">13</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">14</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">15</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def personal_records():
    """Personal records and milestones"""
    return f'''
<!-- Page {pn()}: Personal Records -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Personal Records</span>
    <span class="sh-right">Milestones</span>
  </div>

  <div class="page-title">Personal Records</div>
  <div class="page-subtitle">Your biggest, best, and most memorable</div>

  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th style="width:80px;">Category</th>
      <th>Species</th>
      <th style="width:45px;">Length</th>
      <th style="width:45px;">Weight</th>
      <th style="width:50px;">Date</th>
      <th style="width:55px;">Location</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Bass</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Pike</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Trout</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Walleye</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Catfish</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Most Fish/Day</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">First Catch</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Rarest Catch</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Longest Fight</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">New Species</td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Memorable Stories</div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
  </div>

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def quick_log(page_of, total_pages):
    """One-line-per-catch quick log"""
    return f'''
<!-- Page {pn()}: Quick Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Quick Catch Log</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Quick Catch Log</div>
  <div class="page-subtitle">A bird's-eye view of every catch</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th style="width:42px;">Date</th>
      <th>Location</th>
      <th style="width:50px;">Species</th>
      <th style="width:30px;">Size</th>
      <th style="width:35px;">Bait</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">13</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">14</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">15</td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div class="page-footer">
    <span>Fishing Log Book</span>
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

  <div class="page-title">Fishing Notes</div>
  <div class="page-subtitle">Tips, patterns, and future plans</div>

  {lines}

  <div class="page-footer">
    <span>Fishing Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


# ============================================================
# MAIN
# ============================================================
def main():
    pages = []

    # ---- Front Matter ----
    pages.append(cover_page())                          # 1
    pages.append(owner_page())                           # 2
    pages.append(how_to_use())                           # 3

    # ---- Reference Section ----
    pages.append(fish_species_guide())                   # 4
    pages.append(knots_reference())                      # 5
    pages.append(tackle_inventory())                     # 6

    # ---- Section 1: Catch Logs ----
    pages.append(divider_section(1, "Catch Logs", "50 catches &mdash; detailed records of every fish"))
    NUM_CATCHES = 50
    for i in range(1, NUM_CATCHES + 1):
        pages.append(catch_log_left(i))
        pages.append(catch_log_right(i))

    # ---- Section 2: Quick Catch Log ----
    pages.append(divider_section(2, "Quick Catch Log", "Every catch at a glance"))
    pages.append(quick_log(1, 2))
    pages.append(quick_log(2, 2))

    # ---- Section 3: Spots & Records ----
    pages.append(divider_section(3, "Spots &amp; Records", "Your best fishing spots and personal milestones"))
    pages.append(best_spots())
    pages.append(personal_records())

    # ---- Section 4: Notes ----
    pages.append(divider_section(4, "Notes", "Tips, patterns, and future plans"))
    for i in range(4):
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
    print(f"  How to use: 1")
    print(f"  Species guide: 1")
    print(f"  Knots reference: 1")
    print(f"  Tackle inventory: 1")
    print(f"  Section dividers: 4")
    print(f"  Catch logs ({NUM_CATCHES} x 2): {NUM_CATCHES * 2}")
    print(f"  Quick catch log: 2")
    print(f"  Best spots: 1")
    print(f"  Personal records: 1")
    print(f"  Notes pages: 4")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
