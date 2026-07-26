#!/usr/bin/env python3
"""
Scuba Diving Log Book — KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Trim: 6" x 9"
Pages: 124 (cream paper)
Spine: 124 x 0.0025 = 0.310"
Bleed: 0.125" all outer edges
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "scuba_diving_log_book_us_cover_V1.0.html")

TRIM_W = 6.0
TRIM_H = 9.0
PAGES = 124
SPINE = PAGES * 0.0025
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2
COVER_H = TRIM_H + BLEED * 2

C_CHARCOAL = "#161616"
C_DARK     = "#1E1E1E"
C_GOLD     = "#C4A04A"
C_GOLD_L   = "#D4B896"
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 40%, {C_CHARCOAL} 100%);
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
    radial-gradient(ellipse 24px 14px at 15% 25%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 13px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 26px 15px at 70% 70%, {C_GOLD}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 18px 11px at 50% 50%, {C_GOLD}, transparent);
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
  background: linear-gradient(165deg, {C_CHARCOAL} 0%, {C_DARK} 25%, #1E1E1E 55%, {C_DARK} 85%, {C_CHARCOAL} 100%);
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
    radial-gradient(ellipse 40px 24px at 15% 25%, {C_GOLD}, transparent),
    radial-gradient(ellipse 34px 20px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 38px 22px at 70% 70%, {C_GOLD}, transparent),
    radial-gradient(ellipse 28px 18px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 24px 15px at 50% 50%, {C_GOLD}, transparent),
    radial-gradient(ellipse 30px 18px at 10% 60%, {C_GOLD}, transparent),
    radial-gradient(ellipse 22px 14px at 90% 45%, {C_GOLD}, transparent);
}}

.icon-wrap {{
  width: 120px; height: 120px;
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
  font-size: 26pt;
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
  font-size: 11pt;
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
  <title>Scuba Diving Log Book &mdash; Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- ============ BACK COVER ============ -->
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every dive, every depth, every adventure.</strong>
        This scuba diving log book gives you the space to record every
        detail that matters &mdash; depth, time, gas, conditions, marine
        life, and the gear you used. With 50 detailed two-page dive logs,
        a quick log, dive site tracker, safety reference, gas management
        guide, and gear inventory, it is everything a diver needs to build
        a lifetime of underwater memories.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">
        What's Inside
      </div>
      <ul class="back-features">
        <li>50 two-page dive logs with full profile tracking</li>
        <li>Quick dive log for a bird's-eye view</li>
        <li>Dive safety essentials and hand signal reference</li>
        <li>Gas management guide with SAC rate calculator</li>
        <li>Favorite dive sites tracker with GPS</li>
        <li>Personal records and certification milestones</li>
        <li>Gear inventory and service log</li>
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
    <div class="spine-text">Scuba Diving Log Book</div>
  </div>

  <!-- ============ FRONT COVER ============ -->
  <div class="front-cover">

    <!-- Scuba Diver SVG Icon -->
    <div class="icon-wrap">
      <svg viewBox="0 0 120 120" width="120" height="120" xmlns="http://www.w3.org/2000/svg">
        <circle cx="60" cy="60" r="56" stroke="{C_GOLD}" stroke-width="1" fill="none" opacity="0.12" stroke-dasharray="4,4"/>
        <!-- Diver mask -->
        <ellipse cx="60" cy="38" rx="22" ry="14" stroke="{C_GOLD}" stroke-width="2" fill="rgba(196,160,74,0.1)"/>
        <rect x="42" y="28" width="36" height="6" rx="2" stroke="{C_GOLD}" stroke-width="1.5" fill="none"/>
        <!-- Snorkel -->
        <path d="M 80 28 L 88 28 L 88 12" stroke="{C_GOLD}" stroke-width="2" fill="none" stroke-linecap="round"/>
        <!-- Tank -->
        <rect x="48" y="55" width="24" height="40" rx="3" stroke="{C_GOLD}" stroke-width="2" fill="rgba(196,160,74,0.08)"/>
        <rect x="54" y="50" width="12" height="6" rx="2" stroke="{C_GOLD}" stroke-width="1.5" fill="none"/>
        <!-- Reg hose -->
        <path d="M 72 68 Q 80 65 82 60" stroke="{C_GOLD}" stroke-width="1.5" fill="none"/>
        <!-- Bubbles -->
        <circle cx="30" cy="30" r="4" fill="none" stroke="{C_GOLD}" stroke-width="0.8" opacity="0.4"/>
        <circle cx="24" cy="20" r="3" fill="none" stroke="{C_GOLD}" stroke-width="0.6" opacity="0.3"/>
        <circle cx="35" cy="12" r="2.5" fill="none" stroke="{C_GOLD}" stroke-width="0.5" opacity="0.2"/>
        <circle cx="92" cy="40" r="3.5" fill="none" stroke="{C_GOLD}" stroke-width="0.7" opacity="0.35"/>
        <circle cx="98" cy="30" r="2.5" fill="none" stroke="{C_GOLD}" stroke-width="0.5" opacity="0.25"/>
        <!-- Water ripples -->
        <path d="M 20 100 Q 35 97 50 100 Q 65 103 80 100 Q 95 97 105 100"
          stroke="{C_GOLD}" stroke-width="0.8" fill="none" opacity="0.3"/>
        <path d="M 25 106 Q 40 103 55 106 Q 70 109 85 106 Q 100 103 105 106"
          stroke="{C_GOLD}" stroke-width="0.6" fill="none" opacity="0.2"/>
      </svg>
    </div>

    <!-- Title -->
    <div class="title-block">
      <div class="main-title">Scuba Diving<br>Log Book</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Every Dive, Every Depth,<br>Every Adventure</div>
      <div class="features">
        <span class="feature-badge">50 Dive Logs</span>
        <span class="feature-badge">Gear Tracker</span>
        <span class="feature-badge">Dive Sites</span>
        <span class="feature-badge">Safety Guide</span>
      </div>
      <div class="tagline">Descend &middot; Explore &middot; Remember</div>
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
