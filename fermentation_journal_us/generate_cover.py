#!/usr/bin/env python3
"""
Fermentation Journal — KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Trim: 6" x 9"
Pages: 110 (cream paper)
Spine: 110 x 0.0025 = 0.275"
Bleed: 0.125" all outer edges
Full cover: 12.525 x 9.25 in
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "fermentation_journal_cover_V1.0.html")

# KDP cover specs
TRIM_W = 6.0
TRIM_H = 9.0
PAGES = 110
SPINE = PAGES * 0.0025   # cream paper = 0.275"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.525"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors — Copper / Amber / Charcoal / Olive theme
C_CHARCOAL = "#161616"
C_DARK     = "#1E1E1E"
C_AMBER_D  = "#2E2218"
C_AMBER    = "#4A3320"
C_BROWN    = "#6B4423"
C_COPPER   = "#B87333"
C_GOLD     = "#C4A04A"
C_GOLD_L   = "#D4B896"
C_OLIVE    = "#6B7A4F"
C_OLIVE_L  = "#A8B89C"
C_CREAM    = "#FAF8F4"
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 40%, {C_AMBER_D} 100%);
  padding: 0.75in 0.5in 0.45in 0.5in;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  overflow: hidden;
}}

.back-cover::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 24px 14px at 15% 25%, {C_COPPER}, transparent),
    radial-gradient(ellipse 22px 13px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 26px 15px at 70% 70%, {C_OLIVE}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_COPPER}, transparent),
    radial-gradient(ellipse 18px 11px at 50% 50%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 13px at 10% 60%, {C_OLIVE}, transparent);
}}

.back-cover::after {{
  content: '';
  position: absolute;
  top: -0.3in; right: -0.3in;
  width: 1.2in; height: 1.2in;
  border-radius: 50%;
  background: rgba(184, 115, 51, 0.08);
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
  background: {C_COPPER};
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
  color: {C_COPPER};
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

.spine::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.03;
  background-image:
    radial-gradient(ellipse 10px 6px at 50% 20%, {C_COPPER}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 50%, {C_GOLD}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 80%, {C_OLIVE}, transparent);
}}

.spine-text {{
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  color: rgba(255,255,255,0.95);
  font-size: 7.5pt;
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
  color: {C_COPPER};
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

.front-cover::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 40px 24px at 15% 25%, {C_COPPER}, transparent),
    radial-gradient(ellipse 34px 20px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 38px 22px at 70% 70%, {C_OLIVE}, transparent),
    radial-gradient(ellipse 28px 18px at 25% 80%, {C_COPPER}, transparent),
    radial-gradient(ellipse 24px 15px at 50% 50%, {C_GOLD}, transparent),
    radial-gradient(ellipse 30px 18px at 10% 60%, {C_OLIVE}, transparent),
    radial-gradient(ellipse 22px 14px at 90% 45%, {C_COPPER}, transparent),
    radial-gradient(ellipse 20px 12px at 40% 90%, {C_GOLD}, transparent),
    radial-gradient(ellipse 18px 11px at 60% 35%, {C_OLIVE}, transparent);
}}

/* ============ MASON JAR (SVG) ============ */
.jar-wrap {{
  width: 100px; height: 170px;
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
  background: {C_COPPER};
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
  border: 1px solid rgba(184,115,51,0.4);
  color: {C_COPPER};
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
  color: {C_COPPER};
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  font-weight: 700;
  z-index: 5;
}}

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
  <title>Fermentation Journal — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Transform your kitchen into a living laboratory.</strong>
        From tangy sauerkraut to fizzy kombucha, this journal helps
        you document every batch, track every culture, and refine every
        recipe &mdash; turning fermentation experiments into reliable
        culinary traditions.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>40 two-page batch logs with full fermentation details</li>
        <li>Salt and brine guide with precise ratios for every type</li>
        <li>pH timeline reference for safe, successful ferments</li>
        <li>Starter culture registry (SCOBYs, grains, sourdough)</li>
        <li>Recipe development worksheets for your own creations</li>
        <li>Equipment inventory and supplier directory</li>
        <li>Tasting journal and year-in-review favorites</li>
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
    <div class="spine-text">Fermentation Journal</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Mason jar illustration (SVG line art) -->
    <div class="jar-wrap">
      <svg viewBox="0 0 100 170" width="100" height="170" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="liquid" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_COPPER}" stop-opacity="0.22"/>
            <stop offset="40%" stop-color="{C_BROWN}" stop-opacity="0.28"/>
            <stop offset="70%" stop-color="{C_OLIVE}" stop-opacity="0.20"/>
            <stop offset="100%" stop-color="{C_AMBER_D}" stop-opacity="0.30"/>
          </linearGradient>
          <linearGradient id="glassShine" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="rgba(250,248,244,0)"/>
            <stop offset="35%" stop-color="rgba(250,248,244,0.10)"/>
            <stop offset="65%" stop-color="rgba(250,248,244,0.04)"/>
            <stop offset="100%" stop-color="rgba(250,248,244,0)"/>
          </linearGradient>
        </defs>

        <!-- Jar lid (copper) -->
        <rect x="24" y="8" width="52" height="12" rx="3"
              fill="rgba(184,115,51,0.15)" stroke="rgba(184,115,51,0.45)" stroke-width="1.5"/>

        <!-- Lid texture lines -->
        <line x1="30" y1="10" x2="30" y2="18" stroke="rgba(0,0,0,0.2)" stroke-width="0.8"/>
        <line x1="36" y1="10" x2="36" y2="18" stroke="rgba(0,0,0,0.15)" stroke-width="0.6"/>
        <line x1="42" y1="10" x2="42" y2="18" stroke="rgba(0,0,0,0.15)" stroke-width="0.6"/>
        <line x1="48" y1="10" x2="48" y2="18" stroke="rgba(0,0,0,0.15)" stroke-width="0.6"/>
        <line x1="54" y1="10" x2="54" y2="18" stroke="rgba(0,0,0,0.15)" stroke-width="0.6"/>
        <line x1="60" y1="10" x2="60" y2="18" stroke="rgba(0,0,0,0.15)" stroke-width="0.6"/>
        <line x1="66" y1="10" x2="66" y2="18" stroke="rgba(0,0,0,0.15)" stroke-width="0.6"/>
        <line x1="72" y1="10" x2="72" y2="18" stroke="rgba(0,0,0,0.2)" stroke-width="0.8"/>

        <!-- Lid band (transition) -->
        <rect x="22" y="18" width="56" height="5"
              fill="rgba(107,68,35,0.12)" stroke="rgba(184,115,51,0.30)" stroke-width="1"/>

        <!-- Jar body — mason jar profile -->
        <!-- Shoulders taper slightly, then straight body -->
        <path d="M 22 23
                 L 22 25
                 Q 22 28 25 30
                 L 25 152
                 Q 25 156 29 156
                 L 71 156
                 Q 75 156 75 152
                 L 75 30
                 Q 78 28 78 25
                 L 78 23"
              stroke="rgba(250,248,244,0.40)" stroke-width="1.8" fill="none"
              stroke-linejoin="round"/>

        <!-- Ferment liquid/content -->
        <path d="M 27 50
                 L 73 50
                 L 73 150
                 Q 73 153 70 153
                 L 30 153
                 Q 27 153 27 150
                 Z"
              fill="url(#liquid)"/>

        <!-- Liquid surface line -->
        <ellipse cx="50" cy="50" rx="23" ry="2.5"
                 stroke="rgba(212,184,150,0.35)" stroke-width="1" fill="none"/>

        <!-- Bubbles in liquid -->
        <circle cx="38" cy="65" r="2.5" fill="rgba(250,248,244,0.15)"/>
        <circle cx="58" cy="72" r="2" fill="rgba(250,248,244,0.12)"/>
        <circle cx="45" cy="85" r="3" fill="rgba(250,248,244,0.10)"/>
        <circle cx="62" cy="95" r="1.5" fill="rgba(250,248,244,0.15)"/>
        <circle cx="35" cy="110" r="2" fill="rgba(250,248,244,0.08)"/>
        <circle cx="55" cy="125" r="2.5" fill="rgba(250,248,244,0.10)"/>

        <!-- Jar body shine -->
        <path d="M 30 40 Q 29 90 31 140"
              stroke="rgba(250,248,244,0.10)" stroke-width="1" fill="none"/>

        <!-- Label on jar -->
        <rect x="34" y="100" width="32" height="28" rx="2"
              stroke="rgba(184,115,51,0.25)" stroke-width="1" fill="none"/>
        <line x1="38" y1="108" x2="62" y2="108"
              stroke="rgba(184,115,51,0.18)" stroke-width="0.8"/>
        <line x1="38" y1="114" x2="58" y2="114"
              stroke="rgba(184,115,51,0.12)" stroke-width="0.6"/>
        <line x1="38" y1="120" x2="60" y2="120"
              stroke="rgba(184,115,51,0.12)" stroke-width="0.6"/>

        <!-- Rising vapor/aroma -->
        <path d="M 42 5 Q 40 -2 44 -6" stroke="rgba(184,115,51,0.25)" stroke-width="1" fill="none" stroke-linecap="round"/>
        <path d="M 50 2 Q 48 -6 52 -10" stroke="rgba(196,160,74,0.22)" stroke-width="1" fill="none" stroke-linecap="round"/>
        <path d="M 58 5 Q 60 -2 56 -6" stroke="rgba(184,115,51,0.20)" stroke-width="1" fill="none" stroke-linecap="round"/>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Fermentation<br>Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Track Every Batch,<br>Every Culture, Every Flavor</div>
      <div class="features">
        <span class="feature-badge">40 Batch Logs</span>
        <span class="feature-badge">Brine Guide</span>
        <span class="feature-badge">Culture Registry</span>
        <span class="feature-badge">Tasting Notes</span>
      </div>
      <div class="tagline">For Home Fermenters &amp; Gut Health Enthusiasts</div>
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
