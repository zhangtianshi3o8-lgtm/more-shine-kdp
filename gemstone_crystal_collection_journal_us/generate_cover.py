#!/usr/bin/env python3
"""
Gemstone & Crystal Collection Journal — KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Trim: 6" x 9"
Pages: 112 (cream paper)
Spine: 112 x 0.0025 = 0.280"
Bleed: 0.125" all outer edges
Full cover: 12.53 x 9.25 in
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "gemstone_crystal_collection_journal_cover_V1.0.html")

TRIM_W = 6.0
TRIM_H = 9.0
PAGES = 112
SPINE = PAGES * 0.0025   # 0.280"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.53"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors
C_CHARCOAL = "#161616"
C_DARK     = "#1E1E1E"
C_AMETHYST_D = "#1A1520"
C_AMETHYST = "#6B4C8A"
C_AMETHYST_L = "#8B6FB5"
C_AMETHYST_X = "#A892C4"
C_SILVER   = "#B0B0B0"
C_SILVER_L = "#C8C8C8"
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 35%, {C_AMETHYST_D} 100%);
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
    radial-gradient(ellipse 26px 16px at 15% 25%, {C_AMETHYST_L}, transparent),
    radial-gradient(ellipse 22px 14px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 24px 15px at 70% 70%, {C_SILVER}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_AMETHYST_L}, transparent),
    radial-gradient(ellipse 18px 11px at 50% 50%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 13px at 10% 60%, {C_SILVER}, transparent);
}}

.back-cover::after {{
  content: '';
  position: absolute;
  top: -0.3in; right: -0.3in;
  width: 1.2in; height: 1.2in;
  border-radius: 50%;
  background: rgba(139, 111, 181, 0.08);
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
  color: {C_AMETHYST_X};
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
  background: {C_AMETHYST_L};
  border-radius: 50%;
  box-shadow: 0 0 3px rgba(139,111,181,0.4);
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
  color: {C_AMETHYST_L};
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
    radial-gradient(ellipse 10px 6px at 50% 20%, {C_AMETHYST_L}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 50%, {C_GOLD}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 80%, {C_SILVER}, transparent);
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
  color: {C_AMETHYST_L};
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 20%, {C_AMETHYST_D} 55%, {C_DARK} 85%, {C_CHARCOAL} 100%);
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
    radial-gradient(ellipse 38px 23px at 15% 25%, {C_AMETHYST_L}, transparent),
    radial-gradient(ellipse 32px 19px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 36px 22px at 70% 70%, {C_SILVER}, transparent),
    radial-gradient(ellipse 26px 16px at 25% 80%, {C_AMETHYST_L}, transparent),
    radial-gradient(ellipse 22px 14px at 50% 50%, {C_GOLD}, transparent),
    radial-gradient(ellipse 28px 17px at 10% 60%, {C_SILVER}, transparent),
    radial-gradient(ellipse 20px 12px at 90% 45%, {C_AMETHYST_L}, transparent),
    radial-gradient(ellipse 18px 11px at 40% 90%, {C_GOLD}, transparent),
    radial-gradient(ellipse 16px 10px at 60% 35%, {C_SILVER}, transparent);
}}

/* ============ CRYSTAL CLUSTER (SVG) ============ */
.crystal-wrap {{
  width: 130px; height: 180px;
  position: relative;
  margin: 0 auto 22px;
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
  background: {C_AMETHYST_L};
  margin: 16px auto;
}}

.subtitle {{
  font-size: 11.5pt;
  color: {C_AMETHYST_X};
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
  border: 1px solid rgba(139,111,181,0.45);
  color: {C_AMETHYST_L};
  font-size: 7.5pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 10px;
  border-radius: 3px;
  text-transform: uppercase;
}}

.tagline {{
  font-size: 9pt;
  color: {C_SILVER_L};
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
  color: {C_AMETHYST_L};
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
  <title>Gemstone & Crystal Collection Journal — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every crystal tells a story. This journal helps you remember them all.</strong>
        From the first tumbled stone to a curated collection of rare specimens,
        this journal transforms your passion into a personal crystal encyclopedia.
        Document physical properties, metaphysical associations, and your own
        experiences with each piece.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_AMETHYST_X}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>40 two-page specimen logs (identity + metaphysical)</li>
        <li>Mohs hardness scale with care implications</li>
        <li>Seven crystal systems reference guide</li>
        <li>Chakra and color association chart</li>
        <li>Cleansing and charging methods guide</li>
        <li>Safety notes for fragile and toxic minerals</li>
        <li>Collection overview, supplier directory, storage plan</li>
        <li>Crystal grid and meditation session records</li>
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
    <div class="spine-text">Gemstone & Crystal Journal</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Crystal cluster illustration (SVG) -->
    <div class="crystal-wrap">
      <svg viewBox="0 0 130 180" width="130" height="180" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="amethystGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_AMETHYST_X}" stop-opacity="0.25"/>
            <stop offset="40%" stop-color="{C_AMETHYST}" stop-opacity="0.20"/>
            <stop offset="80%" stop-color="{C_AMETHYST_D}" stop-opacity="0.15"/>
          </linearGradient>
          <linearGradient id="goldGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_GOLD_L}" stop-opacity="0.20"/>
            <stop offset="100%" stop-color="{C_GOLD}" stop-opacity="0.10"/>
          </linearGradient>
          <linearGradient id="silverGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_SILVER_L}" stop-opacity="0.20"/>
            <stop offset="100%" stop-color="{C_SILVER}" stop-opacity="0.08"/>
          </linearGradient>
        </defs>

        <!-- Large central amethyst point -->
        <polygon points="65,10 80,30 78,140 52,140 50,30"
                 fill="url(#amethystGrad)"
                 stroke="rgba(168,146,196,0.45)" stroke-width="1.5"
                 stroke-linejoin="round"/>

        <!-- Crystal facet lines (central) -->
        <line x1="65" y1="10" x2="65" y2="140"
              stroke="rgba(250,248,244,0.12)" stroke-width="1"/>
        <line x1="65" y1="10" x2="52" y2="140"
              stroke="rgba(250,248,244,0.08)" stroke-width="0.6"/>
        <line x1="65" y1="10" x2="78" y2="140"
              stroke="rgba(250,248,244,0.08)" stroke-width="0.6"/>

        <!-- Left gold crystal -->
        <polygon points="30,45 40,60 39,135 21,135 20,60"
                 fill="url(#goldGrad)"
                 stroke="rgba(196,160,74,0.40)" stroke-width="1.5"
                 stroke-linejoin="round"/>
        <line x1="30" y1="45" x2="30" y2="135"
              stroke="rgba(250,248,244,0.10)" stroke-width="0.6"/>

        <!-- Right silver crystal -->
        <polygon points="100,50 110,65 109,135 91,135 90,65"
                 fill="url(#silverGrad)"
                 stroke="rgba(176,176,176,0.40)" stroke-width="1.5"
                 stroke-linejoin="round"/>
        <line x1="100" y1="50" x2="100" y2="135"
              stroke="rgba(250,248,244,0.10)" stroke-width="0.6"/>

        <!-- Small back crystal (amethyst, faded) -->
        <polygon points="50,25 58,40 57,135 43,135 42,40"
                 fill="rgba(107,76,138,0.10)"
                 stroke="rgba(107,76,138,0.25)" stroke-width="1"
                 stroke-linejoin="round"/>

        <!-- Crystal base / matrix -->
        <ellipse cx="65" cy="142" rx="55" ry="6"
                 fill="rgba(250,248,244,0.04)"/>
        <path d="M 12 142 Q 65 148 118 142 L 115 150 Q 65 154 15 150 Z"
              fill="rgba(250,248,244,0.05)"
              stroke="rgba(176,176,176,0.15)" stroke-width="0.8"/>

        <!-- Sparkle highlights -->
        <g opacity="0.7">
          <!-- Top sparkle -->
          <path d="M 65 2 L 66 8 L 72 9 L 66 10 L 65 16 L 64 10 L 58 9 L 64 8 Z"
                fill="rgba(250,248,244,0.5)"/>

          <!-- Left sparkle -->
          <circle cx="25" cy="35" r="2" fill="rgba(196,160,74,0.5)"/>
          <circle cx="25" cy="35" r="0.8" fill="rgba(250,248,244,0.7)"/>

          <!-- Right sparkle -->
          <circle cx="112" cy="38" r="1.5" fill="rgba(176,176,176,0.5)"/>
          <circle cx="112" cy="38" r="0.6" fill="rgba(250,248,244,0.7)"/>

          <!-- Mid sparkle -->
          <path d="M 95 105 L 96 110 L 101 111 L 96 112 L 95 117 L 94 112 L 89 111 L 94 110 Z"
                fill="rgba(168,146,196,0.4)"/>

          <!-- Small dot sparkles -->
          <circle cx="40" cy="100" r="1" fill="rgba(250,248,244,0.3)"/>
          <circle cx="85" cy="75" r="1" fill="rgba(250,248,244,0.3)"/>
          <circle cx="55" cy="60" r="0.8" fill="rgba(250,248,244,0.25)"/>
        </g>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Gemstone &amp; Crystal<br>Collection Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Catalog Every Specimen,<br>Every Property, Every Meaning</div>
      <div class="features">
        <span class="feature-badge">40 Specimen Logs</span>
        <span class="feature-badge">Mohs Hardness</span>
        <span class="feature-badge">Chakra Guide</span>
        <span class="feature-badge">Care &amp; Cleansing</span>
      </div>
      <div class="tagline">For Collectors, Healers &amp; Crystal Enthusiasts</div>
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
