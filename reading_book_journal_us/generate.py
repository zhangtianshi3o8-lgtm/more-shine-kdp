#!/usr/bin/env python3
"""
Reading & Book Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Avid readers, book club members, lifelong learners
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "reading_book_journal_us_V1.0.html")

BOOK_TITLE = "Reading & Book Journal"
BOOK_SUBTITLE = "Track Every Book You Read and Every Story You Love"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

# ============================================================
# CSS — Moleskine luxury: charcoal #161616 + gold #C4A04A
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
  padding: 0.45in 0.5in 0.38in 0.5in;
  page-break-after: always;
  position: relative;
  background: white;
  overflow: hidden;
}
.page:last-child { page-break-after: auto; }

@media screen { .page { border: 1px dashed #ccc; margin: 8px auto; } }
@media print  { .page { border: none; margin: 0; } }

/* ================ COVER (INTERIOR TITLE PAGE) ================ */
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
  opacity: 0.06;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #C4A04A, transparent),
    radial-gradient(ellipse 24px 15px at 10% 55%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 90% 40%, #C4A04A, transparent),
    radial-gradient(ellipse 16px 10px at 40% 90%, #C4A04A, transparent);
}

.cover .icon-wrap {
  width: 120px; height: 120px;
  position: relative;
  margin: 0 auto 16px;
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 28pt;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.15;
  letter-spacing: 0.5pt;
  text-shadow: 2px 2px 6px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 110px; height: 2.5px;
  background: #C4A04A;
  margin: 14px auto;
}

.cover .subtitle {
  font-size: 11pt;
  color: #D4B896;
  font-style: italic;
  line-height: 1.5;
  margin-bottom: 20px;
}

.cover .features {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.cover .feature-badge {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(196,160,74,0.4);
  color: #C4A04A;
  font-size: 7pt;
  font-weight: 700;
  letter-spacing: 0.5pt;
  padding: 4px 9px;
  border-radius: 3px;
  text-transform: uppercase;
}

.cover .tagline {
  font-size: 8.5pt;
  color: #D4B896;
  letter-spacing: 2pt;
  text-transform: uppercase;
  margin-top: 8px;
}

.cover .publisher {
  position: absolute;
  bottom: 0.4in;
  left: 0; right: 0;
  text-align: center;
  font-size: 9pt;
  color: #C4A04A;
  letter-spacing: 2pt;
  text-transform: uppercase;
  font-weight: 700;
}

/* ================ SECTION DIVIDER ================ */
.divider {
  width: 6in; height: 9in;
  page-break-after: always;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  background: linear-gradient(165deg, #161616 0%, #1E1E1E 50%, #161616 100%);
  position: relative;
  overflow: hidden;
}

.divider .div-glow {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 25px 15px at 80% 30%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 13px at 70% 75%, #C4A04A, transparent),
    radial-gradient(ellipse 18px 11px at 25% 85%, #C4A04A, transparent);
}

.divider .div-num {
  font-size: 60pt;
  color: rgba(196,160,74,0.12);
  font-weight: 700;
  position: absolute;
  top: 1in;
}

.divider .div-label {
  font-size: 10pt;
  color: #C4A04A;
  letter-spacing: 3pt;
  text-transform: uppercase;
  margin-bottom: 10px;
  position: relative;
}

.divider .div-title {
  font-size: 24pt;
  color: #ffffff;
  font-weight: 700;
  line-height: 1.2;
  position: relative;
  padding: 0 0.6in;
}

.divider .div-sub {
  font-size: 11pt;
  color: #D4B896;
  font-style: italic;
  margin-top: 14px;
  position: relative;
}

/* ================ CONTENT PAGES ================ */
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 7.5pt;
  color: #999;
  padding-bottom: 4px;
  border-bottom: 1.5px solid #C4A04A;
  margin-bottom: 14px;
}
.section-header .sh-left {
  font-weight: 700;
  letter-spacing: 0.8pt;
  color: #161616;
  text-transform: uppercase;
}
.section-header .sh-right { color: #aaa; }

.page-footer {
  position: absolute;
  bottom: 0.22in;
  left: 0.5in; right: 0.5in;
  font-size: 6.5pt;
  color: #bbb;
  display: flex;
  justify-content: space-between;
  border-top: 0.5px solid #eee;
  padding-top: 3px;
}

.page-title {
  font-size: 14pt;
  font-weight: 700;
  color: #161616;
  margin-bottom: 3px;
}

.page-subtitle {
  font-size: 8pt;
  color: #888;
  font-style: italic;
  margin-bottom: 12px;
}

.wline {
  border-bottom: 0.5px solid #ccc;
  height: 22px;
  margin-bottom: 2px;
}
.wline-sm {
  border-bottom: 0.5px solid #ddd;
  height: 18px;
  margin-bottom: 1px;
}

table.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
}
table.data-table th {
  background: #C4A04A;
  color: white;
  font-weight: 700;
  text-align: left;
  padding: 4px 5px;
  font-size: 7pt;
  letter-spacing: 0.3pt;
  text-transform: uppercase;
}
table.data-table td {
  padding: 4px 5px;
  border-bottom: 0.5px solid #ddd;
  vertical-align: top;
}
table.data-table tr:nth-child(even) td { background: #FAF6F0; }

.check-row {
  display: flex;
  flex-wrap: wrap;
  gap: 5px 10px;
  font-size: 8pt;
  color: #555;
  align-items: center;
}
.check-row .check-item {
  display: inline-flex;
  align-items: center;
  gap: 3px;
}
.check-box {
  width: 10px; height: 10px;
  border: 1px solid #888;
  border-radius: 2px;
  display: inline-block;
}

.info-box {
  background: #FAF6F0;
  border-left: 3px solid #C4A04A;
  padding: 8px 10px;
  margin-bottom: 10px;
  font-size: 8pt;
  color: #333;
  line-height: 1.5;
}
.info-box .info-title {
  font-weight: 700;
  color: #161616;
  font-size: 8.5pt;
  margin-bottom: 4px;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
}

.stars {
  font-size: 13pt;
  color: #ccc;
  letter-spacing: 2pt;
}

.stat-card {
  text-align: center;
  padding: 6px 4px;
  background: #FAF6F0;
  border-radius: 4px;
  border: 1px solid #E8DCC8;
}
.stat-card .stat-label {
  font-size: 6.5pt;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  margin-bottom: 2px;
}
.stat-card .stat-value {
  font-size: 11pt;
  font-weight: 700;
  color: #161616;
}

.field-row {
  display: flex;
  gap: 8px;
  align-items: baseline;
}
.field-label {
  font-size: 7pt;
  font-weight: 700;
  color: #161616;
  text-transform: uppercase;
  letter-spacing: 0.4pt;
  white-space: nowrap;
  min-width: 54px;
}
.field-line {
  flex: 1;
  border-bottom: 0.5px solid #bbb;
  height: 14px;
}
"""

# ============================================================
# PAGE BUILDERS
# ============================================================

def cover_page():
    return f'''
<!-- Page {pn()}: Cover -->
<div class="cover">
  <div class="glow-bg"></div>
  <div class="icon-wrap">
    <svg viewBox="0 0 120 120" width="120" height="120" xmlns="http://www.w3.org/2000/svg">
      <!-- Open book outline -->
      <path d="M 10 30 L 10 90 Q 10 92 12 92 L 58 92 Q 60 92 60 90 L 60 30 Q 60 28 58 28 L 14 28 Q 10 28 10 30 Z"
        stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.06)"/>
      <!-- Right page -->
      <path d="M 60 30 L 60 90 Q 60 92 62 92 L 108 92 Q 110 92 110 90 L 110 30 Q 110 28 108 28 L 62 28 Q 60 28 60 30 Z"
        stroke="#C4A04A" stroke-width="1.5" fill="rgba(196,160,74,0.06)"/>
      <!-- Spine -->
      <line x1="60" y1="28" x2="60" y2="92" stroke="#C4A04A" stroke-width="2" opacity="0.6"/>
      <!-- Text lines left -->
      <line x1="18" y1="42" x2="52" y2="42" stroke="#C4A04A" stroke-width="0.7" opacity="0.3"/>
      <line x1="18" y1="50" x2="50" y2="50" stroke="#C4A04A" stroke-width="0.7" opacity="0.3"/>
      <line x1="18" y1="58" x2="52" y2="58" stroke="#C4A04A" stroke-width="0.7" opacity="0.3"/>
      <line x1="18" y1="66" x2="46" y2="66" stroke="#C4A04A" stroke-width="0.7" opacity="0.3"/>
      <line x1="18" y1="74" x2="52" y2="74" stroke="#C4A04A" stroke-width="0.7" opacity="0.3"/>
      <line x1="18" y1="82" x2="48" y2="82" stroke="#C4A04A" stroke-width="0.7" opacity="0.3"/>
      <!-- Text lines right -->
      <line x1="68" y1="42" x2="102" y2="42" stroke="#C4A04A" stroke-width="0.7" opacity="0.3"/>
      <line x1="68" y1="50" x2="100" y2="50" stroke="#C4A04A" stroke-width="0.7" opacity="0.3"/>
      <line x1="68" y1="58" x2="102" y2="58" stroke="#C4A04A" stroke-width="0.7" opacity="0.3"/>
      <line x1="68" y1="66" x2="96" y2="66" stroke="#C4A04A" stroke-width="0.7" opacity="0.3"/>
      <line x1="68" y1="74" x2="102" y2="74" stroke="#C4A04A" stroke-width="0.7" opacity="0.3"/>
      <line x1="68" y1="82" x2="98" y2="82" stroke="#C4A04A" stroke-width="0.7" opacity="0.3"/>
      <!-- Bookmark ribbon -->
      <path d="M 80 28 L 80 50 L 84 46 L 88 50 L 88 28 Z" stroke="#C4A04A" stroke-width="1" fill="rgba(196,160,74,0.2)"/>
    </svg>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">50 Book Reviews</span>
      <span class="feature-badge">Reading List</span>
      <span class="feature-badge">Book Club</span>
      <span class="feature-badge">Year in Review</span>
    </div>
    <div class="tagline">For Readers, Thinkers &amp; Story Lovers</div>
  </div>
  <div class="publisher">More Shine Press</div>
</div>
'''


def owner_page():
    return f'''
<!-- Page {pn()}: Owner -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">This Book Belongs To</span>
    <span class="sh-right"></span>
  </div>

  <div style="height: 2.5in;"></div>

  <div style="text-align: center; margin-bottom: 30px;">
    <div style="font-size: 16pt; font-weight: 700; color: #161616; margin-bottom: 6px;">This Journal Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #161616; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Genre</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Book of All Time</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Reading Goal This Year</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">My Reading Motto</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Reading &amp; Book Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def how_to_use():
    return f'''
<!-- Page {pn()}: How to Use -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Getting Started</span>
    <span class="sh-right">More Shine Press</span>
  </div>

  <div class="page-title">How to Use This Journal</div>
  <div class="page-subtitle">Make every book an experience worth remembering</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Reading Journal?</div>
    A reading journal transforms books from fleeting experiences into a lasting personal library of thought. It helps you remember what you read, discover patterns in your taste, track your growth as a reader, and build a list of recommendations you can share with friends for years to come.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Tips for Better Reading</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Write while it's fresh.</strong> Record your thoughts within a day or two of finishing. The emotions and impressions fade quickly &mdash; capture them while the story still lives in your mind.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Note your favorite quotes.</strong> Copy passages that moved you. Years later, these quotes become a map of who you were and what mattered to you at each stage of life.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Track patterns.</strong> Over time, your journal reveals what genres, themes, and authors you truly love &mdash; not just what you think you should read.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Rate honestly.</strong> Don't feel pressured to love a book because others did. Your honest rating helps you choose better books in the future.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Set a goal.</strong> Whether it is 12 books a year or 100, a reading goal creates momentum. Use the tracker pages to stay motivated.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Reading Tip:</strong> Keep a small notebook or app handy while reading to jot down page numbers and quotes. Transfer them to this journal when you finish.
  </div>

  <div class="page-footer">
    <span>Reading &amp; Book Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def genre_guide():
    genres = [
        ("Literary Fiction", "Character-driven stories exploring the human condition. Rich prose, complex themes. Think Toni Morrison, Kazuo Ishiguro, Marilynne Robinson."),
        ("Mystery &amp; Thriller", "Suspenseful plots with puzzles, crime, and tension. From cozy mysteries to psychological thrillers. Agatha Christie, Gillian Flynn, Tana French."),
        ("Science Fiction", "Speculative futures, alternate realities, technology. Hard sci-fi to space opera. Isaac Asimov, Ursula K. Le Guin, Andy Weir."),
        ("Fantasy", "Imagined worlds with magic, mythology, and epic quests. Brandon Sanderson, N.K. Jemisin, Patrick Rothfuss."),
        ("Historical Fiction", "Stories set in the past, blending fact with fiction. Hilary Mantel, Anthony Doerr, Kristin Hannah."),
        ("Romance", "Love stories with emotional journeys and happy endings. Emily Henry, Colleen Hoover, Tessa Dare."),
        ("Nonfiction &amp; Memoir", "True stories, essays, and explorations of real life. Tara Westover, Michelle Obama, David Sedaris."),
        ("Biography &amp; History", "Lives of notable figures and events that shaped the world. Walter Isaacson, Erik Larson, Doris Kearns Goodwin."),
        ("Self-Help &amp; Growth", "Practical wisdom for personal development. James Clear, Bren&eacute; Brown, Atomic Habits."),
        ("Poetry &amp; Essays", "Verses and reflections that distill experience into language. Mary Oliver, Amanda Gorman, Joan Didion."),
    ]

    rows = ""
    for genre, desc in genres:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 95px; font-size: 8pt; font-weight: 700; color: #161616;">{genre}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Genre Guide -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Genre Guide</span>
  </div>

  <div class="page-title">Genre Guide</div>
  <div class="page-subtitle">Explore new worlds of reading</div>

  {rows}

  <div class="page-footer">
    <span>Reading &amp; Book Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def reading_goal_tracker():
    """Annual reading goal progress page"""
    return f'''
<!-- Page {pn()}: Reading Goal -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reading Goal</span>
    <span class="sh-right">Annual Progress</span>
  </div>

  <div class="page-title">Reading Goal Tracker</div>
  <div class="page-subtitle">Set your target and watch it grow</div>

  <div style="background: #FAF6F0; border: 1px solid #E8DCC8; border-radius: 4px; padding: 10px; margin-bottom: 14px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
      <div style="display:flex;align-items:baseline;gap:4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; min-width: 54px;">Goal</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:16px;"></div>
        <span style="font-size:7pt;color:#888;">books</span>
      </div>
      <div style="display:flex;align-items:baseline;gap:4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; min-width: 54px;">Year</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:16px;"></div>
      </div>
    </div>
  </div>

  <!-- 50-book progress grid (5x10) -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Mark each book as you finish &mdash; 50 Book Goal</div>
  <div style="display: grid; grid-template-columns: repeat(10, 1fr); gap: 6px; margin-bottom: 14px;">
    {''.join(f'<div style="aspect-ratio:1;border:1.5px solid #C4A04A;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:7pt;color:#C4A04A;font-weight:700;">{i}</div>' for i in range(1,51))}
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Monthly Progress</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr><th>Month</th><th style="width:40px;">Read</th><th style="width:40px;">Goal</th><th>Books Completed</th></tr>
    <tr><td style="font-weight:700;">January</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;">February</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;">March</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;">April</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;">May</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;">June</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;">July</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;">August</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;">September</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;">October</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;">November</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;">December</td><td></td><td></td><td></td></tr>
  </table>

  <div class="page-footer">
    <span>Reading &amp; Book Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def divider_section(num, label, title, subtitle):
    labels = ["One", "Two", "Three", "Four", "Five", "Six", "Seven"]
    label_text = labels[num-1] if num <= 7 else label
    return f'''
<!-- Page {pn()}: Divider -->
<div class="divider">
  <div class="div-glow"></div>
  <div class="div-num">{num:02d}</div>
  <div class="div-label">Part {label_text}</div>
  <div class="div-title">{title}</div>
  <div class="div-sub">{subtitle}</div>
</div>
'''


def book_review_left(entry_num):
    """Left page: book info + rating"""
    return f'''
<!-- Page {pn()}: Book {entry_num} Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Book #{entry_num:02d}</span>
    <span class="sh-right">Reading &amp; Book Journal</span>
  </div>

  <div class="page-title">Book #{entry_num:02d}</div>
  <div class="page-subtitle">Book Details &amp; First Impressions</div>

  <!-- Book Info -->
  <div style="background: #FAF6F0; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Title</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px; grid-column: span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Author</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Genre</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Pages</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Publisher</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 36px;">Year</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Started</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Finished</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Format</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
      <div style="display: flex; align-items: baseline; gap: 4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 54px;">Source</span>
        <div style="flex:1; border-bottom: 0.5px solid #aaa; height: 14px;"></div>
      </div>
    </div>
  </div>

  <!-- Format -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Format</div>
  <div class="check-row" style="margin-bottom: 10px;">
    <span class="check-item"><span class="check-box"></span> Hardcover</span>
    <span class="check-item"><span class="check-box"></span> Paperback</span>
    <span class="check-item"><span class="check-box"></span> eBook</span>
    <span class="check-item"><span class="check-box"></span> Audiobook</span>
    <span class="check-item"><span class="check-box"></span> Library</span>
  </div>

  <!-- Rating -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Overall Rating</div>
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
    <span class="stars">&starf; &starf; &starf; &starf; &starf;</span>
  </div>

  <!-- Quick Ratings -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Rate Each Aspect (1&ndash;5 stars)</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px 14px; font-size: 7.5pt;">
    <div style="display:flex;justify-content:space-between;border-bottom:0.5px solid #ddd;padding-bottom:3px;margin-bottom:2px;">
      <span style="color:#555;">Plot</span>
      <span style="color:#ccc;letter-spacing:1pt;">&starf;&starf;&starf;&starf;&starf;</span>
    </div>
    <div style="display:flex;justify-content:space-between;border-bottom:0.5px solid #ddd;padding-bottom:3px;margin-bottom:2px;">
      <span style="color:#555;">Characters</span>
      <span style="color:#ccc;letter-spacing:1pt;">&starf;&starf;&starf;&starf;&starf;</span>
    </div>
    <div style="display:flex;justify-content:space-between;border-bottom:0.5px solid #ddd;padding-bottom:3px;margin-bottom:2px;">
      <span style="color:#555;">Writing Style</span>
      <span style="color:#ccc;letter-spacing:1pt;">&starf;&starf;&starf;&starf;&starf;</span>
    </div>
    <div style="display:flex;justify-content:space-between;border-bottom:0.5px solid #ddd;padding-bottom:3px;margin-bottom:2px;">
      <span style="color:#555;">Pacing</span>
      <span style="color:#ccc;letter-spacing:1pt;">&starf;&starf;&starf;&starf;&starf;</span>
    </div>
    <div style="display:flex;justify-content:space-between;border-bottom:0.5px solid #ddd;padding-bottom:3px;margin-bottom:2px;">
      <span style="color:#555;">Emotional Impact</span>
      <span style="color:#ccc;letter-spacing:1pt;">&starf;&starf;&starf;&starf;&starf;</span>
    </div>
    <div style="display:flex;justify-content:space-between;border-bottom:0.5px solid #ddd;padding-bottom:3px;margin-bottom:2px;">
      <span style="color:#555;">Would Recommend</span>
      <span style="color:#ccc;letter-spacing:1pt;">&starf;&starf;&starf;&starf;&starf;</span>
    </div>
  </div>

  <div class="page-footer">
    <span>Book #{entry_num:02d} &mdash; Details</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def book_review_right(entry_num):
    """Right page: review, quotes, notes"""
    return f'''
<!-- Page {pn()}: Book {entry_num} Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Book #{entry_num:02d}</span>
    <span class="sh-right">Review &amp; Reflections</span>
  </div>

  <div class="page-title">Review #{entry_num:02d}</div>
  <div class="page-subtitle">Thoughts, quotes, and takeaways</div>

  <!-- Summary -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">My Summary (No Spoilers)</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Favorite Quotes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 4px;">Favorite Quotes</div>
  <div style="display: grid; grid-template-columns: 1fr; gap: 2px;">
    <div style="border-bottom:0.5px solid #ddd;height:18px;font-size:6.5pt;color:#aaa;padding-right:4px;">Page ___:</div>
    <div class="wline-sm"></div>
    <div style="border-bottom:0.5px solid #ddd;height:18px;font-size:6.5pt;color:#aaa;padding-right:4px;">Page ___:</div>
    <div class="wline-sm"></div>
    <div style="border-bottom:0.5px solid #ddd;height:18px;font-size:6.5pt;color:#aaa;padding-right:4px;">Page ___:</div>
    <div class="wline-sm"></div>
  </div>

  <!-- Characters -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 4px;">Memorable Characters</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Themes -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 4px;">Themes &amp; Takeaways</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Full Review -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 4px;">My Full Review</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Recommendation -->
  <div class="check-row" style="margin-top: 10px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Would Recommend</span>
    <span class="check-item"><span class="check-box"></span> Would Re-read</span>
    <span class="check-item"><span class="check-box"></span> New Favorite</span>
    <span class="check-item"><span class="check-box"></span> Book Club Pick</span>
  </div>

  <div class="page-footer">
    <span>Book #{entry_num:02d} &mdash; Review</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def book_log(page_of, total_pages):
    """Quick book log — one-line-per-book summary table"""
    return f'''
<!-- Page {pn()}: Book Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Quick Book Log</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Quick Book Log</div>
  <div class="page-subtitle">A bird's-eye view of everything you've read</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Title &amp; Author</th>
      <th style="width:50px;">Genre</th>
      <th style="width:36px;">Date</th>
      <th style="width:30px;">Rating</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Rating: 1&ndash;5 (5 = loved it)</div>

  <div class="page-footer">
    <span>Reading &amp; Book Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def reading_list(page_of, total_pages):
    """To-be-read wishlist"""
    return f'''
<!-- Page {pn()}: Reading List -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">To Be Read</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Reading Wishlist</div>
  <div class="page-subtitle">Books you can't wait to read</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Title &amp; Author</th>
      <th style="width:52px;">Genre</th>
      <th style="width:36px;">Priority</th>
      <th style="width:22px;">&#10003;</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">13</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">14</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">15</td><td></td><td></td><td></td><td style="text-align:center;"><span class="check-box"></span></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Priority: H = High, M = Medium, L = Low</div>

  <div class="page-footer">
    <span>Reading &amp; Book Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def book_club_log():
    """Book club meeting tracker"""
    return f'''
<!-- Page {pn()}: Book Club -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Book Club</span>
    <span class="sh-right">Meeting Notes</span>
  </div>

  <div class="page-title">Book Club Tracker</div>
  <div class="page-subtitle">Record your book club meetings and discussions</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Book &amp; Author</th>
      <th style="width:50px;">Date</th>
      <th>Host / Location</th>
      <th style="width:28px;">&#10003;</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="margin-top: 12px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Discussion Highlights</div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
  </div>

  <div class="page-footer">
    <span>Reading &amp; Book Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def year_review():
    """Year-end reading review"""
    return f'''
<!-- Page {pn()}: Year Review -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Year in Review</span>
    <span class="sh-right">Reflect on Your Reading</span>
  </div>

  <div class="page-title">Reading Year in Review</div>
  <div class="page-subtitle">Celebrate your reading journey</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="stat-card" style="text-align:center;padding:10px 6px;">
      <div class="stat-label">Books Read</div>
      <div class="stat-value" style="font-size: 16pt;"></div>
    </div>
    <div class="stat-card" style="text-align:center;padding:10px 6px;">
      <div class="stat-label">Pages Read</div>
      <div class="stat-value" style="font-size: 16pt;"></div>
    </div>
    <div class="stat-card" style="text-align:center;padding:10px 6px;">
      <div class="stat-label">New Authors</div>
      <div class="stat-value" style="font-size: 16pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Top 5 Books This Year</div>
  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Title &amp; Author</th>
      <th style="width:40px;">Rating</th>
      <th>Why It Stood Out</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 6px;">Personal Discoveries</div>
  <table class="data-table" style="font-size: 8pt;">
    <tr><th>Category</th><th>Winner</th></tr>
    <tr><td style="font-weight:700;color:#161616;">Favorite Genre</td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Favorite Author</td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Surprise</td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Biggest Disappointment</td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best New Discovery</td><td></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 14px; margin-bottom: 4px;">Reading Goals for Next Year</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Reading &amp; Book Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def notes_page(page_num):
    lines = ""
    for _ in range(18):
        lines += '<div class="wline"></div>\n'

    return f'''
<!-- Page {pn()}: Notes -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Notes</span>
    <span class="sh-right"></span>
  </div>

  <div class="page-title">Reading Notes</div>
  <div class="page-subtitle">Ideas, reflections, and book recommendations</div>

  {lines}

  <div class="page-footer">
    <span>Reading &amp; Book Journal</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


# ============================================================
# MAIN
# ============================================================
def main():
    pages = []

    # ---- Front Matter ----
    pages.append(cover_page())                          # 1: Cover
    pages.append(owner_page())                           # 2: Owner page

    # ---- Reference Section ----
    pages.append(how_to_use())                           # 3: How to use
    pages.append(genre_guide())                          # 4: Genre guide
    pages.append(reading_goal_tracker())                 # 5: Reading goal

    # ---- Section 1: Book Reviews ----
    pages.append(divider_section(1, "One", "Book Reviews", "50 books &mdash; detailed reviews and reflections"))
    NUM_BOOKS = 50
    for i in range(1, NUM_BOOKS + 1):
        pages.append(book_review_left(i))
        pages.append(book_review_right(i))

    # ---- Section 2: Quick Book Log ----
    pages.append(divider_section(2, "Two", "Quick Book Log", "Your reading at a glance"))
    pages.append(book_log(1, 3))
    pages.append(book_log(2, 3))
    pages.append(book_log(3, 3))

    # ---- Section 3: Reading List ----
    pages.append(divider_section(3, "Three", "Reading Wishlist", "Books you can't wait to read"))
    pages.append(reading_list(1, 2))
    pages.append(reading_list(2, 2))

    # ---- Section 4: Book Club ----
    pages.append(divider_section(4, "Four", "Book Club", "Track your meetings and discussions"))
    pages.append(book_club_log())

    # ---- Section 5: Year in Review ----
    pages.append(divider_section(5, "Five", "Year in Review", "Celebrate your reading journey"))
    pages.append(year_review())

    # ---- Section 6: Notes ----
    pages.append(divider_section(6, "Six", "Notes", "Ideas, reflections, and recommendations"))
    for i in range(6):
        pages.append(notes_page(i + 1))

    # Assemble HTML
    body_content = "\n".join(pages)
    total_pages = page_no[0]

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{BOOK_TITLE} &mdash; More Shine Press</title>
<style>{CSS}</style>
</head>
<body>
{body_content}
</body>
</html>'''

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Generated: {HTML_FILE}")
    print(f"Total pages: {total_pages}")

    print(f"\nPage breakdown:")
    print(f"  Cover: 1")
    print(f"  Owner page: 1")
    print(f"  Reference (how-to, genres, goal tracker): 3")
    print(f"  Section dividers: 6")
    print(f"  Book reviews ({NUM_BOOKS} x 2): {NUM_BOOKS * 2}")
    print(f"  Quick book log: 3")
    print(f"  Reading wishlist: 2")
    print(f"  Book club: 1")
    print(f"  Year review: 1")
    print(f"  Notes pages: 6")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
