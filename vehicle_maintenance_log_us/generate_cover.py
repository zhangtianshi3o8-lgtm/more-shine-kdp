#!/usr/bin/env python3
"""
Vehicle Maintenance Log Book -- KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).
Trim: 6" x 9"
Pages: 76 (cream paper)
Spine: 76 x 0.0025 = 0.1900"
Publisher: More Shine Press
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "vehicle_maintenance_log_us_cover_V1.0.html")

TRIM_W = 6.0
TRIM_H = 9.0
PAGES = 76
SPINE = PAGES * 0.0025
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2
COVER_H = TRIM_H + BLEED * 2

# Colors -- Steel blue / charcoal / gold
C_DARK     = "#0E1620"
C_DARK_M   = "#1A2A3A"
C_STEEL    = "#3D6FA8"
C_STEEL_L  = "#5B8AB8"
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
    radial-gradient(ellipse 24px 14px at 15% 25%, {C_STEEL}, transparent),
    radial-gradient(ellipse 22px 13px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 26px 15px at 70% 70%, {C_STEEL}, transparent),
    radial-gradient(ellipse 20px 12px at 25% 80%, {C_GOLD}, transparent);
}}
.back-cover::after {{
  content: ''; position: absolute; top: -0.3in; right: -0.3in; width: 1.2in; height: 1.2in;
  border-radius: 50%; background: rgba(61, 111, 168, 0.08);
}}
.back-text {{ color: rgba(255,255,255,0.92); font-size: 9pt; line-height: 1.6; position: relative; z-index: 2; }}
.back-text .blurb {{ font-style: italic; margin-bottom: 14px; font-size: 9.5pt; line-height: 1.55; }}
.back-text .blurb strong {{ color: {C_GOLD_L}; font-style: normal; }}
.back-features {{ list-style: none; padding: 0; }}
.back-features li {{ font-size: 8pt; color: rgba(255,255,255,0.82); padding: 3px 0; padding-left: 16px; position: relative; line-height: 1.4; }}
.back-features li::before {{ content: ''; position: absolute; left: 0; top: 5px; width: 5px; height: 5px; background: {C_STEEL}; border-radius: 50%; }}
.back-bottom {{ padding-bottom: 0.15in; position: relative; z-index: 2; }}
.back-logo {{ text-align: center; color: {C_GOLD}; font-size: 8pt; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; padding-top: 8px; margin-top: 6px; border-top: 1px solid rgba(255,255,255,0.15); }}

/* SPINE */
.spine {{ width: {SPINE:.4f}in; height: {COVER_H:.4f}in; background: linear-gradient(180deg, {C_DARK} 0%, {C_DARK_M} 50%, {C_DARK} 100%); display: flex; flex-direction: column; align-items: center; justify-content: space-between; padding: 0.6in 0; position: relative; }}
.spine::before {{ content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.03; background-image: radial-gradient(ellipse 10px 6px at 50% 20%, {C_STEEL}, transparent), radial-gradient(ellipse 10px 6px at 50% 50%, {C_GOLD}, transparent), radial-gradient(ellipse 10px 6px at 50% 80%, {C_STEEL}, transparent); }}
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
    radial-gradient(ellipse 40px 24px at 15% 25%, {C_STEEL}, transparent),
    radial-gradient(ellipse 34px 20px at 80% 15%, {C_GOLD}, transparent),
    radial-gradient(ellipse 38px 22px at 70% 70%, {C_STEEL}, transparent),
    radial-gradient(ellipse 28px 18px at 25% 80%, {C_GOLD}, transparent),
    radial-gradient(ellipse 24px 15px at 50% 50%, {C_STEEL}, transparent);
}}

.icon-wrap {{ width: 110px; height: 110px; position: relative; margin: 0 auto 24px; z-index: 5; }}
.title-block {{ position: relative; z-index: 5; padding: 0 0.4in; }}
.main-title {{ font-family: Georgia, serif; font-size: 30pt; font-weight: 700; color: {C_WHITE}; line-height: 1.12; letter-spacing: 0.5pt; text-shadow: 2px 2px 8px rgba(0,0,0,0.55); }}
.accent-bar {{ width: 120px; height: 2.5px; background: {C_STEEL}; margin: 16px auto; }}
.subtitle {{ font-size: 11pt; color: {C_GOLD_L}; font-style: italic; line-height: 1.5; margin-bottom: 22px; }}
.features {{ display: flex; justify-content: center; gap: 8px; margin-bottom: 22px; flex-wrap: wrap; }}
.feature-badge {{ background: rgba(255,255,255,0.08); border: 1px solid rgba(61,111,168,0.4); color: {C_GOLD}; font-size: 7.5pt; font-weight: 700; letter-spacing: 0.5pt; padding: 4px 10px; border-radius: 3px; text-transform: uppercase; }}
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
  <title>Vehicle Maintenance Log Book -- Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Protect your investment.</strong>
        From routine oil changes to major repairs, this log book keeps
        your vehicle's complete service history in one place &mdash; boosting
        resale value and giving you peace of mind on every drive.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: {C_GOLD_L}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">What's Inside</div>
      <ul class="back-features">
        <li>30 two-page service log entries</li>
        <li>Vehicle info page with VIN, insurance, and specs</li>
        <li>Fuel and mileage tracking (MPG calculator)</li>
        <li>Tire condition monitoring per service</li>
        <li>Parts, labor, and cost breakdown per entry</li>
        <li>Annual cost summary every 10 services</li>
        <li>Large 6" x 9" format &mdash; fits in glovebox</li>
      </ul>
    </div>
    <div class="back-bottom">
      <div class="back-logo">More Shine Press</div>
    </div>
  </div>

  <div class="spine">
    <div class="spine-author">More Shine Press</div>
    <div class="spine-text">Vehicle Maintenance Log</div>
  </div>

  <div class="front-cover">
    <div class="icon-wrap">
      <svg viewBox="0 0 110 110" width="110" height="110" xmlns="http://www.w3.org/2000/svg">
        <!-- Wrench + gear icon -->
        <g transform="translate(55,55)">
          <!-- Gear -->
          <circle cx="0" cy="0" r="38" stroke="{C_STEEL}" stroke-width="1.5" fill="none" opacity="0.3"/>
          <circle cx="0" cy="0" r="30" stroke="{C_STEEL}" stroke-width="1.5" fill="none"/>
          <circle cx="0" cy="0" r="12" stroke="{C_STEEL}" stroke-width="1.2" fill="none"/>
          <!-- Gear teeth -->
          <line x1="0" y1="-38" x2="0" y2="-44" stroke="{C_STEEL}" stroke-width="2"/>
          <line x1="0" y1="38" x2="0" y2="44" stroke="{C_STEEL}" stroke-width="2"/>
          <line x1="-38" y1="0" x2="-44" y2="0" stroke="{C_STEEL}" stroke-width="2"/>
          <line x1="38" y1="0" x2="44" y2="0" stroke="{C_STEEL}" stroke-width="2"/>
          <line x1="-27" y1="-27" x2="-31" y2="-31" stroke="{C_STEEL}" stroke-width="2"/>
          <line x1="27" y1="27" x2="31" y2="31" stroke="{C_STEEL}" stroke-width="2"/>
          <line x1="-27" y1="27" x2="-31" y2="31" stroke="{C_STEEL}" stroke-width="2"/>
          <line x1="27" y1="-27" x2="31" y2="-31" stroke="{C_STEEL}" stroke-width="2"/>
          <!-- Center dot -->
          <circle cx="0" cy="0" r="4" fill="{C_STEEL}" opacity="0.7"/>
        </g>
      </svg>
    </div>
    <div class="title-block">
      <div class="main-title">Vehicle<br>Maintenance Log</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Track Every Service,<br>Every Mile, Every Repair</div>
      <div class="features">
        <span class="feature-badge">30 Service Logs</span>
        <span class="feature-badge">Fuel Tracker</span>
        <span class="feature-badge">Tire Monitor</span>
        <span class="feature-badge">Annual Summary</span>
      </div>
      <div class="tagline">For Car &amp; Truck Owners</div>
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
