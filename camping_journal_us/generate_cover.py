#!/usr/bin/env python3
"""
Camping Journal - KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Design: Understated luxury — forest green charcoal + burnished gold.
A single thin-line tent and mountain scene as the graphic element.
Subtle topographic contour texture (represents elevation/terrain).

Trim: 5" x 8"
Pages: 80 (white paper)
Spine: 0.1802"
Bleed: 0.125" all outer edges
Full cover: 10.4302 x 8.25 in
Publisher: More Shine Press

Usage:
  python3 generate_cover.py
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' \\
    --headless --disable-gpu --no-margins --no-pdf-header-footer \\
    --print-to-pdf="camping_journal_cover_V1.0.pdf" \\
    "file://$PWD/camping_journal_cover_V1.0.html"
"""

import os
import math

OUTPUT_FILE = "camping_journal_cover_V1.0.html"

# KDP cover specs
TRIM_W = 5.0
TRIM_H = 8.0
PAGES = 80
SPINE = PAGES * 0.002252   # 0.1802"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 10.4302"
COVER_H = TRIM_H + BLEED * 2               # 8.25"

# Palette — forest green charcoal + burnished gold
C_BG_DARK     = "#121612"    # near-black forest charcoal
C_BG_MID      = "#1a2418"    # forest green charcoal
C_BG_LIGHT    = "#2a3a2e"    # lighter forest green
C_GOLD        = "#C4A04A"    # burnished gold
C_GOLD_DIM    = "#8a7430"    # muted gold for texture
C_GOLD_BRIGHT = "#DABE68"    # brighter gold for highlights
C_CREAM       = "#e8e2d4"    # warm cream text
C_WHITE_SOFT  = "rgba(255,255,255,0.85)"
C_WHITE_DIM   = "rgba(255,255,255,0.45)"
C_WHITE_FAINT = "rgba(255,255,255,0.12)"


def generate_svg_camp_scene(width_in=2.4, height_in=1.4):
    """Generate thin-line SVG tent and mountain scene with stars — the single elegant graphic element."""
    w = width_in * 96   # px at 96dpi
    h = height_in * 96

    # Base line (ground)
    base_y = h * 0.82

    # --- Peak 1 (left, medium) ---
    p1_apex_x = w * 0.22
    p1_apex_y = h * 0.30
    p1_left_x = -w * 0.02
    p1_left_y = base_y
    p1_right_x = w * 0.42
    p1_right_y = base_y

    # Inner ridge line (snow cap hint) for peak 1
    p1_inner_left_x = p1_apex_x - (p1_apex_x - p1_left_x) * 0.22
    p1_inner_left_y = p1_apex_y + (base_y - p1_apex_y) * 0.22
    p1_inner_right_x = p1_apex_x + (p1_right_x - p1_apex_x) * 0.22
    p1_inner_right_y = p1_apex_y + (base_y - p1_apex_y) * 0.22

    # --- Peak 2 (center, tallest) ---
    p2_apex_x = w * 0.52
    p2_apex_y = h * 0.12
    p2_left_x = w * 0.30
    p2_left_y = base_y
    p2_right_x = w * 0.72
    p2_right_y = base_y

    # Inner ridge for peak 2
    p2_inner_left_x = p2_apex_x - (p2_apex_x - p2_left_x) * 0.20
    p2_inner_left_y = p2_apex_y + (base_y - p2_apex_y) * 0.18
    p2_inner_right_x = p2_apex_x + (p2_right_x - p2_apex_x) * 0.20
    p2_inner_right_y = p2_apex_y + (base_y - p2_apex_y) * 0.18

    # --- Peak 3 (right, medium-short) ---
    p3_apex_x = w * 0.80
    p3_apex_y = h * 0.38
    p3_left_x = w * 0.62
    p3_left_y = base_y
    p3_right_x = w * 1.02
    p3_right_y = base_y

    # Inner ridge for peak 3
    p3_inner_left_x = p3_apex_x - (p3_apex_x - p3_left_x) * 0.22
    p3_inner_left_y = p3_apex_y + (base_y - p3_apex_y) * 0.22
    p3_inner_right_x = p3_apex_x + (p3_right_x - p3_apex_x) * 0.22
    p3_inner_right_y = p3_apex_y + (base_y - p3_apex_y) * 0.22

    # Sun/moon circle (upper right area)
    sun_cx = w * 0.78
    sun_cy = h * 0.18
    sun_r = h * 0.085

    # --- Tent (center foreground) ---
    tent_base_y = base_y
    tent_top_y = h * 0.55
    tent_left_x = w * 0.38
    tent_right_x = w * 0.62
    tent_center_x = w * 0.50

    # Inner tent door lines
    door_left_x = w * 0.43
    door_right_x = w * 0.57
    door_top_y = h * 0.65
    door_bottom_y = tent_base_y

    svg = f"""<svg width="{width_in}in" height="{height_in}in" viewBox="0 0 {w:.0f} {h:.0f}" xmlns="http://www.w3.org/2000/svg">
  <!-- Sun / Moon -->
  <circle cx="{sun_cx:.1f}" cy="{sun_cy:.1f}" r="{sun_r:.1f}" fill="none" stroke="{C_GOLD}" stroke-width="1.3" />
  <circle cx="{sun_cx:.1f}" cy="{sun_cy:.1f}" r="{sun_r*0.45:.1f}" fill="none" stroke="{C_GOLD_DIM}" stroke-width="0.7" />

  <!-- Stars -->
  <circle cx="{w*0.10:.1f}" cy="{h*0.10:.1f}" r="0.8" fill="{C_GOLD_DIM}" opacity="0.7" />
  <circle cx="{w*0.25:.1f}" cy="{h*0.06:.1f}" r="0.6" fill="{C_GOLD_DIM}" opacity="0.5" />
  <circle cx="{w*0.35:.1f}" cy="{h*0.15:.1f}" r="0.7" fill="{C_GOLD_DIM}" opacity="0.6" />
  <circle cx="{w*0.65:.1f}" cy="{h*0.08:.1f}" r="0.6" fill="{C_GOLD_DIM}" opacity="0.5" />
  <circle cx="{w*0.92:.1f}" cy="{h*0.35:.1f}" r="0.7" fill="{C_GOLD_DIM}" opacity="0.6" />
  <circle cx="{w*0.05:.1f}" cy="{h*0.25:.1f}" r="0.5" fill="{C_GOLD_DIM}" opacity="0.4" />

  <!-- Peak 1 (left, medium) -->
  <polyline points="{p1_left_x:.1f},{p1_left_y:.1f} {p1_inner_left_x:.1f},{p1_inner_left_y:.1f} {p1_apex_x:.1f},{p1_apex_y:.1f} {p1_inner_right_x:.1f},{p1_inner_right_y:.1f} {p1_right_x:.1f},{p1_right_y:.1f}" fill="none" stroke="{C_GOLD}" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round" />

  <!-- Peak 2 (center, tallest) -->
  <polyline points="{p2_left_x:.1f},{p2_left_y:.1f} {p2_inner_left_x:.1f},{p2_inner_left_y:.1f} {p2_apex_x:.1f},{p2_apex_y:.1f} {p2_inner_right_x:.1f},{p2_inner_right_y:.1f} {p2_right_x:.1f},{p2_right_y:.1f}" fill="none" stroke="{C_GOLD}" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" />

  <!-- Peak 3 (right) -->
  <polyline points="{p3_left_x:.1f},{p3_left_y:.1f} {p3_inner_left_x:.1f},{p3_inner_left_y:.1f} {p3_apex_x:.1f},{p3_apex_y:.1f} {p3_inner_right_x:.1f},{p3_inner_right_y:.1f} {p3_right_x:.1f},{p3_right_y:.1f}" fill="none" stroke="{C_GOLD_DIM}" stroke-width="1.2" stroke-linejoin="round" stroke-linecap="round" />

  <!-- Tent (center foreground) -->
  <polyline points="{tent_left_x:.1f},{tent_base_y:.1f} {tent_center_x:.1f},{tent_top_y:.1f} {tent_right_x:.1f},{tent_base_y:.1f}" fill="none" stroke="{C_GOLD}" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round" />
  <!-- Tent door -->
  <polyline points="{door_left_x:.1f},{door_bottom_y:.1f} {w*0.50:.1f},{door_top_y:.1f} {door_right_x:.1f},{door_bottom_y:.1f}" fill="none" stroke="{C_GOLD_DIM}" stroke-width="0.8" stroke-linejoin="round" />

  <!-- Ground line -->
  <line x1="0" y1="{base_y:.1f}" x2="{w:.0f}" y2="{base_y:.1f}" stroke="{C_GOLD_DIM}" stroke-width="0.7" opacity="0.6" />
</svg>"""
    return svg


def generate_topo_pattern():
    """Generate subtle topographic contour lines as SVG background texture."""
    lines = ""
    # Gentle flowing contour curves
    for level in range(12):
        y_base = 50 + level * 55
        amplitude = 20 + level * 3
        freq = 0.008 + level * 0.001
        offset = level * 15
        path_d = f"M 0 {y_base} "
        for x in range(0, 900, 8):
            y = y_base + amplitude * math.sin(freq * x + offset) + amplitude * 0.4 * math.sin(freq * 2.3 * x)
            path_d += f"L {x} {y:.1f} "
        opacity = 0.02 + (level % 3) * 0.01
        stroke_w = 0.6 if level % 2 == 0 else 0.4
        lines += f'<path d="{path_d}" fill="none" stroke="{C_GOLD_DIM}" stroke-width="{stroke_w}" opacity="{opacity}" />'
    return lines


def generate_front_badges():
    """Generate the front-cover feature badge row (thin gold pills)."""
    badges = [
        "35 Camp Logs",
        "Campsite Tracker",
        "Stargazing Notes",
        "Wildlife Log",
    ]
    items = ""
    for b in badges:
        items += f'<span class="badge-item">{b}</span>'
    return items


CAMP_SVG = generate_svg_camp_scene(2.4, 1.4)
TOPO_SVG = generate_topo_pattern()
FRONT_BADGES = generate_front_badges()


CSS = r"""
<style>
  @page { size: 10.4302in 8.2500in; margin: 0; }
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: Georgia, 'Iowan Old Style', 'Palatino', serif;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  .cover-wrap {
    width: 10.4302in;
    height: 8.2500in;
    position: relative;
    display: flex;
  }

  /* === BACK COVER === */
  .back-cover {
    width: 5.1250in;
    height: 8.2500in;
    background: linear-gradient(170deg, #121612 0%, #1a2418 100%);
    padding: 0.65in 0.45in 0.5in 0.1250in;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
  }

  /* Topographic texture overlay */
  .topo-bg {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    pointer-events: none;
    z-index: 0;
  }
  .topo-bg svg {
    width: 100%; height: 100%;
  }

  .back-content {
    position: relative;
    z-index: 2;
  }

  .back-blurb {
    color: rgba(255,255,255,0.85);
    font-size: 9pt;
    line-height: 1.65;
    font-style: italic;
    margin-bottom: 18px;
  }

  .back-divider {
    width: 36px;
    height: 1px;
    background: #C4A04A;
    margin-bottom: 14px;
    opacity: 0.6;
  }

  .back-features {
    list-style: none;
    padding: 0;
  }
  .back-features li {
    font-size: 8pt;
    color: rgba(255,255,255,0.45);
    padding: 3px 0;
    padding-left: 16px;
    position: relative;
    line-height: 1.4;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    letter-spacing: 0.3px;
  }
  .back-features li::before {
    content: '—';
    position: absolute;
    left: 0;
    color: #8a7430;
    font-size: 8pt;
  }

  .back-bottom {
    position: relative;
    z-index: 2;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .back-logo {
    color: #C4A04A;
    font-size: 7.5pt;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    padding-top: 10px;
    border-top: 1px solid rgba(255,255,255,0.12);
    margin-top: 16px;
    text-align: left;
    padding-right: 20px;
  }

  /* === SPINE === */
  .spine {
    width: 0.1802in;
    height: 8.2500in;
    background: linear-gradient(180deg, #121612 0%, #1a2418 50%, #121612 100%);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 0.6in 0;
    position: relative;
    z-index: 2;
  }
  .spine-text {
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    color: rgba(255,255,255,0.85);
    font-size: 7pt;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    white-space: nowrap;
    line-height: 1;
  }
  .spine-author {
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    color: #C4A04A;
    font-size: 5pt;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-family: 'Helvetica Neue', Arial, sans-serif;
  }
  .spine-dot {
    width: 0.12in; height: 0.12in;
    border: 1px solid #8a7430;
    border-radius: 50%;
    opacity: 0.5;
  }

  /* === FRONT COVER === */
  .front-cover {
    width: 5.1250in;
    height: 8.2500in;
    background: linear-gradient(170deg, #121612 0%, #1a2418 60%, #2a3a2e 100%);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 0.4in;
    text-align: center;
  }

  /* Camp graphic */
  .peak-graphic {
    margin-bottom: 0.35in;
    z-index: 3;
    position: relative;
  }

  /* Title block */
  .title-block {
    z-index: 3;
    position: relative;
  }
  .title-main {
    font-size: 20pt;
    font-weight: 400;
    color: #e8e2d4;
    letter-spacing: 4px;
    line-height: 1.25;
    text-transform: uppercase;
  }
  .title-accent {
    width: 1.8in;
    height: 1px;
    background: linear-gradient(90deg, transparent 0%, #C4A04A 40%, #C4A04A 60%, transparent 100%);
    margin: 0.18in auto;
  }
  .title-sub {
    font-size: 9pt;
    color: rgba(255,255,255,0.45);
    font-style: italic;
    letter-spacing: 1px;
    line-height: 1.4;
  }

  /* Front-cover feature badges */
  .badge-row {
    z-index: 3;
    position: relative;
    margin-top: 0.3in;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 6px 8px;
    max-width: 3.6in;
  }
  .badge-item {
    font-size: 6.5pt;
    color: #C4A04A;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    border: 0.5px solid #8a7430;
    border-radius: 10px;
    padding: 3px 9px;
    white-space: nowrap;
  }

  .publisher {
    position: absolute;
    bottom: 0.45in;
    left: 0; right: 0;
    text-align: center;
    color: #C4A04A;
    font-size: 7pt;
    letter-spacing: 4px;
    text-transform: uppercase;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    z-index: 3;
  }

  /* Screen-only border */
  @media screen {
    .cover-wrap { border: 1px solid #333; }
  }
</style>
"""


def generate(output_path=OUTPUT_FILE):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Camping Journal - Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- BACK COVER -->
  <div class="back-cover">
    <div class="topo-bg">
      <svg viewBox="0 0 900 800" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
        {TOPO_SVG}
      </svg>
    </div>
    <div class="back-content">
      <div class="back-blurb">
        Every campfire tells a story. From the first tent stake<br>
        to the last ember of the night, your camping journey<br>
        deserves to be documented with care. This journal gives<br>
        you the structure to capture every trip &mdash; every starry<br>
        night, every wildlife encounter, every adventure.
      </div>
      <div class="back-divider"></div>
      <ul class="back-features">
        <li>35 two-page camp log spreads</li>
        <li>Leave No Trace reference card</li>
        <li>Packing checklist with essentials</li>
        <li>Camp type and campground tracker</li>
        <li>Wildlife and camp conditions notes</li>
        <li>Year-in-review camping summary</li>
        <li>Sketch area for campsite maps</li>
        <li>Pocket-size 5&Prime; &times; 8&Prime; format for your pack</li>
      </ul>
    </div>
    <div class="back-bottom">
      <div class="back-logo">More Shine Press</div>
      <!-- Barcode: KDP auto-places here -->
    </div>
  </div>

  <!-- SPINE -->
  <div class="spine">
    <div class="spine-author">More Shine Press</div>
    <div class="spine-dot"></div>
    <div class="spine-text">Camping Journal &mdash; More Shine Press</div>
  </div>

  <!-- FRONT COVER -->
  <div class="front-cover">
    <div class="topo-bg">
      <svg viewBox="0 0 500 800" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
        {TOPO_SVG}
      </svg>
    </div>

    <div class="peak-graphic">
      {CAMP_SVG}
    </div>

    <div class="title-block">
      <div class="title-main">Camping<br>Journal</div>
      <div class="title-accent"></div>
      <div class="title-sub">Capture Every Campfire, Every<br>Starry Night, Every Adventure</div>
    </div>

    <div class="badge-row">
      {FRONT_BADGES}
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
    abs_path = os.path.abspath(path)
    print(f"[OK] Cover generated: {abs_path}")
    print(f"     Full cover: {COVER_W:.4f} x {COVER_H:.4f} in")
    print(f"     Spine: {SPINE:.4f} in ({PAGES} pages, white paper)")
    print(f"     At 300 DPI: {COVER_W*300:.0f} x {COVER_H*300:.0f} px")
    print(f"")
    print(f"     Next: open {abs_path} in browser")
    print(f"           Then Cmd+P -> Save as PDF (Margins: None, Scale: 100%)")
