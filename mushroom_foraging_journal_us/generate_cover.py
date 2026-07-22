#!/usr/bin/env python3
"""
Mushroom Foraging Journal — KDP Full Wrap Cover Generator
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
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "mushroom_foraging_journal_cover_V1.0.html")

# KDP cover specs
TRIM_W = 6.0          # inches
TRIM_H = 9.0
PAGES = 112
SPINE = PAGES * 0.0025   # cream paper = 0.28"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.53"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors — Forest / Sage / Mushroom theme (quiet luxury aesthetic)
C_CHARCOAL = "#141A12"   # near-black forest charcoal
C_DARK     = "#1E2820"   # dark moss
C_FOREST   = "#283428"   # dark forest green
C_MOSS_D   = "#3D4A38"   # dark moss
C_MOSS     = "#5A7042"   # moss green
C_SAGE     = "#7A8B6A"   # sage green accent
C_EARTH    = "#8B6F47"   # earthy brown
C_GOLD     = "#C4A04A"   # muted gold
C_GOLD_L   = "#D4C49A"   # light gold
C_CREAM    = "#FAF8F2"   # warm cream
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 40%, {C_FOREST} 100%);
  padding: 0.75in 0.5in 0.45in 0.5in;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  overflow: hidden;
}}

/* Subtle sage texture */
.back-cover::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 24px 14px at 15% 25%, {C_SAGE}, transparent),
    radial-gradient(ellipse 22px 13px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 26px 15px at 70% 70%, {C_SAGE}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 18px 11px at 50% 50%, {C_SAGE}, transparent),
    radial-gradient(ellipse 22px 13px at 10% 60%, {C_GOLD}, transparent);
}}

/* Decorative circle */
.back-cover::after {{
  content: '';
  position: absolute;
  top: -0.3in; right: -0.3in;
  width: 1.2in; height: 1.2in;
  border-radius: 50%;
  background: rgba(122, 139, 106, 0.08);
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
  background: {C_SAGE};
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
    radial-gradient(ellipse 10px 6px at 50% 20%, {C_SAGE}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 50%, {C_GOLD}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 80%, {C_SAGE}, transparent);
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 25%, {C_MOSS_D} 55%, {C_DARK} 85%, {C_CHARCOAL} 100%);
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
    radial-gradient(ellipse 40px 24px at 15% 25%, {C_SAGE}, transparent),
    radial-gradient(ellipse 34px 20px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 38px 22px at 70% 70%, {C_SAGE}, transparent),
    radial-gradient(ellipse 28px 18px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 24px 15px at 50% 50%, {C_SAGE}, transparent),
    radial-gradient(ellipse 30px 18px at 10% 60%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 14px at 90% 45%, {C_SAGE}, transparent),
    radial-gradient(ellipse 20px 12px at 40% 90%, {C_GOLD}, transparent),
    radial-gradient(ellipse 18px 11px at 60% 35%, {C_SAGE}, transparent);
}}

/* ============ MUSHROOM (SVG) ============ */
.mushroom-wrap {{
  width: 140px; height: 180px;
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
  <title>Mushroom Foraging Journal — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every find tells a story.</strong>
        From the first morel of spring to the last chanterelle of fall,
        this journal helps you document every specimen you encounter
        &mdash; its habitat, its features, and the moment you found it.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>40 two-page foraging logs with full specimen details</li>
        <li>Mushroom anatomy and identification guide</li>
        <li>Habitat reference and seasonal fruiting calendar</li>
        <li>Foraging safety rules and best practices</li>
        <li>Species checklist to build your life list</li>
        <li>Spot and location tracker for productive areas</li>
        <li>Year-in-review favorites and personal milestones</li>
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
    <div class="spine-text">Mushroom Foraging Journal</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Mushroom illustration (SVG line art) -->
    <div class="mushroom-wrap">
      <svg viewBox="0 0 140 180" width="140" height="180" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="capGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_SAGE}" stop-opacity="0.6"/>
            <stop offset="100%" stop-color="{C_MOSS_D}" stop-opacity="0.8"/>
          </linearGradient>
          <linearGradient id="stemGrad" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="rgba(250,248,242,0)"/>
            <stop offset="40%" stop-color="rgba(250,248,242,0.15)"/>
            <stop offset="60%" stop-color="rgba(250,248,242,0.06)"/>
            <stop offset="100%" stop-color="rgba(250,248,242,0)"/>
          </linearGradient>
        </defs>

        <!-- Large mushroom cap — classic dome -->
        <path d="M 28 52
                 Q 28 18 70 14
                 Q 112 18 112 52
                 Q 112 60 104 62
                 L 36 62
                 Q 28 60 28 52 Z"
              fill="url(#capGrad)"
              stroke="rgba(196,160,74,0.5)" stroke-width="1.8" stroke-linejoin="round"/>

        <!-- Cap highlight -->
        <ellipse cx="56" cy="28" rx="18" ry="8"
                 fill="rgba(250,248,242,0.12)" transform="rotate(-18 56 28)"/>

        <!-- Gills under cap — radiating lines -->
        <path d="M 38 62 L 42 74 M 48 62 L 50 78 M 58 62 L 58 80
                 M 70 62 L 70 80 M 82 62 L 82 78 M 92 62 L 90 74 M 102 62 L 98 72"
              stroke="rgba(196,160,74,0.3)" stroke-width="0.8" fill="none"/>

        <!-- Gills arc (underside of cap) -->
        <path d="M 36 62 Q 70 78 104 62"
              stroke="rgba(196,160,74,0.35)" stroke-width="1.2" fill="rgba(122,139,106,0.05)"/>

        <!-- Ring/annulus -->
        <ellipse cx="70" cy="86" rx="16" ry="4"
                 fill="rgba(196,160,74,0.08)"
                 stroke="rgba(196,160,74,0.4)" stroke-width="1.2"/>

        <!-- Stem -->
        <path d="M 58 62 L 56 150 Q 56 158 62 160 L 78 160 Q 84 158 82 150 L 80 62"
              fill="url(#stemGrad)"
              stroke="rgba(196,160,74,0.35)" stroke-width="1.2" stroke-linejoin="round"/>

        <!-- Stem outline left -->
        <path d="M 58 62 Q 57 100 56 150"
              stroke="rgba(196,160,74,0.25)" stroke-width="0.8" fill="none"/>

        <!-- Stem outline right -->
        <path d="M 80 62 Q 81 100 82 150"
              stroke="rgba(196,160,74,0.25)" stroke-width="0.8" fill="none"/>

        <!-- Volva/base cup -->
        <ellipse cx="70" cy="160" rx="20" ry="6"
                 fill="rgba(122,139,106,0.06)"
                 stroke="rgba(196,160,74,0.4)" stroke-width="1.2"/>

        <!-- Base shadow -->
        <ellipse cx="70" cy="168" rx="26" ry="3"
                 fill="rgba(0,0,0,0.3)"/>

        <!-- Small companion mushroom -->
        <path d="M 104 118 Q 104 100 118 98 Q 132 100 132 118 Q 132 122 128 123 L 108 123 Q 104 122 104 118 Z"
              fill="url(#capGrad)" opacity="0.7"
              stroke="rgba(196,160,74,0.35)" stroke-width="1" stroke-linejoin="round"/>
        <path d="M 110 123 Q 110 135 109 148 Q 109 153 112 154 L 126 154 Q 129 153 129 148 Q 128 135 128 123"
              fill="rgba(250,248,242,0.03)"
              stroke="rgba(196,160,74,0.25)" stroke-width="1" stroke-linejoin="round"/>

        <!-- Small companion base -->
        <ellipse cx="119" cy="154" rx="12" ry="3"
                 fill="rgba(122,139,106,0.05)"
                 stroke="rgba(196,160,74,0.3)" stroke-width="0.8"/>

        <!-- Spore/particle lines rising -->
        <path d="M 40 8 Q 38 0 42 -4" stroke="rgba(196,160,74,0.2)" stroke-width="1" fill="none"/>
        <path d="M 70 4 Q 72 -4 68 -8" stroke="rgba(196,160,74,0.15)" stroke-width="1" fill="none"/>
        <path d="M 98 6 Q 100 -2 96 -6" stroke="rgba(196,160,74,0.15)" stroke-width="1" fill="none"/>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Mushroom<br>Foraging Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Track Every Find,<br>Every Habitat, Every Season</div>
      <div class="features">
        <span class="feature-badge">40 Foraging Logs</span>
        <span class="feature-badge">Species ID Guide</span>
        <span class="feature-badge">Habitat Tracker</span>
        <span class="feature-badge">Seasonal Calendar</span>
      </div>
      <div class="tagline">For Mushroom Hunters &amp; Nature Lovers</div>
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
