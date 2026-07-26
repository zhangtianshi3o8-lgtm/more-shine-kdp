#!/usr/bin/env python3
"""
Sourdough Baking Log — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Sourdough home bakers, artisan bread enthusiasts
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "sourdough_baking_log_us_V1.0.html")

BOOK_TITLE = "Sourdough Baking Log"
BOOK_SUBTITLE = "Every Loaf Tells a Story"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

def nl(n):
    return "\n".join('<div class="notes-line"></div>' for _ in range(n))

def rating_circles_html(n):
    return " ".join(
        '<span class="rating-circle">%d</span>' % i for i in range(1, n + 1)
    )

def check_items_html(items):
    return "\n".join(
        '<div class="check-item"><div class="check-box"></div><span>%s</span></div>'
        % H.escape(item)
        for item in items
    )

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
  background: linear-gradient(165deg, #161210 0%, #231A15 30%, #161210 65%, #0D0A08 100%);
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
    radial-gradient(ellipse 26px 16px at 80% 15%, #E8A838, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #B87333, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #E8A838, transparent);
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
  color: #B87333;
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
  color: #161210;
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

/* ================ BAKE SPREAD LEFT ================ */
.session-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1.5px solid #B87333;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.session-banner .sb-num {
  display: inline-block;
  border: 1.5px solid #B87333;
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 8pt;
  color: #B87333;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
  margin-bottom: 8px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #B87333;
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

/* Rating circles */
.rating-group {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4px 12px;
  margin-bottom: 8px;
}

.rating-row {
  display: flex;
  align-items: center;
  gap: 4px;
}

.rating-row .rr-label {
  font-size: 7.5pt;
  color: #2A2A2A;
  width: 65px;
  flex-shrink: 0;
}

.rating-circle {
  width: 12px;
  height: 12px;
  border: 1.5px solid #B87333;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 5pt;
  color: #B87333;
  margin-right: 1px;
}

/* ================ BAKE SPREAD RIGHT ================ */
.flavor-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2px 12px;
  margin-bottom: 8px;
}

.check-item {
  display: flex;
  align-items: center;
  gap: 4px;
  height: 16px;
}

.check-box {
  width: 9px;
  height: 9px;
  border: 1px solid #B87333;
  border-radius: 2px;
  flex-shrink: 0;
}

.check-item span {
  font-size: 7.5pt;
  color: #2A2A2A;
}

.write-box {
  border: 1px solid #C4A04A;
  border-radius: 3px;
  padding: 6px 8px;
  margin-bottom: 8px;
}

.write-box .wb-label {
  font-size: 7pt;
  color: #B87333;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 2px;
}

.write-box .wb-area {
  height: 28px;
}

/* Star rating */
.stars {
  font-size: 14pt;
  color: #ccc;
  letter-spacing: 3pt;
}

/* ================ HOW TO USE ================ */
.howto-text {
  font-size: 10pt;
  line-height: 1.7;
  color: #2A2A2A;
}

.howto-text p {
  margin-bottom: 8px;
}

.howto-text .ht-title {
  font-size: 11pt;
  font-weight: 700;
  color: #161210;
  margin-bottom: 4px;
  margin-top: 6px;
}

.howto-text .ht-icon {
  color: #B87333;
  font-weight: 700;
  margin-right: 4px;
}

/* ================ REFERENCE TABLES ================ */
.ref-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
}

.ref-table th {
  font-size: 7pt;
  color: #B87333;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 5px 4px;
  border-bottom: 1.5px solid #B87333;
  text-align: left;
}

.ref-table td {
  padding: 5px 4px;
  border-bottom: 1px solid #eee;
  font-size: 8.5pt;
  vertical-align: top;
}

.ref-table td:first-child {
  font-weight: 700;
  color: #161210;
  width: 1in;
}

/* ============ YEAR REVIEW ============ */
.review-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-bottom: 10px;
}

.review-card {
  border: 1px solid #C4A04A;
  border-radius: 4px;
  padding: 8px;
  background: #FAF6F0;
}

.review-card .rc-label {
  font-size: 7pt;
  color: #B87333;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 4px;
}

.review-card .rc-write {
  height: 28px;
  border-bottom: 1px dotted #ccc;
}

/* Notes */
.notes-line {
  border-bottom: 1px solid #ddd;
  height: 22px;
}

/* Final */
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
    <svg viewBox="0 0 100 120" width="90" height="108" xmlns="http://www.w3.org/2000/svg">
      <!-- Boule (round loaf) -->
      <ellipse cx="50" cy="78" rx="36" ry="30" stroke="#C4A04A" stroke-width="1.8" fill="none"/>
      <!-- Top crust dome -->
      <path d="M 16 75 Q 18 48 50 44 Q 82 48 84 75"
            stroke="#E8A838" stroke-width="1.8" fill="none"/>
      <!-- Scoring lines (ear/grigne) -->
      <path d="M 35 52 Q 40 48 45 52" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.6"/>
      <path d="M 48 50 Q 53 46 58 50" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.6"/>
      <path d="M 32 60 Q 40 56 48 60" stroke="#B87333" stroke-width="1" fill="none" opacity="0.4"/>
      <!-- Flour dusting dots -->
      <circle cx="38" cy="66" r="1" fill="#E8A838" opacity="0.4"/>
      <circle cx="55" cy="63" r="1" fill="#E8A838" opacity="0.4"/>
      <circle cx="62" cy="70" r="1" fill="#E8A838" opacity="0.3"/>
      <circle cx="44" cy="72" r="1" fill="#E8A838" opacity="0.3"/>
      <!-- Shadow -->
      <ellipse cx="50" cy="108" rx="30" ry="3" fill="#000" opacity="0.2"/>
    </svg>
  </div>

  <div class="title-main">Sourdough<br>Baking Log</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Every Loaf Tells a Story</div>

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
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Sourdough Journey</div>
    <p>This log is your companion for mastering sourdough bread. Every loaf
    teaches you something &mdash; about your starter, your flour, your
    environment, and your hands. Capture each bake here and watch your
    bread improve.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Bake Spread</div>
    <p>Each bake uses a <strong>two-page spread</strong>. The left page records
    the formula and process: starter details, flour blend, hydration, salt
    percentage, levain build, bulk fermentation time and temperature, proof
    schedule, and bake parameters. The right page captures the results: crumb
    description, crust evaluation, flavor notes, and what to improve next time.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Key Measurements</div>
    <p>&#9679; <strong>Hydration</strong> = Water weight &divide; Flour weight &times; 100.</p>
    <p>&#9679; <strong>Salt Pct</strong> = Salt weight &divide; Flour weight &times; 100 (typically 2%%).</p>
    <p>&#9679; <strong>Levain Pct</strong> = Levain weight &divide; Flour weight &times; 100 (typically 10&ndash;20%%).</p>
    <p>&#9679; Weigh everything in <strong>grams</strong>. Volume measurements
    are not accurate enough for bread.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Temperature Matters</div>
    <p>Dough temperature is the single most important variable in sourdough.
    Warmer dough ferments faster; cooler dough ferments slower. Most formulas
    target a dough temperature of 75&ndash;78&deg;F (24&ndash;26&deg;C) after mixing.
    Always record your ambient temperature and dough temperature.</p>
  </div>
</div>""" % (pg, pg)


def sourdough_basics_page():
    pg = pn()
    return """<!-- PAGE %d: Sourdough Basics -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Sourdough Basics</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">The Sourdough Process</div>
    <div class="section-line"></div>
  </div>

  <table class="ref-table">
    <thead>
      <tr><th>Stage</th><th>What Happens</th></tr>
    </thead>
    <tbody>
      <tr><td>Levain</td><td>Build a small offshoot of your starter with fresh flour and water. Usually 4&ndash;6 hours before mixing.</td></tr>
      <tr><td>Autolyse</td><td>Mix flour and water only. Rest 30&ndash;60 min. Gluten develops, flour hydrates.</td></tr>
      <tr><td>Mix</td><td>Add levain and salt to the autolysed dough. Pinch and fold to incorporate.</td></tr>
      <tr><td>Bulk Ferment</td><td>4&ndash;6 hours at 75&ndash;78&deg;F. Perform stretch-and-folds every 30&ndash;60 min for the first 2&ndash;3 hours.</td></tr>
      <tr><td>Shape</td><td>Preshape, rest 20 min, then final shape into a boule or batard. Tension on the surface.</td></tr>
      <tr><td>Cold Proof</td><td>Refrerate 12&ndash;18 hours at 37&ndash;39&deg;F. Develops flavor, makes scoring easier.</td></tr>
      <tr><td>Bake</td><td>Preheat Dutch oven 500&deg;F. Bake covered 20 min, then uncovered 20&ndash;25 min at 450&deg;F.</td></tr>
    </tbody>
  </table>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Signs of Good Fermentation</div>
    <p style="font-size: 9pt;">&#9679; Dough increases 30&ndash;50%% in volume during bulk.<br>
    &#9679; Surface looks smooth and slightly domed.<br>
    &#9679; Bubbles visible on edges and surface.<br>
    &#9679; Dough feels light and airy, not dense.<br>
    &#9679; Jiggles when gently shaken.</p>
  </div>
</div>""" % (pg, pg)


def baker_percentage_page():
    pg = pn()
    return """<!-- PAGE %d: Baker's Percentage -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Baker's Percentage</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Understanding the Formula</div>
    <div class="section-line"></div>
  </div>

  <div class="howto-text">
    <p style="font-size: 9.5pt;">In baker's percentages, <strong>flour is always
    100%%</strong>. Every other ingredient is expressed as a percentage of the
    flour weight. This lets you scale any formula up or down.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Standard Sourdough Formula</div>
  </div>

  <table class="ref-table">
    <thead>
      <tr><th>Ingredient</th><th>%%</th><th>For 500g Flour</th></tr>
    </thead>
    <tbody>
      <tr><td>Bread Flour</td><td>100%%</td><td>500 g</td></tr>
      <tr><td>Water</td><td>75%%</td><td>375 g</td></tr>
      <tr><td>Levain</td><td>20%%</td><td>100 g</td></tr>
      <tr><td>Salt</td><td>2%%</td><td>10 g</td></tr>
    </tbody>
  </table>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Scaling Example</div>
    <p style="font-size: 9pt;">To make a larger loaf with 600g flour:<br>
    Water = 600 &times; 0.75 = 450 g<br>
    Levain = 600 &times; 0.20 = 120 g<br>
    Salt = 600 &times; 0.02 = 12 g</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Common Hydration Ranges</div>
    <p style="font-size: 8.5pt; color: #555;">
    65&ndash;70%% = Stiff dough, easier to shape, tighter crumb.<br>
    70&ndash;78%% = Standard sourdough, balanced handling.<br>
    78&ndash;85%% = High hydration, open crumb, harder to handle.<br>
    85%%+ = Very slack dough, ciabatta-style, requires skill.</p>
  </div>
</div>""" % (pg, pg)


def flour_types_page():
    pg = pn()
    flours = [
        ("Bread Flour", "12-13%% protein. High gluten. Best for structured loaves with good oven spring."),
        ("All-Purpose", "10-12%% protein. Works for sourdough but slightly weaker. Good for beginners."),
        ("Whole Wheat", "13-14%% protein. Nutty, dense. Use 10-30%% of blend &mdash; too much weakens gluten."),
        ("Rye", "8-9%% protein. Low gluten. Adds flavor and ferments fast. Use 5-15%% of blend."),
        ("Spelt", "12-14%% protein. Tender gluten. Subtle sweet flavor. Substitute up to 50%%."),
        ("Einkorn", "14-18%% protein. Ancient wheat. Weak, sticky gluten. Needs gentle handling."),
    ]
    rows = ""
    for name, desc in flours:
        rows += "<tr><td>%s</td><td>%s</td></tr>\n" % (H.escape(name), H.escape(desc))

    return """<!-- PAGE %d: Flour Types -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Flour Reference Guide</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Common Flour Types</div>
    <div class="section-line"></div>
  </div>

  <table class="ref-table">
    <thead>
      <tr><th>Flour</th><th>Characteristics</th></tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Protein and Gluten</div>
    <p style="font-size: 9pt;">Higher protein flour absorbs more water and
    develops stronger gluten. If you switch from all-purpose to bread flour,
    you may need to increase hydration by 2&ndash;5%% to get the same dough feel.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Whole Grain Adjustments</div>
    <p style="font-size: 8.5pt; color: #555;">
    Whole wheat and rye absorb more water than white flour. When adding whole
    grains, increase hydration by 2&ndash;5%%. Whole grains also speed up
    fermentation &mdash; watch your bulk time.</p>
  </div>
</div>""" % (pg, pg, rows)


def hydration_guide_page():
    pg = pn()
    return """<!-- PAGE %d: Hydration Guide -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Hydration Reference</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Hydration &amp; Dough Feel</div>
    <div class="section-line"></div>
  </div>

  <table class="ref-table">
    <thead>
      <tr><th>Hydration</th><th>Dough Feel &amp; Result</th></tr>
    </thead>
    <tbody>
      <tr><td>60&ndash;65%%</td><td>Stiff, easy to handle. Tight, even crumb. Good for sandwich loaves.</td></tr>
      <tr><td>65&ndash;70%%</td><td>Manageable, slightly tacky. Reliable for beginners. Moderate crumb.</td></tr>
      <tr><td>70&ndash;75%%</td><td>Soft, slightly sticky. Classic artisan texture. Good oven spring.</td></tr>
      <tr><td>75&ndash;80%%</td><td>Soft and sticky. Open, irregular crumb. Requires coil folds.</td></tr>
      <tr><td>80&ndash;85%%</td><td>Very slack, spreads easily. Large open holes. Advanced technique.</td></tr>
      <tr><td>85%%+</td><td>Almost batter-like. Ciabatta and focaccia territory. Very skilled.</td></tr>
    </tbody>
  </table>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Adjusting Hydration</div>
    <p style="font-size: 9pt;">Start at 72%% if you are new to sourdough. Once
    you can consistently shape and bake good loaves, increase by 2&ndash;3%%
    per bake to push toward more open crumb. If dough is too sticky to shape,
    drop hydration back.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Humidity Factor</div>
    <p style="font-size: 8.5pt; color: #555;">
    In humid environments, flour already contains moisture. You may need to
    reduce water by 1&ndash;2%%. In dry environments, you may need a touch more.</p>
  </div>
</div>""" % (pg, pg)


def baking_timeline_page():
    pg = pn()
    return """<!-- PAGE %d: Baking Timeline -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Baking Timeline</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Two-Day Sourdough Schedule</div>
    <div class="section-line"></div>
  </div>

  <table class="ref-table">
    <thead>
      <tr><th>When</th><th>Action</th></tr>
    </thead>
    <tbody>
      <tr><td>Day 1<br>8:00 AM</td><td>Feed starter. Wait until it has doubled and passes the float test.</td></tr>
      <tr><td>Day 1<br>12:00 PM</td><td>Build levain (10-20g starter + 50g flour + 50g water).</td></tr>
      <tr><td>Day 1<br>4:00 PM</td><td>Levain is ready. Begin autolyse: mix flour + water only.</td></tr>
      <tr><td>Day 1<br>5:00 PM</td><td>Add levain and salt to autolysed dough. Pinch to incorporate.</td></tr>
      <tr><td>Day 1<br>5:30 PM</td><td>First set of stretch-and-folds. Then every 30-45 min.</td></tr>
      <tr><td>Day 1<br>9:00 PM</td><td>Bulk ferment continues. Watch for 30-50%% volume growth.</td></tr>
      <tr><td>Day 1<br>10:00 PM</td><td>Divide and shape. Place in banneton, cover well.</td></tr>
      <tr><td>Day 1<br>10:30 PM</td><td>Into the fridge for cold proof. 12-18 hours.</td></tr>
      <tr><td>Day 2<br>8:00 AM</td><td>Preheat Dutch oven in oven at 500&deg;F for 1 hour.</td></tr>
      <tr><td>Day 2<br>9:00 AM</td><td>Score and bake. Covered 20 min, uncovered 20-25 min.</td></tr>
      <tr><td>Day 2<br>9:45 AM</td><td>Bread is done. Cool completely on wire rack (2+ hours).</td></tr>
    </tbody>
  </table>

  <div class="howto-text">
    <p style="font-size: 8pt; font-style: italic; color: #777;">
    Times are approximate for 75&ndash;78&deg;F dough temperature. In winter,
    everything takes longer; in summer, shorter. Adjust accordingly.
    </p>
  </div>
</div>""" % (pg, pg)


def terminology_page():
    pg = pn()
    terms = [
        ("Autolyse", "Resting flour and water together before adding levain and salt. Develops gluten and improves flavor."),
        ("Banneton", "A proofing basket (often cane or wood) that supports shaped dough during cold proof. Leaves a spiral pattern."),
        ("Batard", "An oblong loaf shape. Easier to slice for sandwiches than a round boule."),
        ("Boule", "A round ball-shaped loaf. The most classic sourdough shape."),
        ("Bulk Ferment", "The first and longest rise, after mixing and before shaping. Where most flavor develops."),
        ("Cold Proof", "Refrigerating shaped dough for 12-18 hours. Develops flavor and makes scoring easier."),
        ("Crumb", "The interior texture of the bread. Open crumb = large irregular holes. Tight crumb = small even holes."),
        ("Ear", "The raised flap of crust where the dough was scored. A sign of good oven spring and technique."),
        ("Grigne", "The cut or burst in the crust created by scoring. French for \"grin.\""),
        ("Hydration", "The ratio of water to flour, expressed as a percentage. Higher hydration = softer, stickier dough."),
        ("Levain", "A small build of starter, flour, and water used to leaven the dough. Different from the maintenance starter."),
        ("Oven Spring", "The rapid rise of dough in the first 10 minutes of baking, caused by steam and yeast activity."),
        ("Retard", "Slowing fermentation by refrigerating the dough. Also called cold proof or cold retard."),
        ("Scoring", "Cutting the dough surface before baking to control where it expands. Done with a razor (lame)."),
        ("Stretch & Fold", "A gentle kneading method: grab dough, stretch up, fold over. Repeated several times during bulk."),
        ("Windowpane Test", "Stretching a small piece of dough thin enough to see light through. Tests gluten development."),
    ]
    items = ""
    for term, definition in terms:
        items += """<div style="margin-bottom: 5px;">
    <span style="font-weight: 700; color: #B87333; font-size: 9pt;">%s</span>
    <span style="font-size: 9pt; color: #2A2A2A; margin-left: 8px;">%s</span>
  </div>
""" % (H.escape(term), H.escape(definition))

    return """<!-- PAGE %d: Terminology -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Baking Terminology</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Sourdough Glossary</div>
    <div class="section-line"></div>
  </div>

  %s
</div>""" % (pg, pg, items)


def bake_left(session_num):
    pg = pn()
    return """<!-- PAGE %d: Bake Left #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Sourdough Bake</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="session-banner">
    <span class="sb-num">Loaf #%03d</span>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Loaf Name / Style</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Flour Blend</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Total Flour (g)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Hydration (%%)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Water (g)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Salt (g / %%)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Levain (g / %%)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Ambient Temp (&deg;F)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Dough Temp (&deg;F)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Bulk Ferment (hrs)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Cold Proof (hrs)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Bake Temp Covered</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Bake Temp Uncovered</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Bake Time (min)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Shape</span>
      <div style="display: flex; gap: 6px; padding-top: 2px;">
        <span style="font-size: 7pt; color: #555;"><span class="check-box" style="display:inline-block; width:8px; height:8px; border:1px solid #B87333; border-radius:2px;"></span> Boule</span>
        <span style="font-size: 7pt; color: #555;"><span class="check-box" style="display:inline-block; width:8px; height:8px; border:1px solid #B87333; border-radius:2px;"></span> Batard</span>
        <span style="font-size: 7pt; color: #555;"><span class="check-box" style="display:inline-block; width:8px; height:8px; border:1px solid #B87333; border-radius:2px;"></span> Other</span>
      </div>
    </div>
    <div class="info-field"><span class="if-label">Vessel</span>
      <div style="display: flex; gap: 6px; padding-top: 2px;">
        <span style="font-size: 7pt; color: #555;"><span class="check-box" style="display:inline-block; width:8px; height:8px; border:1px solid #B87333; border-radius:2px;"></span> Dutch Oven</span>
        <span style="font-size: 7pt; color: #555;"><span class="check-box" style="display:inline-block; width:8px; height:8px; border:1px solid #B87333; border-radius:2px;"></span> Stone</span>
        <span style="font-size: 7pt; color: #555;"><span class="check-box" style="display:inline-block; width:8px; height:8px; border:1px solid #B87333; border-radius:2px;"></span> Loaf Pan</span>
      </div>
    </div>
  </div>

  <div style="font-size: 8pt; font-weight: 700; color: #B87333; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px; margin-top: 4px;">
    Quality Ratings (1 = poor, 5 = excellent)
  </div>

  <div class="rating-group">
    <div class="rating-row">
      <span class="rr-label">Oven Spring</span>
      %s
    </div>
    <div class="rating-row">
      <span class="rr-label">Crust</span>
      %s
    </div>
    <div class="rating-row">
      <span class="rr-label">Crumb</span>
      %s
    </div>
    <div class="rating-row">
      <span class="rr-label">Flavor</span>
      %s
    </div>
    <div class="rating-row">
      <span class="rr-label">Texture</span>
      %s
    </div>
    <div class="rating-row">
      <span class="rr-label">Overall</span>
      %s
    </div>
  </div>
</div>""" % (pg, session_num, pg, session_num,
             rating_circles_html(5), rating_circles_html(5), rating_circles_html(5),
             rating_circles_html(5), rating_circles_html(5), rating_circles_html(5))


def bake_right():
    pg = pn()
    crumb_items = [
        "Open / Holey", "Tight / Even", "Gummy", "Moist", "Tender",
        "Chewy", "Cottony", "Translucent", "Irregular", "Dense",
        "Custard-like", "Dry",
    ]
    crust_items = [
        "Thick", "Thin", "Crackly", "Soft", "Blistered",
        "Burnt", "Pale", "Shiny", "Flour-dusted", "Leathery",
    ]
    flavor_items = [
        "Tangy", "Mild", "Sweet", "Nutty", "Smoky",
        "Yeasty", "Complex", "Acidic", "Earthy", "Neutral",
    ]
    crumb_html = check_items_html(crumb_items)
    crust_html = check_items_html(crust_items)
    flavor_html = check_items_html(flavor_items)

    return """<!-- PAGE %d: Bake Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Bake Results</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div style="font-size: 8pt; font-weight: 700; color: #B87333; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">
    Crumb Description (check all that apply)
  </div>

  <div class="flavor-grid" style="border: 1px solid #C4A04A; border-radius: 4px; padding: 6px; margin-bottom: 8px;">
    %s
  </div>

  <div style="font-size: 8pt; font-weight: 700; color: #B87333; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">
    Crust Description (check all that apply)
  </div>

  <div class="flavor-grid" style="border: 1px solid #C4A04A; border-radius: 4px; padding: 6px; margin-bottom: 8px;">
    %s
  </div>

  <div style="font-size: 8pt; font-weight: 700; color: #B87333; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">
    Flavor Profile (check all that apply)
  </div>

  <div class="flavor-grid" style="border: 1px solid #C4A04A; border-radius: 4px; padding: 6px; margin-bottom: 8px;">
    %s
  </div>

  <div class="write-box">
    <div class="wb-label">Scoring Pattern &amp; Notes</div>
    <div class="wb-area"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
    <div class="write-box">
      <div class="wb-label">What Went Well</div>
      <div class="wb-area" style="height: 32px;"></div>
    </div>
    <div class="write-box">
      <div class="wb-label">What to Change Next Time</div>
      <div class="wb-area" style="height: 32px;"></div>
    </div>
  </div>

  <div class="write-box">
    <div class="wb-label">Overall Rating</div>
    <div class="stars">&#9734; &#9734; &#9734; &#9734; &#9734;</div>
  </div>
</div>""" % (pg, pg, crumb_html, crust_html, flavor_html)


def starter_feeding_page():
    pg = pn()
    rows = ""
    for _ in range(14):
        rows += """<tr>
    <td></td><td></td><td></td><td></td><td></td><td></td>
  </tr>
"""
    return """<!-- PAGE %d: Starter Feeding Log -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Starter Feeding Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Starter Health Tracker</div>
    <div class="section-line"></div>
  </div>

  <table class="ref-table">
    <thead>
      <tr>
        <th>Date</th>
        <th>Time</th>
        <th>Temp (&deg;F)</th>
        <th>Ratio (S:F:W)</th>
        <th>Rise Time</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>

  <div class="howto-text">
    <p style="font-size: 8pt; font-style: italic; color: #777;">
    Ratio format = Starter : Flour : Water. A 1:5:5 feeding means 1 part starter,
    5 parts flour, 5 parts water. A healthy starter doubles in 4&ndash;6 hours
    at 70&ndash;75&deg;F and passes the float test.
    </p>
  </div>
</div>""" % (pg, pg, rows)


def year_review_page():
    pg = pn()
    cards = [
        "Total Loaves Baked", "Best Hydration Found", "Favorite Flour Blend",
        "Best Crumb Achievement", "Top-Rated Loaf", "Biggest Baking Lesson",
    ]
    grid = ""
    for label in cards:
        grid += """<div class="review-card">
  <div class="rc-label">%s</div>
  <div class="rc-write"></div>
</div>
""" % H.escape(label)

    return """<!-- PAGE %d: Year in Review -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Year in Review</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">My Baking Year</div>
    <div class="section-line"></div>
  </div>

  <div class="review-grid">
    %s
  </div>

  <div class="write-box">
    <div class="wb-label">New Techniques I Learned</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Baking Goals for Next Year</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>
</div>""" % (pg, pg, grid)


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
      Good bread takes time.<br>
      Every loaf is a lesson.<br>
      Keep baking.
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

    # 1. Title
    pages.append(interior_title_page())

    # 2. How to use
    pages.append(how_to_use_page())

    # 3. Sourdough basics
    pages.append(sourdough_basics_page())

    # 4. Baker's percentage
    pages.append(baker_percentage_page())

    # 5. Flour types
    pages.append(flour_types_page())

    # 6. Hydration guide
    pages.append(hydration_guide_page())

    # 7. Baking timeline
    pages.append(baking_timeline_page())

    # 8. Terminology
    pages.append(terminology_page())

    # 9-10. Starter feeding log (2 pages)
    pages.append(starter_feeding_page())
    pages.append(starter_feeding_page())

    # 11-90. 40 bake spreads (2 pages each = 80 pages)
    for session in range(1, 41):
        pages.append(bake_left(session))
        pages.append(bake_right())

    # 91. Year in review
    pages.append(year_review_page())

    # 92-93. Notes
    for _ in range(2):
        pages.append(notes_page())

    # 94. Final
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
