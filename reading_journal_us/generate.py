#!/usr/bin/env python3
"""
Reading Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Avid readers, book club members, lifelong learners
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "reading_journal_us_V1.0.html")

BOOK_TITLE = "Reading Journal"
BOOK_SUBTITLE = "Track Every Book, Every Thought, Every Journey"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

def nl(n):
    return "\n".join('<div class="notes-line"></div>' for _ in range(n))

def stars():
    return " ".join('<span class="star">&#9734;</span>' for _ in range(5))

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

/* TITLE PAGE */
.cover {
  width: 6in; height: 9in; padding: 0;
  page-break-after: always;
  position: relative; overflow: hidden;
  background: linear-gradient(165deg, #0F0A1A 0%, #1A1228 30%, #0F0A1A 65%, #08050F 100%);
  display: flex; flex-direction: column;
  justify-content: center; align-items: center; text-align: center;
}
.cover .glow-bg {
  position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.06;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #7B6BA8, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #7B6BA8, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #7B6BA8, transparent);
}
.cover .title-main { font-size: 32pt; font-weight: 700; color: #FAF6F0; line-height: 1.2; letter-spacing: 1pt; position: relative; z-index: 2; text-shadow: 2px 2px 8px rgba(0,0,0,0.5); }
.cover .accent-bar { width: 100px; height: 2px; background: #7B6BA8; margin: 20px auto; position: relative; z-index: 2; }
.cover .subtitle { font-size: 12pt; color: #B8A8D8; font-style: italic; line-height: 1.5; position: relative; z-index: 2; }
.cover .pub { position: absolute; bottom: 0.6in; left: 0; right: 0; text-align: center; font-size: 9pt; color: #C4A04A; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; }

/* PAGE HEADER */
.page-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; padding-bottom: 4px; border-bottom: 0.5px solid #eee; }
.page-header .ph-left { font-size: 8pt; color: #7B6BA8; text-transform: uppercase; letter-spacing: 1pt; font-weight: 700; }
.page-header .ph-right { font-size: 8pt; color: #999; }

/* SECTION */
.section-header { display: flex; align-items: center; justify-content: center; margin-bottom: 14px; }
.section-title { font-size: 14pt; font-weight: 700; color: #0F0A1A; letter-spacing: 0.5pt; text-transform: uppercase; }
.section-line { flex: 1; height: 1px; background: #7B6BA8; margin: 0 12px; opacity: 0.4; }

/* BOOK LOG BANNER */
.book-banner { display: flex; align-items: center; gap: 8px; border-bottom: 1.5px solid #7B6BA8; padding-bottom: 5px; margin-bottom: 10px; }
.book-banner .bb-num { display: inline-block; border: 1.5px solid #7B6BA8; border-radius: 4px; padding: 3px 10px; font-size: 8pt; color: #7B6BA8; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt; }
.book-banner .bb-label { font-size: 8pt; color: #999; text-transform: uppercase; letter-spacing: 0.5pt; }
.book-banner .bb-line { flex: 1; height: 12px; border-bottom: 1px dotted #ccc; }

/* INFO FIELDS */
.info-row { display: grid; grid-template-columns: 1fr 1fr; gap: 6px 12px; margin-bottom: 8px; }
.info-field .if-label { font-size: 6.5pt; color: #7B6BA8; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; display: block; margin-bottom: 1px; }
.info-field .if-write { height: 16px; border-bottom: 1px dotted #ccc; }

/* WRITE BOX */
.write-box { border: 1px solid #7B6BA8; border-radius: 3px; padding: 6px 8px; margin-bottom: 8px; }
.write-box .wb-label { font-size: 7pt; color: #7B6BA8; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; margin-bottom: 3px; }
.write-box .wb-area { height: 24px; }

/* STARS */
.stars-row { display: flex; align-items: center; gap: 2px; margin-bottom: 8px; }
.stars-row .sr-label { font-size: 8pt; width: 60px; flex-shrink: 0; }
.star { font-size: 14pt; color: #7B6BA8; opacity: 0.4; }

/* CHECKBOXES */
.type-row { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 8px; }
.type-check { display: inline-flex; align-items: center; gap: 3px; font-size: 7.5pt; color: #555; }
.type-box { width: 10px; height: 10px; border: 1.5px solid #7B6BA8; border-radius: 2px; }

/* QUOTE BOX */
.quote-box { border-left: 3px solid #C4A04A; padding: 6px 10px; margin-bottom: 8px; background: #F8F5EE; }
.quote-box .qb-label { font-size: 7pt; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; margin-bottom: 3px; }
.quote-box .qb-area { height: 24px; }

/* GENRE CHECK */
.genre-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 3px 10px; margin-bottom: 8px; }

/* NOTES */
.notes-line { border-bottom: 1px solid #ddd; height: 22px; }

/* FINAL */
.final-page { display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; height: 100%; }
.final-page .fp-text { font-size: 12pt; color: #999; font-style: italic; line-height: 1.8; margin-bottom: 20px; }
.final-page .fp-logo { font-size: 11pt; color: #C4A04A; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; }
.final-page .fp-line { width: 60px; height: 1.5px; background: #7B6BA8; margin: 12px auto; opacity: 0.5; }

/* HOW-TO */
.howto-text { font-size: 10pt; line-height: 1.7; }
.howto-text p { margin-bottom: 8px; }
.howto-text .ht-title { font-size: 11pt; font-weight: 700; color: #0F0A1A; margin-bottom: 4px; margin-top: 6px; }
.howto-text .ht-icon { color: #7B6BA8; font-weight: 700; margin-right: 4px; }

/* TBR TABLE */
.tbr-table { width: 100%; border-collapse: collapse; }
.tbr-table th { font-size: 6.5pt; color: #7B6BA8; text-transform: uppercase; padding: 4px 3px; border-bottom: 1.5px solid #7B6BA8; text-align: left; }
.tbr-table td { padding: 4px 3px; border-bottom: 1px solid #eee; height: 22px; font-size: 8pt; }

/* STATS */
.stats-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 10px; }
.stat-box { border: 1px solid #7B6BA8; border-radius: 4px; padding: 8px; text-align: center; }
.stat-box .sb-num { font-size: 24pt; font-weight: 700; color: #7B6BA8; line-height: 1; }
.stat-box .sb-label { font-size: 7pt; color: #999; text-transform: uppercase; letter-spacing: 0.5pt; margin-top: 4px; }
"""


def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- Open book -->
      <path d="M 15 30 Q 15 26 19 26 L 45 26 Q 50 26 50 30 L 50 78 Q 50 74 45 74 L 19 74 Q 15 74 15 78 Z"
            stroke="#7B6BA8" stroke-width="1.5" fill="none"/>
      <path d="M 50 30 Q 50 26 55 26 L 81 26 Q 85 26 85 30 L 85 78 Q 85 74 81 74 L 55 74 Q 50 74 50 78 Z"
            stroke="#7B6BA8" stroke-width="1.5" fill="none"/>
      <!-- Page lines -->
      <line x1="20" y1="34" x2="44" y2="34" stroke="#7B6BA8" stroke-width="0.8" opacity="0.4"/>
      <line x1="20" y1="40" x2="44" y2="40" stroke="#7B6BA8" stroke-width="0.8" opacity="0.4"/>
      <line x1="20" y1="46" x2="40" y2="46" stroke="#7B6BA8" stroke-width="0.8" opacity="0.4"/>
      <line x1="56" y1="34" x2="80" y2="34" stroke="#7B6BA8" stroke-width="0.8" opacity="0.4"/>
      <line x1="56" y1="40" x2="80" y2="40" stroke="#7B6BA8" stroke-width="0.8" opacity="0.4"/>
      <line x1="56" y1="46" x2="76" y2="46" stroke="#7B6BA8" stroke-width="0.8" opacity="0.4"/>
      <!-- Spine center -->
      <line x1="50" y1="30" x2="50" y2="78" stroke="#C4A04A" stroke-width="1.2"/>
    </svg>
  </div>

  <div class="title-main">Reading Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Track Every Book, Every Thought, Every Journey</div>

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
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Reading Companion</div>
    <p>This journal is designed to be a faithful companion on your reading
    journey. Whether you read fiction or nonfiction, classics or thrillers,
    this book helps you capture what you read, what you thought about it,
    and what you want to read next.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Book Log</div>
    <p>Each book uses a <strong>single-page entry</strong>. Record the title, author,
    genre, dates, and page count. Rate the book with stars, write your
    favorite quotes, and capture your thoughts and takeaways.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips</div>
    <p>&#9679; <strong>Write while it's fresh.</strong> Jot notes as you read or right after finishing.</p>
    <p>&#9679; <strong>Note page numbers</strong> for quotes you want to revisit.</p>
    <p>&#9679; <strong>Rate honestly.</strong> Your future self will thank you for honest reviews.</p>
    <p>&#9679; <strong>Keep your TBR list</strong> updated so you never wonder "what's next?"</p>
  </div>
</div>""" % (pg, pg)


def book_log_page(entry_num):
    pg = pn()
    genres = ["Fiction", "Nonfiction", "Mystery", "Romance", "Sci-Fi", "Fantasy",
              "Thriller", "Biography", "History", "Self-Help", "Classic", "Other"]
    genre_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % g
        for g in genres
    )
    return """<!-- PAGE %d: Book Log #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Book Log</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="book-banner">
    <span class="bb-num">Book #%03d</span>
    <span class="bb-label">Title:</span>
    <div class="bb-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Author</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Pages</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Date Started</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Date Finished</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #7B6BA8; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Genre</div>
  <div class="type-row">%s</div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Format (Print / eBook / Audio)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Source (Bought / Library / Gift)</span><div class="if-write"></div></div>
  </div>

  <div class="stars-row">
    <span class="sr-label">Rating</span>
    %s
  </div>

  <div class="quote-box">
    <div class="qb-label">Favorite Quote(s) &mdash; Note Page #</div>
    <div class="qb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">My Thoughts &amp; Review</div>
    <div class="wb-area" style="height: 44px;"></div>
  </div>

  <div class="write-box" style="border-color: #C4A04A;">
    <div class="wb-label" style="color: #C4A04A;">Key Takeaway / What I Learned</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, entry_num, pg, entry_num, genre_html, stars())


def tbr_page():
    pg = pn()
    rows = ""
    for _ in range(14):
        rows += '<tr><td></td><td></td><td></td><td></td></tr>\n'
    return """<!-- PAGE %d: TBR -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">To Be Read (TBR) List</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">My Reading Wishlist</div>
    <div class="section-line"></div>
  </div>

  <table class="tbr-table">
    <thead>
      <tr>
        <th style="width: 30px;">Done</th>
        <th>Title &amp; Author</th>
        <th style="width: 80px;">Genre</th>
        <th style="width: 50px;">Priority</th>
      </tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>
</div>""" % (pg, pg, rows)


def yearly_stats_page():
    pg = pn()
    return """<!-- PAGE %d: Yearly Stats -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Yearly Reading Stats</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">My Year in Books: ______</div>
    <div class="section-line"></div>
  </div>

  <div class="stats-grid">
    <div class="stat-box"><div class="sb-num">&nbsp;</div><div class="sb-label">Books Read</div></div>
    <div class="stat-box"><div class="sb-num">&nbsp;</div><div class="sb-label">Total Pages</div></div>
    <div class="stat-box"><div class="sb-num">&nbsp;</div><div class="sb-label">Avg Rating</div></div>
    <div class="stat-box"><div class="sb-num">&nbsp;</div><div class="sb-label">New Authors</div></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Favorite Book of the Year</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Biggest Surprise</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #C4A04A;">
    <div class="wb-label" style="color: #C4A04A;">Reading Goal for Next Year</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Genres Explored / New Favorites</div>
    <div class="wb-area"></div>
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
      A reader lives a thousand lives<br>
      before he dies.<br>
      The man who never reads<br>
      lives only one.
    </div>
    <div style="font-size: 8pt; color: #bbb; margin-bottom: 12px;">&mdash; George R.R. Martin</div>
    <div class="fp-line"></div>
    <div class="fp-logo">More Shine Press</div>
    <div class="fp-line"></div>
  </div>
</div>""" % pg


def generate(output_path=HTML_FILE):
    pages = []
    pages.append(interior_title_page())
    pages.append(how_to_use_page())

    # 50 book log entries
    for entry in range(1, 51):
        pages.append(book_log_page(entry))
        if entry % 12 == 0:
            pages.append(tbr_page())

    # Extra TBR pages
    pages.append(tbr_page())
    pages.append(tbr_page())

    # Yearly stats
    pages.append(yearly_stats_page())

    # Notes
    for _ in range(2):
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
