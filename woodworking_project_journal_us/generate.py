#!/usr/bin/env python3
"""
Woodworking Project Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Woodworkers, carpenters, DIY makers, hobbyist furniture builders
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "woodworking_project_journal_us_V1.0.html")

BOOK_TITLE = "Woodworking Project Journal"
BOOK_SUBTITLE = "Build It Right, Document Every Cut"

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
   Oak: #8B6B3D, #A07D4A, #6B4E2E
   Steel blue: #5A7A8A, #7A9AAA, #4A6A7A
   Gold: #C4A04A
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #8B6B3D, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #5A7A8A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #8B6B3D, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #7A9AAA, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #6B4E2E, transparent);
}

/* ===== CSS Saw + Wood Illustration ===== */
.cover .tool-wrap {
  width: 120px; height: 170px;
  position: relative;
  margin: 0 auto 18px;
}

/* Wood plank */
.cover .plank-base {
  width: 80px; height: 55px;
  position: absolute;
  top: 90px; left: 20px;
  background: linear-gradient(180deg,
    rgba(139,107,61,0.18) 0%,
    rgba(107,78,46,0.12) 100%);
  border: 1px solid rgba(139,107,61,0.30);
  border-radius: 2px;
}

/* Wood grain lines */
.cover .grain1 {
  width: 72px; height: 1px;
  position: absolute;
  top: 98px; left: 24px;
  background: rgba(107,78,46,0.20);
}
.cover .grain2 {
  width: 72px; height: 1px;
  position: absolute;
  top: 106px; left: 24px;
  background: rgba(107,78,46,0.15);
}
.cover .grain3 {
  width: 72px; height: 1px;
  position: absolute;
  top: 115px; left: 24px;
  background: rgba(107,78,46,0.18);
}
.cover .grain4 {
  width: 72px; height: 1px;
  position: absolute;
  top: 125px; left: 24px;
  background: rgba(107,78,46,0.12);
}
.cover .grain5 {
  width: 72px; height: 1px;
  position: absolute;
  top: 135px; left: 24px;
  background: rgba(107,78,46,0.15);
}

/* Saw blade (circle) */
.cover .saw-blade {
  width: 48px; height: 48px;
  position: absolute;
  top: 20px; left: 36px;
  border-radius: 50%;
  background: radial-gradient(circle,
    rgba(90,122,138,0.15) 0%,
    rgba(90,122,138,0.08) 60%,
    transparent 100%);
  border: 1px solid rgba(90,122,138,0.35);
}

/* Saw teeth (triangles) */
.cover .saw-teeth {
  width: 48px; height: 48px;
  position: absolute;
  top: 20px; left: 36px;
  border-radius: 50%;
  border: 2px dashed rgba(90,122,138,0.25);
}

/* Saw center hole */
.cover .saw-center {
  width: 8px; height: 8px;
  position: absolute;
  top: 40px; left: 56px;
  border-radius: 50%;
  background: rgba(22,22,22,0.30);
  border: 1px solid rgba(90,122,138,0.30);
}

/* Shavings/curls falling */
.cover .curl1 {
  width: 14px; height: 6px;
  position: absolute;
  top: 75px; left: 30px;
  background: rgba(160,125,74,0.15);
  border-radius: 50%;
  border: 1px solid rgba(139,107,61,0.20);
  transform: rotate(-15deg);
}
.cover .curl2 {
  width: 12px; height: 5px;
  position: absolute;
  top: 68px; left: 72px;
  background: rgba(139,107,61,0.12);
  border-radius: 50%;
  border: 1px solid rgba(139,107,61,0.18);
  transform: rotate(20deg);
}
.cover .curl3 {
  width: 10px; height: 4px;
  position: absolute;
  top: 82px; left: 55px;
  background: rgba(160,125,74,0.10);
  border-radius: 50%;
  border: 1px solid rgba(139,107,61,0.15);
  transform: rotate(-30deg);
}

/* Pencil */
.cover .pencil {
  width: 3px; height: 50px;
  position: absolute;
  top: 20px; left: 10px;
  background: linear-gradient(180deg,
    rgba(196,160,74,0.20) 0%,
    rgba(196,160,74,0.15) 70%,
    rgba(160,125,74,0.10) 100%);
  border: 1px solid rgba(196,160,74,0.20);
  border-radius: 1px;
  transform: rotate(-15deg);
}

/* Sparkle */
.cover .sparkle1 {
  width: 4px; height: 4px;
  background: rgba(196,160,74,0.4);
  border-radius: 50%;
  position: absolute;
  top: 15px; left: 90px;
  box-shadow: 0 0 4px rgba(196,160,74,0.3);
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 24pt;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.15;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 6px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 110px; height: 2.5px;
  background: #8B6B3D;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 11pt;
  color: #7A9AAA;
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
  border: 1px solid rgba(139,107,61,0.40);
  color: #8B6B3D;
  font-size: 7pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 9px;
  border-radius: 3px;
  text-transform: uppercase;
}

.cover .tagline {
  font-size: 8.5pt;
  color: #7A9AAA;
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #8B6B3D, transparent),
    radial-gradient(ellipse 25px 15px at 80% 30%, #5A7A8A, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 25% 85%, #8B6B3D, transparent);
}

.divider .div-num {
  font-size: 60pt;
  color: rgba(139,107,61,0.12);
  font-weight: 700;
  position: absolute;
  top: 1in;
}

.divider .div-label {
  font-size: 10pt;
  color: #8B6B3D;
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
  color: #7A9AAA;
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
  border-bottom: 1.5px solid #8B6B3D;
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
  background: #8B6B3D;
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
  border-left: 3px solid #8B6B3D;
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
  border: 1.5px solid #8B6B3D;
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
  color: #8B6B3D;
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
  color: #8B6B3D;
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
  <div class="tool-wrap">
    <div class="sparkle1"></div>
    <div class="pencil"></div>
    <div class="saw-blade"></div>
    <div class="saw-teeth"></div>
    <div class="saw-center"></div>
    <div class="curl1"></div>
    <div class="curl2"></div>
    <div class="curl3"></div>
    <div class="plank-base"></div>
    <div class="grain1"></div>
    <div class="grain2"></div>
    <div class="grain3"></div>
    <div class="grain4"></div>
    <div class="grain5"></div>
  </div>
  <div class="title-block">
    <div class="main-title">%s</div>
    <div class="accent-bar"></div>
    <div class="subtitle">%s</div>
    <div class="features">
      <span class="feature-badge">40 Project Logs</span>
      <span class="feature-badge">Cut Lists</span>
      <span class="feature-badge">Wood Guide</span>
      <span class="feature-badge">Joinery Ref</span>
    </div>
    <div class="tagline">For Woodworkers &amp; Makers</div>
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
      <div style="font-size: 8pt; font-weight: 700; color: #8B6B3D; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Skill Level</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #8B6B3D; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Shop / Workshop</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #8B6B3D; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Primary Tools</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #8B6B3D; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Wood</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Woodworking Project Journal</span>
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
  <div class="page-subtitle">Measure twice, document once</div>

  <div class="info-box">
    <div class="info-title">Why Document Your Builds?</div>
    Every project teaches lessons. A journal captures dimensions that worked, joints that held, and finishes that looked beautiful. When you revisit a project months later, your notes save you from repeating mistakes and help you refine techniques. Your journal becomes a personal reference library of hard-won woodworking knowledge.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Tips for Better Documentation</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Sketch before you cut.</strong> Draw the project with dimensions before heading to the shop. A dimensioned sketch catches design flaws and generates your cut list automatically.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Record the actual dimensions.</strong> Plans change in the shop. Write down the real measurements you used, not just the plan dimensions. This is how reproductions get easier.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Note wood movement.</strong> Record the wood species, grain orientation, and how the piece behaved over seasons. Wood moves &mdash; your joints should account for it.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Document finish schedules.</strong> Write down every step of your finishing process, including products, number of coats, sanding grits, and drying times. Finish results are hard to reproduce from memory.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Track time and cost honestly.</strong> Record actual material costs and hours spent. This transforms future estimates from guesswork into data. You will be surprised what projects actually cost.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>6. Photograph the finished piece.</strong> Take photos from multiple angles in good light. Store a reference photo number in your journal entry.
    </div>
  </div>

  <div class="page-footer">
    <span>Woodworking Project Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def wood_species_reference():
    pg = pn()
    return """<!-- PAGE %d: Wood Species -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Common Wood Species</span>
  </div>

  <div class="page-title">Common Wood Species</div>
  <div class="page-subtitle">Properties of popular workshop woods</div>

  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th>Species</th>
      <th style="width:28px;">Type</th>
      <th style="width:28px;">Hard.</th>
      <th style="width:28px;">Work</th>
      <th style="width:32px;">Price</th>
      <th>Best Uses &amp; Notes</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Pine</td>
      <td>Soft</td>
      <td style="text-align:center;">380</td>
      <td style="text-align:center;">Easy</td>
      <td style="text-align:center;">$</td>
      <td>Shop furniture, framing, practice. Takes stain unevenly.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Poplar</td>
      <td>Hard</td>
      <td style="text-align:center;">540</td>
      <td style="text-align:center;">Easy</td>
      <td style="text-align:center;">$</td>
      <td>Painted furniture, hidden parts. Inexpensive hardwood.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Oak (Red)</td>
      <td>Hard</td>
      <td style="text-align:center;">1290</td>
      <td style="text-align:center;">Med</td>
      <td style="text-align:center;">$$</td>
      <td>Furniture, flooring. Strong open grain. Takes stain well.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Oak (White)</td>
      <td>Hard</td>
      <td style="text-align:center;">1360</td>
      <td style="text-align:center;">Med</td>
      <td style="text-align:center;">$$</td>
      <td>Furniture, outdoor projects. Rot resistant.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Maple (Hard)</td>
      <td>Hard</td>
      <td style="text-align:center;">1450</td>
      <td style="text-align:center;">Hard</td>
      <td style="text-align:center;">$$</td>
      <td>Furniture, cutting boards, floors. Dense and light-colored.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Cherry</td>
      <td>Hard</td>
      <td style="text-align:center;">950</td>
      <td style="text-align:center;">Med</td>
      <td style="text-align:center;">$$$</td>
      <td>Fine furniture. Darkens beautifully with age. Easy to work.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Walnut</td>
      <td>Hard</td>
      <td style="text-align:center;">1010</td>
      <td style="text-align:center;">Med</td>
      <td style="text-align:center;">$$$</td>
      <td>Premium furniture. Rich dark brown. Excellent workability.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Ash</td>
      <td>Hard</td>
      <td style="text-align:center;">1320</td>
      <td style="text-align:center;">Med</td>
      <td style="text-align:center;">$$</td>
      <td>Chairs, bent work, tool handles. Strong and elastic.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Birch</td>
      <td>Hard</td>
      <td style="text-align:center;">1260</td>
      <td style="text-align:center;">Med</td>
      <td style="text-align:center;">$</td>
      <td>Plywood, furniture, drawers. Affordable, even texture.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Cedar</td>
      <td>Soft</td>
      <td style="text-align:center;">350</td>
      <td style="text-align:center;">Easy</td>
      <td style="text-align:center;">$$</td>
      <td>Outdoor projects, chests, closets. Rot and insect resistant.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Douglas Fir</td>
      <td>Soft</td>
      <td style="text-align:center;">660</td>
      <td style="text-align:center;">Med</td>
      <td style="text-align:center;">$</td>
      <td>Structural beams, framing. Stronger than pine.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Mahogany</td>
      <td>Hard</td>
      <td style="text-align:center;">800</td>
      <td style="text-align:center;">Easy</td>
      <td style="text-align:center;">$$$</td>
      <td>Fine furniture, boats. Stable, beautiful grain. Easy to work.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Birch Ply</td>
      <td>Ply</td>
      <td style="text-align:center;">Var.</td>
      <td style="text-align:center;">Easy</td>
      <td style="text-align:center;">$</td>
      <td>Cabinets, casework, jigs. Stable and strong. Edge banding hides plies.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">MDF</td>
      <td>Comp.</td>
      <td style="text-align:center;">Var.</td>
      <td style="text-align:center;">Easy</td>
      <td style="text-align:center;">$</td>
      <td>Painted panels, templates. Very stable. No grain. Dust hazard.</td>
    </tr>
  </table>

  <div style="margin-top: 6px; padding: 5px 8px; background: #FAF8F4; border-radius: 3px; font-size: 6.5pt; color: #777; font-style: italic;">
    Hard. = Janka hardness (higher = harder/denser). Work = ease of working. Price: $ = budget, $$ = moderate, $$$ = premium. Janka values approximate; varies by tree and region. Always account for wood movement when designing solid wood projects.
  </div>

  <div class="page-footer">
    <span>Woodworking Project Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def joinery_reference():
    pg = pn()
    return """<!-- PAGE %d: Joinery -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Joinery Methods</span>
  </div>

  <div class="page-title">Common Woodworking Joints</div>
  <div class="page-subtitle">From simple to refined</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px;">
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Butt Joint</div>
      <div class="prop-card-value">Simplest joint. Two pieces meet at 90&deg;. Weak without fasteners. Use screws, dowels, or biscuits for strength. Good for quick utility projects.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Miter Joint</div>
      <div class="prop-card-value">Two pieces cut at 45&deg; forming a 90&deg; corner. Hides end grain. Elegant but weak without reinforcement. Reinforce with splines or biscuits.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Dado</div>
      <div class="prop-card-value">A square-bottomed groove cut across the grain. Excellent for shelves and cabinet construction. Strong mechanical connection. Cut with dado stack or router.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Rabbet</div>
      <div class="prop-card-value">A groove cut along the edge of a board. Used for cabinet backs, drawer construction, and joinery. Provides good glue surface and alignment.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Dado + Rabbet</div>
      <div class="prop-card-value">Combines both for casework corners. Self-aligning and strong. Standard for cabinet and bookshelf construction.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Mortise &amp; Tenon</div>
      <div class="prop-card-value">A rectangular projection (tenon) fits into a matching hole (mortise). The gold standard for frame construction. Very strong. Used in chairs, tables, doors.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Half-Blind Dovetail</div>
      <div class="prop-card-value">Interlocking pins and tails, hidden from the front. Premium drawer joint. Extremely strong. Machine-cut or hand-cut. Shows craftsmanship.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Through Dovetail</div>
      <div class="prop-card-value">Visible interlocking pins and tails on both faces. The strongest and most decorative joint. Used for boxes, chests, and fine casework. Hand-cut = master level.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Box Joint (Finger)</div>
      <div class="prop-card-value">Rectangular interlocking fingers. Easier to cut than dovetails. Strong glue surface. Great for boxes and drawers. Cut on table saw or router.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Biscuit Joint</div>
      <div class="prop-card-value">Oval compressed wood wafers (biscuits) fit into matching slots. Great for alignment in panel glue-ups and miter joints. Quick with a biscuit joiner.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Pocket Hole</div>
      <div class="prop-card-value">Angled holes drilled with a jig. Screws pull pieces together. Fast and strong. Great for face frames and beginner-friendly joinery.</div>
    </div>
    <div class="prop-card" style="margin-bottom: 4px;">
      <div class="prop-card-label">Tongue &amp; Groove</div>
      <div class="prop-card-value">A projecting tongue on one board fits into a groove on another. Used for flooring, paneling, and tabletops. Self-aligning and hides gaps.</div>
    </div>
  </div>

  <div class="page-footer">
    <span>Woodworking Project Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def finish_reference():
    pg = pn()
    return """<!-- PAGE %d: Finishes -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Finishing Guide</span>
  </div>

  <div class="page-title">Finishing Options</div>
  <div class="page-subtitle">Choose the right finish for each project</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:60px;">Finish Type</th>
      <th style="width:28px;">Durab.</th>
      <th style="width:28px;">Ease</th>
      <th>Application &amp; Notes</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Oil (Linseed/Tung)</td>
      <td style="text-align:center;">Low</td>
      <td style="text-align:center;">Easy</td>
      <td>Penetrating. Brings out grain, natural feel. Apply with rag, wipe off excess. Multiple coats. Food-safe when cured. Best for decorative pieces.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Oil + Wax</td>
      <td style="text-align:center;">Low</td>
      <td style="text-align:center;">Easy</td>
      <td>Oil finish followed by paste wax. Soft satin sheen. Beautiful on fine furniture. Reapply wax annually.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Shellac</td>
      <td style="text-align:center;">Med</td>
      <td style="text-align:center;">Med</td>
      <td>Quick-drying natural resin. French polish for high gloss. Sealer coat under other finishes. Not water/heat resistant. Food-safe (de-waxed).</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Polyurethane</td>
      <td style="text-align:center;">High</td>
      <td style="text-align:center;">Med</td>
      <td>Durable clear coat. Water-based (clear, low odor) or oil-based (amber, tougher). Tabletops, floors. 3+ coats recommended.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Varnish</td>
      <td style="text-align:center;">High</td>
      <td style="text-align:center;">Med</td>
      <td>Durable and weather-resistant. Spar varnish for outdoor projects. Slower drying than poly. Brush or wipe on.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Lacquer</td>
      <td style="text-align:center;">High</td>
      <td style="text-align:center;">Hard</td>
      <td>Fast-drying professional finish. Spray application. Multiple thin coats melt into each other. Beautiful depth. Requires spray equipment.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Water-Based</td>
      <td style="text-align:center;">Med</td>
      <td style="text-align:center;">Easy</td>
      <td>Cleanup with water. Low odor. Non-yellowing. Good for painted projects and light woods. Less durable than oil-based.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Paint</td>
      <td style="text-align:center;">Med</td>
      <td style="text-align:center;">Easy</td>
      <td>Primer + 2 coats. Water-based latex (easy cleanup) or oil-based enamel (tougher). Use on poplar or MDF for painted furniture.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Danish Oil</td>
      <td style="text-align:center;">Med</td>
      <td style="text-align:center;">Easy</td>
      <td>Blend of oil and varnish. Easy wipe-on application. Some build plus grain enhancement. Great all-purpose finish for beginners.</td>
    </tr>
  </table>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Sanding Grit Progression</div>
    <table class="data-table" style="font-size: 7.5pt;">
      <tr><th>Stage</th><th style="width:30px;">Grit</th><th>When</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Rough / Paint Removal</td><td style="text-align:center;">60-80</td><td>Removing old finish, shaping, rough sanding</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Initial Smoothing</td><td style="text-align:center;">100-120</td><td>Removing mill marks, leveling surface</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Pre-Finish</td><td style="text-align:center;">150-180</td><td>Final sanding before finish application</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Between Coats</td><td style="text-align:center;">220-320</td><td>Between finish coats to remove dust nibs</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Final Polish</td><td style="text-align:center;">400+</td><td>Wet sanding final coat for mirror finish</td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Woodworking Project Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def measurements_reference():
    pg = pn()
    return """<!-- PAGE %d: Measurements -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Conversion &amp; Measurement</span>
  </div>

  <div class="page-title">Measurement Reference</div>
  <div class="page-subtitle">Fractions, decimals, and metric conversions</div>

  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th style="width:55px;">Fraction</th>
      <th style="width:55px;">Decimal</th>
      <th style="width:55px;">Metric (mm)</th>
      <th style="width:50px;">Letter</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">1/16"</td><td>0.0625"</td><td>1.6 mm</td><td>&mdash;</td></tr>
    <tr><td style="font-weight:700;color:#161616;">1/8"</td><td>0.1250"</td><td>3.2 mm</td><td>&mdash;</td></tr>
    <tr><td style="font-weight:700;color:#161616;">3/16"</td><td>0.1875"</td><td>4.8 mm</td><td>&mdash;</td></tr>
    <tr><td style="font-weight:700;color:#161616;">1/4"</td><td>0.2500"</td><td>6.4 mm</td><td>E</td></tr>
    <tr><td style="font-weight:700;color:#161616;">5/16"</td><td>0.3125"</td><td>7.9 mm</td><td>&mdash;</td></tr>
    <tr><td style="font-weight:700;color:#161616;">3/8"</td><td>0.3750"</td><td>9.5 mm</td><td>F</td></tr>
    <tr><td style="font-weight:700;color:#161616;">7/16"</td><td>0.4375"</td><td>11.1 mm</td><td>&mdash;</td></tr>
    <tr><td style="font-weight:700;color:#161616;">1/2"</td><td>0.5000"</td><td>12.7 mm</td><td>H</td></tr>
    <tr><td style="font-weight:700;color:#161616;">5/8"</td><td>0.6250"</td><td>15.9 mm</td><td>J/K</td></tr>
    <tr><td style="font-weight:700;color:#161616;">3/4"</td><td>0.7500"</td><td>19.1 mm</td><td>O/P</td></tr>
    <tr><td style="font-weight:700;color:#161616;">7/8"</td><td>0.8750"</td><td>22.2 mm</td><td>Q/R</td></tr>
    <tr><td style="font-weight:700;color:#161616;">1"</td><td>1.0000"</td><td>25.4 mm</td><td>T/U</td></tr>
  </table>

  <div style="margin-top: 12px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Lumber Dimensions (Nominal vs Actual)</div>
    <table class="data-table" style="font-size: 7.5pt;">
      <tr>
        <th style="width:60px;">Nominal</th>
        <th style="width:60px;">Actual (in)</th>
        <th style="width:55px;">Actual (mm)</th>
        <th>Common Uses</th>
      </tr>
      <tr><td style="font-weight:700;color:#161616;">1x2</td><td>3/4 x 1-1/2"</td><td>19 x 38 mm</td><td>Trim, furring, small projects</td></tr>
      <tr><td style="font-weight:700;color:#161616;">1x4</td><td>3/4 x 3-1/2"</td><td>19 x 89 mm</td><td>Shelving, trim, casework</td></tr>
      <tr><td style="font-weight:700;color:#161616;">1x6</td><td>3/4 x 5-1/2"</td><td>19 x 140 mm</td><td>Shelving, paneling, furniture</td></tr>
      <tr><td style="font-weight:700;color:#161616;">1x8</td><td>3/4 x 7-1/4"</td><td>19 x 184 mm</td><td>Wide shelving, furniture sides</td></tr>
      <tr><td style="font-weight:700;color:#161616;">1x12</td><td>3/4 x 11-1/4"</td><td>19 x 286 mm</td><td>Wide panels, tabletops</td></tr>
      <tr><td style="font-weight:700;color:#161616;">2x4</td><td>1-1/2 x 3-1/2"</td><td>38 x 89 mm</td><td>Framing, furniture structure</td></tr>
      <tr><td style="font-weight:700;color:#161616;">2x6</td><td>1-1/2 x 5-1/2"</td><td>38 x 140 mm</td><td>Shelves, table tops, framing</td></tr>
      <tr><td style="font-weight:700;color:#161616;">2x8</td><td>1-1/2 x 7-1/4"</td><td>38 x 184 mm</td><td>Tabletops, wide shelving</td></tr>
      <tr><td style="font-weight:700;color:#161616;">4x4</td><td>3-1/2 x 3-1/2"</td><td>89 x 89 mm</td><td>Table legs, posts, structure</td></tr>
    </table>
  </div>

  <div style="margin-top: 8px; padding: 5px 10px; background: #FAF8F4; border-radius: 3px; font-size: 7pt; color: #777; font-style: italic;">
    <strong style="color: #8B6B3D;">Board Foot Formula:</strong> Board feet = (Thickness (in) x Width (in) x Length (ft)) / 12. Example: a 1" x 6" x 8' board = (1 x 6 x 8) / 12 = 4 board feet.
  </div>

  <div class="page-footer">
    <span>Woodworking Project Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def safety_reference():
    pg = pn()
    return """<!-- PAGE %d: Safety -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Shop Safety</span>
  </div>

  <div class="page-title">Workshop Safety Rules</div>
  <div class="page-subtitle">Protect yourself and your tools</div>

  <div class="info-box">
    <div class="info-title">The Number One Rule</div>
    Never put your fingers in the path of a blade. If an operation feels unsafe, it is. Stop, reassess, use a push stick, jig, or clamp. There is always a safer way to make any cut.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Personal Protection</div>
    <div style="margin-bottom: 5px;"><strong>1.</strong> Safety glasses always. No exceptions. Wood chips, sawdust, and broken bits fly in any direction.</div>
    <div style="margin-bottom: 5px;"><strong>2.</strong> Hearing protection for power tools. Table saws, routers, and planers cause permanent hearing damage over time.</div>
    <div style="margin-bottom: 5px;"><strong>3.</strong> Dust mask or respirator when sanding or cutting MDF. Fine dust causes serious lung damage. Connect dust collection where possible.</div>
    <div style="margin-bottom: 5px;"><strong>4.</strong> No loose clothing, jewelry, or long hair near spinning tools. Roll up sleeves, remove rings.</div>
    <div style="margin-bottom: 12px;"><strong>5.</strong> Closed-toe shoes. Steel-toe boots for heavy work.</div>

    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Power Tool Safety</div>
    <div style="margin-bottom: 5px;"><strong>6.</strong> Table saw: Use the blade guard, riving knife, and anti-kickback pawls. Learn to recognize and avoid kickback.</div>
    <div style="margin-bottom: 5px;"><strong>7.</strong> Always use push sticks for narrow or short cuts. Keep fingers at least 6 inches from any blade.</div>
    <div style="margin-bottom: 5px;"><strong>8.</strong> Never freehand cut on a table saw. Use the fence or miter gauge. Never use both at once.</div>
    <div style="margin-bottom: 5px;"><strong>9.</strong> Unplug tools before changing blades or bits. Wait for blades to stop spinning completely.</div>
    <div style="margin-bottom: 5px;"><strong>10.</strong> Keep blades and bits sharp. Dull tools require more force, increasing risk of slips and kickback.</div>
    <div style="margin-bottom: 12px;"><strong>11.</strong> Keep a clean floor. Sawdust and offcuts cause slips. Sweep between operations.</div>

    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Finishing Safety</div>
    <div style="margin-bottom: 5px;"><strong>12.</strong> Work in a well-ventilated area for solvent-based finishes. Use a vapor respirator for spraying.</div>
    <div style="margin-bottom: 5px;"><strong>13.</strong> No open flames near solvents. Oil-soaked rags can spontaneously combust &mdash; store in water or spread flat to dry.</div>
    <div><strong>14.</strong> Store chemicals properly, away from heat sources and out of reach of children.</div>
  </div>

  <div class="page-footer">
    <span>Woodworking Project Journal</span>
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


def project_log_left(project_num):
    """Left page: project identity, materials, cut list, sketch"""
    pg = pn()
    return """<!-- PAGE %d: Project %d Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Project #%02d</span>
    <span class="sh-right">Plan &amp; Materials</span>
  </div>

  <div class="page-title">Project #%02d &mdash; Blueprint</div>
  <div class="page-subtitle">Design, materials, and cut list</div>

  <!-- Project Info -->
  <div style="background: #FAF8F4; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Status</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Project Name</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">For / Client</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Dimensions -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Overall Dimensions</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">Width</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Depth</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Height</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
  </div>

  <!-- Cut List -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Cut List</div>
  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Part Name</th>
      <th style="width:30px;">Wood</th>
      <th style="width:22px;">Qty</th>
      <th style="width:28px;">L (in)</th>
      <th style="width:28px;">W (in)</th>
      <th style="width:28px;">T (in)</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">4</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">5</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">6</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <!-- Sketch -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Dimensioned Sketch</div>
  <div class="dot-grid" style="width: 100%%; height: 1.6in; border-radius: 4px;"></div>

  <div class="page-footer">
    <span>Project #%02d &mdash; Blueprint</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, project_num, project_num, project_num, project_num, page_no[0])


def project_log_right(project_num):
    """Right page: build log, finish, cost, notes"""
    pg = pn()
    return """<!-- PAGE %d: Project %d Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Project #%02d</span>
    <span class="sh-right">Build Log &amp; Notes</span>
  </div>

  <div class="page-title">Project #%02d &mdash; Build Record</div>
  <div class="page-subtitle">Construction, finishing, and reflection</div>

  <!-- Joinery used -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Joinery Used &mdash; Check All That Apply</div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Butt</span>
    <span class="check-item"><span class="check-box"></span> Miter</span>
    <span class="check-item"><span class="check-box"></span> Dado</span>
    <span class="check-item"><span class="check-box"></span> Rabbet</span>
    <span class="check-item"><span class="check-box"></span> Mortise/Tenon</span>
    <span class="check-item"><span class="check-box"></span> Dovetail</span>
  </div>
  <div class="check-row" style="margin-bottom: 6px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Box Joint</span>
    <span class="check-item"><span class="check-box"></span> Biscuit</span>
    <span class="check-item"><span class="check-box"></span> Pocket Hole</span>
    <span class="check-item"><span class="check-box"></span> Dowel</span>
    <span class="check-item"><span class="check-box"></span> Tongue/Groove</span>
    <span class="check-item"><span class="check-box"></span> Other</span>
  </div>

  <!-- Tools -->
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-bottom: 8px;">
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Primary Tools</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Glue / Adhesive</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
  </div>

  <!-- Finish -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Finish Schedule</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">Finish Type</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label"># Coats</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Final Grit</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
  </div>

  <!-- Cost & Time -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Cost &amp; Time</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">Wood Cost</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Hardware $</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Hours</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
  </div>

  <!-- Quality ratings -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Quality Assessment &mdash; Rate 1 (Poor) to 5 (Excellent)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Joinery</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Finish</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>

  <div style="display: flex; align-items: center; gap: 8px; margin-top: 6px; margin-bottom: 6px;">
    <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt;">Overall</span>
    <span class="stars">&#10022; &#10022; &#10022; &#10022; &#10022;</span>
  </div>

  <!-- Notes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Lessons &amp; Notes</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Project #%02d &mdash; Build Record</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, project_num, project_num, project_num, project_num, page_no[0])


def project_overview(page_of, total_pages):
    pg = pn()
    return """<!-- PAGE %d: Project Overview -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Project Overview</span>
    <span class="sh-right">Page %d of %d</span>
  </div>

  <div class="page-title">Project Overview</div>
  <div class="page-subtitle">Quick-reference inventory of all builds</div>

  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Project Name</th>
      <th style="width:35px;">Wood</th>
      <th style="width:25px;">Status</th>
      <th style="width:25px;">Rating</th>
      <th style="width:25px;">Cost</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">1</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">2</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">3</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">4</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">5</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">6</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">7</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">8</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">9</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">10</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">11</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">12</td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Status: P=Planned, IP=In Progress, D=Done, G=Gifted/Sold | Rating: 1-5 stars</div>

  <div class="page-footer">
    <span>Woodworking Project Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_of, total_pages, page_no[0])


def lumber_inventory():
    """Lumber and sheet goods stock"""
    pg = pn()
    return """<!-- PAGE %d: Lumber Inventory -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Lumber Stock</span>
    <span class="sh-right">Inventory</span>
  </div>

  <div class="page-title">Lumber &amp; Sheet Goods Inventory</div>
  <div class="page-subtitle">Track your wood supply</div>

  <div class="gear-card">
    <div class="gear-label">Solid Lumber</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr>
        <th style="width:18px;">#</th>
        <th>Species</th>
        <th style="width:35px;">Size</th>
        <th style="width:25px;">Qty</th>
        <th style="width:35px;">Length</th>
        <th>Source / Notes</th>
      </tr>
      <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">1</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">2</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">3</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">4</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">5</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">6</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">7</td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">8</td><td></td><td></td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Sheet Goods (Plywood / MDF)</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr>
        <th style="width:18px;">#</th>
        <th>Type</th>
        <th style="width:30px;">Thickness</th>
        <th style="width:25px;">Qty</th>
        <th>Notes</th>
      </tr>
      <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">1</td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">2</td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">3</td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8B6B3D;">4</td><td></td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Hardware &amp; Supplies</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr>
        <th>Item</th>
        <th style="width:30px;">Qty</th>
        <th>Location / Notes</th>
      </tr>
      <tr><td style="font-weight:700;color:#161616;">Screws</td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Hinges</td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Drawer Slides</td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Knobs/Pulls</td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Finishing Supplies</td><td></td><td></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Woodworking Project Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def tools_inventory():
    """Tools inventory"""
    pg = pn()
    return """<!-- PAGE %d: Tools -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Tool Inventory</span>
    <span class="sh-right">My Workshop</span>
  </div>

  <div class="page-title">Tool Inventory</div>
  <div class="page-subtitle">Track your workshop equipment</div>

  <div class="gear-card">
    <div class="gear-label">Power Tools</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Tool</th><th style="width:45px;">Brand/Model</th><th style="width:25px;">Have?</th><th>Notes</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Table Saw</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Miter Saw</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Band Saw</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Router</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Drill Press</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Planer</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Jointer</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Cordless Drill</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Hand Tools</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Tool</th><th style="width:45px;">Type/Brand</th><th style="width:25px;">Have?</th><th>Notes</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Chisels</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Hand Planes</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Hand Saws</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Marking Tools</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Clamps</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Measuring</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Jigs &amp; Accessories</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Item</th><th style="width:45px;">Type</th><th style="width:25px;">Have?</th><th>Notes</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Dovetail Jig</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Pocket Hole Jig</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Biscuit Joiner</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Dust Collection</td><td></td><td style="text-align:center;"><span class="check-box"></span></td><td></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Woodworking Project Journal</span>
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

  <div class="page-title">Woodworking Year in Review</div>
  <div class="page-subtitle">Reflect on the year and plan the next</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Projects Built</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Wood Species Used</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Total Hours</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Best Projects This Year</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Project Name</th>
      <th style="width:30px;">Wood</th>
      <th style="width:30px;">Rating</th>
      <th>Why It Stands Out</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Skills &amp; Milestones</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Winner</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">Best Joinery Work</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Finish Result</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Most Challenging</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">New Skill Learned</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Lesson</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">Goals for Next Year</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Woodworking Project Journal</span>
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
  <div class="page-subtitle">Jigs, techniques, and shop notes</div>
  %s
  <div class="page-footer">
    <span>Woodworking Project Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, lines, page_no[0])


def sketch_page():
    pg = pn()
    return """<!-- PAGE %d: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Design Sketch Pad</span>
    <span class="sh-right">Plans &amp; Ideas</span>
  </div>
  <div class="page-title">Design Sketch Pad</div>
  <div class="page-subtitle">Draw project plans, joinery details, and design ideas</div>
  <div class="dot-grid" style="width: 100%%; height: 6.5in; border-radius: 4px;"></div>
  <div class="page-footer">
    <span>Woodworking Project Journal</span>
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
    <div style="font-size: 18pt; font-weight: 700; color: #ffffff; margin-bottom: 10px;">Measure Twice, Cut Once</div>
    <div class="accent-bar"></div>
    <div class="subtitle" style="font-size: 10pt; color: #7A9AAA; font-style: italic;">
      Every project in this journal<br>is a step toward mastery.
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
    pages.append(wood_species_reference())         # 4: Wood species
    pages.append(joinery_reference())              # 5: Joinery
    pages.append(finish_reference())               # 6: Finishing
    pages.append(measurements_reference())         # 7: Measurements
    pages.append(safety_reference())               # 8: Safety

    # ---- Section 1: Project Logs ----
    pages.append(divider_section(1, "One", "Project Records", "40 detailed project logs &mdash; your personal build archive"))
    NUM_PROJECTS = 40
    for i in range(1, NUM_PROJECTS + 1):
        pages.append(project_log_left(i))
        pages.append(project_log_right(i))

    # ---- Section 2: Shop Management ----
    pages.append(divider_section(2, "Two", "Shop Management", "Inventory, tools, and supplies"))
    pages.append(project_overview(1, 3))
    pages.append(project_overview(2, 3))
    pages.append(project_overview(3, 3))
    pages.append(lumber_inventory())
    pages.append(tools_inventory())

    # ---- Section 3: Reflection & Notes ----
    pages.append(divider_section(3, "Three", "Reflection &amp; Notes", "Year in review and design ideas"))
    pages.append(favorites_summary())
    pages.append(sketch_page())
    pages.append(sketch_page())
    for _ in range(4):
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
    print("  Reference (how-to, wood species, joinery, finishing, measurements, safety): 6")
    print("  Section dividers: 3")
    print("  Project logs (%d x 2 pages): %d" % (NUM_PROJECTS, NUM_PROJECTS * 2))
    print("  Project overview: 3")
    print("  Lumber inventory: 1")
    print("  Tools inventory: 1")
    print("  Year in review: 1")
    print("  Sketch pages: 2")
    print("  Notes pages: 4")
    print("  Final: 1")
    print("  TOTAL: %d" % total_pages)

    assert total_pages % 2 == 0, "Page count %d is odd — KDP requires even" % total_pages


if __name__ == "__main__":
    main()
