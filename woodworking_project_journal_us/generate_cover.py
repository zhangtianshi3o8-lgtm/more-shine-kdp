#!/usr/bin/env python3
"""
Woodworking Project Journal — KDP Full Wrap Cover Generator
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
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "woodworking_project_journal_cover_V1.0.html")

TRIM_W = 6.0
TRIM_H = 9.0
PAGES = 104
SPINE = PAGES * 0.0025   # 0.260"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 12.51"
COVER_H = TRIM_H + BLEED * 2               # 9.25"

# Colors
C_CHARCOAL = "#161616"
C_DARK     = "#1E1E1E"
C_OAK_D    = "#1A1610"
C_OAK      = "#8B6B3D"
C_OAK_L    = "#A07D4A"
C_OAK_X    = "#B8956A"
C_STEEL    = "#5A7A8A"
C_STEEL_L  = "#7A9AAA"
C_STEEL_X  = "#9ABACA"
C_GOLD     = "#C4A04A"
C_GOLD_L   = "#D4B896"
C_BROWN    = "#6B4E2E"
C_CREAM    = "#FAF8F4"
C_WHITE    = "#ffffff"


CSS = """
<style>
@page { size: %.4fin %.4fin; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: Georgia, "Iowan Old Style", "Palatino", serif;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

.cover-wrap {
  width: %.4fin;
  height: %.4fin;
  position: relative;
  display: flex;
}

/* ============ BACK COVER ============ */
.back-cover {
  width: %.4fin;
  height: %.4fin;
  background: linear-gradient(165deg, %s 0%%, %s 35%%, %s 100%%);
  padding: 0.75in 0.5in 0.45in 0.5in;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  overflow: hidden;
}

.back-cover::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 26px 16px at 15%% 25%%, %s, transparent),
    radial-gradient(ellipse 22px 14px at 80%% 15%%, %s, transparent),
    radial-gradient(ellipse 24px 15px at 70%% 70%%, %s, transparent),
    radial-gradient(ellipse 20px 12px at 25%% 80%%, %s, transparent),
    radial-gradient(ellipse 18px 11px at 50%% 50%%, %s, transparent),
    radial-gradient(ellipse 22px 13px at 10%% 60%%, %s, transparent);
}

.back-cover::after {
  content: '';
  position: absolute;
  top: -0.3in; right: -0.3in;
  width: 1.2in; height: 1.2in;
  border-radius: 50%%;
  background: rgba(139, 107, 61, 0.08);
}

.back-text {
  color: rgba(255,255,255,0.92);
  font-size: 9pt;
  line-height: 1.6;
  position: relative;
  z-index: 2;
}
.back-text .blurb {
  font-style: italic;
  margin-bottom: 14px;
  font-size: 9.5pt;
  line-height: 1.55;
}
.back-text .blurb strong {
  color: %s;
  font-style: normal;
}

.back-features {
  list-style: none;
  padding: 0;
}
.back-features li {
  font-size: 8pt;
  color: rgba(255,255,255,0.82);
  padding: 3px 0;
  padding-left: 16px;
  position: relative;
  line-height: 1.4;
}
.back-features li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 5px;
  width: 5px;
  height: 5px;
  background: %s;
  border-radius: 50%%;
  box-shadow: 0 0 3px rgba(139,107,61,0.4);
}

.back-bottom {
  padding-bottom: 0.15in;
  position: relative;
  z-index: 2;
}

.barcode-area {
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
}

.back-logo {
  text-align: center;
  color: %s;
  font-size: 8pt;
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  font-weight: 700;
  padding-top: 8px;
  margin-top: 6px;
  border-top: 1px solid rgba(255,255,255,0.15);
}

/* ============ SPINE ============ */
.spine {
  width: %.4fin;
  height: %.4fin;
  background: linear-gradient(180deg, %s 0%%, %s 50%%, %s 100%%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 0.6in 0;
  position: relative;
}

.spine::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 10px 6px at 50%% 20%%, %s, transparent),
    radial-gradient(ellipse 10px 6px at 50%% 50%%, %s, transparent),
    radial-gradient(ellipse 10px 6px at 50%% 80%%, %s, transparent);
}

.spine-text {
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
}

.spine-author {
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  color: %s;
  font-size: 6pt;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  position: relative;
  z-index: 2;
}

/* ============ FRONT COVER ============ */
.front-cover {
  width: %.4fin;
  height: %.4fin;
  background: linear-gradient(165deg, %s 0%%, %s 20%%, %s 55%%, %s 85%%, %s 100%%);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: %.3fin %.3fin %.3fin %.3fin;
}

.front-cover::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 38px 23px at 15%% 25%%, %s, transparent),
    radial-gradient(ellipse 32px 19px at 80%% 15%%, %s, transparent),
    radial-gradient(ellipse 36px 22px at 70%% 70%%, %s, transparent),
    radial-gradient(ellipse 26px 16px at 25%% 80%%, %s, transparent),
    radial-gradient(ellipse 22px 14px at 50%% 50%%, %s, transparent),
    radial-gradient(ellipse 28px 17px at 10%% 60%%, %s, transparent),
    radial-gradient(ellipse 20px 12px at 90%% 45%%, %s, transparent),
    radial-gradient(ellipse 18px 11px at 40%% 90%%, %s, transparent),
    radial-gradient(ellipse 16px 10px at 60%% 35%%, %s, transparent);
}

/* ============ TOOL ILLUSTRATION ============ */
.tool-wrap {
  width: 110px; height: 180px;
  position: relative;
  margin: 0 auto 20px;
  z-index: 5;
}

/* ============ TITLE ============ */
.title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.5in;
}

.main-title {
  font-family: Georgia, serif;
  font-size: 24pt;
  font-weight: 700;
  color: %s;
  line-height: 1.12;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.55);
}

.accent-bar {
  width: 120px; height: 2.5px;
  background: %s;
  margin: 16px auto;
}

.subtitle {
  font-size: 11.5pt;
  color: %s;
  font-style: italic;
  line-height: 1.5;
  margin-bottom: 22px;
}

.features {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-bottom: 22px;
  flex-wrap: wrap;
}

.feature-badge {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(139,107,61,0.45);
  color: %s;
  font-size: 7.5pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 10px;
  border-radius: 3px;
  text-transform: uppercase;
}

.tagline {
  font-size: 9pt;
  color: %s;
  letter-spacing: 2pt;
  text-transform: uppercase;
  margin-top: 8px;
}

.publisher {
  position: absolute;
  bottom: 0.5in;
  left: 0; right: 0;
  text-align: center;
  font-size: 9.5pt;
  color: %s;
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  font-weight: 700;
  z-index: 5;
}

@media screen { .cover-wrap { border: 1px solid #ccc; } }
</style>
""" % (
    COVER_W, COVER_H,
    COVER_W, COVER_H,
    TRIM_W + BLEED, COVER_H,
    C_CHARCOAL, C_DARK, C_OAK_D,
    C_OAK, C_STEEL_L, C_GOLD, C_OAK, C_STEEL_L, C_BROWN,
    C_OAK_X,
    C_OAK,
    C_OAK,
    SPINE, COVER_H,
    C_CHARCOAL, C_DARK, C_CHARCOAL,
    C_OAK, C_STEEL_L, C_BROWN,
    C_OAK,
    TRIM_W + BLEED, COVER_H,
    C_CHARCOAL, C_DARK, C_OAK_D, C_DARK, C_CHARCOAL,
    BLEED, BLEED, BLEED, BLEED,
    C_OAK, C_STEEL_L, C_GOLD, C_OAK, C_STEEL_L, C_BROWN, C_OAK, C_STEEL_L, C_OAK,
    C_WHITE,
    C_OAK,
    C_STEEL_L,
    C_OAK,
    C_STEEL_L,
    C_GOLD,
)


def generate(output_path=OUTPUT_FILE):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Woodworking Project Journal — Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every cut teaches a lesson. Every project builds a maker.</strong>
        This journal captures the knowledge you earn at the workbench
        &mdash; from dimensioned sketches and cut lists to finish schedules
        and honest cost tracking. Your personal reference library of
        hard-won woodworking expertise.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_OAK_X}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>40 two-page project logs (blueprint + build record)</li>
        <li>Dimensioned sketch area on every project</li>
        <li>Cut list tables with wood, quantity, and dimensions</li>
        <li>14 common wood species with Janka hardness</li>
        <li>12 joinery methods explained</li>
        <li>9 finishing options and sanding grit guide</li>
        <li>Lumber dimension chart (nominal vs actual)</li>
        <li>Board foot calculator and measurement reference</li>
        <li>Shop safety rules and personal protection guide</li>
        <li>Lumber, sheet goods, and hardware inventory</li>
        <li>Tool inventory checklist (power, hand, jigs)</li>
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
    <div class="spine-text">Woodworking Journal</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Tool illustration (SVG: saw blade + wood plank + shavings) -->
    <div class="tool-wrap">
      <svg viewBox="0 0 110 180" width="110" height="180" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="bladeGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_STEEL_L}" stop-opacity="0.20"/>
            <stop offset="100%" stop-color="{C_STEEL}" stop-opacity="0.10"/>
          </linearGradient>
          <linearGradient id="plankGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_OAK_X}" stop-opacity="0.15"/>
            <stop offset="100%" stop-color="{C_OAK}" stop-opacity="0.08"/>
          </linearGradient>
          <linearGradient id="pencilGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{C_GOLD}" stop-opacity="0.25"/>
            <stop offset="100%" stop-color="{C_OAK}" stop-opacity="0.12"/>
          </linearGradient>
        </defs>

        <!-- Wood plank base -->
        <rect x="15" y="95" width="80" height="55" rx="2"
              fill="url(#plankGrad)"
              stroke="rgba(139,107,61,0.30)" stroke-width="1.5"/>

        <!-- Wood grain lines -->
        <path d="M 22 105 Q 55 103 88 105" fill="none"
              stroke="rgba(107,78,46,0.20)" stroke-width="0.8"/>
        <path d="M 22 115 Q 55 113 88 116" fill="none"
              stroke="rgba(107,78,46,0.15)" stroke-width="0.7"/>
        <path d="M 22 125 Q 55 127 88 124" fill="none"
              stroke="rgba(107,78,46,0.18)" stroke-width="0.8"/>
        <path d="M 22 135 Q 55 133 88 136" fill="none"
              stroke="rgba(107,78,46,0.15)" stroke-width="0.7"/>
        <path d="M 22 143 Q 55 145 88 142" fill="none"
              stroke="rgba(107,78,46,0.12)" stroke-width="0.6"/>

        <!-- Saw blade (circular) -->
        <circle cx="55" cy="48" r="26"
                fill="url(#bladeGrad)"
                stroke="rgba(90,122,138,0.35)" stroke-width="1.5"/>

        <!-- Saw teeth ring (dashed circle) -->
        <circle cx="55" cy="48" r="26"
                fill="none"
                stroke="rgba(90,122,138,0.20)" stroke-width="3"
                stroke-dasharray="3 2"/>

        <!-- Inner blade ring -->
        <circle cx="55" cy="48" r="18"
                fill="none"
                stroke="rgba(90,122,138,0.20)" stroke-width="0.8"/>

        <!-- Center arbor hole -->
        <circle cx="55" cy="48" r="4"
                fill="rgba(22,22,22,0.30)"
                stroke="rgba(90,122,138,0.30)" stroke-width="0.8"/>

        <!-- Blade rotation marks -->
        <line x1="55" y1="26" x2="55" y2="32"
              stroke="rgba(90,122,138,0.20)" stroke-width="1"/>
        <line x1="55" y1="64" x2="55" y2="70"
              stroke="rgba(90,122,138,0.15)" stroke-width="0.8"/>
        <line x1="33" y1="48" x2="39" y2="48"
              stroke="rgba(90,122,138,0.15)" stroke-width="0.8"/>
        <line x1="71" y1="48" x2="77" y2="48"
              stroke="rgba(90,122,138,0.15)" stroke-width="0.8"/>

        <!-- Wood shavings/curls (falling from blade) -->
        <ellipse cx="38" cy="80" rx="7" ry="3"
                 fill="rgba(160,125,74,0.18)"
                 stroke="rgba(139,107,61,0.20)" stroke-width="0.6"
                 transform="rotate(-15 38 80)"/>
        <ellipse cx="72" cy="85" rx="6" ry="2.5"
                 fill="rgba(139,107,61,0.15)"
                 stroke="rgba(139,107,61,0.18)" stroke-width="0.5"
                 transform="rotate(25 72 85)"/>
        <ellipse cx="55" cy="88" rx="5" ry="2"
                 fill="rgba(160,125,74,0.12)"
                 stroke="rgba(139,107,61,0.15)" stroke-width="0.5"
                 transform="rotate(-35 55 88)"/>

        <!-- Carpenter's pencil (left) -->
        <rect x="8" y="20" width="3.5" height="42" rx="1"
              fill="url(#pencilGrad)"
              stroke="rgba(196,160,74,0.25)" stroke-width="0.6"
              transform="rotate(-12 10 41)"/>
        <!-- Pencil tip -->
        <polygon points="8,62 11.5,62 9.75,70"
                 fill="rgba(196,160,74,0.20)"
                 stroke="rgba(196,160,74,0.20)" stroke-width="0.4"
                 transform="rotate(-12 10 41)"/>

        <!-- Square (right, small) -->
        <rect x="92" y="30" width="3" height="35" rx="0.5"
              fill="rgba(90,122,138,0.12)"
              stroke="rgba(90,122,138,0.25)" stroke-width="0.6"/>
        <rect x="85" y="62" width="16" height="3" rx="0.5"
              fill="rgba(90,122,138,0.12)"
              stroke="rgba(90,122,138,0.25)" stroke-width="0.6"/>

        <!-- Sparkle accents -->
        <g opacity="0.6">
          <circle cx="25" cy="15" r="2.5" fill="rgba(196,160,74,0.4)"/>
          <circle cx="25" cy="15" r="1" fill="rgba(250,248,244,0.6)"/>
          <circle cx="90" cy="10" r="1.5" fill="rgba(122,154,170,0.4)"/>
          <circle cx="100" cy="85" r="1.5" fill="rgba(196,160,74,0.3)"/>
          <circle cx="5" cy="100" r="1" fill="rgba(250,248,244,0.25)"/>
          <circle cx="14" cy="165" r="1.5" fill="rgba(139,107,61,0.3)"/>
        </g>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Woodworking<br>Project Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Build It Right,<br>Document Every Cut</div>
      <div class="features">
        <span class="feature-badge">40 Project Logs</span>
        <span class="feature-badge">Cut Lists</span>
        <span class="feature-badge">Wood Guide</span>
        <span class="feature-badge">Joinery Ref</span>
      </div>
      <div class="tagline">For Woodworkers &amp; Makers</div>
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
