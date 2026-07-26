#!/usr/bin/env python3
"""
Essential Oil & Aromatherapy Journal — KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Generates a print-ready full wrap cover (back + spine + front) as
standalone HTML. Export with Chrome headless to PDF.

Trim: 6" x 9"
Pages: 116 (cream paper)
Spine: 116 x 0.0025 = 0.29"
Bleed: 0.125" all outer edges
Full cover: 12.54 x 9.25 in
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "essential_oil_aromatherapy_journal_cover_V1.0.html")

# KDP cover specs
TRIM_W = 6.0          # inches
TRIM_H = 9.0
PAGES = 116
SPINE = PAGES * 0.0025   # cream paper = 0.29"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.54"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors — Sage / Charcoal / Gold theme (quiet luxury aesthetic)
C_CHARCOAL = "#161616"   # near-black charcoal
C_DARK     = "#1E1E1E"   # dark warm charcoal
C_SAGE_D   = "#2A3328"   # dark sage
C_SAGE     = "#4A5A43"   # muted sage
C_SAGE_M   = "#7A8B6F"   # medium sage green
C_SAGE_L   = "#A8B89C"   # light sage
C_GOLD     = "#C4A04A"   # muted gold
C_GOLD_L   = "#D4B896"   # light gold / champagne
C_CREAM    = "#FAF8F4"   # warm cream
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 40%, {C_SAGE_D} 100%);
  padding: 0.75in 0.5in 0.45in 0.5in;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  overflow: hidden;
}}

/* Subtle sage/gold texture */
.back-cover::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 24px 14px at 15% 25%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 13px at 80% 15%, {C_SAGE_M}, transparent),
    radial-gradient(ellipse 26px 15px at 70% 70%, {C_GOLD}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_SAGE_M}, transparent),
    radial-gradient(ellipse 18px 11px at 50% 50%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 13px at 10% 60%, {C_SAGE_M}, transparent);
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
  color: {C_SAGE_L};
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
    radial-gradient(ellipse 10px 6px at 50% 50%, {C_SAGE_M}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 80%, {C_GOLD}, transparent);
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 25%, {C_SAGE_D} 55%, {C_DARK} 85%, {C_CHARCOAL} 100%);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: {BLEED}in {BLEED}in {BLEED}in {BLEED}in;
}}

/* Subtle sage/gold texture on front */
.front-cover::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 40px 24px at 15% 25%, {C_SAGE_M}, transparent),
    radial-gradient(ellipse 34px 20px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 38px 22px at 70% 70%, {C_SAGE_M}, transparent),
    radial-gradient(ellipse 28px 18px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 24px 15px at 50% 50%, {C_SAGE_M}, transparent),
    radial-gradient(ellipse 30px 18px at 10% 60%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 14px at 90% 45%, {C_SAGE_M}, transparent),
    radial-gradient(ellipse 20px 12px at 40% 90%, {C_GOLD}, transparent),
    radial-gradient(ellipse 18px 11px at 60% 35%, {C_SAGE_M}, transparent);
}}

/* ============ DROPPER BOTTLE (SVG) ============ */
.bottle-wrap {{
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
  font-size: 26pt;
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
  font-size: 11pt;
  color: {C_SAGE_L};
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
  color: {C_SAGE_L};
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
  <title>Essential Oil & Aromatherapy Journal — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every drop holds a world of wellness.</strong>
        From calming lavender to energizing citrus, this journal
        helps you track every blend, every oil, and every benefit
        &mdash; building your personal aromatherapy reference one
        page at a time.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_SAGE_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>40 two-page blend recipe logs with full details</li>
        <li>Essential oil categories reference (6 families, 40+ oils)</li>
        <li>Dilution guide with safe ratios for every use</li>
        <li>Blending principles and the note system explained</li>
        <li>Safety guidelines for responsible oil use</li>
        <li>Oil collection inventory and supplier tracking</li>
        <li>Weekly wellness tracker for daily use and mood</li>
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
    <div class="spine-text">Essential Oil Journal</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Dropper bottle illustration (SVG line art) -->
    <div class="bottle-wrap">
      <svg viewBox="0 0 100 170" width="100" height="170" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="liquid" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_SAGE_M}" stop-opacity="0.35"/>
            <stop offset="50%" stop-color="{C_SAGE}" stop-opacity="0.40"/>
            <stop offset="100%" stop-color="{C_SAGE_D}" stop-opacity="0.45"/>
          </linearGradient>
          <linearGradient id="glassShine" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="rgba(250,248,244,0)"/>
            <stop offset="35%" stop-color="rgba(250,248,244,0.10)"/>
            <stop offset="65%" stop-color="rgba(250,248,244,0.05)"/>
            <stop offset="100%" stop-color="rgba(250,248,244,0)"/>
          </linearGradient>
        </defs>

        <!-- Dropper bulb (top) -->
        <ellipse cx="50" cy="12" rx="13" ry="10"
                 stroke="rgba(196,160,74,0.45)" stroke-width="1.5"
                 fill="rgba(196,160,74,0.06)"/>

        <!-- Cap -->
        <rect x="38" y="20" width="24" height="14" rx="2"
              stroke="rgba(196,160,74,0.55)" stroke-width="1.5"
              fill="rgba(196,160,74,0.15)"/>

        <!-- Cap highlight -->
        <line x1="42" y1="23" x2="42" y2="31"
              stroke="rgba(250,248,244,0.35)" stroke-width="1.5"/>

        <!-- Bottle neck -->
        <path d="M 42 34 L 42 42 L 58 42 L 58 34"
              stroke="rgba(250,248,244,0.35)" stroke-width="1.2" fill="none"/>

        <!-- Bottle body — rounded rectangle -->
        <path d="M 28 44
                 Q 28 42 30 42
                 L 70 42
                 Q 72 42 72 44
                 L 72 130
                 Q 72 134 68 134
                 L 32 134
                 Q 28 134 28 130
                 Z"
              stroke="rgba(250,248,244,0.45)" stroke-width="1.8" fill="none"
              stroke-linejoin="round"/>

        <!-- Oil liquid inside bottle -->
        <path d="M 31 70
                 L 69 70
                 L 69 128
                 Q 69 131 66 131
                 L 34 131
                 Q 31 131 31 128
                 Z"
              fill="url(#liquid)"/>

        <!-- Liquid surface line -->
        <ellipse cx="50" cy="70" rx="19" ry="2"
                 stroke="rgba(168,184,156,0.4)" stroke-width="1" fill="none"/>

        <!-- Bottle body shine -->
        <path d="M 34 55 Q 33 90 35 120"
              stroke="rgba(250,248,244,0.12)" stroke-width="1" fill="none"/>

        <!-- Label area on bottle -->
        <rect x="36" y="88" width="28" height="30" rx="2"
              stroke="rgba(196,160,74,0.30)" stroke-width="1" fill="none"/>
        <line x1="40" y1="96" x2="60" y2="96"
              stroke="rgba(196,160,74,0.20)" stroke-width="0.8"/>
        <line x1="40" y1="102" x2="58" y2="102"
              stroke="rgba(196,160,74,0.15)" stroke-width="0.6"/>
        <line x1="40" y1="108" x2="56" y2="108"
              stroke="rgba(196,160,74,0.15)" stroke-width="0.6"/>

        <!-- Aroma vapor lines rising -->
        <path d="M 42 8 Q 40 0 44 -4" stroke="rgba(196,160,74,0.25)" stroke-width="1" fill="none" stroke-linecap="round"/>
        <path d="M 50 5 Q 48 -4 52 -8" stroke="rgba(168,184,156,0.20)" stroke-width="1" fill="none" stroke-linecap="round"/>
        <path d="M 58 8 Q 60 0 56 -4" stroke="rgba(196,160,74,0.20)" stroke-width="1" fill="none" stroke-linecap="round"/>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Essential Oil<br>&amp; Aromatherapy Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Track Every Blend,<br>Every Oil, Every Benefit</div>
      <div class="features">
        <span class="feature-badge">40 Blend Recipes</span>
        <span class="feature-badge">Dilution Guide</span>
        <span class="feature-badge">Oil Inventory</span>
        <span class="feature-badge">Wellness Tracker</span>
      </div>
      <div class="tagline">For Wellness Seekers &amp; Oil Enthusiasts</div>
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
    print(f"[OK] Cover generated: {{path}}")
    print(f"     Full cover: {COVER_W:.4f} x {COVER_H:.4f} in")
    print(f"     Spine: {SPINE:.4f} in ({PAGES} pages, cream paper)")
    print(f"     At 300 DPI: {COVER_W*300:.0f} x {COVER_H*300:.0f} px")
