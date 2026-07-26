#!/usr/bin/env python3
"""
Astronomy Observation Journal — KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Trim: 6" x 9"
Pages: 102 (cream paper)
Spine: 102 x 0.0025 = 0.255"
Bleed: 0.125" all outer edges
Full cover: 12.505 x 9.25 in
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "astronomy_observation_journal_cover_V1.0.html")

TRIM_W = 6.0
TRIM_H = 9.0
PAGES = 102
SPINE = PAGES * 0.0025   # 0.255"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.505"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

C_CHARCOAL = "#161616"
C_DARK     = "#1E1E1E"
C_BLUE_D   = "#1A1E2A"
C_BLUE     = "#3A4A7A"
C_BLUE_L   = "#5A6A9A"
C_BLUE_X   = "#7A8ABA"
C_GOLD     = "#C4A04A"
C_GOLD_L   = "#D4B896"
C_CYAN     = "#4A7A8A"
C_CYAN_L   = "#6A9AAA"
C_CYAN_X   = "#8ABACA"
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 35%, {C_BLUE_D} 100%);
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
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 26px 16px at 15% 25%, {C_BLUE}, transparent),
    radial-gradient(ellipse 22px 14px at 80% 15%, {C_CYAN_L}, transparent),
    radial-gradient(ellipse 24px 15px at 70% 70%, {C_GOLD}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_BLUE}, transparent),
    radial-gradient(ellipse 18px 11px at 50% 50%, {C_CYAN_L}, transparent),
    radial-gradient(ellipse 22px 13px at 10% 60%, {C_BLUE_D}, transparent);
}}

.back-cover::after {{
  content: '';
  position: absolute;
  top: -0.3in; right: -0.3in;
  width: 1.2in; height: 1.2in;
  border-radius: 50%;
  background: rgba(58, 74, 122, 0.08);
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
  background: {C_BLUE};
  border-radius: 50%;
  box-shadow: 0 0 3px rgba(58,74,122,0.4);
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
  color: {C_BLUE};
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
    radial-gradient(ellipse 10px 6px at 50% 20%, {C_BLUE}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 50%, {C_CYAN_L}, transparent),
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
  color: {C_BLUE};
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 20%, {C_BLUE_D} 55%, {C_DARK} 85%, {C_CHARCOAL} 100%);
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
    radial-gradient(ellipse 38px 23px at 15% 25%, {C_BLUE}, transparent),
    radial-gradient(ellipse 32px 19px at 80% 15%, {C_CYAN_L}, transparent),
    radial-gradient(ellipse 36px 22px at 70% 70%, {C_GOLD}, transparent),
    radial-gradient(ellipse 26px 16px at 25% 80%, {C_BLUE}, transparent),
    radial-gradient(ellipse 22px 14px at 50% 50%, {C_CYAN_L}, transparent),
    radial-gradient(ellipse 28px 17px at 10% 60%, {C_BLUE_D}, transparent),
    radial-gradient(ellipse 20px 12px at 90% 45%, {C_GOLD}, transparent),
    radial-gradient(ellipse 18px 11px at 40% 90%, {C_BLUE}, transparent),
    radial-gradient(ellipse 16px 10px at 60% 35%, {C_CYAN_L}, transparent);
}}

/* ============ TITLE ============ */
.title-block {{
  position: relative;
  z-index: 5;
  padding: 0 0.5in;
}}

.main-title {{
  font-family: Georgia, serif;
  font-size: 22pt;
  font-weight: 700;
  color: {C_WHITE};
  line-height: 1.12;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.55);
}}

.accent-bar {{
  width: 120px; height: 2.5px;
  background: {C_BLUE};
  margin: 16px auto;
}}

.subtitle {{
  font-size: 11.5pt;
  color: {C_CYAN_L};
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
  border: 1px solid rgba(58,74,122,0.45);
  color: {C_BLUE_X};
  font-size: 7.5pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 10px;
  border-radius: 3px;
  text-transform: uppercase;
}}

.tagline {{
  font-size: 9pt;
  color: {C_CYAN_L};
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
  <title>Astronomy Observation Journal — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Under the same stars, always wondering.</strong>
        This journal transforms casual stargazing into systematic
        discovery. From seeing and transparency ratings to equipment
        configurations and field sketches, every observing session
        becomes part of your personal astronomical archive.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>40 two-page observation session logs</li>
        <li>Weather, seeing, and transparency tracking</li>
        <li>Bortle dark sky scale and Moon phase</li>
        <li>Equipment configuration per session</li>
        <li>Field sketch areas with dot-grid</li>
        <li>Stellar magnitude reference (16 entries)</li>
        <li>Top 20 Messier deep-sky objects guide</li>
        <li>Telescope types comparison and eyepiece guide</li>
        <li>Bortle dark sky scale (Classes 1-9)</li>
        <li>Seeing and transparency rating system</li>
        <li>Observing wishlist (24 entries)</li>
        <li>Equipment inventory and year-in-review</li>
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
    <div class="spine-text">Astronomy Observation Journal</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Telescope + star field illustration (SVG) -->
    <div style="width: 110px; height: 180px; margin: 0 auto 20px; position: relative; z-index: 5;">
      <svg viewBox="0 0 110 180" width="110" height="180" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="scopeGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_BLUE_X}" stop-opacity="0.15"/>
            <stop offset="100%" stop-color="{C_CYAN}" stop-opacity="0.08"/>
          </linearGradient>
          <radialGradient id="moonGrad">
            <stop offset="0%" stop-color="{C_GOLD_L}" stop-opacity="0.20"/>
            <stop offset="100%" stop-color="{C_GOLD}" stop-opacity="0.05"/>
          </radialGradient>
          <linearGradient id="glowGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_GOLD}" stop-opacity="0.25"/>
            <stop offset="100%" stop-color="{C_GOLD}" stop-opacity="0.02"/>
          </linearGradient>
        </defs>

        <!-- Crescent moon (top right) -->
        <circle cx="85" cy="28" r="11" fill="url(#moonGrad)"
                stroke="rgba(196,160,74,0.20)" stroke-width="0.8"/>
        <circle cx="88" cy="26" r="10" fill="{C_DARK}" opacity="0.6"/>

        <!-- Stars (various sizes) -->
        <circle cx="25" cy="15" r="2.5" fill="rgba(196,160,74,0.5)"/>
        <circle cx="25" cy="15" r="1" fill="rgba(250,248,244,0.7)"/>

        <circle cx="60" cy="25" r="2" fill="rgba(250,248,244,0.4)"/>

        <circle cx="95" cy="55" r="1.8" fill="rgba(196,160,74,0.4)"/>

        <circle cx="15" cy="45" r="1.5" fill="rgba(250,248,244,0.35)"/>

        <circle cx="45" cy="50" r="1.2" fill="rgba(250,248,244,0.3)"/>

        <circle cx="75" cy="65" r="1" fill="rgba(250,248,244,0.25)"/>

        <circle cx="10" cy="70" r="0.8" fill="rgba(196,160,74,0.3)"/>

        <!-- Constellation lines (faint) -->
        <line x1="25" y1="15" x2="60" y2="25"
              stroke="rgba(196,160,74,0.08)" stroke-width="0.6"/>
        <line x1="60" y1="25" x2="95" y2="55"
              stroke="rgba(196,160,74,0.06)" stroke-width="0.5"/>
        <line x1="95" y1="55" x2="75" y2="65"
              stroke="rgba(196,160,74,0.05)" stroke-width="0.4"/>

        <!-- Telescope tube (diagonal) -->
        <g transform="rotate(-25, 55, 95)">
          <rect x="37" y="88" width="36" height="14"
                fill="url(#scopeGrad)"
                stroke="rgba(58,74,122,0.35)" stroke-width="1.2"
                rx="2"/>
          <!-- Aperture ring -->
          <ellipse cx="73" cy="95" rx="2" ry="7"
                   fill="rgba(22,22,22,0.2)"
                   stroke="rgba(58,74,122,0.25)" stroke-width="0.6"/>
          <!-- Focuser/eyepiece end -->
          <rect x="34" y="91" width="4" height="8"
                fill="rgba(58,74,122,0.12)"
                stroke="rgba(58,74,122,0.20)" stroke-width="0.4"/>
          <!-- Dew shield hint -->
          <rect x="68" y="87" width="6" height="16"
                fill="none"
                stroke="rgba(58,74,122,0.15)" stroke-width="0.5"/>
        </g>

        <!-- Finder scope (small tube on top) -->
        <g transform="rotate(-25, 55, 95)">
          <rect x="48" y="83" width="16" height="5"
                fill="rgba(74,122,138,0.10)"
                stroke="rgba(74,122,138,0.20)" stroke-width="0.4"
                rx="1"/>
        </g>

        <!-- Tripod legs -->
        <line x1="48" y1="130" x2="35" y2="162"
              stroke="rgba(90,106,154,0.18)" stroke-width="2"
              stroke-linecap="round"/>
        <line x1="55" y1="130" x2="55" y2="165"
              stroke="rgba(90,106,154,0.15)" stroke-width="2"
              stroke-linecap="round"/>
        <line x1="62" y1="130" x2="75" y2="162"
              stroke="rgba(90,106,154,0.18)" stroke-width="2"
              stroke-linecap="round"/>

        <!-- Mount head -->
        <polygon points="48,128 62,128 58,132 52,132"
                 fill="rgba(58,74,122,0.15)"
                 stroke="rgba(58,74,122,0.25)" stroke-width="0.5"/>

        <!-- Ground line -->
        <line x1="10" y1="166" x2="100" y2="166"
              stroke="rgba(58,74,122,0.10)" stroke-width="1"/>

        <!-- Diffraction spikes on brightest star -->
        <line x1="22" y1="10" x2="28" y2="20"
              stroke="rgba(196,160,74,0.15)" stroke-width="0.4"/>
        <line x1="28" y1="10" x2="22" y2="20"
              stroke="rgba(196,160,74,0.15)" stroke-width="0.4"/>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Astronomy<br>Observation<br>Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Under the Same Stars,<br>Always Wondering</div>
      <div class="features">
        <span class="feature-badge">40 Sessions</span>
        <span class="feature-badge">Object Log</span>
        <span class="feature-badge">Star Charts</span>
        <span class="feature-badge">Gear Ref</span>
      </div>
      <div class="tagline">For Amateur Astronomers &amp; Stargazers</div>
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
