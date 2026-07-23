#!/usr/bin/env python3
"""
Stargazing Journal - KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Design: Deep night sky navy + burnished gold.
A thin-line constellation star chart as the elegant graphic element.
Subtle star-field texture overlay.

Trim: 5" x 8"
Pages: 80 (white paper)
Spine: 0.1802"
Bleed: 0.125" all outer edges
Full cover: 10.4302 x 8.25 in
Publisher: More Shine Press

Usage:
  python3 generate_cover.py
  open stargazing_journal_cover_V1.0.html
"""

import os
import math

OUTPUT_FILE = "stargazing_journal_cover_V1.0.html"

# KDP cover specs
TRIM_W = 5.0
TRIM_H = 8.0
PAGES = 80
SPINE = PAGES * 0.002252   # 0.1802"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 10.4302"
COVER_H = TRIM_H + BLEED * 2               # 8.25"

# Palette — deep night sky navy + gold
C_BG_DARK     = "#0A0E1A"    # deep navy near-black
C_BG_MID      = "#101830"    # mid navy
C_BG_LIGHT    = "#1a2848"    # lighter navy
C_GOLD        = "#C4A04A"    # burnished gold
C_GOLD_DIM    = "#8a7430"    # muted gold for texture
C_GOLD_BRIGHT = "#DABE68"    # brighter gold for highlights
C_CREAM       = "#e8e2d4"    # warm cream text
C_WHITE_SOFT  = "rgba(255,255,255,0.85)"
C_WHITE_DIM   = "rgba(255,255,255,0.45)"
C_WHITE_FAINT = "rgba(255,255,255,0.12)"


def generate_svg_constellation(width_in=2.4, height_in=1.4):
    """Generate thin-line SVG constellation (stars connected by gold lines)."""
    w = width_in * 96   # px at 96dpi
    h = height_in * 96

    # Constellation star positions (Orion-inspired)
    stars = [
        # (cx, cy, r) — named stars approximating Orion
        (w * 0.30, h * 0.15, 2.8),   # Betelgeuse (top-left)
        (w * 0.68, h * 0.20, 2.2),   # Bellatrix (top-right)
        (w * 0.43, h * 0.48, 2.0),   # Belt star 1
        (w * 0.50, h * 0.52, 2.2),   # Belt star 2
        (w * 0.57, h * 0.56, 2.0),   # Belt star 3
        (w * 0.35, h * 0.82, 2.5),   # Saiph (bottom-left)
        (w * 0.66, h * 0.85, 2.4),   # Rigel (bottom-right)
        (w * 0.48, h * 0.66, 1.6),   # sword/nebula area
    ]

    # Connections between stars (index pairs)
    connections = [
        (0, 1),   # Betelgeuse - Bellatrix (shoulders)
        (0, 2),   # Betelgeuse - Belt 1
        (1, 4),   # Bellatrix - Belt 3
        (2, 3),   # Belt 1 - Belt 2
        (3, 4),   # Belt 2 - Belt 3
        (2, 5),   # Belt 1 - Saiph
        (4, 6),   # Belt 3 - Rigel
        (5, 6),   # Saiph - Rigel (feet)
        (3, 7),   # Belt 2 - sword
    ]

    lines_svg = ""
    for a, b in connections:
        x1, y1, _ = stars[a]
        x2, y2, _ = stars[b]
        lines_svg += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{C_GOLD}" stroke-width="0.6" opacity="0.7" stroke-linecap="round" />'

    stars_svg = ""
    for cx, cy, r in stars:
        # Outer glow
        stars_svg += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r*1.8:.1f}" fill="{C_GOLD_BRIGHT}" opacity="0.15" />'
        # Star body
        stars_svg += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{C_GOLD_BRIGHT}" />'
        # Inner bright dot
        stars_svg += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r*0.4:.1f}" fill="#ffffff" opacity="0.9" />'

    svg = f"""<svg width="{width_in}in" height="{height_in}in" viewBox="0 0 {w:.0f} {h:.0f}" xmlns="http://www.w3.org/2000/svg">
  {lines_svg}
  {stars_svg}
</svg>"""
    return svg


def generate_starfield():
    """Generate subtle scattered star field as SVG background texture."""
    import random
    random.seed(42)  # deterministic output
    stars = ""
    for _ in range(180):
        x = random.uniform(0, 900)
        y = random.uniform(0, 800)
        r = random.choice([0.3, 0.4, 0.5, 0.6, 0.8, 1.0])
        opacity = random.uniform(0.08, 0.4)
        stars += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#ffffff" opacity="{opacity:.2f}" />'
    return stars


def generate_front_badges():
    """Generate the front-cover feature badge row (thin gold pills)."""
    badges = [
        "35 Observation Sessions",
        "Constellation Guide",
        "Object Tracker",
        "Sketch Circle",
    ]
    items = ""
    for b in badges:
        items += f'<span class="badge-item">{b}</span>'
    return items


CONSTELLATION_SVG = generate_svg_constellation(2.4, 1.4)
STARFIELD_SVG = generate_starfield()
FRONT_BADGES = generate_front_badges()


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

  /* Star field texture overlay */
  .starfield-bg {{
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    pointer-events: none;
    z-index: 0;
  }}
  .starfield-bg svg {{
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
    content: '\\9733';
    position: absolute;
    left: 0;
    color: {C_GOLD_DIM};
    font-size: 7pt;
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
  <!-- Barcode: KDP auto-places here -->

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
    font-size: 7pt;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    white-space: nowrap;
    line-height: 1;
  }}
  .spine-author {{
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    color: {C_GOLD};
    font-size: 5pt;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-family: 'Helvetica Neue', Arial, sans-serif;
  }}
  .spine-dot {{
    width: 0.12in; height: 0.12in;
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

  /* Constellation graphic */
  .constellation-graphic {{
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

  /* Front-cover feature badges */
  .badge-row {{
    z-index: 3;
    position: relative;
    margin-top: 0.3in;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 6px 8px;
    max-width: 3.6in;
  }}
  .badge-item {{
    font-size: 6.5pt;
    color: {C_GOLD};
    letter-spacing: 1.2px;
    text-transform: uppercase;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    border: 0.5px solid {C_GOLD_DIM};
    border-radius: 10px;
    padding: 3px 9px;
    white-space: nowrap;
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
  <title>Stargazing Journal - Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- BACK COVER -->
  <div class="back-cover">
    <div class="starfield-bg">
      <svg viewBox="0 0 900 800" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
        {STARFIELD_SVG}
      </svg>
    </div>
    <div class="back-content">
      <div class="back-blurb">
        Every night sky observation is worth recording.<br>
        Whether you are spotting constellations from your<br>
        backyard or chasing galaxies under dark skies, this<br>
        journal gives you the structure to capture every<br>
        session &mdash; every object, every meteor, every<br>
        moment of wonder.
      </div>
      <div class="back-divider"></div>
      <ul class="back-features">
        <li>35 two-page observation spreads</li>
        <li>Constellation guide with 12 targets</li>
        <li>Objects observed tracker tables</li>
        <li>Eyepiece field sketch circles</li>
        <li>Sky condition and Bortle scale log</li>
        <li>Meteor shower and planet tracker</li>
        <li>Year-in-review stargazing summary</li>
        <li>Pocket-size 5&Prime; &times; 8&Prime; format for the field</li>
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
    <div class="spine-text">Stargazing Journal &mdash; More Shine Press</div>
  </div>

  <!-- FRONT COVER -->
  <div class="front-cover">
    <div class="starfield-bg">
      <svg viewBox="0 0 500 800" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
        {STARFIELD_SVG}
      </svg>
    </div>

    <div class="constellation-graphic">
      {CONSTELLATION_SVG}
    </div>

    <div class="title-block">
      <div class="title-main">Stargazing<br>Journal</div>
      <div class="title-accent"></div>
      <div class="title-sub">Track Every Constellation, Every Planet,<br>Every Meteor Shower</div>
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
