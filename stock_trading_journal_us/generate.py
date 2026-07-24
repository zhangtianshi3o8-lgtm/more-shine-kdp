#!/usr/bin/env python3
"""
Stock Trading Journal -- KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Active stock and options traders
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "stock_trading_journal_us_V1.0.html")

BOOK_TITLE = "Stock Trading Journal"
BOOK_SUBTITLE = "Track Every Trade, Analyze Every Move, Master Your Strategy"

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
  background: linear-gradient(165deg, #0D1117 0%, #1A2332 30%, #0D1117 65%, #060A0F 100%);
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #2E7D32, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #2E7D32, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #2E7D32, transparent);
}

.cover .title-main {
  font-size: 30pt;
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
  background: #2E7D32;
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
  color: #2E7D32;
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
  color: #0D1117;
  letter-spacing: 0.5pt;
  text-transform: uppercase;
}

.section-line {
  flex: 1;
  height: 1px;
  background: #2E7D32;
  margin: 0 12px;
  opacity: 0.4;
}

/* ================ HOW TO USE ================ */
.howto-text { font-size: 10pt; line-height: 1.7; }
.howto-text p { margin-bottom: 8px; }
.howto-text .ht-title {
  font-size: 11pt; font-weight: 700; color: #0D1117;
  margin-bottom: 4px; margin-top: 6px;
}
.howto-text .ht-icon { color: #2E7D32; font-weight: 700; margin-right: 4px; }

/* ================ INFO FIELDS ================ */
.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
  margin-bottom: 8px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #2E7D32;
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

/* ================ TRADE BANNER ================ */
.trade-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1.5px solid #2E7D32;
  padding-bottom: 5px;
  margin-bottom: 10px;
}

.trade-banner .tb-num {
  display: inline-block;
  border: 1.5px solid #2E7D32;
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 8pt;
  color: #2E7D32;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.trade-banner .tb-label {
  font-size: 8pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.trade-banner .tb-line {
  flex: 1;
  height: 12px;
  border-bottom: 1px dotted #ccc;
}

/* ================ TYPE CHECKBOXES ================ */
.type-row {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-bottom: 8px;
}

.type-check {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 7.5pt;
  color: #555;
}

.type-box {
  width: 10px; height: 10px;
  border: 1.5px solid #2E7D32;
  border-radius: 2px;
}

/* ================ DATA TABLE ================ */
.data-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
}

.data-table th {
  font-size: 6.5pt;
  color: #2E7D32;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 5px 3px;
  border-bottom: 1.5px solid #2E7D32;
  text-align: center;
}

.data-table th:first-child { text-align: left; }

.data-table td {
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
  color: #2E7D32;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 3px;
}

.write-box .wb-area {
  height: 28px;
}

/* ================ METRIC ROWS ================ */
.metric-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 6px 10px;
  margin-bottom: 8px;
}

.metric-field .mf-label {
  font-size: 6.5pt;
  color: #2E7D32;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  display: block;
  margin-bottom: 1px;
}

.metric-field .mf-write {
  height: 18px;
  border-bottom: 1px dotted #ccc;
}

/* ================ SCORE DOTS ================ */
.score-dots {
  display: flex;
  gap: 4px;
  margin-top: 2px;
}

.score-dot {
  width: 12px; height: 12px;
  border: 1.5px solid #2E7D32;
  border-radius: 50%;
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
  width: 60px; height: 1.5px; background: #2E7D32;
  margin: 12px auto; opacity: 0.5;
}
"""


def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- Chart line going up -->
      <g transform="translate(50,50)">
        <polyline points="-35,20 -20,10 -8,15 5,-5 18,-10 32,-22" stroke="#2E7D32" stroke-width="2.5" fill="none" stroke-linejoin="round"/>
        <!-- Axis -->
        <line x1="-38" y1="25" x2="35" y2="25" stroke="#C4A04A" stroke-width="1" opacity="0.5"/>
        <line x1="-38" y1="25" x2="-38" y2="-25" stroke="#C4A04A" stroke-width="1" opacity="0.5"/>
        <!-- Arrow at end -->
        <polygon points="32,-22 28,-18 28,-26" fill="#2E7D32"/>
        <!-- Data points -->
        <circle cx="-20" cy="10" r="2" fill="#2E7D32"/>
        <circle cx="5" cy="-5" r="2" fill="#2E7D32"/>
        <circle cx="18" cy="-10" r="2" fill="#2E7D32"/>
      </g>
    </svg>
  </div>

  <div class="title-main">Stock<br>Trading<br>Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Track Every Trade, Analyze Every Move,<br>Master Your Strategy</div>

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
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Trading Edge</div>
    <p>This journal is designed to make you a more disciplined, self-aware
    trader. Every professional trader keeps records -- not because they
    enjoy paperwork, but because reviewing past trades is the fastest
    path to consistent profits.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Two-Page Trade Spread</div>
    <p>Each trade uses a <strong>two-page spread</strong>. The left page
    captures the setup: ticker, direction, entry and exit prices, position
    size, and risk parameters. The right page is for your analysis:
    the reasoning behind the trade, what went right or wrong, lessons
    learned, and an emotion and confidence check.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> The Weekly Review</div>
    <p>After every 10 trades, a <strong>weekly review page</strong> helps
    you spot patterns: win rate, average gain vs. average loss, best and
    worst trades, and recurring mistakes. This is where edge is built.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Rules to Follow</div>
    <p>&#9679; <strong>Fill it in immediately</strong> after each trade, while
    details are fresh.</p>
    <p>&#9679; <strong>Be honest.</strong> Record your emotions, not just
    numbers.</p>
    <p>&#9679; <strong>Review weekly.</strong> Patterns emerge over 20+ trades.</p>
    <p>&#9679; <strong>Define risk before entry.</strong> Know your stop loss
    and profit target.</p>
  </div>
</div>""" % (pg, pg)


def strategy_setup_page():
    pg = pn()
    return """<!-- PAGE %d: Trading Plan -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">My Trading Plan</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Trading Plan</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Account Size</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Max Risk Per Trade</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Starting Date</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Target Return (Monthly)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Daily Loss Limit</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Max Positions at Once</span><div class="if-write"></div></div>
  </div>

  <div class="write-box">
    <div class="wb-label">My Trading Style (Swing / Day / Position)</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #2E7D32;">
    <div class="wb-label">My Setup Criteria (What Must Be True to Enter)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Risk Management Rules</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #2E7D32;">
    <div class="wb-label">Markets / Sectors I Trade</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">My Exit Rules (When Do I Sell?)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>
</div>""" % (pg, pg)


def trade_left(entry_num):
    pg = pn()
    directions = ["Long", "Short"]
    dir_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % d
        for d in directions
    )
    outcomes = ["Win", "Loss", "Breakeven", "Scratch"]
    out_html = " ".join(
        '<span class="type-check"><span class="type-box"></span>%s</span>' % o
        for o in outcomes
    )
    return """<!-- PAGE %d: Trade Left #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Trade Record</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="trade-banner">
    <span class="tb-num">Trade #%03d</span>
    <span class="tb-label">Ticker:</span>
    <div class="tb-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Date Entered</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Date Exited</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #2E7D32; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Direction</div>
  <div class="type-row">%s</div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Entry Price</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Exit Price</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Stop Loss</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Target Price</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Shares / Contracts</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Risk Amount ($)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">P&amp;L ($)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">R Multiple</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">%% Return</span><div class="mf-write"></div></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #2E7D32; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Outcome</div>
  <div class="type-row">%s</div>

  <div class="write-box" style="border-color: #2E7D32;">
    <div class="wb-label">Setup / Pattern (Breakout, Pullback, Reversal, Gap, etc.)</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Market Context (Trend, Sector, News, Earnings)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>
</div>""" % (pg, entry_num, pg, entry_num, dir_html, out_html)


def trade_right():
    pg = pn()
    return """<!-- PAGE %d: Trade Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Trade Analysis</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="write-box">
    <div class="wb-label">Why I Entered (My Thesis)</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box" style="border-color: #2E7D32;">
    <div class="wb-label">What Went Right</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box" style="border-color: #C0392B;">
    <div class="wb-label">What Went Wrong</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Mistake? (Did I Break My Rules?)</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #2E7D32;">
    <div class="wb-label">Key Lesson (What Will I Do Differently?)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 6px;">
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #2E7D32; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Confidence Before Entry</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Low &#160; 5 = High</div>
    </div>
    <div>
      <div style="font-size: 7pt; font-weight: 700; color: #2E7D32; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Emotional Control</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 5.5pt; color: #999; margin-top: 2px;">1 = Reckless &#160; 5 = Disciplined</div>
    </div>
  </div>

  <div class="write-box" style="margin-top: 8px; border-color: #C4A04A;">
    <div class="wb-label">Chart Sketch / Key Levels</div>
    <div class="wb-area" style="height: 44px;"></div>
  </div>
</div>""" % (pg, pg)


def weekly_review_page(review_num):
    pg = pn()
    return """<!-- PAGE %d: Weekly Review #%d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Weekly Review</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="trade-banner">
    <span class="tb-num">Review #%02d</span>
    <span class="tb-label">Week of:</span>
    <div class="tb-line"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Total Trades</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Wins</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Losses</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Win Rate (%%)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Net P&amp;L ($)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Avg Win ($)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Avg Loss ($)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Profit Factor</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Largest Win ($)</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #2E7D32;">
    <div class="wb-label">Best Trade This Week (What Made It Work)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box" style="border-color: #C0392B;">
    <div class="wb-label">Worst Trade This Week (What Went Wrong)</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Recurring Pattern or Mistake</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #2E7D32;">
    <div class="wb-label">One Thing to Improve Next Week</div>
    <div class="wb-area"></div>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-top: 4px;">
    <div>
      <div style="font-size: 6.5pt; font-weight: 700; color: #2E7D32; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Did I Follow My Plan?</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
    </div>
    <div>
      <div style="font-size: 6.5pt; font-weight: 700; color: #2E7D32; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Overall Discipline</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
    </div>
    <div>
      <div style="font-size: 6.5pt; font-weight: 700; color: #2E7D32; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">Emotional Control</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
        <div class="score-dot"></div><div class="score-dot"></div>
      </div>
    </div>
  </div>
</div>""" % (pg, review_num, pg, review_num)


def watchlist_page():
    pg = pn()
    return """<!-- PAGE %d: Watchlist -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Watchlist</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="data-table">
    <thead>
      <tr>
        <th>Ticker</th>
        <th>Company / Sector</th>
        <th>Price</th>
        <th>Setup</th>
        <th>Target Entry</th>
        <th>Stop</th>
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
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
      <tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    </tbody>
  </table>
</div>""" % (pg, pg)


def monthly_summary_page():
    pg = pn()
    return """<!-- PAGE %d: Monthly Summary -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Monthly Summary</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Month / Year</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Starting Balance</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Ending Balance</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Net P&amp;L</span><div class="if-write"></div></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">Total Trades</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Win Rate (%%)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Profit Factor</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Avg Win ($)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Avg Loss ($)</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">Expectancy</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #2E7D32;">
    <div class="wb-label">What I Did Well This Month</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #C0392B;">
    <div class="wb-label">Biggest Mistake / Area to Fix</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #2E7D32;">
    <div class="wb-label">Goal for Next Month</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Notes / Observations</div>
    <div class="wb-area" style="height: 32px;"></div>
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
      The market rewards discipline.<br>
      Every trade is a lesson.<br>
      Review. Adapt. Improve.
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
    pages.append(strategy_setup_page())

    # 25 trade spreads (50 pages), with a weekly review every 5 trades
    trade_count = 0
    review_count = 0
    for entry in range(1, 26):
        pages.append(trade_left(entry))
        pages.append(trade_right())
        trade_count += 1
        # Insert weekly review after every 5th trade
        if trade_count % 5 == 0:
            review_count += 1
            pages.append(weekly_review_page(review_count))

    # Watchlist (2 pages)
    for _ in range(2):
        pages.append(watchlist_page())

    # Monthly summary (2 pages)
    for _ in range(2):
        pages.append(monthly_summary_page())

    # Notes (3 pages)
    for _ in range(3):
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
