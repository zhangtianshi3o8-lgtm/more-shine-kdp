#!/usr/bin/env python3
"""
Pickleball Journal — KDP Full Wrap Cover Generator
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
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "pickleball_journal_cover_V1.0.html")

# KDP cover specs
TRIM_W = 6.0          # inches
TRIM_H = 9.0
PAGES = 112
SPINE = PAGES * 0.0025   # cream paper = 0.28"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.53"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors — Pickleball Court Navy theme (quiet luxury aesthetic)
C_NAVY_N   = "#0A1B2E"   # near-black navy
C_NAVY_D   = "#14254B"   # dark navy
C_NAVY_M   = "#1A3A6B"   # mid navy
C_NAVY_L   = "#2A5A8E"   # lighter navy
C_BLUE     = "#3A6A9E"   # blue accent
C_BLUE_L   = "#5A8ABE"   # lighter blue
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
  background: linear-gradient(165deg, {C_NAVY_N} 0%, {C_NAVY_D} 40%, {C_NAVY_M} 100%);
  padding: 0.75in 0.5in 0.45in 0.5in;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  overflow: hidden;
}}

/* Subtle navy texture */
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
  background: linear-gradient(180deg, {C_NAVY_N} 0%, {C_NAVY_D} 50%, {C_NAVY_N} 100%);
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
  background: linear-gradient(165deg, {C_NAVY_N} 0%, {C_NAVY_D} 25%, {C_NAVY_M} 55%, {C_NAVY_D} 85%, {C_NAVY_N} 100%);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: {BLEED}in {BLEED}in {BLEED}in {BLEED}in;
}}

/* Subtle navy texture on front */
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

/* ============ PICKLEBALL PADDLE & BALL (SVG) ============ */
.glass-wrap {{
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
  <title>Pickleball Journal — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every game tells a story.</strong>
        From the first serve to the final dink rally, your pickleball
        journey deserves to be documented with care. This journal gives
        you the structure to capture every match &mdash; every point,
        every partner, every tournament result.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>52 game tracker pages with scoring</li>
        <li>Game statistics and trend analysis</li>
        <li>Shot reference guide (serve, dink, drive)</li>
        <li>DUPR rating progression tracker</li>
        <li>Court and venue log</li>
        <li>Paddle and gear inventory</li>
        <li>Practice drills and goals tracker</li>
        <li>Season wrap-up with awards</li>
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
    <div class="spine-text">Pickleball Journal</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Pickleball paddle and ball illustration (SVG line art) -->
    <div class="glass-wrap">
      <svg viewBox="0 0 120 170" width="120" height="170" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="paddleGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_BLUE}" stop-opacity="0.9"/>
            <stop offset="100%" stop-color="{C_NAVY_L}" stop-opacity="0.95"/>
          </linearGradient>
          <radialGradient id="ballGrad" cx="0.35" cy="0.35" r="0.7">
            <stop offset="0%" stop-color="{C_GOLD_L}" stop-opacity="0.95"/>
            <stop offset="100%" stop-color="{C_GOLD}" stop-opacity="0.85"/>
          </radialGradient>
        </defs>

        <!-- Paddle head — rounded teardrop/octagonal (flat bottom, rounded top) -->
        <path d="M 42 18
                 C 30 18 22 28 22 42
                 L 22 82
                 C 22 88 27 92 33 92
                 L 87 92
                 C 93 92 98 88 98 82
                 L 98 42
                 C 98 28 90 18 78 18
                 Z"
              stroke="{C_GOLD}" stroke-width="2" fill="url(#paddleGrad)"
              stroke-linejoin="round" stroke-linecap="round"/>

        <!-- Paddle inner edge accent line -->
        <path d="M 46 24
                 C 36 24 28 31 28 42
                 L 28 78
                 C 28 82 31 86 35 86
                 L 85 86
                 C 89 86 92 82 92 78
                 L 92 42
                 C 92 31 84 24 74 24
                 Z"
              stroke="{C_GOLD_L}" stroke-width="0.8" fill="none"
              opacity="0.35"/>

        <!-- Paddle handle -->
        <rect x="52" y="92" width="16" height="32" rx="3" ry="3"
              stroke="{C_GOLD}" stroke-width="1.8" fill="rgba(58,106,158,0.5)"
              stroke-linejoin="round"/>

        <!-- Paddle grip lines -->
        <line x1="54" y1="98" x2="66" y2="98" stroke="{C_GOLD}" stroke-width="0.6" opacity="0.6"/>
        <line x1="54" y1="104" x2="66" y2="104" stroke="{C_GOLD}" stroke-width="0.6" opacity="0.6"/>
        <line x1="54" y1="110" x2="66" y2="110" stroke="{C_GOLD}" stroke-width="0.6" opacity="0.6"/>
        <line x1="54" y1="116" x2="66" y2="116" stroke="{C_GOLD}" stroke-width="0.6" opacity="0.6"/>

        <!-- Paddle buttcap -->
        <rect x="54" y="124" width="12" height="5" rx="2" ry="2"
              stroke="{C_GOLD}" stroke-width="1.5" fill="rgba(58,106,158,0.6)"/>

        <!-- Pickleball — small circle with perforated holes -->
        <circle cx="90" cy="135" r="14"
                stroke="{C_GOLD}" stroke-width="2" fill="url(#ballGrad)"/>

        <!-- Perforated holes on ball -->
        <circle cx="86" cy="132" r="1.5" fill="{C_NAVY_N}" opacity="0.7"/>
        <circle cx="93" cy="130" r="1.5" fill="{C_NAVY_N}" opacity="0.7"/>
        <circle cx="95" cy="137" r="1.5" fill="{C_NAVY_N}" opacity="0.7"/>
        <circle cx="88" cy="139" r="1.5" fill="{C_NAVY_N}" opacity="0.7"/>
        <circle cx="91" cy="135" r="1.5" fill="{C_NAVY_N}" opacity="0.7"/>

        <!-- Ball shadow -->
        <ellipse cx="90" cy="151" rx="10" ry="2"
                 fill="rgba(0,0,0,0.3)"/>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Pickleball<br>Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Track Every Game,<br>Every Partner, Every Tournament</div>
      <div class="features">
        <span class="feature-badge">52 Game Trackers</span>
        <span class="feature-badge">Stat Analysis</span>
        <span class="feature-badge">DUPR Rating Log</span>
        <span class="feature-badge">Tournament Tracker</span>
      </div>
      <div class="tagline">For Players &amp; Competitors</div>
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
