#!/usr/bin/env python3
"""
Genealogy Research Log Book -- KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Family historians, genealogy researchers
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "genealogy_research_log_us_V1.0.html")

BOOK_TITLE = "Genealogy Research Log Book"
BOOK_SUBTITLE = "Trace Every Ancestor, Every Record, Every Story"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

def nl(n):
    return "\n".join('<div class="notes-line"></div>' for _ in range(n))

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
@media print { .page { border: none; margin: 0; } }

/* ================ INTERIOR TITLE PAGE ================ */
.cover {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(165deg, #1A1520 0%, #2A1F30 30%, #1A1520 65%, #100A14 100%);
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #8B6B3E, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #8B6B3E, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #8B6B3E, transparent);
}

.cover .title-main {
  font-size: 28pt;
  font-weight: 700;
  color: #FAF6F0;
  line-height: 1.2;
  letter-spacing: 0.5pt;
  position: relative;
  z-index: 2;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 100px; height: 2px;
  background: #8B6B3E;
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
  color: #8B6B3E;
  text-transform: uppercase;
  letter-spacing: 1pt;
  font-weight: 700;
}

.page-header .ph-right {
  font-size: 8pt;
  color: #999;
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
  color: #1A1520;
  letter-spacing: 0.5pt;
  text-transform: uppercase;
}

.section-line {
  flex: 1;
  height: 1px;
  background: #8B6B3E;
  margin: 0 12px;
  opacity: 0.4;
}

/* ================ HOW TO USE ================ */
.howto-text { font-size: 10pt; line-height: 1.7; }
.howto-text p { margin-bottom: 8px; }
.howto-text .ht-title {
  font-size: 11pt; font-weight: 700; color: #1A1520;
  margin-bottom: 4px; margin-top: 6px;
}
.howto-text .ht-icon { color: #8B6B3E; font-weight: 700; margin-right: 4px; }

/* ================ INFO FIELDS ================ */
.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
  margin-bottom: 8px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #8B6B3E;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  display: block;
  margin-bottom: 1px;
}

.info-field .if-write {
  height: 16px;
  border-bottom: 1px dotted #ccc;
}

/* ================ PERSON TABLE ================ */
.person-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
}

.person-table th {
  font-size: 6.5pt;
  color: #8B6B3E;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 5px 3px;
  border-bottom: 1.5px solid #8B6B3E;
  text-align: center;
}

.person-table th:first-child { text-align: left; }

.person-table td {
  padding: 4px 3px;
  border-bottom: 1px solid #eee;
  height: 24px;
  font-size: 9pt;
}

/* ================ WRITE BOX ================ */
.write-box {
  border: 1px solid #C4A04A;
  border-radius: 3px;
  padding: 6px 8px;
  margin-bottom: 8px;
}

.write-box .wb-label {
  font-size: 7pt;
  color: #8B6B3E;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 3px;
}

.write-box .wb-area {
  height: 28px;
}

/* ================ RESEARCH BANNER ================ */
.research-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1.5px solid #8B6B3E;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.research-banner .rb-num {
  display: inline-block;
  border: 1.5px solid #8B6B3E;
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 8pt;
  color: #8B6B3E;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.research-banner .rb-label {
  font-size: 8pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.research-banner .rb-line {
  flex: 1;
  height: 12px;
  border-bottom: 1px dotted #ccc;
}

/* ================ RECORD TABLE ================ */
.record-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 8px;
}

.record-table th {
  font-size: 6pt;
  color: #8B6B3E;
  text-transform: uppercase;
  padding: 4px 2px;
  border-bottom: 1.5px solid #8B6B3E;
  text-align: center;
}

.record-table th:first-child { text-align: left; }

.record-table td {
  padding: 3px 2px;
  border-bottom: 1px solid #eee;
  height: 20px;
  font-size: 8.5pt;
}

/* ================ NOTES ================ */
.notes-line { border-bottom: 1px solid #ddd; height: 22px; }

/* ================ FINAL PAGE ================ */
.final-page {
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  text-align: center; height: 100%;
}
.final-page .fp-text {
  font-size: 12pt; color: #999; font-style: italic;
  line-height: 1.8; margin-bottom: 20px;
}
.final-page .fp-logo {
  font-size: 11pt; color: #C4A04A;
  letter-spacing: 2.5pt; text-transform: uppercase;
  font-weight: 700;
}
.final-page .fp-line {
  width: 60px; height: 1.5px; background: #8B6B3E;
  margin: 12px auto; opacity: 0.5;
}
"""


def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- Tree icon -->
      <g transform="translate(50,50)">
        <!-- Trunk -->
        <rect x="-3" y="10" width="6" height="28" rx="1" fill="#8B6B3E" opacity="0.5"/>
        <!-- Branches -->
        <line x1="0" y1="10" x2="0" y2="-30" stroke="#8B6B3E" stroke-width="2"/>
        <line x1="0" y1="-5" x2="-18" y2="-20" stroke="#8B6B3E" stroke-width="1.5"/>
        <line x1="0" y1="-5" x2="18" y2="-20" stroke="#8B6B3E" stroke-width="1.5"/>
        <line x1="0" y1="-15" x2="-14" y2="-32" stroke="#8B6B3E" stroke-width="1.2"/>
        <line x1="0" y1="-15" x2="14" y2="-32" stroke="#8B6B3E" stroke-width="1.2"/>
        <!-- Nodes -->
        <circle cx="0" cy="-30" r="5" fill="#8B6B3E" opacity="0.7"/>
        <circle cx="-18" cy="-20" r="4" fill="#8B6B3E" opacity="0.6"/>
        <circle cx="18" cy="-20" r="4" fill="#8B6B3E" opacity="0.6"/>
        <circle cx="-14" cy="-32" r="3" fill="#8B6B3E" opacity="0.5"/>
        <circle cx="14" cy="-32" r="3" fill="#8B6B3E" opacity="0.5"/>
        <circle cx="0" cy="10" r="4" fill="#8B6B3E" opacity="0.8"/>
      </g>
    </svg>
  </div>

  <div class="title-main">Genealogy<br>Research Log</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Trace Every Ancestor, Every Record, Every Story</div>

  <div class="pub">More Shine Press</div>
</div>""" % pn()


def how_to_use_page():
    pg = pn()
    return """<!-- PAGE %d: How to Use -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">How to Use This Log Book</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Family History Journal</div>
    <p>This log book helps you organize your genealogy research systematically.
    Track each ancestor, every source you consult, and every lead you follow.
    Over time, these pages become a permanent record of your family's story.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Research Pages</div>
    <p>Each ancestor gets a <strong>two-page spread</strong>. The left page
    captures vital statistics and family connections. The right page records
    your research sources, findings, and next steps.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips</div>
    <p>&#9679; <strong>Cite every source.</strong> Note archives, websites, book pages,
    and film numbers so you can find them again.</p>
    <p>&#9679; <strong>Record negative results.</strong> Knowing where you already
    looked saves repeating the same search.</p>
    <p>&#9679; <strong>Work backward in time.</strong> Start with yourself and go
    back one generation at a time.</p>
    <p>&#9679; <strong>Talk to relatives.</strong> Older family members are your
    most irreplaceable source.</p>
  </div>
</div>""" % (pg, pg)


def family_tree_page():
    pg = pn()
    return """<!-- PAGE %d: Family Tree Overview -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Family Tree Index</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Ancestor Index</div>
    <div class="section-line"></div>
  </div>

  <table class="person-table">
    <thead>
      <tr>
        <th>Name</th>
        <th>Born</th>
        <th>Died</th>
        <th>Birth Place</th>
        <th>Page</th>
      </tr>
    </thead>
    <tbody>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="write-box" style="border-color: #8B6B3E;">
    <div class="wb-label">Family Surnames Being Researched</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Key Regions / Countries of Origin</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def ancestor_left(entry_num):
    pg = pn()
    return """<!-- PAGE %d: Ancestor Left #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Ancestor Profile</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="research-banner">
    <span class="rb-num">Person #%03d</span>
    <span class="rb-label">Name:</span>
    <div class="rb-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Full Name at Birth</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Married / Other Names</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Date of Birth</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Place of Birth</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Date of Death</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Place of Death</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Date of Marriage</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Place of Marriage</span><div class="if-write"></div></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Spouse(s)</div>
    <div class="wb-area"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Father (Name / Birth)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Mother (Name / Birth)</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #8B6B3E;">
    <div class="wb-label">Children (Names / Birth Dates)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Occupation / Religion / Military Service</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, entry_num, pg, entry_num)


def ancestor_right():
    pg = pn()
    return """<!-- PAGE %d: Ancestor Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Research Sources &amp; Notes</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #8B6B3E; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">
    Records Searched
  </div>
  <table class="record-table">
    <thead>
      <tr>
        <th>Record Type</th>
        <th>Source / Archive</th>
        <th>Date Found</th>
        <th>Result</th>
      </tr>
    </thead>
    <tbody>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="write-box" style="border-color: #8B6B3E;">
    <div class="wb-label">Key Findings &amp; Discoveries</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Next Steps / To-Do</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #8B6B3E;">
    <div class="wb-label">Stories &amp; Family Memories</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>
</div>""" % (pg, pg)


def census_tracker_page():
    pg = pn()
    return """<!-- PAGE %d: Census Tracker -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Census Tracker</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Family: __________</div>
    <div class="section-line"></div>
  </div>

  <table class="record-table">
    <thead>
      <tr>
        <th>Census Year</th>
        <th>Location</th>
        <th>Age</th>
        <th>Occupation</th>
        <th>Film / Page</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>

  <div class="write-box">
    <div class="wb-label">Migration Path (Places Lived Over Time)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>
</div>""" % (pg, pg)


def notes_page():
    pg = pn()
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes</span>
    <span class="ph-right">Page %d</span>
  </div>
  <div>%s</div>
</div>""" % (pg, pg, nl(28))


def final_page():
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="page">
  <div class="final-page">
    <div class="fp-text">
      Every family has a story.<br>
      Every ancestor deserves to be remembered.<br>
      Keep searching. Keep recording.
    </div>
    <div class="fp-line"></div>
    <div class="fp-logo">More Shine Press</div>
    <div class="fp-line"></div>
  </div>
</div>""" % pg


def generate(output_path=HTML_FILE):
    pages = []
    pages.append(interior_title_page())
    pages.append(how_to_use_page())
    pages.append(family_tree_page())

    # 25 ancestor spreads (50 pages)
    for entry in range(1, 26):
        pages.append(ancestor_left(entry))
        pages.append(ancestor_right())
        if entry % 5 == 0:
            pages.append(census_tracker_page())

    # Census trackers (5 already added, add 3 more standalone)
    for _ in range(3):
        pages.append(census_tracker_page())

    # Notes (4 pages)
    for _ in range(4):
        pages.append(notes_page())

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
