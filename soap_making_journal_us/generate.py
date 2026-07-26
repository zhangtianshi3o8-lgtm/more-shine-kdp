#!/usr/bin/env python3
"""
Soap Making Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Cold process and hot process soap makers, hobbyist and small-batch artisans
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "soap_making_journal_us_V1.0.html")

BOOK_TITLE = "Soap Making Journal"
BOOK_SUBTITLE = "Track Every Batch, Perfect Every Bar"

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
   Lavender: #8A7AA8, #A08AB8, #6A5A88
   Herbal green: #7A9A6A, #9ABA8A, #5A7A4A
   Honey gold: #C4A04A, #D4B896
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

/* ================ INTERIOR COVER ================ */
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #8A7AA8, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #7A9A6A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #8A7AA8, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #9ABA8A, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #6A5A88, transparent);
}

/* CSS Soap Bar Illustration */
.cover .soap-wrap {
  width: 120px; height: 170px;
  position: relative;
  margin: 0 auto 18px;
}

/* Soap bar */
.cover .soap-base {
  width: 78px; height: 48px;
  position: absolute;
  top: 75px; left: 21px;
  background: linear-gradient(180deg,
    rgba(196,160,74,0.15) 0%,
    rgba(122,154,106,0.10) 100%);
  border: 1px solid rgba(196,160,74,0.30);
  border-radius: 8px;
}

/* Soap top swirl */
.cover .soap-swirl1 {
  width: 60px; height: 3px;
  position: absolute;
  top: 85px; left: 30px;
  background: rgba(138,122,168,0.20);
  border-radius: 50%;
  transform: rotate(-8deg);
}
.cover .soap-swirl2 {
  width: 56px; height: 3px;
  position: absolute;
  top: 92px; left: 32px;
  background: rgba(122,154,106,0.18);
  border-radius: 50%;
  transform: rotate(5deg);
}
.cover .soap-swirl3 {
  width: 52px; height: 2px;
  position: absolute;
  top: 99px; left: 34px;
  background: rgba(196,160,74,0.15);
  border-radius: 50%;
  transform: rotate(-3deg);
}

/* Soap bubbles */
.cover .bubble1 {
  width: 14px; height: 14px;
  position: absolute;
  top: 25px; left: 30px;
  border-radius: 50%;
  background: rgba(138,122,168,0.12);
  border: 1px solid rgba(138,122,168,0.25);
}
.cover .bubble2 {
  width: 10px; height: 10px;
  position: absolute;
  top: 35px; left: 65px;
  border-radius: 50%;
  background: rgba(122,154,106,0.12);
  border: 1px solid rgba(122,154,106,0.22);
}
.cover .bubble3 {
  width: 8px; height: 8px;
  position: absolute;
  top: 50px; left: 45px;
  border-radius: 50%;
  background: rgba(196,160,74,0.10);
  border: 1px solid rgba(196,160,74,0.20);
}
.cover .bubble4 {
  width: 6px; height: 6px;
  position: absolute;
  top: 20px; left: 75px;
  border-radius: 50%;
  background: rgba(160,138,184,0.15);
  border: 1px solid rgba(138,122,168,0.20);
}
.cover .bubble5 {
  width: 12px; height: 12px;
  position: absolute;
  top: 55px; left: 80px;
  border-radius: 50%;
  background: rgba(154,186,138,0.10);
  border: 1px solid rgba(122,154,106,0.20);
}

/* Lavender sprig */
.cover .sprig {
  width: 4px; height: 35px;
  position: absolute;
  top: 15px; left: 15px;
  background: rgba(122,154,106,0.20);
  border-radius: 1px;
  transform: rotate(5deg);
}
.cover .sprig-leaf1 {
  width: 8px; height: 4px;
  position: absolute;
  top: 22px; left: 10px;
  background: rgba(122,154,106,0.15);
  border-radius: 50%;
  border: 1px solid rgba(122,154,106,0.20);
  transform: rotate(-30deg);
}
.cover .sprig-leaf2 {
  width: 7px; height: 3px;
  position: absolute;
  top: 30px; left: 12px;
  background: rgba(122,154,106,0.12);
  border-radius: 50%;
  border: 1px solid rgba(122,154,106,0.18);
  transform: rotate(-20deg);
}

/* Soap dish */
.cover .dish {
  width: 86px; height: 6px;
  position: absolute;
  top: 128px; left: 17px;
  background: rgba(90,90,90,0.15);
  border-radius: 50%;
  border: 1px solid rgba(196,160,74,0.15);
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
  background: #8A7AA8;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 11pt;
  color: #9ABA8A;
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
  border: 1px solid rgba(138,122,168,0.40);
  color: #8A7AA8;
  font-size: 7pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 9px;
  border-radius: 3px;
  text-transform: uppercase;
}

.cover .tagline {
  font-size: 8.5pt;
  color: #9ABA8A;
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #8A7AA8, transparent),
    radial-gradient(ellipse 25px 15px at 80% 30%, #7A9A6A, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 25% 85%, #8A7AA8, transparent);
}

.divider .div-num {
  font-size: 60pt;
  color: rgba(138,122,168,0.12);
  font-weight: 700;
  position: absolute;
  top: 1in;
}

.divider .div-label {
  font-size: 10pt;
  color: #8A7AA8;
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
  color: #9ABA8A;
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
  border-bottom: 1.5px solid #8A7AA8;
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
  background: #8A7AA8;
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
  border-left: 3px solid #8A7AA8;
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
  border: 1.5px solid #8A7AA8;
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
  color: #8A7AA8;
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
  color: #8A7AA8;
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
  <div class="soap-wrap">
    <div class="sparkle1"></div>
    <div class="sprig"></div>
    <div class="sprig-leaf1"></div>
    <div class="sprig-leaf2"></div>
    <div class="bubble1"></div>
    <div class="bubble2"></div>
    <div class="bubble3"></div>
    <div class="bubble4"></div>
    <div class="bubble5"></div>
    <div class="soap-base"></div>
    <div class="soap-swirl1"></div>
    <div class="soap-swirl2"></div>
    <div class="soap-swirl3"></div>
    <div class="dish"></div>
  </div>
  <div class="title-block">
    <div class="main-title">%s</div>
    <div class="accent-bar"></div>
    <div class="subtitle">%s</div>
    <div class="features">
      <span class="feature-badge">40 Batch Logs</span>
      <span class="feature-badge">SAP Values</span>
      <span class="feature-badge">Oil Guide</span>
      <span class="feature-badge">Safety</span>
    </div>
    <div class="tagline">For Artisan Soap Makers</div>
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
      <div style="font-size: 8pt; font-weight: 700; color: #8A7AA8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Experience Level</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #8A7AA8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Preferred Method</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #8A7AA8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Oils</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #8A7AA8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Signature Scent</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Soap Making Journal</span>
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
  <div class="page-subtitle">Every batch is a learning opportunity</div>

  <div class="info-box">
    <div class="info-title">Why Document Your Soap?</div>
    Soap making is both art and science. A single degree change in temperature, a different oil ratio, or a new fragrance oil can transform your results. Without records, you cannot reproduce your best batches or learn from the ones that failed. This journal turns every batch into accumulated expertise.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Tips for Better Soap Records</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Weigh everything.</strong> Soap making requires precision. Use a digital scale accurate to 0.1 oz or 1 gram. Record actual weights, not just percentages. Volume measurements (cups, spoons) are not accurate enough.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Note temperatures.</strong> Record the temperature of your oils and lye solution at trace. Temperature affects saponification speed, color, and texture. Ideal range is typically 90-110&deg;F for cold process.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Time your trace.</strong> Record how long it took to reach trace and what kind of trace (thin, medium, thick). This reveals how oils, fragrances, and temperatures affect your formula.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Track cure time and results.</strong> Test bars at 2, 4, and 6 weeks. Note hardness, lather quality, scent strength, and skin feel. A soap that seems harsh at 2 weeks may be perfect at 6.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Photograph every batch.</strong> Cut bars and photograph cross-sections. Record a reference photo number in your journal. Colors and patterns are hard to describe in words.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>6. Record failures honestly.</strong> Ricing, seizing, acceleration, DOS (dreaded orange spots), and lye-heavy batches happen to everyone. Documenting the cause prevents repeating mistakes.
    </div>
  </div>

  <div class="page-footer">
    <span>Soap Making Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def oil_properties_reference():
    pg = pn()
    return """<!-- PAGE %d: Oil Properties -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Common Soap Making Oils</span>
  </div>

  <div class="page-title">Oil Properties Guide</div>
  <div class="page-subtitle">How common oils contribute to your soap</div>

  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th>Oil / Fat</th>
      <th style="width:22px;">Hard</th>
      <th style="width:22px;">Cleans</th>
      <th style="width:22px;">Cond.</th>
      <th style="width:22px;">Bubbly</th>
      <th style="width:22px;">Creamy</th>
      <th style="width:35px;">SAP NaOH</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Olive Oil</td>
      <td style="text-align:center;">15</td><td style="text-align:center;">0</td><td style="text-align:center;">82</td><td style="text-align:center;">0</td><td style="text-align:center;">22</td><td style="text-align:center;">.135</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Coconut Oil</td>
      <td style="text-align:center;">68</td><td style="text-align:center;">67</td><td style="text-align:center;">12</td><td style="text-align:center;">46</td><td style="text-align:center;">22</td><td style="text-align:center;">.183</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Palm Oil</td>
      <td style="text-align:center;">58</td><td style="text-align:center;">1</td><td style="text-align:center;">49</td><td style="text-align:center;">1</td><td style="text-align:center;">50</td><td style="text-align:center;">.142</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Palm Kernel</td>
      <td style="text-align:center;">70</td><td style="text-align:center;">63</td><td style="text-align:center;">15</td><td style="text-align:center;">43</td><td style="text-align:center;">29</td><td style="text-align:center;">.176</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Shea Butter</td>
      <td style="text-align:center;">40</td><td style="text-align:center;">0</td><td style="text-align:center;">62</td><td style="text-align:center;">0</td><td style="text-align:center;">40</td><td style="text-align:center;">.133</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Cocoa Butter</td>
      <td style="text-align:center;">50</td><td style="text-align:center;">0</td><td style="text-align:center;">56</td><td style="text-align:center;">0</td><td style="text-align:center;">44</td><td style="text-align:center;">.137</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Castor Oil</td>
      <td style="text-align:center;">2</td><td style="text-align:center;">9</td><td style="text-align:center;">90</td><td style="text-align:center;">64</td><td style="text-align:center;">26</td><td style="text-align:center;">.129</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Sunflower Oil</td>
      <td style="text-align:center;">11</td><td style="text-align:center;">2</td><td style="text-align:center;">63</td><td style="text-align:center;">2</td><td style="text-align:center;">19</td><td style="text-align:center;">.135</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Sweet Almond</td>
      <td style="text-align:center;">12</td><td style="text-align:center;">3</td><td style="text-align:center;">59</td><td style="text-align:center;">3</td><td style="text-align:center;">18</td><td style="text-align:center;">.137</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Avocado Oil</td>
      <td style="text-align:center;">12</td><td style="text-align:center;">3</td><td style="text-align:center;">60</td><td style="text-align:center;">3</td><td style="text-align:center;">18</td><td style="text-align:center;">.134</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Lard</td>
      <td style="text-align:center;">41</td><td style="text-align:center;">0</td><td style="text-align:center;">53</td><td style="text-align:center;">0</td><td style="text-align:center;">47</td><td style="text-align:center;">.141</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Tallow (Beef)</td>
      <td style="text-align:center;">54</td><td style="text-align:center;">9</td><td style="text-align:center;">47</td><td style="text-align:center;">9</td><td style="text-align:center;">45</td><td style="text-align:center;">.144</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Hemp Seed</td>
      <td style="text-align:center;">6</td><td style="text-align:center;">4</td><td style="text-align:center;">50</td><td style="text-align:center;">4</td><td style="text-align:center;">14</td><td style="text-align:center;">.137</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Jojoba (wax)</td>
      <td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">0</td><td style="text-align:center;">.069</td>
    </tr>
  </table>

  <div style="margin-top: 6px; padding: 5px 8px; background: #FAF8F4; border-radius: 3px; font-size: 6.5pt; color: #777; font-style: italic;">
    Values are approximate ranges from typical fatty acid profiles. Hard = bar hardness, Cleans = cleansing power, Cond. = conditioning, Bubbly = fluffy lather, Creamy = stable creamy lather. SAP = mg NaOH per gram of oil. Always verify with a lye calculator before making soap.
  </div>

  <div class="page-footer">
    <span>Soap Making Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def lye_safety_reference():
    pg = pn()
    return """<!-- PAGE %d: Lye Safety -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Lye Safety</span>
  </div>

  <div class="page-title">Lye Safety Guidelines</div>
  <div class="page-subtitle">Essential safety for working with sodium hydroxide</div>

  <div class="info-box">
    <div class="info-title">The Most Important Rule</div>
    Always add lye to water. Never add water to lye. Adding water to lye causes a violent exothermic reaction that can boil, splash, and cause severe chemical burns. Memorize: "Snow falls on the lake."
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Personal Protection</div>
    <div style="margin-bottom: 5px;"><strong>1.</strong> Safety goggles (not glasses) at all times when handling lye. Lye in eyes causes permanent blindness.</div>
    <div style="margin-bottom: 5px;"><strong>2.</strong> Long rubber or nitrile gloves. Lye burns skin on contact.</div>
    <div style="margin-bottom: 5px;"><strong>3.</strong> Long sleeves, pants, and closed-toe shoes. Protect all skin.</div>
    <div style="margin-bottom: 5px;"><strong>4.</strong> Keep vinegar nearby for skin contact (neutralizes alkaline burn). Rinse with water first, then vinegar.</div>
    <div style="margin-bottom: 12px;"><strong>5.</strong> Work in a well-ventilated area. Lye fumes are harmful. Never lean over the lye solution.</div>

    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Equipment</div>
    <div style="margin-bottom: 5px;"><strong>6.</strong> Use only stainless steel, heat-safe glass, or heavy plastic for lye. Never use aluminum (reacts violently) or copper.</div>
    <div style="margin-bottom: 5px;"><strong>7.</strong> Dedicated soap-making equipment only. Do not reuse pots, spoons, or containers for food.</div>
    <div style="margin-bottom: 5px;"><strong>8.</strong> Use an immersion blender dedicated to soap making. Clean all equipment thoroughly after use.</div>
    <div style="margin-bottom: 12px;"><strong>9.</strong> Digital scale accurate to 0.1 oz or 1 gram. Precision is non-negotiable.</div>

    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Mixing Lye Solution</div>
    <div style="margin-bottom: 5px;"><strong>10.</strong> Weigh lye and water separately. Always add lye to water, never reverse.</div>
    <div style="margin-bottom: 5px;"><strong>11.</strong> Stir slowly with a heat-safe spatula. Solution reaches 200&deg;F+ instantly.</div>
    <div style="margin-bottom: 5px;"><strong>12.</strong> Let solution cool to 90-110&deg;F before mixing with oils. Track temperature.</div>
    <div style="margin-bottom: 5px;"><strong>13.</strong> Label and store lye containers clearly. Keep away from children and pets.</div>
    <div><strong>14.</strong> Clean spills immediately with paper towels, then wash with water and vinegar.</div>
  </div>

  <div class="page-footer">
    <span>Soap Making Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def eo_reference():
    pg = pn()
    return """<!-- PAGE %d: Essential Oils -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Essential Oils &amp; Fragrances</span>
  </div>

  <div class="page-title">Fragrance Guide</div>
  <div class="page-subtitle">Scenting your soap safely and effectively</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th>Essential Oil</th>
      <th style="width:50px;">Usage Rate</th>
      <th style="width:30px;">Behav.</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">Lavender</td><td>0.5-1 oz/lb</td><td style="text-align:center;">Stable</td><td>Reliable, versatile. Survives saponification well. Floral-herbal.</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Peppermint</td><td>0.3-0.5 oz/lb</td><td style="text-align:center;">Stable</td><td>Cooling sensation on skin. Strong scent. Use less for face soap.</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Sweet Orange</td><td>0.5-1 oz/lb</td><td style="text-align:center;">Var.</td><td>Citrus oils fade faster. Use 1 oz/lb minimum. Uplifting scent.</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Lemon</td><td>0.5-1 oz/lb</td><td style="text-align:center;">Var.</td><td>Fades in cure. Consider lemon peel powder for lasting scent.</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Tea Tree</td><td>0.3-0.5 oz/lb</td><td style="text-align:center;">Stable</td><td>Antibacterial, medicinal scent. Good for acne-prone skin.</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Eucalyptus</td><td>0.3-0.5 oz/lb</td><td style="text-align:center;">Stable</td><td>Refreshing, decongestant. Strong camphor scent.</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Rosemary</td><td>0.3-0.5 oz/lb</td><td style="text-align:center;">Stable</td><td>Herbal, stimulating. Pairs well with peppermint.</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Cedarwood</td><td>0.5-0.8 oz/lb</td><td style="text-align:center;">Stable</td><td>Earthy, woody. Base note. Very stable in soap.</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Patchouli</td><td>0.5-0.8 oz/lb</td><td style="text-align:center;">Stable</td><td>Deep earthy scent. Fixative — helps hold other scents.</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Litsea Cubeba</td><td>0.5-1 oz/lb</td><td style="text-align:center;">Stable</td><td>"Mountain pepper." Strong lemon scent that lasts longer than lemon EO.</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Clary Sage</td><td>0.3-0.5 oz/lb</td><td style="text-align:center;">Stable</td><td>Herbal-floral. Relaxing. Pairs with lavender.</td></tr>
    <tr><td style="font-weight:700;color:#161616;">Ylang Ylang</td><td>0.3-0.5 oz/lb</td><td style="text-align:center;">Var.</td><td>Exotic floral. Can accelerate trace slightly. Use at light trace.</td></tr>
  </table>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Fragrance Oil Behavior in CP Soap</div>
    <table class="data-table" style="font-size: 7.5pt;">
      <tr><th>Behavior</th><th>What It Means</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Stable</td><td>No effect on trace. Easy to work with. Ideal for beginners.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Accelerates</td><td>Causes trace to thicken quickly. Work fast. Mix at lower temperature.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Rices</td><td>Causes lumpy, grainy texture in batter. Usually from vanilla or floral FOs.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Seizes</td><td>Batter turns solid instantly. Very difficult to save. Test new FOs in small batches.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Discolors</td><td>Turns soap tan, brown, or dark over time. Vanilla content is common cause.</td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Soap Making Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def cure_reference():
    pg = pn()
    return """<!-- PAGE %d: Curing -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Curing &amp; Testing</span>
  </div>

  <div class="page-title">Curing Your Soap</div>
  <div class="page-subtitle">Patience makes perfect bars</div>

  <div class="info-box">
    <div class="info-title">Why Cure?</div>
    Fresh soap contains excess water and the saponification process is not fully complete. Curing allows water to evaporate (making bars harder and longer-lasting) and lets the pH settle. A well-cured bar is milder, harder, and lathers better. Rush this step and you get soft, dissolving, harsh bars.
  </div>

  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th style="width:60px;">Timeline</th>
      <th style="width:55px;">Water Loss</th>
      <th>What to Check</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Week 1</td>
      <td style="text-align:center;">~5-8%%</td>
      <td>Bars are still soft. Keep in mold first 24-48 hrs, then cut. Place on curing racks with airflow.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Week 2</td>
      <td style="text-align:center;">~10-15%%</td>
      <td>Bars firming up. Test for hardness with thumbnail press. Should leave slight indent.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Week 4</td>
      <td style="text-align:center;">~15-20%%</td>
      <td>Bars feel hard. Initial lather test. Scent should be noticeable. pH should test below 10.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Week 6</td>
      <td style="text-align:center;">~20-25%%</td>
      <td>Standard cure complete for most recipes. Good lather, mild feel, lasting bar.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Week 8+</td>
      <td style="text-align:center;">~25-30%%</td>
      <td>Extended cure for high-olive recipes. Even milder, denser lather. Bars last longest.</td>
    </tr>
  </table>

  <div style="margin-top: 12px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Curing Best Practices</div>
    <table class="data-table" style="font-size: 8pt;">
      <tr><th style="width:60px;">Factor</th><th>Ideal</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Airflow</td><td>Open shelving or racks. Fans circulating air. No sealed containers.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Humidity</td><td>Low (under 50%% if possible). Use dehumidifier in damp climates.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Temperature</td><td>Room temperature (65-75&deg;F). Avoid extreme heat or cold.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Spacing</td><td>Bars not touching. At least 0.5 inch between for airflow.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Light</td><td>Avoid direct sunlight (causes fading and DOS). Dark or dim storage.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Turning</td><td>Flip bars every few days for even drying on all sides.</td></tr>
    </table>
  </div>

  <div style="margin-top: 8px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 5px;">Testing Your Soap</div>
    <table class="data-table" style="font-size: 8pt;">
      <tr><th style="width:60px;">Test</th><th>What to Look For</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Zap Test</td><td>Lick the soap. A "zap" or tingle = lye-heavy, not ready. No zap = safe to use.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">pH Strip</td><td>Wet soap surface, press pH strip. Readings 8-10 are normal for soap. Above 11 = uncured.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Lather</td><td>Wash hands. Check for bubbly vs creamy lather, how it rinses, skin feel after.</td></tr>
      <tr><td style="font-weight:700;color:#161616;">Hardness</td><td>Press thumbnail into bar. Hard, slight give = good. Soft, crumbly = keep curing.</td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Soap Making Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def troubleshooting_reference():
    pg = pn()
    return """<!-- PAGE %d: Troubleshooting -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Troubleshooting</span>
  </div>

  <div class="page-title">Common Soap Problems</div>
  <div class="page-subtitle">Identify and fix batch issues</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:80px;">Problem</th>
      <th>Likely Cause</th>
      <th style="width:95px;">Solution</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Seize</td>
      <td>Fragrance oil reacts instantly. Temperature too high. FO not CP-safe.</td>
      <td>Work at lower temp. Test FO in small batch. Switch FO. Use hot process.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Acceleration</td>
      <td>FO/EO speeds trace. Stearic acid, hard butters. Temp too high.</td>
      <td>Lower oil/lye temps. Add FO at very light trace. Work fast.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Ricing</td>
      <td>FO forms rice-like lumps in batter. Common with floral FOs.</td>
      <td>Stick blend vigorously to incorporate. May incorporate or need straining.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">DOS (Orange Spots)</td>
      <td>Oil rancidity. Old oils, high superfat, humidity during cure.</td>
      <td>Use fresh oils. Add ROE or vitamin E. Lower superfat. Cure in low humidity.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Lye Heavy</td>
      <td>Mismeasured lye. Wrong SAP values. Scale error. Insufficient cure.</td>
      <td>Always verify with lye calculator. Zap test before use. Recalculate recipe.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Soda Ash</td>
      <td>Lye reacts with air CO2 on surface. Uncovered during saponification.</td>
      <td>Spray with rubbing alcohol after pour. Cover with plastic wrap. Steam or wash off.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Gel Partial</td>
      <td>Uneven temperature during saponification. Center gels, edges do not.</td>
      <td>Insulate mold fully. Force gel phase (oven process). Or embrace ungelled look.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Cracking</td>
      <td>High lye concentration. Too much coconut oil. Temperature shock.</td>
      <td>Use more water. Reduce coconut oil. Control temperatures.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Color Fade</td>
      <td>UV light exposure. Unstable colorant. High pH destroying pigment.</td>
      <td>Use stable pigments (oxides, micas). Store dark. Avoid plant colorants.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">No Scent</td>
      <td>Insufficient EO/FO. Citrus oils fading. Volatile oils evaporating.</td>
      <td>Increase usage rate. Use stable oils (patchouli, litsea). Seal cure area.</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Soft Bars</td>
      <td>High water. High soft oil ratio. Not fully cured. High superfat.</td>
      <td>Cure longer. Reduce water. Increase hard oils (palm, cocoa butter).</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Glycerin Rivers</td>
      <td>Temperature too high during gel. High glycerin in recipe.</td>
      <td>Lower lye concentration. Reduce gel temp. Prevent overheating.</td>
    </tr>
  </table>

  <div style="margin-top: 8px; padding: 6px 10px; background: #FAF8F4; border-radius: 3px; font-size: 7.5pt; color: #555; font-style: italic;">
    <strong style="color: #8A7AA8;">Pro Tip:</strong> When a batch fails, do not throw it away. Document the problem, let it cure fully, then zap-test. Many "failed" batches become usable after a longer cure. Lye-heavy soap can be rebatched (hot process) or used for laundry.
  </div>

  <div class="page-footer">
    <span>Soap Making Journal</span>
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


def batch_log_left(batch_num):
    """Left page: batch identity, oils, lye, additives"""
    pg = pn()
    return """<!-- PAGE %d: Batch %d Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Batch #%02d</span>
    <span class="sh-right">Recipe &amp; Formula</span>
  </div>

  <div class="page-title">Batch #%02d &mdash; Recipe</div>
  <div class="page-subtitle">Formula, oils, lye, and additives</div>

  <!-- Batch Info -->
  <div style="background: #FAF8F4; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 42px;">Method</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Batch Name</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Superfat</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 42px;">Batch Size</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Oil Recipe -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Oil Recipe</div>
  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Oil / Fat</th>
      <th style="width:30px;">Pct</th>
      <th style="width:35px;">Grams</th>
      <th style="width:35px;">Ounces</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">6</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <!-- Lye & Water -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Lye Solution</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 5px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">NaOH g</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Water g</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Lye Conc.</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Water : Lye</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
  </div>

  <!-- Additives -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Additives &amp; Scent</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-bottom: 6px;">
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Essential Oil / Fragrance</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Amount (g / oz)</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Colorant(s)</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Other Additives</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Batch #%02d &mdash; Recipe</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, batch_num, batch_num, batch_num, batch_num, page_no[0])


def batch_log_right(batch_num):
    """Right page: process log, cure, testing, evaluation"""
    pg = pn()
    return """<!-- PAGE %d: Batch %d Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Batch #%02d</span>
    <span class="sh-right">Process &amp; Results</span>
  </div>

  <div class="page-title">Batch #%02d &mdash; Process Log</div>
  <div class="page-subtitle">Make day, cure tracking, and evaluation</div>

  <!-- Temperatures -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Make Day Conditions</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 5px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">Oil Temp</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Lye Temp</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Ambient</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Time to Trace</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
  </div>

  <!-- Trace type -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Trace Type &mdash; Check All That Apply</div>
  <div class="check-row" style="margin-bottom: 6px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> None</span>
    <span class="check-item"><span class="check-box"></span> Thin</span>
    <span class="check-item"><span class="check-box"></span> Medium</span>
    <span class="check-item"><span class="check-box"></span> Thick</span>
    <span class="check-item"><span class="check-box"></span> Emulsion</span>
    <span class="check-item"><span class="check-box"></span> Seized</span>
  </div>

  <!-- Issues -->
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-bottom: 8px;">
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Mold Used</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Cut Date</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Issues / Problems</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Bars Yielded</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
  </div>

  <!-- Cure Tracking -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Cure Tracking</div>
  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:28px;">Wk</th>
      <th>Test Date</th>
      <th style="width:30px;">Zap?</th>
      <th style="width:30px;">pH</th>
      <th>Hardness / Lather / Scent</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">6</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <!-- Quality ratings -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Final Evaluation &mdash; Rate 1 (Poor) to 5 (Excellent)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Lather</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Scent</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Skin Feel</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>

  <div style="display: flex; align-items: center; gap: 8px; margin-top: 4px; margin-bottom: 4px;">
    <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt;">Overall</span>
    <span class="stars">&#10022; &#10022; &#10022; &#10022; &#10022;</span>
  </div>

  <!-- Notes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 4px; margin-bottom: 3px;">Notes &amp; Changes for Next Time</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Batch #%02d &mdash; Process &amp; Results</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, batch_num, batch_num, batch_num, batch_num, page_no[0])


def recipe_library(page_of, total_pages):
    pg = pn()
    return """<!-- PAGE %d: Recipe Library -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Recipe Library</span>
    <span class="sh-right">Page %d of %d</span>
  </div>

  <div class="page-title">Recipe Library</div>
  <div class="page-subtitle">Quick-reference index of all formulas</div>

  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Recipe Name</th>
      <th style="width:35px;">Method</th>
      <th style="width:25px;">SF%%</th>
      <th style="width:25px;">Rating</th>
      <th style="width:25px;">Repeat?</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">1</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">2</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">3</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">4</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">5</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">6</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">7</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">8</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">9</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">10</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">11</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">12</td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">SF%% = Superfat percentage | Method: CP=Cold Process, HP=Hot Process, M&M=Melt &amp; Pour | Repeat: Y=Yes, N=No, M=Maybe</div>

  <div class="page-footer">
    <span>Soap Making Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_of, total_pages, page_no[0])


def supply_inventory():
    pg = pn()
    return """<!-- PAGE %d: Supply Inventory -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Supply Inventory</span>
    <span class="sh-right">Oils, Lye, Additives</span>
  </div>

  <div class="page-title">Supply Inventory</div>
  <div class="page-subtitle">Track your soap-making supplies</div>

  <div class="gear-card">
    <div class="gear-label">Oils &amp; Butters</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr>
        <th style="width:18px;">#</th>
        <th>Item</th>
        <th style="width:30px;">Qty</th>
        <th style="width:25px;">Unit</th>
        <th>Source / Notes</th>
      </tr>
      <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">1</td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">2</td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">3</td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">4</td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">5</td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">6</td><td></td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Lye &amp; Liquids</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr>
        <th style="width:18px;">#</th>
        <th>Item</th>
        <th style="width:30px;">Qty</th>
        <th style="width:25px;">Unit</th>
        <th>Source / Notes</th>
      </tr>
      <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">1</td><td>NaOH (Lye)</td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">2</td><td>Distilled Water</td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">3</td><td></td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Essential Oils, Fragrance &amp; Colorants</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr>
        <th style="width:18px;">#</th>
        <th>Item</th>
        <th style="width:30px;">Qty</th>
        <th style="width:25px;">Unit</th>
        <th>Source / Notes</th>
      </tr>
      <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">1</td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">2</td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">3</td><td></td><td></td><td></td><td></td></tr>
      <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">4</td><td></td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Soap Making Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def gift_sales_log():
    pg = pn()
    return """<!-- PAGE %d: Gift & Sales Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Gift &amp; Sales Log</span>
    <span class="sh-right">Distribution Record</span>
  </div>

  <div class="page-title">Gift &amp; Sales Log</div>
  <div class="page-subtitle">Track where your soap goes</div>

  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Date</th>
      <th>Recipe / Batch</th>
      <th style="width:25px;">Qty</th>
      <th style="width:40px;">Recipient / Buyer</th>
      <th style="width:30px;">Gift/Sale</th>
      <th style="width:30px;">Price</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">2</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">4</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">5</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">6</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">7</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">8</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">9</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">10</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">11</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#8A7AA8;">12</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div class="page-footer">
    <span>Soap Making Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def year_in_review():
    pg = pn()
    return """<!-- PAGE %d: Year in Review -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Year in Review</span>
    <span class="sh-right">Reflection</span>
  </div>

  <div class="page-title">Soap Making Year in Review</div>
  <div class="page-subtitle">Reflect on your progress and plan ahead</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Batches Made</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Bars Produced</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Best Batch #</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Top Recipes This Year</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Recipe Name</th>
      <th style="width:30px;">Method</th>
      <th style="width:30px;">Rating</th>
      <th>Why It Was Great</th>
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
      <th>Answer</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">Best Lather</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Scent Combo</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Most Challenging</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">New Technique Learned</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Lesson</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">Goals for Next Year</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Soap Making Journal</span>
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
  <div class="page-subtitle">Ideas, recipes, and observations</div>
  %s
  <div class="page-footer">
    <span>Soap Making Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, lines, page_no[0])


def final_page():
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="cover">
  <div class="glow-bg"></div>
  <div class="title-block">
    <div style="font-size: 18pt; font-weight: 700; color: #ffffff; margin-bottom: 10px;">Every Batch Is Progress</div>
    <div class="accent-bar"></div>
    <div class="subtitle" style="font-size: 10pt; color: #9ABA8A; font-style: italic;">
      Your best soap is<br>the next one you make.
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
    pages.append(oil_properties_reference())       # 4: Oil properties
    pages.append(lye_safety_reference())           # 5: Lye safety
    pages.append(eo_reference())                   # 6: Fragrance guide
    pages.append(cure_reference())                 # 7: Curing
    pages.append(troubleshooting_reference())      # 8: Troubleshooting

    # ---- Section 1: Batch Logs ----
    pages.append(divider_section(1, "One", "Batch Records", "40 detailed batch logs &mdash; your personal soap archive"))
    NUM_BATCHES = 40
    for i in range(1, NUM_BATCHES + 1):
        pages.append(batch_log_left(i))
        pages.append(batch_log_right(i))

    # ---- Section 2: Management ----
    pages.append(divider_section(2, "Two", "Management", "Recipes, inventory, and distribution"))
    pages.append(recipe_library(1, 3))
    pages.append(recipe_library(2, 3))
    pages.append(recipe_library(3, 3))
    pages.append(supply_inventory())
    pages.append(gift_sales_log())

    # ---- Section 3: Reflection & Notes ----
    pages.append(divider_section(3, "Three", "Reflection &amp; Notes", "Year in review and ideas"))
    pages.append(year_in_review())
    for _ in range(6):
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
    print("  Reference (how-to, oils, lye safety, fragrance, curing, troubleshooting): 6")
    print("  Section dividers: 3")
    print("  Batch logs (%d x 2 pages): %d" % (NUM_BATCHES, NUM_BATCHES * 2))
    print("  Recipe library: 3")
    print("  Supply inventory: 1")
    print("  Gift/sales log: 1")
    print("  Year in review: 1")
    print("  Notes pages: 5")
    print("  Final: 1")
    print("  TOTAL: %d" % total_pages)

    assert total_pages % 2 == 0, "Page count %d is odd — KDP requires even" % total_pages


if __name__ == "__main__":
    main()
