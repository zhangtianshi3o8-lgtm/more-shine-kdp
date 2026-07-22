#!/usr/bin/env python3
"""
Cycling Adventure Journal - KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Design: Understated luxury — charcoal black + burnished gold.
A single thin-line bicycle wheel as the only graphic element.
Subtle topographic contour texture (represents elevation/terrain).

Trim: 5" x 8"
Pages: 80 (white paper)
Spine: 0.1802"
Bleed: 0.125" all outer edges
Full cover: 10.43 x 8.25 in
Publisher: More Shine Press

Usage:
  python3 generate_cover.py
  open cycling_cover.html
  # Cmd+P -> Save as PDF (Margins: None, Scale: 100%)
"""

import os
import math

OUTPUT_FILE = "cycling_cover.html"

# KDP cover specs
TRIM_W = 5.0
TRIM_H = 8.0
PAGES = 80
SPINE = PAGES * 0.002252   # 0.1802"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 10.4302"
COVER_H = TRIM_H + BLEED * 2               # 8.25"

# Palette — understated luxury
C_BG_DARK     = "#161616"    # near-black charcoal
C_BG_MID      = "#1e1e20"
C_BG_LIGHT    = "#2a2a2e"
C_GOLD        = "#C4A04A"    # burnished gold
C_GOLD_DIM    = "#8a7430"    # muted gold for texture
C_GOLD_BRIGHT = "#DABE68"    # brighter gold for highlights
C_CREAM       = "#e8e2d4"    # warm cream text
C_WHITE_SOFT  = "rgba(255,255,255,0.85)"
C_WHITE_DIM   = "rgba(255,255,255,0.45)"
C_WHITE_FAINT = "rgba(255,255,255,0.12)"


def generate_svg_bicycle_wheel(diameter_in=1.4):
    """Generate a thin-line SVG bicycle wheel — the single elegant graphic element."""
    cx = diameter_in / 2 * 96  # px at 96dpi
    cy = cx
    r_outer = diameter_in / 2 * 96 * 0.95
    r_inner_hub = r_outer * 0.12
    r_rim = r_outer * 0.88
    num_spokes = 20

    spokes_svg = ""
    for i in range(num_spokes):
        angle = 2 * math.pi * i / num_spokes
        x1 = cx + r_inner_hub * math.cos(angle)
        y1 = cy + r_inner_hub * math.sin(angle)
        x2 = cx + r_rim * math.cos(angle)
        y2 = cy + r_rim * math.sin(angle)
        spokes_svg += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{C_GOLD_DIM}" stroke-width="0.6" />'

    return f"""<svg width="{diameter_in}in" height="{diameter_in}in" viewBox="0 0 {cx*2:.0f} {cy*2:.0f}" xmlns="http://www.w3.org/2000/svg">
  <!-- Outer rim -->
  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r_outer:.1f}" fill="none" stroke="{C_GOLD}" stroke-width="1.5" />
  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r_rim:.1f}" fill="none" stroke="{C_GOLD_DIM}" stroke-width="0.8" />
  <!-- Spokes -->
  {spokes_svg}
  <!-- Hub -->
  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r_inner_hub:.1f}" fill="none" stroke="{C_GOLD}" stroke-width="1.2" />
  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r_inner_hub * 0.5:.1f}" fill="{C_GOLD_DIM}" />
</svg>"""


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


WHEEL_SVG = generate_svg_bicycle_wheel(1.35)
TOPO_SVG = generate_topo_pattern()


CSS = f"""
<style>
  @page {{ size: {COVER_W:.4f}in {COVER_H:.4f}in; margin: 0; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: Georgia, 'Iowan Old Style', 'Palatino', serif;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  .cover-wrap {{
    width: {COVER_W:.4f}in;
    height: {COVER_H:.4f}in;
    position: relative;
    display: flex;
  }}

  /* === BACK COVER === */
  .back-cover {{
    width: {TRIM_W + BLEED:.4f}in;
    height: {COVER_H:.4f}in;
    background: linear-gradient(170deg, {C_BG_DARK} 0%, {C_BG_MID} 100%);
    padding: 0.65in 0.45in 0.5in {BLEED:.4f}in;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
  }}

  /* Topographic texture overlay */
  .topo-bg {{
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    pointer-events: none;
    z-index: 0;
  }}
  .topo-bg svg {{
    width: 100%; height: 100%;
  }}

  .back-content {{
    position: relative;
    z-index: 2;
  }}

  .back-blurb {{
    color: {C_WHITE_SOFT};
    font-size: 9pt;
    line-height: 1.65;
    font-style: italic;
    margin-bottom: 18px;
  }}

  .back-divider {{
    width: 36px;
    height: 1px;
    background: {C_GOLD};
    margin-bottom: 14px;
    opacity: 0.6;
  }}

  .back-features {{
    list-style: none;
    padding: 0;
  }}
  .back-features li {{
    font-size: 8pt;
    color: {C_WHITE_DIM};
    padding: 3px 0;
    padding-left: 16px;
    position: relative;
    line-height: 1.4;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    letter-spacing: 0.3px;
  }}
  .back-features li::before {{
    content: '—';
    position: absolute;
    left: 0;
    color: {C_GOLD_DIM};
    font-size: 8pt;
  }}

  .back-bottom {{
    position: relative;
    z-index: 2;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }}
  .back-logo {{
    color: {C_GOLD};
    font-size: 7.5pt;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    padding-top: 10px;
    border-top: 1px solid {C_WHITE_FAINT};
    margin-top: 16px;
    text-align: left;
    padding-right: 20px;
  }}
  .barcode-area {{
    width: 2in;
    height: 1.2in;
    background: white;
    border-radius: 1px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 6pt;
    color: #ccc;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    flex-shrink: 0;
  }}

  /* === SPINE === */
  .spine {{
    width: {SPINE:.4f}in;
    height: {COVER_H:.4f}in;
    background: linear-gradient(180deg, {C_BG_DARK} 0%, {C_BG_MID} 50%, {C_BG_DARK} 100%);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 0.6in 0;
    position: relative;
    z-index: 2;
  }}
  .spine-text {{
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    color: {C_WHITE_SOFT};
    font-size: 7.5pt;
    font-weight: 600;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    white-space: nowrap;
    line-height: 1;
  }}
  .spine-author {{
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    color: {C_GOLD};
    font-size: 5.5pt;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-family: 'Helvetica Neue', Arial, sans-serif;
  }}
  .spine-dot {{
    width: 0.14in; height: 0.14in;
    border: 1px solid {C_GOLD_DIM};
    border-radius: 50%;
    opacity: 0.5;
  }}

  /* === FRONT COVER === */
  .front-cover {{
    width: {TRIM_W + BLEED:.4f}in;
    height: {COVER_H:.4f}in;
    background: linear-gradient(170deg, {C_BG_DARK} 0%, {C_BG_MID} 60%, {C_BG_LIGHT} 100%);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 0.4in;
    text-align: center;
  }}

  /* Wheel graphic */
  .wheel-graphic {{
    margin-bottom: 0.35in;
    z-index: 3;
    position: relative;
  }}

  /* Title block */
  .title-block {{
    z-index: 3;
    position: relative;
  }}
  .title-main {{
    font-size: 20pt;
    font-weight: 400;
    color: {C_CREAM};
    letter-spacing: 4px;
    line-height: 1.25;
    text-transform: uppercase;
  }}
  .title-accent {{
    width: 1.8in;
    height: 1px;
    background: linear-gradient(90deg, transparent 0%, {C_GOLD} 40%, {C_GOLD} 60%, transparent 100%);
    margin: 0.18in auto;
  }}
  .title-sub {{
    font-size: 9pt;
    color: {C_WHITE_DIM};
    font-style: italic;
    letter-spacing: 1px;
    line-height: 1.4;
  }}

  .publisher {{
    position: absolute;
    bottom: 0.45in;
    left: 0; right: 0;
    text-align: center;
    color: {C_GOLD};
    font-size: 7pt;
    letter-spacing: 4px;
    text-transform: uppercase;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    z-index: 3;
  }}

  /* Screen-only border */
  @media screen {{
    .cover-wrap {{ border: 1px solid #333; }}
  }}
</style>
"""


def generate(output_path=OUTPUT_FILE):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cycling Adventure Journal - Cover</title>
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
        Every ride has a story &mdash; the climbs, the descents,<br>
        the weather, the road. This journal gives you the space<br>
        to capture it all.
      </div>
      <div class="back-divider"></div>
      <ul class="back-features">
        <li>35 two-page ride logs with detailed stats</li>
        <li>Route sketch area for maps and directions</li>
        <li>Elevation, weather, and difficulty tracking</li>
        <li>Space for highlights, challenges, memories</li>
        <li>Bike setup page and season summary</li>
        <li>Pocket-size 5&Prime; &times; 8&Prime;</li>
      </ul>
    </div>
    <div class="back-bottom">
      <div class="back-logo">More Shine Press</div>
      <div class="barcode-area">ISBN Barcode Area</div>
    </div>
  </div>

  <!-- SPINE -->
  <div class="spine">
    <div class="spine-author">More Shine Press</div>
    <div class="spine-dot"></div>
    <div class="spine-text">Cycling Adventure Journal</div>
  </div>

  <!-- FRONT COVER -->
  <div class="front-cover">
    <div class="topo-bg">
      <svg viewBox="0 0 500 800" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
        {TOPO_SVG}
      </svg>
    </div>

    <div class="wheel-graphic">
      {WHEEL_SVG}
    </div>

    <div class="title-block">
      <div class="title-main">Cycling<br>Adventure<br>Journal</div>
      <div class="title-accent"></div>
      <div class="title-sub">A Rider's Log for Roads,<br>Trails &amp; Journeys</div>
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
