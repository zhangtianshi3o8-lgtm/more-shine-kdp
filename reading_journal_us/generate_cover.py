#!/usr/bin/env python3
"""Reading Journal — KDP Full Wrap Cover Generator"""
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "reading_journal_us_cover_V1.0.html")

TRIM_W = 6.0; TRIM_H = 9.0; PAGES = 60
SPINE = PAGES * 0.0025; BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2; COVER_H = TRIM_H + BLEED * 2

C_CHARCOAL = "#0F0A1A"; C_DARK = "#1A1228"
C_PURPLE = "#7B6BA8"; C_PURPLE_D = "#5B4B88"
C_GOLD = "#C4A04A"; C_GOLD_L = "#D4B896"
C_CREAM = "#FAF6F0"; C_WHITE = "#ffffff"

CSS = """<style>
@page { size: %.4fin %.4fin; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: Georgia, "Iowan Old Style", "Palatino", serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.cover-wrap { width: %.4fin; height: %.4fin; position: relative; display: flex; }
.back-cover { width: %.4fin; height: %.4fin; background: linear-gradient(165deg, %s 0%%, %s 40%%, %s 100%%); padding: 0.75in 0.5in 0.45in 0.5in; display: flex; flex-direction: column; justify-content: space-around; position: relative; overflow: hidden; }
.back-cover::before { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.04; background-image: radial-gradient(ellipse 24px 14px at 15%% 25%%, %s, transparent), radial-gradient(ellipse 22px 13px at 80%% 15%%, %s, transparent), radial-gradient(ellipse 26px 15px at 70%% 70%%, %s, transparent), radial-gradient(ellipse 20px 12px at 25%% 80%%, %s, transparent); }
.back-cover::after { content: ''; position: absolute; top: -0.3in; right: -0.3in; width: 1.2in; height: 1.2in; border-radius: 50%%; background: rgba(123,107,168,0.08); }
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
.book-icon-wrap { width: 120px; height: 120px; position: relative; margin: 0 auto 24px; z-index: 5; }
.title-block { position: relative; z-index: 5; padding: 0 0.5in; }
.main-title { font-family: Georgia, serif; font-size: 32pt; font-weight: 700; color: %s; line-height: 1.12; letter-spacing: 0.5pt; text-shadow: 2px 2px 8px rgba(0,0,0,0.55); }
.accent-bar { width: 120px; height: 2.5px; background: %s; margin: 16px auto; }
.subtitle { font-size: 11pt; color: %s; font-style: italic; line-height: 1.5; margin-bottom: 22px; }
.features { display: flex; justify-content: center; gap: 8px; margin-bottom: 22px; flex-wrap: wrap; }
.feature-badge { background: rgba(255,255,255,0.08); border: 1px solid rgba(123,107,168,0.4); color: %s; font-size: 7.5pt; font-weight: 700; letter-spacing: 0.5pt; padding: 4px 10px; border-radius: 3px; text-transform: uppercase; }
.tagline { font-size: 9pt; color: %s; letter-spacing: 2pt; text-transform: uppercase; margin-top: 8px; }
.publisher { position: absolute; bottom: 0.5in; left: 0; right: 0; text-align: center; font-size: 9.5pt; color: %s; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; z-index: 5; }
@media screen { .cover-wrap { border: 1px solid #ccc; } }
</style>""" % (
    COVER_W, COVER_H, COVER_W, COVER_H,
    TRIM_W + BLEED, COVER_H, C_CHARCOAL, C_DARK, C_CHARCOAL,
    C_PURPLE, C_GOLD, C_PURPLE, C_GOLD,
    C_GOLD_L, C_PURPLE, C_GOLD,
    SPINE, COVER_H, C_CHARCOAL, C_DARK, C_CHARCOAL,
    C_PURPLE, C_GOLD, C_PURPLE, C_GOLD,
    TRIM_W + BLEED, COVER_H, C_CHARCOAL, C_DARK, C_DARK, C_DARK, C_CHARCOAL,
    BLEED,
    C_PURPLE, C_GOLD, C_PURPLE, C_GOLD, C_PURPLE,
    C_WHITE, C_PURPLE, C_GOLD_L, C_GOLD, C_GOLD_L, C_GOLD
)

html_body = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Reading Journal — Cover</title>
  %s
</head>
<body>
<div class="cover-wrap">
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>A reader lives a thousand lives.</strong>
        This journal is your companion through every one of them. Record the
        books you've read, capture your favorite quotes, rate each story,
        and keep your reading wishlist organized in one beautiful place.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: %s; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">What's Inside</div>
      <ul class="back-features">
        <li>50 detailed book log entries</li>
        <li>Star ratings, genre tags, and format tracking</li>
        <li>Favorite quote sections with page references</li>
        <li>To Be Read (TBR) wishlist pages</li>
        <li>Yearly reading statistics and goals</li>
        <li>Large 6" x 9" format &mdash; room to write</li>
      </ul>
    </div>
    <div class="back-bottom">
      <div class="barcode-area">ISBN Barcode Area</div>
      <div class="back-logo">More Shine Press</div>
    </div>
  </div>

  <div class="spine">
    <div class="spine-author">More Shine Press</div>
    <div class="spine-text">Reading Journal</div>
  </div>

  <div class="front-cover">
    <div class="book-icon-wrap">
      <svg viewBox="0 0 120 120" width="120" height="120" xmlns="http://www.w3.org/2000/svg">
        <path d="M 18 36 Q 18 31 23 31 L 54 31 Q 60 31 60 36 L 60 92 Q 60 87 54 87 L 23 87 Q 18 87 18 92 Z"
              stroke="#7B6BA8" stroke-width="1.5" fill="none"/>
        <path d="M 60 36 Q 60 31 66 31 L 97 31 Q 102 31 102 36 L 102 92 Q 102 87 97 87 L 66 87 Q 60 87 60 92 Z"
              stroke="#7B6BA8" stroke-width="1.5" fill="none"/>
        <line x1="24" y1="41" x2="53" y2="41" stroke="#7B6BA8" stroke-width="0.8" opacity="0.4"/>
        <line x1="24" y1="48" x2="53" y2="48" stroke="#7B6BA8" stroke-width="0.8" opacity="0.4"/>
        <line x1="24" y1="55" x2="48" y2="55" stroke="#7B6BA8" stroke-width="0.8" opacity="0.4"/>
        <line x1="67" y1="41" x2="96" y2="41" stroke="#7B6BA8" stroke-width="0.8" opacity="0.4"/>
        <line x1="67" y1="48" x2="96" y2="48" stroke="#7B6BA8" stroke-width="0.8" opacity="0.4"/>
        <line x1="67" y1="55" x2="91" y2="55" stroke="#7B6BA8" stroke-width="0.8" opacity="0.4"/>
        <line x1="60" y1="36" x2="60" y2="92" stroke="#C4A04A" stroke-width="1.2"/>
      </svg>
    </div>
    <div class="title-block">
      <div class="main-title">Reading Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Track Every Book,<br>Every Thought, Every Journey</div>
      <div class="features">
        <span class="feature-badge">50 Book Logs</span>
        <span class="feature-badge">TBR Wishlist</span>
        <span class="feature-badge">Star Ratings</span>
        <span class="feature-badge">Yearly Stats</span>
      </div>
      <div class="tagline">Read &middot; Reflect &middot; Remember</div>
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
