#!/usr/bin/env python3
"""
KDP Bible Study Handbook — Cover Generator (Redesigned)
========================================================
Market-researched cover design based on Amazon bestseller analysis.

Style: "Modern Botanical Moody"
- Deep forest green background with subtle gradient depth
- Gold olive-branch line art (SVG, hand-drawn feel)
- Elegant serif typography with refined hierarchy
- No author name (per user request)
- Premium, cross-denominational, gender-neutral

This file generates BOTH:
1. A standalone cover preview (single page, easy to view)
2. The cover integrated into the full handbook HTML

Trim: 8.5" x 11" (matches interior)

Usage:
  python3 generate_cover.py
  # Open cover_preview.html → Cmd+P → Save as PDF
"""

import os

OUTPUT_FILE = "cover_preview.html"

# ====================================================================
# PALETTE — Forest Green + Gold (market-researched premium combo)
# ====================================================================
FOREST_DARK   = "#1a3329"   # deep forest — main background
FOREST_MID    = "#244438"   # lighter forest — gradient
FOREST_LIGHT  = "#2d5a47"   # subtle highlight
GOLD          = "#c9a84c"   # antique gold — botanical & accents
GOLD_BRIGHT   = "#dcc078"   # brighter gold — title highlight
GOLD_PALE     = "rgba(201,168,76,0.3)"
CREAM         = "#f5f0e1"   # warm ivory — subtitle text
WHITE_SOFT    = "rgba(255,255,255,0.85)"

SERIF_ELEGANT = "'Playfair Display', 'Cormorant Garamond', 'Georgia', serif"
SERIF_CLASSIC = "'Lora', 'Georgia', 'Palatino Linotype', serif"
SANS_CLEAN    = "'Montserrat', 'Helvetica Neue', 'Arial', sans-serif"

# ====================================================================
# SVG BOTANICAL ELEMENTS
# Gold olive branch line art — hand-drawn aesthetic
# ====================================================================

def olive_branch_corner(corner="bottom-right", flip_x=False, flip_y=False, scale=1.0):
    """
    SVG olive branch suitable for corner placement.
    Uses simple path strokes + ellipse leaves for a line-art look.
    """
    sx = "scale(1,1)" if not flip_x else "scale(-1,1)"
    sy = "" if not flip_y else "scale(1,-1)"
    s = f"scale({scale})"

    return f"""
<svg class="botanical" viewBox="0 0 300 400" xmlns="http://www.w3.org/2000/svg"
     preserveAspectRatio="xMidYMid meet"
     style="position:absolute; {corner}:0; width:340px; opacity:0.75;">
  <g transform="{s}">
    <!-- main stem -->
    <path d="M 250 380 Q 220 300 200 250 Q 180 190 160 130 Q 145 90 130 50"
          fill="none" stroke="{GOLD}" stroke-width="1.2" stroke-linecap="round"/>
    <!-- secondary stem branch -->
    <path d="M 200 250 Q 230 230 260 210"
          fill="none" stroke="{GOLD}" stroke-width="0.8" stroke-linecap="round" opacity="0.6"/>
    <path d="M 160 130 Q 130 110 100 95"
          fill="none" stroke="{GOLD}" stroke-width="0.8" stroke-linecap="round" opacity="0.6"/>

    <!-- olive leaves along main stem -->
    <g fill="none" stroke="{GOLD}" stroke-width="1">
      <!-- leaf pairs going up the stem -->
      <ellipse cx="245" cy="340" rx="14" ry="5" transform="rotate(35 245 340)" opacity="0.8"/>
      <ellipse cx="235" cy="310" rx="14" ry="5" transform="rotate(-30 235 310)" opacity="0.8"/>
      <ellipse cx="225" cy="285" rx="13" ry="4.5" transform="rotate(40 225 285)" opacity="0.7"/>
      <ellipse cx="210" cy="265" rx="13" ry="4.5" transform="rotate(-35 210 265)" opacity="0.7"/>

      <ellipse cx="200" cy="230" rx="12" ry="4" transform="rotate(30 200 230)" opacity="0.7"/>
      <ellipse cx="195" cy="210" rx="12" ry="4" transform="rotate(-25 195 210)" opacity="0.7"/>

      <ellipse cx="175" cy="175" rx="11" ry="4" transform="rotate(35 175 175)" opacity="0.6"/>
      <ellipse cx="168" cy="155" rx="11" ry="4" transform="rotate(-30 168 155)" opacity="0.6"/>

      <ellipse cx="155" cy="120" rx="10" ry="3.5" transform="rotate(30 155 120)" opacity="0.6"/>
      <ellipse cx="148" cy="102" rx="10" ry="3.5" transform="rotate(-25 148 102)" opacity="0.6"/>

      <ellipse cx="138" cy="75" rx="9" ry="3" transform="rotate(35 138 75)" opacity="0.5"/>
      <ellipse cx="130" cy="58" rx="8" ry="3" transform="rotate(-30 130 58)" opacity="0.5"/>

      <!-- leaves on secondary branches -->
      <ellipse cx="240" cy="225" rx="10" ry="3.5" transform="rotate(15 240 225)" opacity="0.5"/>
      <ellipse cx="250" cy="215" rx="9" ry="3" transform="rotate(-10 250 215)" opacity="0.5"/>
      <ellipse cx="120" cy="105" rx="9" ry="3" transform="rotate(-15 120 105)" opacity="0.5"/>
      <ellipse cx="110" cy="100" rx="8" ry="2.5" transform="rotate(10 110 100)" opacity="0.5"/>
    </g>

    <!-- small berries -->
    <circle cx="228" cy="300" r="2.5" fill="{GOLD}" opacity="0.6"/>
    <circle cx="222" cy="295" r="2" fill="{GOLD}" opacity="0.5"/>
    <circle cx="188" cy="195" r="2" fill="{GOLD}" opacity="0.5"/>
    <circle cx="182" cy="190" r="1.8" fill="{GOLD}" opacity="0.4"/>
  </g>
</svg>"""


def olive_branch_left():
    """Smaller botanical for top-left or bottom-left corner."""
    return f"""
<svg class="botanical" viewBox="0 0 250 300" xmlns="http://www.w3.org/2000/svg"
     preserveAspectRatio="xMidYMid meet"
     style="position:absolute; bottom:0; left:0; width:280px; opacity:0.6;
            transform: scaleX(-1);">
  <g>
    <path d="M 50 280 Q 70 220 90 170 Q 110 120 125 70 Q 135 40 140 20"
          fill="none" stroke="{GOLD}" stroke-width="1" stroke-linecap="round"/>
    <path d="M 90 170 Q 65 155 45 145"
          fill="none" stroke="{GOLD}" stroke-width="0.7" stroke-linecap="round" opacity="0.5"/>

    <g fill="none" stroke="{GOLD}" stroke-width="0.9">
      <ellipse cx="55" cy="250" rx="12" ry="4" transform="rotate(-35 55 250)" opacity="0.7"/>
      <ellipse cx="65" cy="225" rx="12" ry="4" transform="rotate(30 65 225)" opacity="0.7"/>
      <ellipse cx="75" cy="200" rx="11" ry="3.5" transform="rotate(-30 75 200)" opacity="0.6"/>
      <ellipse cx="85" cy="175" rx="11" ry="3.5" transform="rotate(25 85 175)" opacity="0.6"/>
      <ellipse cx="98" cy="145" rx="10" ry="3" transform="rotate(-30 98 145)" opacity="0.6"/>
      <ellipse cx="108" cy="120" rx="10" ry="3" transform="rotate(25 108 120)" opacity="0.5"/>
      <ellipse cx="118" cy="90" rx="9" ry="3" transform="rotate(-30 118 90)" opacity="0.5"/>
      <ellipse cx="125" cy="65" rx="8" ry="2.5" transform="rotate(20 125 65)" opacity="0.5"/>
      <ellipse cx="132" cy="40" rx="7" ry="2.5" transform="rotate(-25 132 40)" opacity="0.4"/>

      <ellipse cx="55" cy="155" rx="9" ry="3" transform="rotate(-15 55 155)" opacity="0.5"/>
      <ellipse cx="50" cy="150" rx="8" ry="2.5" transform="rotate(10 50 150)" opacity="0.4"/>
    </g>

    <circle cx="72" cy="215" r="2" fill="{GOLD}" opacity="0.5"/>
    <circle cx="78" cy="210" r="1.8" fill="{GOLD}" opacity="0.4"/>
  </g>
</svg>"""


def decorative_cross():
    """Small elegant cross ornament in gold."""
    return f"""
<svg viewBox="0 0 60 80" xmlns="http://www.w3.org/2000/svg"
     style="width:36px; height:48px; display:block; margin:0 auto;">
  <g fill="none" stroke="{GOLD}" stroke-width="1.5" stroke-linecap="round">
    <!-- vertical beam -->
    <line x1="30" y1="10" x2="30" y2="72"/>
    <!-- horizontal beam -->
    <line x1="12" y1="28" x2="48" y2="28"/>
    <!-- small decorative serifs -->
    <line x1="26" y1="10" x2="34" y2="10"/>
    <line x1="26" y1="72" x2="34" y2="72"/>
    <line x1="12" y1="24" x2="12" y2="32"/>
    <line x1="48" y1="24" x2="48" y2="32"/>
  </g>
  <!-- subtle center dot -->
  <circle cx="30" cy="28" r="2" fill="{GOLD}" opacity="0.6"/>
</svg>"""


def ornamental_divider(width="3in"):
    """Gold decorative divider line with center diamond."""
    return f"""
<div style="display:flex; align-items:center; justify-content:center;
     width:{width}; margin:0.3in auto;">
  <div style="flex:1; height:1px; background:linear-gradient(to right, transparent, {GOLD}, {GOLD});"></div>
  <div style="margin:0 10px; color:{GOLD}; font-size:8pt;">&#10022;</div>
  <div style="flex:1; height:1px; background:linear-gradient(to right, {GOLD}, {GOLD}, transparent);"></div>
</div>"""


# ====================================================================
# COVER CSS
# ====================================================================

COVER_CSS = f"""
<style>
  @page {{ size: 8.5in 11in; margin: 0; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: {SERIF_CLASSIC};
    -webkit-print-color-adjust: exact;
    background: #333;
  }}

  /* ===== COVER PAGE ===== */
  .cover {{
    width: 8.5in; height: 11in;
    position: relative; overflow: hidden;
    page-break-after: always;
    background:
      radial-gradient(ellipse at 50% 30%, {FOREST_LIGHT} 0%, {FOREST_MID} 40%, {FOREST_DARK} 100%);
  }}

  /* subtle texture overlay */
  .cover::before {{
    content: '';
    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background-image:
      repeating-linear-gradient(
        45deg,
        transparent, transparent 2px,
        rgba(0,0,0,0.015) 2px, rgba(0,0,0,0.015) 4px
      );
    pointer-events: none;
  }}

  /* vignette */
  .cover::after {{
    content: '';
    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.35) 100%);
    pointer-events: none;
  }}

  /* thin gold border frame */
  .cover-frame {{
    position: absolute;
    top: 0.38in; left: 0.38in; right: 0.38in; bottom: 0.38in;
    border: 1.5px solid {GOLD};
    pointer-events: none; z-index: 3;
  }}
  .cover-frame-inner {{
    position: absolute;
    top: 0.44in; left: 0.44in; right: 0.44in; bottom: 0.44in;
    border: 0.5px solid {GOLD_PALE};
    pointer-events: none; z-index: 3;
  }}

  /* botanical elements */
  .botanical {{ z-index: 2; pointer-events: none; }}

  /* main content */
  .cover-content {{
    position: relative; z-index: 5;
    height: 100%; display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 1.2in 1in;
    text-align: center;
  }}

  /* cross ornament at top */
  .cover-cross {{ margin-bottom: 0.45in; opacity: 0.9; }}

  /* overline label */
  .cover-overline {{
    font-family: {SANS_CLEAN};
    font-size: 9pt; font-weight: 600;
    color: {GOLD};
    letter-spacing: 7pt; text-transform: uppercase;
    margin-bottom: 0.3in; text-indent: 7pt;
  }}

  /* main title */
  .cover-title {{
    font-family: {SERIF_ELEGANT};
    font-size: 44pt; font-weight: 700;
    color: {CREAM};
    line-height: 1.2;
    letter-spacing: 1pt;
    text-shadow: 0 2px 8px rgba(0,0,0,0.4);
  }}
  .cover-title .line2 {{
    display: block; font-style: italic; font-weight: 400;
    color: {GOLD_BRIGHT};
    font-size: 48pt; margin-top: 4px;
  }}

  /* divider between title and subtitle */
  .cover-divider {{
    display: flex; align-items: center; justify-content: center;
    margin: 0.35in auto; width: 2.8in;
  }}
  .cover-divider-line {{
    flex: 1; height: 1px;
    background: linear-gradient(to right, transparent, {GOLD}, transparent);
  }}
  .cover-divider-icon {{
    color: {GOLD}; font-size: 10pt; margin: 0 12px;
  }}

  /* subtitle */
  .cover-subtitle {{
    font-family: {SANS_CLEAN};
    font-size: 11pt; font-weight: 500;
    color: {WHITE_SOFT};
    letter-spacing: 4pt; text-transform: uppercase;
    line-height: 1.8; text-indent: 4pt;
    max-width: 4.5in;
  }}

  /* study methods badges */
  .cover-badges {{
    display: flex; gap: 16px; margin-top: 0.5in;
    justify-content: center; flex-wrap: wrap;
  }}
  .cover-badge {{
    font-family: {SANS_CLEAN};
    font-size: 7.5pt; font-weight: 500;
    color: {GOLD};
    letter-spacing: 2pt; text-transform: uppercase;
    border: 1px solid {GOLD_PALE};
    padding: 5px 12px; border-radius: 2px;
    text-indent: 2pt;
  }}

  /* scripture verse at bottom */
  .cover-verse-block {{
    position: absolute; bottom: 0.85in;
    left: 0; right: 0; z-index: 5;
    text-align: center;
  }}
  .cover-verse {{
    font-family: {SERIF_ELEGANT};
    font-size: 11pt; font-style: italic;
    color: {WHITE_SOFT};
    line-height: 1.6; max-width: 4in; margin: 0 auto;
  }}
  .cover-verse-ref {{
    font-family: {SANS_CLEAN};
    font-size: 8.5pt; font-weight: 600;
    color: {GOLD};
    letter-spacing: 3pt; text-transform: uppercase;
    margin-top: 6px; text-indent: 3pt;
  }}

  /* screen-only styling */
  @media screen {{
    body {{ background: #333; padding: 20px; }}
    .cover {{ margin: 0 auto; box-shadow: 0 8px 40px rgba(0,0,0,0.5); }}
  }}
</style>
"""


# ====================================================================
# COVER HTML
# ====================================================================

def cover_html():
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bible Study Handbook — Cover</title>
  {COVER_CSS}
</head>
<body>
  <div class="cover">
    <!-- gold frame -->
    <div class="cover-frame"></div>
    <div class="cover-frame-inner"></div>

    <!-- botanical line art -->
    {olive_branch_corner("bottom-right")}
    {olive_branch_left()}

    <!-- main content -->
    <div class="cover-content">
      <!-- cross ornament -->
      <div class="cover-cross">{decorative_cross()}</div>

      <!-- overline -->
      <div class="cover-overline">A Study Journal</div>

      <!-- title -->
      <div class="cover-title">
        Bible Study
        <span class="line2">Handbook</span>
      </div>

      <!-- divider -->
      <div class="cover-divider">
        <div class="cover-divider-line"></div>
        <span class="cover-divider-icon">&#10022;</span>
        <div class="cover-divider-line"></div>
      </div>

      <!-- subtitle -->
      <div class="cover-subtitle">
        Reflection &middot; Prayer &middot; Spiritual Growth
      </div>

      <!-- method badges -->
      <div class="cover-badges">
        <span class="cover-badge">SOAP</span>
        <span class="cover-badge">Inductive</span>
        <span class="cover-badge">Verse Mapping</span>
        <span class="cover-badge">Prayer Journal</span>
      </div>
    </div>

    <!-- scripture verse at bottom -->
    <div class="cover-verse-block">
      <div class="cover-verse">
        &ldquo;Your word is a lamp to my feet<br/>and a light to my path.&rdquo;
      </div>
      <div class="cover-verse-ref">Psalm 119:105</div>
    </div>
  </div>
</body>
</html>"""


# ====================================================================
# MAIN
# ====================================================================

def generate(output_path=OUTPUT_FILE):
    html = cover_html()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    return output_path


if __name__ == "__main__":
    path = generate()
    print(f"[OK] Cover generated: {os.path.abspath(path)}")
    print(f"     Style: Modern Botanical Moody (Forest Green + Gold)")
    print(f"     Trim: 8.5 x 11 inches")
    print(f"")
    print(f"     Open cover_preview.html in browser to preview")
