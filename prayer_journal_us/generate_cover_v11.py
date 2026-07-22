#!/usr/bin/env python3
"""
Prayer Journal — Cover V1.1 "Quiet Luxury" Demo
Demonstrates tone-on-tone subtle background pattern approach.
Compare side-by-side with V1.0 to see the difference.
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "prayer_journal_cover_V1.1_quiet_luxury_demo.html")

TRIM_W = 6.0
TRIM_H = 9.0
BLEED = 0.125
SPINE = 0.320
COVER_W = TRIM_W * 2 + SPINE + BLEED * 2
COVER_H = TRIM_H + BLEED * 2

BOOK_TITLE = "Prayer Journal"
BOOK_SUBTITLE = "A 52-Week Guided Journal for Prayer, Scripture & Gratitude"
PUBLISHER = "More Shine Press"

CSS = f"""
@page {{ size: {COVER_W}in {COVER_H}in; margin: 0; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}

body {{
  font-family: Georgia, "Iowan Old Style", "Palatino", serif;
  background: #222;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}

.cover-wrap {{
  width: {COVER_W}in;
  height: {COVER_H}in;
  position: relative;
  overflow: hidden;
  display: flex;
}}

/* ===== BACK COVER ===== */
.back-cover {{
  width: {TRIM_W}in;
  height: {COVER_H}in;
  margin-left: {BLEED}in;
  background: #0A1320;
  display: flex;
  flex-direction: column;
  padding: 0.55in 0.50in 0.40in 0.50in;
  position: relative;
  overflow: hidden;
  color: white;
}}

/* TONE-ON-TONE: subtle cross pattern — barely visible */
.back-cover .bc-subtle-pattern {{
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.04;
  background-image:
    repeating-linear-gradient(45deg,
      transparent 0px, transparent 28px,
      #C9A84C 28px, #C9A84C 29px,
      transparent 29px, transparent 57px,
      #C9A84C 57px, #C9A84C 58px);
  z-index: 0;
}}

/* TONE-ON-TONE: large faded cross watermark */
.back-cover .bc-watermark {{
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 2.5in; height: 4in;
  opacity: 0.025;
  z-index: 0;
}}

.back-cover .bc-watermark::before {{
  content: "";
  position: absolute;
  left: 50%; top: 0;
  transform: translateX(-50%);
  width: 0.5in; height: 4in;
  background: #C9A84C;
}}

.back-cover .bc-watermark::after {{
  content: "";
  position: absolute;
  left: 50%; top: 1.1in;
  transform: translateX(-50%);
  width: 1.8in; height: 0.5in;
  background: #C9A84C;
}}

.back-cover .bc-content {{
  position: relative;
  z-index: 2;
  flex: 1;
  display: flex;
  flex-direction: column;
}}

.back-cover .bc-blurb-title {{
  font-size: 11pt;
  color: #A89058;
  font-weight: 700;
  letter-spacing: 2pt;
  text-transform: uppercase;
  margin-bottom: 0.15in;
  text-align: center;
}}

.back-cover .bc-blurb {{
  font-size: 9.5pt;
  color: #C8C0B0;
  line-height: 1.65;
  text-align: justify;
  margin-bottom: 0.25in;
}}

.back-cover .bc-divider {{
  width: 1.5in;
  height: 1px;
  background: linear-gradient(90deg, transparent, #8A7438, transparent);
  margin: 0.1in auto;
}}

.back-cover .bc-features {{
  margin-top: 0.1in;
}}

.back-cover .bc-feature {{
  font-size: 9pt;
  color: #C8C0B0;
  line-height: 1.8;
  padding-left: 0.18in;
  position: relative;
}}

/* CSS dot instead of unicode bullet */
.back-cover .bc-feature::before {{
  width: 4px; height: 4px;
  background: #8A7438;
  border-radius: 50%;
  position: absolute;
  left: 0;
  top: 7px;
}}

.back-cover .bc-quote {{
  margin-top: 0.25in;
  padding: 0.12in 0.15in;
  border-left: 1px solid #5A4E30;
  font-size: 9pt;
  font-style: italic;
  color: #A89058;
  line-height: 1.5;
}}

.back-cover .bc-bottom {{
  position: relative;
  z-index: 2;
  margin-top: auto;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}}

.back-cover .bc-pub {{
  font-size: 7pt;
  color: #5A6A85;
  letter-spacing: 2pt;
  text-transform: uppercase;
  margin-bottom: 0.12in;
  align-self: center;
}}

.back-cover .bc-barcode {{
  width: 2in;
  height: 1.2in;
  background: white;
  border: 1px solid #ccc;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 7pt;
  color: #999;
}}

/* ===== SPINE ===== */
.spine {{
  width: {SPINE}in;
  height: {COVER_H}in;
  background: #0A1320;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
}}

.spine .sp-text {{
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  font-size: 10pt;
  color: #A89058;
  font-weight: 700;
  letter-spacing: 3pt;
  text-transform: uppercase;
  white-space: nowrap;
}}

.spine .sp-pub {{
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  font-size: 6pt;
  color: #5A6A85;
  letter-spacing: 2pt;
  text-transform: uppercase;
  position: absolute;
  bottom: 0.6in;
}}

.spine .sp-top-orn {{
  position: absolute;
  top: 0.6in;
  width: 60%;
  height: 1px;
  background: #5A4E30;
}}

.spine .sp-bot-orn {{
  position: absolute;
  bottom: 1.5in;
  width: 60%;
  height: 1px;
  background: #5A4E30;
}}

/* ===== FRONT COVER — "QUIET LUXURY" ===== */
.front-cover {{
  width: {TRIM_W}in;
  height: {COVER_H}in;
  background: #0A1320;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  position: relative;
  overflow: hidden;
  color: white;
  padding: 0.5in 0.5in;
  margin-right: {BLEED}in;
}}

/* TONE-ON-TONE PATTERN LAYER 1: Diagonal lines */
.front-cover .fc-diagonal {{
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.025;
  background-image: repeating-linear-gradient(
    45deg,
    transparent 0px, transparent 40px,
    #C9A84C 40px, #C9A84C 41px);
  z-index: 1;
}}

/* TONE-ON-TONE PATTERN LAYER 2: Subtle dot grid */
.front-cover .fc-dots {{
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  opacity: 0.03;
  background-image: radial-gradient(circle, #C9A84C 0.8px, transparent 1px);
  background-size: 18px 18px;
  z-index: 1;
}}

/* TONE-ON-TONE PATTERN LAYER 3: Large faded cross watermark */
.front-cover .fc-watermark {{
  position: absolute;
  left: 50%; top: 40%;
  transform: translate(-50%, -50%);
  z-index: 1;
  opacity: 0.03;
}}

.front-cover .fc-wm-v {{
  position: absolute;
  left: 50%; top: -1.5in;
  transform: translateX(-50%);
  width: 1.2in; height: 5in;
  background: #C9A84C;
}}

.front-cover .fc-wm-h {{
  position: absolute;
  left: 50%; top: 0;
  transform: translateX(-50%);
  width: 3.5in; height: 1.2in;
  background: #C9A84C;
}}

/* TONE-ON-TONE PATTERN LAYER 4: Corner ornaments */
.front-cover .fc-corner {{
  position: absolute;
  width: 0.8in; height: 0.8in;
  opacity: 0.06;
  z-index: 1;
}}

.front-cover .fc-corner-tl {{
  top: 0.35in; left: 0.35in;
  border-top: 1px solid #C9A84C;
  border-left: 1px solid #C9A84C;
}}

.front-cover .fc-corner-tr {{
  top: 0.35in; right: 0.35in;
  border-top: 1px solid #C9A84C;
  border-right: 1px solid #C9A84C;
}}

.front-cover .fc-corner-bl {{
  bottom: 0.35in; left: 0.35in;
  border-bottom: 1px solid #C9A84C;
  border-left: 1px solid #C9A84C;
}}

.front-cover .fc-corner-br {{
  bottom: 0.35in; right: 0.35in;
  border-bottom: 1px solid #C9A84C;
  border-right: 1px solid #C9A84C;
}}

/* === VISIBLE MAIN ELEMENT (for Amazon thumbnail) === */
/* Small visible cross — the anchor */
.front-cover .fc-cross-wrap {{
  position: relative;
  z-index: 3;
  width: 40px; height: 68px;
  margin: 0 auto 0.35in;
  margin-top: 0.6in;
}}

.front-cover .fc-cross-vert {{
  position: absolute;
  left: 50%; top: 0;
  transform: translateX(-50%);
  width: 9px; height: 68px;
  background: linear-gradient(180deg, #A89058, #8A7438);
  border-radius: 1px;
}}

.front-cover .fc-cross-horiz {{
  position: absolute;
  left: 50%; top: 18px;
  transform: translateX(-50%);
  width: 32px; height: 9px;
  background: linear-gradient(180deg, #A89058, #8A7438);
  border-radius: 1px;
}}

/* Title — MUST be clearly visible */
.front-cover .fc-title-area {{
  position: relative;
  z-index: 3;
}}

.front-cover .fc-title {{
  font-size: 30pt;
  font-weight: 400;
  color: white;
  letter-spacing: 4pt;
  margin-bottom: 0.08in;
}}

.front-cover .fc-ornament {{
  width: 1.5in;
  height: 1px;
  background: linear-gradient(90deg, transparent, #8A7438 30%, #8A7438 70%, transparent);
  margin: 0.15in auto;
}}

.front-cover .fc-subtitle {{
  font-size: 10.5pt;
  font-style: italic;
  color: #A89058;
  max-width: 4in;
  line-height: 1.55;
  margin: 0 auto;
  font-weight: 400;
}}

/* Bottom area */
.front-cover .fc-bottom {{
  position: absolute;
  bottom: 0.65in;
  left: 0; right: 0;
  text-align: center;
  z-index: 3;
}}

.front-cover .fc-verse {{
  font-size: 8.5pt;
  color: #C8C0B0;
  font-style: italic;
  line-height: 1.6;
  max-width: 3.5in;
  margin: 0 auto 0.08in;
}}

.front-cover .fc-verse-ref {{
  font-size: 7pt;
  color: #8A7438;
  letter-spacing: 1.5pt;
  text-transform: uppercase;
}}

.front-cover .fc-pub {{
  font-size: 7pt;
  color: #5A6A85;
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  margin-top: 0.15in;
}}

/* Side-by-side comparison label */
.compare-label {{
  position: absolute;
  top: -28px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 9pt;
  color: #888;
  letter-spacing: 1pt;
  white-space: nowrap;
}}

@media screen {{
  .cover-wrap {{ border: 1px solid #444; margin: 40px auto; position: relative; }}
}}
"""

BACK_BLURB = (
    "Deepen your prayer life one week at a time.\n\n"
    "This guided prayer journal walks you through fifty-two weeks of intentional "
    "communion with God. Each week features a Scripture passage to anchor your "
    "heart, along with generous writing space organized around the time-tested "
    "ACTS prayer model."
)

BACK_FEATURES = [
    "52 undated weekly spreads — start any time, any year",
    "52 Scripture passages from the World English Bible",
    "Guided ACTS prayer sections on every spread",
    "Dedicated Answered Prayers section",
    "Gratitude pages to cultivate a thankful heart",
    "Elegant design for both men and women",
]

def main():
    features_html = "\n".join(
        f'      <div class="bc-feature">{feat}</div>' for feat in BACK_FEATURES
    )

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{BOOK_TITLE} — Cover V1.1 Quiet Luxury</title>
<style>{CSS}</style>
</head>
<body>
<div class="cover-wrap">

  <!-- ====== BACK COVER ====== -->
  <div class="back-cover">
    <div class="bc-subtle-pattern"></div>
    <div class="bc-watermark"></div>
    <div class="bc-content">
      <div class="bc-blurb-title">About This Journal</div>
      <div class="bc-blurb">{BACK_BLURB.replace(chr(10), '<br/>')}</div>
      <div class="bc-divider"></div>
      <div class="bc-features">
{features_html}
      </div>
      <div class="bc-quote">
        "The Lord is near to all who call on him,<br/>
        to all who call on him in truth."<br/>
        <span style="font-size:7.5pt;color:#8A7438;font-style:normal;letter-spacing:1pt;">PSALM 145:18 (WEB)</span>
      </div>
    </div>
    <div class="bc-bottom">
      <div class="bc-pub">{PUBLISHER}</div>
      <div class="bc-barcode">Barcode Area</div>
    </div>
  </div>

  <!-- ====== SPINE ====== -->
  <div class="spine">
    <div class="sp-top-orn"></div>
    <div class="sp-text">{BOOK_TITLE}</div>
    <div class="sp-bot-orn"></div>
    <div class="sp-pub">{PUBLISHER}</div>
  </div>

  <!-- ====== FRONT COVER ====== -->
  <div class="front-cover">
    <!-- Hidden pattern layers -->
    <div class="fc-diagonal"></div>
    <div class="fc-dots"></div>
    <div class="fc-watermark">
      <div class="fc-wm-v"></div>
      <div class="fc-wm-h"></div>
    </div>
    <div class="fc-corner fc-corner-tl"></div>
    <div class="fc-corner fc-corner-tr"></div>
    <div class="fc-corner fc-corner-bl"></div>
    <div class="fc-corner fc-corner-br"></div>

    <!-- Visible main elements -->
    <div class="fc-cross-wrap">
      <div class="fc-cross-vert"></div>
      <div class="fc-cross-horiz"></div>
    </div>
    <div class="fc-title-area">
      <div class="fc-title">{BOOK_TITLE}</div>
      <div class="fc-ornament"></div>
      <div class="fc-subtitle">{BOOK_SUBTITLE}</div>
    </div>
    <div class="fc-bottom">
      <div class="fc-verse">
        "Call to me, and I will answer you,<br/>
        and will show you great things."
      </div>
      <div class="fc-verse-ref">Jeremiah 33:3 (WEB)</div>
      <div class="fc-pub">{PUBLISHER}</div>
    </div>
  </div>

</div>
</body>
</html>'''

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Generated: {HTML_FILE}")
    print(f"V1.1 'Quiet Luxury' design features:")
    print(f"  - Tone-on-tone diagonal lines (opacity 0.025)")
    print(f"  - Subtle gold dot grid (opacity 0.03)")
    print(f"  - Large faded cross watermark (opacity 0.03)")
    print(f"  - Corner ornaments (opacity 0.06)")
    print(f"  - Muted gold tones (#8A7438 vs V1.0's brighter #C9A84C)")
    print(f"  - Title: lighter weight (400 vs 700) for elegance")
    print(f"  - All hidden patterns only visible on close inspection")


if __name__ == "__main__":
    main()
