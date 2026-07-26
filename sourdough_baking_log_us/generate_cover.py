#!/usr/bin/env python3
"""
Sourdough Baking Log — KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Trim: 6" x 9"
Pages: 94 (cream paper)
Spine: 94 x 0.0025 = 0.235"
Bleed: 0.125" all outer edges
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "sourdough_baking_log_us_cover_V1.0.html")

TRIM_W = 6.0
TRIM_H = 9.0
PAGES = 94
SPINE = PAGES * 0.0025
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2
COVER_H = TRIM_H + BLEED * 2

# Colors — Wheat / Golden / Charcoal
C_CHARCOAL = "#161210"
C_DARK     = "#231A15"
C_BROWN    = "#2E2218"
C_AMBER_D  = "#4A3320"
C_AMBER    = "#6B4423"
C_COPPER   = "#B87333"
C_GOLD     = "#C4A04A"
C_GOLD_L   = "#D4B896"
C_HONEY    = "#E8A838"
C_CREAM    = "#FAF6F0"
C_WHITE    = "#ffffff"


CSS = f"""<style>
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

.back-cover::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 24px 14px at 15% 25%, {C_HONEY}, transparent),
    radial-gradient(ellipse 22px 13px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 26px 15px at 70% 70%, {C_HONEY}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 18px 11px at 50% 50%, {C_HONEY}, transparent);
}}

.back-cover::after {{
  content: '';
  position: absolute;
  top: -0.3in; right: -0.3in;
  width: 1.2in; height: 1.2in;
  border-radius: 50%;
  background: rgba(232, 168, 56, 0.08);
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
  background: {C_HONEY};
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

.spine::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.03;
  background-image:
    radial-gradient(ellipse 10px 6px at 50% 20%, {C_HONEY}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 50%, {C_GOLD}, transparent),
    radial-gradient(ellipse 10px 6px at 50% 80%, {C_HONEY}, transparent);
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 25%, {C_AMBER_D} 55%, {C_DARK} 85%, {C_CHARCOAL} 100%);
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
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 40px 24px at 15% 25%, {C_HONEY}, transparent),
    radial-gradient(ellipse 34px 20px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 38px 22px at 70% 70%, {C_HONEY}, transparent),
    radial-gradient(ellipse 28px 18px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 24px 15px at 50% 50%, {C_HONEY}, transparent),
    radial-gradient(ellipse 30px 18px at 10% 60%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 14px at 90% 45%, {C_HONEY}, transparent);
}}

.loaf-wrap {{
  width: 120px; height: 150px;
  position: relative;
  margin: 0 auto 24px;
  z-index: 5;
}}

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

@media screen {{
  .cover-wrap {{ border: 1px solid #ccc; }}
}}
</style>"""


def generate(output_path=OUTPUT_FILE):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sourdough Baking Log — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every loaf tells a story.</strong>
        This journal is your companion for mastering sourdough bread.
        From starter management to the final bake, capture every detail
        &mdash; hydration, fermentation time, temperature, scoring
        pattern, and crumb results.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>40 two-page bake logs with full formula tracking</li>
        <li>Baker's percentage guide and hydration reference</li>
        <li>Sourdough process timeline (two-day schedule)</li>
        <li>Flour types and protein content guide</li>
        <li>16-term sourdough baking glossary</li>
        <li>Starter feeding log (2 pages)</li>
        <li>Crumb, crust, and flavor description checklists</li>
        <li>Year-in-review and space for notes</li>
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
    <div class="spine-text">Sourdough Baking Log</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Sourdough Loaf SVG -->
    <div class="loaf-wrap">
      <svg viewBox="0 0 120 150" width="120" height="150" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <radialGradient id="crustGrad" cx="0.5" cy="0.4" r="0.6">
            <stop offset="0%" stop-color="{C_GOLD}" stop-opacity="0.7"/>
            <stop offset="60%" stop-color="{C_COPPER}" stop-opacity="0.8"/>
            <stop offset="100%" stop-color="{C_AMBER}" stop-opacity="0.9"/>
          </radialGradient>
        </defs>

        <!-- Shadow base -->
        <ellipse cx="60" cy="140" rx="40" ry="4" fill="rgba(0,0,0,0.35)"/>

        <!-- Boule body (round loaf) -->
        <ellipse cx="60" cy="95" rx="46" ry="38" fill="url(#crustGrad)" stroke="rgba(250,246,240,0.4)" stroke-width="1.5"/>

        <!-- Top crust dome -->
        <path d="M 18 92 Q 20 55 60 50 Q 100 55 102 92"
              stroke="rgba(250,246,240,0.3)" stroke-width="1.5" fill="none"/>

        <!-- Scoring / grigne lines (the signature sourdough cuts) -->
        <path d="M 40 62 Q 48 56 56 62" stroke="rgba(20,15,10,0.5)" stroke-width="2" fill="none" stroke-linecap="round"/>
        <path d="M 56 58 Q 64 52 72 58" stroke="rgba(20,15,10,0.5)" stroke-width="2" fill="none" stroke-linecap="round"/>
        <path d="M 72 62 Q 80 56 88 62" stroke="rgba(20,15,10,0.5)" stroke-width="2" fill="none" stroke-linecap="round"/>

        <!-- Ear (raised crust flap from scoring) -->
        <path d="M 38 60 Q 42 54 46 58 L 48 62" stroke="rgba(250,246,240,0.35)" stroke-width="1.2" fill="rgba(250,246,240,0.06)"/>

        <!-- Secondary score lines (lower) -->
        <path d="M 35 76 Q 45 71 55 76" stroke="rgba(20,15,10,0.3)" stroke-width="1.5" fill="none" stroke-linecap="round"/>
        <path d="M 65 76 Q 75 71 85 76" stroke="rgba(20,15,10,0.3)" stroke-width="1.5" fill="none" stroke-linecap="round"/>

        <!-- Flour dusting -->
        <circle cx="42" cy="72" r="1.5" fill="{C_CREAM}" opacity="0.5"/>
        <circle cx="68" cy="68" r="1.2" fill="{C_CREAM}" opacity="0.4"/>
        <circle cx="78" cy="74" r="1.5" fill="{C_CREAM}" opacity="0.5"/>
        <circle cx="50" cy="80" r="1" fill="{C_CREAM}" opacity="0.4"/>
        <circle cx="86" cy="82" r="1" fill="{C_CREAM}" opacity="0.3"/>
        <circle cx="32" cy="84" r="1" fill="{C_CREAM}" opacity="0.3"/>
        <circle cx="58" cy="84" r="1.2" fill="{C_CREAM}" opacity="0.4"/>

        <!-- Steam wisps (from fresh bake) -->
        <path d="M 48 40 Q 50 32 48 26 Q 46 20 48 14" stroke="rgba(250,246,240,0.15)" stroke-width="1.5" fill="none" stroke-linecap="round"/>
        <path d="M 60 38 Q 62 30 60 24 Q 58 18 60 12" stroke="rgba(250,246,240,0.12)" stroke-width="1.5" fill="none" stroke-linecap="round"/>
        <path d="M 72 40 Q 74 32 72 26 Q 70 20 72 14" stroke="rgba(250,246,240,0.1)" stroke-width="1.5" fill="none" stroke-linecap="round"/>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Sourdough<br>Baking Log</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Track Every Loaf,<br>Every Hydration, Every Crumb</div>
      <div class="features">
        <span class="feature-badge">40 Bake Logs</span>
        <span class="feature-badge">Baker's %</span>
        <span class="feature-badge">Hydration Guide</span>
        <span class="feature-badge">Starter Tracker</span>
      </div>
      <div class="tagline">For Artisan Bakers &amp; Home Enthusiasts</div>
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
