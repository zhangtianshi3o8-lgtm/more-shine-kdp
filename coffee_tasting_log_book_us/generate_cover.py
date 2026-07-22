#!/usr/bin/env python3
"""
Coffee Tasting Log Book — KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Generates a print-ready full wrap cover (back + spine + front) as
standalone HTML. Export with Chrome headless to PDF.

Trim: 6" x 9"
Pages: 112 (cream paper)
Spine: 112 x 0.0025 = 0.28"
Bleed: 0.125" all outer edges
Full cover: 12.53 x 9.25 in
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "coffee_tasting_log_book_cover_V1.0.html")

# KDP cover specs
TRIM_W = 6.0          # inches
TRIM_H = 9.0
PAGES = 112
SPINE = PAGES * 0.0025   # cream paper = 0.28"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.53"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors — Coffee / Espresso theme
C_DARKEST = "#1E1008"    # darkest espresso
C_DARK    = "#2A1810"    # dark roast
C_ESPRESSO = "#3B2417"   # espresso
C_BREW    = "#4A3020"    # brewed coffee
C_COFFEE  = "#6F4E37"    # coffee brown
C_MOCHA   = "#8B5E3C"    # mocha
C_CARAMEL = "#C8A041"    # caramel gold
C_GOLD_L  = "#D4B896"    # light gold / latte art
C_CREAM   = "#FAF6F0"    # cream
C_FOAM    = "#F5EDE3"    # foam
C_WHITE   = "#ffffff"


CSS = f"""
<style>
@page {{ size: {COVER_W:.4f}in {COVER_H:.4f}in; margin: 0; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}

body {{
  font-family: Georgia, "Iowan Old Style", "Palatino", serif;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}

.cover-wrap {{
  width: {COVER_W:.4f}in;
  height: {COVER_H:.4f}in;
  position: relative;
  display: flex;
}}

/* ============ BACK COVER ============ */
.back-cover {{
  width: {TRIM_W + BLEED:.4f}in;
  height: {COVER_H:.4f}in;
  background: linear-gradient(165deg, {C_DARKEST} 0%, {C_DARK} 40%, {C_ESPRESSO} 100%);
  padding: 0.75in 0.5in 0.45in 0.5in;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  overflow: hidden;
}}

/* Coffee bean texture */
.back-cover::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 24px 14px at 15% 25%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 22px 13px at 80% 15%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 26px 15px at 70% 70%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 18px 11px at 50% 50%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 22px 13px at 10% 60%, {C_CARAMEL}, transparent);
}}

/* Decorative circle */
.back-cover::after {{
  content: '';
  position: absolute;
  top: -0.3in; right: -0.3in;
  width: 1.2in; height: 1.2in;
  border-radius: 50%;
  background: rgba(200, 160, 65, 0.08);
}}

.back-text {{
  color: rgba(255,255,255,0.92);
  font-size: 9pt;
  line-height: 1.6;
  position: relative;
  z-index: 2;
}}
.back-text .blurb {{
  font-style: italic;
  margin-bottom: 14px;
  font-size: 9.5pt;
  line-height: 1.55;
}}
.back-text .blurb strong {{
  color: {C_GOLD_L};
  font-style: normal;
}}

.back-features {{
  list-style: none;
  padding: 0;
}}
.back-features li {{
  font-size: 8pt;
  color: rgba(255,255,255,0.82);
  padding: 3px 0;
  padding-left: 16px;
  position: relative;
  line-height: 1.4;
}}
.back-features li::before {{
  content: '';
  position: absolute;
  left: 0;
  top: 5px;
  width: 5px;
  height: 5px;
  background: {C_CARAMEL};
  border-radius: 50%;
}}

.back-bottom {{
  padding-bottom: 0.15in;
  position: relative;
  z-index: 2;
}}

.barcode-area {{
  width: 2in;
  height: 1.2in;
  background: white;
  margin-left: auto;
  margin-right: 0;
  border-radius: 2px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 6pt;
  color: #ccc;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}}

.back-logo {{
  text-align: center;
  color: {C_CARAMEL};
  font-size: 8pt;
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  font-weight: 700;
  padding-top: 8px;
  margin-top: 6px;
  border-top: 1px solid rgba(255,255,255,0.15);
}}

/* ============ SPINE ============ */
.spine {{
  width: {SPINE:.4f}in;
  height: {COVER_H:.4f}in;
  background: linear-gradient(180deg, {C_DARKEST} 0%, {C_DARK} 50%, {C_DARKEST} 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 0.6in 0;
  position: relative;
}}

/* Spine texture */
.spine::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.03;
  background-image:
    radial-gradient(ellipse 10px 6px at 50% 20%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 50%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 80%, {C_CARAMEL}, transparent);
}}

.spine-text {{
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  color: rgba(255,255,255,0.95);
  font-size: 8pt;
  font-weight: bold;
  letter-spacing: 2px;
  text-transform: uppercase;
  white-space: nowrap;
  line-height: 1;
  position: relative;
  z-index: 2;
}}

.spine-author {{
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  color: {C_CARAMEL};
  font-size: 6pt;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  position: relative;
  z-index: 2;
}}

/* ============ FRONT COVER ============ */
.front-cover {{
  width: {TRIM_W + BLEED:.4f}in;
  height: {COVER_H:.4f}in;
  background: linear-gradient(165deg, {C_DARKEST} 0%, {C_DARK} 25%, {C_ESPRESSO} 55%, {C_DARK} 85%, {C_DARKEST} 100%);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: {BLEED}in 0 {BLEED}in {BLEED}in;
}}

/* Coffee bean texture on front */
.front-cover::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 40px 24px at 15% 25%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 34px 20px at 80% 15%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 38px 22px at 70% 70%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 28px 18px at 25% 80%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 24px 15px at 50% 50%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 30px 18px at 10% 60%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 22px 14px at 90% 45%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 20px 12px at 40% 90%, {C_CARAMEL}, transparent),
    radial-gradient(ellipse 18px 11px at 60% 35%, {C_CARAMEL}, transparent);
}}

/* ============ CSS COFFEE CUP ============ */
.cup-wrap {{
  width: 170px; height: 140px;
  position: relative;
  margin: 0 auto 28px;
  z-index: 5;
}}

/* Steam */
.steam1 {{
  width: 4px; height: 40px;
  background: linear-gradient(180deg, transparent, rgba(250,246,240,0.35), transparent);
  position: absolute;
  top: -20px; left: 45px;
  border-radius: 50%;
  transform: rotate(-12deg);
}}
.steam2 {{
  width: 4px; height: 48px;
  background: linear-gradient(180deg, transparent, rgba(250,246,240,0.28), transparent);
  position: absolute;
  top: -26px; left: 75px;
  border-radius: 50%;
  transform: rotate(10deg);
}}
.steam3 {{
  width: 4px; height: 36px;
  background: linear-gradient(180deg, transparent, rgba(250,246,240,0.22), transparent);
  position: absolute;
  top: -16px; left: 100px;
  border-radius: 50%;
  transform: rotate(-6deg);
}}

/* Cup body — trapezoid */
.cup-body {{
  width: 130px; height: 90px;
  background: linear-gradient(180deg, {C_CREAM} 0%, {C_FOAM} 50%, #E8DCC8 100%);
  position: absolute;
  top: 20px; left: 10px;
  border-radius: 0 0 16px 16px;
  clip-path: polygon(8% 0, 92% 0, 82% 100%, 18% 100%);
  box-shadow: 3px 3px 12px rgba(0,0,0,0.45);
}}

/* Cup rim */
.cup-rim {{
  width: 130px; height: 20px;
  background: {C_ESPRESSO};
  border-radius: 50%;
  position: absolute;
  top: 14px; left: 10px;
  border: 2.5px solid {C_CREAM};
  box-shadow: 0 2px 8px rgba(0,0,0,0.35);
  z-index: 3;
}}

/* Coffee surface */
.cup-coffee {{
  width: 116px; height: 15px;
  background: linear-gradient(180deg, {C_COFFEE} 0%, {C_ESPRESSO} 100%);
  border-radius: 50%;
  position: absolute;
  top: 17px; left: 17px;
  z-index: 4;
}}

/* Crema swirl */
.cup-crema {{
  width: 52px; height: 7px;
  background: rgba(200,160,65,0.5);
  border-radius: 50%;
  position: absolute;
  top: 20px; left: 40px;
  transform: rotate(-15deg);
  z-index: 5;
}}

/* Cup handle */
.cup-handle {{
  width: 36px; height: 42px;
  border: 6px solid {C_CREAM};
  border-left: none;
  border-radius: 0 50% 50% 0;
  position: absolute;
  top: 38px; left: 130px;
  box-shadow: 2px 2px 8px rgba(0,0,0,0.35);
}}

/* Saucer */
.cup-saucer {{
  width: 160px; height: 16px;
  background: linear-gradient(180deg, {C_FOAM} 0%, #E0D2BC 100%);
  border-radius: 50%;
  position: absolute;
  top: 108px; left: -5px;
  box-shadow: 2px 4px 10px rgba(0,0,0,0.45);
}}

/* Saucer rim accent */
.cup-saucer::before {{
  content: '';
  position: absolute;
  top: 3px; left: 50%;
  transform: translateX(-50%);
  width: 130px; height: 8px;
  background: rgba(0,0,0,0.06);
  border-radius: 50%;
}}

/* ============ TITLE ============ */
.title-block {{
  position: relative;
  z-index: 5;
  padding: 0 0.5in;
}}

.main-title {{
  font-family: Georgia, serif;
  font-size: 34pt;
  font-weight: 700;
  color: {C_WHITE};
  line-height: 1.12;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.55);
}}

.accent-bar {{
  width: 120px; height: 2.5px;
  background: {C_CARAMEL};
  margin: 16px auto;
}}

.subtitle {{
  font-size: 12pt;
  color: {C_GOLD_L};
  font-style: italic;
  line-height: 1.5;
  margin-bottom: 22px;
}}

.features {{
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-bottom: 22px;
  flex-wrap: wrap;
}}

.feature-badge {{
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(200,160,65,0.4);
  color: {C_CARAMEL};
  font-size: 7.5pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 10px;
  border-radius: 3px;
  text-transform: uppercase;
}}

.tagline {{
  font-size: 9pt;
  color: {C_GOLD_L};
  letter-spacing: 2pt;
  text-transform: uppercase;
  margin-top: 8px;
}}

.publisher {{
  position: absolute;
  bottom: 0.5in;
  left: 0; right: 0;
  text-align: center;
  font-size: 9.5pt;
  color: {C_CARAMEL};
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  font-weight: 700;
  z-index: 5;
}}

/* Screen-only border */
@media screen {{
  .cover-wrap {{ border: 1px solid #ccc; }}
}}
</style>
"""


def generate(output_path=OUTPUT_FILE):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Coffee Tasting Log Book — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every cup has a story.</strong>
        From the first aroma to the last sip, this log book helps you
        capture the flavors, origins, and brewing details that turn a
        daily habit into a lifelong passion.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>40 two-page tasting logs with full brewing details</li>
        <li>Coffee flavor wheel with 8 categories and 50+ notes</li>
        <li>Brewing methods guide and tasting terminology</li>
        <li>Coffee growing regions reference (12 origins)</li>
        <li>Bean collection and roaster inventory pages</li>
        <li>32-origin coffee belt checklist</li>
        <li>Year-in-review favorites and personal discoveries</li>
        <li>Large 6" x 9" format &mdash; easy to write in</li>
      </ul>
    </div>
    <div class="back-bottom">
      <div class="barcode-area">ISBN Barcode Area</div>
      <div class="back-logo">More Shine Press</div>
    </div>
  </div>

  <!-- ============ SPINE ============ -->
  <div class="spine">
    <div class="spine-author">More Shine Press</div>
    <div class="spine-text">Coffee Tasting Log Book</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Coffee cup illustration -->
    <div class="cup-wrap">
      <div class="steam1"></div>
      <div class="steam2"></div>
      <div class="steam3"></div>
      <div class="cup-saucer"></div>
      <div class="cup-body"></div>
      <div class="cup-handle"></div>
      <div class="cup-rim"></div>
      <div class="cup-coffee"></div>
      <div class="cup-crema"></div>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Coffee Tasting<br>Log Book</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Track Every Cup,<br>Every Origin, Every Flavor</div>
      <div class="features">
        <span class="feature-badge">40 Tasting Sessions</span>
        <span class="feature-badge">Flavor Wheel</span>
        <span class="feature-badge">Brewing Tracker</span>
        <span class="feature-badge">Bean Inventory</span>
      </div>
      <div class="tagline">For Coffee Lovers &amp; Home Brewers</div>
    </div>

    <div class="publisher">More Shine Press</div>
  </div>

</div>
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    return output_path


if __name__ == "__main__":
    path = generate()
    print(f"[OK] Cover generated: {path}")
    print(f"     Full cover: {COVER_W:.4f} x {COVER_H:.4f} in")
    print(f"     Spine: {SPINE:.4f} in ({PAGES} pages, cream paper)")
    print(f"     At 300 DPI: {COVER_W*300:.0f} x {COVER_H*300:.0f} px")
