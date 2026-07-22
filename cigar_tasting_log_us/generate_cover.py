#!/usr/bin/env python3
"""
Cigar Tasting Log — KDP Full Wrap Cover Generator
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
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "cigar_tasting_log_cover_V1.0.html")

# KDP cover specs
TRIM_W = 6.0          # inches
TRIM_H = 9.0
PAGES = 112
SPINE = PAGES * 0.0025   # cream paper = 0.28"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.53"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors — Tobacco / Brown / Copper theme (quiet luxury aesthetic)
C_TOBACCO_DARK   = "#1A130A"   # near-black tobacco dark
C_WARM_DARK      = "#251A0E"   # warm dark tobacco
C_LEAF_DARK      = "#2E2415"   # dark tobacco leaf
C_EARTH          = "#4A3618"   # dark earth
C_TOBACCO        = "#6B4A20"   # tobacco brown
C_TOBACCO_COPPER = "#9A6B3A"   # tobacco copper
C_TOBACCO_LIGHT  = "#B88740"   # lighter tobacco
C_GOLD           = "#C4A04A"   # muted gold
C_GOLD_L         = "#D4B896"   # light gold / champagne
C_CREAM          = "#FAF6F0"   # warm cream
C_WHITE          = "#ffffff"


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
  background: linear-gradient(165deg, {C_TOBACCO_DARK} 0%, {C_WARM_DARK} 40%, {C_LEAF_DARK} 100%);
  padding: 0.75in 0.5in 0.45in 0.5in;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  overflow: hidden;
}}

/* Subtle tobacco texture */
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
  background: linear-gradient(180deg, {C_TOBACCO_DARK} 0%, {C_WARM_DARK} 50%, {C_TOBACCO_DARK} 100%);
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

/* ============ FRONT COVER ============ */
.front-cover {{
  width: {TRIM_W + BLEED:.4f}in;
  height: {COVER_H:.4f}in;
  background: linear-gradient(165deg, {C_TOBACCO_DARK} 0%, {C_WARM_DARK} 25%, {C_EARTH} 55%, {C_WARM_DARK} 85%, {C_TOBACCO_DARK} 100%);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: {BLEED}in {BLEED}in {BLEED}in {BLEED}in;
}}

/* Subtle tobacco texture on front */
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

/* ============ CIGAR ILLUSTRATION (SVG) ============ */
.cigar-wrap {{
  width: 120px; height: 170px;
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
  <title>Cigar Tasting Log &mdash; Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every smoke tells a story.</strong>
        From the cedar and leather notes of an aged Maduro to the
        creamy caramel of a mild Connecticut wrapper, your cigar
        journey deserves to be documented with care. This journal
        gives you the structure to capture every smoke &mdash; every
        draw, every flavor note, every pairing.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>40 two-page tasting spreads</li>
        <li>Cigar flavor wheel with 8 categories</li>
        <li>12 cigar region reference guide</li>
        <li>Vitola (shape) and wrapper guide</li>
        <li>28-origin checklist for your journey</li>
        <li>Humidor inventory log</li>
        <li>Year-in-review favorites summary</li>
        <li>Compact 6&times;9&rdquo; format for shelf or bag</li>
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
    <div class="spine-text">Cigar Tasting Log</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Cigar illustration (SVG line art) -->
    <div class="cigar-wrap">
      <svg viewBox="0 0 120 170" width="120" height="170" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="leaf" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_TOBACCO_COPPER}" stop-opacity="0.92"/>
            <stop offset="60%" stop-color="{C_TOBACCO}" stop-opacity="0.95"/>
            <stop offset="100%" stop-color="{C_EARTH}" stop-opacity="0.98"/>
          </linearGradient>
          <linearGradient id="band" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_GOLD}"/>
            <stop offset="100%" stop-color="{C_TOBACCO_COPPER}"/>
          </linearGradient>
          <linearGradient id="cylShine" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="rgba(250,246,240,0)"/>
            <stop offset="30%" stop-color="rgba(250,246,240,0.16)"/>
            <stop offset="60%" stop-color="rgba(250,246,240,0.05)"/>
            <stop offset="100%" stop-color="rgba(250,246,240,0)"/>
          </linearGradient>
        </defs>

        <!-- Slight diagonal tilt for the whole cigar -->
        <g transform="rotate(-15 60 85)">

          <!-- Cigar body: rounded head (cap) at top, tapered foot at bottom -->
          <path d="M 47 33
                   Q 47 19 60 19
                   Q 73 19 73 33
                   L 73 138
                   L 68 153
                   L 52 153
                   L 47 138 Z"
                stroke="{C_GOLD}" stroke-width="1.8"
                fill="url(#leaf)" stroke-linejoin="round" stroke-linecap="round"/>

          <!-- Cylindrical sheen highlight across the body -->
          <path d="M 47 33
                   Q 47 19 60 19
                   Q 73 19 73 33
                   L 73 138
                   L 68 153
                   L 52 153
                   L 47 138 Z"
                stroke="none" fill="url(#cylShine)"/>

          <!-- Wrapper leaf veins (subtle gold strokes) -->
          <path d="M 51 35 Q 49 90 53 150"
                stroke="rgba(196,160,74,0.30)" stroke-width="0.8" fill="none" stroke-linecap="round"/>
          <path d="M 60 21 L 60 150"
                stroke="rgba(196,160,74,0.22)" stroke-width="0.8" fill="none" stroke-linecap="round"/>
          <path d="M 69 35 Q 71 90 67 150"
                stroke="rgba(196,160,74,0.30)" stroke-width="0.8" fill="none" stroke-linecap="round"/>

          <!-- Cap seam line just below the rounded head -->
          <path d="M 47 33 Q 60 40 73 33"
                stroke="rgba(196,160,74,0.55)" stroke-width="1" fill="none"/>

          <!-- Cigar band near the head (upper third) -->
          <rect x="45" y="48" width="30" height="15" rx="1.5"
                fill="url(#band)" stroke="{C_TOBACCO_COPPER}" stroke-width="0.8"/>
          <!-- Band top + bottom edge lines -->
          <line x1="45" y1="48" x2="75" y2="48"
                stroke="{C_TOBACCO_DARK}" stroke-width="0.6"/>
          <line x1="45" y1="63" x2="75" y2="63"
                stroke="{C_TOBACCO_DARK}" stroke-width="0.6"/>
          <!-- Band center emblem -->
          <ellipse cx="60" cy="55.5" rx="4" ry="3"
                   fill="none" stroke="{C_TOBACCO_DARK}" stroke-width="1"/>
          <circle cx="60" cy="55.5" r="1.1" fill="{C_TOBACCO_DARK}"/>

          <!-- Foot end: cut face showing filler tobacco -->
          <ellipse cx="60" cy="153" rx="8" ry="2.8"
                   fill="{C_LEAF_DARK}" stroke="rgba(196,160,74,0.45)" stroke-width="1"/>
          <!-- Subtle filler rings on the cut face -->
          <ellipse cx="60" cy="153" rx="4.5" ry="1.6"
                   fill="none" stroke="rgba(196,160,74,0.25)" stroke-width="0.6"/>

          <!-- Soft ground shadow under the foot -->
          <ellipse cx="64" cy="160" rx="16" ry="2.5"
                   fill="rgba(0,0,0,0.28)"/>

        </g>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Cigar Tasting<br>Log</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Track Every Smoke,<br>Every Blend, Every Nuance</div>
      <div class="features">
        <span class="feature-badge">40 Smoking Sessions</span>
        <span class="feature-badge">Flavor Wheel</span>
        <span class="feature-badge">Brand Tracker</span>
        <span class="feature-badge">Cigar Glossary</span>
      </div>
      <div class="tagline">For Aficionados &amp; Connoisseurs</div>
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
