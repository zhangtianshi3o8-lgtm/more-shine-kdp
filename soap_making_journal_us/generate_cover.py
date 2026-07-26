#!/usr/bin/env python3
"""
Soap Making Journal — KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Trim: 6" x 9"
Pages: 104 (cream paper)
Spine: 104 x 0.0025 = 0.260"
Bleed: 0.125" all outer edges
Full cover: 12.51 x 9.25 in
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "soap_making_journal_cover_V1.0.html")

TRIM_W = 6.0
TRIM_H = 9.0
PAGES = 104
SPINE = PAGES * 0.0025   # 0.260"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.51"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

C_CHARCOAL = "#161616"
C_DARK     = "#1E1E1E"
C_LAV_D    = "#1A1518"
C_LAV      = "#8A7AA8"
C_LAV_L    = "#A08AB8"
C_LAV_X    = "#B8A8C8"
C_HERB     = "#7A9A6A"
C_HERB_L   = "#9ABA8A"
C_HERB_X   = "#BACA9A"
C_GOLD     = "#C4A04A"
C_GOLD_L   = "#D4B896"
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 35%, {C_LAV_D} 100%);
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
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 26px 16px at 15% 25%, {C_LAV}, transparent),
    radial-gradient(ellipse 22px 14px at 80% 15%, {C_HERB_L}, transparent),
    radial-gradient(ellipse 24px 15px at 70% 70%, {C_GOLD}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_LAV}, transparent),
    radial-gradient(ellipse 18px 11px at 50% 50%, {C_HERB_L}, transparent),
    radial-gradient(ellipse 22px 13px at 10% 60%, {C_LAV_D}, transparent);
}}

.back-cover::after {{
  content: '';
  position: absolute;
  top: -0.3in; right: -0.3in;
  width: 1.2in; height: 1.2in;
  border-radius: 50%;
  background: rgba(138, 122, 168, 0.08);
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
  color: {C_LAV_X};
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
  background: {C_LAV};
  border-radius: 50%;
  box-shadow: 0 0 3px rgba(138,122,168,0.4);
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
  color: {C_LAV};
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
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 10px 6px at 50% 20%, {C_LAV}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 50%, {C_HERB_L}, transparent),
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
  color: {C_LAV};
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 20%, {C_LAV_D} 55%, {C_DARK} 85%, {C_CHARCOAL} 100%);
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
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 38px 23px at 15% 25%, {C_LAV}, transparent),
    radial-gradient(ellipse 32px 19px at 80% 15%, {C_HERB_L}, transparent),
    radial-gradient(ellipse 36px 22px at 70% 70%, {C_GOLD}, transparent),
    radial-gradient(ellipse 26px 16px at 25% 80%, {C_LAV}, transparent),
    radial-gradient(ellipse 22px 14px at 50% 50%, {C_HERB_L}, transparent),
    radial-gradient(ellipse 28px 17px at 10% 60%, {C_LAV_D}, transparent),
    radial-gradient(ellipse 20px 12px at 90% 45%, {C_GOLD}, transparent),
    radial-gradient(ellipse 18px 11px at 40% 90%, {C_LAV}, transparent),
    radial-gradient(ellipse 16px 10px at 60% 35%, {C_HERB_L}, transparent);
}}

/* ============ SOAP ILLUSTRATION ============ */
.soap-wrap {{
  width: 110px; height: 180px;
  position: relative;
  margin: 0 auto 20px;
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
  font-size: 24pt;
  font-weight: 700;
  color: {C_WHITE};
  line-height: 1.12;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.55);
}}

.accent-bar {{
  width: 120px; height: 2.5px;
  background: {C_LAV};
  margin: 16px auto;
}}

.subtitle {{
  font-size: 11.5pt;
  color: {C_HERB_L};
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
  border: 1px solid rgba(138,122,168,0.45);
  color: {C_LAV};
  font-size: 7.5pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 10px;
  border-radius: 3px;
  text-transform: uppercase;
}}

.tagline {{
  font-size: 9pt;
  color: {C_HERB_L};
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

@media screen {{ .cover-wrap {{ border: 1px solid #ccc; }} }}
</style>
"""


def generate(output_path=OUTPUT_FILE):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Soap Making Journal — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every batch teaches a lesson. Every bar is progress.</strong>
        This journal captures the science and art of soap making — from
        oil ratios and lye calculations to cure tracking and quality
        evaluation. Your personal archive of formulas that work and
        lessons learned along the way.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_LAV_X}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>40 two-page batch logs (recipe + process)</li>
        <li>14 common oils with SAP values and properties</li>
        <li>Lye safety guidelines and mixing protocol</li>
        <li>Essential oil usage rates and behavior chart</li>
        <li>Curing timeline with weekly testing guide</li>
        <li>12 common soap problems with solutions</li>
        <li>Recipe library index (36 entries)</li>
        <li>Supply and ingredient inventory tracker</li>
        <li>Gift and sales distribution log</li>
        <li>Year-in-review favorites and goal-setting pages</li>
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
    <div class="spine-text">Soap Making Journal</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Soap bar illustration (SVG) -->
    <div class="soap-wrap">
      <svg viewBox="0 0 110 180" width="110" height="180" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="soapGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_GOLD_L}" stop-opacity="0.15"/>
            <stop offset="100%" stop-color="{C_HERB}" stop-opacity="0.08"/>
          </linearGradient>
          <linearGradient id="bubbleGrad" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="{C_LAV_L}" stop-opacity="0.15"/>
            <stop offset="100%" stop-color="{C_LAV}" stop-opacity="0.05"/>
          </linearGradient>
          <linearGradient id="herbGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_HERB_X}" stop-opacity="0.20"/>
            <stop offset="100%" stop-color="{C_HERB}" stop-opacity="0.10"/>
          </linearGradient>
        </defs>

        <!-- Soap bar -->
        <rect x="16" y="90" width="78" height="48" rx="8"
              fill="url(#soapGrad)"
              stroke="rgba(196,160,74,0.30)" stroke-width="1.5"/>

        <!-- Soap swirl patterns -->
        <path d="M 24 100 Q 55 97 86 100" fill="none"
              stroke="rgba(138,122,168,0.20)" stroke-width="2"
              stroke-linecap="round"/>
        <path d="M 24 108 Q 55 111 86 108" fill="none"
              stroke="rgba(122,154,106,0.18)" stroke-width="2"
              stroke-linecap="round"/>
        <path d="M 24 116 Q 55 113 86 116" fill="none"
              stroke="rgba(196,160,74,0.15)" stroke-width="1.5"
              stroke-linecap="round"/>
        <path d="M 24 124 Q 55 127 86 124" fill="none"
              stroke="rgba(138,122,168,0.12)" stroke-width="1.5"
              stroke-linecap="round"/>

        <!-- Soap top edge highlight -->
        <path d="M 16 90 L 94 90" fill="none"
              stroke="rgba(250,248,244,0.15)" stroke-width="1"/>

        <!-- Bubbles floating above soap -->
        <circle cx="30" cy="35" r="9"
                fill="url(#bubbleGrad)"
                stroke="rgba(138,122,168,0.25)" stroke-width="0.8"/>
        <circle cx="30" cy="33" r="3"
                fill="rgba(250,248,244,0.12)"/>

        <circle cx="68" cy="45" r="7"
                fill="url(#bubbleGrad)"
                stroke="rgba(122,154,106,0.22)" stroke-width="0.8"/>
        <circle cx="66" cy="43" r="2.5"
                fill="rgba(250,248,244,0.10)"/>

        <circle cx="50" cy="60" r="5"
                fill="rgba(196,160,74,0.10)"
                stroke="rgba(196,160,74,0.20)" stroke-width="0.6"/>

        <circle cx="80" cy="65" r="6"
                fill="rgba(160,138,184,0.10)"
                stroke="rgba(138,122,168,0.20)" stroke-width="0.6"/>

        <circle cx="22" cy="55" r="4"
                fill="rgba(154,186,138,0.08)"
                stroke="rgba(122,154,106,0.18)" stroke-width="0.5"/>

        <circle cx="88" cy="30" r="3.5"
                fill="rgba(196,160,74,0.12)"
                stroke="rgba(196,160,74,0.20)" stroke-width="0.5"/>

        <!-- Lavender sprig (left) -->
        <line x1="12" y1="80" x2="14" y2="50"
              stroke="rgba(122,154,106,0.20)" stroke-width="1.2"
              stroke-linecap="round"/>
        <ellipse cx="11" cy="55" rx="3" ry="2"
                 fill="url(#herbGrad)"
                 stroke="rgba(122,154,106,0.20)" stroke-width="0.5"
                 transform="rotate(-30 11 55)"/>
        <ellipse cx="15" cy="60" rx="3" ry="2"
                 fill="url(#herbGrad)"
                 stroke="rgba(122,154,106,0.18)" stroke-width="0.5"
                 transform="rotate(30 15 60)"/>
        <ellipse cx="10" cy="65" rx="2.5" ry="1.5"
                 fill="url(#herbGrad)"
                 stroke="rgba(122,154,106,0.15)" stroke-width="0.4"
                 transform="rotate(-25 10 65)"/>

        <!-- Lavender buds at top of sprig -->
        <ellipse cx="13" cy="48" rx="2.5" ry="3.5"
                 fill="rgba(138,122,168,0.20)"
                 stroke="rgba(138,122,168,0.25)" stroke-width="0.5"/>
        <ellipse cx="14" cy="44" rx="2" ry="3"
                 fill="rgba(138,122,168,0.15)"
                 stroke="rgba(138,122,168,0.22)" stroke-width="0.4"/>

        <!-- Soap dish shadow -->
        <ellipse cx="55" cy="142" rx="42" ry="3"
                 fill="rgba(22,22,22,0.08)"/>

        <!-- Sparkle accents -->
        <g opacity="0.6">
          <circle cx="96" cy="50" r="2" fill="rgba(196,160,74,0.4)"/>
          <circle cx="96" cy="50" r="0.8" fill="rgba(250,248,244,0.6)"/>
          <circle cx="5" cy="100" r="1.5" fill="rgba(138,122,168,0.3)"/>
          <circle cx="100" cy="120" r="1.5" fill="rgba(196,160,74,0.3)"/>
          <circle cx="20" cy="15" r="1" fill="rgba(250,248,244,0.25)"/>
        </g>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Soap Making<br>Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Track Every Batch,<br>Perfect Every Bar</div>
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
