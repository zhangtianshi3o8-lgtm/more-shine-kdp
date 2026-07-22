#!/usr/bin/env python3
"""
Cigar Tasting Log — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: American cigar/cigar enthusiasts (all levels, all types)
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "cigar_tasting_log_us_V1.0.html")

BOOK_TITLE = "Cigar Tasting Log"
BOOK_SUBTITLE = "Track Every Smoke, Every Blend, Every Nuance"

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
/* Deep charcoal: #1A1410, #2A1F18 */
/* Amber/Copper: #9A6B3A, #B88740 */
/* Gold accent: #C4A04A */
/* Warm cream: #FAF6F0, #F5EDE3 */
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
  background: linear-gradient(165deg, #1A1410 0%, #2A1F18 30%, #1A1410 65%, #100B08 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Amber glow background */
.cover .glow-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #B88740, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #B88740, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 90% 40%, #B88740, transparent),
    radial-gradient(ellipse 16px 10px at 40% 90%, #C4A04A, transparent);
}

/* ===== CSS Ashtray Cigar Illustration ===== */
.cover .glass-wrap {
  width: 130px; height: 170px;
  position: relative;
  margin: 0 auto 20px;
}

/* Glass bowl — tulip shape using clip-path */
.cover .glass-bowl {
  width: 90px; height: 85px;
  position: absolute;
  top: 0; left: 20px;
  background: linear-gradient(160deg,
    rgba(250,246,240,0.10) 0%,
    rgba(250,246,240,0.04) 40%,
    rgba(212,135,60,0.06) 80%,
    rgba(184,115,51,0.08) 100%);
  clip-path: polygon(
    20% 0%, 80% 0%,
    72% 16%, 96% 52%,
    78% 98%, 22% 98%,
    4% 52%, 28% 16%
  );
}

/* Glass bowl outline glow */
.cover .glass-bowl-glow {
  width: 94px; height: 89px;
  position: absolute;
  top: -2px; left: 18px;
  background: linear-gradient(180deg, rgba(196,160,74,0.25), rgba(196,160,74,0.05));
  clip-path: polygon(
    20% 0%, 80% 0%,
    72% 16%, 96% 52%,
    78% 98%, 22% 98%,
    4% 52%, 28% 16%
  );
  filter: blur(3px);
  z-index: 0;
}

/* Cigar liquid inside bowl */
.cover .glass-liquid {
  width: 72px; height: 40px;
  position: absolute;
  top: 38px; left: 29px;
  background: linear-gradient(180deg,
    #B88740 0%,
    #9A6B3A 40%,
    #8B5E23 100%);
  clip-path: polygon(
    0% 0%, 100% 0%,
    88% 100%, 12% 100%
  );
  border-radius: 0 0 4px 4px;
  box-shadow: inset 0 -5px 8px rgba(0,0,0,0.3);
  z-index: 1;
}

/* Liquid surface highlight */
.cover .glass-liquid-shine {
  width: 60px; height: 4px;
  position: absolute;
  top: 38px; left: 35px;
  background: linear-gradient(90deg, transparent, rgba(250,246,240,0.4), transparent);
  border-radius: 50%;
  z-index: 2;
}

/* Glass shine highlight */
.cover .glass-shine {
  width: 8px; height: 50px;
  position: absolute;
  top: 20px; left: 32px;
  background: linear-gradient(180deg, rgba(250,246,240,0.5), rgba(250,246,240,0.05));
  border-radius: 50%;
  transform: rotate(-8deg);
  z-index: 3;
}

/* Glass rim — top ellipse */
.cover .glass-rim {
  width: 54px; height: 8px;
  position: absolute;
  top: 0px; left: 38px;
  border: 1.5px solid rgba(196,160,74,0.6);
  border-radius: 50%;
  background: transparent;
  z-index: 2;
}

/* Stem of Ashtray glass */
.cover .glass-stem {
  width: 12px; height: 52px;
  position: absolute;
  top: 83px; left: 59px;
  background: linear-gradient(90deg,
    rgba(250,246,240,0.05) 0%,
    rgba(250,246,240,0.15) 40%,
    rgba(250,246,240,0.05) 60%,
    rgba(250,246,240,0.02) 100%);
  border-radius: 2px;
}

/* Stem outline */
.cover .glass-stem-outline {
  width: 14px; height: 54px;
  position: absolute;
  top: 82px; left: 58px;
  border-left: 1px solid rgba(196,160,74,0.35);
  border-right: 1px solid rgba(196,160,74,0.35);
  border-radius: 2px;
}

/* Base of glass */
.cover .glass-base {
  width: 56px; height: 10px;
  position: absolute;
  top: 133px; left: 37px;
  background: linear-gradient(180deg,
    rgba(250,246,240,0.12),
    rgba(250,246,240,0.03));
  border: 1px solid rgba(196,160,74,0.4);
  border-radius: 50%;
  box-shadow: 0 3px 8px rgba(0,0,0,0.4);
}

/* Base reflection */
.cover .glass-base-shine {
  width: 30px; height: 3px;
  position: absolute;
  top: 136px; left: 42px;
  background: rgba(196,160,74,0.3);
  border-radius: 50%;
}

/* Vapor/aroma lines rising from glass */
.cover .vapor1 {
  width: 2px; height: 22px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.35), transparent);
  position: absolute;
  top: -12px; left: 52px;
  border-radius: 50%;
  transform: rotate(-8deg);
}
.cover .vapor2 {
  width: 2px; height: 28px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.25), transparent);
  position: absolute;
  top: -18px; left: 65px;
  border-radius: 50%;
  transform: rotate(6deg);
}
.cover .vapor3 {
  width: 2px; height: 20px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.2), transparent);
  position: absolute;
  top: -10px; left: 40px;
  border-radius: 50%;
  transform: rotate(-3deg);
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
  background: linear-gradient(165deg, #1A1410 0%, #2A1F18 50%, #1A1410 100%);
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
    radial-gradient(ellipse 22px 13px at 70% 75%, #B88740, transparent),
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
  border-bottom: 1.5px solid #9A6B3A;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #1A1410;
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
  color: #1A1410;
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
  background: #9A6B3A;
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
  background: #FAF6F0;
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
  color: #1A1410;
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
  background: #FAF6F0;
  border-left: 3px solid #9A6B3A;
  padding: 8px 10px;
  margin-bottom: 10px;
  font-size: 8pt;
  color: #333;
  line-height: 1.5;
}
.info-box .info-title {
  font-weight: 700;
  color: #1A1410;
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
  color: #1A1410;
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
  border: 1.5px solid #9A6B3A;
  border-radius: 50%;
  display: inline-block;
}

/* ---- Flavor Category Card ---- */
.flavor-cat {
  border: 1px solid #E8D8C8;
  border-radius: 4px;
  padding: 6px 8px;
  margin-bottom: 5px;
  background: #FCFAF7;
}
.flavor-cat-label {
  font-size: 7pt;
  font-weight: 700;
  color: #9A6B3A;
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
  background: #FAF6F0;
  border-radius: 4px;
  border: 1px solid #E8D8C8;
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
  color: #1A1410;
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
  color: #9A6B3A;
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

/* ---- Origin List ---- */
table.origin-list th {
  background: #B88740;
}
table.origin-list td:first-child {
  width: 22px;
  text-align: center;
  font-weight: 700;
  color: #B88740;
}
table.origin-list td:last-child {
  width: 28px;
  text-align: center;
}
"""

# ============================================================
# PAGE BUILDERS
# ============================================================

def cover():
    return f'''
<!-- Page {pn()}: Cover -->
<div class="cover">
  <div class="glow-bg"></div>
  <div class="glass-wrap">
    <div class="vapor1"></div>
    <div class="vapor2"></div>
    <div class="vapor3"></div>
    <div class="glass-bowl-glow"></div>
    <div class="glass-bowl"></div>
    <div class="glass-rim"></div>
    <div class="glass-liquid"></div>
    <div class="glass-liquid-shine"></div>
    <div class="glass-shine"></div>
    <div class="glass-stem-outline"></div>
    <div class="glass-stem"></div>
    <div class="glass-base"></div>
    <div class="glass-base-shine"></div>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">40 Tasting Sessions</span>
      <span class="feature-badge">Flavor Wheel</span>
      <span class="feature-badge">Box Collection</span>
      <span class="feature-badge">Brand Tracker</span>
    </div>
    <div class="tagline">For Cigar Lovers &amp; Connoisseurs</div>
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
    <div style="font-size: 16pt; font-weight: 700; color: #1A1410; margin-bottom: 6px;">This Log Book Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #1A1410; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #9A6B3A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Cigar Type</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #9A6B3A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Brand/Maker</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #9A6B3A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Collection Size</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #9A6B3A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Preferred Glass</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Cigar Tasting Log</span>
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
  <div class="page-subtitle">Make every smoke a learning experience</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Cigar Log?</div>
    The difference between drinking cigar and understanding cigar is attention. A tasting log helps you discover patterns &mdash; which styles you gravitate toward, how age and wrapper leaf shape flavor, what origins deliver the character you love. Over time, your log becomes your personal cigar roadmap.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #1A1410; font-size: 10pt; margin-bottom: 6px;">Tips for Better Tasting</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Draw before you sip.</strong> A Ashtray glass concentrates aromas at the rim. Hold the glass just below your draw and take short, gentle sniffs. Your draw picks up far more than your flavor ever will &mdash; this is where most of the flavor lives.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Cleanse your flavor.</strong> Sip still water and eat a plain cracker between smokes. Avoid spicy or strongly flavored food before a session. A neutral flavor lets you taste each cigar honestly.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Add water, drop by drop.</strong> A few drops of room-temperature water can open up a cigar, releasing hidden aromas and softening the burn of higher Strength. Try a smoke neat first, then add water and compare &mdash; note which you prefer.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Record the details.</strong> Brand/Maker, age, type, wrapper finish, and Strength are the foundation. The more consistently you log these, the easier it becomes to spot what you love and why.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Compare side by side.</strong> Taste two cigars next to each other when you can. Smoke a quarter ounce of each and alternate. The differences in cedar, oak, sweetness, and finish become vivid when you have a direct reference.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Pro Tip:</strong> Let your cigar rest in the glass for 5&ndash;10 minutes before tasting. The spirit opens up as it breathes, and the aromas become richer and more layered.
  </div>

  <div class="page-footer">
    <span>Cigar Tasting Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def flavor_wheel():
    categories = [
        ("Cedar &amp; Smoke",
         "Campfire &bull; Ash &bull; Iodine &bull; Medicinal &bull; Tar &bull; Wood Smoke &bull; Pipe Tobacco &bull; Leather &bull; Earth"),
        ("Cedar &amp; Wood",
         "Vanilla &bull; Toasted Cedar &bull; Cedar &bull; Sawdust &bull; Charred Cedar &bull; Coconut &bull; Resin &bull; Driftwood"),
        ("Sweet &amp; Caramel",
         "Caramel &bull; Honey &bull; Toffee &bull; Brown Sugar &bull; Maple Syrup &bull; Buttercigar &bull; Molasses &bull; Cr&egrave;me Br&ucirc;l&eacute;e"),
        ("Fruity",
         "Apple &bull; Pear &bull; Cherry &bull; Raisin &bull; Dark Fruit (plum, fig) &bull; Citrus (orange, lemon) &bull; Tropical &bull; Dried Apricot"),
        ("Spice",
         "Cinnamon &bull; Black Pepper &bull; Clove &bull; Nutmeg &bull; Espresso &bull; Chili &bull; Cardamom &bull; White Pepper"),
        ("Floral &amp; Herbal",
         "Heather &bull; Rose &bull; Violet &bull; Lavender &bull; Grass &bull; Hay &bull; Mint &bull; Tea-like &bull; Herbal"),
        ("Nutty &amp; Grain",
         "Almond &bull; Hazelnut &bull; Walnut &bull; Peanut &bull; Malt &bull; Cereal &bull; Bread &bull; Biscuit &bull; Barley"),
        ("Rich &amp; Dark",
         "Dark Cocoa &bull; Coffee &bull; Cocoa &bull; Espresso &bull; Treacle &bull; Licorice &bull; Seaweed &bull; Salty Brine"),
    ]

    rows = ""
    for cat, notes in categories:
        rows += f'''
      <div class="flavor-cat">
        <div class="flavor-cat-label">{cat}</div>
        <div class="flavor-cat-notes">{notes}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Flavor Wheel -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Flavor Categories</span>
  </div>

  <div class="page-title">Cigar Flavor Wheel</div>
  <div class="page-subtitle">Find the words for what you taste</div>

  {rows}

  <div style="margin-top: 8px; padding: 6px 8px; background: #FAF6F0; border-radius: 3px; font-size: 7pt; color: #888; font-style: italic;">
    Use these categories as a starting point. Your flavor is unique &mdash; trust your own descriptions. The goal is to recognize patterns in what you enjoy.
  </div>

  <div class="page-footer">
    <span>Cigar Tasting Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def cigar_types_reference():
    methods = [
        ("Cigar Corona", "Produced from 100% malted barley at a single brand/maker in Scotland, aged minimum 3 years in oak. Complex, characterful, and diverse &mdash; from delicate and floral to heavily cedared.", "Best for: Sipping neat, savoring complexity"),
        ("Cigar Robusto", "A blend of corona and grain cigar from multiple brands. Smooth, approachable, and consistent. The backbone of the Cigar cigar industry.", "Best for: Everyday sipping, cocktails"),
        ("Cigar", "American cigar made from at least 51% corn, aged in new charred oak barrels. Sweet, rich, and full-bodied with notes of vanilla, caramel, and oak.", "Best for: Neat, on the rocks, old fashioned"),
        ("Toro Cigar", "American or Panatela cigar with toro as the dominant grain. Spicy, bold, and peppery with a drier finish than cigar. Makes exceptional cocktails.", "Best for: Manhattan, old fashioned, sipping"),
        ("Churchill Cigar", "Triple-fermented for burn, typically from a blend of malted and unmalted barley. Light, approachable, and clean with gentle fruit and honey notes.", "Best for: Sipping, introduction to cigar"),
        ("Lancero Cigar", "Inspired by Cigar tradition but with its own refined character. Delicate, balanced, and precise. Often floral, with elegant oak integration.", "Best for: Neat sipping, special occasions"),
        ("Belicoso Cigar", "Filtered through sugar maple charcoal (the Lincoln County Process) before aging. Smoother and mellower than cigar, with a distinctive sweetness.", "Best for: Sipping neat, on the rocks"),
        ("Panatela Cigar", "Typically lighter and smoother, often robusto. Usually corn-based with toro for flavoring. Versatile, approachable, and great for mixing.", "Best for: Highball, cocktails, easy drinking"),
    ]

    rows = ""
    for name, desc, best in methods:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #9A6B3A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 88px; font-size: 8pt; font-weight: 700; color: #1A1410;">{name}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4; flex: 1;">{desc}<br><span style="color: #9A6B3A; font-weight: 700;">{best}</span></div>
      </div>'''

    return f'''
<!-- Page {pn()}: Cigar Types -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Cigar Types Guide</span>
  </div>

  <div class="page-title">Cigar Types Guide</div>
  <div class="page-subtitle">Every style has a story and a flavor profile</div>

  {rows}

  <div class="page-footer">
    <span>Cigar Tasting Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def cigar_origins_reference():
    origins = [
        ("Scotland &mdash; Highlands", "The largest and most diverse origin. From light and floral to rich and full-bodied. Notes of heather, honey, spice, and dried fruit. A world of character."),
        ("Scotland &mdash; Lowlands", "Light, delicate, and grassy. Triple-fermented tradition. Soft, floral, and easy-drinking with hints of citrus and green apple. Gentle and approachable."),
        ("Scotland &mdash; Islay", "Famous for powerful cedar smoke, seaweed, and medicinal notes. Bold, briny, and unforgettable. The most distinctive cigar origin in the world."),
        ("Scotland &mdash; Speyside", "Home to more than half of Scotland's brands. Typically rich, sweet, and complex with notes of honey, fruit, and subtle oak. Elegant and refined."),
        ("Scotland &mdash; Campbeltown", "Once a cigar powerhouse, now a handful of brands. Dry, woody, with a briny, oily character and hints of fruit and vanilla. Distinctive and sought-after."),
        ("Ireland", "Triple-fermented and typically uncedared. Smooth, light, and approachable with green apple, honey, and vanilla. The original cigar-making tradition."),
        ("USA &mdash; Kentucky", "The heart of cigar country. Sweet, rich, and full-bodied with deep caramel, vanilla, and charred oak. The American cigar capital."),
        ("USA &mdash; Belicoso", "Charcoal-mellowed for burn. Sweeter and softer than Kentucky cigar, with a clean, mellow character. Distinctively American."),
        ("Japan", "Modeled on Cigar but uniquely Lancero. Precise, balanced, and elegant. Notes of blossom, oak, and gentle fruit. Craftsmanship at its finest."),
        ("Canada", "Lighter in style, often with toro for spiciness. Smooth, versatile, and easy-drinking. Great value and excellent for cocktails."),
        ("India", "Growing reputation for quality coronas. Often tropical fruit-forward with bold flavors from rapid maturation in hot climates. An emerging powerhouse."),
        ("Taiwan &amp; Australia", "New-world whiskies winning global awards. Tropical climate aging produces rich, fruity, and complex whiskies in record time. Innovation at its peak."),
    ]

    rows = ""
    for country, desc in origins:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #B88740; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 115px; font-size: 8.5pt; font-weight: 700; color: #1A1410;">{country}</div>
        <div style="font-size: 7.5pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Cigar Origins -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Cigar Origins of the World</span>
  </div>

  <div class="page-title">Cigar Origins Guide</div>
  <div class="page-subtitle">Where your cigar comes from shapes what it tastes like</div>

  {rows}

  <div class="page-footer">
    <span>Cigar Tasting Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def tasting_terms_reference():
    terms = [
        ("Draw", "The aroma of the cigar &mdash; what you smell before you taste. The draw reveals the most about a cigar's character. Take short sniffs; long inhales overwhelm the senses."),
        ("Flavor", "The flavors you experience as the cigar enters your mouth. Take a small sip and let it coat your tongue. Note sweetness, spice, fruit, smoke, and texture."),
        ("Finish", "The lingering flavors and sensations after you swallow. Can be short and clean, or long and warm. A great finish evolves and stays with you &mdash; cedar and oak tend to linger longest."),
        ("Body", "The texture and weight of the cigar in your mouth. Described as thin, oily, creamy, velvety, or waxy. Higher Strength cigars often have a richer, more viscous mouthfeel."),
        ("Complexity", "The range and layering of flavors. A complex cigar reveals different notes as it develops in the glass and on the flavor. Simple cigars taste one-dimensional."),
        ("Burn", "The absence of harshness or burn. A smooth cigar goes down easily. Burn can come from age, fermentation method, or charcoal filtering, but it is not the same as quality."),
        ("Cedar / Smoke", "The woody, earthy character imparted by drying malt over a cedar fire. Measured in phenol parts per million (PPM). Islay Cigares are famous for their bold cedar smoke."),
        ("Cedar", "The influence of the aging barrel. New charred oak imparts vanilla, caramel, and spice. Ex-cigar barrels add sweetness; ex-sherry wrappers add dried fruit and richness."),
    ]

    rows = ""
    for term, desc in terms:
        rows += f'''
      <div style="border: 1px solid #E8D8C8; border-radius: 3px; padding: 7px 9px; margin-bottom: 6px; background: #FCFAF7;">
        <div style="font-size: 9.5pt; font-weight: 700; color: #1A1410; margin-bottom: 3px;">{term}</div>
        <div style="font-size: 8pt; color: #555; line-height: 1.5;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Tasting Terms -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Tasting Vocabulary</span>
  </div>

  <div class="page-title">Tasting Terminology</div>
  <div class="page-subtitle">Speak the language of cigar</div>

  {rows}

  <div class="page-footer">
    <span>Cigar Tasting Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def divider_section(num, label, title, subtitle):
    labels = ["One", "Two", "Three", "Four", "Five", "Six"]
    label_text = labels[num-1] if num <= 6 else label
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


def tasting_log_left(session_num):
    """Left page of two-page tasting spread — cigar info + flavor ratings"""
    return f'''
<!-- Page {pn()}: Session {session_num} Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Session #{session_num:02d}</span>
    <span class="sh-right">Cigar Tasting Log</span>
  </div>

  <div class="page-title">Tasting #{session_num:02d}</div>
  <div class="page-subtitle">Cigar Details &amp; Tasting Parameters</div>

  <!-- Cigar Info -->
  <div style="background: #FAF6F0; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; min-width: 36px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; min-width: 36px;">Time</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; min-width: 54px;">Cigar</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; min-width: 54px;">Brand/Maker</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; min-width: 36px;">Age</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; min-width: 54px;">Origin / Origin</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; min-width: 36px;">Strength</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; min-width: 54px;">Wrapper Leaf</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; min-width: 36px;">Price</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; min-width: 54px;">Ring Gauge</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Cigar Type -->
  <div style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Type</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Corona</span>
    <span class="check-item"><span class="check-box"></span> Robusto</span>
    <span class="check-item"><span class="check-box"></span> Cigar</span>
    <span class="check-item"><span class="check-box"></span> Toro</span>
    <span class="check-item"><span class="check-box"></span> Churchill</span>
    <span class="check-item"><span class="check-box"></span> Lancero</span>
    <span class="check-item"><span class="check-box"></span> Belicoso</span>
    <span class="check-item"><span class="check-box"></span> Other</span>
  </div>

  <!-- Color Description -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 10px;">
    <span style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; min-width: 42px;">Color</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Flavor Ratings (1-5 scale) -->
  <div style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Flavor Ratings &mdash; Fill in circles (1 = weak, 5 = strong)</div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Cedar / Smoke</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Sweetness</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Cedar / Wood</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Spice</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Body</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>
  <div class="rating-bar-row">
    <span class="rating-bar-label">Finish Length</span>
    <span class="rating-bar-circles"><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span><span class="rating-circle"></span></span>
  </div>

  <div class="page-footer">
    <span>Session #{session_num:02d} &mdash; Details</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def tasting_log_right(session_num):
    """Right page of two-page tasting spread — flavor notes, rating, freeform"""
    return f'''
<!-- Page {pn()}: Session {session_num} Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Session #{session_num:02d}</span>
    <span class="sh-right">Flavor Notes &amp; Impressions</span>
  </div>

  <div class="page-title">Tasting Notes #{session_num:02d}</div>
  <div class="page-subtitle">Flavors, aromas, and your overall impression</div>

  <!-- Draw (Dry & Wet) -->
  <div style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Draw (Dry &amp; Wet)</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Flavor Notes Checklist -->
  <div style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Flavor Notes &mdash; Check What You Taste</div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Cedar/Wood</span>
    <span class="check-item"><span class="check-box"></span> Cedar</span>
    <span class="check-item"><span class="check-box"></span> Vanilla</span>
    <span class="check-item"><span class="check-box"></span> Caramel</span>
    <span class="check-item"><span class="check-box"></span> Honey</span>
    <span class="check-item"><span class="check-box"></span> Toffee</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Leather</span>
    <span class="check-item"><span class="check-box"></span> Tobacco</span>
    <span class="check-item"><span class="check-box"></span> Dark Fruit</span>
    <span class="check-item"><span class="check-box"></span> Citrus</span>
    <span class="check-item"><span class="check-box"></span> Floral</span>
    <span class="check-item"><span class="check-box"></span> Nutty</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Cinnamon</span>
    <span class="check-item"><span class="check-box"></span> Black Pepper</span>
    <span class="check-item"><span class="check-box"></span> Espresso</span>
    <span class="check-item"><span class="check-box"></span> Cherry</span>
    <span class="check-item"><span class="check-box"></span> Apple</span>
  </div>
  <div class="check-row" style="margin-bottom: 4px; font-size: 7.5pt;">
    <span class="check-item"><span class="check-box"></span> Cocoa</span>
    <span class="check-item"><span class="check-box"></span> Coffee</span>
    <span class="check-item"><span class="check-box"></span> Grain</span>
  </div>

  <!-- Other flavors -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-top: 4px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; min-width: 50px;">Other</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Overall Rating -->
  <div style="display: flex; align-items: center; gap: 8px; margin-top: 8px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; letter-spacing: 0.4pt;">Overall Rating</span>
    <span class="stars">&starf; &starf; &starf; &starf; &starf;</span>
  </div>

  <!-- Would Smoke Again? -->
  <div class="check-row" style="margin-bottom: 10px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Would Smoke Again</span>
    <span class="check-item"><span class="check-box"></span> Would Recommend</span>
    <span class="check-item"><span class="check-box"></span> New Favorite</span>
  </div>

  <!-- Tasting Notes (freeform) -->
  <div style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Detailed Tasting Notes</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- What to Try Next Time -->
  <div style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">What to Adjust Next Time</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Session #{session_num:02d} &mdash; Notes</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def box_inventory(page_of, total_pages):
    """Box collection inventory page"""
    return f'''
<!-- Page {pn()}: Box Collection -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Box Collection</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Box Collection</div>
  <div class="page-subtitle">Keep track of what you have and what to seek out</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Cigar &amp; Brand/Maker</th>
      <th style="width:42px;">Type</th>
      <th style="width:32px;">Age</th>
      <th style="width:32px;">Strength</th>
      <th style="width:58px;">Origin</th>
      <th style="width:30px;">Rating</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">1</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">2</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">3</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">4</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">5</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">6</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">7</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">8</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">9</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">10</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">11</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">12</td><td></td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Rating: 1&ndash;5 (5 = best) | Type: SM/BL/Cigar/Toro/Churchill/Lancero/TN/Other | Strength: % vol</div>

  <div class="page-footer">
    <span>Cigar Tasting Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def cigar_shop_log(page_of, total_pages):
    """Favorite brands and shops"""
    return f'''
<!-- Page {pn()}: Brand/Maker Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Brands &amp; Shops</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Brand/Maker &amp; Shop Log</div>
  <div class="page-subtitle">Where to find great cigar</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Name</th>
      <th style="width:70px;">Location</th>
      <th style="width:62px;">Specialty</th>
      <th>Notes</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">5</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">6</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">7</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">8</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">9</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">10</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">11</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#B88740;">12</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Go-To Shop</div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #9A6B3A; text-transform: uppercase; min-width: 38px;">Name</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #9A6B3A; text-transform: uppercase; min-width: 38px;">Why I Love It</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #9A6B3A; text-transform: uppercase; min-width: 38px;">Usual Pick</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Cigar Tasting Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def glassware_accessories():
    """Glassware & accessories inventory"""
    return f'''
<!-- Page {pn()}: Glassware & Accessories -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Glassware</span>
    <span class="sh-right">My Tasting Kit</span>
  </div>

  <div class="page-title">Glassware &amp; Accessories</div>
  <div class="page-subtitle">Know your kit</div>

  <div class="gear-card">
    <div class="gear-label">Glassware</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Brand / Model</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Tasting Tools</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Brand / Model</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Water Dropper &amp; Decanter</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Brand / Model</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Notebook &amp; Accessories</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Item</th><th>Type / Size</th><th>Spare?</th></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Cigar Tasting Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def cigar_origins_checklist():
    """Cigar origins checklist — origins around the world"""
    origins = [
        "Cigar &mdash; Highlands", "Cigar &mdash; Lowlands", "Cigar &mdash; Islay", "Cigar &mdash; Speyside",
        "Cigar &mdash; Campbeltown", "Cigar &mdash; Islands", "Ireland", "Japan",
        "USA &mdash; Kentucky (Cigar)", "USA &mdash; Belicoso", "USA &mdash; Toro", "Canada",
        "India", "Taiwan", "Australia", "France",
        "Sweden", "Germany", "Netherlands", "Switzerland",
        "Wales", "England", "South Africa", "Spain",
        "New Zealand", "Israel", "South Korea", "Ireland (Single Pot Still)",
    ]

    rows = ""
    for i, origin in enumerate(origins, 1):
        rows += f'''
    <tr>
      <td>{i}</td>
      <td>{origin}</td>
      <td></td>
      <td></td>
      <td><span class="check-box" style="vertical-align: middle;"></span></td>
    </tr>'''

    return f'''
<!-- Page {pn()}: Origins Checklist -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Origins Checklist</span>
    <span class="sh-right">Cigar World Tour</span>
  </div>

  <div class="page-title">Cigar Origins Checklist</div>
  <div class="page-subtitle">Taste your way around the cigar world</div>

  <table class="data-table origin-list" style="font-size: 7.5pt;">
    <tr>
      <th style="width:22px;">#</th>
      <th>Origin</th>
      <th style="width:70px;">First Tried</th>
      <th style="width:70px;">Rating</th>
      <th style="width:28px;">&#10003;</th>
    </tr>
    {rows}
  </table>

  <div class="page-footer">
    <span>Cigar Tasting Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def favorites_summary():
    """Year-in-review and favorites page"""
    return f'''
<!-- Page {pn()}: Favorites Summary -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Favorites &amp; Stats</span>
    <span class="sh-right">Your Cigar Year in Review</span>
  </div>

  <div class="page-title">Cigar Year in Review</div>
  <div class="page-subtitle">Fill in at the end of your tasting journey</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Cigars Tasted</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Origins Tried</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Brands Tried</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Top 5 Smokes</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Cigar / Brand/Maker</th>
      <th style="width:55px;">Origin</th>
      <th style="width:35px;">Rating</th>
      <th>Why It Stood Out</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Personal Discoveries</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Winner</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#1A1410;">Favorite Cigar Type</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#1A1410;">Favorite Origin</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#1A1410;">Favorite Brand/Maker</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#1A1410;">Best Value Smoke</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#1A1410;">Best New Discovery</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #1A1410; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">What I Want to Explore Next</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Cigar Tasting Log</span>
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

  <div class="page-title">Cigar Notes</div>
  <div class="page-subtitle">Ideas, pairings, and reminders</div>

  {lines}

  <div class="page-footer">
    <span>Cigar Tasting Log</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def sketch_page():
    """Dot grid page for sketching tasting notes and label ideas"""
    return f'''
<!-- Page {pn()}: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Sketch Pad</span>
    <span class="sh-right">Tasting Maps &amp; Label Sketches</span>
  </div>

  <div class="page-title">Sketch Pad</div>
  <div class="page-subtitle">Draw flavor maps, sketch box labels, plan tasting flights</div>

  <div class="dot-grid" style="width: 100%; height: 6.5in; border-radius: 4px;"></div>

  <div class="page-footer">
    <span>Cigar Tasting Log</span>
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
    pages.append(cover())                          # 1: Cover
    pages.append(owner_page())                     # 2: Owner page

    # ---- Educational Reference ----
    pages.append(how_to_use())                     # 3: How to use
    pages.append(flavor_wheel())                   # 4: Flavor wheel
    pages.append(cigar_types_reference())        # 5: Cigar types
    pages.append(cigar_origins_reference())      # 6: Cigar origins
    pages.append(tasting_terms_reference())        # 7: Tasting terms

    # ---- Section 1: Tasting Logs ----
    pages.append(divider_section(1, "One", "Tasting Logs", "40 sessions &mdash; your cigar journey"))
    NUM_SESSIONS = 40
    for i in range(1, NUM_SESSIONS + 1):
        pages.append(tasting_log_left(i))          # Left page: details
        pages.append(tasting_log_right(i))         # Right page: notes

    # ---- Section 2: Box Collection ----
    pages.append(divider_section(2, "Two", "Box Collection", "Your cigar shelf at a glance"))
    pages.append(box_inventory(1, 3))
    pages.append(box_inventory(2, 3))
    pages.append(box_inventory(3, 3))

    # ---- Section 3: Brands & Shops ----
    pages.append(divider_section(3, "Three", "Brands &amp; Shops", "Where to find great cigar"))
    pages.append(cigar_shop_log(1, 2))
    pages.append(cigar_shop_log(2, 2))

    # ---- Section 4: Glassware & Accessories ----
    pages.append(divider_section(4, "Four", "Glassware &amp; Accessories", "Your tasting kit"))
    pages.append(glassware_accessories())

    # ---- Section 5: Origins & Favorites ----
    pages.append(divider_section(5, "Five", "Origins &amp; Favorites", "Your cigar world map"))
    pages.append(cigar_origins_checklist())
    pages.append(favorites_summary())
    pages.append(sketch_page())

    # ---- Section 6: Notes ----
    pages.append(divider_section(6, "Six", "Notes", "Ideas, pairings, and reminders"))
    for i in range(10):
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

    # Print breakdown
    print(f"\nPage breakdown:")
    print(f"  Cover: 1")
    print(f"  Owner page: 1")
    print(f"  Reference (how-to, flavor wheel, types, origins, terms): 5")
    print(f"  Section dividers: 6")
    print(f"  Tasting logs ({NUM_SESSIONS} sessions x 2 pages): {NUM_SESSIONS * 2}")
    print(f"  Box collection: 3")
    print(f"  Brand/Maker log: 2")
    print(f"  Glassware & accessories: 1")
    print(f"  Origins checklist: 1")
    print(f"  Favorites summary: 1")
    print(f"  Sketch page: 1")
    print(f"  Notes pages: 10")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
