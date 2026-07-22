#!/usr/bin/env python3
"""
KDP Bible Study Handbook Generator
===================================
Complete, print-ready Bible study handbook for Amazon KDP.
Zero-dependency (pure Python stdlib). Outputs HTML → browser print to PDF.

Trim Size: 8.5" x 11" (large workspace, premium handbook feel)
Theme: Deep Navy + Warm Gold (elegant, cross-denominational, unisex)
Content: SOAP, Inductive, Verse Mapping, Sermon Notes, Prayer Journal,
         Topical Study, Reading Plan, + Lined/Grid notes
Copyright-safe: Verse addresses only, no translated text.

Usage:
  python3 generate_handbook.py
  # Open bible_study_handbook.html in browser → Cmd+P → Save as PDF
"""

import os

OUTPUT_FILE = "bible_study_handbook.html"

# ====================================================================
# THEME
# ====================================================================
NAVY        = "#1a365d"   # deep navy — primary
NAVY_LIGHT  = "#2c5282"   # lighter navy for accents
GOLD        = "#c5a55a"   # warm gold — accent / dividers
GOLD_LIGHT  = "#f5edd6"   # pale gold — label backgrounds
CREAM       = "#fbf9f4"   # warm off-white
GRAY_TEXT   = "#3d3d3d"
GRAY_LIGHT  = "#999999"
GRAY_BORDER = "#d0d0d0"

SERIF = "'Georgia', 'Palatino Linotype', 'Book Antiqua', serif"
SANS  = "'Helvetica Neue', 'Arial', sans-serif"

# ====================================================================
# CSS
# ====================================================================
CSS = f"""
<style>
  @page {{ size: 8.5in 11in; margin: 0; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: {SERIF}; color: {GRAY_TEXT};
    background: #e8e8e8; -webkit-print-color-adjust: exact;
  }}

  .page {{
    width: 8.5in; height: 11in;
    padding: 0.65in 0.7in 0.6in 0.7in;
    page-break-after: always; position: relative;
    background: white;
    overflow: hidden;
  }}
  .page:last-child {{ page-break-after: auto; }}

  /* Screen-only dashed border; removed in print */
  @media screen {{ .page {{ border: 1px dashed #bbb; margin: 8px auto; }} }}
  @media print  {{ .page {{ border: none; margin: 0; }} }}

  /* ----- COVER PAGE (Modern Botanical Moody) ----- */
  .cover {{
    width: 8.5in; height: 11in; padding: 0;
    background: radial-gradient(ellipse at 50% 30%, #2d5a47 0%, #244438 40%, #1a3329 100%);
    color: white;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    page-break-after: always; position: relative;
    overflow: hidden;
  }}
  .cover-texture {{
    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background-image: repeating-linear-gradient(
      45deg, transparent, transparent 2px,
      rgba(0,0,0,0.015) 2px, rgba(0,0,0,0.015) 4px);
    pointer-events: none;
  }}
  .cover-frame {{
    position: absolute; top: 0.38in; left: 0.38in;
    right: 0.38in; bottom: 0.38in;
    border: 1.5px solid #c9a84c;
    pointer-events: none; z-index: 3;
  }}
  .cover-frame-inner {{
    position: absolute; top: 0.44in; left: 0.44in;
    right: 0.44in; bottom: 0.44in;
    border: 0.5px solid rgba(201,168,76,0.3);
    pointer-events: none; z-index: 3;
  }}
  .cover-botanical-r {{
    position: absolute; bottom: 0; right: 0;
    width: 340px; height: 450px; opacity: 0.75;
    z-index: 2; pointer-events: none;
  }}
  .cover-botanical-l {{
    position: absolute; bottom: 0; left: 0;
    width: 280px; height: 340px; opacity: 0.6;
    z-index: 2; pointer-events: none;
  }}
  .cover-content-new {{
    position: relative; z-index: 5;
    height: 100%; display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 1.2in 1in; text-align: center;
  }}
  .cover-cross-new {{
    width: 36px; height: 48px;
    margin-bottom: 0.45in; opacity: 0.9;
  }}
  .cover-overline-new {{
    font-family: 'Montserrat','Helvetica Neue',Arial,sans-serif;
    font-size: 9pt; font-weight: 600;
    color: #c9a84c;
    letter-spacing: 7pt; text-transform: uppercase;
    margin-bottom: 0.3in; text-indent: 7pt;
  }}
  .cover-title-new {{
    font-family: 'Playfair Display','Cormorant Garamond','Georgia',serif;
    font-size: 44pt; font-weight: 700;
    color: #f5f0e1;
    line-height: 1.2; letter-spacing: 1pt;
    text-shadow: 0 2px 8px rgba(0,0,0,0.4);
  }}
  .cover-title-italic-new {{
    font-family: 'Playfair Display','Cormorant Garamond','Georgia',serif;
    font-size: 48pt; font-weight: 400; font-style: italic;
    color: #dcc078;
    line-height: 1.2; margin-top: 4px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.4);
  }}
  .cover-divider-new {{
    display: flex; align-items: center; justify-content: center;
    margin: 0.35in auto; width: 2.8in;
  }}
  .cover-divider-line-new {{
    flex: 1; height: 1px;
    background: linear-gradient(to right, transparent, #c9a84c, transparent);
  }}
  .cover-divider-icon-new {{
    color: #c9a84c; font-size: 10pt; margin: 0 12px;
  }}
  .cover-subtitle-new {{
    font-family: 'Montserrat','Helvetica Neue',Arial,sans-serif;
    font-size: 11pt; font-weight: 500;
    color: rgba(255,255,255,0.85);
    letter-spacing: 4pt; text-transform: uppercase;
    line-height: 1.8; text-indent: 4pt;
    max-width: 4.5in;
  }}
  .cover-badges-new {{
    display: flex; gap: 16px; margin-top: 0.5in;
    justify-content: center; flex-wrap: wrap;
  }}
  .cover-badge-new {{
    font-family: 'Montserrat','Helvetica Neue',Arial,sans-serif;
    font-size: 7.5pt; font-weight: 500;
    color: #c9a84c;
    letter-spacing: 2pt; text-transform: uppercase;
    border: 1px solid rgba(201,168,76,0.3);
    padding: 5px 12px; border-radius: 2px;
    text-indent: 2pt;
  }}
  .cover-verse-block-new {{
    position: absolute; bottom: 0.85in;
    left: 0; right: 0; z-index: 5; text-align: center;
  }}
  .cover-verse-new {{
    font-family: 'Playfair Display','Georgia',serif;
    font-size: 11pt; font-style: italic;
    color: rgba(255,255,255,0.85);
    line-height: 1.6; max-width: 4in; margin: 0 auto;
  }}
  .cover-verse-ref-new {{
    font-family: 'Montserrat','Helvetica Neue',Arial,sans-serif;
    font-size: 8.5pt; font-weight: 600;
    color: #c9a84c;
    letter-spacing: 3pt; text-transform: uppercase;
    margin-top: 6px; text-indent: 3pt;
  }}

  /* ----- SECTION DIVIDER (full-page) ----- */
  .divider-page {{
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    text-align: center;
  }}
  .divider-num {{
    font-size: 72pt; color: {GOLD}; opacity: 0.25;
    font-weight: bold; line-height: 1;
  }}
  .divider-label {{
    font-size: 10pt; color: {NAVY}; letter-spacing: 5pt;
    text-transform: uppercase; margin-top: 0.15in;
  }}
  .divider-title {{
    font-size: 32pt; color: {NAVY}; font-weight: bold;
    margin: 0.2in 0 0.15in 0;
  }}
  .divider-line {{
    width: 1.5in; height: 2px; background: {GOLD};
    margin: 0.1in auto;
  }}
  .divider-desc {{
    font-size: 12pt; color: {GRAY_LIGHT};
    font-style: italic; max-width: 4in; line-height: 1.6;
    margin-top: 0.15in;
  }}

  /* ----- HEADERS / LABELS ----- */
  .page-tag {{
    font-size: 8pt; letter-spacing: 3pt;
    color: {GOLD}; text-transform: uppercase;
    text-align: center; margin-bottom: 2px;
  }}
  .page-title {{
    font-size: 18pt; font-weight: bold; text-align: center;
    color: {NAVY}; letter-spacing: 2pt; text-transform: uppercase;
    margin-bottom: 2px;
  }}
  .page-rule {{
    width: 1.2in; height: 2px; background: {GOLD};
    margin: 4px auto 16px auto;
  }}
  .meta-row {{
    display: flex; justify-content: space-between;
    font-size: 9.5pt; color: {GRAY_LIGHT};
    margin-bottom: 14px; border-bottom: 1px solid {GRAY_BORDER};
    padding-bottom: 8px;
  }}
  .meta-row span {{ flex: 1; }}
  .meta-row .right {{ text-align: right; }}

  /* ----- WRITING FIELDS ----- */
  .field-label {{
    font-size: 9.5pt; font-weight: bold; color: {NAVY};
    text-transform: uppercase; letter-spacing: 1.5pt;
    margin-top: 10px; margin-bottom: 4px;
  }}
  .field-sub {{
    font-size: 8.5pt; color: {GRAY_LIGHT}; font-style: italic;
    margin-bottom: 3px;
  }}
  .lines-5  {{ /* 5 writing lines */ }}
  .lines-8  {{ /* 8 writing lines */ }}
  .write-line {{
    border-bottom: 1px solid #e0e0e0; height: 26px;
  }}
  .write-line-tight {{
    border-bottom: 1px solid #e0e0e0; height: 22px;
  }}

  /* dotted-line for short answers */
  .dotted-line {{
    border-bottom: 1px dotted #bbb; height: 22px;
  }}

  /* ----- SOAP BOXES ----- */
  .soap-section {{
    border: 1px solid {GRAY_BORDER};
    border-radius: 4px; padding: 12px 14px;
    margin-bottom: 10px; min-height: 1.4in;
    background: {CREAM};
  }}
  .soap-section.scripture {{ min-height: 1.1in; }}
  .soap-letter {{
    display: inline-block; width: 28px; height: 28px;
    border-radius: 50%; background: {NAVY}; color: white;
    text-align: center; line-height: 28px;
    font-size: 14pt; font-weight: bold; font-family: {SANS};
    margin-right: 8px; vertical-align: middle;
  }}
  .soap-label {{
    font-size: 12pt; font-weight: bold; color: {NAVY};
    text-transform: uppercase; letter-spacing: 2pt;
    vertical-align: middle;
  }}
  .soap-hint {{
    font-size: 8pt; color: {GRAY_LIGHT}; font-style: italic;
    float: right; line-height: 28px;
  }}
  .soap-lines {{ margin-top: 6px; }}

  /* ----- VERSE MAPPING ----- */
  .vm-step {{
    border-left: 3px solid {GOLD};
    padding: 6px 0 6px 12px; margin-bottom: 8px;
  }}
  .vm-step-title {{
    font-size: 10pt; font-weight: bold; color: {NAVY};
    text-transform: uppercase; letter-spacing: 1pt;
    margin-bottom: 2px;
  }}

  /* ----- PRAYER JOURNAL ----- */
  .prayer-box {{
    border: 1px solid {GRAY_BORDER}; border-radius: 4px;
    padding: 10px 12px; margin-bottom: 8px;
    min-height: 0.7in; background: {CREAM};
  }}
  .prayer-label {{
    font-size: 9pt; font-weight: bold; color: {NAVY};
    text-transform: uppercase; letter-spacing: 1.5pt;
    margin-bottom: 4px;
  }}

  /* ----- READING PLAN ----- */
  .plan-table {{
    width: 100%; border-collapse: collapse; font-size: 9.5pt;
  }}
  .plan-table th {{
    background: {NAVY}; color: white; padding: 6px 4px;
    text-align: center; font-size: 9pt;
    text-transform: uppercase; letter-spacing: 1pt;
  }}
  .plan-table td {{
    border: 1px solid #e0e0e0; padding: 3px 5px;
    height: 20px; font-size: 9pt;
  }}
  .plan-table .book {{ font-weight: bold; color: {NAVY}; }}
  .plan-table .checkbox {{
    width: 28px; text-align: center; font-size: 12pt;
  }}

  /* ----- SERMON NOTES ----- */
  .sermon-info {{
    display: flex; gap: 0; margin-bottom: 10px;
    border: 1px solid {GRAY_BORDER}; border-radius: 4px;
    overflow: hidden;
  }}
  .sermon-info-cell {{
    flex: 1; padding: 8px 10px; border-right: 1px solid {GRAY_BORDER};
  }}
  .sermon-info-cell:last-child {{ border-right: none; }}
  .sermon-info-label {{
    font-size: 7.5pt; color: {GRAY_LIGHT};
    text-transform: uppercase; letter-spacing: 1pt;
  }}

  /* ----- TOC ----- */
  .toc-item {{
    display: flex; align-items: baseline;
    border-bottom: 1px dotted #ccc; padding: 8px 0;
    font-size: 12pt;
  }}
  .toc-num {{
    color: {GOLD}; font-weight: bold; width: 30px;
  }}
  .toc-name {{ color: {NAVY}; flex: 1; }}
  .toc-dots {{
    flex: 1; border-bottom: 1px dotted #ccc;
    margin: 0 6px; height: 14px;
  }}
  .toc-page {{ color: {GRAY_LIGHT}; font-size: 10pt; }}

  /* ----- LINED PAGES ----- */
  .lined-fill {{
    margin-top: 10px;
  }}

  /* ----- GRID PAGES ----- */
  .grid-area {{
    width: 100%; min-height: 8.5in;
    background-image:
      linear-gradient(to right, #eaeaea 1px, transparent 1px),
      linear-gradient(to bottom, #eaeaea 1px, transparent 1px);
    background-size: 0.28in 0.28in;
    border: 1px solid {GRAY_BORDER};
  }}

  /* ----- GRATITUDE ----- */
  .gratitude-row {{
    display: flex; align-items: flex-start;
    padding: 8px 0; border-bottom: 1px solid #eee;
  }}
  .gratitude-num {{
    width: 24px; height: 24px; border-radius: 50%;
    border: 1.5px solid {GOLD}; color: {GOLD};
    text-align: center; line-height: 22px;
    font-size: 10pt; font-weight: bold; margin-right: 10px;
    flex-shrink: 0;
  }}

  /* ----- CHARACTER STUDY ----- */
  .char-grid {{
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 10px; margin-top: 6px;
  }}
  .char-cell {{
    border: 1px solid {GRAY_BORDER}; padding: 8px;
    border-radius: 4px; min-height: 1.2in; background: {CREAM};
  }}
  .char-cell-label {{
    font-size: 8.5pt; font-weight: bold; color: {NAVY};
    text-transform: uppercase; letter-spacing: 1pt;
    margin-bottom: 4px;
  }}

  /* ----- FOOTER ----- */
  .page-footer {{
    position: absolute; bottom: 0.3in; left: 0.7in; right: 0.7in;
    display: flex; justify-content: space-between;
    font-size: 7.5pt; color: {GRAY_LIGHT};
    border-top: 1px solid #eee; padding-top: 4px;
  }}
  .footer-brand {{ color: {GOLD}; letter-spacing: 2pt; }}
</style>
"""

# ====================================================================
# HELPER FUNCTIONS
# ====================================================================

def lines(n, cls="write-line"):
    """Generate n writing lines."""
    return "".join([f'<div class="{cls}"></div>' for _ in range(n)])


def footer(page_num, section=""):
    """Page footer with brand + page number."""
    return f'''<div class="page-footer">
      <span class="footer-brand">BIBLE STUDY HANDBOOK</span>
      <span>{section}</span>
      <span>{page_num}</span>
    </div>'''


# ====================================================================
# PAGE BUILDERS
# ====================================================================

def cover_page():
    """Redesigned cover: Modern Botanical Moody (Forest Green + Gold)."""
    return """
<div class="cover">
  <!-- texture overlay -->
  <div class="cover-texture"></div>
  <!-- gold frame -->
  <div class="cover-frame"></div>
  <div class="cover-frame-inner"></div>
  <!-- right olive branch -->
  <svg class="cover-botanical-r" viewBox="0 0 300 400" xmlns="http://www.w3.org/2000/svg"
       preserveAspectRatio="xMidYEnd meet">
    <path d="M 250 380 Q 220 300 200 250 Q 180 190 160 130 Q 145 90 130 50"
          fill="none" stroke="#c9a84c" stroke-width="1.2" stroke-linecap="round"/>
    <path d="M 200 250 Q 230 230 260 210"
          fill="none" stroke="#c9a84c" stroke-width="0.8" stroke-linecap="round" opacity="0.6"/>
    <path d="M 160 130 Q 130 110 100 95"
          fill="none" stroke="#c9a84c" stroke-width="0.8" stroke-linecap="round" opacity="0.6"/>
    <g fill="none" stroke="#c9a84c" stroke-width="1">
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
      <ellipse cx="240" cy="225" rx="10" ry="3.5" transform="rotate(15 240 225)" opacity="0.5"/>
      <ellipse cx="250" cy="215" rx="9" ry="3" transform="rotate(-10 250 215)" opacity="0.5"/>
      <ellipse cx="120" cy="105" rx="9" ry="3" transform="rotate(-15 120 105)" opacity="0.5"/>
      <ellipse cx="110" cy="100" rx="8" ry="2.5" transform="rotate(10 110 100)" opacity="0.5"/>
    </g>
    <circle cx="228" cy="300" r="2.5" fill="#c9a84c" opacity="0.6"/>
    <circle cx="222" cy="295" r="2" fill="#c9a84c" opacity="0.5"/>
    <circle cx="188" cy="195" r="2" fill="#c9a84c" opacity="0.5"/>
    <circle cx="182" cy="190" r="1.8" fill="#c9a84c" opacity="0.4"/>
  </svg>
  <!-- left olive branch (mirrored) -->
  <svg class="cover-botanical-l" viewBox="0 0 250 300" xmlns="http://www.w3.org/2000/svg"
       preserveAspectRatio="xMidYEnd meet">
    <g transform="scale(-1,1)" transform-origin="125 150">
      <path d="M 50 280 Q 70 220 90 170 Q 110 120 125 70 Q 135 40 140 20"
            fill="none" stroke="#c9a84c" stroke-width="1" stroke-linecap="round"/>
      <path d="M 90 170 Q 65 155 45 145"
            fill="none" stroke="#c9a84c" stroke-width="0.7" stroke-linecap="round" opacity="0.5"/>
      <g fill="none" stroke="#c9a84c" stroke-width="0.9">
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
      <circle cx="72" cy="215" r="2" fill="#c9a84c" opacity="0.5"/>
      <circle cx="78" cy="210" r="1.8" fill="#c9a84c" opacity="0.4"/>
    </g>
  </svg>
  <!-- main content -->
  <div class="cover-content-new">
    <!-- cross -->
    <svg viewBox="0 0 60 80" xmlns="http://www.w3.org/2000/svg" class="cover-cross-new">
      <g fill="none" stroke="#c9a84c" stroke-width="1.5" stroke-linecap="round">
        <line x1="30" y1="10" x2="30" y2="72"/>
        <line x1="12" y1="28" x2="48" y2="28"/>
        <line x1="26" y1="10" x2="34" y2="10"/>
        <line x1="26" y1="72" x2="34" y2="72"/>
        <line x1="12" y1="24" x2="12" y2="32"/>
        <line x1="48" y1="24" x2="48" y2="32"/>
      </g>
      <circle cx="30" cy="28" r="2" fill="#c9a84c" opacity="0.6"/>
    </svg>
    <div class="cover-overline-new">A Study Journal</div>
    <div class="cover-title-new">Bible Study</div>
    <div class="cover-title-italic-new">Handbook</div>
    <div class="cover-divider-new">
      <div class="cover-divider-line-new"></div>
      <span class="cover-divider-icon-new">&#10022;</span>
      <div class="cover-divider-line-new"></div>
    </div>
    <div class="cover-subtitle-new">Reflection &middot; Prayer &middot; Spiritual Growth</div>
    <div class="cover-badges-new">
      <span class="cover-badge-new">SOAP</span>
      <span class="cover-badge-new">Inductive</span>
      <span class="cover-badge-new">Verse Mapping</span>
      <span class="cover-badge-new">Prayer Journal</span>
    </div>
  </div>
  <!-- verse at bottom -->
  <div class="cover-verse-block-new">
    <div class="cover-verse-new">&ldquo;Your word is a lamp to my feet<br/>and a light to my path.&rdquo;</div>
    <div class="cover-verse-ref-new">Psalm 119:105</div>
  </div>
</div>"""


def belongs_to_page():
    return f"""
<div class="page">
  <div style="display:flex; flex-direction:column; align-items:center;
       justify-content:center; height:100%; text-align:center;">
    <div style="font-size:10pt; letter-spacing:5pt; color:{GOLD};
         text-transform:uppercase; margin-bottom:20px;">This Handbook Belongs To</div>
    <div style="width:5in; border-bottom:2px solid {NAVY}; height:40px;
         margin-bottom:12px;"></div>
    <div style="font-size:10pt; color:{GRAY_LIGHT}; letter-spacing:1pt;">NAME</div>
    <div style="height:50px;"></div>
    <div style="width:5in; border-bottom:2px solid {NAVY}; height:40px;
         margin-bottom:12px;"></div>
    <div style="font-size:10pt; color:{GRAY_LIGHT}; letter-spacing:1pt;">DATE STARTED</div>
    <div style="height:40px;"></div>
    <div style="font-size:14pt; color:{NAVY}; font-style:italic; margin-top:10px;">
      "Commit your work to the Lord,<br/>and your plans will be established."
    </div>
    <div style="font-size:10pt; color:{GOLD}; margin-top:6px; letter-spacing:1pt;">
      — PROVERBS 16:3 —
    </div>
  </div>
</div>"""


def toc_page(toc_entries, page_num=3):
    items = ""
    for i, (name, sec) in enumerate(toc_entries):
        items += f"""<div class="toc-item">
          <span class="toc-num">{i+1:02d}</span>
          <span class="toc-name">{name}</span>
          <span class="toc-dots"></span>
          <span class="toc-page">p. {page_num}</span>
        </div>"""
        page_num += 1  # simplified; real pages set manually below
    return f"""
<div class="page">
  <div class="page-tag">Contents</div>
  <div class="page-title">Table of Contents</div>
  <div class="page-rule"></div>
  {items}
</div>"""


def how_to_page():
    return f"""
<div class="page">
  <div class="page-tag">Getting Started</div>
  <div class="page-title">How to Use This Handbook</div>
  <div class="page-rule"></div>

  <p style="font-size:11pt; line-height:1.7; color:{GRAY_TEXT}; margin-bottom:14px;">
    This handbook is designed to guide you deeper into God's Word through
    a variety of study methods. You don't need to use every method at once —
    choose the one that fits your current season and let the Spirit lead.
    Below is a brief overview of each section.
  </p>

  <div style="font-size:10.5pt; line-height:1.8;">
    <div style="margin-bottom:10px;">
      <strong style="color:{NAVY};">1. Bible Reading Plan</strong><br/>
      <span style="color:{GRAY_LIGHT}; font-style:italic;">
      Track your progress through all 66 books of the Bible. Check off each
      book as you complete it.</span>
    </div>
    <div style="margin-bottom:10px;">
      <strong style="color:{NAVY};">2. SOAP Study Method</strong><br/>
      <span style="color:{GRAY_LIGHT}; font-style:italic;">
      Scripture &mdash; Observation &mdash; Application &mdash; Prayer.
      A simple, powerful four-step method for daily study.</span>
    </div>
    <div style="margin-bottom:10px;">
      <strong style="color:{NAVY};">3. Inductive Bible Study</strong><br/>
      <span style="color:{GRAY_LIGHT}; font-style:italic;">
      Observation, Interpretation, and Application for deeper, more
      structured study of any passage.</span>
    </div>
    <div style="margin-bottom:10px;">
      <strong style="color:{NAVY};">4. Verse Mapping</strong><br/>
      <span style="color:{GRAY_LIGHT}; font-style:italic;">
      Deep-dive into a single verse: context, keywords, cross-references,
      and personal application.</span>
    </div>
    <div style="margin-bottom:10px;">
      <strong style="color:{NAVY};">5. Character Study</strong><br/>
      <span style="color:{GRAY_LIGHT}; font-style:italic;">
      Examine the life of a biblical figure: their strengths, struggles,
      and what God teaches through them.</span>
    </div>
    <div style="margin-bottom:10px;">
      <strong style="color:{NAVY};">6. Topical Study</strong><br/>
      <span style="color:{GRAY_LIGHT}; font-style:italic;">
      Explore what the Bible says about a specific theme across multiple
      books and verses.</span>
    </div>
    <div style="margin-bottom:10px;">
      <strong style="color:{NAVY};">7. Sermon Notes</strong><br/>
      <span style="color:{GRAY_LIGHT}; font-style:italic;">
      Capture key points, scripture references, and action items from
      Sunday services and conferences.</span>
    </div>
    <div style="margin-bottom:10px;">
      <strong style="color:{NAVY};">8. Prayer Journal</strong><br/>
      <span style="color:{GRAY_LIGHT}; font-style:italic;">
      Record requests, thanksgivings, and God's answers over time.</span>
    </div>
    <div style="margin-bottom:10px;">
      <strong style="color:{NAVY};">9. Gratitude</strong><br/>
      <span style="color:{GRAY_LIGHT}; font-style:italic;">
      Count your blessings daily and cultivate a heart of thanksgiving.</span>
    </div>
    <div style="margin-bottom:10px;">
      <strong style="color:{NAVY};">10. Notes &amp; Reflection</strong><br/>
      <span style="color:{GRAY_LIGHT}; font-style:italic;">
      Open lined and grid pages for free journaling, sketches, and
      additional reflections.</span>
    </div>
  </div>

  <div style="margin-top:18px; padding:12px 16px; background:{GOLD_LIGHT};
       border-radius:4px; font-size:10pt; color:{NAVY}; font-style:italic;
       line-height:1.6;">
    <strong>Tip:</strong> There is no "right" way to use this handbook.
    Make it your own. Write in the margins. Underline. Doodle. This is
    your personal journey with God's Word.
  </div>

  {footer("", "Getting Started")}
</div>"""


def section_divider(number, label, title, description):
    return f"""
<div class="page divider-page">
  <div class="divider-num">{number:02d}</div>
  <div class="divider-label">{label}</div>
  <div class="divider-title">{title}</div>
  <div class="divider-line"></div>
  <div class="divider-desc">{description}</div>
</div>"""


# ---- READING PLAN ----

BIBLE_BOOKS = [
    ("Genesis", "Gen"), ("Exodus", "Ex"), ("Leviticus", "Lev"),
    ("Numbers", "Num"), ("Deuteronomy", "Deut"),
    ("Joshua", "Josh"), ("Judges", "Judg"), ("Ruth", "Ruth"),
    ("1 Samuel", "1 Sam"), ("2 Samuel", "2 Sam"),
    ("1 Kings", "1 Kgs"), ("2 Kings", "2 Kgs"),
    ("1 Chronicles", "1 Chr"), ("2 Chronicles", "2 Chr"),
    ("Ezra", "Ezra"), ("Nehemiah", "Neh"), ("Esther", "Est"),
    ("Job", "Job"), ("Psalms", "Ps"), ("Proverbs", "Prov"),
    ("Ecclesiastes", "Ecc"), ("Song of Solomon", "Song"),
    ("Isaiah", "Isa"), ("Jeremiah", "Jer"), ("Lamentations", "Lam"),
    ("Ezekiel", "Ezek"), ("Daniel", "Dan"),
    ("Hosea", "Hos"), ("Joel", "Joel"), ("Amos", "Amos"),
    ("Obadiah", "Obad"), ("Jonah", "Jon"), ("Micah", "Mic"),
    ("Nahum", "Nah"), ("Habakkuk", "Hab"), ("Zephaniah", "Zeph"),
    ("Haggai", "Hag"), ("Zechariah", "Zech"), ("Malachi", "Mal"),
    # NT
    ("Matthew", "Matt"), ("Mark", "Mark"), ("Luke", "Luke"),
    ("John", "John"), ("Acts", "Acts"),
    ("Romans", "Rom"), ("1 Corinthians", "1 Cor"),
    ("2 Corinthians", "2 Cor"), ("Galatians", "Gal"),
    ("Ephesians", "Eph"), ("Philippians", "Phil"),
    ("Colossians", "Col"), ("1 Thessalonians", "1 Thess"),
    ("2 Thessalonians", "2 Thess"),
    ("1 Timothy", "1 Tim"), ("2 Timothy", "2 Tim"),
    ("Titus", "Titus"), ("Philemon", "Phlm"),
    ("Hebrews", "Heb"), ("James", "Jas"),
    ("1 Peter", "1 Pet"), ("2 Peter", "2 Pet"),
    ("1 John", "1 John"), ("2 John", "2 John"), ("3 John", "3 John"),
    ("Jude", "Jude"), ("Revelation", "Rev"),
]


def reading_plan_page(books, title, page_num):
    rows = ""
    for book, abbrev in books:
        rows += f"""<tr>
          <td class="checkbox">&#9744;</td>
          <td class="book">{book}</td>
          <td style="color:{GRAY_LIGHT}">{abbrev}</td>
          <td class="checkbox">&#9744;</td>
          <td style="font-size:8pt; color:{GRAY_LIGHT};">________</td>
        </tr>"""
    return f"""
<div class="page">
  <div class="page-tag">Reading Plan</div>
  <div class="page-title">{title}</div>
  <div class="page-rule"></div>
  <table class="plan-table">
    <thead><tr>
      <th style="width:8%">&#10003;</th>
      <th style="width:35%">Book</th>
      <th style="width:12%">Abbr.</th>
      <th style="width:8%">Done</th>
      <th style="width:37%">Date Completed</th>
    </tr></thead>
    <tbody>{rows}</tbody>
  </table>
  {footer(page_num, "Reading Plan")}
</div>"""


# ---- SOAP ----

def soap_page(page_num):
    return f"""
<div class="page">
  <div class="page-tag">Daily Study</div>
  <div class="page-title">SOAP Study</div>
  <div class="page-rule"></div>
  <div class="meta-row">
    <span>Date: ______________</span>
    <span style="text-align:center;">Passage: ________________________</span>
    <span class="right">Page ___ of ___</span>
  </div>

  <div class="soap-section scripture">
    <span class="soap-letter">S</span>
    <span class="soap-label">Scripture</span>
    <span class="soap-hint">Write the verse address and key phrase</span>
    <div class="soap-lines">{lines(3)}</div>
  </div>

  <div class="soap-section">
    <span class="soap-letter">O</span>
    <span class="soap-label">Observation</span>
    <span class="soap-hint">What does the text say? Who, what, when, where?</span>
    <div class="soap-lines">{lines(5)}</div>
  </div>

  <div class="soap-section">
    <span class="soap-letter">A</span>
    <span class="soap-label">Application</span>
    <span class="soap-hint">How does this apply to my life today?</span>
    <div class="soap-lines">{lines(5)}</div>
  </div>

  <div class="soap-section">
    <span class="soap-letter">P</span>
    <span class="soap-label">Prayer</span>
    <span class="soap-hint">Respond to God in prayer</span>
    <div class="soap-lines">{lines(4)}</div>
  </div>

  {footer(page_num, "SOAP")}
</div>"""


# ---- INDUCTIVE ----

def inductive_page(page_num):
    return f"""
<div class="page">
  <div class="page-tag">Deep Study</div>
  <div class="page-title">Inductive Study</div>
  <div class="page-rule"></div>
  <div class="meta-row">
    <span>Date: ______________</span>
    <span style="text-align:center;">Book &amp; Chapter: ________________________</span>
    <span class="right">Page ___ of ___</span>
  </div>

  <div class="field-label">Context &amp; Background</div>
  <div class="field-sub">Author, audience, historical setting, literary genre</div>
  {lines(3)}

  <div class="field-label">1. Observation &mdash; What does it say?</div>
  <div class="field-sub">Key words, repeated phrases, commands, promises, warnings</div>
  {lines(5)}

  <div class="field-label">2. Interpretation &mdash; What does it mean?</div>
  <div class="field-sub">Main idea, theological truths, cross-references</div>
  {lines(5)}

  <div class="field-label">3. Application &mdash; How does it apply?</div>
  <div class="field-sub">What will I do? What needs to change?</div>
  {lines(5)}

  {footer(page_num, "Inductive")}
</div>"""


# ---- VERSE MAPPING ----

def verse_map_page(page_num):
    return f"""
<div class="page">
  <div class="page-tag">Deep Study</div>
  <div class="page-title">Verse Mapping</div>
  <div class="page-rule"></div>
  <div class="meta-row">
    <span>Date: ______________</span>
    <span style="text-align:center;">Verse: ________________________________</span>
    <span class="right">Page ___ of ___</span>
  </div>

  <div class="vm-step">
    <div class="vm-step-title">Step 1 &mdash; Write the Verse Address</div>
    <div class="field-sub">Book, chapter, verse (look it up in your Bible)</div>
    {lines(2)}
  </div>

  <div class="vm-step">
    <div class="vm-step-title">Step 2 &mdash; Context</div>
    <div class="field-sub">Surrounding verses, book context, historical background</div>
    {lines(3)}
  </div>

  <div class="vm-step">
    <div class="vm-step-title">Step 3 &mdash; Key Words</div>
    <div class="field-sub">Original meaning, repeated themes, significance</div>
    <div style="display:flex; gap:12px;">
      <div style="flex:1;">{lines(2)}</div>
      <div style="flex:1;">{lines(2)}</div>
    </div>
  </div>

  <div class="vm-step">
    <div class="vm-step-title">Step 4 &mdash; Cross-References</div>
    <div class="field-sub">Other verses that connect to this passage</div>
    {lines(3)}
  </div>

  <div class="vm-step">
    <div class="vm-step-title">Step 5 &mdash; Application &amp; Prayer</div>
    <div class="field-sub">What is God saying to me? How will I respond?</div>
    {lines(3)}
  </div>

  {footer(page_num, "Verse Mapping")}
</div>"""


# ---- CHARACTER STUDY ----

def character_page(page_num):
    return f"""
<div class="page">
  <div class="page-tag">Deep Study</div>
  <div class="page-title">Character Study</div>
  <div class="page-rule"></div>
  <div class="meta-row">
    <span>Date: ______________</span>
    <span style="text-align:center;">Character: ______________________________</span>
    <span class="right">Page ___ of ___</span>
  </div>

  <div class="field-label">Key Scripture References</div>
  {lines(2)}

  <div class="char-grid">
    <div class="char-cell">
      <div class="char-cell-label">Background</div>
      <div class="field-sub">Family, era, role</div>
      {lines(3, "write-line-tight")}
    </div>
    <div class="char-cell">
      <div class="char-cell-label">Strengths &amp; Faith</div>
      {lines(3, "write-line-tight")}
    </div>
    <div class="char-cell">
      <div class="char-cell-label">Struggles &amp; Weaknesses</div>
      {lines(3, "write-line-tight")}
    </div>
    <div class="char-cell">
      <div class="char-cell-label">Lessons Learned</div>
      {lines(3, "write-line-tight")}
    </div>
  </div>

  <div class="field-label" style="margin-top:10px;">How Their Story Points to Christ</div>
  {lines(3)}

  <div class="field-label">Personal Application</div>
  {lines(3)}

  {footer(page_num, "Character Study")}
</div>"""


# ---- TOPICAL STUDY ----

def topical_page(page_num):
    return f"""
<div class="page">
  <div class="page-tag">Deep Study</div>
  <div class="page-title">Topical Study</div>
  <div class="page-rule"></div>
  <div class="meta-row">
    <span>Date: ______________</span>
    <span style="text-align:center;">Topic: ________________________________</span>
    <span class="right">Page ___ of ___</span>
  </div>

  <div class="field-label">Why I'm Studying This Topic</div>
  {lines(2)}

  <div class="field-label">Key Verses &amp; References</div>
  <div class="field-sub">List verse addresses and what each says about the topic</div>
  <table style="width:100%; font-size:9pt; border-collapse:collapse;">
    <thead><tr>
      <th style="text-align:left; border-bottom:1px solid {GRAY_BORDER};
           padding:4px; font-size:8.5pt; color:{NAVY};
           text-transform:uppercase; width:30%;">Reference</th>
      <th style="text-align:left; border-bottom:1px solid {GRAY_BORDER};
           padding:4px; font-size:8.5pt; color:{NAVY};
           text-transform:uppercase;">Key Insight</th>
    </tr></thead>
    <tbody>
      {''.join([f'<tr><td style="border-bottom:1px solid #eee; padding:3px; height:28px;"></td><td style="border-bottom:1px solid #eee; padding:3px;"></td></tr>' for _ in range(8)])}
    </tbody>
  </table>

  <div class="field-label" style="margin-top:10px;">Summary &amp; Conclusion</div>
  {lines(3)}

  <div class="field-label">Application</div>
  {lines(3)}

  {footer(page_num, "Topical Study")}
</div>"""


# ---- SERMON NOTES ----

def sermon_page(page_num):
    return f"""
<div class="page">
  <div class="page-tag">Sunday &amp; Conference</div>
  <div class="page-title">Sermon Notes</div>
  <div class="page-rule"></div>

  <div class="sermon-info">
    <div class="sermon-info-cell">
      <div class="sermon-info-label">Date</div>
      <div style="border-bottom:1px solid #ddd; height:20px; margin-top:2px;"></div>
    </div>
    <div class="sermon-info-cell">
      <div class="sermon-info-label">Speaker</div>
      <div style="border-bottom:1px solid #ddd; height:20px; margin-top:2px;"></div>
    </div>
    <div class="sermon-info-cell">
      <div class="sermon-info-label">Scripture</div>
      <div style="border-bottom:1px solid #ddd; height:20px; margin-top:2px;"></div>
    </div>
  </div>

  <div class="field-label">Main Message / Title</div>
  {lines(2)}

  <div class="field-label">Key Points</div>
  <div class="field-sub">Outline the main ideas shared</div>
  {lines(8)}

  <div class="field-label">Scripture References Mentioned</div>
  {lines(3)}

  <div class="field-label">Personal Takeaway &amp; Action Items</div>
  <div class="field-sub">What will I do differently this week?</div>
  {lines(4)}

  {footer(page_num, "Sermon Notes")}
</div>"""


# ---- PRAYER JOURNAL ----

def prayer_page(page_num):
    return f"""
<div class="page">
  <div class="page-tag">Prayer</div>
  <div class="page-title">Prayer Journal</div>
  <div class="page-rule"></div>
  <div class="meta-row">
    <span>Week of: ____________</span>
    <span class="right">Page ___ of ___</span>
  </div>

  <div class="prayer-box">
    <div class="prayer-label">Thanksgiving &mdash; What I'm grateful for</div>
    {lines(3, "write-line-tight")}
  </div>

  <div class="prayer-box">
    <div class="prayer-label">Requests &mdash; For myself and loved ones</div>
    {lines(4, "write-line-tight")}
  </div>

  <div class="prayer-box">
    <div class="prayer-label">Intercession &mdash; For others, community, world</div>
    {lines(4, "write-line-tight")}
  </div>

  <div class="prayer-box">
    <div class="prayer-label">God's Answers &mdash; How He has responded</div>
    {lines(3, "write-line-tight")}
  </div>

  {footer(page_num, "Prayer")}
</div>"""


# ---- GRATITUDE ----

def gratitude_page(page_num):
    rows = ""
    for i in range(1, 11):
        rows += f"""<div class="gratitude-row">
          <div class="gratitude-num">{i}</div>
          <div style="flex:1; border-bottom:1px solid #eee; height:24px;"></div>
        </div>"""
    return f"""
<div class="page">
  <div class="page-tag">Gratitude</div>
  <div class="page-title">Count Your Blessings</div>
  <div class="page-rule"></div>
  <div class="meta-row">
    <span>Date: ______________</span>
    <span class="right">"Give thanks in all circumstances" &mdash; 1 Thess 5:18</span>
  </div>
  {rows}
  <div style="margin-top:12px;">
    <div class="field-label">Why I'm Thankful Today</div>
    {lines(3)}
  </div>
  {footer(page_num, "Gratitude")}
</div>"""


# ---- LINED NOTES ----

def lined_notes_page(page_num, heading="Notes & Reflection"):
    return f"""
<div class="page">
  <div class="page-tag">Reflection</div>
  <div class="page-title">{heading}</div>
  <div class="page-rule"></div>
  <div class="meta-row">
    <span>Date: ______________</span>
    <span class="right">Page ___ of ___</span>
  </div>
  <div class="lined-fill">{lines(26)}</div>
  {footer(page_num, "Notes")}
</div>"""


# ---- GRID PAGE ----

def grid_page(page_num, heading="Sketch & Diagram"):
    return f"""
<div class="page">
  <div class="page-tag">Visual Study</div>
  <div class="page-title">{heading}</div>
  <div class="page-rule"></div>
  <div class="meta-row">
    <span>Date: ______________</span>
    <span class="right">Topic: ____________________</span>
  </div>
  <div class="grid-area" style="min-height:8.3in;"></div>
  {footer(page_num, "Grid")}
</div>"""


# ====================================================================
# ASSEMBLE THE FULL BOOK
# ====================================================================

def generate(output_path=OUTPUT_FILE):
    pages = []
    pg = 1  # page counter (starts after cover)

    # --- FRONT MATTER ---
    pages.append(cover_page())
    pages.append(belongs_to_page())

    # TOC entries (manually set page numbers to match below)
    toc_data = [
        ("How to Use This Handbook", 4),
        ("Bible Reading Plan (OT & NT)", 6),
        ("SOAP Study Method", 9),
        ("Inductive Bible Study", 15),
        ("Verse Mapping", 19),
        ("Character Study", 23),
        ("Topical Study", 25),
        ("Sermon Notes", 27),
        ("Prayer Journal", 33),
        ("Gratitude Log", 39),
        ("Notes & Reflection", 42),
        ("Sketch & Diagram", 46),
    ]
    pages.append(toc_page(toc_data, page_num=3))
    pages.append(how_to_page())

    # --- SECTION 1: READING PLAN ---
    pages.append(section_divider(
        1, "Reading Plan",
        "Bible Reading Plan",
        "Journey through all 66 books of Scripture. Check off each book "
        "as you read it, and record the date completed."
    ))
    ot_books = BIBLE_BOOKS[:39]
    nt_books = BIBLE_BOOKS[39:]
    pages.append(reading_plan_page(ot_books, "Old Testament &#8226; 39 Books", 7))
    pages.append(reading_plan_page(nt_books, "New Testament &#8226; 27 Books", 8))

    # --- SECTION 2: SOAP (20 pages = ~20 studies) ---
    pages.append(section_divider(
        2, "Daily Study",
        "SOAP Study Method",
        "Scripture, Observation, Application, Prayer. "
        "A simple four-step framework for daily engagement with God's Word."
    ))
    for i in range(20):
        pages.append(soap_page(10 + i))

    # --- SECTION 3: INDUCTIVE (12 pages) ---
    pages.append(section_divider(
        3, "Deep Study",
        "Inductive Bible Study",
        "Observe what the text says, interpret what it means, "
        "and apply it to your life. For passages that deserve deeper attention."
    ))
    for i in range(12):
        pages.append(inductive_page(16 + i))

    # --- SECTION 4: VERSE MAPPING (8 pages) ---
    pages.append(section_divider(
        4, "Deep Study",
        "Verse Mapping",
        "Dig deep into a single verse: context, keywords, "
        "cross-references, and personal application."
    ))
    for i in range(8):
        pages.append(verse_map_page(20 + i))

    # --- SECTION 5: CHARACTER STUDY (4 pages) ---
    pages.append(section_divider(
        5, "Deep Study",
        "Character Study",
        "Examine biblical figures &mdash; their faith, flaws, and the "
        "lessons God teaches through their lives."
    ))
    for i in range(4):
        pages.append(character_page(24 + i))

    # --- SECTION 6: TOPICAL STUDY (4 pages) ---
    pages.append(section_divider(
        6, "Deep Study",
        "Topical Study",
        "Trace a theme across Scripture &mdash; grace, faith, love, "
        "forgiveness, or any topic God places on your heart."
    ))
    for i in range(4):
        pages.append(topical_page(26 + i))

    # --- SECTION 7: SERMON NOTES (12 pages) ---
    pages.append(section_divider(
        7, "Sunday & Conference",
        "Sermon Notes",
        "Capture the message, scripture references, and personal "
        "action items from weekly services and conferences."
    ))
    for i in range(12):
        pages.append(sermon_page(28 + i))

    # --- SECTION 8: PRAYER JOURNAL (12 pages) ---
    pages.append(section_divider(
        8, "Prayer",
        "Prayer Journal",
        "Record your requests, intercessions, and God's faithful answers. "
        "Watch your prayer life grow over time."
    ))
    for i in range(12):
        pages.append(prayer_page(34 + i))

    # --- SECTION 9: GRATITUDE (6 pages) ---
    pages.append(section_divider(
        9, "Gratitude",
        "Gratitude Log",
        "A heart of gratitude transforms everything. "
        "Count your blessings and watch them multiply."
    ))
    for i in range(6):
        pages.append(gratitude_page(40 + i))

    # --- SECTION 10: NOTES (8 lined + 2 grid) ---
    pages.append(section_divider(
        10, "Reflection",
        "Notes & Reflection",
        "Open space for free journaling, additional thoughts, "
        "and creative reflection on your journey through Scripture."
    ))
    for i in range(8):
        pages.append(lined_notes_page(42 + i))
    for i in range(2):
        pages.append(grid_page(50 + i))

    # --- BACK COVER (simple closing page) ---
    pages.append(f"""
<div class="page" style="display:flex; flex-direction:column;
     align-items:center; justify-content:center; text-align:center;">
  <div style="font-size:28pt; color:{GOLD}; letter-spacing:8pt; margin-bottom:20px;">
    &#10022;
  </div>
  <div style="font-size:18pt; color:{NAVY}; font-style:italic;
       line-height:1.6; max-width:4.5in;">
    "All Scripture is breathed out by God<br/>
    and profitable for teaching, for reproof,<br/>
    for correction, and for training in righteousness."
  </div>
  <div style="font-size:12pt; color:{GOLD}; margin-top:16px;
       letter-spacing:2pt;">— 2 TIMOTHY 3:16 —</div>
  <div style="width:2in; height:2px; background:{GOLD}; margin:30px auto;"></div>
  <div style="font-size:10pt; color:{GRAY_LIGHT}; letter-spacing:3pt;
       text-transform:uppercase;">
    Bible Study Handbook
  </div>
</div>""")

    # --- WRITE HTML ---
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bible Study Handbook</title>
  {CSS}
</head>
<body>
{''.join(pages)}
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    # Count pages
    page_count = len(pages)
    return output_path, page_count


if __name__ == "__main__":
    path, count = generate()
    print(f"[OK] Bible Study Handbook generated: {os.path.abspath(path)}")
    print(f"     Total pages: {count}")
    print(f"     Trim size: 8.5 x 11 inches")
    print(f"")
    print(f"     Next steps:")
    print(f"       1. Open {path} in your browser")
    print(f"       2. File > Print > Save as PDF")
    print(f"       3. Upload interior PDF to KDP")
