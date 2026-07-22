#!/usr/bin/env python3
"""
Youth Sports Development Handbook V2.0 — KDP Interior Generator
Trim: 8.5 x 11 in | Language: English
Target: American families / parents coaching young athletes
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import json
import os
import html as html_mod

# ============================================================
# CONFIG
# ============================================================
OUTPUT_DIR = os.path.expanduser("~/sports_handbook_us")
DATA_FILE = os.path.join(OUTPUT_DIR, "content_us.json")
HTML_FILE = os.path.join(OUTPUT_DIR, "sports_handbook_us_V2.0.html")

# ============================================================
# CSS
# ============================================================
def build_css():
    return """
@page { size: 8.5in 11in; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: Georgia, "Iowan Old Style", "Palatino", serif;
  color: #2C2C2C;
  background: white;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

.page {
  width: 8.5in; height: 11in;
  padding: 0.65in 0.875in 0.55in 0.875in;
  page-break-after: always;
  position: relative;
  background: white;
  overflow: hidden;
}
.page:last-child { page-break-after: auto; }

@media screen { .page { border: 1px dashed #ccc; margin: 10px auto; } }
@media print  { .page { border: none; margin: 0; } }

/* ---- Header & Footer ---- */
.page-header {
  display: flex; justify-content: space-between; align-items: center;
  font-size: 8pt; color: #999;
  padding-bottom: 5px; border-bottom: 1px solid #e0e0e0;
  margin-bottom: 18px;
}
.page-header .part-tag { font-weight: 700; letter-spacing: 0.5pt; }
.page-header .topic-tag { color: #bbb; font-style: italic; }

.page-footer {
  position: absolute;
  bottom: 0.32in; left: 0.875in; right: 0.875in;
  font-size: 7.5pt; color: #bbb;
  display: flex; justify-content: space-between;
  border-top: 1px solid #eee; padding-top: 4px;
}

/* ---- Title Page ---- */
.title-page {
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  text-align: center;
  height: 100%;
  padding-top: 0;
}
.title-page .title-main {
  font-size: 34pt; font-weight: 700; color: #1B4D89;
  line-height: 1.2; margin-bottom: 8px;
  letter-spacing: -0.5pt;
}
.title-page .title-bar {
  width: 180px; height: 3px; background: #C25E1C;
  margin: 14px auto 20px;
}
.title-page .title-sub {
  font-size: 13pt; color: #555; font-style: italic;
  line-height: 1.6; max-width: 5in; margin-bottom: 30px;
}
.title-page .title-purpose {
  font-size: 9.5pt; color: #777; line-height: 1.8;
  max-width: 4.5in;
}
.title-page .title-pur-label {
  font-size: 8pt; font-weight: 700; color: #1B4D89;
  letter-spacing: 1.5pt; margin-bottom: 10px;
}

/* ---- Table of Contents ---- */
.toc-title {
  font-size: 22pt; font-weight: 700; color: #1B4D89;
  margin-bottom: 4px;
}
.toc-subtitle {
  font-size: 10pt; color: #aaa; font-style: italic;
  margin-bottom: 20px;
  padding-bottom: 12px; border-bottom: 2px solid #1B4D89;
}
.toc-section { margin-bottom: 16px; }
.toc-section-header {
  display: flex; justify-content: space-between; align-items: baseline;
  font-size: 10pt; font-weight: 700;
  margin-bottom: 4px;
}
.toc-section-header .sec-name { letter-spacing: 0.5pt; }
.toc-section-header .sec-page { font-size: 8.5pt; color: #999; font-weight: 400; }
.toc-item {
  display: flex; justify-content: space-between; align-items: baseline;
  font-size: 9pt; color: #555;
  padding: 2px 0 2px 12px;
}
.toc-item .toc-name { }
.toc-item .toc-dots {
  flex: 1; border-bottom: 1px dotted #ccc; margin: 0 6px 3px;
}
.toc-item .toc-page { color: #888; font-size: 8.5pt; }
.toc-tools-header {
  display: flex; justify-content: space-between; align-items: baseline;
  font-size: 10pt; font-weight: 700; color: #333;
  margin-top: 8px; margin-bottom: 4px;
}

/* ---- Section Divider ---- */
.divider-content {
  color: white;
  padding: 1.6in 1.2in;
  margin-top: 0.2in;
  min-height: 8.5in;
  position: relative;
}
.divider-part-label {
  font-size: 10pt; opacity: 0.7; margin-bottom: 8px;
  letter-spacing: 2pt; text-transform: uppercase;
}
.divider-title {
  font-size: 32pt; font-weight: 700; margin-bottom: 4px;
  line-height: 1.15;
}
.divider-subtitle {
  font-size: 12pt; opacity: 0.6; font-style: italic;
  margin-bottom: 24px;
}
.divider-desc {
  font-size: 10pt; line-height: 1.85; opacity: 0.85;
  max-width: 5.5in; margin-bottom: 24px;
}
.divider-topics {
  font-size: 9pt; line-height: 1.8; opacity: 0.75;
  max-width: 5in;
}
.divider-topic-num {
  display: inline-block; width: 22px; opacity: 0.6;
}

/* ---- Topic Page (Parts 1, 2, 4) ---- */
.topic-title {
  font-size: 20pt; font-weight: 700;
  margin-bottom: 2px; line-height: 1.25;
}
.topic-subtitle {
  font-size: 10pt; color: #aaa; font-style: italic;
  margin-bottom: 16px;
}

/* ---- Sport Page (Part 3) ---- */
.sport-header {
  display: flex; justify-content: space-between; align-items: flex-end;
  margin-bottom: 4px;
}
.sport-title {
  font-size: 20pt; font-weight: 700;
  line-height: 1.25;
}
.sport-age {
  font-size: 8.5pt; color: #888; font-style: italic;
  text-align: right; max-width: 2.2in;
  padding-bottom: 3px;
}

/* ---- Info Boxes ---- */
.info-box {
  padding: 10px 14px; margin-bottom: 10px;
}
.box-label {
  font-size: 8pt; font-weight: 700; letter-spacing: 1pt;
  margin-bottom: 6px; display: block;
  text-transform: uppercase;
}
.info-item {
  position: relative; padding-left: 14px;
  margin-bottom: 4px; font-size: 9.5pt; line-height: 1.55;
}
.info-item:last-child { margin-bottom: 0; }
.info-item::before {
  content: ''; position: absolute; left: 0; top: 7px;
  width: 4px; height: 4px; border-radius: 50%;
}
.info-item-dash::before {
  content: ''; position: absolute; left: 0; top: 9px;
  width: 7px; height: 2px; border-radius: 0;
}

/* ---- Equipment line ---- */
.equipment-line {
  font-size: 8.5pt; color: #777;
  padding: 8px 14px; margin-bottom: 10px;
  border: 1px solid #ddd; border-radius: 3px;
  line-height: 1.5;
}
.equipment-line .equip-label {
  font-weight: 700; letter-spacing: 0.5pt;
}

/* ---- Note Area ---- */
.note-section { margin-top: 6px; }
.note-label {
  font-size: 8pt; font-weight: 700;
  margin-bottom: 8px; letter-spacing: 0.5pt;
  text-transform: uppercase;
}
.note-line {
  height: 20px; border-bottom: 1px solid #BFBFBF;
}

/* ---- Tool Pages ---- */
.tool-title {
  font-size: 18pt; font-weight: 700;
  margin-bottom: 4px;
}
.tool-desc {
  font-size: 9pt; color: #888; font-style: italic;
  margin-bottom: 14px;
}
.tool-field {
  display: flex; align-items: baseline; margin-bottom: 8px;
  font-size: 9.5pt;
}
.tool-field-label {
  font-weight: 700; min-width: 80px;
}
.tool-field-line {
  flex: 1; border-bottom: 1px solid #ccc; height: 16px;
}
.tool-table {
  width: 100%; border-collapse: collapse;
  font-size: 8.5pt; margin-bottom: 12px;
}
.tool-table th {
  background: #f0f0f0; padding: 5px 6px; text-align: left;
  font-weight: 700; border: 1px solid #ccc;
  font-size: 8pt;
}
.tool-table td {
  padding: 5px 6px; border: 1px solid #ccc;
  height: 22px;
}
.tool-table td.td-blank { background: #fafafa; }

/* ---- Generic note page ---- */
.note-page-title {
  font-size: 14pt; font-weight: 700; color: #999;
  margin-bottom: 20px; text-align: center;
  letter-spacing: 2pt; text-transform: uppercase;
}
"""


# ============================================================
# PAGE BUILDERS
# ============================================================

page_counter = [0]

def footer(book_title):
    p = page_counter[0]
    return f'<div class="page-footer"><span>{html_mod.escape(book_title)}</span><span>Page {p}</span></div>'


def page_header(part_label, topic_label):
    return f'''<div class="page-header">
      <span class="part-tag">{html_mod.escape(part_label)}</span>
      <span class="topic-tag">{html_mod.escape(topic_label)}</span>
    </div>'''


def note_lines(n):
    return ''.join('<div class="note-line"></div>' for _ in range(n))


def build_title_page(data):
    book_title = html_mod.escape(data["book_title"])
    book_sub = html_mod.escape(data["book_subtitle"])
    page_counter[0] += 1
    return f'''<div class="page">
  <div class="title-page">
    <div class="title-main">{book_title}</div>
    <div class="title-bar"></div>
    <div class="title-sub">{book_sub}</div>
    <div class="title-pur-label">A PRACTICAL GUIDE FOR PARENTS</div>
    <div class="title-purpose">
      Train fundamental athletic skills. Explore nine of America's most popular
      youth sports. Discover where your child's natural talents lie.
      This handbook gives you the knowledge, drills, and tools to support
      your young athlete's journey from the backyard to the field.
    </div>
  </div>
  <div class="page-footer"><span>{book_title}</span><span>Page {page_counter[0]}</span></div>
</div>'''


def build_toc(data):
    page_counter[0] += 1
    parts = []
    # Calculate page offsets
    # Page 1 = title, Page 2 = TOC, Page 3 = first divider
    current_page = 3
    for sec in data["sections"]:
        sec_start = current_page
        current_page += 1  # divider
        # content pages
        current_page += len(sec["topics"])
        parts.append((sec, sec_start))

    tools_start = current_page
    num_tools = len(data.get("tools", []))
    notes_start = tools_start + num_tools

    toc_sections = ""
    for sec, start in parts:
        color = sec["color"]
        items = ""
        for i, topic in enumerate(sec["topics"]):
            p = start + 1 + i
            items += f'''<div class="toc-item">
        <span class="toc-name">{html_mod.escape(topic["title"])}</span>
        <span class="toc-dots"></span>
        <span class="toc-page">{p}</span>
      </div>'''
        toc_sections += f'''<div class="toc-section">
      <div class="toc-section-header">
        <span class="sec-name" style="color:{color}">{html_mod.escape(sec["part_num"])} &middot; {html_mod.escape(sec["title"])}</span>
        <span class="sec-page">Page {start}</span>
      </div>
      {items}
    </div>'''

    # Tools section
    tools_items = ""
    for i, tool in enumerate(data.get("tools", [])):
        p = tools_start + i
        tools_items += f'''<div class="toc-item">
        <span class="toc-name">{html_mod.escape(tool["title"])}</span>
        <span class="toc-dots"></span>
        <span class="toc-page">{p}</span>
      </div>'''

    # Notes
    tools_items += f'''<div class="toc-item">
        <span class="toc-name">Notes</span>
        <span class="toc-dots"></span>
        <span class="toc-page">{notes_start}</span>
      </div>'''

    toc_sections += f'''<div class="toc-section">
      <div class="toc-tools-header">
        <span>Tools &amp; Resources</span>
      </div>
      {tools_items}
    </div>'''

    return f'''<div class="page">
  <div class="toc-title">Contents</div>
  <div class="toc-subtitle">Your roadmap to developing young athletes</div>
  {toc_sections}
  {footer(data["book_title"])}
</div>'''


def build_divider(sec, data):
    page_counter[0] += 1
    color = sec["color"]
    topics_list = ""
    for i, t in enumerate(sec["topics"]):
        num = f"{i+1:02d}"
        topics_list += f'<div><span class="divider-topic-num">{num}</span>{html_mod.escape(t["title"])}</div>'

    return f'''<div class="page">
  <div class="divider-content" style="background:{color}">
    <div class="divider-part-label">{html_mod.escape(sec["part_num"])}</div>
    <div class="divider-title">{html_mod.escape(sec["title"])}</div>
    <div class="divider-subtitle">{html_mod.escape(sec["subtitle"])}</div>
    <div class="divider-desc">{html_mod.escape(sec["description"])}</div>
    <div class="divider-topics">{topics_list}</div>
  </div>
  {footer(data["book_title"])}
</div>'''


def build_topic_page(topic, sec, data, is_sport=False):
    page_counter[0] += 1
    color = sec["color"]
    color_light = sec["color_light"]
    part_label = f'{sec["part_num"]} &middot; {sec["title"]}'

    if is_sport:
        # Sport page with richer layout
        age_html = ""
        if "age_range" in topic:
            age_html = f'<div class="sport-age">{html_mod.escape(topic["age_range"])}</div>'

        header_html = f'''{page_header(part_label, topic["title"])}
    <div class="sport-header">
      <div class="sport-title" style="color:{color}">{html_mod.escape(topic["title"])}</div>
      {age_html}
    </div>'''

        # Key Skills box
        kp_items = ""
        for kp in topic.get("key_points", []):
            kp_items += f'<div class="info-item" style="color:#333">{html_mod.escape(kp)}</div>'

        # Talent Indicators
        ti_items = ""
        for ti in topic.get("talent_indicators", []):
            ti_items += f'<div class="info-item info-item-dash" style="color:#555">{html_mod.escape(ti)}</div>'

        # Home Drills
        hd_items = ""
        for hd in topic.get("home_drills", []):
            hd_items += f'<div class="info-item info-item-dash" style="color:#555">{html_mod.escape(hd)}</div>'

        # Equipment
        equip_html = ""
        if "equipment" in topic:
            equip_html = f'''<div class="equipment-line">
        <span class="equip-label">EQUIPMENT:</span> {html_mod.escape(topic["equipment"])}
      </div>'''

        # Calculate remaining space for note lines
        num_notes = 3

        return f'''<div class="page">
  {header_html}
  <div class="info-box" style="background:{color_light};border-left:4px solid {color}">
    <span class="box-label" style="color:{color}">Key Skills to Develop</span>
    {kp_items}
  </div>
  <div class="info-box" style="background:#FBF0E4;border-left:4px solid #C25E1C">
    <span class="box-label" style="color:#C25E1C">Talent Indicators</span>
    {ti_items}
  </div>
  <div class="info-box" style="background:#E8F0E8;border-left:4px solid #2E7D32">
    <span class="box-label" style="color:#2E7D32">Home Practice Drills</span>
    {hd_items}
  </div>
  {equip_html}
  <div class="note-section">
    <div class="note-label" style="color:{color}">Practice Notes</div>
    {note_lines(num_notes)}
  </div>
  {footer(data["book_title"])}
</div>'''

    else:
        # Regular topic page (Parts 1, 2, 4)
        header_html = f'''{page_header(part_label, topic["title"])}
    <div class="topic-title" style="color:{color}">{html_mod.escape(topic["title"])}</div>
    <div class="topic-subtitle">Key knowledge for parents</div>'''

        kp_items = ""
        for kp in topic.get("key_points", []):
            kp_items += f'<div class="info-item" style="color:#333">{html_mod.escape(kp)}</div>'

        pt_items = ""
        for pt in topic.get("parent_tips", []):
            pt_items += f'<div class="info-item info-item-dash" style="color:#555">{html_mod.escape(pt)}</div>'

        num_notes = 5

        return f'''<div class="page">
  {header_html}
  <div class="info-box" style="background:{color_light};border-left:4px solid {color}">
    <span class="box-label" style="color:{color}">What Parents Need to Know</span>
    {kp_items}
  </div>
  <div class="info-box" style="background:#FBF0E4;border-left:4px solid #C25E1C">
    <span class="box-label" style="color:#C25E1C">Practical Tips for Parents</span>
    {pt_items}
  </div>
  <div class="note-section">
    <div class="note-label" style="color:{color}">Your Notes</div>
    {note_lines(num_notes)}
  </div>
  {footer(data["book_title"])}
</div>'''


def build_tool_page(tool, idx, total, data):
    page_counter[0] += 1
    title = tool["title"]
    desc = tool["description"]

    if title == "Season Training Planner":
        content = f'''
    <div class="tool-field">
      <span class="tool-field-label">Athlete:</span>
      <span class="tool-field-line"></span>
      <span class="tool-field-label" style="margin-left:20px">Season:</span>
      <span class="tool-field-line"></span>
    </div>
    <div class="tool-field">
      <span class="tool-field-label">Primary Sport:</span>
      <span class="tool-field-line"></span>
    </div>
    <table class="tool-table">
      <tr>
        <th style="width:14%">Week</th>
        <th style="width:20%">Focus Area</th>
        <th style="width:22%">Practice Goals</th>
        <th style="width:22%">Games / Events</th>
        <th style="width:22%">Rest Days</th>
      </tr>
      {''.join(f'<tr><td>{i+1}</td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td></tr>' for i in range(12))}
    </table>
    <div class="note-section">
      <div class="note-label">Season Goals &amp; Reflections</div>
      {note_lines(4)}
    </div>'''

    elif title == "Weekly Practice Log":
        content = f'''
    <div class="tool-field">
      <span class="tool-field-label">Week of:</span>
      <span class="tool-field-line"></span>
      <span class="tool-field-label" style="margin-left:20px">Sport:</span>
      <span class="tool-field-line"></span>
    </div>
    <table class="tool-table">
      <tr>
        <th style="width:12%">Day</th>
        <th style="width:20%">Activity</th>
        <th style="width:12%">Duration</th>
        <th style="width:16%">Intensity</th>
        <th style="width:40%">Notes / How They Felt</th>
      </tr>
      <tr><td>Mon</td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td></tr>
      <tr><td>Tue</td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td></tr>
      <tr><td>Wed</td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td></tr>
      <tr><td>Thu</td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td></tr>
      <tr><td>Fri</td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td></tr>
      <tr><td>Sat</td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td></tr>
      <tr><td>Sun</td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td></tr>
    </table>
    <div class="note-section">
      <div class="note-label">Weekly Summary</div>
      {note_lines(3)}
    </div>'''

    elif title == "Skill Assessment Tracker":
        sports = ["Basketball", "Baseball", "Football", "Soccer", "Swimming",
                  "Tennis", "Track", "Volleyball", "Golf"]
        rows = ""
        for sp in sports:
            rows += f'<tr><td>{sp}</td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td></tr>'

        skills = ["Speed", "Strength", "Agility", "Coordination", "Endurance", "Flexibility"]
        skill_rows = ""
        for sk in skills:
            skill_rows += f'<tr><td>{sk}</td><td class="td-blank"></td><td class="td-blank"></td><td class="td-blank"></td></tr>'

        content = f'''
    <div class="note-label" style="margin-bottom:6px">Sport Skill Ratings (1 = Beginner, 5 = Advanced)</div>
    <table class="tool-table">
      <tr><th style="width:25%">Sport</th><th style="width:18%">Current</th><th style="width:18%">Last Check</th><th style="width:18%">Goal</th><th style="width:21%">Notes</th></tr>
      {rows}
    </table>
    <div class="note-label" style="margin:10px 0 6px">Athletic Ability Ratings</div>
    <table class="tool-table">
      <tr><th style="width:25%">Ability</th><th style="width:25%">Current</th><th style="width:25%">Last Check</th><th style="width:25%">Goal</th></tr>
      {skill_rows}
    </table>
    <div class="note-section">
      <div class="note-label">Overall Assessment</div>
      {note_lines(3)}
    </div>'''

    elif title == "Talent Discovery Journal":
        content = f'''
    <div class="tool-field">
      <span class="tool-field-label">Date:</span>
      <span class="tool-field-line"></span>
    </div>
    <div class="note-section">
      <div class="note-label">Sports Observed Today</div>
      {note_lines(2)}
    </div>
    <div class="note-section">
      <div class="note-label">What Came Naturally (Strengths I Noticed)</div>
      {note_lines(4)}
    </div>
    <div class="note-section">
      <div class="note-label">What Needed Extra Effort (Areas to Develop)</div>
      {note_lines(4)}
    </div>
    <div class="note-section">
      <div class="note-label">My Child's Reactions &amp; Enthusiasm Level (1-5)</div>
      {note_lines(3)}
    </div>
    <div class="note-section">
      <div class="note-label">Next Steps &amp; Activities to Try</div>
      {note_lines(4)}
    </div>'''

    else:
        content = note_lines(25)

    return f'''<div class="page">
  {page_header("Tools &amp; Resources", title)}
  <div class="tool-title" style="color:#333">{html_mod.escape(title)}</div>
  <div class="tool-desc">{html_mod.escape(desc)}</div>
  {content}
  {footer(data["book_title"])}
</div>'''


def build_note_page(data, note_num):
    page_counter[0] += 1
    return f'''<div class="page">
  {page_header("Notes", "")}
  <div class="note-page-title">Notes</div>
  {note_lines(25)}
  {footer(data["book_title"])}
</div>'''


# ============================================================
# MAIN
# ============================================================
def main():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    pages = []

    # 1. Title page
    pages.append(build_title_page(data))

    # 2. Table of Contents
    pages.append(build_toc(data))

    # 3. Sections
    for sec in data["sections"]:
        # Divider
        pages.append(build_divider(sec, data))
        # Topics
        is_sport = (sec["id"] == 3)
        for topic in sec["topics"]:
            pages.append(build_topic_page(topic, sec, data, is_sport=is_sport))

    # 4. Tools
    tools = data.get("tools", [])
    for i, tool in enumerate(tools):
        pages.append(build_tool_page(tool, i, len(tools), data))

    # 5. Note pages
    note_count = data.get("note_page_count", 5)
    for i in range(note_count):
        pages.append(build_note_page(data, i+1))

    # Assemble HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{html_mod.escape(data["book_title"])} — {html_mod.escape(data.get("version",""))}</title>
<style>
{build_css()}
</style>
</head>
<body>
{''.join(pages)}
</body>
</html>'''

    with open(HTML_FILE, "w") as f:
        f.write(html)

    total_pages = page_counter[0]
    print(f"Generated: {HTML_FILE}")
    print(f"Total pages: {total_pages}")


if __name__ == "__main__":
    main()
