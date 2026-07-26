#!/usr/bin/env python3
"""
Watercolor & Art Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Watercolor artists, sketchers, art students, hobbyists
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "watercolor_art_journal_us_V1.0.html")

BOOK_TITLE = "Watercolor & Art Journal"
BOOK_SUBTITLE = "A Sketchbook for Painting, Drawing, and Creative Expression"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

def nl(n):
    return "\n".join('<div class="notes-line"></div>' for _ in range(n))

# ============================================================
# CSS
# ============================================================
CSS = r"""
@page { size: 6in 9in; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: Georgia, "Iowan Old Style", "Palatino", serif;
  color: #2A2A2A;
  background: white;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

.page {
  width: 6in; height: 9in;
  padding: 0.5in 0.5in 0.4in 0.5in;
  page-break-after: always;
  position: relative;
  background: white;
  overflow: hidden;
}
.page:last-child { page-break-after: auto; }

@media screen { .page { border: 1px dashed #ccc; margin: 8px auto; } }
@media print  { .page { border: none; margin: 0; } }

/* ================ INTERIOR TITLE PAGE ================ */
.cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(165deg, #161616 0%, #1E1E1E 30%, #161616 65%, #0D0D0D 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.cover .glow-bg {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #C4A04A, transparent);
}

.cover .title-main {
  font-size: 30pt;
  font-weight: 700;
  color: #FAF6F0;
  line-height: 1.2;
  letter-spacing: 1pt;
  position: relative;
  z-index: 2;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 100px;
  height: 2px;
  background: #C4A04A;
  margin: 20px auto;
  position: relative;
  z-index: 2;
}

.cover .subtitle {
  font-size: 12pt;
  color: #D4B896;
  font-style: italic;
  line-height: 1.5;
  position: relative;
  z-index: 2;
}

.cover .pub {
  position: absolute;
  bottom: 0.6in;
  left: 0; right: 0;
  text-align: center;
  font-size: 9pt;
  color: #C4A04A;
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  font-weight: 700;
}

/* ================ SECTION HEADERS ================ */
.section-header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 14px;
}

.section-title {
  font-size: 14pt;
  font-weight: 700;
  color: #161616;
  letter-spacing: 0.5pt;
  text-transform: uppercase;
}

.section-line {
  flex: 1;
  height: 1px;
  background: #C4A04A;
  margin: 0 12px;
  opacity: 0.5;
}

/* ================ PAGE HEADER ================ */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  padding-bottom: 4px;
  border-bottom: 0.5px solid #eee;
}

.page-header .ph-left {
  font-size: 8pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 1pt;
  font-weight: 700;
}

.page-header .ph-right {
  font-size: 8pt;
  color: #999;
}

/* ================ HOW TO USE ================ */
.howto-text {
  font-size: 10pt;
  line-height: 1.7;
  color: #2A2A2A;
}

.howto-text p {
  margin-bottom: 10px;
}

.howto-text .ht-title {
  font-size: 11pt;
  font-weight: 700;
  color: #161616;
  margin-bottom: 4px;
  margin-top: 6px;
}

.howto-text .ht-icon {
  color: #C4A04A;
  font-weight: 700;
  margin-right: 4px;
}

/* ================ REFERENCE TABLES ================ */
.ref-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9pt;
  margin-bottom: 10px;
}

.ref-table th {
  background: #FAF6F0;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-size: 8pt;
  padding: 5px 8px;
  border-bottom: 1.5px solid #C4A04A;
  text-align: left;
}

.ref-table td {
  padding: 4px 8px;
  border-bottom: 0.5px solid #eee;
  color: #2A2A2A;
}

.ref-table tr:nth-child(even) td {
  background: #FCFAF7;
}

.ref-section {
  margin-bottom: 14px;
}

.ref-heading {
  font-size: 9pt;
  font-weight: 700;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 1pt;
  margin-bottom: 4px;
}

/* ================ COLOR WHEEL REFERENCE ================ */
.color-wheel-info {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-bottom: 12px;
}

.cw-box {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 6px 8px;
}

.cw-box .cwb-label {
  font-size: 7pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 3px;
}

.cw-box .cwb-swatches {
  display: flex;
  gap: 4px;
  margin-top: 4px;
}

.swatch {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 1px solid #ddd;
}

/* ================ SKETCH/CANVAS PAGES ================ */
/* Light dot grid for sketching pages */
.dot-grid {
  width: 100%;
  height: 100%;
  position: relative;
  background-image: radial-gradient(circle, #ddd 0.8px, transparent 1px);
  background-size: 16px 16px;
}

/* Light grid for drawing pages */
.draw-grid {
  width: 100%;
  height: 100%;
  position: relative;
  background-image:
    linear-gradient(to right, #eee 0.5px, transparent 0.5px),
    linear-gradient(to bottom, #eee 0.5px, transparent 0.5px);
  background-size: 20px 20px;
}

/* Blank canvas (no grid) */
.blank-canvas {
  width: 100%;
  height: 100%;
}

/* Framed canvas with border */
.framed-canvas {
  width: 100%;
  height: 100%;
  border: 1px solid #ccc;
  position: relative;
}

/* ================ ARTWORK LOG ENTRY ================ */
.art-entry {
  margin-bottom: 0;
}

.art-header-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 8px;
  border-bottom: 2px solid #161616;
  padding-bottom: 4px;
}

.art-title-line {
  flex: 1;
}

.art-title-label {
  font-size: 7pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  display: block;
  margin-bottom: 1px;
}

.art-title-write {
  height: 22px;
}

.art-date-box {
  margin-left: 12px;
  text-align: right;
}

.art-date-box .adb-label {
  font-size: 6pt;
  color: #aaa;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.art-date-box .adb-line {
  width: 80px;
  border-bottom: 1px dotted #ccc;
  height: 16px;
}

.art-meta {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 5px;
  margin-bottom: 6px;
}

.art-meta .am-box {
  text-align: center;
}

.art-meta .am-label {
  font-size: 6pt;
  color: #aaa;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  display: block;
  margin-bottom: 1px;
}

.art-meta .am-write {
  height: 14px;
  border-bottom: 1px dotted #ccc;
}

.art-canvas-area {
  border: 1px solid #ddd;
  height: 4.6in;
  position: relative;
  background-image: radial-gradient(circle, #eee 0.6px, transparent 0.8px);
  background-size: 18px 18px;
  margin-bottom: 6px;
}

.art-canvas-blank {
  border: 1px solid #ddd;
  height: 4.6in;
  margin-bottom: 6px;
}

.art-notes {
  border-left: 3px solid #C4A04A;
  padding: 4px 8px;
  background: #FAF6F0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}

.art-notes .an-label {
  font-size: 6pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 2px;
  display: block;
}

.art-notes .an-line {
  border-bottom: 0.5px dotted #ccc;
  height: 16px;
}

/* ================ INDEX ================ */
.index-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9pt;
}

.index-table th {
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-size: 7.5pt;
  padding: 4px 6px;
  border-bottom: 1.5px solid #C4A04A;
  text-align: left;
}

.index-table td {
  padding: 3px 6px;
  border-bottom: 0.5px dotted #ddd;
  height: 24px;
  vertical-align: bottom;
}

.idx-letter {
  width: 20px;
  font-weight: 700;
  color: #C4A04A;
  font-size: 10pt;
}

.idx-name {
  width: auto;
}

.idx-medium {
  width: 80px;
  font-size: 7.5pt;
  color: #999;
}

.idx-page {
  width: 35px;
  text-align: right;
  color: #999;
  font-size: 8pt;
}

/* ================ NOTES ================ */
.notes-line {
  border-bottom: 1px solid #ddd;
  height: 22px;
}

/* ================ FINAL PAGE ================ */
.final-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100%;
}

.final-page .fp-text {
  font-size: 12pt;
  color: #999;
  font-style: italic;
  line-height: 1.8;
  margin-bottom: 20px;
}

.final-page .fp-logo {
  font-size: 11pt;
  color: #C4A04A;
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  font-weight: 700;
}

.final-page .fp-line {
  width: 60px;
  height: 1.5px;
  background: #C4A04A;
  margin: 12px auto;
  opacity: 0.5;
}
"""

# ============================================================
# PAGE GENERATORS
# ============================================================

def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="90" height="90" xmlns="http://www.w3.org/2000/svg">
      <!-- Palette -->
      <ellipse cx="50" cy="62" rx="35" ry="20" stroke="#C4A04A" stroke-width="1.5" fill="none"/>
      <!-- Paint blobs -->
      <circle cx="35" cy="55" r="5" stroke="#C4A04A" stroke-width="1" fill="none"/>
      <circle cx="48" cy="50" r="5" stroke="#C4A04A" stroke-width="1" fill="none"/>
      <circle cx="62" cy="52" r="5" stroke="#C4A04A" stroke-width="1" fill="none"/>
      <circle cx="55" cy="65" r="5" stroke="#C4A04A" stroke-width="1" fill="none"/>
      <!-- Thumb hole -->
      <ellipse cx="68" cy="62" rx="4" ry="3" stroke="#C4A04A" stroke-width="1" fill="none"/>
      <!-- Brush -->
      <line x1="78" y1="30" x2="88" y2="20" stroke="#C4A04A" stroke-width="1.5"/>
      <ellipse cx="77" cy="31" rx="3" ry="5" stroke="#C4A04A" stroke-width="1" fill="none" transform="rotate(-45 77 31)"/>
    </svg>
  </div>

  <div class="title-main">Watercolor<br>&amp; Art Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">A Sketchbook for Painting,<br>Drawing, and Creative Expression</div>

  <div class="pub">More Shine Press</div>
</div>""" % pn()


def how_to_use_page():
    pg = pn()
    return """<!-- PAGE %d: How to Use -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">How to Use This Journal</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Creative Space</div>
    <p>This journal is designed to be your personal art companion &mdash;
    a place to experiment, practice, and capture inspiration wherever
    you go. Every page is an invitation to create without judgment.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Three Page Types</div>
    <p><strong>Dotted canvas pages</strong> feature a light dot grid
    that guides proportions and composition without interfering with
    your artwork. Perfect for watercolor sketches and studies.</p>
    <p><strong>Grid practice pages</strong> offer a light rectangular
    grid ideal for perspective drawing, geometric patterns, and
    learning exercises.</p>
    <p><strong>Blank canvas pages</strong> give you completely open
    space for finished pieces, mixed media, or free expression.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Artwork Log Pages</div>
    <p>Log pages let you record the title, date, medium, colors used,
    techniques, and notes for each piece &mdash; so you can track your
    progress and revisit ideas later.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips</div>
    <p>&#9679; Use the dot grid for light pencil sketches before painting.</p>
    <p>&#9679; Test colors on the edge of the page before committing.</p>
    <p>&#9679; Don't be afraid to make mistakes &mdash; they are part
    of the creative journey.</p>
    <p>&#9679; Date every piece so you can see your progress over time.</p>
  </div>
</div>""" % (pg, pg)


def color_theory_page():
    pg = pn()
    return """<!-- PAGE %d: Color Theory Reference -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Color Theory Reference</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="ref-section">
    <div class="ref-heading">Primary, Secondary &amp; Tertiary Colors</div>
    <table class="ref-table">
      <tr><th>Category</th><th>Colors</th><th>Mix</th></tr>
      <tr><td>Primary</td><td>Red, Yellow, Blue</td><td>Cannot be mixed</td></tr>
      <tr><td>Secondary</td><td>Orange, Green, Purple</td><td>Two primaries combined</td></tr>
      <tr><td>Tertiary</td><td>Red-Orange, Yellow-Orange, etc.</td><td>Primary + adjacent secondary</td></tr>
    </table>
  </div>

  <div class="ref-section">
    <div class="ref-heading">Color Harmonies</div>
    <table class="ref-table">
      <tr><th>Harmony</th><th>Description</th><th>Example</th></tr>
      <tr><td>Complementary</td><td>Opposite on color wheel</td><td>Blue &amp; Orange</td></tr>
      <tr><td>Analogous</td><td>Adjacent on wheel</td><td>Blue, Blue-Green, Green</td></tr>
      <tr><td>Triadic</td><td>Three evenly spaced</td><td>Red, Yellow, Blue</td></tr>
      <tr><td>Monochromatic</td><td>One hue, varied values</td><td>Pale blue to dark blue</td></tr>
      <tr><td>Split-Complementary</td><td>Base + two adjacent to opposite</td><td>Blue + Yellow-Orange + Red-Orange</td></tr>
    </table>
  </div>

  <div class="ref-section">
    <div class="ref-heading">Warm vs. Cool Colors</div>
    <table class="ref-table">
      <tr><th>Warm</th><th>Cool</th></tr>
      <tr><td>Reds, Oranges, Yellows</td><td>Blues, Greens, Purples</td></tr>
      <tr><td>Advance in composition</td><td>Recede in composition</td></tr>
      <tr><td>Energetic, passionate</td><td>Calm, serene</td></tr>
      <tr><td>Good for focal points</td><td>Good for backgrounds</td></tr>
    </table>
  </div>

  <div class="ref-section">
    <div class="ref-heading">Watercolor Value Scale Practice</div>
    <p style="font-size: 9pt; line-height: 1.5; color: #666; margin-bottom: 6px;">
    Paint a value scale from light (lots of water) to dark (lots of pigment)
    to understand how much water and pigment to use for each tone.
    </p>
    <div style="display: flex; gap: 0;">
      <div style="flex: 1; height: 30px; border: 1px solid #ddd; display: flex; align-items: center; justify-content: center; font-size: 7pt; color: #999;">1 Light</div>
      <div style="flex: 1; height: 30px; border: 1px solid #ddd; border-left: none; display: flex; align-items: center; justify-content: center; font-size: 7pt; color: #999;">2</div>
      <div style="flex: 1; height: 30px; border: 1px solid #ddd; border-left: none; display: flex; align-items: center; justify-content: center; font-size: 7pt; color: #999;">3 Mid</div>
      <div style="flex: 1; height: 30px; border: 1px solid #ddd; border-left: none; display: flex; align-items: center; justify-content: center; font-size: 7pt; color: #999;">4</div>
      <div style="flex: 1; height: 30px; border: 1px solid #ddd; border-left: none; display: flex; align-items: center; justify-content: center; font-size: 7pt; color: #999;">5 Dark</div>
    </div>
  </div>
</div>""" % (pg, pg)


def techniques_page():
    pg = pn()
    return """<!-- PAGE %d: Techniques Reference -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Watercolor Techniques</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="ref-section">
    <div class="ref-heading">Essential Techniques</div>
    <table class="ref-table">
      <tr><th>Technique</th><th>How To</th><th>Best For</th></tr>
      <tr><td>Wet on Wet</td><td>Wet paper first, then add pigment</td><td>Soft skies, backgrounds</td></tr>
      <tr><td>Wet on Dry</td><td>Wet brush on dry paper</td><td>Sharp edges, details</td></tr>
      <tr><td>Dry Brush</td><td>Damp brush, minimal water</td><td>Texture, foliage</td></tr>
      <tr><td>Glazing</td><td>Layer dry washes over dried paint</td><td>Depth, color richness</td></tr>
      <tr><td>Salt Texture</td><td>Sprinkle salt on wet wash</td><td>Organic star patterns</td></tr>
      <tr><td>Lifting</td><td>Remove wet paint with tissue/sponge</td><td>Clouds, highlights</td></tr>
      <tr><td>Splatter</td><td>Flick brush to create dots</td><td>Snow, stars, texture</td></tr>
      <tr><td>Flat Wash</td><td>Even stroke left to right, top to bottom</td><td>Solid backgrounds</td></tr>
      <tr><td>Graded Wash</td><td>Gradually dilute pigment each row</td><td>Sky gradients</td></tr>
    </table>
  </div>

  <div class="ref-section">
    <div class="ref-heading">Brush Types Guide</div>
    <table class="ref-table">
      <tr><th>Brush</th><th>Best For</th></tr>
      <tr><td>Round (size 4-12)</td><td>Details, lines, varied strokes</td></tr>
      <tr><td>Flat (1/4&quot; - 1&quot;)</td><td>Washes, straight edges</td></tr>
      <tr><td>Mop</td><td>Large washes, wetting paper</td></tr>
      <tr><td>Detail/Rigger</td><td>Fine lines, branches, signatures</td></tr>
      <tr><td>Fan</td><td>Texture, grass, foliage</td></tr>
    </table>
  </div>

  <div class="ref-section">
    <div class="ref-heading">Paper Weights &amp; Textures</div>
    <table class="ref-table">
      <tr><th>Type</th><th>Weight</th><th>Characteristics</th></tr>
      <tr><td>Cold Press</td><td>140lb / 300gsm+</td><td>Slightly textured, most versatile</td></tr>
      <tr><td>Hot Press</td><td>300gsm+</td><td>Smooth surface, fine detail</td></tr>
      <tr><td>Rough</td><td>300gsm+</td><td>Heavy texture, expressive washes</td></tr>
    </table>
  </div>
</div>""" % (pg, pg)


def artwork_index_page(letter_start, letter_end):
    pg = pn()
    letters = [chr(c) for c in range(ord(letter_start), ord(letter_end) + 1)]
    rows_html = ""
    for letter in letters:
        for _ in range(2):
            rows_html += """<tr>
  <td class="idx-letter">%s</td>
  <td class="idx-name"></td>
  <td class="idx-medium"></td>
  <td class="idx-page"></td>
</tr>
""" % letter

    return """<!-- PAGE %d: Artwork Index -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Artwork Index</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="index-table">
    <tr>
      <th style="width:20px;"></th>
      <th>Artwork Title</th>
      <th style="width:80px;">Medium</th>
      <th style="text-align:right; width:35px;">Page</th>
    </tr>
    %s
  </table>
</div>""" % (pg, pg, rows_html)


def sketch_dotted_page():
    """Full-page dot grid canvas for sketching."""
    pg = pn()
    return """<!-- PAGE %d: Sketch (Dotted) -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Sketch &middot; Dotted Grid</span>
    <span class="ph-right">Page %d</span>
  </div>
  <div class="dot-grid" style="height: 7.4in;"></div>
</div>""" % (pg, pg)


def sketch_grid_page():
    """Full-page light grid for drawing practice."""
    pg = pn()
    return """<!-- PAGE %d: Sketch (Grid) -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Practice &middot; Grid</span>
    <span class="ph-right">Page %d</span>
  </div>
  <div class="draw-grid" style="height: 7.4in;"></div>
</div>""" % (pg, pg)


def sketch_blank_page():
    """Full-page blank canvas."""
    pg = pn()
    return """<!-- PAGE %d: Sketch (Blank) -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Canvas &middot; Blank</span>
    <span class="ph-right">Page %d</span>
  </div>
  <div class="blank-canvas" style="height: 7.4in;"></div>
</div>""" % (pg, pg)


def art_log_page():
    """Artwork log entry with metadata fields + canvas area."""
    pg = pn()
    return """<!-- PAGE %d: Artwork Log -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Artwork Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="art-entry">
    <div class="art-header-row">
      <div class="art-title-line">
        <span class="art-title-label">Title</span>
        <div class="art-title-write"></div>
      </div>
      <div class="art-date-box">
        <span class="adb-label">Date</span>
        <div class="adb-line"></div>
      </div>
    </div>

    <div class="art-meta">
      <div class="am-box">
        <span class="am-label">Medium</span>
        <div class="am-write"></div>
      </div>
      <div class="am-box">
        <span class="am-label">Paper</span>
        <div class="am-write"></div>
      </div>
      <div class="am-box">
        <span class="am-label">Brushes</span>
        <div class="am-write"></div>
      </div>
      <div class="am-box">
        <span class="am-label">Size</span>
        <div class="am-write"></div>
      </div>
    </div>

    <div class="art-canvas-area"></div>

    <div class="art-notes">
      <div>
        <span class="an-label">Colors Used</span>
        <div class="an-line"></div>
      </div>
      <div>
        <span class="an-label">Techniques &amp; Notes</span>
        <div class="an-line"></div>
      </div>
    </div>
  </div>
</div>""" % (pg, pg)


def notes_page():
    pg = pn()
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes &amp; Inspiration</span>
    <span class="ph-right">Page %d</span>
  </div>
  <div>
    %s
  </div>
</div>""" % (pg, pg, nl(28))


def final_page():
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="page">
  <div class="final-page">
    <div class="fp-text">
      Every stroke<br>
      is a step forward.<br>
      Keep painting.
    </div>
    <div class="fp-line"></div>
    <div class="fp-logo">More Shine Press</div>
    <div class="fp-line"></div>
  </div>
</div>""" % pg


# ============================================================
# MAIN
# ============================================================
def generate(output_path=HTML_FILE):
    pages = []

    # 1. Title page
    pages.append(interior_title_page())

    # 2. How to use
    pages.append(how_to_use_page())

    # 3. Color theory reference
    pages.append(color_theory_page())

    # 4. Techniques reference
    pages.append(techniques_page())

    # 5-8. Artwork index (4 pages, A-Z)
    index_ranges = [("A", "G"), ("H", "N"), ("O", "T"), ("U", "Z")]
    for ls, le in index_ranges:
        pages.append(artwork_index_page(ls, le))

    # 9-104. Sketch & canvas pages (96 pages)
    # Pattern: 3 dotted + 1 grid + 1 blank, repeated = 5 per cycle, x19 = 95
    # Plus 1 more blank = 96 total
    for cycle in range(19):
        pages.append(sketch_dotted_page())
        pages.append(sketch_dotted_page())
        pages.append(sketch_dotted_page())
        pages.append(sketch_grid_page())
        pages.append(sketch_blank_page())
    # 1 more dotted to reach 96
    pages.append(sketch_dotted_page())

    # 105-109. Artwork log pages (5 entries)
    for _ in range(5):
        pages.append(art_log_page())

    # Notes (3 pages)
    for _ in range(3):
        pages.append(notes_page())

    # Final
    pages.append(final_page())

    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>%s</title>
  <style>%s</style>
</head>
<body>
%s
</body>
</html>""" % (H.escape(BOOK_TITLE), CSS, "\n".join(pages))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    return output_path, page_no[0]


if __name__ == "__main__":
    path, count = generate()
    print("[OK] Interior generated: %s" % path)
    print("     Total pages: %d" % count)
