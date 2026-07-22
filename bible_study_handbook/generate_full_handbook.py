#!/usr/bin/env python3
"""
52-Week Bible Study Handbook Generator (v2 - Amazon Review Optimized)
======================================================================
Fixes based on top 20 Amazon competitor negative reviews:
  #1  Paper bleed-through mitigation (decorative back-page elements)
  #2  More writing space (expanded boxes, more lines)
  #3  Darker writing lines (#b8b8b8 not #d5d5d5)
  #5  Varied layouts (3 rotating journal templates)
  #6  Wider binding gutter (0.85in inner margin)
  #8  Larger fonts (10pt body minimum)
  #10 No wasted space (every area purposeful)
  #15 Specific guided questions (not vague)
  #19 Navigation aids (Week __ of 52 on every page)
  +   Pen recommendation page
  +   Page numbers in TOC

Usage:
  python3 generate_full_handbook.py
  Open bible_curriculum.html -> Cmd+P -> Save as PDF
"""

import json, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "curriculum_data.json")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "bible_curriculum.html")

EPOCHS = {
    1:  {"name": "Beginnings",        "desc": "Creation, Fall, Flood & Babel — Genesis 1-11"},
    2:  {"name": "The Patriarchs",    "desc": "Abraham, Isaac, Jacob & Joseph — Genesis 12-50"},
    3:  {"name": "Exodus & Conquest", "desc": "Moses, Sinai, Wilderness & Joshua"},
    4:  {"name": "Kingdom & Kings",   "desc": "Judges, Samuel, David & Solomon"},
    5:  {"name": "Exile & Return",    "desc": "Divided Kingdom, Exile, Daniel & Esther"},
    6:  {"name": "Wisdom & Poetry",   "desc": "Job, Psalms, Proverbs, Song of Solomon"},
    7:  {"name": "The Prophets",      "desc": "Isaiah through Malachi — Voices of Justice & Hope"},
    8:  {"name": "The Gospels",       "desc": "The Life, Death & Resurrection of Jesus"},
    9:  {"name": "The Church Begins", "desc": "Acts, Paul's Letters & the General Epistles"},
    10: {"name": "New Creation",      "desc": "Revelation — The Return of the King"},
}

# Forest green + gold palette
FOREST_DARK  = "#1a3329"
FOREST_MID   = "#244438"
FOREST_LIGHT = "#2d5a47"
GOLD         = "#c9a84c"
GOLD_LIGHT   = "#dcc078"
GOLD_PALE    = "rgba(201,168,76,0.12)"
CREAM        = "#f5f0e1"
CREAM_DEEP   = "#ebe4d0"
GRAY_TEXT    = "#3d3d3d"
GRAY_LIGHT   = "#777777"
GRAY_BORDER  = "#cccccc"
LINE_COLOR   = "#b8b8b8"   # darker lines (#3 fix)
LINE_LIGHT   = "#c8c8c8"

SERIF = "'Georgia', 'Palatino Linotype', serif"
SANS  = "'Helvetica Neue', 'Arial', sans-serif"

# ══════════════════════════════════════════════════
# CSS — all Amazon review fixes applied
# ══════════════════════════════════════════════════

CSS = f"""
<style>
  @page {{ size: 8.5in 11in; margin: 0; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: {SERIF};
    color: {GRAY_TEXT};
    -webkit-print-color-adjust: exact;
    background: #e8e8e8;
  }}

  /* FIX #6: Wider binding gutter (0.85in inner) */
  .page {{
    width: 8.5in; height: 11in;
    padding: 0.5in 0.6in 0.45in 0.85in;
    page-break-after: always;
    position: relative;
    background: white;
    overflow: hidden;
  }}
  .page:last-child {{ page-break-after: auto; }}

  @media screen {{ .page {{ border: 1px dashed #ccc; margin: 8px auto; }} }}
  @media print  {{ .page {{ border: none; margin: 0; }} }}

  /* ═══ COVER ═══ */
  .cover {{
    width: 8.5in; height: 11in; padding: 0;
    background: radial-gradient(ellipse at 50% 30%, {FOREST_LIGHT} 0%, {FOREST_MID} 40%, {FOREST_DARK} 100%);
    color: white; display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    page-break-after: always; position: relative; overflow: hidden;
  }}
  .cover::after {{
    content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.3) 100%);
    pointer-events: none;
  }}
  .cover-frame {{
    position: absolute; top: 0.38in; left: 0.38in; right: 0.38in; bottom: 0.38in;
    border: 1.5px solid {GOLD}; z-index: 3; pointer-events: none;
  }}
  .cover-frame-inner {{
    position: absolute; top: 0.44in; left: 0.44in; right: 0.44in; bottom: 0.44in;
    border: 0.5px solid rgba(201,168,76,0.3); z-index: 3; pointer-events: none;
  }}
  .cover-cross {{ width: 32px; height: 42px; z-index: 5; margin-bottom: 0.35in; position: relative; }}
  .cover-overline {{
    font-family: {SANS}; font-size: 9pt; font-weight: 600; color: {GOLD};
    letter-spacing: 6pt; text-transform: uppercase; z-index: 5;
    margin-bottom: 0.25in; text-indent: 6pt; text-align: center;
  }}
  .cover-title {{
    font-size: 42pt; font-weight: bold; color: {CREAM}; line-height: 1.15;
    z-index: 5; text-align: center; text-shadow: 0 2px 8px rgba(0,0,0,0.4);
  }}
  .cover-title-italic {{
    font-size: 46pt; font-style: italic; color: {GOLD_LIGHT};
    z-index: 5; text-align: center; margin-top: 2px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.4);
  }}
  .cover-divider {{
    display: flex; align-items: center; justify-content: center;
    margin: 0.3in auto; width: 2.5in; z-index: 5;
  }}
  .cover-divider-line {{
    flex: 1; height: 1px;
    background: linear-gradient(to right, transparent, {GOLD}, transparent);
  }}
  .cover-divider-icon {{ color: {GOLD}; font-size: 10pt; margin: 0 10px; }}
  .cover-subtitle {{
    font-family: {SANS}; font-size: 11pt; font-weight: 500;
    color: rgba(255,255,255,0.85); letter-spacing: 3pt; text-transform: uppercase;
    z-index: 5; text-align: center; text-indent: 3pt; max-width: 4.5in; line-height: 1.8;
  }}
  .cover-badges {{ display: flex; gap: 14px; margin-top: 0.4in; z-index: 5; flex-wrap: wrap; justify-content: center; }}
  .cover-badge {{
    font-family: {SANS}; font-size: 8pt; font-weight: 500; color: {GOLD};
    letter-spacing: 2pt; text-transform: uppercase;
    border: 1px solid rgba(201,168,76,0.3); padding: 5px 12px; border-radius: 2px; text-indent: 2pt;
  }}
  .cover-verse-block {{
    position: absolute; bottom: 0.8in; left: 0; right: 0; z-index: 5; text-align: center;
  }}
  .cover-verse {{
    font-size: 12pt; font-style: italic; color: rgba(255,255,255,0.8);
    line-height: 1.6; max-width: 4in; margin: 0 auto;
  }}
  .cover-verse-ref {{
    font-family: {SANS}; font-size: 9pt; font-weight: 600; color: {GOLD};
    letter-spacing: 3pt; text-transform: uppercase; margin-top: 5px; text-indent: 3pt;
  }}

  /* ═══ EPOCH DIVIDER ═══ */
  .divider-page {{
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    text-align: center; background: {FOREST_DARK}; color: white;
    padding: 0.5in 0.6in 0.45in 0.85in;
  }}
  .divider-num {{
    font-size: 80pt; color: {GOLD}; opacity: 0.2; font-weight: bold; line-height: 1;
  }}
  .divider-label {{
    font-family: {SANS}; font-size: 11pt; color: {GOLD}; letter-spacing: 6pt;
    text-transform: uppercase; margin-top: 0.1in;
  }}
  .divider-title {{
    font-size: 30pt; color: {CREAM}; font-weight: bold; margin: 0.15in 0;
  }}
  .divider-line {{ width: 1.5in; height: 2px; background: {GOLD}; margin: 0.1in auto; }}
  .divider-desc {{
    font-size: 13pt; color: rgba(255,255,255,0.6); font-style: italic;
    max-width: 4.5in; line-height: 1.6; margin-top: 0.1in;
  }}

  /* ═══ WEEKLY STUDY PAGE ═══ */
  .study-header {{
    display: flex; align-items: center; gap: 12px;
    margin-bottom: 8px; padding-bottom: 6px;
    border-bottom: 2px solid {GOLD};
  }}
  .week-badge {{
    background: {FOREST_DARK}; color: {CREAM};
    font-family: {SANS}; font-size: 10pt; font-weight: bold;
    padding: 5px 14px; border-radius: 3px;
    letter-spacing: 1pt; white-space: nowrap;
  }}
  .epoch-tag {{
    font-family: {SANS}; font-size: 9pt; color: {GOLD};
    letter-spacing: 3pt; text-transform: uppercase; text-indent: 3pt;
  }}
  /* FIX #19: Week of 52 navigation */
  .week-nav {{
    margin-left: auto; font-family: {SANS}; font-size: 8.5pt; color: {GRAY_LIGHT};
  }}
  .study-title {{
    font-size: 21pt; font-weight: bold; color: {FOREST_DARK};
    margin-bottom: 1px;
  }}
  .study-subtitle {{
    font-size: 12pt; font-style: italic; color: {GRAY_LIGHT}; margin-bottom: 8px;
  }}
  .passage-box {{
    background: {GOLD_PALE}; border-left: 3px solid {GOLD};
    padding: 8px 14px; margin-bottom: 10px; font-size: 10.5pt; color: {FOREST_DARK};
  }}

  /* FIX #8: All labels minimum 8pt */
  .section-label {{
    font-family: {SANS}; font-size: 8.5pt; font-weight: bold; color: {GOLD};
    letter-spacing: 2pt; text-transform: uppercase; text-indent: 2pt;
    margin-top: 7px; margin-bottom: 3px;
  }}
  .theme-text {{
    font-size: 10pt; line-height: 1.6; color: {GRAY_TEXT}; margin-bottom: 8px;
  }}

  .keyverse-box {{
    background: {CREAM}; border: 1px solid {GRAY_BORDER}; border-radius: 4px;
    padding: 8px 14px; margin-bottom: 8px;
  }}
  .keyverse-ref {{
    font-size: 11pt; font-weight: bold; color: {FOREST_DARK}; margin-bottom: 3px;
  }}
  .keyverse-note {{ font-size: 9.5pt; font-style: italic; color: {GRAY_TEXT}; line-height: 1.5; }}

  .bigidea-box {{
    background: {FOREST_DARK}; color: {CREAM}; border-radius: 4px;
    padding: 8px 16px; margin-bottom: 8px;
  }}
  .bigidea-label {{
    font-family: {SANS}; font-size: 8pt; color: {GOLD}; letter-spacing: 2pt;
    text-transform: uppercase; text-indent: 2pt; margin-bottom: 2px;
  }}
  .bigidea-text {{ font-size: 10.5pt; line-height: 1.45; font-style: italic; }}

  .questions-list {{ margin-bottom: 8px; }}
  .question-item {{
    display: flex; gap: 8px; margin-bottom: 4px; font-size: 9.5pt; line-height: 1.5;
  }}
  .question-num {{
    color: {GOLD}; font-weight: bold; flex-shrink: 0; width: 16px;
  }}

  .connection-box {{
    border: 1px solid {GOLD}; border-radius: 4px; padding: 7px 12px; margin-bottom: 7px;
  }}
  .connection-label {{
    font-family: {SANS}; font-size: 8pt; font-weight: bold; color: {GOLD};
    letter-spacing: 2pt; text-transform: uppercase; text-indent: 2pt; margin-bottom: 2px;
  }}
  .connection-text {{ font-size: 9pt; line-height: 1.5; color: {GRAY_TEXT}; }}

  .action-box {{
    background: {GOLD_PALE}; border-radius: 4px; padding: 7px 12px; margin-bottom: 5px;
  }}
  .action-label {{
    font-family: {SANS}; font-size: 8pt; font-weight: bold; color: {FOREST_DARK};
    letter-spacing: 2pt; text-transform: uppercase; text-indent: 2pt; margin-bottom: 2px;
  }}
  .action-text {{ font-size: 9pt; line-height: 1.5; color: {GRAY_TEXT}; }}

  /* FIX #6: Footer adjusted for wider gutter */
  .page-footer {{
    position: absolute; bottom: 0.2in; left: 0.85in; right: 0.6in;
    display: flex; justify-content: space-between;
    font-family: {SANS}; font-size: 8pt; color: {GRAY_LIGHT};
    border-top: 1px solid #e0e0e0; padding-top: 3px;
  }}
  .footer-brand {{ color: {GOLD}; letter-spacing: 2pt; }}

  /* ═══ TOC ═══ */
  .toc-item {{
    display: flex; align-items: baseline; padding: 3px 0; font-size: 9.5pt;
  }}
  .toc-num {{ color: {GOLD}; font-weight: bold; width: 28px; flex-shrink: 0; }}
  .toc-name {{ color: {FOREST_DARK}; }}
  .toc-dots {{ flex: 1; border-bottom: 1px dotted #bbb; margin: 0 5px; height: 12px; }}
  .toc-epoch {{ color: {GRAY_LIGHT}; font-size: 8.5pt; font-style: italic; }}
  .toc-pg {{ color: {GRAY_LIGHT}; font-size: 8.5pt; width: 24px; text-align: right; }}

  /* ═══ CONTENTS PAGE HEADER ═══ */
  .page-tag {{
    font-family: {SANS}; font-size: 9pt; letter-spacing: 4pt;
    color: {GOLD}; text-transform: uppercase; text-align: center; text-indent: 4pt;
  }}
  .page-title {{
    font-size: 22pt; font-weight: bold; text-align: center;
    color: {FOREST_DARK}; margin: 2px 0;
  }}
  .page-rule {{ width: 1.2in; height: 2px; background: {GOLD}; margin: 4px auto 14px; }}

  /* ═══ REFLECTION / JOURNAL PAGE ═══ */
  .journal-header {{
    display: flex; align-items: center; justify-content: space-between;
    margin-bottom: 8px; padding-bottom: 5px; border-bottom: 1.5px solid {GOLD};
  }}
  .journal-week {{
    font-family: {SANS}; font-size: 9.5pt; font-weight: bold; color: {FOREST_DARK};
    letter-spacing: 1pt;
  }}
  .journal-title {{
    font-size: 13pt; font-weight: bold; color: {FOREST_DARK}; font-style: italic;
  }}
  .journal-date {{
    font-family: {SANS}; font-size: 8.5pt; color: {GRAY_LIGHT}; letter-spacing: 1pt;
  }}

  /* SOAP grid */
  .soap-grid {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 8px;
  }}
  .soap-box {{
    border: 1px solid {GRAY_BORDER}; border-radius: 4px; padding: 7px 10px;
    background: #faf9f5;
  }}
  .soap-label {{
    font-family: {SANS}; font-size: 8pt; font-weight: bold; color: {GOLD};
    letter-spacing: 2pt; text-transform: uppercase; text-indent: 2pt; margin-bottom: 4px;
  }}
  .soap-label span {{ color: {FOREST_DARK}; }}

  /* FIX #3: Darker writing lines */
  .write-line {{
    border-bottom: 1px solid {LINE_COLOR}; height: 22px;
  }}
  .write-line:last-child {{ border-bottom: none; }}

  /* FIX #2: More writing lines per section */
  .write-line-tight {{
    border-bottom: 1px solid {LINE_COLOR}; height: 20px;
  }}
  .write-line-tight:last-child {{ border-bottom: none; }}

  /* question with answer space */
  .reflect-q {{
    margin-bottom: 7px;
  }}
  .reflect-q-text {{
    font-size: 9pt; color: {FOREST_DARK}; font-weight: 600; line-height: 1.35;
    margin-bottom: 2px;
  }}
  .reflect-q-text .num {{ color: {GOLD}; font-weight: bold; }}

  /* prayer section */
  .prayer-box {{
    border: 1.5px solid {GOLD}; border-radius: 4px; padding: 8px 14px;
    background: {GOLD_PALE}; margin-bottom: 7px;
  }}
  .prayer-label {{
    font-family: {SANS}; font-size: 8.5pt; font-weight: bold; color: {FOREST_DARK};
    letter-spacing: 2pt; text-transform: uppercase; text-indent: 2pt; margin-bottom: 4px;
  }}

  /* notes area */
  .notes-box {{
    border: 1px solid {GRAY_BORDER}; border-radius: 4px; padding: 6px 10px;
  }}
  .notes-label {{
    font-family: {SANS}; font-size: 8pt; font-weight: bold; color: {GRAY_LIGHT};
    letter-spacing: 2pt; text-transform: uppercase; text-indent: 2pt; margin-bottom: 4px;
  }}

  /* Verse mapping layout */
  .vm-grid {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 8px;
  }}
  .vm-box {{
    border: 1px solid {GRAY_BORDER}; border-radius: 4px; padding: 7px 10px;
    background: #faf9f5;
  }}

  /* Inductive study layout */
  .inductive-box {{
    border: 1px solid {GRAY_BORDER}; border-radius: 4px; padding: 7px 10px;
    margin-bottom: 7px; background: #faf9f5;
  }}

  /* FIX #1: Back-page bleed-through mitigation decorative element */
  .decor-back {{
    width: 8.5in; height: 11in; padding: 0;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    text-align: center; background: {CREAM}; position: relative;
    page-break-after: always; overflow: hidden;
  }}
  .decor-back-frame {{
    position: absolute; top: 0.5in; left: 0.85in; right: 0.6in; bottom: 0.5in;
    border: 1px solid {LINE_LIGHT}; border-radius: 4px;
  }}
  .decor-verse {{
    font-size: 14pt; font-style: italic; color: {FOREST_DARK}; line-height: 1.8;
    max-width: 4in; margin: 0 auto; z-index: 2; position: relative;
  }}
  .decor-ref {{
    font-family: {SANS}; font-size: 10pt; color: {GOLD}; margin-top: 12px;
    letter-spacing: 2pt; z-index: 2; position: relative;
  }}
  .decor-icon {{
    font-size: 24pt; color: {GOLD}; opacity: 0.15; margin-bottom: 20px;
    z-index: 1; position: relative;
  }}

  /* highlighted key word area for inductive */
  .keyword-row {{
    display: flex; gap: 6px; margin-bottom: 4px;
  }}
  .keyword-box {{
    border: 1px dashed {GOLD}; border-radius: 3px; padding: 3px 8px;
    font-size: 9pt; color: {FOREST_DARK}; min-width: 60px; text-align: center;
    background: {CREAM};
  }}

  /* BONUS: Scripture writing section */
  .scripture-write {{
    border: 1.5px solid {GOLD}; border-radius: 4px; padding: 7px 12px;
    margin-bottom: 8px; background: {CREAM}; 
  }}
  .scripture-write-label {{
    font-family: {SANS}; font-size: 8pt; font-weight: bold; color: {FOREST_DARK};
    letter-spacing: 2pt; text-transform: uppercase; text-indent: 2pt; margin-bottom: 4px;
  }}
  .scripture-write-label .ref {{ color: {GOLD}; font-style: italic; text-transform: none; letter-spacing: 0; }}

  /* BONUS: Gratitude section */
  .gratitude-box {{
    border: 1px solid {LINE_LIGHT}; border-left: 3px solid {GOLD}; border-radius: 0 4px 4px 0;
    padding: 6px 12px; margin-bottom: 6px; background: #faf8f0;
  }}
  .gratitude-label {{
    font-family: {SANS}; font-size: 8pt; font-weight: bold; color: {GOLD};
    letter-spacing: 2pt; text-transform: uppercase; text-indent: 2pt; margin-bottom: 3px;
  }}

  /* BONUS: Sermon notes */
  .sermon-field {{
    display: flex; align-items: baseline; gap: 8px; margin-bottom: 6px; font-size: 9.5pt;
  }}
  .sermon-field-label {{
    font-family: {SANS}; font-size: 8.5pt; font-weight: bold; color: {FOREST_DARK};
    letter-spacing: 1pt; text-transform: uppercase; flex-shrink: 0; min-width: 55px;
  }}
  .sermon-field-line {{
    flex: 1; border-bottom: 1px solid {LINE_COLOR}; height: 16px;
  }}
</style>
"""


# ══════════════════════════════════════════════════
# PAGE BUILDERS
# ══════════════════════════════════════════════════

def cover_page():
    return f"""
<div class="cover">
  <div class="cover-frame"></div>
  <div class="cover-frame-inner"></div>
  <svg class="cover-cross" viewBox="0 0 60 80" xmlns="http://www.w3.org/2000/svg">
    <g fill="none" stroke="{GOLD}" stroke-width="1.5" stroke-linecap="round">
      <line x1="30" y1="10" x2="30" y2="72"/>
      <line x1="12" y1="28" x2="48" y2="28"/>
      <line x1="26" y1="10" x2="34" y2="10"/>
      <line x1="26" y1="72" x2="34" y2="72"/>
    </g>
    <circle cx="30" cy="28" r="2" fill="{GOLD}" opacity="0.6"/>
  </svg>
  <div class="cover-overline">A 52-Week Guide Through Scripture</div>
  <div class="cover-title">Bible Study</div>
  <div class="cover-title-italic">Handbook</div>
  <div class="cover-divider">
    <div class="cover-divider-line"></div>
    <span class="cover-divider-icon">&#10022;</span>
    <div class="cover-divider-line"></div>
  </div>
  <div class="cover-subtitle">Reflect &middot; Pray &middot; Grow</div>
  <div class="cover-badges">
    <span class="cover-badge">10 Epochs</span>
    <span class="cover-badge">66 Books</span>
    <span class="cover-badge">52 Weeks</span>
  </div>
  <div class="cover-verse-block">
    <div class="cover-verse">&ldquo;Your word is a lamp to my feet<br/>and a light to my path.&rdquo;</div>
    <div class="cover-verse-ref">Psalm 119:105</div>
  </div>
</div>"""


def belongs_to_page():
    return f"""
<div class="page" style="display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
  <div style="font-size:11pt; letter-spacing:5pt; color:{GOLD}; text-transform:uppercase; text-indent:5pt; margin-bottom:24px;">This Handbook Belongs To</div>
  <div style="width:5in; border-bottom:2px solid {FOREST_DARK}; height:40px; margin-bottom:10px;"></div>
  <div style="font-size:10pt; color:{GRAY_LIGHT}; letter-spacing:1pt;">NAME</div>
  <div style="height:40px;"></div>
  <div style="width:5in; border-bottom:2px solid {FOREST_DARK}; height:40px; margin-bottom:10px;"></div>
  <div style="font-size:10pt; color:{GRAY_LIGHT}; letter-spacing:1pt;">DATE STARTED</div>
  <div style="height:30px;"></div>
  <div style="font-size:14pt; color:{FOREST_DARK}; font-style:italic; margin-top:10px; line-height:1.6;">
    &ldquo;Commit your work to the Lord,<br/>and your plans will be established.&rdquo;
  </div>
  <div style="font-size:10pt; color:{GOLD}; margin-top:5px; letter-spacing:1pt;">Proverbs 16:3</div>
</div>"""


def how_to_page():
    return f"""
<div class="page">
  <div class="page-tag">Getting Started</div>
  <div class="page-title">How to Use This Handbook</div>
  <div class="page-rule"></div>
  <p style="font-size:10.5pt; line-height:1.7; margin-bottom:12px;">
    This handbook is a 52-week journey through the entire Bible, from Genesis to Revelation.
    Each week covers a major passage, theme, or biblical figure. The curriculum is organized
    into 10 epochs that trace God's redemptive story from creation to new creation.
  </p>
  <div style="font-size:10pt; line-height:1.8;">
    <div style="margin-bottom:6px;"><strong style="color:{FOREST_DARK}; font-size:11pt;">Weekly Structure</strong></div>
    <div style="margin-bottom:6px; padding-left:16px;">
      <strong>Passage:</strong> The scripture reading for the week. Look it up in your own Bible.<br/>
      <strong>Theme:</strong> A teaching overview to guide your study and reflection.<br/>
      <strong>Key Verse:</strong> One verse to memorize or meditate on throughout the week.<br/>
      <strong>Big Idea:</strong> The one-sentence takeaway to carry with you.<br/>
      <strong>Questions:</strong> Four reflection prompts for personal study or group discussion.<br/>
      <strong>Christ Connection:</strong> How this passage points to Jesus.<br/>
      <strong>Action Step:</strong> One practical thing to do this week.
    </div>
    <div style="margin-top:10px; margin-bottom:6px;"><strong style="color:{FOREST_DARK}; font-size:11pt;">Journal Page</strong></div>
    <div style="margin-bottom:6px; padding-left:16px;">
      Each week includes a full journaling page with space to write. The layout rotates between<br/>
      three study methods so your experience stays fresh all year long:<br/><br/>
      <strong>Layout A &mdash; SOAP Method:</strong> Write your own observation, application, and prayer.<br/>
      <strong>Layout B &mdash; Verse Mapping:</strong> Break down keywords, cross-references, and meaning.<br/>
      <strong>Layout C &mdash; Inductive Study:</strong> Observe, interpret, and apply the text directly.
    </div>
    <div style="margin-top:10px; margin-bottom:6px;"><strong style="color:{FOREST_DARK}; font-size:11pt;">Tips</strong></div>
    <div style="margin-bottom:6px; padding-left:16px;">
      Set aside a regular time each day (even 15 minutes).<br/>
      Use the questions for journaling or small group discussion.<br/>
      Don't rush. Some weeks may take longer than seven days &mdash; that's okay.<br/>
      Pray before you read. Ask the Holy Spirit to illuminate the text.
    </div>
  </div>
  <div style="margin-top:12px; padding:10px 14px; background:{GOLD_PALE}; border-radius:4px; font-size:9.5pt; color:{FOREST_DARK}; font-style:italic;">
    This handbook uses only verse references &mdash; no translated Scripture text &mdash; so you can
    use it alongside any Bible translation you prefer.
  </div>
  <div class="page-footer"><span class="footer-brand">BIBLE STUDY HANDBOOK</span><span>Getting Started</span><span>3</span></div>
</div>"""


def pen_tips_page():
    """FIX: Pen recommendation page to address bleed-through complaints."""
    return f"""
<div class="page">
  <div class="page-tag">A Helpful Note</div>
  <div class="page-title">Choosing the Right Pen</div>
  <div class="page-rule"></div>
  <p style="font-size:10.5pt; line-height:1.7; margin-bottom:14px; color:{GRAY_TEXT};">
    Because this handbook is printed on Amazon's standard paper, some pens and markers
    may bleed through or ghost on the reverse side. Here is what we recommend for
    the best writing experience:
  </p>

  <div style="font-size:10pt; line-height:1.8;">
    <div style="margin-bottom:10px; padding:10px 14px; background:#e8f5e9; border-radius:4px; border:1px solid #c8e6c9;">
      <div style="font-weight:bold; color:#2e7d32; margin-bottom:4px;">&#10003; RECOMMENDED &mdash; No Bleed-Through</div>
      <div style="font-size:9.5pt; color:{GRAY_TEXT}; line-height:1.7;">
        <strong>Ballpoint pens</strong> (Bic, PaperMate) &mdash; the safest choice, zero bleed-through<br/>
        <strong>Gel pens, fine tip</strong> (Pilot G2 0.38mm, Muji 0.38mm) &mdash; minimal ghosting<br/>
        <strong>Pencils</strong> (mechanical or traditional) &mdash; erasable and clean<br/>
        <strong>Colored pencils</strong> &mdash; great for highlighting and creative journaling
      </div>
    </div>

    <div style="margin-bottom:10px; padding:10px 14px; background:#fff3e0; border-radius:4px; border:1px solid #ffe0b2;">
      <div style="font-weight:bold; color:#e65100; margin-bottom:4px;">&#9888; USE WITH CARE &mdash; May Ghost</div>
      <div style="font-size:9.5pt; color:{GRAY_TEXT}; line-height:1.7;">
        <strong>Felt-tip pens</strong> (PaperMate Flair, Sharpie Pen) &mdash; use light pressure<br/>
        <strong>Gel pens, medium tip</strong> (Pilot G2 0.5mm+) &mdash; write slowly to avoid pooling<br/>
        <strong>Eraser pens</strong> (FriXion) &mdash; safe but ink disappears with heat
      </div>
    </div>

    <div style="margin-bottom:8px; padding:10px 14px; background:#fce4ec; border-radius:4px; border:1px solid #f8bbd0;">
      <div style="font-weight:bold; color:#c62828; margin-bottom:4px;">&#10007; NOT RECOMMENDED &mdash; Will Bleed Through</div>
      <div style="font-size:9.5pt; color:{GRAY_TEXT}; line-height:1.7;">
        <strong>Markers</strong> (Sharpies, Copic, alcohol-based markers)<br/>
        <strong>Highlighters</strong> (liquid ink type) &mdash; use colored pencils instead<br/>
        <strong>Fountain pens</strong> with heavy ink flow
      </div>
    </div>
  </div>

  <div style="margin-top:10px; padding:8px 14px; background:{GOLD_PALE}; border-radius:4px; font-size:9pt; color:{FOREST_DARK}; font-style:italic; text-align:center;">
    Tip: The decorative scripture pages between weeks are designed to minimize
    visible ghosting on the reverse side.
  </div>

  <div class="page-footer"><span class="footer-brand">BIBLE STUDY HANDBOOK</span><span>Pen Guide</span><span>4</span></div>
</div>"""


def toc_page(page_map, page_num_start=5):
    """FIX: TOC split into 2 pages to prevent overflow.
    Page 1: Epochs 1-5 (Weeks 1-26)
    Page 2: Epochs 6-10 (Weeks 27-52)"""
    pages_html = ""
    epoch_halves = [
        ("Part 1: The Old Testament Story", [1, 2, 3, 4, 5]),
        ("Part 2: Christ & The Church", [6, 7, 8, 9, 10]),
    ]
    current_pg = page_num_start
    for half_title, epoch_nums in epoch_halves:
        pages_html += f"""
<div class="page">
  <div class="page-tag">Contents</div>
  <div class="page-title">52-Week Curriculum</div>
  <div class="page-rule"></div>
  <div style="font-size:10pt; color:{GRAY_LIGHT}; font-style:italic; margin-bottom:8px; text-align:center;">{half_title}</div>"""
        for ep_num in epoch_nums:
            weeks_in_epoch = [w for w in DATA if w["epoch"] == ep_num]
            if not weeks_in_epoch:
                continue
            ep = EPOCHS[ep_num]
            pages_html += f"""
    <div style="margin-top:5px; margin-bottom:2px; font-size:9pt; font-weight:bold; color:{GOLD}; letter-spacing:2pt; text-transform:uppercase; text-indent:2pt; border-bottom:1px solid {GOLD_PALE}; padding-bottom:2px;">Epoch {ep_num} &middot; {ep["name"]}</div>"""
            for w in weeks_in_epoch:
                pg = page_map.get(w["week"], "")
                passages_short = w["passages"][:24] + ("..." if len(w["passages"]) > 24 else "")
                pages_html += f"""
    <div class="toc-item">
      <span class="toc-num">{w["week"]:02d}</span>
      <span class="toc-name">{w["title"]}</span>
      <span class="toc-dots"></span>
      <span class="toc-epoch">{passages_short}</span>
      <span class="toc-pg">{pg}</span>
    </div>"""
        pages_html += f"""
  <div class="page-footer"><span class="footer-brand">BIBLE STUDY HANDBOOK</span><span>Contents</span><span>{current_pg}</span></div>
</div>"""
        current_pg += 1
    return pages_html


def epoch_divider(epoch_num):
    ep = EPOCHS[epoch_num]
    return f"""
<div class="page divider-page">
  <div class="divider-num">{epoch_num:02d}</div>
  <div class="divider-label">Epoch {epoch_num}</div>
  <div class="divider-title">{ep["name"]}</div>
  <div class="divider-line"></div>
  <div class="divider-desc">{ep["desc"]}</div>
</div>"""


def study_page(week_data, page_num):
    w = week_data
    ep = EPOCHS[w["epoch"]]

    questions_html = ""
    for i, q in enumerate(w["questions"]):
        questions_html += f'<div class="question-item"><span class="question-num">{i+1}.</span><span>{q}</span></div>\n'

    return f"""
<div class="page">
  <div class="study-header">
    <span class="week-badge">WEEK {w["week"]:02d}</span>
    <span class="epoch-tag">Epoch {w["epoch"]} &middot; {ep["name"]}</span>
    <span class="week-nav">Week {w["week"]} of 52</span>
  </div>
  <div class="study-title">{w["title"]}</div>
  <div class="study-subtitle">{w["subtitle"]}</div>

  <div class="passage-box"><strong>Scripture:</strong> {w["passages"]}</div>

  <div class="section-label">Theme &amp; Teaching</div>
  <div class="theme-text">{w["theme"]}</div>

  <div class="keyverse-box">
    <div class="keyverse-ref">{w["key_verse_ref"]}</div>
    <div class="keyverse-note">{w["key_verse_note"]}</div>
  </div>

  <div class="bigidea-box">
    <div class="bigidea-label">Big Idea</div>
    <div class="bigidea-text">{w["big_idea"]}</div>
  </div>

  <div class="section-label">Reflection Questions</div>
  <div class="questions-list">
    {questions_html}
  </div>

  <div class="connection-box">
    <div class="connection-label">Christ Connection</div>
    <div class="connection-text">{w["christ_connection"]}</div>
  </div>

  <div class="action-box">
    <div class="action-label">Action Step</div>
    <div class="action-text">{w["action_step"]}</div>
  </div>

  <div class="page-footer">
    <span class="footer-brand">BIBLE STUDY HANDBOOK</span>
    <span>Epoch {w["epoch"]} &middot; {ep["name"]}</span>
    <span>{page_num}</span>
  </div>
</div>"""


# FIX #5: Three rotating journal layouts to prevent monotony

def journal_layout_a(week_data, page_num):
    """Layout A: SOAP Method — every 3rd week (1,4,7,...)
    Bonus: scripture writing + gratitude sections added per positive review research."""
    w = week_data
    reflect_html = ""
    for i, q in enumerate(w["questions"]):
        reflect_html += f"""    <div class="reflect-q">
      <div class="reflect-q-text"><span class="num">{i+1}.</span> {q}</div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
    </div>
"""
    return f"""
<div class="page">
  <div class="journal-header">
    <span class="journal-week">WEEK {w["week"]:02d} &middot; JOURNAL</span>
    <span class="journal-title">{w["title"]}</span>
    <span class="journal-date">Date: ________</span>
  </div>

  <div class="scripture-write">
    <div class="scripture-write-label">Write the Verse <span class="ref">&mdash; {w["key_verse_ref"]}</span></div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="section-label">SOAP Study Method</div>
  <div class="soap-grid">
    <div class="soap-box">
      <div class="soap-label">S &mdash; <span>Scripture</span></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
    </div>
    <div class="soap-box">
      <div class="soap-label">O &mdash; <span>Observation</span></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
    </div>
    <div class="soap-box">
      <div class="soap-label">A &mdash; <span>Application</span></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
    </div>
    <div class="soap-box">
      <div class="soap-label">P &mdash; <span>Prayer</span></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
    </div>
  </div>

  <div class="section-label">Reflection &amp; Response</div>
{reflect_html}

  <div class="gratitude-box">
    <div class="gratitude-label">Today I'm Grateful For</div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="prayer-box">
    <div class="prayer-label">Prayer This Week</div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="page-footer">
    <span class="footer-brand">BIBLE STUDY HANDBOOK</span>
    <span>Week {w["week"]:02d} &middot; Journal A (SOAP)</span>
    <span>{page_num}</span>
  </div>
</div>"""


def journal_layout_b(week_data, page_num):
    """Layout B: Verse Mapping — every 3rd week (2,5,8,...)"""
    w = week_data
    return f"""
<div class="page">
  <div class="journal-header">
    <span class="journal-week">WEEK {w["week"]:02d} &middot; JOURNAL</span>
    <span class="journal-title">{w["title"]}</span>
    <span class="journal-date">Date: ________</span>
  </div>

  <div class="section-label">Verse Mapping</div>

  <div class="vm-grid">
    <div class="vm-box">
      <div class="soap-label">Write the Verse</div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
    </div>
    <div class="vm-box">
      <div class="soap-label">Key Words to Define</div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
    </div>
    <div class="vm-box">
      <div class="soap-label">Cross-References</div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
    </div>
    <div class="vm-box">
      <div class="soap-label">What This Reveals About God</div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
      <div class="write-line-tight"></div>
    </div>
  </div>

  <div class="section-label">Personal Application</div>
  <div class="vm-box" style="margin-bottom:7px;">
    <div class="write-line"></div>
    <div class="write-line"></div>
    <div class="write-line"></div>
  </div>

  <div class="section-label">Reflection Questions</div>
  <div class="reflect-q">
    <div class="reflect-q-text"><span class="num">1.</span> {w["questions"][0]}</div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>
  <div class="reflect-q">
    <div class="reflect-q-text"><span class="num">2.</span> {w["questions"][1]}</div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="prayer-box">
    <div class="prayer-label">Prayer Response</div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="gratitude-box">
    <div class="gratitude-label">Today I'm Grateful For</div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="page-footer">
    <span class="footer-brand">BIBLE STUDY HANDBOOK</span>
    <span>Week {w["week"]:02d} &middot; Journal B (Verse Mapping)</span>
    <span>{page_num}</span>
  </div>
</div>"""


def journal_layout_c(week_data, page_num):
    """Layout C: Inductive Study — every 3rd week (3,6,9,...)"""
    w = week_data
    return f"""
<div class="page">
  <div class="journal-header">
    <span class="journal-week">WEEK {w["week"]:02d} &middot; JOURNAL</span>
    <span class="journal-title">{w["title"]}</span>
    <span class="journal-date">Date: ________</span>
  </div>

  <div class="scripture-write">
    <div class="scripture-write-label">Write the Verse <span class="ref">&mdash; {w["key_verse_ref"]}</span></div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="section-label">Inductive Bible Study</div>

  <div class="inductive-box">
    <div class="soap-label">Observe &mdash; <span style="color:{GRAY_LIGHT}; font-weight:normal; text-transform:none; letter-spacing:0;">What does the text say?</span></div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="inductive-box">
    <div class="soap-label">Interpret &mdash; <span style="color:{GRAY_LIGHT}; font-weight:normal; text-transform:none; letter-spacing:0;">What does the text mean?</span></div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="inductive-box">
    <div class="soap-label">Apply &mdash; <span style="color:{GRAY_LIGHT}; font-weight:normal; text-transform:none; letter-spacing:0;">How does this change my life?</span></div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="section-label">Key Words &amp; Phrases</div>
  <div class="keyword-row">
    <div class="keyword-box">&nbsp;</div>
    <div class="keyword-box">&nbsp;</div>
    <div class="keyword-box">&nbsp;</div>
  </div>
  <div style="height:4px;"></div>
  <div class="keyword-row">
    <div class="keyword-box">&nbsp;</div>
    <div class="keyword-box">&nbsp;</div>
    <div class="keyword-box">&nbsp;</div>
  </div>

  <div style="margin-top:6px;"></div>
  <div class="section-label">Further Reflection</div>
  <div class="reflect-q">
    <div class="reflect-q-text"><span class="num">1.</span> {w["questions"][2]}</div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>
  <div class="reflect-q">
    <div class="reflect-q-text"><span class="num">2.</span> {w["questions"][3]}</div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="prayer-box">
    <div class="prayer-label">Prayer This Week</div>
    <div class="write-line-tight"></div>
  </div>

  <div class="gratitude-box">
    <div class="gratitude-label">Today I'm Grateful For</div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="page-footer">
    <span class="footer-brand">BIBLE STUDY HANDBOOK</span>
    <span>Week {w["week"]:02d} &middot; Journal C (Inductive)</span>
    <span>{page_num}</span>
  </div>
</div>"""


def decor_page(verse_text, verse_ref, page_num):
    """FIX #1: Decorative scripture page to mitigate bleed-through from journal pages."""
    return f"""
<div class="decor-back">
  <div class="decor-back-frame"></div>
  <div class="decor-icon">&#10022;</div>
  <div class="decor-verse">{verse_text}</div>
  <div class="decor-ref">{verse_ref}</div>
</div>"""


def group_study_page(page_num):
    """BONUS: Group study guide page — for small groups / Bible study circles."""
    return f"""
<div class="page">
  <div class="page-tag">For Small Groups</div>
  <div class="page-title">Group Study Guide</div>
  <div class="page-rule"></div>
  <p style="font-size:10.5pt; line-height:1.7; margin-bottom:10px; color:{GRAY_TEXT};">
    This handbook works beautifully for group study. Whether you meet weekly in homes,
    at church, or online, here is a suggested format for a 60&ndash;90 minute gathering.
  </p>
  <div style="font-size:10pt; line-height:1.8;">
    <div style="margin-bottom:8px; padding:8px 12px; background:{GOLD_PALE}; border-radius:4px; border-left:3px solid {GOLD};">
      <div style="font-weight:bold; color:{FOREST_DARK}; margin-bottom:3px;">Before You Meet</div>
      <div style="font-size:9.5pt; color:{GRAY_TEXT};">
        Each member reads the week's Scripture passage and completes the journal page independently.
        Come prepared to share one insight or question.
      </div>
    </div>
    <div style="margin-bottom:6px;"><strong style="color:{FOREST_DARK};">Suggested Meeting Format</strong></div>
    <div style="padding-left:16px; margin-bottom:8px; line-height:1.8;">
      <strong>1. Open in Prayer</strong> (5 min) &mdash; Invite the Holy Spirit to guide your discussion.<br/>
      <strong>2. Read the Passage Aloud</strong> (10 min) &mdash; Take turns reading. Try different translations.<br/>
      <strong>3. Discuss the Big Idea</strong> (10 min) &mdash; What stood out? What surprised you?<br/>
      <strong>4. Work Through the Questions</strong> (25 min) &mdash; Use the four reflection questions from the study page.<br/>
      <strong>5. Share Christ Connections</strong> (10 min) &mdash; How does this passage point to Jesus?<br/>
      <strong>6. Commit to Action Steps</strong> (10 min) &mdash; Each person shares their action step for the week.<br/>
      <strong>7. Close in Prayer</strong> (10 min) &mdash; Pray for each other by name.
    </div>
    <div style="margin-bottom:6px; padding:8px 12px; background:#faf9f5; border-radius:4px; border:1px solid {GRAY_BORDER};">
      <div style="font-weight:bold; color:{FOREST_DARK}; margin-bottom:3px;">Facilitator Tips</div>
      <div style="font-size:9.5pt; color:{GRAY_TEXT}; line-height:1.7;">
        Let silence happen &mdash; people need time to think before sharing.<br/>
        There are no wrong answers in personal reflection. Honor every perspective.<br/>
        If debate arises on interpretation, point back to the text: "What does the Scripture actually say?"<br/>
        Keep Christ at the center. Every passage ultimately points to Him.
      </div>
    </div>
  </div>
  <div class="page-footer"><span class="footer-brand">BIBLE STUDY HANDBOOK</span><span>Group Guide</span><span>{page_num}</span></div>
</div>"""


def sermon_notes_page(page_num, note_num):
    """BONUS: Sermon notes page — multi-use appeal for Sunday worship."""
    return f"""
<div class="page">
  <div class="page-tag">Sermon Notes</div>
  <div class="page-title">Sunday Worship</div>
  <div class="page-rule"></div>

  <div style="margin-bottom:12px;">
    <div class="sermon-field">
      <span class="sermon-field-label">Date</span>
      <div class="sermon-field-line"></div>
    </div>
    <div class="sermon-field">
      <span class="sermon-field-label">Speaker</span>
      <div class="sermon-field-line"></div>
    </div>
    <div class="sermon-field">
      <span class="sermon-field-label">Passage</span>
      <div class="sermon-field-line"></div>
    </div>
    <div class="sermon-field">
      <span class="sermon-field-label">Title</span>
      <div class="sermon-field-line"></div>
    </div>
  </div>

  <div class="section-label">Main Points</div>
  <div style="margin-bottom:10px;">
    <div class="write-line"></div>
    <div class="write-line"></div>
    <div class="write-line"></div>
    <div class="write-line"></div>
    <div class="write-line"></div>
    <div class="write-line"></div>
  </div>

  <div class="section-label">Key Scripture &amp; Quotes</div>
  <div style="margin-bottom:10px;">
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="section-label">How Will I Apply This?</div>
  <div style="margin-bottom:10px;">
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="gratitude-box">
    <div class="gratitude-label">One Thing I Don't Want to Forget</div>
    <div class="write-line-tight"></div>
    <div class="write-line-tight"></div>
  </div>

  <div class="page-footer"><span class="footer-brand">BIBLE STUDY HANDBOOK</span><span>Sermon Notes {note_num}</span><span>{page_num}</span></div>
</div>"""


def back_cover():
    return f"""
<div class="page" style="display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
  <div style="font-size:28pt; color:{GOLD}; letter-spacing:8pt; margin-bottom:16px;">&#10022;</div>
  <div style="font-size:16pt; color:{FOREST_DARK}; font-style:italic; line-height:1.6; max-width:5in;">
    &ldquo;All Scripture is breathed out by God<br/>
    and profitable for teaching, for reproof,<br/>
    for correction, and for training in righteousness.&rdquo;
  </div>
  <div style="font-size:11pt; color:{GOLD}; margin-top:12px; letter-spacing:2pt;">2 Timothy 3:16</div>
  <div style="width:2in; height:2px; background:{GOLD}; margin:28px auto;"></div>
  <div style="font-size:10pt; color:{GRAY_LIGHT}; letter-spacing:3pt; text-transform:uppercase;">
    Bible Study Handbook
  </div>
</div>"""


# ══════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════

with open(DATA_FILE, "r", encoding="utf-8") as f:
    DATA = json.load(f)

# Decorative verses for back of journal pages (one per week, mostly from that week's passages)
DECOR_VERSES = [
    ("In the beginning, God created the heavens and the earth.", "Genesis 1:1"),
    ("I will put enmity between you and the woman, and between your offspring and her offspring.", "Genesis 3:15"),
    ("Noah found favor in the eyes of the Lord.", "Genesis 6:8"),
    ("Let us make a name for ourselves.", "Genesis 11:4"),
    ("He believed the Lord, and He counted it to him as righteousness.", "Genesis 15:6"),
    ("You are a God of seeing... Have I indeed seen Him who looks after me?", "Genesis 16:13"),
    ("Your name shall no longer be called Jacob, but Israel.", "Genesis 32:28"),
    ("You meant evil against me, but God meant it for good.", "Genesis 50:20"),
    ("God said to Moses, 'I AM WHO I AM.'", "Exodus 3:14"),
    ("When I see the blood, I will pass over you.", "Exodus 12:13"),
    ("The Lord will fight for you, and you have only to be silent.", "Exodus 14:14"),
    ("I am the Lord your God, who brought you out of the land of Egypt.", "Exodus 20:2"),
    ("Let them make me a sanctuary, that I may dwell in their midst.", "Exodus 25:8"),
    ("Be strong and courageous. Do not be frightened, for the Lord your God will be with you.", "Joshua 1:9"),
    ("I will surely go with you. The Lord will sell Sisera into the hand of a woman.", "Judges 4:9"),
    ("Where you go I will go, and your God my God.", "Ruth 1:16"),
    ("To obey is better than sacrifice.", "1 Samuel 15:22"),
    ("The Lord looks on the heart.", "1 Samuel 16:7"),
    ("I have sinned against the Lord.", "2 Samuel 12:13"),
    ("Fear God and keep His commandments, for this is the whole duty of man.", "Ecclesiastes 12:13"),
    ("How long will you go limping between two different opinions?", "1 Kings 18:21"),
    ("Save us, that all the kingdoms of the earth may know that You alone are God.", "2 Kings 19:19"),
    ("Because your heart was penitent, I also have heard you.", "2 Kings 22:19"),
    ("I know the plans I have for you, declares the Lord.", "Jeremiah 29:11"),
    ("Our God whom we serve is able to deliver us. But if not, we will not serve your gods.", "Daniel 3:17-18"),
    ("Who knows whether you have not come to the kingdom for such a time as this?", "Esther 4:14"),
    ("I had heard of You by the hearing of the ear, but now my eye sees You.", "Job 42:5"),
    ("How long, O Lord? Will You forget me forever?", "Psalm 13:1"),
    ("I praise You, for I am fearfully and wonderfully made.", "Psalm 139:14"),
    ("The fear of the Lord is the beginning of wisdom.", "Proverbs 9:10"),
    ("I am my beloved's and my beloved is mine.", "Song of Solomon 6:3"),
    ("He was pierced for our transgressions; with His wounds we are healed.", "Isaiah 53:5"),
    ("I will put My law within them, and I will write it on their hearts.", "Jeremiah 31:33"),
    ("I will give you a new heart, and a new spirit I will put within you.", "Ezekiel 36:26"),
    ("Let justice roll down like waters, and righteousness like an ever-flowing stream.", "Amos 5:24"),
    ("Should not I pity Nineveh, that great city?", "Jonah 4:11"),
    ("The sun of righteousness shall rise with healing in its wings.", "Malachi 4:2"),
    ("Behold, I am the servant of the Lord; let it be to me according to Your word.", "Luke 1:38"),
    ("Blessed are the poor in spirit, for theirs is the kingdom of heaven.", "Matthew 5:3"),
    ("I who speak to you am He.", "John 4:26"),
    ("My God, My God, why have You forsaken Me?", "Matthew 27:46"),
    ("He is not here, for He has risen, as He said.", "Matthew 28:6"),
    ("Go therefore and make disciples of all nations.", "Matthew 28:19"),
    ("You will receive power when the Holy Spirit has come upon you.", "Acts 1:8"),
    ("By grace you have been saved through faith... not a result of works.", "Ephesians 2:8-9"),
    ("The fruit of the Spirit is love, joy, peace, patience, kindness, goodness, faithfulness.", "Galatians 5:22"),
    ("I commend to you our sister Phoebe, a servant of the church.", "Romans 16:1"),
    ("Let us then with confidence draw near to the throne of grace.", "Hebrews 4:16"),
    ("Count it all joy when you meet trials of various kinds.", "James 1:2"),
    ("Behold, I stand at the door and knock.", "Revelation 3:20"),
    ("Worthy is the Lamb who was slain.", "Revelation 5:12"),
    ("Behold, I am making all things new.", "Revelation 21:5"),
]


def generate():
    pages = []
    page_num = 0  # tracks the LAST page number used
    page_map = {}  # week -> study page number

    # Front matter — pattern: increment FIRST, then append
    page_num += 1; pages.append(cover_page())           # page 1
    page_num += 1; pages.append(belongs_to_page())       # page 2
    page_num += 1; pages.append(how_to_page())           # page 3
    page_num += 1; pages.append(pen_tips_page())         # page 4
    page_num += 1; pages.append("__TOC_PLACEHOLDER__")   # page 5-6 (rebuilt later)
    page_num += 1                                          # page 6 (second TOC page)

    # Weekly studies with epoch dividers
    current_epoch = 0
    for i, week in enumerate(DATA):
        if week["epoch"] != current_epoch:
            current_epoch = week["epoch"]
            page_num += 1  # divider page
            pages.append(epoch_divider(current_epoch))

        page_num += 1  # study page
        page_map[week["week"]] = page_num
        pages.append(study_page(week, page_num))

        # FIX #5: Rotating journal layout
        page_num += 1  # journal page
        layout_choice = week["week"] % 3
        if layout_choice == 1:
            pages.append(journal_layout_a(week, page_num))
        elif layout_choice == 2:
            pages.append(journal_layout_b(week, page_num))
        else:
            pages.append(journal_layout_c(week, page_num))

        # FIX #1: Decorative verse page after journal (mitigates bleed-through)
        page_num += 1  # decor page
        idx = week["week"] - 1
        if idx < len(DECOR_VERSES):
            vtext, vref = DECOR_VERSES[idx]
        else:
            vtext, vref = DECOR_VERSES[0]
        pages.append(decor_page(vtext, vref, page_num))

    # BONUS: Group study guide
    page_num += 1
    pages.append(group_study_page(page_num))

    # BONUS: 4 sermon notes pages
    for sn in range(1, 5):
        page_num += 1
        pages.append(sermon_notes_page(page_num, sn))

    # Back cover
    page_num += 1
    pages.append(back_cover())

    # Rebuild TOC with actual page numbers
    # Find and replace the placeholder (index 4)
    pages[4] = toc_page(page_map, page_num_start=5)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bible Study Handbook - 52 Week Curriculum</title>
  {CSS}
</head>
<body>
{''.join(pages)}
</body>
</html>"""

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    return len(pages)


if __name__ == "__main__":
    count = generate()
    print(f"[OK] 52-Week Bible Study Handbook generated: {OUTPUT_FILE}")
    print(f"     Total pages: {count}")
    print(f"     Trim size: 8.5 x 11 inches")
    print(f"     10 epochs / 52 weeks / 66 books")
    print(f"     Fixes: darker lines, wider gutter, 3 rotating layouts, pen guide,")
    print(f"            decorative bleed-through pages, larger fonts, navigation aids")
