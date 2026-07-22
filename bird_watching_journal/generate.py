#!/usr/bin/env python3
"""
Bird Watching Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: American bird watchers / birders (all levels)
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "bird_watching_journal_V1.0.html")

BOOK_TITLE = "Bird Watching Journal"
BOOK_SUBTITLE = "Your Field Companion for Birding Adventures"

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

/* ---- Colors ---- */
/* Forest: #2D5016, #3A6B1F, #4A7C28 */
/* Sky: #4A90B8, #6BAED6 */
/* Earth: #6B5B3F, #8B7A5A */
/* Gold: #C8A441 */
/* Cream: #FAF6ED, #F5F0E1 */

/* ---- Cover ---- */
.cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(160deg, #1a3608 0%, #2D5016 30%, #3A6B1F 60%, #2D5016 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Leaf/branch texture on cover */
.cover .nature-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 20px 8px at 15% 20%, #ffffff, transparent),
    radial-gradient(ellipse 18px 7px at 85% 15%, #ffffff, transparent),
    radial-gradient(ellipse 22px 9px at 75% 80%, #ffffff, transparent),
    radial-gradient(ellipse 16px 6px at 25% 75%, #ffffff, transparent),
    radial-gradient(ellipse 14px 5px at 50% 50%, #ffffff, transparent),
    radial-gradient(ellipse 12px 5px at 10% 60%, #ffffff, transparent),
    radial-gradient(ellipse 15px 6px at 90% 55%, #ffffff, transparent),
    radial-gradient(ellipse 13px 5px at 40% 90%, #ffffff, transparent);
}

/* CSS Bird silhouette */
.cover .bird-silhouette {
  width: 90px; height: 60px;
  position: relative;
  margin: 0 auto 24px;
}
/* Bird body */
.cover .bird-body {
  width: 50px; height: 32px;
  background: #C8A441;
  border-radius: 50% 50% 45% 55%;
  position: absolute;
  top: 14px; left: 20px;
  box-shadow: 1px 2px 6px rgba(0,0,0,0.3);
}
/* Bird head */
.cover .bird-head {
  width: 26px; height: 26px;
  background: #C8A441;
  border-radius: 50%;
  position: absolute;
  top: 6px; left: 52px;
  box-shadow: 1px 1px 4px rgba(0,0,0,0.2);
}
/* Bird beak */
.cover .bird-beak {
  width: 0; height: 0;
  border-left: 12px solid #D4941C;
  border-top: 4px solid transparent;
  border-bottom: 4px solid transparent;
  position: absolute;
  top: 16px; left: 76px;
}
/* Bird eye */
.cover .bird-eye {
  width: 4px; height: 4px;
  background: #1a1a1a;
  border-radius: 50%;
  position: absolute;
  top: 15px; left: 66px;
}
/* Bird tail */
.cover .bird-tail {
  width: 22px; height: 16px;
  background: #C8A441;
  position: absolute;
  top: 20px; left: 2px;
  border-radius: 0 0 0 60%;
  clip-path: polygon(100% 0, 0 50%, 100% 100%);
}
/* Bird wing */
.cover .bird-wing {
  width: 36px; height: 20px;
  background: #B8941C;
  border-radius: 50%;
  position: absolute;
  top: 18px; left: 22px;
  transform: rotate(-10deg);
}

/* Branch under bird */
.cover .branch {
  width: 160px; height: 3px;
  background: #8B7A5A;
  position: absolute;
  bottom: -8px; left: 50%;
  transform: translateX(-50%);
  border-radius: 2px;
}
.cover .branch::before {
  content: "";
  position: absolute;
  width: 30px; height: 2px;
  background: #8B7A5A;
  top: -1px; left: -12px;
  transform: rotate(-30deg);
}
.cover .branch::after {
  content: "";
  position: absolute;
  width: 25px; height: 2px;
  background: #8B7A5A;
  top: 2px; right: -8px;
  transform: rotate(40deg);
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
  text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
}

.cover .accent-bar {
  width: 100px; height: 2.5px;
  background: #C8A441;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 11pt;
  color: #c4d4a8;
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
  background: rgba(255,255,255,0.10);
  border: 1px solid rgba(200,164,65,0.5);
  color: #C8A441;
  font-size: 7pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 9px;
  border-radius: 3px;
  text-transform: uppercase;
}

.cover .season-tag {
  font-size: 8.5pt;
  color: #c4d4a8;
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
  color: #C8A441;
  letter-spacing: 2pt;
  text-transform: uppercase;
  font-weight: 700;
}

/* ---- Section Divider ---- */
.divider {
  width: 6in; height: 9in;
  page-break-after: always;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  background: linear-gradient(160deg, #1a3608 0%, #2D5016 50%, #1a3608 100%);
  position: relative;
  overflow: hidden;
}
.divider .div-leaf {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 20px 8px at 15% 20%, #ffffff, transparent),
    radial-gradient(ellipse 18px 7px at 85% 15%, #ffffff, transparent),
    radial-gradient(ellipse 22px 9px at 75% 80%, #ffffff, transparent),
    radial-gradient(ellipse 16px 6px at 25% 75%, #ffffff, transparent),
    radial-gradient(ellipse 14px 5px at 50% 50%, #ffffff, transparent);
}
.divider .div-num {
  font-size: 60pt;
  color: rgba(200,164,65,0.15);
  font-weight: 700;
  position: absolute;
  top: 1in;
}
.divider .div-label {
  font-size: 10pt;
  color: #C8A441;
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
  color: #c4d4a8;
  font-style: italic;
  margin-top: 14px;
  position: relative;
}

/* ---- Content Pages ---- */
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 7.5pt;
  color: #999;
  padding-bottom: 4px;
  border-bottom: 1.5px solid #3A6B1F;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #2D5016;
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
  color: #2D5016;
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
  border-bottom: 0.5px solid #c8c8c8;
  height: 22px;
}
.wline-wide {
  border-bottom: 0.5px solid #c8c8c8;
  height: 26px;
}

/* ---- Dotted Lines (for sketch areas) ---- */
.dot-line {
  border-bottom: 1px dotted #d0d0d0;
  height: 22px;
}

/* ---- Field Labels ---- */
.field-label {
  font-size: 7.5pt;
  font-weight: 700;
  color: #2D5016;
  text-transform: uppercase;
  letter-spacing: 0.8pt;
  margin-bottom: 3px;
  margin-top: 8px;
}
.field-label .small-note {
  font-weight: 400;
  text-transform: none;
  letter-spacing: 0;
  color: #aaa;
  font-style: italic;
  font-size: 6.5pt;
  float: right;
}

.fill-blank {
  border-bottom: 0.5px solid #999;
  height: 16px;
  display: inline-block;
}

/* ---- Checkbox ---- */
.checkbox {
  display: inline-block;
  width: 10px; height: 10px;
  border: 1px solid #555;
  border-radius: 2px;
  margin-right: 4px;
  vertical-align: middle;
}

/* ---- Data Table ---- */
.log-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 7pt;
  margin-bottom: 8px;
}
.log-table th {
  background: #3A6B1F;
  color: white;
  padding: 3px 3px;
  text-align: center;
  font-weight: 700;
  font-size: 6.5pt;
  letter-spacing: 0.3pt;
}
.log-table td {
  border: 0.5px solid #bbb;
  padding: 3px;
  font-size: 7pt;
  height: 20px;
  text-align: center;
}
.log-table td.text-col {
  text-align: left;
  padding-left: 4px;
}

/* ---- Life List Table ---- */
.life-list-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 7pt;
}
.life-list-table th {
  background: #3A6B1F;
  color: white;
  padding: 3px 4px;
  font-size: 6.5pt;
  font-weight: 700;
  text-align: center;
}
.life-list-table td {
  border: 0.5px solid #ccc;
  padding: 3px 4px;
  font-size: 7pt;
  height: 18px;
}
.life-list-table td.num-col {
  text-align: center;
  font-weight: 700;
  color: #3A6B1F;
  width: 8%;
}
.life-list-table td.name-col {
  text-align: left;
  width: 42%;
}
.life-list-table td.check-col {
  text-align: center;
  width: 8%;
}

/* ---- Checkbox circle ---- */
.check-circle {
  display: inline-block;
  width: 12px; height: 12px;
  border: 1px solid #888;
  border-radius: 50%;
  vertical-align: middle;
}

/* ---- Owner Page ---- */
.owner-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100%;
}
.owner-page .owner-icon {
  width: 40px; height: 40px;
  background: #C8A441;
  border-radius: 50% 50% 45% 55%;
  position: relative;
  margin: 0 auto 20px;
}
.owner-page .owner-icon::before {
  content: "";
  position: absolute;
  width: 20px; height: 20px;
  background: #C8A441;
  border-radius: 50%;
  top: -8px; right: -6px;
}
.owner-page .owner-title {
  font-size: 18pt;
  font-weight: 700;
  color: #2D5016;
  margin-bottom: 6px;
}
.owner-page .owner-sub {
  font-size: 9pt;
  color: #888;
  font-style: italic;
  margin-bottom: 28px;
}
.owner-line {
  width: 4in;
  margin: 10px auto;
  text-align: left;
}
.owner-line .ol-label {
  font-size: 8pt;
  font-weight: 700;
  color: #2D5016;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  margin-bottom: 2px;
}
.owner-line .ol-blank {
  border-bottom: 1px solid #999;
  height: 20px;
}

/* ---- Sketch / Drawing Area ---- */
.sketch-box {
  border: 0.5px dashed #aaa;
  background: #fcfaf5;
  border-radius: 3px;
}

/* ---- Season Box ---- */
.season-box {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
}
.season-card {
  border: 0.5px solid #bbb;
  padding: 5px 6px;
  border-radius: 3px;
  font-size: 7pt;
}
.season-card .sc-label {
  font-weight: 700;
  color: #3A6B1F;
  text-transform: uppercase;
  font-size: 6.5pt;
  letter-spacing: 0.5pt;
  margin-bottom: 2px;
}

/* ---- Info Box ---- */
.info-box {
  background: #F5F0E1;
  border-left: 3px solid #C8A441;
  padding: 8px 10px;
  margin: 8px 0;
  border-radius: 0 3px 3px 0;
}
.info-box .ib-title {
  font-size: 7.5pt;
  font-weight: 700;
  color: #2D5016;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  margin-bottom: 4px;
}
.info-box p {
  font-size: 7.5pt;
  color: #555;
  line-height: 1.6;
}

/* ---- Notes Page ---- */
.notes-page-title {
  font-size: 12pt;
  font-weight: 700;
  color: #2D5016;
  margin-bottom: 10px;
  border-bottom: 2px solid #C8A441;
  padding-bottom: 5px;
}

/* ---- Back Cover ---- */
.back-cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: auto;
  background: linear-gradient(160deg, #1a3608 0%, #2D5016 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.back-cover .bc-leaf {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 20px 8px at 15% 20%, #ffffff, transparent),
    radial-gradient(ellipse 22px 9px at 75% 80%, #ffffff, transparent),
    radial-gradient(ellipse 16px 6px at 25% 75%, #ffffff, transparent);
}
.back-cover .bc-content {
  position: relative;
  z-index: 2;
  padding: 0 0.6in;
}
.back-cover .bc-title {
  font-size: 15pt;
  color: #C8A441;
  font-weight: 700;
  margin-bottom: 12px;
  letter-spacing: 1pt;
}
.back-cover .bc-text {
  font-size: 9pt;
  color: #c4d4a8;
  line-height: 1.8;
  margin-bottom: 20px;
}
.back-cover .bc-features {
  text-align: left;
  margin: 0 auto 24px;
  max-width: 3.5in;
}
.back-cover .bc-features li {
  list-style: none;
  font-size: 8pt;
  color: #e0e0e0;
  margin: 5px 0;
}
.back-cover .bc-features li::before {
  content: "\25B8 ";
  color: #C8A441;
}
.back-cover .bc-publisher {
  font-size: 9pt;
  color: #C8A441;
  letter-spacing: 2pt;
  text-transform: uppercase;
  font-weight: 700;
}
"""

# ============================================================
# HELPER FUNCTIONS
# ============================================================
def esc(s):
    return H.escape(str(s))

def footer(text=BOOK_TITLE):
    return f'<div class="page-footer"><span></span><span>{esc(text)}</span></div>'

def sh(left, right=""):
    return f'<div class="section-header"><span class="sh-left">{esc(left)}</span><span class="sh-right">{esc(right)}</span></div>'

def writing_lines(n, wide=False):
    cls = "wline-wide" if wide else "wline"
    return "\n".join(f'<div class="{cls}"></div>' for _ in range(n))

def page_open(sec_left, sec_right, title=None, subtitle=None):
    pnum = pn()
    html = f'<div class="page">{sh(sec_left, sec_right)}'
    if title:
        html += f'<div class="page-title">{esc(title)}</div>'
    if subtitle:
        html += f'<div class="page-subtitle">{esc(subtitle)}</div>'
    return html, pnum

# ============================================================
# PAGE BUILDERS
# ============================================================

def build_cover():
    pn()
    return '''<div class="cover">
  <div class="nature-bg"></div>
  <div class="title-block">
    <div class="bird-silhouette">
      <div class="bird-tail"></div>
      <div class="bird-body"></div>
      <div class="bird-wing"></div>
      <div class="bird-head"></div>
      <div class="bird-eye"></div>
      <div class="bird-beak"></div>
      <div class="branch"></div>
    </div>
    <div class="main-title">BIRD WATCHING<br/>JOURNAL</div>
    <div class="accent-bar"></div>
    <div class="subtitle">Your Field Companion for<br/>Birding Adventures &amp; Discoveries</div>
    <div class="features">
      <span class="feature-badge">Life List</span>
      <span class="feature-badge">Sighting Log</span>
      <span class="feature-badge">Field Notes</span>
      <span class="feature-badge">Sketch Pages</span>
    </div>
    <div class="season-tag">&#9737; Explore. Observe. Record. &#9737;</div>
  </div>
  <div class="publisher">More Shine Press</div>
</div>'''

def build_back_cover():
    pn()
    return '''<div class="back-cover">
  <div class="bc-leaf"></div>
  <div class="bc-content">
    <div class="bc-title">&#9737; A Perfect Gift for Nature Lovers &#9737;</div>
    <p class="bc-text">Whether you're a seasoned birder or just discovering the joy of birdwatching, this journal is your companion for every adventure.</p>
    <ul class="bc-features">
      <li>Keep a running life list of every species you see</li>
      <li>Log detailed sighting records with location and weather</li>
      <li>Track birds by season, habitat, and behavior</li>
      <li>Sketch and describe your feathered discoveries</li>
      <li>Plan birding trips and record your adventures</li>
      <li>Reflect on the beauty of nature all year long</li>
    </ul>
    <p class="bc-text" style="font-style:italic;">Every bird tells a story. Start recording yours!</p>
  </div>
  <div class="bc-publisher">More Shine Press</div>
</div>'''

def build_owner_page():
    pn()
    return f'''<div class="page">
<div class="owner-page">
  <div class="owner-icon"></div>
  <div class="owner-title">This Journal Belongs To</div>
  <div class="owner-sub">Fill in your details below</div>
  <div class="owner-line">
    <div class="ol-label">Name</div>
    <div class="ol-blank"></div>
  </div>
  <div class="owner-line">
    <div class="ol-label">Home Location / Region</div>
    <div class="ol-blank"></div>
  </div>
  <div class="owner-line">
    <div class="ol-label">Favorite Birding Spot</div>
    <div class="ol-blank"></div>
  </div>
  <div class="owner-line">
    <div class="ol-label">Favorite Bird Species</div>
    <div class="ol-blank"></div>
  </div>
  <div class="owner-line">
    <div class="ol-label">Year Started Birding</div>
    <div class="ol-blank"></div>
  </div>
</div>
</div>'''

def build_how_to_use():
    pn()
    tips = [
        ("Sighting Log", "Record every bird you spot in the field. Note the species, date, location, weather, and behavior. Use the field marks section to describe identifying features."),
        ("Life List", "Your running tally of every species you've ever identified. Check off each bird the first time you see it, and record the date and location of that exciting first sighting."),
        ("Trip Journal", "Document your birding trips — where you went, who you were with, what conditions were like, and the highlights of your adventure."),
        ("Sketch Pages", "Use the blank and lightly-lined pages to sketch birds you observe. Drawing helps you notice details and improves your identification skills."),
        ("Seasonal Guide", "Track migration patterns and seasonal changes. Note when birds arrive in spring and depart in fall, and how behavior changes throughout the year."),
    ]
    html = f'''<div class="page">
{sh("Getting Started", "How to Use This Journal")}
<div class="page-title">How to Use This Journal</div>
<div class="page-subtitle">A quick guide to getting the most out of your birding adventures</div>
'''
    for i, (title, desc) in enumerate(tips, 1):
        html += f'''<div style="margin-bottom: 10px;">
<div style="display:flex; align-items:baseline; margin-bottom:2px;">
<span style="font-size:13pt; font-weight:700; color:#C8A441; margin-right:6px;">{i}</span>
<span style="font-size:9.5pt; font-weight:700; color:#2D5016;">{esc(title)}</span>
</div>
<p style="font-size:8pt; color:#555; line-height:1.55; padding-left:20px;">{esc(desc)}</p>
</div>'''

    html += f'''<div class="info-box" style="margin-top:16px;">
<div class="ib-title">&#9737; Birding Ethics</div>
<p>Always respect wildlife and their habitats. Keep a respectful distance, never disturb nesting birds, and follow all local rules in parks and natural areas. Leave no trace — take only photos and memories.</p>
</div>
{footer()}
</div>'''
    return html

def build_birder_profile():
    pn()
    return f'''<div class="page">
{sh("My Birding Journey", "My Profile")}
<div class="page-title">My Birding Profile</div>
<div class="page-subtitle">Record your birding identity and goals</div>

<div class="field-label">My Experience Level</div>
<div style="font-size:8pt; color:#555; margin:4px 0;">
<span class="checkbox"></span> Beginner &nbsp;&nbsp;
<span class="checkbox"></span> Intermediate &nbsp;&nbsp;
<span class="checkbox"></span> Advanced &nbsp;&nbsp;
<span class="checkbox"></span> Expert
</div>

<div class="field-label">How I Got Started Birding</div>
{writing_lines(3)}

<div class="field-label">My Birding Gear</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">Binoculars, field guide, camera, apps, etc.</div>
{writing_lines(3)}

<div class="field-label">My Favorite Places to Bird</div>
{writing_lines(4)}

<div class="field-label">Birds I Most Hope to See (Bucket List)</div>
{writing_lines(5)}

<div class="field-label">My Goals for This Year</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">e.g., Identify 50 new species, visit 5 new birding spots, learn 20 bird songs</div>
{writing_lines(4)}

{footer()}
</div>'''

def build_habitat_ref():
    pn()
    habitats = [
        ("Backyard / Feeder", "Songbirds, finches, sparrows, woodpeckers, hummingbirds"),
        ("Deciduous Forest", "Warblers, thrushes, vireos, tanagers, owls"),
        ("Coniferous Forest", "Crossbills, kinglets, nuthatches, grouse"),
        ("Wetlands / Marsh", "Herons, egrets, ducks, rails, marsh wrens"),
        ("Lakes &amp; Ponds", "Grebes, loons, geese, swallows, kingfishers"),
        ("Grasslands / Fields", "Meadowlarks, bobolinks, hawks, sparrows"),
        ("Coast / Shoreline", "Gulls, terns, sandpipers, plovers, pelicans"),
        ("Urban / City Parks", "Pigeons, doves, starlings, crows, raptors"),
    ]

    html = f'''<div class="page">
{sh("Reference", "Habitat Guide")}
<div class="page-title">Habitat Quick Reference</div>
<div class="page-subtitle">Common birding habitats and species you might find there</div>
'''
    for habitat, birds in habitats:
        html += f'''<div style="margin-bottom: 6px; padding: 4px 8px; background:#F5F0E1; border-radius:3px; border-left:3px solid #3A6B1F;">
<div style="font-size:8pt; font-weight:700; color:#2D5016; margin-bottom:1px;">{habitat}</div>
<div style="font-size:7pt; color:#666;">{birds}</div>
</div>'''

    html += f'''
<div class="info-box">
<div class="ib-title">&#9737; Tip</div>
<p>Different habitats attract different species. Visit a variety of habitats throughout the year to maximize the number of species on your life list!</p>
</div>
{footer()}
</div>'''
    return html

def build_seasonal_ref():
    pn()
    seasons = [
        ("Spring (Mar-May)", "Migration season! Warblers, thrushes, and flycatchers return. Courtship displays, territorial singing, and nest building begin. Peak time for diversity."),
        ("Summer (Jun-Aug)", "Breeding season. Fledglings are everywhere. Look for nesting behavior and juvenile plumages. Shorebirds begin southbound migration in late summer."),
        ("Fall (Sep-Nov)", "Southbound migration. Hawks, eagles, and falcons soar overhead. Sparrows and waterfowl arrive. Confusing fall plumages challenge identification skills."),
        ("Winter (Dec-Feb)", "Year-round residents plus northern visitors. Owls, hawks, finches, and sparrows. Feeder activity peaks. Great time for waterfowl and raptor watching."),
    ]

    html = f'''<div class="page">
{sh("Reference", "Seasonal Guide")}
<div class="page-title">Seasonal Birding Guide</div>
<div class="page-subtitle">What to expect and watch for each season</div>
'''
    for season, desc in seasons:
        html += f'''<div style="margin-bottom: 8px;">
<div style="font-size:9pt; font-weight:700; color:#2D5016; margin-bottom:2px;">{season}</div>
<p style="font-size:7.5pt; color:#555; line-height:1.55; padding-left:8px;">{desc}</p>
</div>'''

    html += f'''
<div class="field-label" style="margin-top:6px;">My Seasonal Notes</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">Record what you notice about birds in each season where you live</div>

<div class="season-box" style="margin-top:4px;">
<div class="season-card">
<div class="sc-label">Spring</div>
{writing_lines(3)}
</div>
<div class="season-card">
<div class="sc-label">Summer</div>
{writing_lines(3)}
</div>
<div class="season-card">
<div class="sc-label">Fall</div>
{writing_lines(3)}
</div>
<div class="season-card">
<div class="sc-label">Winter</div>
{writing_lines(3)}
</div>
</div>
{footer()}
</div>'''
    return html

def build_identification_ref():
    pn()
    html = f'''<div class="page">
{sh("Reference", "Identification")}
<div class="page-title">Bird Identification Tips</div>
<div class="page-subtitle">Key features to look for when identifying birds</div>

<div class="field-label">The Five Keys to Identification</div>
'''

    keys = [
        ("Size &amp; Shape", "Compare to familiar birds. Is it sparrow-sized? Robin-sized? Crow-sized? Note the silhouette — body shape, bill, tail, and wings."),
        ("Color Pattern", "Note overall color, but also look for specific markings: wing bars, eye rings, caps, bibs, streaks, and patches. Remember: light matters!"),
        ("Behavior", "How does it move? Does it tail-bob, wing-flick, or hover? Does it walk, hop, or climb? Is it alone or in a flock? What is it eating?"),
        ("Habitat", "Where are you? Forest, field, wetland, or shore? Habitat narrows down possibilities dramatically."),
        ("Voice", "Songs and calls are often the best clue. Learn common bird sounds. Note rhythm, pitch, and quality."),
    ]

    for i, (title, desc) in enumerate(keys, 1):
        html += f'''<div style="margin-bottom: 7px;">
<div style="display:flex; align-items:baseline;">
<span style="font-size:11pt; font-weight:700; color:#C8A441; margin-right:5px;">{i}</span>
<span style="font-size:8.5pt; font-weight:700; color:#2D5016;">{title}</span>
</div>
<p style="font-size:7.5pt; color:#555; line-height:1.5; padding-left:20px;">{desc}</p>
</div>'''

    html += f'''
<div class="field-label">Field Marks to Note</div>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:3px; font-size:7pt; color:#555;">
<div><span class="checkbox"></span> Bill shape &amp; color</div>
<div><span class="checkbox"></span> Eye color / eye ring</div>
<div><span class="checkbox"></span> Head pattern / cap</div>
<div><span class="checkbox"></span> Wing bars / patches</div>
<div><span class="checkbox"></span> Tail shape / pattern</div>
<div><span class="checkbox"></span> Leg &amp; foot color</div>
<div><span class="checkbox"></span> Underpart streaks</div>
<div><span class="checkbox"></span> Rump / vent color</div>
</div>

<div class="info-box" style="margin-top:8px;">
<div class="ib-title">&#9737; Remember</div>
<p>Lighting, distance, and season can all affect how a bird looks. Don't rely on just one feature — use a combination of clues for confident identification.</p>
</div>
{footer()}
</div>'''
    return html

def build_monthly_tracker():
    """Monthly checklist — what birds to look for each month."""
    pn()
    months = [
        ("January", "Winter residents at feeders. Look for owls, hawks, winter finches, waterfowl."),
        ("February", "Owls begin nesting. Early spring songs. Duck migration begins."),
        ("March", "Early migrants arrive. Red-winged blackbirds, robins, killdeer. Woodpeckers drumming."),
        ("April", "Peak migration begins. Warblers, swallows, thrushes return. Courtship displays."),
        ("May", "Peak warbler migration! Flycatchers, vireos, tanagers arrive. Shorebird migration."),
        ("June", "Breeding season peak. Baby birds everywhere. Nesting activity. Song at maximum."),
        ("July", "Shorebirds begin southbound migration. Young birds learning to feed. Quiet post-breeding."),
        ("August", "Fall migration ramps up. Warblers in fall plumage. Hummingbirds heading south."),
        ("September", "Hawk migration peaks. Broad-winged hawks in kettles. Nighthawks and swifts moving."),
        ("October", "Sparrow migration. Waterfowl arriving. Late warblers. Kinglets and creepers."),
        ("November", "Waterfowl peak. Late hawks. Northern finches may arrive. Winter residents settling in."),
        ("December", "Christmas Bird Count season! Winter residents established. Owl prowls. Feeder birds."),
    ]

    html = f'''<div class="page">
{sh("Reference", "Monthly Guide")}
<div class="page-title">Month-by-Month Guide</div>
<div class="page-subtitle">What to watch for throughout the year</div>
'''

    for month, desc in months:
        html += f'''<div style="margin-bottom: 5px; padding: 3px 6px; border-left: 3px solid #3A6B1F; background:#fafaf5; border-radius:0 3px 3px 0;">
<div style="font-size:7.5pt; font-weight:700; color:#2D5016; display:inline-block; width:70px;">{month}</div>
<span style="font-size:6.5pt; color:#666;">{desc}</span>
</div>'''

    html += f'''{footer()}
</div>'''
    return html

def build_sighting_log():
    """Detailed sighting log — one page per sighting block."""
    html, pnum = page_open(
        "Sighting Log",
        "Field Record",
        "Sighting Log",
        "Record your observations in the field"
    )

    html += '''
<table class="log-table">
<tr>
<th>Date</th>
<th>Time</th>
<th>Species</th>
<th>#</th>
<th>Location</th>
</tr>
<tr><td></td><td></td><td class="text-col"></td><td></td><td class="text-col"></td></tr>
<tr><td></td><td></td><td class="text-col"></td><td></td><td class="text-col"></td></tr>
<tr><td></td><td></td><td class="text-col"></td><td></td><td class="text-col"></td></tr>
<tr><td></td><td></td><td class="text-col"></td><td></td><td class="text-col"></td></tr>
<tr><td></td><td></td><td class="text-col"></td><td></td><td class="text-col"></td></tr>
<tr><td></td><td></td><td class="text-col"></td><td></td><td class="text-col"></td></tr>
<tr><td></td><td></td><td class="text-col"></td><td></td><td class="text-col"></td></tr>
<tr><td></td><td></td><td class="text-col"></td><td></td><td class="text-col"></td></tr>
</table>

<div style="display:flex; gap:8px; margin-top:4px;">
  <div style="flex:1;">
    <div class="field-label" style="margin-top:2px;">Weather</div>
    <div style="font-size:7pt; color:#555;">
    <span class="checkbox"></span> Sunny &nbsp;
    <span class="checkbox"></span> Cloudy &nbsp;
    <span class="checkbox"></span> Rainy &nbsp;
    <span class="checkbox"></span> Foggy<br/>
    Temp: <span class="fill-blank" style="width:40px;"></span> Wind: <span class="fill-blank" style="width:40px;"></span>
    </div>
  </div>
  <div style="flex:1;">
    <div class="field-label" style="margin-top:2px;">Habitat</div>
    <div style="font-size:7pt; color:#555;">
    <span class="checkbox"></span> Forest &nbsp;
    <span class="checkbox"></span> Wetland &nbsp;
    <span class="checkbox"></span> Field<br/>
    <span class="checkbox"></span> Backyard &nbsp;
    <span class="checkbox"></span> Shore &nbsp;
    <span class="checkbox"></span> Urban
    </div>
  </div>
</div>

<div class="field-label">Behavior &amp; Activity Notes <span class="small-note">feeding, singing, flying, nesting, perching, etc.</span></div>
'''

    for _ in range(6):
        html += '<div style="border-bottom:0.5px solid #ddd; height:20px; display:flex;"><span style="font-size:6pt; color:#ccc; padding-top:3px;">Species:</span><span style="flex:1;"></span></div>'

    html += f'''
<div style="font-size:7pt; color:#aaa; margin-top:2px;">
<span class="checkbox"></span> First sighting (life bird!) &nbsp;&nbsp;
<span class="checkbox"></span> Photo taken &nbsp;&nbsp;
<span class="checkbox"></span> Audio recorded &nbsp;&nbsp;
<span class="checkbox"></span> Heard only
</div>

<div class="field-label">Field Notes &amp; Observations</div>
{writing_lines(2)}

{footer()}
</div>'''
    return html

def build_life_list(title_suffix="", start_num=1):
    """Life list checklist page."""
    html, pnum = page_open(
        "Life List",
        f"Species Checklist{title_suffix}",
        f"Life List{title_suffix}",
        "Check off each species the first time you identify it"
    )

    html += '<table class="life-list-table">'
    html += '<tr><th>#</th><th>Species Name</th><th>Date First Seen</th><th>Location</th><th>&#10003;</th></tr>'

    for i in range(start_num, start_num + 20):
        html += f'<tr><td class="num-col">{i}</td><td class="name-col"></td><td></td><td></td><td class="check-col"><span class="check-circle"></span></td></tr>'

    html += f'</table>\n{footer()}\n</div>'
    return html

def build_trip_journal():
    """Birding trip journal page."""
    html, pnum = page_open(
        "Trip Journal",
        "Birding Adventure",
        "Birding Trip Journal",
        "Document your birding adventures"
    )

    html += '''
<div style="display:flex; justify-content:space-between; margin-bottom:6px;">
  <div style="font-size:8pt; color:#555;">Date: <span class="fill-blank" style="width:100px;"></span></div>
  <div style="font-size:8pt; color:#555;">Start Time: <span class="fill-blank" style="width:60px;"></span> End: <span class="fill-blank" style="width:60px;"></span></div>
</div>

<div class="field-label">Location / Site Name</div>
{w1}

<div class="field-label">Companions</div>
{w2}

<div class="field-label">Weather Conditions</div>
<div style="font-size:7pt; color:#555;">
Sky: <span class="fill-blank" style="width:80px;"></span> &nbsp;
Temp: <span class="fill-blank" style="width:50px;"></span> &nbsp;
Wind: <span class="fill-blank" style="width:50px;"></span>
</div>

<div class="field-label">Species Observed <span class="small-note">list each species and count</span></div>
<table class="log-table">
<tr><th style="width:55%;">Species</th><th style="width:15%;">Count</th><th>Notes</th></tr>'''.format(
        w1=writing_lines(1),
        w2=writing_lines(1)
    )

    for _ in range(8):
        html += '<tr><td class="text-col"></td><td></td><td class="text-col"></td></tr>'

    html += '</table>'

    html += '''
<div class="field-label">Trip Highlights &amp; Memorable Moments</div>
'''
    html += writing_lines(4)

    html += '''
<div class="field-label">Total Species Count</div>
<div style="font-size:24pt; font-weight:700; color:#3A6B1F; text-align:center; padding:4px;">_______</div>

<div class="field-label">Field Notes &amp; Observations</div>
'''
    html += writing_lines(2)

    html += f'''
<div style="font-size:7pt; color:#aaa;">
<span class="checkbox"></span> Life bird seen &nbsp;&nbsp;
<span class="checkbox"></span> Photos taken &nbsp;&nbsp;
<span class="checkbox"></span> First visit to this site &nbsp;&nbsp;
<span class="checkbox"></span> Would return
</div>
{footer()}
</div>'''
    return html

def build_backyard_log():
    """Backyard feeder watch log."""
    html, pnum = page_open(
        "Backyard Watch",
        "Feeder &amp; Garden",
        "Backyard Bird Watch Log",
        "Track the birds that visit your yard and feeders"
    )

    html += '''
<div style="display:flex; justify-content:space-between; margin-bottom:6px;">
  <div style="font-size:8pt; color:#555;">Date: <span class="fill-blank" style="width:100px;"></span></div>
  <div style="font-size:8pt; color:#555;">Season: <span class="fill-blank" style="width:80px;"></span></div>
</div>

<div class="field-label">Weather</div>
<div style="font-size:7pt; color:#555;">
<span class="checkbox"></span> Sunny &nbsp;
<span class="checkbox"></span> Cloudy &nbsp;
<span class="checkbox"></span> Rainy &nbsp;
<span class="checkbox"></span> Snowy &nbsp;
Temp: <span class="fill-blank" style="width:50px;"></span>
</div>

<div class="field-label">Feeder Types in Use</div>
<div style="font-size:7pt; color:#555;">
<span class="checkbox"></span> Tube feeder &nbsp;
<span class="checkbox"></span> Hopper &nbsp;
<span class="checkbox"></span> Suet &nbsp;
<span class="checkbox"></span> Nyjer/thistle &nbsp;
<span class="checkbox"></span> Hummingbird &nbsp;
<span class="checkbox"></span> Ground/tray
</div>

<div class="field-label">Visitor Log <span class="small-note">species &amp; how many at once</span></div>
<table class="log-table">
<tr><th style="width:40%;">Species</th><th style="width:15%;">Max Count</th><th>Behavior / Food</th></tr>'''

    for _ in range(10):
        html += '<tr><td class="text-col"></td><td></td><td class="text-col"></td></tr>'

    html += '</table>'

    html += f'''
<div class="field-label">Observations &amp; Notes</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">Interactions, dominance, new visitors, nesting activity, etc.</div>
{writing_lines(3)}

<div style="font-size:7pt; color:#aaa;">
<span class="checkbox"></span> New yard bird! &nbsp;&nbsp;
<span class="checkbox"></span> Predator seen (hawk/cat) &nbsp;&nbsp;
<span class="checkbox"></span> Refilled feeder today
</div>
{footer()}
</div>'''
    return html

def build_sketch_page(title="Field Sketch", subtitle="Draw what you see — notes help you remember"):
    """Sketch/drawing page with blank space and notes area."""
    html, pnum = page_open(
        "Field Sketch",
        "",
        title,
        subtitle
    )

    # Large sketch area
    html += '<div class="sketch-box" style="height:4.2in; margin-bottom:8px;"></div>'

    html += '''
<div class="field-label">Species</div>
<div style="border-bottom:0.5px solid #999; height:16px;"></div>

<div style="display:flex; gap:10px; margin-top:4px;">
  <div style="flex:1;">
    <div class="field-label" style="margin-top:2px;">Date &amp; Location</div>
    <div style="border-bottom:0.5px solid #999; height:16px;"></div>
  </div>
  <div style="flex:1;">
    <div class="field-label" style="margin-top:2px;">Size / Color</div>
    <div style="border-bottom:0.5px solid #999; height:16px;"></div>
  </div>
</div>

<div class="field-label">Field Marks &amp; Description <span class="small-note">beak, plumage, behavior, distinctive features</span></div>
'''

    html += writing_lines(4)

    html += f'{footer()}\n</div>'
    return html

def build_migration_tracker():
    """Seasonal migration tracker."""
    html, pnum = page_open(
        "Migration Tracker",
        "Seasonal Movements",
        "Migration Tracker",
        "Record arrival and departure dates for migrating species"
    )

    html += '''
<div class="field-label">Spring Arrival Dates</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">When do migrants first appear in your area each spring?</div>
<table class="log-table">
<tr><th style="width:40%;">Species</th><th style="width:20%;">First Seen</th><th style="width:20%;">Last Year</th><th>Notes</th></tr>'''
    for _ in range(6):
        html += '<tr><td class="text-col"></td><td></td><td></td><td class="text-col"></td></tr>'
    html += '</table>'

    html += '''
<div class="field-label">Fall Departure Dates</div>
<div style="font-size:7pt; color:#aaa; font-style:italic;">When do migrants leave your area each fall?</div>
<table class="log-table">
<tr><th style="width:40%;">Species</th><th style="width:20%;">Last Seen</th><th style="width:20%;">Last Year</th><th>Notes</th></tr>'''
    for _ in range(6):
        html += '<tr><td class="text-col"></td><td></td><td></td><td class="text-col"></td></tr>'
    html += '</table>'

    html += f'''
<div class="field-label">Migration Notes &amp; Patterns</div>
{writing_lines(2)}
{footer()}
</div>'''
    return html

def build_year_summary():
    """Year-in-review summary page."""
    html, pnum = page_open(
        "Year in Review",
        "Annual Summary",
        "My Birding Year in Review",
        "Reflect on your birding adventures this year"
    )

    html += '''
<div style="font-size:10pt; font-weight:700; color:#2D5016; text-align:center; margin-bottom:10px;">
Year: <span class="fill-blank" style="width:80px;"></span>
</div>

<div class="field-label">Total Species Identified This Year</div>
<div style="font-size:20pt; font-weight:700; color:#3A6B1F; text-align:center; padding:2px;">_______</div>

<div class="field-label">Total Birding Trips</div>
<div style="font-size:20pt; font-weight:700; color:#3A6B1F; text-align:center; padding:2px;">_______</div>

<div class="field-label">New Life Birds This Year</div>
<div style="font-size:9pt; color:#555; text-align:center; padding:2px;">
Added <span class="fill-blank" style="width:30px;"></span> species to my life list!
</div>

<div class="field-label">Best Birding Moment of the Year</div>
'''
    html += writing_lines(3)

    html += '''
<div class="field-label">Best New Bird (My Favorite Discovery)</div>
'''
    html += writing_lines(2)

    html += '''
<div class="field-label">New Places I Went Birding</div>
'''
    html += writing_lines(3)

    html += '''
<div class="field-label">What I Learned This Year</div>
'''
    html += writing_lines(3)

    html += '''
<div class="field-label">Goals for Next Year</div>
'''
    html += writing_lines(3)

    html += f'{footer()}\n</div>'
    return html

def build_notes_page(title="Field Notes"):
    html, pnum = page_open("Notes", "", title)
    html += writing_lines(26)
    html += f'{footer()}\n</div>'
    return html

def build_divider(part_num, label, title, subtitle):
    pn()
    return f'''<div class="divider">
  <div class="div-leaf"></div>
  <div class="div-num">{part_num}</div>
  <div style="position:relative; text-align:center;">
    <div class="div-label">{esc(label)}</div>
    <div class="div-title">{esc(title)}</div>
    <div class="div-sub">{esc(subtitle)}</div>
  </div>
</div>'''

# ============================================================
# MAIN
# ============================================================
def main():
    pages = []

    # === FRONT MATTER ===
    pages.append(build_cover())
    pages.append(build_owner_page())
    pages.append(build_how_to_use())
    pages.append(build_birder_profile())
    pages.append(build_habitat_ref())
    pages.append(build_seasonal_ref())
    pages.append(build_identification_ref())
    pages.append(build_monthly_tracker())

    # === SECTION 1: SIGHTING LOG ===
    pages.append(build_divider("01", "Part One", "Sighting\nLog", "Record every bird you observe in the field"))

    for _ in range(24):
        pages.append(build_sighting_log())

    # === SECTION 2: LIFE LIST ===
    pages.append(build_divider("02", "Part Two", "Life\nList", "Your running tally of every species identified"))

    # 6 pages x 20 entries = 120 life list slots
    for i in range(6):
        start = i * 20 + 1
        suffix = f" (cont. {i+1})" if i > 0 else ""
        pages.append(build_life_list(suffix, start))

    # === SECTION 3: TRIP JOURNAL ===
    pages.append(build_divider("03", "Part Three", "Trip\nJournal", "Document your birding adventures and travels"))

    for _ in range(14):
        pages.append(build_trip_journal())

    # === SECTION 4: BACKYARD WATCH ===
    pages.append(build_divider("04", "Part Four", "Backyard\nBird Watch", "Track the feathered visitors to your yard and feeders"))

    for _ in range(10):
        pages.append(build_backyard_log())

    # === SECTION 5: MIGRATION & SEASONS ===
    pages.append(build_divider("05", "Part Five", "Migration\nTracker", "Record the rhythms of bird movement through the year"))

    for _ in range(6):
        pages.append(build_migration_tracker())

    # === SECTION 6: SKETCH PAGES ===
    pages.append(build_divider("06", "Part Six", "Field\nSketches", "Draw and describe the birds you encounter"))

    for _ in range(16):
        pages.append(build_sketch_page())

    # === SECTION 7: YEAR IN REVIEW & NOTES ===
    pages.append(build_divider("07", "Part Seven", "Year in Review\n& Notes", "Reflect on your birding journey and record your thoughts"))

    pages.append(build_year_summary())
    pages.append(build_year_summary())

    for _ in range(26):
        pages.append(build_notes_page())

    # === BACK COVER ===
    pages.append(build_back_cover())

    # === Assemble ===
    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(BOOK_TITLE)} — {esc(BOOK_SUBTITLE)}</title>
<style>{CSS}</style>
</head>
<body>
{"".join(pages)}
</body>
</html>'''

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)

    total_pages = page_no[0]
    print(f"Generated: {HTML_FILE}")
    print(f"Total pages: {total_pages}")
    print(f"File size: {os.path.getsize(HTML_FILE):,} bytes")

if __name__ == "__main__":
    main()
