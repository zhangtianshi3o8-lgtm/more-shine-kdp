#!/usr/bin/env python3
"""
Bird Watching Journal — KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Generates a print-ready full wrap cover (back + spine + front) as
standalone HTML. Export with Chrome headless to PDF.

Trim: 6" x 9"
Pages: 120 (cream paper)
Spine: 120 x 0.0025 = 0.30"
Bleed: 0.125" all outer edges
Full cover: 12.55 x 9.25 in
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "bird_watching_journal_cover_V1.0.html")

# KDP cover specs
TRIM_W = 6.0          # inches
TRIM_H = 9.0
PAGES = 120
SPINE = PAGES * 0.0025   # cream paper = 0.30"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.55"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors — Forest / Nature theme (quiet luxury aesthetic)
C_CHARCOAL = "#141A12"   # near-black with forest undertone
C_DARK     = "#1a3608"   # deep forest
C_BROWN    = "#2A2520"   # dark earth
C_FOREST_D = "#1A3608"   # dark forest green
C_FOREST   = "#2D5016"   # forest green
C_FOREST_L = "#3A6B1F"   # lighter forest
C_EARTH    = "#6B5B3F"   # earth brown
C_GOLD     = "#C8A441"   # forest gold
C_GOLD_L   = "#D4B896"   # light gold
C_CREAM    = "#FAF6F0"   # cream
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

/* Subtle forest texture */
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
  background: rgba(200, 164, 65, 0.08);
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 25%, {C_FOREST_D} 55%, {C_DARK} 85%, {C_CHARCOAL} 100%);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: {BLEED}in {BLEED}in {BLEED}in {BLEED}in;
}}

/* Subtle forest texture on front */
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

/* ============ BIRD ILLUSTRATION (SVG) ============ */
.bird-wrap {{
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
  border: 1px solid rgba(200,164,65,0.4);
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
  <title>Bird Watching Journal — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every bird tells a story.</strong>
        From the first flash of color in the trees to the familiar song
        at dawn, this journal helps you capture every sighting, every
        species, and every moment in the field.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>Sighting logs with full identification fields</li>
        <li>Bird habitat and seasonal reference guides</li>
        <li>Life list to track every species you've seen</li>
        <li>Trip journal for birding adventures</li>
        <li>Backyard birding log</li>
        <li>Monthly migration tracker</li>
        <li>Birder profile and birding gear pages</li>
        <li>Large 6&quot; x 9&quot; format &mdash; easy to write in</li>
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
    <div class="spine-text">Bird Watching Journal</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Bird illustration (SVG line art) -->
    <div class="bird-wrap">
      <svg viewBox="0 0 120 170" width="120" height="170" xmlns="http://www.w3.org/2000/svg">
        <!-- Branch (curved line) -->
        <path d="M 10 112 Q 40 104 60 110 Q 80 116 112 106"
              stroke="rgba(250,246,240,0.55)" stroke-width="2.2" fill="none" stroke-linecap="round"/>
        <!-- Small branch twig -->
        <path d="M 68 110 Q 72 100 76 90"
              stroke="rgba(250,246,240,0.40)" stroke-width="1.5" fill="none" stroke-linecap="round"/>
        <!-- Small leaf on twig -->
        <path d="M 76 90 Q 82 86 84 92 Q 80 96 76 90 Z"
              stroke="rgba(250,246,240,0.35)" stroke-width="1" fill="rgba(58,107,31,0.25)"/>

        <!-- Bird body (finch/sparrow silhouette, line art) -->
        <!-- Tail -->
        <path d="M 30 82 L 18 78 L 22 88 L 16 92 L 30 90 Z"
              stroke="rgba(250,246,240,0.55)" stroke-width="1.8" fill="none" stroke-linejoin="round"/>

        <!-- Main body -->
        <path d="M 30 90
                 Q 28 75 40 68
                 Q 52 60 66 64
                 Q 80 68 86 78
                 Q 88 86 82 92
                 Q 74 96 64 96
                 Q 50 96 40 94
                 Q 32 92 30 90 Z"
              stroke="rgba(250,246,240,0.55)" stroke-width="1.8" fill="none" stroke-linejoin="round"/>

        <!-- Head -->
        <path d="M 70 62
                 Q 82 56 86 50
                 Q 92 48 96 52
                 Q 98 58 94 62
                 Q 90 68 82 70
                 Q 72 72 70 62 Z"
              stroke="rgba(250,246,240,0.55)" stroke-width="1.8" fill="none" stroke-linejoin="round"/>

        <!-- Beak -->
        <path d="M 96 56 L 108 54 L 96 60 Z"
              stroke="rgba(250,246,240,0.55)" stroke-width="1.5" fill="none" stroke-linejoin="round"/>

        <!-- Eye -->
        <circle cx="89" cy="56" r="1.8"
                stroke="rgba(250,246,240,0.55)" stroke-width="1.2" fill="none"/>

        <!-- Wing detail -->
        <path d="M 48 76 Q 58 72 70 78 Q 74 84 66 88 Q 54 88 48 76 Z"
              stroke="rgba(250,246,240,0.40)" stroke-width="1.5" fill="none" stroke-linejoin="round"/>

        <!-- Wing feather lines -->
        <path d="M 52 80 Q 58 82 62 80"
              stroke="rgba(250,246,240,0.30)" stroke-width="1" fill="none" stroke-linecap="round"/>
        <path d="M 55 84 Q 61 86 65 84"
              stroke="rgba(250,246,240,0.30)" stroke-width="1" fill="none" stroke-linecap="round"/>

        <!-- Legs -->
        <path d="M 56 96 L 54 108 L 50 112"
              stroke="rgba(250,246,240,0.50)" stroke-width="1.5" fill="none" stroke-linecap="round"/>
        <path d="M 66 96 L 68 108 L 72 112"
              stroke="rgba(250,246,240,0.50)" stroke-width="1.5" fill="none" stroke-linecap="round"/>

        <!-- Small toes on branch -->
        <path d="M 50 112 L 47 113 M 50 112 L 53 113"
              stroke="rgba(250,246,240,0.40)" stroke-width="1" fill="none" stroke-linecap="round"/>
        <path d="M 72 112 L 69 113 M 72 112 L 75 113"
              stroke="rgba(250,246,240,0.40)" stroke-width="1" fill="none" stroke-linecap="round"/>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Bird Watching<br>Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Your Field Companion for<br>Birding Adventures &amp; Discoveries</div>
      <div class="features">
        <span class="feature-badge">Sighting Logs</span>
        <span class="feature-badge">Life List</span>
        <span class="feature-badge">Trip Journal</span>
        <span class="feature-badge">Habitat Guide</span>
      </div>
      <div class="tagline">For Birders &amp; Nature Lovers</div>
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
