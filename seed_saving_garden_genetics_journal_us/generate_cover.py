#!/usr/bin/env python3
"""
Seed Saving & Garden Genetics Journal — KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Trim: 6" x 9"
Pages: 106 (cream paper)
Spine: 106 x 0.0025 = 0.265"
Bleed: 0.125" all outer edges
Full cover: 12.515 x 9.25 in
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "seed_saving_garden_genetics_journal_cover_V1.0.html")

TRIM_W = 6.0
TRIM_H = 9.0
PAGES = 106
SPINE = PAGES * 0.0025   # 0.265"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.515"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors
C_CHARCOAL = "#161616"
C_DARK     = "#1E1E1E"
C_WHEAT_D  = "#1A1810"
C_GOLD     = "#C4A04A"
C_GOLD_L   = "#D4B896"
C_SAGE     = "#5A7A4A"
C_SAGE_L   = "#7A9A6A"
C_SAGE_X   = "#9ABA8A"
C_RUST     = "#A05A30"
C_BROWN    = "#6B4423"
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 35%, {C_WHEAT_D} 100%);
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
    radial-gradient(ellipse 26px 16px at 15% 25%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 14px at 80% 15%, {C_SAGE_L}, transparent),
    radial-gradient(ellipse 24px 15px at 70% 70%, {C_RUST}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 18px 11px at 50% 50%, {C_SAGE_L}, transparent),
    radial-gradient(ellipse 22px 13px at 10% 60%, {C_RUST}, transparent);
}}

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
  box-shadow: 0 0 3px rgba(196,160,74,0.4);
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

.spine::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 10px 6px at 50% 20%, {C_GOLD}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 50%, {C_SAGE_L}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 80%, {C_RUST}, transparent);
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 20%, {C_WHEAT_D} 55%, {C_DARK} 85%, {C_CHARCOAL} 100%);
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
    radial-gradient(ellipse 38px 23px at 15% 25%, {C_GOLD}, transparent),
    radial-gradient(ellipse 32px 19px at 80% 15%, {C_SAGE_L}, transparent),
    radial-gradient(ellipse 36px 22px at 70% 70%, {C_RUST}, transparent),
    radial-gradient(ellipse 26px 16px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 14px at 50% 50%, {C_SAGE_L}, transparent),
    radial-gradient(ellipse 28px 17px at 10% 60%, {C_RUST}, transparent),
    radial-gradient(ellipse 20px 12px at 90% 45%, {C_GOLD}, transparent),
    radial-gradient(ellipse 18px 11px at 40% 90%, {C_SAGE_L}, transparent),
    radial-gradient(ellipse 16px 10px at 60% 35%, {C_GOLD}, transparent);
}}

/* ============ SEED ENVELOPE (SVG) ============ */
.seed-wrap {{
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
  background: {C_GOLD};
  margin: 16px auto;
}}

.subtitle {{
  font-size: 11.5pt;
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
  border: 1px solid rgba(196,160,74,0.45);
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
  <title>Seed Saving & Garden Genetics Journal — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every seed is a link in a living chain stretching back millennia.</strong>
        This journal helps you become a seed saver &mdash; preserving heritage
        varieties, adapting crops to your garden, and building a personal
        seed library that grows more valuable with every season.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>40 two-page variety logs (identity + seed record)</li>
        <li>Pollination guide for 15 common garden crops</li>
        <li>Seed processing methods (dry and wet)</li>
        <li>Germination testing protocol and viability chart</li>
        <li>Storage guide for maximum seed longevity</li>
        <li>10 garden plant families with crossing rules</li>
        <li>Seed library inventory (48 entries)</li>
        <li>Seed swap/exchange log and acquisition wishlist</li>
        <li>Year-in-review and garden layout planning pages</li>
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
    <div class="spine-text">Seed Saving Journal</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Seed envelope illustration (SVG) -->
    <div class="seed-wrap">
      <svg viewBox="0 0 110 180" width="110" height="180" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="envGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_GOLD_L}" stop-opacity="0.15"/>
            <stop offset="100%" stop-color="{C_GOLD}" stop-opacity="0.08"/>
          </linearGradient>
          <linearGradient id="leafGrad" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="{C_SAGE_X}" stop-opacity="0.20"/>
            <stop offset="100%" stop-color="{C_SAGE}" stop-opacity="0.10"/>
          </linearGradient>
        </defs>

        <!-- Seed envelope body -->
        <rect x="20" y="50" width="70" height="85" rx="3"
              fill="url(#envGrad)"
              stroke="rgba(196,160,74,0.35)" stroke-width="1.5"/>

        <!-- Envelope flap (triangle at top) -->
        <polygon points="20,50 55,30 90,50"
                 fill="rgba(180,150,110,0.10)"
                 stroke="rgba(196,160,74,0.25)" stroke-width="1"
                 stroke-linejoin="round"/>

        <!-- Flap fold line -->
        <line x1="20" y1="50" x2="90" y2="50"
              stroke="rgba(196,160,74,0.20)" stroke-width="0.8"/>

        <!-- Label rectangle -->
        <rect x="32" y="65" width="46" height="28" rx="2"
              fill="rgba(250,248,244,0.05)"
              stroke="rgba(196,160,74,0.20)" stroke-width="1"/>

        <!-- Label text lines -->
        <line x1="36" y1="73" x2="74" y2="73"
              stroke="rgba(196,160,74,0.15)" stroke-width="0.6"/>
        <line x1="36" y1="79" x2="68" y2="79"
              stroke="rgba(196,160,74,0.12)" stroke-width="0.5"/>
        <line x1="36" y1="85" x2="72" y2="85"
              stroke="rgba(196,160,74,0.12)" stroke-width="0.5"/>

        <!-- Envelope bottom fold -->
        <line x1="20" y1="135" x2="90" y2="135"
              stroke="rgba(196,160,74,0.15)" stroke-width="0.6"/>

        <!-- Seeds spilling out (top, above envelope) -->
        <ellipse cx="50" cy="22" rx="3" ry="4"
                 fill="rgba(196,160,74,0.30)"
                 transform="rotate(-20 50 22)"/>
        <ellipse cx="42" cy="16" rx="2.5" ry="3.5"
                 fill="rgba(160,90,48,0.25)"
                 transform="rotate(15 42 16)"/>
        <ellipse cx="60" cy="20" rx="2.5" ry="3.5"
                 fill="rgba(122,154,106,0.25)"
                 transform="rotate(-35 60 20)"/>
        <circle cx="56" cy="12" r="2" fill="rgba(196,160,74,0.20)"/>
        <circle cx="46" cy="8" r="1.5" fill="rgba(180,150,110,0.15)"/>

        <!-- Sprout growing from envelope -->
        <path d="M 55 30 Q 55 20 55 14"
              fill="none"
              stroke="rgba(122,154,106,0.30)" stroke-width="1.5"
              stroke-linecap="round"/>

        <!-- Sprout leaves -->
        <ellipse cx="49" cy="22" rx="4" ry="2.5"
                 fill="url(#leafGrad)"
                 stroke="rgba(122,154,106,0.25)" stroke-width="0.8"
                 transform="rotate(-30 49 22)"/>
        <ellipse cx="61" cy="20" rx="4" ry="2.5"
                 fill="url(#leafGrad)"
                 stroke="rgba(122,154,106,0.25)" stroke-width="0.8"
                 transform="rotate(30 61 20)"/>

        <!-- Decorative leaf (left side) -->
        <ellipse cx="10" cy="80" rx="8" ry="4"
                 fill="url(#leafGrad)"
                 stroke="rgba(122,154,106,0.20)" stroke-width="0.8"
                 transform="rotate(-30 10 80)"/>
        <line x1="6" y1="84" x2="14" y2="76"
              stroke="rgba(122,154,106,0.15)" stroke-width="0.5"/>

        <!-- Decorative leaf (right side) -->
        <ellipse cx="100" cy="95" rx="7" ry="3.5"
                 fill="url(#leafGrad)"
                 stroke="rgba(122,154,106,0.18)" stroke-width="0.8"
                 transform="rotate(25 100 95)"/>
        <line x1="96" y1="92" x2="104" y2="98"
              stroke="rgba(122,154,106,0.12)" stroke-width="0.5"/>

        <!-- Seeds at bottom (scattered) -->
        <ellipse cx="35" cy="150" rx="3" ry="2"
                 fill="rgba(160,90,48,0.20)"
                 transform="rotate(-15 35 150)"/>
        <ellipse cx="72" cy="155" rx="2.5" ry="1.5"
                 fill="rgba(196,160,74,0.18)"
                 transform="rotate(20 72 155)"/>
        <ellipse cx="55" cy="162" rx="3" ry="2"
                 fill="rgba(122,154,106,0.15)"
                 transform="rotate(-25 55 162)"/>

        <!-- Sparkle accents -->
        <g opacity="0.6">
          <circle cx="18" cy="40" r="2" fill="rgba(196,160,74,0.4)"/>
          <circle cx="18" cy="40" r="0.8" fill="rgba(250,248,244,0.6)"/>
          <circle cx="95" cy="35" r="1.5" fill="rgba(122,154,106,0.4)"/>
          <circle cx="5" cy="120" r="1" fill="rgba(250,248,244,0.25)"/>
          <circle cx="100" cy="140" r="1.5" fill="rgba(196,160,74,0.3)"/>
        </g>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Seed Saving &amp;<br>Garden Genetics<br>Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Preserving Heritage,<br>One Seed at a Time</div>
      <div class="features">
        <span class="feature-badge">40 Variety Logs</span>
        <span class="feature-badge">Pollination Guide</span>
        <span class="feature-badge">Germination Tests</span>
        <span class="feature-badge">Seed Library</span>
      </div>
      <div class="tagline">For Homesteaders &amp; Heritage Gardeners</div>
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
