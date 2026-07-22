#!/usr/bin/env python3
"""
Fishing Log Book — KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Generates a print-ready full wrap cover (back + spine + front) as
standalone HTML. Export with Chrome headless to PDF.

Trim: 6" x 9"
Pages: 133 (cream paper)
Spine: 133 × 0.0025 = 0.3325"
Bleed: 0.125" all outer edges
Full cover: 12.5825 x 9.25 in
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "fishing_log_book_cover_V1.0.html")

# KDP cover specs
TRIM_W = 6.0          # inches
TRIM_H = 9.0
PAGES = 133
SPINE = PAGES * 0.0025   # cream paper = 0.3325"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.5825"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors — Fishing / Deep Water theme
C_DEEP   = "#062430"    # darkest water
C_DARK   = "#0D3B4C"    # deep water
C_MED    = "#164E63"    # steel water
C_BLUE   = "#1B6B8C"    # mid blue
C_STEEL  = "#2A6F97"    # steel blue
C_GOLD   = "#D4A017"    # gold / amber
C_GOLD_L = "#F0CE6A"    # light gold
C_FOAM   = "#F0F5F7"    # foam white
C_SAND   = "#E8D5A0"    # sand
C_WHITE  = "#ffffff"
C_DARK2  = "#1A1A1A"


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
  background: linear-gradient(165deg, {C_DEEP} 0%, {C_DARK} 40%, {C_MED} 100%);
  padding: 0.55in 0.5in 0.45in {BLEED}in;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
}}

/* Water ripple texture */
.back-cover::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 30px 8px at 15% 25%, {C_WHITE}, transparent),
    radial-gradient(ellipse 24px 6px at 80% 15%, {C_WHITE}, transparent),
    radial-gradient(ellipse 28px 7px at 70% 70%, {C_WHITE}, transparent),
    radial-gradient(ellipse 20px 6px at 25% 80%, {C_WHITE}, transparent),
    radial-gradient(ellipse 18px 5px at 50% 50%, {C_WHITE}, transparent),
    radial-gradient(ellipse 22px 6px at 10% 60%, {C_WHITE}, transparent);
}}

/* Decorative circle */
.back-cover::after {{
  content: '';
  position: absolute;
  top: -0.3in; right: -0.3in;
  width: 1.2in; height: 1.2in;
  border-radius: 50%;
  background: rgba(212, 160, 23, 0.08);
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
  background: {C_GOLD};
  border-radius: 50%;
}}

.back-bottom {{
  margin-top: auto;
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
  color: {C_GOLD};
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
  background: linear-gradient(180deg, {C_DEEP} 0%, {C_DARK} 50%, {C_DEEP} 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 0.6in 0;
  position: relative;
}}

/* Spine ripple texture */
.spine::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.03;
  background-image:
    radial-gradient(ellipse 10px 4px at 50% 20%, {C_WHITE}, transparent),
    radial-gradient(ellipse 10px 4px at 50% 50%, {C_WHITE}, transparent),
    radial-gradient(ellipse 10px 4px at 50% 80%, {C_WHITE}, transparent);
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
  color: {C_GOLD};
  font-size: 6pt;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  position: relative;
  z-index: 2;
}}

.spine-icon {{
  width: 0.35in;
  height: 0.35in;
  position: relative;
  z-index: 2;
}}
/* Spine hook icon */
.spine-icon::before {{
  content: '';
  position: absolute;
  top: 0; left: 50%;
  transform: translateX(-50%);
  width: 1.5px;
  height: 0.18in;
  background: {C_GOLD};
}}
.spine-icon::after {{
  content: '';
  position: absolute;
  top: 0.15in; left: 50%;
  transform: translateX(-50%);
  width: 0.14in;
  height: 0.14in;
  border: 1.5px solid {C_GOLD};
  border-top: none;
  border-left: none;
  border-radius: 0 0 50% 0;
}}

/* ============ FRONT COVER ============ */
.front-cover {{
  width: {TRIM_W + BLEED:.4f}in;
  height: {COVER_H:.4f}in;
  background: linear-gradient(165deg, {C_DEEP} 0%, {C_DARK} 25%, {C_MED} 55%, {C_DARK} 85%, {C_DEEP} 100%);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: {BLEED}in {BLEED}in {BLEED}in 0;
}}

/* Water ripple texture on front */
.front-cover::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 40px 10px at 15% 25%, {C_WHITE}, transparent),
    radial-gradient(ellipse 34px 8px at 80% 15%, {C_WHITE}, transparent),
    radial-gradient(ellipse 38px 9px at 70% 70%, {C_WHITE}, transparent),
    radial-gradient(ellipse 28px 8px at 25% 80%, {C_WHITE}, transparent),
    radial-gradient(ellipse 24px 7px at 50% 50%, {C_WHITE}, transparent),
    radial-gradient(ellipse 30px 8px at 10% 60%, {C_WHITE}, transparent),
    radial-gradient(ellipse 22px 7px at 90% 45%, {C_WHITE}, transparent),
    radial-gradient(ellipse 20px 6px at 40% 90%, {C_WHITE}, transparent),
    radial-gradient(ellipse 18px 5px at 60% 35%, {C_WHITE}, transparent);
}}

/* ============ CSS FISH ============ */
.fish-wrap {{
  width: 160px; height: 80px;
  position: relative;
  margin: 0 auto 25px;
  z-index: 5;
}}
.fish-body {{
  width: 115px; height: 48px;
  background: {C_GOLD};
  border-radius: 50%;
  position: absolute;
  top: 16px; left: 18px;
  box-shadow: 2px 2px 10px rgba(0,0,0,0.45),
              inset -8px -4px 10px rgba(0,0,0,0.18),
              inset 8px 4px 10px rgba(255,255,255,0.1);
}}
.fish-belly {{
  width: 92px; height: 16px;
  background: {C_GOLD_L};
  border-radius: 50%;
  position: absolute;
  top: 40px; left: 28px;
  opacity: 0.6;
}}
.fish-head {{
  width: 48px; height: 42px;
  background: #C89010;
  border-radius: 50%;
  position: absolute;
  top: 18px; left: 72px;
  opacity: 0.5;
}}
.fish-tail {{
  width: 0; height: 0;
  border-right: 32px solid {C_GOLD};
  border-top: 23px solid transparent;
  border-bottom: 23px solid transparent;
  position: absolute;
  top: 17px; left: -12px;
  filter: drop-shadow(-2px 1px 4px rgba(0,0,0,0.3));
}}
.fish-dorsal {{
  width: 0; height: 0;
  border-bottom: 18px solid #B8860B;
  border-left: 10px solid transparent;
  border-right: 20px solid transparent;
  position: absolute;
  top: 4px; left: 55px;
}}
.fish-pectoral {{
  width: 22px; height: 11px;
  background: #B8860B;
  border-radius: 50% 50% 50% 0;
  position: absolute;
  top: 42px; left: 68px;
  transform: rotate(15deg);
  opacity: 0.8;
}}
.fish-eye {{
  width: 7px; height: 7px;
  background: {C_DARK2};
  border-radius: 50%;
  position: absolute;
  top: 28px; left: 104px;
}}
.fish-eye::after {{
  content: "";
  width: 2.5px; height: 2.5px;
  background: white;
  border-radius: 50%;
  position: absolute;
  top: 1px; left: 3px;
}}
.fish-gill {{
  width: 2px; height: 32px;
  background: #B8860B;
  position: absolute;
  top: 22px; left: 76px;
  border-radius: 1px;
  transform: rotate(5deg);
  opacity: 0.4;
}}

/* Hook decoration */
.hook-deco {{
  width: 34px; height: 50px;
  position: absolute;
  top: 120px; left: 50%;
  transform: translateX(-50%);
  opacity: 0.12;
  z-index: 3;
}}
.hook-deco::before {{
  content: "";
  width: 2px; height: 28px;
  background: {C_GOLD};
  position: absolute;
  top: 0; left: 16px;
  border-radius: 1px;
}}
.hook-deco::after {{
  content: "";
  width: 20px; height: 20px;
  border: 2px solid {C_GOLD};
  border-top: none;
  border-left: none;
  border-radius: 0 0 50% 0;
  position: absolute;
  top: 24px; left: 16px;
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
  background: {C_GOLD};
  margin: 16px auto;
}}

.subtitle {{
  font-size: 12pt;
  color: #A8C8D8;
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
  border: 1px solid rgba(212,160,23,0.4);
  color: {C_GOLD};
  font-size: 7.5pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 10px;
  border-radius: 3px;
  text-transform: uppercase;
}}

.tagline {{
  font-size: 9pt;
  color: #A8C8D8;
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
  color: {C_GOLD};
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
  <title>Fishing Log Book — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every cast tells a story.</strong>
        From the first light on the water to the last catch of the day,
        this log book helps you capture the details that turn good days
        into great seasons.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>52 two-page trip logs with catch details and conditions</li>
        <li>60-species life list for freshwater and saltwater</li>
        <li>Knot guide, species reference, and seasonal calendar</li>
        <li>Tackle and lure inventory pages</li>
        <li>Favorite spots log and sketch pages for maps</li>
        <li>Season summary with personal bests tracking</li>
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
    <div class="spine-text">Fishing Log Book</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Fish illustration -->
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

    <div class="hook-deco"></div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Fishing<br>Log Book</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Track Every Catch,<br>Every Trip, Every Story</div>
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
