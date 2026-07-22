#!/usr/bin/env python3
"""
Beekeeping Log Book — KDP Full Wrap Cover Generator
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
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "beekeeping_log_book_cover_V1.0.html")

# KDP cover specs
TRIM_W = 6.0          # inches
TRIM_H = 9.0
PAGES = 112
SPINE = PAGES * 0.0025   # cream paper = 0.28"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.53"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors — Honey / Forest / Sage theme (quiet luxury aesthetic)
C_CHARCOAL = "#141A12"   # near-black forest green
C_DARK     = "#1E2820"   # dark forest
C_BROWN    = "#1A2818"   # dark green-brown
C_AMBER_D  = "#2A3828"   # mid green
C_AMBER    = "#5A7042"   # sage green
C_COPPER   = "#C4A04A"   # honey gold (replaces copper)
C_SAGE_L   = "#7A8B5A"   # light sage
C_GOLD     = "#C4A04A"   # muted gold
C_GOLD_L   = "#D4B896"   # light gold / champagne
C_CREAM    = "#FAF6F0"   # warm cream
C_WHITE    = "#ffffff"


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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 40%, {C_BROWN} 100%);
  padding: 0.75in 0.5in 0.45in 0.5in;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  overflow: hidden;
}}

/* Subtle honey-gold texture */
.back-cover::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 24px 14px at 15% 25%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 13px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 26px 15px at 70% 70%, {C_GOLD}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 18px 11px at 50% 50%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 13px at 10% 60%, {C_GOLD}, transparent);
}}

/* Decorative circle */
.back-cover::after {{
  content: '';
  position: absolute;
  top: -0.3in; right: -0.3in;
  width: 1.2in; height: 1.2in;
  border-radius: 50%;
  background: rgba(196, 160, 74, 0.08);
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
  background: linear-gradient(180deg, {C_CHARCOAL} 0%, {C_DARK} 50%, {C_CHARCOAL} 100%);
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
    radial-gradient(ellipse 10px 6px at 50% 20%, {C_GOLD}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 50%, {C_GOLD}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 80%, {C_GOLD}, transparent);
}}

.spine-text {{
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  color: rgba(255,255,255,0.95);
  font-size: 7pt;
  font-weight: bold;
  letter-spacing: 1.5px;
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
  font-size: 5.5pt;
  letter-spacing: 1px;
  text-transform: uppercase;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  position: relative;
  z-index: 2;
}}

/* ============ FRONT COVER ============ */
.front-cover {{
  width: {TRIM_W + BLEED:.4f}in;
  height: {COVER_H:.4f}in;
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 25%, {C_AMBER_D} 55%, {C_DARK} 85%, {C_CHARCOAL} 100%);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: {BLEED}in {BLEED}in {BLEED}in {BLEED}in;
}}

/* Subtle honey-gold texture on front */
.front-cover::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 40px 24px at 15% 25%, {C_GOLD}, transparent),
    radial-gradient(ellipse 34px 20px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 38px 22px at 70% 70%, {C_GOLD}, transparent),
    radial-gradient(ellipse 28px 18px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 24px 15px at 50% 50%, {C_GOLD}, transparent),
    radial-gradient(ellipse 30px 18px at 10% 60%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 14px at 90% 45%, {C_GOLD}, transparent),
    radial-gradient(ellipse 20px 12px at 40% 90%, {C_GOLD}, transparent),
    radial-gradient(ellipse 18px 11px at 60% 35%, {C_GOLD}, transparent);
}}

/* ============ HONEYCOMB (SVG) ============ */
.glass-wrap {{
  width: 130px; height: 160px;
  position: relative;
  margin: 0 auto 24px;
  z-index: 5;
}}

/* ============ TITLE ============ */
.title-block {{
  position: relative;
  z-index: 5;
  padding: 0 0.5in;
}}

.main-title {{
  font-family: Georgia, serif;
  font-size: 32pt;
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
  border: 1px solid rgba(196,160,74,0.4);
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
  <title>Beekeeping Log Book — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every hive tells a story.</strong>
        From the first spring inspection to the fall honey harvest,
        your beekeeping journey deserves to be documented with care.
        This journal gives you the structure to capture every inspection
        &mdash; every brood pattern, every nectar flow, every season of growth.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>40 two-page hive inspection spreads</li>
        <li>Hive anatomy and components guide</li>
        <li>Seasonal beekeeping calendar</li>
        <li>Safety rules and best practices</li>
        <li>Nectar and pollen plant checklist</li>
        <li>Honey harvest and year-in-review log</li>
        <li>Apiary setup and equipment guide</li>
        <li>Compact 6&quot;&times;9&quot; format for the bee yard</li>
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
    <div class="spine-text">Beekeeping Log Book &mdash; More Shine Press</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Honeycomb cluster + bee illustration (SVG line art) -->
    <div class="glass-wrap">
      <svg viewBox="0 0 130 160" width="130" height="160" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="honeyGlow" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_GOLD}" stop-opacity="0.18"/>
            <stop offset="100%" stop-color="{C_AMBER}" stop-opacity="0.10"/>
          </linearGradient>
        </defs>

        <!-- ===== INTERLOCKING HONEYCOMB HEXAGONS (pointy-top, r=24) ===== -->
        <!-- Hex cluster: D(top) A(left-mid) B(right-mid) C(bottom) -->
        <!-- Centers: D(55,31) A(33,70) B(78,70) C(55,109) -->

        <!-- Hex A (left-middle): center (33,70) -->
        <polygon points="33,46 53.9,58 53.9,82 33,94 12.1,82 12.1,58"
                 stroke="{C_GOLD}" stroke-width="1.6" fill="url(#honeyGlow)" stroke-linejoin="round"/>

        <!-- Hex B (right-middle): center (78,70) -->
        <polygon points="78,46 98.9,58 98.9,82 78,94 57.1,82 57.1,58"
                 stroke="{C_GOLD}" stroke-width="1.6" fill="url(#honeyGlow)" stroke-linejoin="round"/>

        <!-- Hex D (top): center (55.5,31) -->
        <polygon points="55.5,7 76.4,19 76.4,43 55.5,55 34.6,43 34.6,19"
                 stroke="{C_GOLD}" stroke-width="1.6" fill="url(#honeyGlow)" stroke-linejoin="round"/>

        <!-- Hex C (bottom): center (55.5,109) -->
        <polygon points="55.5,85 76.4,97 76.4,121 55.5,133 34.6,121 34.6,97"
                 stroke="{C_GOLD}" stroke-width="1.6" fill="url(#honeyGlow)" stroke-linejoin="round"/>

        <!-- Inner hex outline accents (subtle) -->
        <polygon points="55.5,93 67.8,100 67.8,114 55.5,121 43.2,114 43.2,100"
                 stroke="rgba(212,184,150,0.35)" stroke-width="0.8" fill="none" stroke-linejoin="round"/>

        <!-- ===== STYLIZED BEE (centered in bottom hex C, ~55.5,109) ===== -->
        <g transform="translate(55.5,109)">

          <!-- Left wing -->
          <ellipse cx="-9" cy="-10" rx="13" ry="7"
                   transform="rotate(-25 -9 -10)"
                   fill="rgba(212,184,150,0.22)"
                   stroke="rgba(212,184,150,0.5)" stroke-width="0.8"/>
          <!-- Right wing -->
          <ellipse cx="9" cy="-10" rx="13" ry="7"
                   transform="rotate(25 9 -10)"
                   fill="rgba(212,184,150,0.22)"
                   stroke="rgba(212,184,150,0.5)" stroke-width="0.8"/>

          <!-- Body (oval, honey-gold fill) -->
          <ellipse cx="0" cy="2" rx="12" ry="7.5"
                   fill="{C_GOLD}" stroke="rgba(20,26,18,0.6)" stroke-width="0.8"/>

          <!-- Body stripes (dark) -->
          <path d="M -3.5 -5 Q -5 2 -3.5 9" stroke="rgba(20,26,18,0.8)" stroke-width="2" fill="none" stroke-linecap="round"/>
          <path d="M 1 -5.5 Q -0.5 2 1 9.5" stroke="rgba(20,26,18,0.8)" stroke-width="2" fill="none" stroke-linecap="round"/>
          <path d="M 5.5 -4.5 Q 4 2 5.5 8.5" stroke="rgba(20,26,18,0.8)" stroke-width="1.6" fill="none" stroke-linecap="round"/>

          <!-- Head -->
          <circle cx="-11" cy="2" r="4.5"
                  fill="{C_BROWN}" stroke="{C_GOLD}" stroke-width="0.6"/>

          <!-- Antennae -->
          <path d="M -13 -1 Q -17 -6 -15 -10" stroke="{C_GOLD_L}" stroke-width="0.8" fill="none" stroke-linecap="round"/>
          <path d="M -11 -2 Q -12 -7 -9 -10" stroke="{C_GOLD_L}" stroke-width="0.8" fill="none" stroke-linecap="round"/>

          <!-- Tiny eye -->
          <circle cx="-12.5" cy="1" r="0.8" fill="rgba(255,255,255,0.7)"/>

        </g>

      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Beekeeping<br>Log Book</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Track Every Hive,<br>Every Harvest, Every Season</div>
      <div class="features">
        <span class="feature-badge">40 Hive Inspections</span>
        <span class="feature-badge">Hive Health Tracker</span>
        <span class="feature-badge">Honey Harvest Log</span>
        <span class="feature-badge">Seasonal Calendar</span>
      </div>
      <div class="tagline">For Beekeepers &amp; Apiarists</div>
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
