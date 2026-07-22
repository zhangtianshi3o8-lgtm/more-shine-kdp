#!/usr/bin/env python3
"""
Mushroom Foraging Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: American mushroom foragers and nature enthusiasts (all levels)
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "mushroom_foraging_journal_us_V1.0.html")

BOOK_TITLE = "Mushroom Foraging Journal"
BOOK_SUBTITLE = "Track Every Find, Every Habitat, Every Season"

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
/* Forest charcoal: #141A12, #1E2820 */
/* Sage/moss: #7A8B6A, #3D4A38 */
/* Earthy brown: #8B6F47 */
/* Gold accent: #C4A04A */
/* Warm cream: #FAF8F2, #F5F2EA */

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
  background: linear-gradient(165deg, #141A12 0%, #1E2820 30%, #141A12 65%, #0C100A 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* Sage glow background */
.cover .glow-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #7A8B6A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #7A8B6A, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 90% 40%, #7A8B6A, transparent),
    radial-gradient(ellipse 16px 10px at 40% 90%, #C4A04A, transparent);
}

/* ===== CSS Mushroom Illustration ===== */
.cover .mushroom-wrap {
  width: 130px; height: 170px;
  position: relative;
  margin: 0 auto 20px;
}

/* Mushroom cap — dome shape using border-radius */
.cover .cap {
  width: 100px; height: 65px;
  position: absolute;
  top: 0; left: 15px;
  background: linear-gradient(170deg,
    rgba(250,248,242,0.12) 0%,
    rgba(250,248,242,0.04) 40%,
    rgba(196,160,74,0.06) 80%,
    rgba(122,139,106,0.08) 100%);
  border-radius: 50% 50% 22% 22% / 80% 80% 20% 20%;
  border: 1.5px solid rgba(196,160,74,0.5);
}

/* Cap highlight */
.cover .cap-shine {
  width: 35px; height: 18px;
  position: absolute;
  top: 10px; left: 32px;
  background: linear-gradient(160deg, rgba(250,248,242,0.25), rgba(250,248,242,0.03));
  border-radius: 50%;
  transform: rotate(-15deg);
}

/* Gills under cap */
.cover .gills {
  width: 80px; height: 14px;
  position: absolute;
  top: 58px; left: 25px;
  background: repeating-linear-gradient(
    90deg,
    transparent 0px,
    transparent 4px,
    rgba(196,160,74,0.2) 4px,
    rgba(196,160,74,0.2) 5px);
  border-radius: 0 0 50% 50% / 0 0 100% 100%;
  clip-path: ellipse(50% 100% at 50% 0%);
}

/* Stem */
.cover .stem {
  width: 26px; height: 85px;
  position: absolute;
  top: 65px; left: 52px;
  background: linear-gradient(90deg,
    rgba(250,248,242,0.04) 0%,
    rgba(250,248,242,0.12) 40%,
    rgba(250,248,242,0.06) 60%,
    rgba(250,248,242,0.02) 100%);
  border-radius: 3px 3px 8px 8px;
  border-left: 1px solid rgba(196,160,74,0.35);
  border-right: 1px solid rgba(196,160,74,0.35);
}

/* Ring/annulus on stem */
.cover .ring {
  width: 36px; height: 8px;
  position: absolute;
  top: 80px; left: 47px;
  background: rgba(196,160,74,0.15);
  border: 1px solid rgba(196,160,74,0.35);
  border-radius: 50%;
}

/* Base/volva */
.cover .base {
  width: 38px; height: 16px;
  position: absolute;
  top: 144px; left: 46px;
  background: linear-gradient(180deg,
    rgba(250,248,242,0.08),
    rgba(250,248,242,0.02));
  border: 1px solid rgba(196,160,74,0.4);
  border-radius: 50%;
  box-shadow: 0 3px 8px rgba(0,0,0,0.4);
}

/* Base shadow */
.cover .base-shadow {
  width: 50px; height: 4px;
  position: absolute;
  top: 158px; left: 40px;
  background: rgba(0,0,0,0.25);
  border-radius: 50%;
  filter: blur(2px);
}

/* Small mushroom companion */
.cover .cap2 {
  width: 50px; height: 32px;
  position: absolute;
  top: 118px; left: 100px;
  background: linear-gradient(170deg,
    rgba(250,248,242,0.08) 0%,
    rgba(122,139,106,0.08) 100%);
  border-radius: 50% 50% 18% 18% / 75% 75% 25% 25%;
  border: 1px solid rgba(196,160,74,0.35);
}

.cover .stem2 {
  width: 12px; height: 38px;
  position: absolute;
  top: 145px; left: 119px;
  background: rgba(250,248,242,0.05);
  border-left: 0.8px solid rgba(196,160,74,0.25);
  border-right: 0.8px solid rgba(196,160,74,0.25);
  border-radius: 2px;
}

/* Vapor/spore lines */
.cover .spore1 {
  width: 2px; height: 20px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.3), transparent);
  position: absolute;
  top: -6px; left: 45px;
  border-radius: 50%;
  transform: rotate(-8deg);
}
.cover .spore2 {
  width: 2px; height: 26px;
  background: linear-gradient(180deg, transparent, rgba(196,160,74,0.2), transparent);
  position: absolute;
  top: -12px; left: 62px;
  border-radius: 50%;
  transform: rotate(6deg);
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
  color: #D4C49A;
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
  color: #D4C49A;
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
  background: linear-gradient(165deg, #141A12 0%, #1E2820 50%, #141A12 100%);
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
    radial-gradient(ellipse 22px 13px at 70% 75%, #7A8B6A, transparent),
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
  color: #D4C49A;
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
  border-bottom: 1.5px solid #7A8B6A;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #141A12;
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
  color: #141A12;
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
  background: #7A8B6A;
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
  background: #FAF8F2;
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
  color: #141A12;
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
  background: #FAF8F2;
  border-left: 3px solid #7A8B6A;
  padding: 8px 10px;
  margin-bottom: 10px;
  font-size: 8pt;
  color: #333;
  line-height: 1.5;
}
.info-box .info-title {
  font-weight: 700;
  color: #141A12;
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
  color: #141A12;
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
  border: 1.5px solid #7A8B6A;
  border-radius: 50%;
  display: inline-block;
}

/* ---- Category Card ---- */
.cat-card {
  border: 1px solid #D8E0D0;
  border-radius: 4px;
  padding: 6px 8px;
  margin-bottom: 5px;
  background: #FCFBF8;
}
.cat-card-label {
  font-size: 7pt;
  font-weight: 700;
  color: #7A8B6A;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 3px;
}
.cat-card-notes {
  font-size: 7.5pt;
  color: #888;
  line-height: 1.5;
}

/* ---- Stat Card ---- */
.stat-card {
  text-align: center;
  padding: 6px 4px;
  background: #FAF8F2;
  border-radius: 4px;
  border: 1px solid #D8E0D0;
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
  color: #141A12;
}

/* ---- Gear Card ---- */
.gear-card {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 8px;
  margin-bottom: 6px;
  background: #FCFBF8;
}
.gear-card .gear-label {
  font-size: 7pt;
  font-weight: 700;
  color: #7A8B6A;
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

/* ---- Species List ---- */
table.species-list th {
  background: #7A8B6A;
}
table.species-list td:first-child {
  width: 22px;
  text-align: center;
  font-weight: 700;
  color: #7A8B6A;
}
table.species-list td:last-child {
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
  <div class="mushroom-wrap">
    <div class="spore1"></div>
    <div class="spore2"></div>
    <div class="cap"></div>
    <div class="cap-shine"></div>
    <div class="gills"></div>
    <div class="ring"></div>
    <div class="stem"></div>
    <div class="base"></div>
    <div class="base-shadow"></div>
    <div class="cap2"></div>
    <div class="stem2"></div>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">40 Foraging Sessions</span>
      <span class="feature-badge">Species ID Guide</span>
      <span class="feature-badge">Habitat Tracker</span>
      <span class="feature-badge">Seasonal Calendar</span>
    </div>
    <div class="tagline">For Mushroom Hunters &amp; Nature Lovers</div>
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
    <div style="font-size: 16pt; font-weight: 700; color: #141A12; margin-bottom: 6px;">This Journal Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #141A12; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #7A8B6A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Home Region</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #7A8B6A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Mushroom</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #7A8B6A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Years Foraging</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #7A8B6A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Foraging Spot</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Mushroom Foraging Journal</span>
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
  <div class="page-subtitle">Make every foray a learning experience</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Foraging Journal?</div>
    The difference between picking mushrooms and understanding them is attention. A foraging journal helps you recognize patterns &mdash; which species appear where, how weather and season affect fruiting, and which habitats consistently produce. Over time, your journal becomes your personal map of the forest.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #141A12; font-size: 10pt; margin-bottom: 6px;">Tips for Better Foraging</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Learn from local experts.</strong> Join a local mycological society, attend forays, and go with experienced foragers before relying on field guides alone. There is no substitute for hands-on learning from someone who knows your local species.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Never eat anything you cannot identify with certainty.</strong> When in doubt, throw it out. Many edible mushrooms have toxic look-alikes. Spore prints, habitat, and microscopic details matter. A single mistake can be fatal.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Record the habitat, not just the mushroom.</strong> Note the trees, soil, elevation, moisture, and weather. Mushrooms are not random &mdash; they have relationships with specific trees and environments. Understanding habitat is the key to finding more.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Take spore prints.</strong> Place a cap gill-side down on paper for 4 to 24 hours. Spore color &mdash; white, brown, pink, purple-black, rusty, or yellowish &mdash; is one of the most important identification features. Use half white and half dark paper.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Photograph everything.</strong> Capture the cap from above, the gills or pores underneath, the stem base (including any volva or bulb), and the mushroom in its habitat. You cannot take too many reference photos.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #F5F2E8; border: 1px solid #D8E0C0; border-radius: 3px; font-size: 8pt; color: #555; font-style: italic;">
    <strong style="color: #5A7042;">Pro Tip:</strong> Carry a basket or mesh bag, not a plastic bag. Mushrooms need to breathe, and a mesh bag lets spores spread as you walk &mdash; helping future flushes.
  </div>

  <div class="page-footer">
    <span>Mushroom Foraging Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def mushroom_anatomy():
    """Anatomical parts of a mushroom — educational reference"""
    parts = [
        ("Cap (Pileus)",
         "The top of the mushroom. Note its shape (convex, flat, conical, depressed), "
         "texture (smooth, scaly, hairy, slimy), color, and size in inches or centimeters. "
         "The cap often changes shape as the mushroom ages."),
        ("Gills, Pores, or Teeth",
         "The spore-producing surface under the cap. Gills are blade-like ridges; "
         "pores look like a sponge; teeth are spine-like projections. Note their spacing, "
         "attachment to the stem, and color. This is critical for identification."),
        ("Spore Print Color",
         "Place a fresh cap on paper for 4 to 24 hours. The deposited spore dust "
         "reveals a characteristic color: white, cream, pink, brown, rusty-brown, "
         "purple-black, or yellowish. One of the most reliable identification features."),
        ("Stem (Stipe)",
         "Note the height, thickness, shape (equal, club-shaped, bulbous), texture, "
         "and color. Check for a hollow or solid interior. Some stems snap cleanly, "
         "others are fibrous &mdash; this difference matters for identification."),
        ("Ring (Annulus)",
         "A skirt-like remnant of the partial veil on the upper stem. Note its "
         "position, texture, and color. Some mushrooms have no ring; others have a "
         "prominent one that may disappear with age."),
        ("Volva (Cup)",
         "A cup-like sac at the base of the stem, remnant of the universal veil. "
         "Present in some species (notably Amanitas). Always dig carefully around "
         "the base &mdash; the presence or absence of a volva can be a matter of life "
         "and death in identification."),
        ("Flesh",
         "Cut the mushroom open. Note the color, thickness, and any color changes "
         "when bruised or exposed to air. Some species turn blue, red, or yellow "
         "on contact with air &mdash; an important identification clue."),
        ("Odor",
         "Smell the mushroom. Common descriptions include mild, farinaceous "
         "(like raw pastry dough), anise, garlic, fishy, fruity, rancid, or "
         "none. Odor can be subtle, so take a good sniff of a fresh specimen."),
    ]

    rows = ""
    for name, desc in parts:
        rows += f'''
      <div style="border: 1px solid #D8E0D0; border-radius: 3px; padding: 6px 9px; margin-bottom: 5px; background: #FCFBF8;">
        <div style="font-size: 9pt; font-weight: 700; color: #141A12; margin-bottom: 3px;">{name}</div>
        <div style="font-size: 7.5pt; color: #555; line-height: 1.5;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Mushroom Anatomy -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Mushroom Anatomy</span>
  </div>

  <div class="page-title">Mushroom Anatomy &amp; Identification</div>
  <div class="page-subtitle">Know the parts &mdash; accurate records start here</div>

  {rows}

  <div class="page-footer">
    <span>Mushroom Foraging Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def habitat_guide():
    """Common mushroom habitats reference page"""
    habitats = [
        ("Deciduous Forest",
         "Oak, beech, birch, maple. Rich in mycorrhizal species like chanterelles, "
         "boletes, and amanitas. Ground-dwelling species thrive in leaf litter and "
         "mossy soil. Peak season varies by region, typically late summer through fall."),
        ("Coniferous Forest",
         "Pine, spruce, fir, hemlock. Home to king boletes, matsutake, and many "
         "brittle gills (Russula). Acidic soil and needle duff create distinct "
         "communities. Some of the most prized edibles grow only here."),
        ("Mixed Forest",
         "Where deciduous and coniferous trees intermingle. Often the most "
         "productive habitat due to diverse tree hosts. Look for edge zones where "
         "two forest types meet &mdash; mushrooms love boundaries."),
        ("Grasslands & Meadows",
         "Open fields, pastures, and lawns. Home to puffballs, parasols, ink caps, "
         "and field mushrooms. Fairy rings are a telltale sign of underground "
         "mycelium. Avoid chemically treated lawns and livestock pastures."),
        ("Wood Chips & Mulch",
         "Landscaped areas, garden beds, and trails. Decomposer species like "
         "wine caps, inky caps, and some psilocybes fruit abundantly in fresh "
         "wood chips. Check urban parks and municipal landscaping."),
        ("Burned Ground",
         "Forest areas after wildfire. Morels famously fruit in the spring "
         "following a fire, especially in conifer burn zones. This niche is "
         "short-lived but incredibly productive for determined foragers."),
        ("Decaying Wood & Logs",
         "Fallen trees, stumps, and standing deadwood. Look for oyster mushrooms, "
         "lion's mane, turkey tail, and sulfur tufts. Decomposer species that "
         "recycle dead wood into soil &mdash; nature's recyclers."),
        ("Wetlands & Stream Banks",
         "Damp, shaded areas near water. Moisture-loving species thrive here, "
         "especially after heavy rain. Check mossy banks and flood plains where "
         "organic matter accumulates."),
    ]

    rows = ""
    for name, desc in habitats:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #7A8B6A; background: #FAF8F2; border-radius: 0 3px 3px 0;">
        <div style="min-width: 100px; font-size: 8pt; font-weight: 700; color: #141A12;">{name}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Habitat Guide -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Where to Look</span>
  </div>

  <div class="page-title">Habitat Guide</div>
  <div class="page-subtitle">Mushrooms grow where their food grows</div>

  {rows}

  <div class="page-footer">
    <span>Mushroom Foraging Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def foraging_safety():
    """Safety rules — the most important reference page"""
    return f'''
<!-- Page {pn()}: Foraging Safety -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Safety First</span>
    <span class="sh-right">Read Before You Forage</span>
  </div>

  <div class="page-title">Foraging Safety Rules</div>
  <div class="page-subtitle">These rules exist because people have died breaking them</div>

  <div style="background: #FFF5F5; border: 1.5px solid #C04040; border-radius: 4px; padding: 10px 12px; margin-bottom: 12px;">
    <div style="font-size: 10pt; font-weight: 700; color: #C04040; margin-bottom: 6px;">The Golden Rule</div>
    <div style="font-size: 8.5pt; color: #555; line-height: 1.55;">
      <strong>Never eat a wild mushroom unless you can identify it with 100% certainty.</strong>
      Some toxic species look nearly identical to edible ones. A single bite of the
      death cap (Amanita phalloides) can cause liver failure and death. When in any
      doubt whatsoever, do not eat it. There is no room for guesswork.
    </div>
  </div>

  <div style="font-size: 8.5pt; line-height: 1.65; color: #333;">
    <div style="margin-bottom: 8px;">
      <strong>1. Start with the easy ones.</strong> Learn a few unmistakable species first &mdash;
      chanterelles, morels, chicken of the woods, puffballs. Master these before
      tackling difficult groups. Do not rush.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>2. Dig, don't pull.</strong> Carefully excavate the entire mushroom including
      the base. The volva and bulb at the base are essential for identification in
      many groups, especially Amanitas.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>3. Cook all wild mushrooms.</strong> Even choice edibles can cause stomach upset
      when raw. Always cook thoroughly. Avoid alcohol with certain species (notably
      Coprinus comatus and related ink caps) as it can trigger severe reactions.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>4. Keep species separate.</strong> Do not mix different species in the same
      container. A single toxic specimen hidden among edibles can contaminate the
      entire harvest. Use divided baskets or separate paper bags.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>5. Try new species in small amounts.</strong> Even edible species can cause
      allergic reactions in some people. Eat a small portion the first time and
      wait 24 hours before eating more. Save a specimen in the refrigerator in
      case of adverse reaction.
    </div>
    <div style="margin-bottom: 8px;">
      <strong>6. Know your local emergency resources.</strong> If you suspect mushroom
      poisoning, call Poison Control immediately at <strong>1-800-222-1222</strong>.
      Keep a sample of the mushroom for identification. Do not wait for symptoms &mdash;
      some toxins have a delayed onset of 6 to 24 hours.
    </div>
  </div>

  <div style="margin-top: 10px; padding: 7px 10px; background: #FAF8F2; border: 1px solid #E0D8C0; border-radius: 3px; font-size: 7.5pt; color: #777; font-style: italic;">
    This journal is a record-keeping tool. It is not a field guide and cannot replace expert knowledge or a comprehensive regional guidebook. Always cross-reference multiple sources before consuming any wild mushroom.
  </div>

  <div class="page-footer">
    <span>Mushroom Foraging Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def seasonal_calendar():
    """Seasonal fruiting calendar reference"""
    seasons = [
        ("Spring (Mar &ndash; May)",
         "Morels are the stars of spring, fruiting in elm orchards, burn sites, "
         "and under dying elms and ash. Pheasant backs appear on dead deciduous "
         "wood. Oyster mushrooms begin to flush. Asparagus and ramps share the "
         "season &mdash; a forager's paradise. Watch soil temperatures: morels "
         "appear when ground temps reach the low 50s F.",
         "Morels, Pheasant Back, Oysters, Wood Ear"),
        ("Summer (Jun &ndash; Aug)",
         "Chanterelles begin in early summer after warm rains. Chicken of the "
         "woods and sulfur tuft appear on dead wood. Boletes start to show in "
         "mid-summer under conifers and oaks. Lobster mushrooms push up through "
         "the duff. The season shifts from dead-wood decomposers to "
         "mycorrhizal ground species.",
         "Chanterelles, Boletes, Chicken of the Woods, Lobster, Black Trumpet"),
        ("Fall (Sep &ndash; Nov)",
         "The peak season for diversity and abundance. King boletes, matsutake, "
         "hedgehogs, hen of the woods, and giant puffballs all appear. This is "
         "when the serious foraging happens &mdash; cool nights and warm, wet days "
         "trigger massive fruiting. Keep your basket ready and check spots "
         "repeatedly.",
         "King Boletes, Hen of the Woods, Hedgehogs, Matsutake, Puffballs"),
        ("Winter (Dec &ndash; Feb)",
         "The quiet season, but not empty. Oyster mushrooms tolerate freezing "
         "and fruit on dead wood after thaws. Enoki (wild form) appears on "
         "fallen logs. Velvet shank (Flammulina) pushes through snow. Winter "
         "truffles are for the dedicated with trained dogs. Most species rest, "
         "waiting for spring's warmth.",
         "Oysters, Velvet Shank, Enoki (wild), Wood Ear, Truffles"),
    ]

    rows = ""
    for season, desc, species in seasons:
        rows += f'''
      <div style="border: 1px solid #D8E0D0; border-radius: 4px; padding: 8px 10px; margin-bottom: 6px; background: #FCFBF8;">
        <div style="font-size: 9.5pt; font-weight: 700; color: #5A7042; margin-bottom: 4px;">{season}</div>
        <div style="font-size: 7.5pt; color: #555; line-height: 1.5; margin-bottom: 4px;">{desc}</div>
        <div style="font-size: 7pt; font-weight: 700; color: #7A8B6A; text-transform: uppercase; letter-spacing: 0.3pt;">Key Species</div>
        <div style="font-size: 7.5pt; color: #888; font-style: italic;">{species}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Seasonal Calendar -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Seasonal Calendar</span>
  </div>

  <div class="page-title">Seasonal Fruiting Calendar</div>
  <div class="page-subtitle">When to look &mdash; timing is everything</div>

  {rows}

  <div class="page-footer">
    <span>Mushroom Foraging Journal</span>
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


def foraging_log_left(session_num):
    """Left page of two-page foraging spread — specimen details"""
    return f'''
<!-- Page {pn()}: Session {session_num} Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Find #{session_num:02d}</span>
    <span class="sh-right">Mushroom Foraging Journal</span>
  </div>

  <div class="page-title">Find #{session_num:02d}</div>
  <div class="page-subtitle">Specimen Details &amp; Field Conditions</div>

  <!-- Date/Time/Weather -->
  <div style="background: #FAF8F2; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 30px;">Date</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 30px;">Time</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 40px;">Weather</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 40px;">Temp</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 44px;">Rain?</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 32px;">Soil</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Location -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 6px;">
    <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 52px;">Location</span>
    <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 16px;"></div>
  </div>
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 52px;">GPS / Trail</span>
    <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 16px;"></div>
  </div>

  <!-- Habitat Type -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Habitat</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Deciduous</span>
    <span class="check-item"><span class="check-box"></span> Coniferous</span>
    <span class="check-item"><span class="check-box"></span> Mixed Woods</span>
    <span class="check-item"><span class="check-box"></span> Meadow</span>
    <span class="check-item"><span class="check-box"></span> On Wood</span>
    <span class="check-item"><span class="check-box"></span> Burn Site</span>
    <span class="check-item"><span class="check-box"></span> Other</span>
  </div>

  <!-- Tree Association -->
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 54px;">Tree ID</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <!-- Mushroom Details -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Specimen Identification</div>
  <div style="background: #FCFBF8; border: 1px solid #E0E0E0; border-radius: 4px; padding: 8px 10px; margin-bottom: 8px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 42px;">Common</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 42px;">Scientific</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 30px;">Cap</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 28px;">Size</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 42px;">Gills/Pores</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 42px;">Spore Color</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 30px;">Stem</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 42px;">Ring/Volva</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 30px;">Odor</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Confidence Level -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Identification Confidence</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Certain</span>
    <span class="check-item"><span class="check-box"></span> Probable</span>
    <span class="check-item"><span class="check-box"></span> Uncertain</span>
    <span class="check-item"><span class="check-box"></span> Submitted for Expert ID</span>
  </div>

  <div class="page-footer">
    <span>Find #{session_num:02d} &mdash; Details</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def foraging_log_right(session_num):
    """Right page of two-page foraging spread — notes, edibility, sketch"""
    return f'''
<!-- Page {pn()}: Session {session_num} Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Find #{session_num:02d}</span>
    <span class="sh-right">Notes &amp; Impressions</span>
  </div>

  <div class="page-title">Field Notes #{session_num:02d}</div>
  <div class="page-subtitle">Observations, edibility, and your impressions</div>

  <!-- Abundance & Condition -->
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px; margin-bottom: 8px;">
    <div style="display: flex; align-items: baseline; gap: 6px;">
      <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 50px;">Quantity</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px;">
      <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; min-width: 50px;">Condition</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
  </div>

  <!-- Edibility -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Edibility</div>
  <div class="check-row" style="margin-bottom: 8px;">
    <span class="check-item"><span class="check-box"></span> Choice Edible</span>
    <span class="check-item"><span class="check-box"></span> Edible</span>
    <span class="check-item"><span class="check-box"></span> Inedible</span>
    <span class="check-item"><span class="check-box"></span> Poisonous</span>
    <span class="check-item"><span class="check-box"></span> Unknown</span>
    <span class="check-item"><span class="check-box"></span> Medicinal</span>
  </div>

  <!-- Look-alikes Noted? -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Look-alikes Checked Against</div>
  <div class="wline-sm" style="margin-bottom: 1px;"></div>
  <div class="wline-sm" style="margin-bottom: 8px;"></div>

  <!-- Photos / Specimen Taken -->
  <div class="check-row" style="margin-bottom: 8px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Photos Taken</span>
    <span class="check-item"><span class="check-box"></span> Spore Print Made</span>
    <span class="check-item"><span class="check-box"></span> Specimen Collected</span>
    <span class="check-item"><span class="check-box"></span> Tasted (cooked)</span>
  </div>

  <!-- Detailed Description -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Detailed Description &amp; Observations</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Habitat & Location Notes -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Habitat &amp; Surroundings</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Overall Experience -->
  <div style="display: flex; align-items: center; gap: 8px; margin-top: 10px; margin-bottom: 8px;">
    <span style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt;">Experience Rating</span>
    <span class="stars">&starf; &starf; &starf; &starf; &starf;</span>
  </div>

  <!-- Will Return to This Spot? -->
  <div class="check-row" style="margin-bottom: 8px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Will Return</span>
    <span class="check-item"><span class="check-box"></span> New Spot</span>
    <span class="check-item"><span class="check-box"></span> Productive Area</span>
  </div>

  <!-- Next Steps -->
  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">Notes for Next Time</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Find #{session_num:02d} &mdash; Notes</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def species_checklist(page_of, total_pages):
    """Species checklist — common North American mushrooms to track"""
    species_pages = [
        [
            "Morel (Morchella)",
            "Chanterelle (Cantharellus)",
            "King Bolete (Boletus edulis)",
            "Chicken of the Woods (Laetiporus)",
            "Hen of the Woods (Grifola)",
            "Oyster Mushroom (Pleurotus)",
            "Lion's Mane (Hericium)",
            "Hedgehog (Hydnum)",
            "Black Trumpet (Craterellus)",
            "Giant Puffball (Calvatia)",
            "Shaggy Mane (Coprinus)",
            "Parasol (Macrolepiota)",
        ],
        [
            "Lobster Mushroom (Hypomyces)",
            "Wine Cap (Stropharia)",
            "Matsutake (Tricholoma)",
            "Wood Ear (Auricularia)",
            "Turkey Tail (Trametes)",
            "Cauliflower Mushroom (Sparassis)",
            "Beech Mushroom (Hypsizygus)",
            "Enoki (Flammulina)",
            "Dryad's Saddle (Polyporus)",
            "Fried Chicken Mushroom (Lyophyllum)",
            "Blewit (Lepista)",
            "King Trumpet (Pleurotus eryngii)",
        ],
        [
            "", "", "", "", "", "", "", "", "", "", "", "",
        ],
    ]
    species_list = species_pages[page_of - 1] if page_of <= len(species_pages) else species_pages[-1]

    rows = ""
    start_num = (page_of - 1) * 12 + 1
    for i, sp in enumerate(species_list):
        n = start_num + i
        if sp:
            rows += f'''<tr><td>{n}</td><td style="font-style:italic;">{sp}</td><td></td><td></td><td><span class="check-box"></span></td></tr>\n'''
        else:
            rows += f'''<tr><td>{n}</td><td></td><td></td><td></td><td><span class="check-box"></span></td></tr>\n'''

    return f'''
<!-- Page {pn()}: Species Checklist -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Species Checklist</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Species Checklist</div>
  <div class="page-subtitle">Build your life list of finds</div>

  <table class="data-table species-list" style="font-size: 7.5pt;">
    <tr>
      <th style="width:22px;">#</th>
      <th>Species</th>
      <th style="width:65px;">First Found</th>
      <th style="width:50px;">Edible?</th>
      <th style="width:28px;">&#10003;</th>
    </tr>
    {rows}
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Add your own species as your knowledge grows. Edible? = Y / N / Unknown</div>

  <div class="page-footer">
    <span>Mushroom Foraging Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def location_log(page_of, total_pages):
    """Favorite foraging spots and location log"""
    return f'''
<!-- Page {pn()}: Location Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Foraging Spots</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Spot &amp; Location Log</div>
  <div class="page-subtitle">Your personal map of productive spots</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th style="width:90px;">Location Name</th>
      <th style="width:50px;">Habitat</th>
      <th style="width:50px;">Best Season</th>
      <th>Key Species &amp; Notes</th>
      <th style="width:28px;">&#10003;</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6A;">1</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6A;">2</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6A;">3</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6A;">4</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6A;">5</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6A;">6</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6A;">7</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6A;">8</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6A;">9</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#7A8B6A;">10</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Best Spot</div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #7A8B6A; text-transform: uppercase; min-width: 38px;">Name</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #7A8B6A; text-transform: uppercase; min-width: 38px;">Why</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
    <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 4px;">
      <span style="font-size: 7pt; font-weight: 700; color: #7A8B6A; text-transform: uppercase; min-width: 38px;">Best Find</span>
      <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Mushroom Foraging Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def equipment_kit():
    """Foraging kit and equipment page"""
    return f'''
<!-- Page {pn()}: Equipment & Kit -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Gear</span>
    <span class="sh-right">My Foraging Kit</span>
  </div>

  <div class="page-title">Foraging Kit &amp; Equipment</div>
  <div class="page-subtitle">What you carry matters</div>

  <div class="gear-card">
    <div class="gear-label">Baskets &amp; Bags</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Details</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Cutting &amp; Digging Tools</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Type</th><th>Details</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Field Guides &amp; References</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Title</th><th>Region</th><th>Notes</th></tr>
      <tr><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Navigation &amp; Safety</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Item</th><th>Type / Model</th><th>Spare?</th></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
    </table>
  </div>

  <div class="gear-card">
    <div class="gear-label">Other Essentials</div>
    <table class="data-table" style="font-size: 7pt;">
      <tr><th>Item</th><th>Purpose</th><th>Packed?</th></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
      <tr><td></td><td></td><td style="text-align:center;"></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Mushroom Foraging Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def foraging_favorites():
    """Year-in-review and favorites page"""
    return f'''
<!-- Page {pn()}: Favorites Summary -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Favorites &amp; Stats</span>
    <span class="sh-right">Your Foraging Year in Review</span>
  </div>

  <div class="page-title">Foraging Year in Review</div>
  <div class="page-subtitle">Fill in at the end of your foraging season</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Species Found</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Forays Made</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
    <div class="stat-card" style="padding: 12px 6px;">
      <div class="stat-label">Spots Explored</div>
      <div class="stat-value" style="font-size: 18pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">My Top 5 Finds</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Species</th>
      <th style="width:55px;">Location</th>
      <th style="width:35px;">Date</th>
      <th>Why It Was Special</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Personal Milestones</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th>Category</th>
      <th>Achievement</th>
      <th>Notes</th>
    </tr>
    <tr><td style="font-weight:700;color:#141A12;">Best Season</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#141A12;">Best New Spot</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#141A12;">First New Species</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#141A12;">Biggest Haul</td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#141A12;">Hardest Identification</td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #141A12; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">What I Want to Find Next Season</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Mushroom Foraging Journal</span>
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

  <div class="page-title">Foraging Notes</div>
  <div class="page-subtitle">Species to research, recipes, and reminders</div>

  {lines}

  <div class="page-footer">
    <span>Mushroom Foraging Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def sketch_page():
    """Dot grid page for sketching specimens and location maps"""
    return f'''
<!-- Page {pn()}: Sketch -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Sketch Pad</span>
    <span class="sh-right">Specimen Drawings &amp; Spot Maps</span>
  </div>

  <div class="page-title">Sketch Pad</div>
  <div class="page-subtitle">Draw specimens, map locations, plan forays</div>

  <div class="dot-grid" style="width: 100%; height: 6.5in; border-radius: 4px;"></div>

  <div class="page-footer">
    <span>Mushroom Foraging Journal</span>
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
    pages.append(mushroom_anatomy())               # 4: Mushroom anatomy
    pages.append(habitat_guide())                  # 5: Habitat guide
    pages.append(foraging_safety())                # 6: Foraging safety
    pages.append(seasonal_calendar())              # 7: Seasonal calendar

    # ---- Section 1: Foraging Logs ----
    pages.append(divider_section(1, "One", "Foraging Logs", "40 finds &mdash; your foraging journey"))
    NUM_SESSIONS = 40
    for i in range(1, NUM_SESSIONS + 1):
        pages.append(foraging_log_left(i))          # Left page: details
        pages.append(foraging_log_right(i))         # Right page: notes

    # ---- Section 2: Species Checklist ----
    pages.append(divider_section(2, "Two", "Species Checklist", "Build your life list"))
    pages.append(species_checklist(1, 3))
    pages.append(species_checklist(2, 3))
    pages.append(species_checklist(3, 3))

    # ---- Section 3: Spot & Location Log ----
    pages.append(divider_section(3, "Three", "Spot &amp; Location Log", "Your personal foraging map"))
    pages.append(location_log(1, 3))
    pages.append(location_log(2, 3))
    pages.append(location_log(3, 3))

    # ---- Section 4: Equipment & Kit ----
    pages.append(divider_section(4, "Four", "Foraging Kit &amp; Equipment", "What you carry into the woods"))
    pages.append(equipment_kit())

    # ---- Section 5: Seasonal Favorites ----
    pages.append(divider_section(5, "Five", "Seasonal Favorites", "Your foraging year in review"))
    pages.append(foraging_favorites())
    pages.append(sketch_page())

    # ---- Section 6: Notes ----
    pages.append(divider_section(6, "Six", "Notes", "Species to research, recipes, and reminders"))
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
    print(f"  Reference (how-to, anatomy, habitat, safety, seasonal): 5")
    print(f"  Section dividers: 6")
    print(f"  Foraging logs ({NUM_SESSIONS} sessions x 2 pages): {NUM_SESSIONS * 2}")
    print(f"  Species checklist: 2")
    print(f"  Location log: 2")
    print(f"  Equipment & kit: 1")
    print(f"  Favorites summary: 1")
    print(f"  Sketch page: 1")
    print(f"  Notes pages: 10")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
