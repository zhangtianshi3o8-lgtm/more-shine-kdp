#!/usr/bin/env python3
"""
Gemstone & Crystal Collection Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Crystal collectors, spiritual/healing practitioners, mineral enthusiasts
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "gemstone_crystal_collection_journal_us_V1.0.html")

BOOK_TITLE = "Gemstone & Crystal Collection Journal"
BOOK_SUBTITLE = "Catalog Every Specimen, Every Property, Every Meaning"

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
/* Amethyst purple: #6B4C8A, #8B6FB5, #A892C4 */
/* Silver/platinum: #B0B0B0, #C8C8C8, #D4D4D4 */
/* Gold accent: #C4A04A */
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
    radial-gradient(ellipse 26px 16px at 80% 15%, #8B6FB5, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #B0B0B0, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #8B6FB5, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #B0B0B0, transparent),
    radial-gradient(ellipse 18px 11px at 90% 40%, #C4A04A, transparent),
    radial-gradient(ellipse 16px 10px at 40% 90%, #8B6FB5, transparent);
}

/* ===== CSS Crystal Illustration ===== */
.cover .crystal-wrap {
  width: 110px; height: 170px;
  position: relative;
  margin: 0 auto 20px;
}

/* Large central crystal (amethyst point) */
.cover .crystal-main {
  width: 36px; height: 90px;
  position: absolute;
  top: 40px; left: 37px;
  background: linear-gradient(160deg,
    rgba(168,146,196,0.18) 0%,
    rgba(139,111,181,0.12) 40%,
    rgba(107,76,138,0.08) 80%,
    rgba(168,146,196,0.10) 100%);
  border: 1px solid rgba(168,146,196,0.30);
  clip-path: polygon(50% 0%, 100% 15%, 85% 100%, 15% 100%, 0% 15%);
}

/* Crystal shine */
.cover .crystal-shine {
  width: 4px; height: 50px;
  position: absolute;
  top: 50px; left: 45px;
  background: linear-gradient(180deg, rgba(250,248,244,0.30), rgba(250,248,244,0.03));
}

/* Small crystal left */
.cover .crystal-left {
  width: 22px; height: 55px;
  position: absolute;
  top: 65px; left: 12px;
  background: linear-gradient(160deg,
    rgba(196,160,74,0.15) 0%,
    rgba(184,115,51,0.08) 100%);
  border: 1px solid rgba(196,160,74,0.25);
  clip-path: polygon(50% 0%, 100% 20%, 80% 100%, 20% 100%, 0% 20%);
}

/* Small crystal right */
.cover .crystal-right {
  width: 20px; height: 48px;
  position: absolute;
  top: 70px; right: 14px;
  background: linear-gradient(160deg,
    rgba(176,176,176,0.15) 0%,
    rgba(150,150,150,0.08) 100%);
  border: 1px solid rgba(176,176,176,0.25);
  clip-path: polygon(50% 0%, 100% 20%, 80% 100%, 20% 100%, 0% 20%);
}

/* Base/shelf */
.cover .crystal-base {
  width: 80px; height: 4px;
  position: absolute;
  top: 130px; left: 15px;
  background: linear-gradient(90deg,
    transparent,
    rgba(196,160,74,0.20),
    transparent);
  border-radius: 50%;
}

/* Sparkle dots */
.cover .sparkle1 {
  width: 4px; height: 4px;
  background: rgba(250,248,244,0.4);
  border-radius: 50%;
  position: absolute;
  top: 20px; left: 25px;
  box-shadow: 0 0 4px rgba(250,248,244,0.3);
}
.cover .sparkle2 {
  width: 3px; height: 3px;
  background: rgba(196,160,74,0.5);
  border-radius: 50%;
  position: absolute;
  top: 30px; left: 85px;
  box-shadow: 0 0 3px rgba(196,160,74,0.3);
}
.cover .sparkle3 {
  width: 3px; height: 3px;
  background: rgba(168,146,196,0.5);
  border-radius: 50%;
  position: absolute;
  top: 145px; left: 55px;
  box-shadow: 0 0 3px rgba(168,146,196,0.3);
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 22pt;
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
  color: #A892C4;
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
  color: #B0B0B0;
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
    radial-gradient(ellipse 25px 15px at 80% 30%, #8B6FB5, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #B0B0B0, transparent),
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
  color: #A892C4;
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
  border-bottom: 1.5px solid #6B4C8A;
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
  background: #6B4C8A;
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
  border-left: 3px solid #6B4C8A;
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
  border: 1.5px solid #6B4C8A;
  border-radius: 50%;
  display: inline-block;
}

/* ---- Property Card ---- */
.prop-card {
  border: 1px solid #D8D0E0;
  border-radius: 4px;
  padding: 6px 8px;
  margin-bottom: 5px;
  background: #FCFAF7;
}
.prop-card-label {
  font-size: 7pt;
  font-weight: 700;
  color: #6B4C8A;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 3px;
}
.prop-card-value {
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
  border: 1px solid #D8D0E0;
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
  color: #6B4C8A;
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

/* ---- Chakra Color Strip ---- */
.chakra-strip {
  display: flex;
  height: 16px;
  border-radius: 3px;
  overflow: hidden;
  margin-bottom: 4px;
}
.chakra-cell {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 5.5pt;
  font-weight: 700;
  color: white;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
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
  <div class="crystal-wrap">
    <div class="sparkle1"></div>
    <div class="sparkle2"></div>
    <div class="sparkle3"></div>
    <div class="crystal-left"></div>
    <div class="crystal-main"></div>
    <div class="crystal-shine"></div>
    <div class="crystal-right"></div>
    <div class="crystal-base"></div>
  </div>
  <div class="title-block">
    <div class="main-title">%s</div>
    <div class="accent-bar"></div>
    <div class="subtitle">%s</div>
    <div class="features">
      <span class="feature-badge">40 Specimen Logs</span>
      <span class="feature-badge">Mohs Hardness</span>
      <span class="feature-badge">Chakra Guide</span>
      <span class="feature-badge">Care &amp; Cleansing</span>
    </div>
    <div class="tagline">For Collectors, Healers &amp; Crystal Enthusiasts</div>
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
      <div style="font-size: 8pt; font-weight: 700; color: #6B4C8A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Crystal</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #6B4C8A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Collection Started</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #6B4C8A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Collection Size</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #6B4C8A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Primary Interest</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
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
  <div class="page-subtitle">Build your personal crystal encyclopedia</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Crystal Journal?</div>
    A journal transforms a random collection into a curated reference. By recording where you found each specimen, its physical and metaphysical properties, and your personal experiences, you build a database that grows more valuable with every entry. Your journal becomes your own crystal grimoire.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Tips for Better Collecting</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Document on arrival.</strong> When you acquire a new specimen, log it immediately while details are fresh. Record where you got it, how much you paid, and your first impressions. Provenance adds value and meaning.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Photograph your collection.</strong> A quick photo alongside each entry creates a visual record for insurance, reference, and sharing. Natural daylight shows true colors best.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Trust your experience.</strong> Reference books describe general properties, but your personal connection matters most. Note how each stone feels in your hand, what thoughts or sensations arise, and how you use it.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Cleanse and charge regularly.</strong> Crystals absorb energy. Record when and how you cleanse them (moonlight, sunlight, sound, smoke, earth) and notice if their energy shifts afterward.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Handle with knowledge.</strong> Some crystals are fragile, water-soluble, or light-sensitive. Understanding each specimen's physical properties ensures your collection lasts for generations.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #F5F0E8; border: 1px solid #D8D0E0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #5A4A6A;">A Note on Metaphysical Properties:</strong> The information in this journal is for personal reference and entertainment. Crystal healing is a complementary practice and not a substitute for professional medical advice, diagnosis, or treatment.
  </div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def mohs_hardness_reference():
    pg = pn()
    return """<!-- PAGE %d: Mohs Hardness -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Mohs Hardness Scale</span>
  </div>

  <div class="page-title">Mohs Hardness Scale</div>
  <div class="page-subtitle">The 10-point mineral scratch resistance scale</div>

  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Hardness</th>
      <th>Reference Mineral</th>
      <th>Common Gems</th>
      <th>Notes</th>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #6B4C8A; text-align: center;">1</td>
      <td style="font-weight: 700;">Talc</td>
      <td>Soapstone</td>
      <td>Very soft, scratches with fingernail</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #6B4C8A; text-align: center;">2</td>
      <td style="font-weight: 700;">Gypsum</td>
      <td>Selenite, Satin Spar</td>
      <td>Scratches with fingernail</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #6B4C8A; text-align: center;">3</td>
      <td style="font-weight: 700;">Calcite</td>
      <td>Calcite, Limestone, Marble</td>
      <td>Scratches with copper coin</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #6B4C8A; text-align: center;">4</td>
      <td style="font-weight: 700;">Fluorite</td>
      <td>Fluorite</td>
      <td>Scratches with steel knife</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #6B4C8A; text-align: center;">5</td>
      <td style="font-weight: 700;">Apatite</td>
      <td>Apatite</td>
      <td>Scratches with knife with difficulty</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #6B4C8A; text-align: center;">6</td>
      <td style="font-weight: 700;">Orthoclase</td>
      <td>Moonstone, Sunstone, Amazonite</td>
      <td>Scratches glass</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #6B4C8A; text-align: center;">7</td>
      <td style="font-weight: 700;">Quartz</td>
      <td>Amethyst, Citrine, Clear Quartz, Rose Quartz, Smoky Quartz, Agate, Jasper, Tiger's Eye</td>
      <td>Scratches steel easily</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #6B4C8A; text-align: center;">8</td>
      <td style="font-weight: 700;">Topaz</td>
      <td>Topaz, Spinel</td>
      <td>Very hard, scratches quartz</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #6B4C8A; text-align: center;">9</td>
      <td style="font-weight: 700;">Corundum</td>
      <td>Ruby, Sapphire</td>
      <td>Extremely hard, scratches topaz</td>
    </tr>
    <tr>
      <td style="font-weight: 700; color: #6B4C8A; text-align: center;">10</td>
      <td style="font-weight: 700;">Diamond</td>
      <td>Diamond</td>
      <td>Hardest natural mineral</td>
    </tr>
  </table>

  <div style="margin-top: 10px; padding: 8px 10px; background: #FAF8F4; border-left: 3px solid #6B4C8A; border-radius: 0 4px 4px 0; font-size: 8pt; color: #555; line-height: 1.5;">
    <strong style="color: #161616; text-transform: uppercase; font-size: 8pt; letter-spacing: 0.3pt;">Care Implications:</strong><br>
    Stones below 5 on the Mohs scale should not be cleaned in water for long periods or tumbled with harder stones. Stones rated 7+ are generally durable for daily wear and water cleansing. Opal (5.5-6.5) is fragile and can crack if exposed to sudden temperature changes.
  </div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def crystal_systems_reference():
    pg = pn()
    systems = [
        ("Cubic (Isometric)",
         "Equal-length axes at 90&deg;. Symmetrical, often cube or octahedron. Examples: Diamond, Pyrite, Fluorite, Garnet, Galena, Halite, Magnetite, Pyrite."),
        ("Hexagonal",
         "Three equal axes at 120&deg;, one vertical axis. Six-sided prisms. Examples: Apatite, Beryl (Aquamarine, Emerald), Benitoite."),
        ("Trigonal (Rhombohedral)",
         "Modified hexagonal &mdash; threefold symmetry. Triangular cross-sections. Examples: All Quartz varieties, Calcite, Tourmaline, Corundum (Ruby/Sapphire), Hematite."),
        ("Tetragonal",
         "Two equal horizontal axes, one different vertical, all at 90&deg;. Rectangular prisms. Examples: Zircon, Rutile, Vesuvianite, Scapolite."),
        ("Orthorhombic",
         "Three unequal axes at 90&deg;. Rhombic prisms. Examples: Olivine (Peridot), Topaz, Tanzanite, Iolite, Celestite, Danburite, Aragonite."),
        ("Monoclinic",
         "Three unequal axes, two at 90&deg;, one oblique. Examples: Gypsum (Selenite), Orthoclase (Moonstone), Jadeite, Spodumene (Kunzite), Azurite, Malachite."),
        ("Triclinic",
         "Three unequal axes, none at right angles. Least symmetrical. Examples: Plagioclase Feldspar (Labradorite, Sunstone), Kyanite, Turquoise, Rhodonite, Amazonite."),
    ]

    rows = ""
    for sys_name, desc in systems:
        rows += """
      <div class="prop-card">
        <div class="prop-card-label">%s</div>
        <div class="prop-card-value">%s</div>
      </div>""" % (sys_name, desc)

    return """<!-- PAGE %d: Crystal Systems -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Crystal Systems</span>
  </div>

  <div class="page-title">Crystal Systems</div>
  <div class="page-subtitle">The seven geometric patterns of mineral formation</div>

  %s

  <div style="margin-top: 8px; padding: 6px 8px; background: #FAF8F4; border-radius: 3px; font-size: 7pt; color: #888; font-style: italic;">
    Crystal system describes the internal atomic arrangement that determines a mineral's outward shape. The same mineral always forms in the same system &mdash; quartz is always trigonal, no matter where it is found.
  </div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, rows, page_no[0])


def chakra_reference():
    pg = pn()
    return """<!-- PAGE %d: Chakra Reference -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Chakra Color Guide</span>
  </div>

  <div class="page-title">Chakras &amp; Crystal Colors</div>
  <div class="page-subtitle">Match stones to energy centers by color</div>

  <div class="chakra-strip">
    <div class="chakra-cell" style="background: #8B0000;">Root</div>
    <div class="chakra-cell" style="background: #D35400;">Sacral</div>
    <div class="chakra-cell" style="background: #D4AC0D;">Solar</div>
    <div class="chakra-cell" style="background: #229954;">Heart</div>
    <div class="chakra-cell" style="background: #5DADE2;">Throat</div>
    <div class="chakra-cell" style="background: #5B2C83;">Third Eye</div>
    <div class="chakra-cell" style="background: #9B59B6;">Crown</div>
  </div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th>Chakra</th>
      <th>Color</th>
      <th>Location</th>
      <th>Representative Stones</th>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Root</td>
      <td>Red / Black</td>
      <td>Base of spine</td>
      <td>Garnet, Red Jasper, Black Tourmaline, Hematite, Obsidian, Smoky Quartz</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Sacral</td>
      <td>Orange</td>
      <td>Lower abdomen</td>
      <td>Carnelian, Orange Calcite, Sunstone, Peach Moonstone, Tiger's Eye</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Solar Plexus</td>
      <td>Yellow / Gold</td>
      <td>Upper abdomen</td>
      <td>Citrine, Yellow Jasper, Pyrite, Tiger's Eye, Amber, Golden Topaz</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Heart</td>
      <td>Green / Pink</td>
      <td>Center of chest</td>
      <td>Rose Quartz, Green Aventurine, Jade, Emerald, Malachite, Rhodonite, Unakite</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Throat</td>
      <td>Blue</td>
      <td>Throat</td>
      <td>Sodalite, Lapis Lazuli, Aquamarine, Blue Lace Agate, Turquoise, Angelite</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Third Eye</td>
      <td>Indigo / Purple</td>
      <td>Forehead</td>
      <td>Amethyst, Fluorite, Iolite, Lepidolite, Sugilite, Purple Sapphire</td>
    </tr>
    <tr>
      <td style="font-weight:700;color:#161616;">Crown</td>
      <td>Violet / White</td>
      <td>Top of head</td>
      <td>Clear Quartz, Selenite, Howlite, Moonstone, Diamond, Ametrine</td>
    </tr>
  </table>

  <div style="margin-top: 10px; padding: 6px 10px; background: #FFF8E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 7.5pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Color matching</strong> is a simple starting point: stones of the corresponding color tend to resonate with that chakra. Some stones work with multiple chakras (e.g., Clear Quartz amplifies all). Trust your intuition when selecting stones.
  </div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def cleansing_reference():
    pg = pn()
    methods = [
        ("Moonlight",
         "Place crystals outside or on a windowsill overnight, especially during a full moon. Gentle and safe for all stones. Best done monthly."),
        ("Sunlight",
         "Brief sun exposure energizes and cleanses. Caution: some stones fade in sunlight (Amethyst, Citrine, Rose Quartz, Fluorite, Aquamarine, Kunzite). Limit to 1-2 hours."),
        ("Running Water",
         "Hold under cool running water for 1-2 minutes to wash away accumulated energy. Safe for stones rated 6+ on Mohs scale. Never use water with Selenite, Halite, Calcite, or Angelite &mdash; they will dissolve."),
        ("Sound",
         "Use singing bowls, bells, tuning forks, or chanting. Sound vibrations clear energy without physical contact. Excellent for fragile or water-sensitive stones."),
        ("Smoke (Smudging)",
         "Pass crystals through the smoke of sage, palo santo, cedar, or sweetgrass. Traditional and effective. Ensure good ventilation."),
        ("Earth Burial",
         "Bury crystals in soil for 24 hours to a week to ground and reset their energy. Mark the spot clearly. Deeply cleansing but requires patience."),
        ("Salt",
         "Place crystals on or near a bed of dry sea salt or Himalayan salt. Salt absorbs negative energy. Do not let soft or porous stones (under Mohs 5) directly touch salt."),
        ("Other Crystals",
         "Clear Quartz, Selenite, and Carnelian are self-cleansing and can cleanse other stones. Place smaller stones on a Clear Quartz cluster or Selenite plate overnight."),
    ]

    rows = ""
    for method, desc in methods:
        rows += """
      <div style="border: 1px solid #D8D0E0; border-radius: 3px; padding: 7px 9px; margin-bottom: 6px; background: #FCFAF7;">
        <div style="font-size: 9.5pt; font-weight: 700; color: #161616; margin-bottom: 3px;">%s</div>
        <div style="font-size: 8pt; color: #555; line-height: 1.5;">%s</div>
      </div>""" % (method, desc)

    return """<!-- PAGE %d: Cleansing & Charging -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Cleansing &amp; Charging</span>
  </div>

  <div class="page-title">Cleansing &amp; Charging Methods</div>
  <div class="page-subtitle">Keep your crystals energetically clear</div>

  %s

  <div style="margin-top: 8px; padding: 6px 10px; background: #FFF8E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 7.5pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Remember:</strong> Cleanse new crystals before first use, after heavy use or emotional work, and at least monthly. Charging (adding positive energy) follows cleansing &mdash; sunlight, moonlight, or intention are common charging methods.
  </div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, rows, page_no[0])


def safety_reference():
    pg = pn()
    terms = [
        ("Water-Soluble Stones",
         "Never soak or rinse with water: Selenite, Halite (rock salt), Calcite, Angelite, Malachite, Turquoise, Pyrite (can rust), Lepidolite. These dissolve, tarnish, or degrade with water exposure."),
        ("Sunlight-Fading Stones",
         "Keep out of direct prolonged sunlight to prevent color loss: Amethyst, Citrine, Rose Quartz, Smoky Quartz, Fluorite, Aquamarine, Kunzite, Hiddenite, Topaz (some)."),
        ("Toxic Minerals (Do Not Make Elixirs)",
         "Never put in drinking water or handle with bare hands then eat: Malachite, Pyrite, Galena, Cinnabar, Realgar, Orpiment, Stibnite, Chrysocolla, Amazonite (may contain copper), Copper minerals generally. If making gem elixirs, use the indirect method (stone in a separate glass inside the water)."),
        ("Fragile / Heat-Sensitive",
         "Opal can crack with temperature changes. Amber and Jet melt with heat. Kyanite has perfect cleavage and splits easily. Selenite scratches easily (Mohs 2). Handle with care."),
        ("Soft Stones (Under Mohs 5)",
         "Scratch easily and should not be stored with harder stones. Keep separately wrapped: Selenite (2), Gypsum (2), Calcite (3), Fluorite (4). Use soft pouches or individual compartments."),
        ("Dust &amp; Storage",
         "Dust can scratch soft stones over time. Store in closed cabinets, display cases, or cloth-lined boxes. Keep silica gel packets nearby in humid climates to prevent damage to moisture-sensitive stones."),
    ]

    rows = ""
    for term, desc in terms:
        rows += """
      <div style="border: 1px solid #D8D0E0; border-radius: 3px; padding: 7px 9px; margin-bottom: 6px; background: #FCFAF7;">
        <div style="font-size: 9.5pt; font-weight: 700; color: #161616; margin-bottom: 3px;">%s</div>
        <div style="font-size: 8pt; color: #555; line-height: 1.5;">%s</div>
      </div>""" % (term, desc)

    return """<!-- PAGE %d: Safety -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Safety &amp; Care</span>
  </div>

  <div class="page-title">Safety &amp; Care Guidelines</div>
  <div class="page-subtitle">Protect your collection and yourself</div>

  %s

  <div style="margin-top: 8px; padding: 6px 10px; background: #FFF0F0; border: 1px solid #E8C0C0; border-radius: 3px; font-size: 7.5pt; color: #888; font-style: italic;">
    <strong style="color: #8B3333;">Important:</strong> Crystal healing properties described in this journal are for personal reference and entertainment only. They are not a substitute for professional medical advice, diagnosis, or treatment. Always research a mineral's safety before any use beyond display.
  </div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
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


def specimen_log_left(specimen_num):
    """Left page: identification and physical properties"""
    pg = pn()
    return """<!-- PAGE %d: Specimen %d Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Specimen #%02d</span>
    <span class="sh-right">Physical Properties</span>
  </div>

  <div class="page-title">Specimen #%02d &mdash; Identity</div>
  <div class="page-subtitle">Catalog, identify, and document</div>

  <!-- Basic Info -->
  <div style="background: #FAF8F4; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">ID/Cat #</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Stone Name</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Variety/Form</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Acquisition -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Acquisition Record</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 8px;">
    <div style="background: #F5F0E8; padding: 4px 6px; border-radius: 3px;">
      <div style="font-size: 6.5pt; color: #888; text-transform: uppercase;">Source</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div style="background: #F5F0E8; padding: 4px 6px; border-radius: 3px;">
      <div style="font-size: 6.5pt; color: #888; text-transform: uppercase;">Location</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
    <div style="background: #F5F0E8; padding: 4px 6px; border-radius: 3px;">
      <div style="font-size: 6.5pt; color: #888; text-transform: uppercase;">Price</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 14px;"></div>
    </div>
  </div>

  <!-- Physical Properties Grid -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Physical Properties</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-bottom: 8px;">
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Color(s)</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Crystal System</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Mohs Hardness</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Luster</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Transparency</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Mineral Class</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
  </div>

  <!-- Dimensions -->
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-bottom: 8px;">
    <div class="stat-card">
      <div class="stat-label">Weight (g)</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Size (mm)</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Formation</div>
      <div style="border-bottom: 0.5px solid #aaa; height: 16px;"></div>
    </div>
  </div>

  <!-- Visual Description -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Visual Description</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Specimen #%02d &mdash; Identity</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, specimen_num, specimen_num, specimen_num, specimen_num, page_no[0])


def specimen_log_right(specimen_num):
    """Right page: metaphysical properties, care, and personal notes"""
    pg = pn()
    return """<!-- PAGE %d: Specimen %d Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Specimen #%02d</span>
    <span class="sh-right">Metaphysical &amp; Personal</span>
  </div>

  <div class="page-title">Specimen #%02d &mdash; Properties</div>
  <div class="page-subtitle">Metaphysical attributes, care, and personal experience</div>

  <!-- Chakra & Element -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Chakra &amp; Element Association</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-bottom: 8px;">
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Chakra(s)</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Element</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Zodiac Signs</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
    <div class="prop-card" style="margin-bottom: 3px;">
      <div class="prop-card-label">Planet</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 14px;"></div>
    </div>
  </div>

  <!-- Metaphysical Properties -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Metaphysical Keywords &mdash; Check What Applies</div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Protection</span>
    <span class="check-item"><span class="check-box"></span> Grounding</span>
    <span class="check-item"><span class="check-box"></span> Love</span>
    <span class="check-item"><span class="check-box"></span> Calm</span>
    <span class="check-item"><span class="check-box"></span> Clarity</span>
    <span class="check-item"><span class="check-box"></span> Energy</span>
  </div>
  <div class="check-row" style="margin-bottom: 6px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Abundance</span>
    <span class="check-item"><span class="check-box"></span> Healing</span>
    <span class="check-item"><span class="check-box"></span> Intuition</span>
    <span class="check-item"><span class="check-box"></span> Creativity</span>
    <span class="check-item"><span class="check-box"></span> Communication</span>
    <span class="check-item"><span class="check-box"></span> Spiritual Growth</span>
  </div>

  <!-- Care Method -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Preferred Cleansing Method</div>
  <div class="check-row" style="margin-bottom: 8px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Moonlight</span>
    <span class="check-item"><span class="check-box"></span> Sunlight</span>
    <span class="check-item"><span class="check-box"></span> Water</span>
    <span class="check-item"><span class="check-box"></span> Sound</span>
    <span class="check-item"><span class="check-box"></span> Smoke</span>
    <span class="check-item"><span class="check-box"></span> Earth</span>
    <span class="check-item"><span class="check-box"></span> Salt</span>
    <span class="check-item"><span class="check-box"></span> Selenite/Quartz</span>
  </div>

  <!-- Energy Ratings -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Energy Ratings &mdash; Fill in Circles (1 = Subtle, 5 = Powerful)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Vibration</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Resonance</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>

  <!-- Overall Rating -->
  <div style="display: flex; align-items: center; gap: 8px; margin-top: 6px; margin-bottom: 6px;">
    <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt;">Overall</span>
    <span class="stars">&#10022; &#10022; &#10022; &#10022; &#10022;</span>
  </div>

  <div class="check-row" style="margin-bottom: 6px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Favorite</span>
    <span class="check-item"><span class="check-box"></span> Daily Carry</span>
    <span class="check-item"><span class="check-box"></span> Meditation</span>
    <span class="check-item"><span class="check-box"></span> Display</span>
    <span class="check-item"><span class="check-box"></span> Grid Work</span>
  </div>

  <!-- Personal Notes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Personal Experience &amp; Notes</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Specimen #%02d &mdash; Properties</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, specimen_num, specimen_num, specimen_num, specimen_num, page_no[0])


def collection_overview(page_of, total_pages):
    """Quick-reference collection inventory"""
    pg = pn()
    return """<!-- PAGE %d: Collection Overview -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Collection Overview</span>
    <span class="sh-right">Page %d of %d</span>
  </div>

  <div class="page-title">Collection Overview</div>
  <div class="page-subtitle">Quick-reference inventory of all specimens</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Stone Name</th>
      <th style="width:45px;">Variety</th>
      <th style="width:28px;">Hard.</th>
      <th style="width:40px;">Chakra</th>
      <th style="width:30px;">Rating</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">1</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">2</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">3</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">4</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">5</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">6</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">7</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">8</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">9</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">10</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">11</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">12</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Hard.: Mohs hardness | Chakra: Root/Sacral/Solar/Heart/Throat/Third Eye/Crown | Rating: 1-5 stars</div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_of, total_pages, page_no[0])


def suppliers_log(page_of, total_pages):
    """Sources and dealers directory"""
    pg = pn()
    return """<!-- PAGE %d: Suppliers -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Sources &amp; Dealers</span>
    <span class="sh-right">Page %d of %d</span>
  </div>

  <div class="page-title">Sources &amp; Dealers</div>
  <div class="page-subtitle">Where to find quality specimens</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Name</th>
      <th style="width:60px;">Specialty</th>
      <th style="width:45px;">Quality</th>
      <th>Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">6</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">7</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">8</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">9</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">10</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">11</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">12</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Go-To Source</div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #6B4C8A; text-transform: uppercase; min-width: 38px;">Name</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #6B4C8A; text-transform: uppercase; min-width: 38px;">Why I Trust Them</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #6B4C8A; text-transform: uppercase; min-width: 38px;">Usual Finds</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_of, total_pages, page_no[0])


def display_storage():
    """Display and storage system"""
    pg = pn()
    return """<!-- PAGE %d: Display & Storage -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Display &amp; Storage</span>
    <span class="sh-right">My Collection System</span>
  </div>

  <div class="page-title">Display &amp; Storage</div>
  <div class="page-subtitle">Organize and protect your collection</div>

  <div class="gear-card">
    <div class="gear-label">Display Areas</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Location</th><th>Type / Setup</th><th>Lighting</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Storage Solutions</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Size / Details</th><th>Used For</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Cleansing Tools</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Tool</th><th>Type / Details</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Categorization System</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Method</th><th>Details</th></tr>
      <tr><td style="font-weight:700;color:#161616;">By Color?</td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">By Chakra?</td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">By Mineral Family?</td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">By Size?</td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Other System?</td><td></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def crystal_grids():
    """Crystal grid and layout records"""
    pg = pn()
    return """<!-- PAGE %d: Crystal Grids -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Crystal Grids</span>
    <span class="sh-right">Layout Records</span>
  </div>

  <div class="page-title">Crystal Grid Records</div>
  <div class="page-subtitle">Document your sacred geometry layouts</div>

  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 40px;">Grid Name</span>
    <div style="flex:1; border-bottom: 1px solid #161616; height: 18px;"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 8px;">
    <div style="background: #FAF8F4; padding: 6px 8px; border-radius: 4px;">
      <div style="font-size: 7pt; font-weight: 700; color: #6B4C8A; text-transform: uppercase; margin-bottom: 2px;">Date Created</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="background: #FAF8F4; padding: 6px 8px; border-radius: 4px;">
      <div style="font-size: 7pt; font-weight: 700; color: #6B4C8A; text-transform: uppercase; margin-bottom: 2px;">Sacred Geometry</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Intention / Purpose</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Stones Used &mdash; Record Each Stone and Its Position</div>
  <table class="data-table" style="font-size: 7pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Stone Name</th>
      <th style="width:70px;">Position/Role</th>
      <th>Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">1</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">2</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">3</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">4</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">5</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">6</td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">7</td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Layout Sketch</div>
  <div class="dot-grid" style="width: 100%%; height: 1.8in; border-radius: 4px;"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 6px; margin-bottom: 4px;">Experience &amp; Results</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def meditation_log():
    """Crystal meditation and work session log"""
    pg = pn()
    return """<!-- PAGE %d: Meditation Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Meditation Log</span>
    <span class="sh-right">Crystal Work Sessions</span>
  </div>

  <div class="page-title">Meditation &amp; Crystal Work</div>
  <div class="page-subtitle">Track your practice and experiences</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th style="width:35px;">Date</th>
      <th>Stones Used</th>
      <th style="width:50px;">Intention</th>
      <th>Experience / Observations</th>
      <th style="width:30px;">Rating</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">1</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">2</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">3</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">4</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">5</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">6</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">7</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#6B4C8A;">8</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="margin-top: 10px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Monthly Reflection</div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
  </div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, page_no[0])


def favorites_summary():
    """Year-in-review favorites page"""
    pg = pn()
    return """<!-- PAGE %d: Favorites -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Favorites &amp; Stats</span>
    <span class="sh-right">Your Collection Year in Review</span>
  </div>

  <div class="page-title">Collection Year in Review</div>
  <div class="page-subtitle">Fill in at the end of your collecting journey</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Specimens</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Mineral Families</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Chakras Covered</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Top 5 Specimens</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Stone Name</th>
      <th style="width:45px;">Chakra</th>
      <th style="width:30px;">Rating</th>
      <th>Why It's Special</th>
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
    <tr><td style="font-weight:700;color:#161616;">Most Powerful Energy</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Most Beautiful Specimen</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best for Meditation</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best New Discovery</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Crystal Find (Source)</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">What I Want to Add Next</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
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
  <div class="page-subtitle">Observations, references, and reminders</div>

  %s

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
    <span>%d</span>
  </div>
</div>
""" % (pg, lines, page_no[0])


def sketch_page():
    """Dot grid sketch page"""
    pg = pn()
    return """<!-- PAGE %d: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Sketch Pad</span>
    <span class="sh-right">Drawings &amp; Grids</span>
  </div>

  <div class="page-title">Sketch Pad</div>
  <div class="page-subtitle">Draw specimen sketches, crystal grid layouts, display plans</div>

  <div class="dot-grid" style="width: 100%%; height: 6.5in; border-radius: 4px;"></div>

  <div class="page-footer">
    <span>Gemstone &amp; Crystal Collection Journal</span>
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
    <div style="font-size: 20pt; font-weight: 700; color: #ffffff; margin-bottom: 10px;">Your Collection Is Your Story</div>
    <div class="accent-bar"></div>
    <div class="subtitle" style="font-size: 10pt; color: #A892C4; font-style: italic;">
      Every specimen you acquire,<br>every sensation you record,<br>weaves the tapestry of your journey.
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
    pages.append(mohs_hardness_reference())        # 4: Mohs hardness scale
    pages.append(crystal_systems_reference())      # 5: Crystal systems
    pages.append(chakra_reference())               # 6: Chakra & color guide
    pages.append(cleansing_reference())            # 7: Cleansing & charging
    pages.append(safety_reference())               # 8: Safety & care

    # ---- Section 1: Specimen Logs ----
    pages.append(divider_section(1, "One", "Specimen Catalog", "40 detailed specimen entries &mdash; your personal crystal database"))
    NUM_SPECIMENS = 40
    for i in range(1, NUM_SPECIMENS + 1):
        pages.append(specimen_log_left(i))         # Left page: identity
        pages.append(specimen_log_right(i))        # Right page: properties

    # ---- Section 2: Collection Management ----
    pages.append(divider_section(2, "Two", "Collection Management", "Inventory, sources, and storage"))
    pages.append(collection_overview(1, 4))
    pages.append(collection_overview(2, 4))
    pages.append(collection_overview(3, 4))
    pages.append(collection_overview(4, 4))
    pages.append(suppliers_log(1, 2))
    pages.append(suppliers_log(2, 2))
    pages.append(display_storage())

    # ---- Section 3: Crystal Work ----
    pages.append(divider_section(3, "Three", "Crystal Work", "Grids, meditation, and spiritual practice"))
    pages.append(crystal_grids())
    pages.append(crystal_grids())
    pages.append(meditation_log())
    pages.append(meditation_log())

    # ---- Section 4: Favorites & Notes ----
    pages.append(divider_section(4, "Four", "Favorites &amp; Notes", "Reflections and observations"))
    pages.append(favorites_summary())
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

    print("\nPage breakdown:")
    print("  Cover: 1")
    print("  Owner page: 1")
    print("  Reference (how-to, Mohs, systems, chakra, cleansing, safety): 6")
    print("  Section dividers: 4")
    print("  Specimen logs (%d x 2 pages): %d" % (NUM_SPECIMENS, NUM_SPECIMENS * 2))
    print("  Collection overview: 4")
    print("  Suppliers log: 2")
    print("  Display & storage: 1")
    print("  Crystal grids: 2")
    print("  Meditation log: 2")
    print("  Favorites summary: 1")
    print("  Sketch page: 1")
    print("  Notes pages: 6")
    print("  Final page: 1")
    print("  TOTAL: %d" % total_pages)

    assert total_pages % 2 == 0, "Page count %d is odd — KDP requires even" % total_pages


if __name__ == "__main__":
    main()
