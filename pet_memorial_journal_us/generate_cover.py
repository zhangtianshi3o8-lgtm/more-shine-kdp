#!/usr/bin/env python3
"""
Pet Memorial Journal — KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Generates a print-ready full wrap cover (back + spine + front) as
standalone HTML. Export with Chrome headless to PDF.

Trim: 6" x 9"
Pages: 60 (cream paper)
Spine: 60 x 0.0025 = 0.15"
Bleed: 0.125" all outer edges
Full cover: 12.40 x 9.25 in
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "pet_memorial_journal_us_cover_V1.0.html")

# KDP cover specs
TRIM_W = 6.0          # inches
TRIM_H = 9.0
PAGES = 60
SPINE = PAGES * 0.0025   # cream paper = 0.15"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.40"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors — Charcoal / Gold / Cream theme (quiet luxury aesthetic)
C_CHARCOAL = "#0F1A18"   # near-black warm charcoal
C_DARK     = "#16261F"   # slightly lighter charcoal
C_WARM_D   = "#1A2E26"   # deep brown-charcoal
C_MAUVE    = "#7A9B8E"   # soft mauve accent
C_GOLD     = "#8FA8A0"   # muted gold
C_GOLD_L   = "#B0C8BE"   # light gold
C_CREAM    = "#F6FAF8"   # warm cream
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 40%, {C_WARM_D} 100%);
  padding: 0.75in 0.5in 0.45in 0.5in;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  overflow: hidden;
}}

/* Subtle charcoal-gold texture */
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 25%, {C_WARM_D} 55%, {C_DARK} 85%, {C_CHARCOAL} 100%);
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

/* ============ PET SVG ============ */
.pet-wrap {{
  width: 130px; height: 150px;
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
  font-size: 30pt;
  font-weight: 700;
  color: {C_WHITE};
  line-height: 1.15;
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
  <title>In Loving Memory of My Pet — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Some loves leave paw prints on our hearts forever.</strong>
        This memorial journal offers a gentle, private space to honor
        the life of a beloved pet &mdash; to remember their quirks,
        cherish their photos, and write the words that still need
        to be said.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>Guided profile pages for your pet's story and personality</li>
        <li>8 two-page memory spreads with photo space</li>
        <li>Photo gallery with room for 36+ photos and captions</li>
        <li>Letter-writing pages for expressing what's in your heart</li>
        <li>Paw print keepsake page for a lasting impression</li>
        <li>The final goodbye and legacy reflection sections</li>
        <li>Words of comfort from literature's greatest voices</li>
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
    <div class="spine-text">In Loving Memory of My Pet</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Pet silhouette SVG line art -->
    <div class="pet-wrap">
      <svg viewBox="0 0 120 130" width="100" height="108" xmlns="http://www.w3.org/2000/svg">
        <!-- Toe pads -->
        <ellipse cx="25" cy="38" rx="10" ry="14" transform="rotate(-15 25 38)"
                 fill="rgba(196,160,74,0.15)" stroke="#8FA8A0" stroke-width="1.2" opacity="0.7"/>
        <ellipse cx="48" cy="25" rx="10" ry="15"
                 fill="rgba(196,160,74,0.18)" stroke="#8FA8A0" stroke-width="1.2" opacity="0.75"/>
        <ellipse cx="72" cy="25" rx="10" ry="15"
                 fill="rgba(196,160,74,0.18)" stroke="#8FA8A0" stroke-width="1.2" opacity="0.75"/>
        <ellipse cx="95" cy="38" rx="10" ry="14" transform="rotate(15 95 38)"
                 fill="rgba(196,160,74,0.15)" stroke="#8FA8A0" stroke-width="1.2" opacity="0.7"/>
        <!-- Main pad -->
        <path d="M 60 50 Q 30 55 25 75 Q 22 95 35 105 Q 50 112 60 112 Q 70 112 85 105 Q 98 95 95 75 Q 90 55 60 50 Z"
              fill="rgba(196,160,74,0.10)" stroke="#8FA8A0" stroke-width="1.5"/>
        <!-- Subtle highlight on main pad -->
        <ellipse cx="50" cy="72" rx="8" ry="5" fill="rgba(255,255,255,0.06)"/>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">In Loving Memory<br>of My Pet</div>
      <div class="accent-bar"></div>
      <div class="subtitle">A Memorial Journal and Keepsake</div>
      <div class="features">
        <span class="feature-badge">Memory Spreads</span>
        <span class="feature-badge">Photo Gallery</span>
        <span class="feature-badge">Paw Print Page</span>
        <span class="feature-badge">Letter Pages</span>
      </div>
      <div class="tagline">Cherish Every Memory</div>
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
