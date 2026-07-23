#!/usr/bin/env python3
"""Dog Training & Puppy Journal — KDP Full Wrap Cover Generator"""
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "dog_training_journal_us_cover_V1.0.html")

TRIM_W = 6.0; TRIM_H = 9.0; PAGES = 28
SPINE = PAGES * 0.0025; BLEED = 0.125
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2; COVER_H = TRIM_H + BLEED * 2

C_CHARCOAL = "#161616"; C_DARK = "#1E1E1E"
C_SAGE = "#7A8B6F"; C_SAGE_D = "#5A6B4F"
C_GOLD = "#C4A04A"; C_GOLD_L = "#D4B896"
C_CREAM = "#FAF6F0"; C_WHITE = "#ffffff"

# Read page count from generate.py output for correct spine
# We'll use 28 pages = 7 intro + 16 weeks + 3 notes + 1 final + 1 title
PAGES = 28

CSS = """<style>
@page { size: %.4fin %.4fin; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: Georgia, "Iowan Old Style", "Palatino", serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.cover-wrap { width: %.4fin; height: %.4fin; position: relative; display: flex; }
.back-cover { width: %.4fin; height: %.4fin; background: linear-gradient(165deg, %s 0%%, %s 40%%, %s 100%%); padding: 0.75in 0.5in 0.45in 0.5in; display: flex; flex-direction: column; justify-content: space-around; position: relative; overflow: hidden; }
.back-cover::before { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.04; background-image: radial-gradient(ellipse 24px 14px at 15%% 25%%, %s, transparent), radial-gradient(ellipse 22px 13px at 80%% 15%%, %s, transparent), radial-gradient(ellipse 26px 15px at 70%% 70%%, %s, transparent), radial-gradient(ellipse 20px 12px at 25%% 80%%, %s, transparent); }
.back-cover::after { content: ''; position: absolute; top: -0.3in; right: -0.3in; width: 1.2in; height: 1.2in; border-radius: 50%%; background: rgba(122,139,111,0.08); }
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
.spine-text { writing-mode: vertical-rl; transform: rotate(180deg); color: rgba(255,255,255,0.95); font-size: 7pt; font-weight: bold; letter-spacing: 1.5px; text-transform: uppercase; white-space: nowrap; line-height: 1; position: relative; z-index: 2; }
.spine-author { writing-mode: vertical-rl; transform: rotate(180deg); color: %s; font-size: 6pt; letter-spacing: 1.5px; text-transform: uppercase; font-family: 'Helvetica Neue', Arial, sans-serif; position: relative; z-index: 2; }
.front-cover { width: %.4fin; height: %.4fin; background: linear-gradient(165deg, %s 0%%, %s 25%%, %s 55%%, %s 85%%, %s 100%%); position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: %.4fin %.4fin %.4fin %.4fin; }
.front-cover::before { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.05; background-image: radial-gradient(ellipse 40px 24px at 15%% 25%%, %s, transparent), radial-gradient(ellipse 34px 20px at 80%% 15%%, %s, transparent), radial-gradient(ellipse 38px 22px at 70%% 70%%, %s, transparent), radial-gradient(ellipse 28px 18px at 25%% 80%%, %s, transparent), radial-gradient(ellipse 24px 15px at 50%% 50%%, %s, transparent); }
.paw-wrap { width: 120px; height: 120px; position: relative; margin: 0 auto 24px; z-index: 5; }
.title-block { position: relative; z-index: 5; padding: 0 0.5in; }
.main-title { font-family: Georgia, serif; font-size: 24pt; font-weight: 700; color: %s; line-height: 1.12; letter-spacing: 0.5pt; text-shadow: 2px 2px 8px rgba(0,0,0,0.55); }
.accent-bar { width: 120px; height: 2.5px; background: %s; margin: 16px auto; }
.subtitle { font-size: 11pt; color: %s; font-style: italic; line-height: 1.5; margin-bottom: 22px; }
.features { display: flex; justify-content: center; gap: 8px; margin-bottom: 22px; flex-wrap: wrap; }
.feature-badge { background: rgba(255,255,255,0.08); border: 1px solid rgba(122,139,111,0.4); color: %s; font-size: 7.5pt; font-weight: 700; letter-spacing: 0.5pt; padding: 4px 10px; border-radius: 3px; text-transform: uppercase; }
.tagline { font-size: 9pt; color: %s; letter-spacing: 2pt; text-transform: uppercase; margin-top: 8px; }
.publisher { position: absolute; bottom: 0.5in; left: 0; right: 0; text-align: center; font-size: 9.5pt; color: %s; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; z-index: 5; }
@media screen { .cover-wrap { border: 1px solid #ccc; } }
</style>""" % (
    COVER_W, COVER_H,
    COVER_W, COVER_H,
    TRIM_W + BLEED, COVER_H, C_CHARCOAL, C_DARK, C_CHARCOAL,
    C_SAGE, C_GOLD, C_SAGE, C_GOLD,
    C_GOLD_L, C_SAGE, C_GOLD,
    SPINE, COVER_H, C_CHARCOAL, C_DARK, C_CHARCOAL,
    C_SAGE, C_GOLD, C_SAGE, C_GOLD,
    TRIM_W + BLEED, COVER_H, C_CHARCOAL, C_DARK, C_DARK, C_DARK, C_CHARCOAL,
    BLEED, BLEED, BLEED, BLEED,
    C_SAGE, C_GOLD, C_SAGE, C_GOLD, C_SAGE,
    C_WHITE, C_SAGE, C_GOLD_L, C_GOLD, C_GOLD_L, C_GOLD
)

html_body = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dog Training &amp; Puppy Journal — Cover</title>
  %s
</head>
<body>
<div class="cover-wrap">
  <div class="back-cover">
    <div class="back-text">
      <div class="blurb">
        <strong>From first paw print to best friend.</strong>
        This journal guides you through your puppy's first months with
        training logs, milestone tracking, health records, and weekly
        progress reviews. Capture every wag, every trick, every milestone.
      </div>
      <div style="margin-bottom: 8px; font-size: 8.5pt; color: %s; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt;">What's Inside</div>
      <ul class="back-features">
        <li>Dog profile page with all vital details</li>
        <li>25-item puppy milestone checklist</li>
        <li>18-command training progress tracker</li>
        <li>16 weeks of training session logs</li>
        <li>Health and vaccination record pages</li>
        <li>Monthly weight tracker and diet log</li>
        <li>Large 6" x 9" format &mdash; easy to write in</li>
      </ul>
    </div>
    <div class="back-bottom">
      <div class="barcode-area">ISBN Barcode Area</div>
      <div class="back-logo">More Shine Press</div>
    </div>
  </div>

  <div class="spine">
    <div class="spine-author">More Shine Press</div>
    <div class="spine-text">Dog Training &amp; Puppy Journal</div>
  </div>

  <div class="front-cover">
    <div class="paw-wrap">
      <svg viewBox="0 0 120 120" width="120" height="120" xmlns="http://www.w3.org/2000/svg">
        <path d="M 36 66 Q 36 50 46 48 Q 60 43 74 48 Q 84 50 84 66 Q 84 86 60 86 Q 36 86 36 66 Z"
              stroke="#C4A04A" stroke-width="1.5" fill="none"/>
        <ellipse cx="30" cy="38" rx="8" ry="12" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.7"/>
        <ellipse cx="48" cy="26" rx="8" ry="12" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.7"/>
        <ellipse cx="72" cy="26" rx="8" ry="12" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.7"/>
        <ellipse cx="90" cy="38" rx="8" ry="12" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.7"/>
      </svg>
    </div>
    <div class="title-block">
      <div class="main-title">Dog Training<br>&amp; Puppy Journal</div>
      <div class="accent-bar"></div>
      <div class="subtitle">Your Companion from<br>First Day to Best Friend</div>
      <div class="features">
        <span class="feature-badge">16 Weekly Logs</span>
        <span class="feature-badge">Milestones</span>
        <span class="feature-badge">Command Tracker</span>
        <span class="feature-badge">Health Record</span>
      </div>
      <div class="tagline">Train &middot; Track &middot; Celebrate</div>
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
