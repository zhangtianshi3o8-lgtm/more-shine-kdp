#!/usr/bin/env python3
"""
Running Training Log -- KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).
Trim: 6" x 9"
Pages: 68 (cream paper)
Spine: 68 x 0.0025 = 0.1700"
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "running_training_log_us_cover_V1.0.html")

TRIM_W = 6.0
TRIM_H = 9.0
PAGES = 68
SPINE = PAGES * 0.0025
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2
COVER_H = TRIM_H + BLEED * 2

# Colors -- Dark charcoal + electric orange + gold
C_DARK     = "#161616"
C_DARK_M   = "#2A2520"
C_ORANGE   = "#E85D2A"
C_ORANGE_D = "#C04A1F"
C_GOLD     = "#C4A04A"
C_GOLD_L   = "#D4B896"
C_CREAM    = "#FAF6F0"
C_WHITE    = "#ffffff"


CSS = f"""<style>
@page {{ size: {COVER_W:.4f}in {COVER_H:.4f}in; margin: 0; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: Georgia, "Iowan Old Style", "Palatino", serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}

.cover-wrap {{ width: {COVER_W:.4f}in; height: {COVER_H:.4f}in; position: relative; display: flex; }}

/* BACK */
.back-cover {{
  width: {TRIM_W + BLEED:.4f}in; height: {COVER_H:.4f}in;
  background: linear-gradient(165deg, {C_DARK} 0%, {C_DARK_M} 40%, {C_DARK} 100%);
  padding: 0.75in 0.5in 0.45in 0.5in; display: flex; flex-direction: column;
  justify-content: space-around; position: relative; overflow: hidden;
}}
.back-cover::before {{
  content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.04;
  background-image:
    radial-gradient(ellipse 24px 14px at 15% 25%, {C_ORANGE}, transparent),
    radial-gradient(ellipse 22px 13px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 26px 15px at 70% 70%, {C_ORANGE}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_GOLD}, transparent);
}}
.back-cover::after {{
  content: ''; position: absolute; top: -0.3in; right: -0.3in; width: 1.2in; height: 1.2in;
  border-radius: 50%; background: rgba(232, 93, 42, 0.06);
}}
.back-text {{ color: rgba(255,255,255,0.92); font-size: 9pt; line-height: 1.6; position: relative; z-index: 2; }}
.back-text .blurb {{ font-style: italic; margin-bottom: 14px; font-size: 9.5pt; line-height: 1.55; }}
.back-text .blurb strong {{ color: {C_GOLD_L}; font-style: normal; }}
.back-features {{ list-style: none; padding: 0; }}
.back-features li {{ font-size: 8pt; color: rgba(255,255,255,0.82); padding: 3px 0; padding-left: 16px; position: relative; line-height: 1.4; }}
.back-features li::before {{ content: ''; position: absolute; left: 0; top: 5px; width: 5px; height: 5px; background: {C_ORANGE}; border-radius: 50%; }}
.back-bottom {{ padding-bottom: 0.15in; position: relative; z-index: 2; }}
.back-logo {{ text-align: center; color: {C_GOLD}; font-size: 8pt; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; padding-top: 8px; margin-top: 6px; border-top: 1px solid rgba(255,255,255,0.15); }}

/* SPINE */
.spine {{ width: {SPINE:.4f}in; height: {COVER_H:.4f}in; background: linear-gradient(180deg, {C_DARK} 0%, {C_DARK_M} 50%, {C_DARK} 100%); display: flex; flex-direction: column; align-items: center; justify-content: space-between; padding: 0.6in 0; position: relative; }}
.spine::before {{ content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.03; background-image: radial-gradient(ellipse 10px 6px at 50% 20%, {C_ORANGE}, transparent), radial-gradient(ellipse 10px 6px at 50% 50%, {C_GOLD}, transparent), radial-gradient(ellipse 10px 6px at 50% 80%, {C_ORANGE}, transparent); }}
.spine-text {{ writing-mode: vertical-rl; transform: rotate(180deg); color: rgba(255,255,255,0.95); font-size: 8pt; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; white-space: nowrap; line-height: 1; position: relative; z-index: 2; }}
.spine-author {{ writing-mode: vertical-rl; transform: rotate(180deg); color: {C_GOLD}; font-size: 6pt; letter-spacing: 1.5px; text-transform: uppercase; font-family: 'Helvetica Neue', Arial, sans-serif; position: relative; z-index: 2; }}

/* FRONT */
.front-cover {{
  width: {TRIM_W + BLEED:.4f}in; height: {COVER_H:.4f}in;
  background: linear-gradient(165deg, {C_DARK} 0%, {C_DARK_M} 25%, {C_DARK_M} 55%, {C_DARK} 85%, {C_DARK} 100%);
  position: relative; overflow: hidden; display: flex; flex-direction: column;
  justify-content: center; align-items: center; text-align: center;
  padding: {BLEED}in {BLEED}in {BLEED}in {BLEED}in;
}}
.front-cover::before {{
  content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.05;
  background-image:
    radial-gradient(ellipse 40px 24px at 15% 25%, {C_ORANGE}, transparent),
    radial-gradient(ellipse 34px 20px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 38px 22px at 70% 70%, {C_ORANGE}, transparent),
    radial-gradient(ellipse 28px 18px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 24px 15px at 50% 50%, {C_ORANGE}, transparent);
}}

.icon-wrap {{ width: 110px; height: 110px; position: relative; margin: 0 auto 24px; z-index: 5; }}
.title-block {{ position: relative; z-index: 5; padding: 0 0.4in; }}
.main-title {{ font-family: Georgia, serif; font-size: 28pt; font-weight: 700; color: {C_WHITE}; line-height: 1.12; letter-spacing: 0.5pt; text-shadow: 2px 2px 8px rgba(0,0,0,0.55); }}
.accent-bar {{ width: 120px; height: 2.5px; background: {C_ORANGE}; margin: 16px auto; }}
.subtitle {{ font-size: 11pt; color: {C_GOLD_L}; font-style: italic; line-height: 1.5; margin-bottom: 22px; }}
.features {{ display: flex; justify-content: center; gap: 8px; margin-bottom: 22px; flex-wrap: wrap; }}
.feature-badge {{ background: rgba(255,255,255,0.08); border: 1px solid rgba(232,93,42,0.4); color: {C_GOLD}; font-size: 7.5pt; font-weight: 700; letter-spacing: 0.5pt; padding: 4px 10px; border-radius: 3px; text-transform: uppercase; }}
.tagline {{ font-size: 9pt; color: {C_GOLD_L}; letter-spacing: 2pt; text-transform: uppercase; margin-top: 8px; }}
.publisher {{ position: absolute; bottom: 0.5in; left: 0; right: 0; text-align: center; font-size: 9.5pt; color: {C_GOLD}; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; z-index: 5; }}
@media screen {{ .cover-wrap {{ border: 1px solid #ccc; }} }}
</style>"""


def generate(output_path=OUTPUT_FILE):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Running Training Log -- Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Train smarter. Run stronger.</strong>
        Whether you are building base mileage, preparing for a marathon,
        or just starting out, this log helps you track every run with
        purpose -- distance, pace, effort, heart rate, and how you felt.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">What's Inside</div>
      <ul class="back-features">
        <li>25 two-page run log spreads</li>
        <li>Season goals and race target page</li>
        <li>Weekly summaries every 5 runs</li>
        <li>Shoe mileage tracker (retire before injury)</li>
        <li>Race results and personal records</li>
        <li>Monthly summary with habit tracking</li>
        <li>Large 6" x 9" format for detailed logging</li>
      </ul>
    </div>
    <div class="back-bottom">
      <div class="back-logo">More Shine Press</div>
    </div>
  </div>

  <div class="spine">
    <div class="spine-author">More Shine Press</div>
    <div class="spine-text">Running Training Log</div>
  </div>

  <div class="front-cover">
    <div class="icon-wrap">
      <svg viewBox="0 0 110 110" width="110" height="110" xmlns="http://www.w3.org/2000/svg">
        <!-- Running shoe silhouette (minimal line art) -->
        <g transform="translate(55,56)">
          <!-- Sole -->
          <path d="M -38,18 Q -40,24 -32,24 L 30,24 Q 38,24 38,17 L 38,12 L -36,12 Z"
                fill="none" stroke="{C_ORANGE}" stroke-width="2.5" stroke-linejoin="round"/>
          <!-- Upper shoe body -->
          <path d="M -34,12 L -34,0 Q -32,-8 -22,-10 L -6,-14 Q 4,-16 14,-11 Q 24,-5 34,3 L 38,8 L 38,12"
                fill="none" stroke="{C_ORANGE}" stroke-width="2.5" stroke-linejoin="round"/>
          <!-- Laces -->
          <line x1="-16" y1="-6" x2="-4" y2="-3" stroke="{C_ORANGE}" stroke-width="1.2" opacity="0.6"/>
          <line x1="-14" y1="-1" x2="-2" y2="2" stroke="{C_ORANGE}" stroke-width="1.2" opacity="0.6"/>
          <line x1="-12" y1="4" x2="0" y2="6" stroke="{C_ORANGE}" stroke-width="1.2" opacity="0.6"/>
          <!-- Heel curve -->
          <path d="M -34,0 Q -38,8 -34,12" fill="none" stroke="{C_ORANGE}" stroke-width="2.5"/>
          <!-- Accent dot -->
          <circle cx="22" cy="-2" r="2.5" fill="{C_GOLD}"/>
        </g>
      </svg>
    </div>
    <div class="title-block">
      <div class="main-title">Running<br>Training<br>Log</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Track Every Run,<br>Every Mile, Every Goal</div>
      <div class="features">
        <span class="feature-badge">25 Run Logs</span>
        <span class="feature-badge">Weekly Review</span>
        <span class="feature-badge">Shoe Tracker</span>
        <span class="feature-badge">Race Results</span>
      </div>
      <div class="tagline">For Runners of All Levels</div>
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
    print(f"     Spine: {SPINE:.4f} in ({PAGES} pages)")
