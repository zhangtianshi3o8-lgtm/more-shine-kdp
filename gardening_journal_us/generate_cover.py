#!/usr/bin/env python3
"""
Gardening Journal - KDP Full Wrap Cover Generator
Zero-dependency (Python stdlib only).

Design: Understated luxury — sage/olive earth + burnished gold.
A single thin-line leaf/seedling illustration as the only graphic element.
Subtle organic texture (represents soil/growth layers).

Trim: 5" x 8"
Pages: 80 (white paper)
Spine: 0.1802"
Bleed: 0.125" all outer edges
Full cover: 10.4302 x 8.25 in
Publisher: More Shine Press

Usage:
  python3 generate_cover.py
  open gardening_journal_cover_V1.0.html
"""

import os
import math

OUTPUT_FILE = "gardening_journal_cover_V1.0.html"

# KDP cover specs
TRIM_W = 5.0
TRIM_H = 8.0
PAGES = 80
SPINE = PAGES * 0.002252   # 0.1802"
BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2   # 10.4302"
COVER_H = TRIM_H + BLEED * 2               # 8.25"

# Palette — sage/olive earth + gold
C_BG_DARK     = "#12160E"    # near-black olive
C_BG_MID      = "#1A2014"
C_BG_LIGHT    = "#2A3320"
C_GOLD        = "#C4A04A"    # burnished gold
C_GOLD_DIM    = "#8a7430"    # muted gold for texture
C_GOLD_BRIGHT = "#DABE68"    # brighter gold for highlights
C_CREAM       = "#e8e2d4"    # warm cream text
C_WHITE_SOFT  = "rgba(255,255,255,0.85)"
C_WHITE_DIM   = "rgba(255,255,255,0.45)"
C_WHITE_FAINT = "rgba(255,255,255,0.12)"


def generate_svg_seedling(width_in=2.4, height_in=1.4):
    """Generate thin-line SVG leaf/seedling — the single elegant graphic element."""
    w = width_in * 96   # px at 96dpi
    h = height_in * 96

    # Ground line
    base_y = h * 0.82

    # --- Center stem ---
    stem_base_x = w * 0.50
    stem_top_y = h * 0.28

    # --- Left leaf ---
    left_leaf_tip_x = w * 0.20
    left_leaf_tip_y = h * 0.36
    left_leaf_base_x = w * 0.46
    left_leaf_base_y = h * 0.50
    # left leaf curve control points
    left_ctrl_top_x = w * 0.30
    left_ctrl_top_y = h * 0.34
    left_ctrl_bot_x = w * 0.38
    left_ctrl_bot_y = h * 0.54

    # --- Right leaf ---
    right_leaf_tip_x = w * 0.80
    right_leaf_tip_y = h * 0.30
    right_leaf_base_x = w * 0.54
    right_leaf_base_y = h * 0.46
    # right leaf curve control points
    right_ctrl_top_x = w * 0.70
    right_ctrl_top_y = h * 0.26
    right_ctrl_bot_x = w * 0.62
    right_ctrl_bot_y = h * 0.50

    # --- Top sprout leaf ---
    top_leaf_tip_x = w * 0.50
    top_leaf_tip_y = h * 0.14
    top_leaf_left_x = w * 0.44
    top_leaf_right_x = w * 0.56

    # Midrib lines for leaves
    left_mid_x1 = w * 0.46
    left_mid_y1 = h * 0.50
    left_mid_x2 = w * 0.22
    left_mid_y2 = h * 0.37

    right_mid_x1 = w * 0.54
    right_mid_y1 = h * 0.46
    right_mid_x2 = w * 0.78
    right_mid_y2 = h * 0.31

    svg = f"""<svg width="{width_in}in" height="{height_in}in" viewBox="0 0 {w:.0f} {h:.0f}" xmlns="http://www.w3.org/2000/svg">
  <!-- Stem -->
  <path d="M {stem_base_x:.1f} {base_y:.1f} Q {stem_base_x:.1f} {h*0.55:.1f} {stem_base_x:.1f} {stem_top_y:.1f}" fill="none" stroke="{C_GOLD}" stroke-width="1.5" stroke-linecap="round" />

  <!-- Left leaf outline -->
  <path d="M {left_leaf_base_x:.1f} {left_leaf_base_y:.1f} Q {left_ctrl_top_x:.1f} {left_ctrl_top_y:.1f} {left_leaf_tip_x:.1f} {left_leaf_tip_y:.1f} Q {left_ctrl_bot_x:.1f} {left_ctrl_bot_y:.1f} {left_leaf_base_x:.1f} {left_leaf_base_y:.1f}" fill="none" stroke="{C_GOLD}" stroke-width="1.3" stroke-linejoin="round" />
  <!-- Left leaf midrib -->
  <line x1="{left_mid_x1:.1f}" y1="{left_mid_y1:.1f}" x2="{left_mid_x2:.1f}" y2="{left_mid_y2:.1f}" stroke="{C_GOLD_DIM}" stroke-width="0.7" />

  <!-- Right leaf outline -->
  <path d="M {right_leaf_base_x:.1f} {right_leaf_base_y:.1f} Q {right_ctrl_top_x:.1f} {right_ctrl_top_y:.1f} {right_leaf_tip_x:.1f} {right_leaf_tip_y:.1f} Q {right_ctrl_bot_x:.1f} {right_ctrl_bot_y:.1f} {right_leaf_base_x:.1f} {right_leaf_base_y:.1f}" fill="none" stroke="{C_GOLD}" stroke-width="1.4" stroke-linejoin="round" />
  <!-- Right leaf midrib -->
  <line x1="{right_mid_x1:.1f}" y1="{right_mid_y1:.1f}" x2="{right_mid_x2:.1f}" y2="{right_mid_y2:.1f}" stroke="{C_GOLD_DIM}" stroke-width="0.7" />

  <!-- Top sprout leaf -->
  <path d="M {top_leaf_left_x:.1f} {stem_top_y:.1f} Q {top_leaf_tip_x:.1f} {top_leaf_tip_y:.1f} {top_leaf_right_x:.1f} {stem_top_y:.1f}" fill="none" stroke="{C_GOLD}" stroke-width="1.2" stroke-linejoin="round" />

  <!-- Ground line -->
  <line x1="0" y1="{base_y:.1f}" x2="{w:.0f}" y2="{base_y:.1f}" stroke="{C_GOLD_DIM}" stroke-width="0.7" opacity="0.6" />
</svg>"""
    return svg


def generate_organic_pattern():
    """Generate subtle organic contour lines as SVG background texture (soil/growth layers)."""
    lines = ""
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
        "35 Garden Entries",
        "Season Tracker",
        "Harvest Log",
        "Companion Guide",
    ]
    items = ""
    for b in badges:
        items += f'<span class="badge-item">{b}</span>'
    return items


SEEDLING_SVG = generate_svg_seedling(2.4, 1.4)
ORGANIC_SVG = generate_organic_pattern()
FRONT_BADGES = generate_front_badges()


CSS = r"""
<style>
  @page { size: 10.4302in 8.25in; margin: 0; }
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: Georgia, 'Iowan Old Style', 'Palatino', serif;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  .cover-wrap {
    width: 10.4302in;
    height: 8.25in;
    position: relative;
    display: flex;
  }

  /* === BACK COVER === */
  .back-cover {
    width: 5.125in;
    height: 8.25in;
    background: linear-gradient(170deg, #12160E 0%, #1A2014 100%);
    padding: 0.65in 0.45in 0.5in 0.125in;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
  }

  /* Organic texture overlay */
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
    height: 8.25in;
    background: linear-gradient(180deg, #12160E 0%, #1A2014 50%, #12160E 100%);
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
    width: 5.125in;
    height: 8.25in;
    background: linear-gradient(170deg, #12160E 0%, #1A2014 60%, #2A3320 100%);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 0.4in;
    text-align: center;
  }

  /* Seedling graphic */
  .seedling-graphic {
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
  <title>Gardening Journal - Cover</title>
  {CSS}
</head>
<body>
<div class="cover-wrap">

  <!-- BACK COVER -->
  <div class="back-cover">
    <div class="topo-bg">
      <svg viewBox="0 0 900 800" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
        {ORGANIC_SVG}
      </svg>
    </div>
    <div class="back-content">
      <div class="back-blurb">
        There is a quiet joy in watching your garden grow &mdash; from<br>
        the first seed pushing through the soil to the last harvest<br>
        of the season. This journal gives you the structure to record<br>
        every planting, every bloom, and every harvest through all<br>
        four seasons of your gardening year.
      </div>
      <div class="back-divider"></div>
      <ul class="back-features">
        <li>35 two-page garden entry spreads</li>
        <li>Season and weather tracker</li>
        <li>Companion planting guide</li>
        <li>Garden essentials checklist</li>
        <li>Pest and disease log</li>
        <li>Harvest tracker with weight totals</li>
        <li>Bed layout sketch area with dot grid</li>
        <li>Pocket-size 5&Prime; &times; 8&Prime; format for the garden shed</li>
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
    <div class="spine-text">Gardening Journal &mdash; More Shine Press</div>
  </div>

  <!-- FRONT COVER -->
  <div class="front-cover">
    <div class="topo-bg">
      <svg viewBox="0 0 500 800" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
        {ORGANIC_SVG}
      </svg>
    </div>

    <div class="seedling-graphic">
      {SEEDLING_SVG}
    </div>

    <div class="title-block">
      <div class="title-main">Gardening<br>Journal</div>
      <div class="title-accent"></div>
      <div class="title-sub">Track Every Seed, Every Bloom,<br>Every Harvest</div>
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
