#!/usr/bin/env python3
"""
Sake Tasting Journal — KDP Full Wrap Cover Generator
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
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "sake_tasting_journal_us_cover_V1.0.html")

# KDP cover specs
TRIM_W = 6.0          # inches
TRIM_H = 9.0
PAGES = 112
SPINE = PAGES * 0.0025   # cream paper = 0.28"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.53"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors — Indigo / Charcoal / Gold theme (quiet luxury aesthetic)
C_CHARCOAL = "#0F1628"   # near-black with indigo undertone
C_DARK     = "#16203A"   # deep indigo-navy
C_INDIGO_D = "#1A2A48"   # dark indigo
C_INDIGO   = "#1E3A5F"   # indigo — main accent
C_INDIGO_L = "#2A4A73"   # light indigo
C_GOLD     = "#C4A04A"   # muted gold
C_GOLD_L   = "#D4B896"   # light gold
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 40%, {C_INDIGO_D} 100%);
  padding: 0.75in 0.5in 0.45in 0.5in;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  overflow: hidden;
}}

/* Subtle indigo-gold texture */
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 25%, {C_INDIGO_D} 55%, {C_DARK} 85%, {C_CHARCOAL} 100%);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: {BLEED}in {BLEED}in {BLEED}in {BLEED}in;
}}

/* Subtle texture on front */
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

/* ============ TOKKURI (SAKE FLASK) SVG ============ */
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
  <title>Sake Tasting Journal — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every cup tells a story.</strong>
        From the first pour to the lingering finish, this journal
        helps you capture the character of every sake you taste
        &mdash; from crisp Junmai to aromatic Daiginjo.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>40 two-page tasting logs with full sake details</li>
        <li>Sake flavor wheel with 8 categories and 50+ notes</li>
        <li>Sake types guide and brewing terminology</li>
        <li>Sake regions reference (Niigata, Hyogo, Kyoto, and more)</li>
        <li>Sake shelf and bottle collection inventory pages</li>
        <li>Comprehensive prefectures checklist</li>
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
    <div class="spine-text">Sake Tasting Journal</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Tokkuri (sake flask) + ochoko (cup) illustration (SVG line art) -->
    <div class="glass-wrap">
      <svg viewBox="0 0 120 170" width="120" height="170" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <!-- Sake liquid gradient (clear with golden warmth) -->
          <linearGradient id="sake" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_GOLD_L}" stop-opacity="0.20"/>
            <stop offset="100%" stop-color="{C_GOLD}" stop-opacity="0.35"/>
          </linearGradient>
          <!-- Aroma wisp gradients (gold, fading upward) -->
          <linearGradient id="aroma1" x1="0" y1="1" x2="0" y2="0">
            <stop offset="0%" stop-color="{C_GOLD}" stop-opacity="0.0"/>
            <stop offset="100%" stop-color="{C_GOLD_L}" stop-opacity="0.55"/>
          </linearGradient>
          <linearGradient id="aroma2" x1="0" y1="1" x2="0" y2="0">
            <stop offset="0%" stop-color="{C_GOLD}" stop-opacity="0.0"/>
            <stop offset="100%" stop-color="{C_GOLD_L}" stop-opacity="0.4"/>
          </linearGradient>
          <linearGradient id="aroma3" x1="0" y1="1" x2="0" y2="0">
            <stop offset="0%" stop-color="{C_GOLD}" stop-opacity="0.0"/>
            <stop offset="100%" stop-color="{C_GOLD_L}" stop-opacity="0.45"/>
          </linearGradient>
        </defs>

        <!-- Aroma wisps rising from flask neck (drawn behind glass) -->
        <path d="M 50 22 Q 47 12 51 2 Q 49 -3 52 -8"
              stroke="url(#aroma1)" stroke-width="1.4" fill="none"
              stroke-linecap="round"/>
        <path d="M 60 22 Q 63 10 58 0 Q 61 -5 57 -10"
              stroke="url(#aroma2)" stroke-width="1.4" fill="none"
              stroke-linecap="round"/>
        <path d="M 70 22 Q 73 13 68 4 Q 71 -2 67 -7"
              stroke="url(#aroma3)" stroke-width="1.4" fill="none"
              stroke-linecap="round"/>

        <!-- Flask lip (top ellipse) -->
        <ellipse cx="60" cy="28" rx="14" ry="3"
                 stroke="rgba(250,246,240,0.55)" stroke-width="1.8" fill="none"/>

        <!-- Flask neck (narrow column) -->
        <path d="M 46 28 L 48 45 Q 48 48 50 50
                 M 74 28 L 72 45 Q 72 48 70 50"
              stroke="rgba(250,246,240,0.55)" stroke-width="1.8" fill="none"
              stroke-linejoin="round" stroke-linecap="round"/>

        <!-- Flask body — rounded teardrop shape -->
        <path d="M 50 50
                 Q 32 55 30 80
                 Q 28 105 36 118
                 Q 44 128 60 130
                 Q 76 128 84 118
                 Q 92 105 90 80
                 Q 88 55 70 50
                 Q 65 49 60 49
                 Q 55 49 50 50"
              stroke="rgba(250,246,240,0.55)" stroke-width="1.8" fill="none"
              stroke-linejoin="round" stroke-linecap="round"/>

        <!-- Sake liquid inside flask (from y=65 to bottom) -->
        <path d="M 36 72
                 Q 30 82 30 95
                 Q 28 110 38 120
                 Q 46 127 60 128
                 Q 74 127 82 120
                 Q 92 110 90 95
                 Q 88 82 84 72
                 Q 80 70 60 70
                 Q 40 70 36 72
                 Z"
              fill="url(#sake)"/>

        <!-- Liquid surface ellipse at y=72 -->
        <ellipse cx="60" cy="72" rx="24" ry="3"
                 fill="rgba(196,160,74,0.15)"/>
        <!-- Subtle shine highlight on liquid surface -->
        <ellipse cx="54" cy="71" rx="9" ry="1"
                 fill="rgba(250,246,240,0.12)"/>

        <!-- Flask body subtle shine highlight -->
        <path d="M 34 65 Q 30 88 34 110"
              stroke="rgba(250,246,240,0.15)" stroke-width="1" fill="none"/>

        <!-- Ochoko (small sake cup) beside flask, bottom-left -->
        <ellipse cx="22" cy="130" rx="12" ry="2.5"
                 stroke="rgba(250,246,240,0.50)" stroke-width="1.5" fill="none"/>
        <path d="M 10 130 Q 11 138 14 141 Q 18 143 22 143 Q 26 143 30 141 Q 33 138 34 130"
              stroke="rgba(250,246,240,0.50)" stroke-width="1.5" fill="none"
              stroke-linejoin="round"/>
        <!-- Sake in ochoko -->
        <path d="M 11 131 Q 12 137 15 139 Q 18 141 22 141 Q 26 141 29 139 Q 32 137 33 131"
              fill="rgba(196,160,74,0.12)"/>

        <!-- Base shadow -->
        <ellipse cx="60" cy="135" rx="32" ry="2.5"
                 fill="rgba(0,0,0,0.25)"/>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Sake Tasting<br>Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Discover Every Brew,<br>Every Aroma, Every Kura</div>
      <div class="features">
        <span class="feature-badge">40 Tasting Sessions</span>
        <span class="feature-badge">Flavor Wheel</span>
        <span class="feature-badge">Sake Shelf</span>
        <span class="feature-badge">Kura Guide</span>
      </div>
      <div class="tagline">For Sake Lovers &amp; Explorers</div>
    </div>

    <div class="publisher">More Shine Press</div>
  </div>
</div>
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Generated: {output_path}")
    print(f"Cover dimensions: {COVER_W:.4f}in x {COVER_H:.4f}in")
    print(f"Spine width: {SPINE:.4f}in ({PAGES}pp cream)")


if __name__ == "__main__":
    generate()
