#!/usr/bin/env python3
"""
Pregnancy Journal -- KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).
Trim: 8" x 10"
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "pregnancy_journal_us_cover_V1.0.html")

TRIM_W = 8.0
TRIM_H = 10.0
PAGES = 66
SPINE = PAGES * 0.0025
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2
COVER_H = TRIM_H + BLEED * 2

C_DARK     = "#161616"
C_DARK_M   = "#1A1A18"
C_AMBER    = "#B8860B"
C_ROSE     = "#8B4040"
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
    radial-gradient(ellipse 24px 14px at 15% 25%, {C_AMBER}, transparent),
    radial-gradient(ellipse 22px 13px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 26px 15px at 70% 70%, {C_AMBER}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_GOLD}, transparent);
}}
.back-cover::after {{
  content: ''; position: absolute; top: -0.3in; right: -0.3in; width: 1.2in; height: 1.2in;
  border-radius: 50%; background: rgba(184, 134, 11, 0.08);
}}
.back-text {{ color: rgba(255,255,255,0.92); font-size: 9pt; line-height: 1.6; position: relative; z-index: 2; }}
.back-text .blurb {{ font-style: italic; margin-bottom: 14px; font-size: 9.5pt; line-height: 1.55; }}
.back-text .blurb strong {{ color: {C_GOLD_L}; font-style: normal; }}
.back-features {{ list-style: none; padding: 0; }}
.back-features li {{ font-size: 8pt; color: rgba(255,255,255,0.82); padding: 3px 0; padding-left: 16px; position: relative; line-height: 1.4; }}
.back-features li::before {{ content: ''; position: absolute; left: 0; top: 5px; width: 5px; height: 5px; background: {C_AMBER}; border-radius: 50%; }}
.back-bottom {{ padding-bottom: 0.15in; position: relative; z-index: 2; }}
.back-logo {{ text-align: center; color: {C_GOLD}; font-size: 8pt; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; padding-top: 8px; margin-top: 6px; border-top: 1px solid rgba(255,255,255,0.15); }}

/* SPINE */
.spine {{ width: {SPINE:.4f}in; height: {COVER_H:.4f}in; background: linear-gradient(180deg, {C_DARK} 0%, {C_DARK_M} 50%, {C_DARK} 100%); display: flex; flex-direction: column; align-items: center; justify-content: space-between; padding: 0.6in 0; position: relative; }}
.spine::before {{ content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.03; background-image: radial-gradient(ellipse 10px 6px at 50% 20%, {C_AMBER}, transparent), radial-gradient(ellipse 10px 6px at 50% 50%, {C_GOLD}, transparent), radial-gradient(ellipse 10px 6px at 50% 80%, {C_AMBER}, transparent); }}
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
    radial-gradient(ellipse 40px 24px at 15% 25%, {C_AMBER}, transparent),
    radial-gradient(ellipse 34px 20px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 38px 22px at 70% 70%, {C_AMBER}, transparent),
    radial-gradient(ellipse 28px 18px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 24px 15px at 50% 50%, {C_AMBER}, transparent);
}}

.icon-wrap {{ width: 120px; height: 120px; position: relative; margin: 0 auto 24px; z-index: 5; }}
.title-block {{ position: relative; z-index: 5; padding: 0 0.4in; }}
.main-title {{ font-family: Georgia, serif; font-size: 32pt; font-weight: 700; color: {C_WHITE}; line-height: 1.12; letter-spacing: 0.5pt; text-shadow: 2px 2px 8px rgba(0,0,0,0.55); }}
.accent-bar {{ width: 120px; height: 2.5px; background: {C_AMBER}; margin: 16px auto; }}
.subtitle {{ font-size: 12pt; color: {C_GOLD_L}; font-style: italic; line-height: 1.5; margin-bottom: 22px; }}
.features {{ display: flex; justify-content: center; gap: 8px; margin-bottom: 22px; flex-wrap: wrap; }}
.feature-badge {{ background: rgba(255,255,255,0.08); border: 1px solid rgba(184,134,11,0.4); color: {C_GOLD}; font-size: 7.5pt; font-weight: 700; letter-spacing: 0.5pt; padding: 4px 10px; border-radius: 3px; text-transform: uppercase; }}
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
  <title>Pregnancy Journal -- Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Every kick, every craving, every milestone -- capture it all.</strong>
        This beautifully designed journal guides you through all 40 weeks
        of pregnancy with thoughtful prompts, symptom trackers, bump photo
        spaces, and reflection pages. From the first positive test to the
        first cry in the delivery room, keep every memory safe in one
        elegant keepsake you will treasure forever.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">What's Inside</div>
      <ul class="back-features">
        <li>37 weekly tracking pages (weeks 4-40)</li>
        <li>Symptom checklist, mood tracker, bump photo space</li>
        <li>Three trimester dividers with reflection pages</li>
        <li>Prenatal appointment log (4 pages)</li>
        <li>Ultrasound gallery with memory prompts</li>
        <li>Baby names brainstorm and nursery planning</li>
        <li>Hospital bag checklist and birth plan</li>
        <li>Birth day record and baby shower planner</li>
        <li>Large 8&quot; x 10&quot; format, 66 pages</li>
      </ul>
    </div>
    <div class="back-bottom">
      <div class="back-logo">More Shine Press</div>
    </div>
  </div>

  <div class="spine">
    <div class="spine-author">More Shine Press</div>
    <div class="spine-text">Pregnancy Journal</div>
  </div>

  <div class="front-cover">
    <div class="icon-wrap">
      <svg viewBox="0 0 120 120" width="120" height="120" xmlns="http://www.w3.org/2000/svg">
        <!-- Mother heart -->
        <g transform="translate(60,62)">
          <!-- Large heart outline -->
          <path d="M 0,28 C -26,8 -36,-4 -36,-16 C -36,-28 -26,-34 -16,-30 C -8,-27 -3,-20 0,-14 C 3,-20 8,-27 16,-30 C 26,-34 36,-28 36,-16 C 36,-4 26,8 0,28 Z"
                stroke="{C_AMBER}" stroke-width="2.5" fill="none"/>
          <!-- Inner highlight -->
          <path d="M -22,-22 C -25,-17 -20,-12 -14,-12" stroke="{C_GOLD_L}" stroke-width="1.2" fill="none"/>
          <path d="M 22,-22 C 25,-17 20,-12 14,-12" stroke="{C_GOLD_L}" stroke-width="1.2" fill="none"/>
          <!-- Small inner heart (baby) -->
          <path d="M 0,8 C -8,0 -12,-4 -12,-8 C -12,-12 -8,-14 -4,-12 C -1,-10 0,-8 0,-6 C 0,-8 1,-10 4,-12 C 8,-14 12,-12 12,-8 C 12,-4 8,0 0,8 Z"
                stroke="{C_GOLD}" stroke-width="1.5" fill="none"/>
          <!-- Sparkle dots -->
          <circle cx="0" cy="-3" r="1.5" fill="{C_GOLD_L}"/>
          <circle cx="-4" cy="-10" r="1" fill="{C_GOLD_L}" opacity="0.6"/>
          <circle cx="4" cy="-10" r="1" fill="{C_GOLD_L}" opacity="0.6"/>
        </g>
      </svg>
    </div>
    <div class="title-block">
      <div class="main-title">Pregnancy<br>Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">A 40-Week Guided Journal<br>for Moms to Be</div>
      <div class="features">
        <span class="feature-badge">40 Weeks</span>
        <span class="feature-badge">Symptom Tracker</span>
        <span class="feature-badge">Birth Plan</span>
        <span class="feature-badge">Keepsake</span>
      </div>
      <div class="tagline">For Moms to Be</div>
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
