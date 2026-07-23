#!/usr/bin/env python3
"""Travel Journal — KDP Full Wrap Cover Generator"""
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "travel_journal_us_cover_V1.0.html")

TRIM_W = 6.0; TRIM_H = 9.0; PAGES = 52
SPINE = PAGES * 0.0025; BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2; COVER_H = TRIM_H + BLEED * 2

C_CHARCOAL = "#0A1620"; C_DARK = "#102838"
C_TEAL = "#2E86AB"; C_TEAL_D = "#1E6688"
C_GOLD = "#C4A04A"; C_GOLD_L = "#D4B896"
C_CREAM = "#FAF6F0"; C_WHITE = "#ffffff"

CSS = """<style>
@page { size: %.4fin %.4fin; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: Georgia, "Iowan Old Style", "Palatino", serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.cover-wrap { width: %.4fin; height: %.4fin; position: relative; display: flex; }
.back-cover { width: %.4fin; height: %.4fin; background: linear-gradient(165deg, %s 0%%, %s 40%%, %s 100%%); padding: 0.75in 0.5in 0.45in 0.5in; display: flex; flex-direction: column; justify-content: space-around; position: relative; overflow: hidden; }
.back-cover::before { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.04; background-image: radial-gradient(ellipse 24px 14px at 15%% 25%%, %s, transparent), radial-gradient(ellipse 22px 13px at 80%% 15%%, %s, transparent), radial-gradient(ellipse 26px 15px at 70%% 70%%, %s, transparent), radial-gradient(ellipse 20px 12px at 25%% 80%%, %s, transparent); }
.back-cover::after { content: ''; position: absolute; top: -0.3in; right: -0.3in; width: 1.2in; height: 1.2in; border-radius: 50%%; background: rgba(46,134,171,0.08); }
.back-text { color: rgba(255,255,255,0.92); font-size: 9pt; line-height: 1.6; position: relative; z-index: 2; }
.back-text .blurb { font-style: italic; margin-bottom: 14px; font-size: 9.5pt; line-height: 1.55; }
.back-text .blurb strong { color: %s; font-style: normal; }
.back-features { list-style: none; padding: 0; }
.back-features li { font-size: 8pt; color: rgba(255,255,255,0.82); padding: 3px 0; padding-left: 16px; position: relative; line-height: 1.4; }
.back-features li::before { content: ''; position: absolute; left: 0; top: 5px; width: 5px; height: 5px; background: %s; border-radius: 50%%; }
.back-bottom { padding-bottom: 0.15in; position: relative; z-index: 2; }
.barcode-area { width: 2in; height: 1.2in; background: white; margin-left: auto; border-radius: 2px; display: flex; align-items: center; justify-content: center; font-size: 6pt; color: #ccc; font-family: 'Helvetica Neue', Arial, sans-serif; }
.back-logo { text-align: center; color: %s; font-size: 8pt; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; padding-top: 8px; margin-top: 6px; border-top: 1px solid rgba(255,255,255,0.15); }
.spine { width: %.4fin; height: %.4fin; background: linear-gradient(180deg, %s 0%%, %s 50%%, %s 100%%); display: flex; flex-direction: column; align-items: center; justify-content: space-between; padding: 0.6in 0; position: relative; }
.spine::before { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.03; background-image: radial-gradient(ellipse 10px 6px at 50%% 20%%, %s, transparent), radial-gradient(ellipse 10px 6px at 50%% 50%%, %s, transparent), radial-gradient(ellipse 10px 6px at 50%% 80%%, %s, transparent); }
.spine-text { writing-mode: vertical-rl; transform: rotate(180deg); color: rgba(255,255,255,0.95); font-size: 8pt; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; white-space: nowrap; line-height: 1; position: relative; z-index: 2; }
.spine-author { writing-mode: vertical-rl; transform: rotate(180deg); color: %s; font-size: 6pt; letter-spacing: 1.5px; text-transform: uppercase; font-family: 'Helvetica Neue', Arial, sans-serif; position: relative; z-index: 2; }
.front-cover { width: %.4fin; height: %.4fin; background: linear-gradient(165deg, %s 0%%, %s 25%%, %s 55%%, %s 85%%, %s 100%%); position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: %.4fin; }
.front-cover::before { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.05; background-image: radial-gradient(ellipse 40px 24px at 15%% 25%%, %s, transparent), radial-gradient(ellipse 34px 20px at 80%% 15%%, %s, transparent), radial-gradient(ellipse 38px 22px at 70%% 70%%, %s, transparent), radial-gradient(ellipse 28px 18px at 25%% 80%%, %s, transparent), radial-gradient(ellipse 24px 15px at 50%% 50%%, %s, transparent); }
.compass-wrap { width: 120px; height: 120px; position: relative; margin: 0 auto 24px; z-index: 5; }
.title-block { position: relative; z-index: 5; padding: 0 0.5in; }
.main-title { font-family: Georgia, serif; font-size: 32pt; font-weight: 700; color: %s; line-height: 1.12; letter-spacing: 0.5pt; text-shadow: 2px 2px 8px rgba(0,0,0,0.55); }
.accent-bar { width: 120px; height: 2.5px; background: %s; margin: 16px auto; }
.subtitle { font-size: 11pt; color: %s; font-style: italic; line-height: 1.5; margin-bottom: 22px; }
.features { display: flex; justify-content: center; gap: 8px; margin-bottom: 22px; flex-wrap: wrap; }
.feature-badge { background: rgba(255,255,255,0.08); border: 1px solid rgba(46,134,171,0.4); color: %s; font-size: 7.5pt; font-weight: 700; letter-spacing: 0.5pt; padding: 4px 10px; border-radius: 3px; text-transform: uppercase; }
.tagline { font-size: 9pt; color: %s; letter-spacing: 2pt; text-transform: uppercase; margin-top: 8px; }
.publisher { position: absolute; bottom: 0.5in; left: 0; right: 0; text-align: center; font-size: 9.5pt; color: %s; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; z-index: 5; }
@media screen { .cover-wrap { border: 1px solid #ccc; } }
</style>""" % (
    COVER_W, COVER_H, COVER_W, COVER_H,
    TRIM_W + BLEED, COVER_H, C_CHARCOAL, C_DARK, C_CHARCOAL,
    C_TEAL, C_GOLD, C_TEAL, C_GOLD,
    C_GOLD_L, C_TEAL, C_GOLD,
    SPINE, COVER_H, C_CHARCOAL, C_DARK, C_CHARCOAL,
    C_TEAL, C_GOLD, C_TEAL, C_GOLD,
    TRIM_W + BLEED, COVER_H, C_CHARCOAL, C_DARK, C_DARK, C_DARK, C_CHARCOAL,
    BLEED,
    C_TEAL, C_GOLD, C_TEAL, C_GOLD, C_TEAL,
    C_WHITE, C_TEAL, C_GOLD_L, C_GOLD, C_GOLD_L, C_GOLD
)

html_body = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Travel Journal — Cover</title>
  %s
</head>
<body>
<div class="cover-wrap">
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>Not all those who wander are lost.</strong>
        From weekend getaways to bucket-list adventures, this journal
        helps you plan every trip, record every moment, and preserve
        your travel memories for a lifetime. Plan, explore, reflect,
        and remember.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: %s; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">What's Inside</div>
      <ul class="back-features">
        <li>15 three-page trip spreads (45 pages of travel logs)</li>
        <li>Travel bucket list with 24 dream destinations</li>
        <li>Daily itinerary planner for each trip</li>
        <li>Expense tracker with budget vs actual</li>
        <li>Food and drink discovery sections</li>
        <li>Countries and places visited tracker</li>
        <li>Large 6" x 9" format &mdash; room to write and sketch</li>
      </ul>
    </div>
    <div class="back-bottom">
      <div class="barcode-area">ISBN Barcode Area</div>
      <div class="back-logo">More Shine Press</div>
    </div>
  </div>

  <div class="spine">
    <div class="spine-author">More Shine Press</div>
    <div class="spine-text">Travel Journal</div>
  </div>

  <div class="front-cover">
    <div class="compass-wrap">
      <svg viewBox="0 0 120 120" width="120" height="120" xmlns="http://www.w3.org/2000/svg">
        <circle cx="60" cy="60" r="48" stroke="#2E86AB" stroke-width="1.5" fill="none"/>
        <circle cx="60" cy="60" r="38" stroke="#2E86AB" stroke-width="1" fill="none" opacity="0.3"/>
        <polygon points="60,22 54,60 60,55 66,60" fill="#2E86AB" opacity="0.6"/>
        <polygon points="60,98 54,60 60,65 66,60" fill="#C4A04A" opacity="0.6"/>
        <text x="55" y="18" font-family="Georgia" font-size="9" fill="#2E86AB" font-weight="bold">N</text>
        <text x="55" y="112" font-family="Georgia" font-size="9" fill="#C4A04A">S</text>
        <text x="96" y="65" font-family="Georgia" font-size="9" fill="#C4A04A">E</text>
        <text x="16" y="65" font-family="Georgia" font-size="9" fill="#C4A04A">W</text>
        <circle cx="60" cy="60" r="3" fill="#2E86AB"/>
      </svg>
    </div>
    <div class="title-block">
      <div class="main-title">Travel Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Capture Every Journey,<br>Every Memory, Every Adventure</div>
      <div class="features">
        <span class="feature-badge">15 Trip Logs</span>
        <span class="feature-badge">Bucket List</span>
        <span class="feature-badge">Itinerary</span>
        <span class="feature-badge">Expense Tracker</span>
      </div>
      <div class="tagline">Plan &middot; Explore &middot; Remember</div>
    </div>
    <div class="publisher">More Shine Press</div>
  </div>
</div>
</body>
</html>""" % (CSS, C_GOLD_L)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_body)
print("[OK] Cover generated: %s" % OUTPUT_FILE)
print("     Full cover: %.4f x %.4f in" % (COVER_W, COVER_H))
print("     Spine: %.4f in (%d pages)" % (SPINE, PAGES))
