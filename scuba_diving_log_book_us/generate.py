#!/usr/bin/env python3
"""
Scuba Diving Log Book — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Certified scuba divers, recreational divers, dive enthusiasts
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "scuba_diving_log_book_us_V1.0.html")

BOOK_TITLE = "Scuba Diving Log Book"
BOOK_SUBTITLE = "Every Dive, Every Depth, Every Adventure"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

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

/* ================ COVER ================ */
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
    radial-gradient(ellipse 18px 11px at 90% 40%, #C4A04A, transparent);
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
      <!-- Diver mask -->
      <ellipse cx="60" cy="38" rx="22" ry="14" stroke="#C4A04A" stroke-width="2" fill="rgba(196,160,74,0.1)"/>
      <rect x="42" y="28" width="36" height="6" rx="2" stroke="#C4A04A" stroke-width="1.5" fill="none"/>
      <!-- Snorkel -->
      <path d="M 80 28 L 88 28 L 88 12" stroke="#C4A04A" stroke-width="2" fill="none" stroke-linecap="round"/>
      <!-- Tank -->
      <rect x="48" y="55" width="24" height="40" rx="3" stroke="#C4A04A" stroke-width="2" fill="rgba(196,160,74,0.08)"/>
      <rect x="54" y="50" width="12" height="6" rx="2" stroke="#C4A04A" stroke-width="1.5" fill="none"/>
      <!-- Reg hose -->
      <path d="M 72 68 Q 80 65 82 60" stroke="#C4A04A" stroke-width="1.5" fill="none"/>
      <!-- Bubbles -->
      <circle cx="30" cy="30" r="4" fill="none" stroke="#C4A04A" stroke-width="0.8" opacity="0.4"/>
      <circle cx="24" cy="20" r="3" fill="none" stroke="#C4A04A" stroke-width="0.6" opacity="0.3"/>
      <circle cx="35" cy="12" r="2.5" fill="none" stroke="#C4A04A" stroke-width="0.5" opacity="0.2"/>
      <circle cx="92" cy="40" r="3.5" fill="none" stroke="#C4A04A" stroke-width="0.7" opacity="0.35"/>
      <circle cx="98" cy="30" r="2.5" fill="none" stroke="#C4A04A" stroke-width="0.5" opacity="0.25"/>
      <!-- Water ripples -->
      <path d="M 20 100 Q 35 97 50 100 Q 65 103 80 100 Q 95 97 105 100"
        stroke="#C4A04A" stroke-width="0.8" fill="none" opacity="0.3"/>
      <path d="M 25 106 Q 40 103 55 106 Q 70 109 85 106 Q 100 103 105 106"
        stroke="#C4A04A" stroke-width="0.6" fill="none" opacity="0.2"/>
    </svg>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">50 Dive Logs</span>
      <span class="feature-badge">Gear Tracker</span>
      <span class="feature-badge">Dive Sites</span>
      <span class="feature-badge">Safety Guide</span>
    </div>
    <div class="tagline">Descend &middot; Explore &middot; Remember</div>
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
    <div style="font-size: 16pt; font-weight: 700; color: #161616; margin-bottom: 6px;">This Log Book Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #161616; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Certification Level</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Certification Agency</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Total Dives to Date</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Favorite Dive Site</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Scuba Diving Log Book</span>
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

  <div class="page-title">How to Use This Log Book</div>
  <div class="page-subtitle">Your personal record of every dive</div>

  <div class="info-box">
    <div class="info-title">Why Keep a Dive Log?</div>
    A dive log is more than a record &mdash; it is proof of your experience, a tool for tracking your air consumption and comfort at depth, and a passport to deeper adventures. Dive operators worldwide require log books as evidence of your certification level and dive count. Your log tells the story of your underwater journey.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">What to Record Every Dive</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Log immediately.</strong> Record depth, time, and air while the details are fresh. Waiting even a few hours means forgetting key data.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Track your gas.</strong> Start pressure, end pressure, and breathing rate reveal your air consumption trends and help you plan future dives.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. Record conditions.</strong> Water temperature, visibility, current, and surge affect every dive. Note what gear configuration worked best.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Note the wildlife.</strong> The creatures you encounter make each dive unique. From reef fish to pelagics, your log becomes a marine life journal.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Reflect on skills.</strong> What went well? What needs improvement? Buoyancy, navigation, air management &mdash; track your growth as a diver.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Pro Tip:</strong> Use a waterproof dive slate underwater to note depth, time, and air. Transfer the data to your log book on the surface.
  </div>

  <div class="page-footer">
    <span>Scuba Diving Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def dive_safety_tips():
    return f'''
<!-- Page {pn()}: Dive Safety Tips -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Safety Essentials</span>
  </div>

  <div class="page-title">Dive Safety Essentials</div>
  <div class="page-subtitle">Plan the dive, dive the plan</div>

  <div style="font-size: 8.5pt; line-height: 1.6; color: #333;">

    <div style="margin-bottom: 8px; padding: 6px 10px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
      <div style="font-size: 8pt; font-weight: 700; color: #161616; margin-bottom: 2px;">Plan Your Dive</div>
      <div style="font-size: 7.5pt; color: #555; line-height: 1.4;">Agree on max depth, bottom time, and air turn-around point with your buddy before entering the water.</div>
    </div>

    <div style="margin-bottom: 8px; padding: 6px 10px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
      <div style="font-size: 8pt; font-weight: 700; color: #161616; margin-bottom: 2px;">Buddy System</div>
      <div style="font-size: 7.5pt; color: #555; line-height: 1.4;">Stay close to your buddy. Perform buddy checks before every dive &mdash; BCD, Weights, Releases, Air, Final check.</div>
    </div>

    <div style="margin-bottom: 8px; padding: 6px 10px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
      <div style="font-size: 8pt; font-weight: 700; color: #161616; margin-bottom: 2px;">Ascend Slowly</div>
      <div style="font-size: 7.5pt; color: #555; line-height: 1.4;">Never exceed 30 feet (9 meters) per minute. A safety stop at 15 feet for 3 minutes is mandatory on every dive deeper than 30 feet.</div>
    </div>

    <div style="margin-bottom: 8px; padding: 6px 10px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
      <div style="font-size: 8pt; font-weight: 700; color: #161616; margin-bottom: 2px;">Monitor Your Air</div>
      <div style="font-size: 7.5pt; color: #555; line-height: 1.4;">Check your pressure gauge frequently. Turn the dive when you reach the agreed reserve &mdash; typically 500 psi / 50 bar.</div>
    </div>

    <div style="margin-bottom: 8px; padding: 6px 10px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
      <div style="font-size: 8pt; font-weight: 700; color: #161616; margin-bottom: 2px;">Equalize Early</div>
      <div style="font-size: 7.5pt; color: #555; line-height: 1.4;">Equalize your ears before feeling discomfort. If you cannot equalize, ascend slightly and try again. Never force it.</div>
    </div>

    <div style="margin-bottom: 8px; padding: 6px 10px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
      <div style="font-size: 8pt; font-weight: 700; color: #161616; margin-bottom: 2px;">Dive Within Your Limits</div>
      <div style="font-size: 7.5pt; color: #555; line-height: 1.4;">Stay within your certification level. If something feels wrong, call the dive. Any diver can end a dive at any time for any reason.</div>
    </div>

  </div>

  <div style="margin-top: 10px; padding: 6px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 7.5pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Remember:</strong> This log book is a personal record. It does not replace proper training. Always follow your certifying agency's standards and local diving regulations.
  </div>

  <div class="page-footer">
    <span>Scuba Diving Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def dive_types_guide():
    types = [
        ("Reef Dive", "The most popular recreational dive. Explore coral gardens teeming with marine life. Depths typically 15-80 feet."),
        ("Wall Dive", "Follow a vertical drop-off into the deep blue. Spectacular visibility and pelagic encounters. Watch your depth gauge closely."),
        ("Wreck Dive", "Explore sunken ships, planes, and artificial reefs. Requires additional training for penetration. Rich in history and marine life."),
        ("Drift Dive", "Float with the current while the boat follows. Effortless and exhilarating. Requires a surface marker buoy (SMB)."),
        ("Night Dive", "Experience the underwater world after dark. Different marine life emerges. Requires a primary dive light and backup."),
        ("Cavern/Cave Dive", "Explore overhead environments. Requires specialized cave diving certification. Always maintain a continuous guideline to the surface."),
        ("Deep Dive", "Beyond 60 feet (18m). Requires deep diver specialty training. Shorter bottom times due to nitrogen absorption."),
        ("Shore Dive", "Enter from the beach. Economical and flexible. Plan your exit point and tide conditions carefully."),
    ]

    rows = ""
    for name, desc in types:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 95px; font-size: 8pt; font-weight: 700; color: #161616;">{name}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4; flex: 1;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Dive Types -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Dive Types</span>
  </div>

  <div class="page-title">Types of Diving</div>
  <div class="page-subtitle">Know your dive environments</div>

  {rows}

  <div class="page-footer">
    <span>Scuba Diving Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def hand_signals_reference():
    signals = [
        ("OK", "Touch thumb and index finger to form a circle. Used both on surface and underwater."),
        ("Stop / Hold", "Palm facing outward, fingers up. Signal to stop and hold position."),
        ("Go Up / Ascend", "Thumb up. Signal that you or the group should ascend."),
        ("Go Down / Descend", "Thumb down. Signal to descend or go deeper."),
        ("Out of Air", "Hand slashing across the throat. Emergency signal &mdash; buddy must share air immediately."),
        ("Low on Air", "Clenched fist moved in a cutting motion across the chest. Signal that air supply is running low."),
        ("How Much Air?", "Fingers and thumb tapping together. Asking buddy to show their pressure gauge."),
        ("Something Wrong", "Flat hand waved side to side, palm down. Followed by pointing to the problem area."),
        ("Look at Me", "Point two fingers at own eyes. Direct buddy's attention to you."),
        ("Danger / Hazard", "Closed fist. Used to warn of danger or signal buddy to pay attention."),
    ]

    rows = ""
    for name, desc in signals:
        rows += f'''
      <div style="margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="font-size: 8pt; font-weight: 700; color: #161616; margin-bottom: 1px;">{name}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Hand Signals -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Hand Signals</span>
  </div>

  <div class="page-title">Essential Hand Signals</div>
  <div class="page-subtitle">Silent communication underwater</div>

  {rows}

  <div style="margin-top: 8px; padding: 6px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 7.5pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Signal Tip:</strong> Always respond to a signal &mdash; even a simple "OK" back confirms you saw and understood. Underwater communication is a two-way agreement.
  </div>

  <div class="page-footer">
    <span>Scuba Diving Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def gas_management_reference():
    return f'''
<!-- Page {pn()}: Gas Management -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Gas Management</span>
  </div>

  <div class="page-title">Understanding Air Consumption</div>
  <div class="page-subtitle">Track your breathing rate to dive smarter</div>

  <div class="info-box">
    <div class="info-title">Why Track Your Air?</div>
    Your breathing rate (Surface Air Consumption, or SAC rate) is one of the most important personal metrics in diving. Knowing your SAC helps you plan dive times, choose the right cylinder, and dive with confidence. It varies with depth, exertion, stress, and experience.
  </div>

  <div style="font-size: 8pt; line-height: 1.6; color: #333;">

    <div style="font-weight: 700; color: #161616; font-size: 9pt; margin-bottom: 6px;">How to Calculate SAC Rate</div>

    <div style="margin-bottom: 8px; padding: 6px 8px; background: #FAF6F0; border-radius: 3px;">
      <div style="font-size: 7.5pt; color: #555; line-height: 1.5;">
        <strong>SAC (psi/min)</strong> = Air Used (psi) &divide; Bottom Time (min) &divide; Pressure at Depth (ATA)
      </div>
    </div>

    <div style="margin-bottom: 8px;">
      <strong>Example:</strong> You start with 3000 psi, finish with 1000 psi after a 40-minute dive at an average depth of 33 feet (2 ATA).
    </div>

    <div style="margin-bottom: 8px; padding: 6px 8px; background: #FAF6F0; border-radius: 3px;">
      <div style="font-size: 7.5pt; color: #555; line-height: 1.5;">
        Air used = 3000 &minus; 1000 = 2000 psi<br>
        SAC = 2000 &divide; 40 &divide; 2 = <strong>25 psi/min</strong>
      </div>
    </div>

    <div style="font-weight: 700; color: #161616; font-size: 9pt; margin-top: 10px; margin-bottom: 6px;">Typical SAC Rates</div>

    <table class="data-table" style="font-size: 7.5pt;">
      <tr><th>Experience Level</th><th>SAC Rate (psi/min)</th><th>SAC Rate (L/min)</th></tr>
      <tr><td>Beginner</td><td>25-35</td><td>20-28</td></tr>
      <tr><td>Intermediate</td><td>20-28</td><td>16-22</td></tr>
      <tr><td>Experienced</td><td>15-22</td><td>12-18</td></tr>
      <tr><td>Expert / Technical</td><td>12-18</td><td>10-15</td></tr>
    </table>

  </div>

  <div style="margin-top: 10px; padding: 6px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 7.5pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Track Your Progress:</strong> Record start pressure, end pressure, depth, and bottom time for every dive. Over time, you will see your SAC rate improve as your buoyancy and relaxation underwater get better.
  </div>

  <div class="page-footer">
    <span>Scuba Diving Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def divider_section(num, title, subtitle):
    labels = ["One", "Two", "Three", "Four", "Five", "Six", "Seven"]
    label_text = labels[num-1] if num <= 7 else ""
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


def dive_log_left(entry_num):
    """Left page: dive details, depth/time profile"""
    return f'''
<!-- Page {pn()}: Dive {entry_num} Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Dive #{entry_num:03d}</span>
    <span class="sh-right">Details</span>
  </div>

  <div class="page-title">Dive #{entry_num:03d}</div>
  <div class="page-subtitle">The full story of every descent</div>

  <!-- Dive Info -->
  <div style="background: #FAF6F0; border-radius: 4px; padding: 8px 10px; margin-bottom: 10px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 10px;">
      <div style="display:flex;align-items:baseline;gap:4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 42px;">Date</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
      <div style="display:flex;align-items:baseline;gap:4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 42px;">Time In</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
      <div style="display:flex;align-items:baseline;gap:4px;grid-column:span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 42px;">Location</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
      <div style="display:flex;align-items:baseline;gap:4px;grid-column:span 2;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 42px;">Dive Site</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
      <div style="display:flex;align-items:baseline;gap:4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 42px;">Buddy</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
      <div style="display:flex;align-items:baseline;gap:4px;">
        <span style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; min-width: 42px;">Boat/Shore</span>
        <div style="flex:1;border-bottom:0.5px solid #aaa;height:14px;"></div>
      </div>
    </div>
  </div>

  <!-- Dive Type -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Dive Type</div>
  <div class="check-row" style="margin-bottom: 10px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Reef</span>
    <span class="check-item"><span class="check-box"></span> Wall</span>
    <span class="check-item"><span class="check-box"></span> Wreck</span>
    <span class="check-item"><span class="check-box"></span> Drift</span>
    <span class="check-item"><span class="check-box"></span> Night</span>
    <span class="check-item"><span class="check-box"></span> Deep</span>
    <span class="check-item"><span class="check-box"></span> Cavern</span>
    <span class="check-item"><span class="check-box"></span> Shore</span>
  </div>

  <!-- Depth & Time -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Depth &amp; Time</div>
  <table class="data-table" style="font-size: 7.5pt; margin-bottom: 10px;">
    <tr>
      <th>Max Depth</th>
      <th>Avg Depth</th>
      <th>Bottom Time</th>
      <th>Total Time</th>
    </tr>
    <tr><td></td><td></td><td></td><td></td></tr>
  </table>

  <!-- Gas -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Gas / Air</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4px 10px; margin-bottom: 10px;">
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;">Start</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;">End</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;">Used</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
  </div>

  <!-- Conditions -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Conditions</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-bottom:10px;">
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;">Vis</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;">Water</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;">Air</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
  </div>
  <div class="check-row" style="margin-bottom: 8px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Calm</span>
    <span class="check-item"><span class="check-box"></span> Current</span>
    <span class="check-item"><span class="check-box"></span> Surge</span>
    <span class="check-item"><span class="check-box"></span> Waves</span>
  </div>

  <div class="page-footer">
    <span>Dive #{entry_num:03d} &mdash; Details</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def dive_log_right(entry_num):
    """Right page: gear, wildlife, notes"""
    return f'''
<!-- Page {pn()}: Dive {entry_num} Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Dive #{entry_num:03d}</span>
    <span class="sh-right">Notes &amp; Wildlife</span>
  </div>

  <div class="page-title">Dive #{entry_num:03d}</div>
  <div class="page-subtitle">Gear, wildlife, and memories</div>

  <!-- Exposure Protection -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Exposure Protection</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px 10px; margin-bottom: 10px;">
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;min-width:38px;">Suit</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;min-width:38px;">Weight</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;min-width:38px;">Cylinder</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
    <div style="display:flex;align-items:baseline;gap:4px;">
      <span style="font-size:7pt;font-weight:700;color:#161616;text-transform:uppercase;min-width:38px;">Gas Mix</span>
      <div style="flex:1;border-bottom:0.5px solid #aaa;height:12px;"></div>
    </div>
  </div>

  <!-- Marine Life -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Marine Life Spotted</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Dive Highlights -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 4px;">Dive Highlights</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <!-- Skills Practiced -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 4px;">Skills Practiced</div>
  <div class="check-row" style="margin-bottom: 8px; font-size: 8pt;">
    <span class="check-item"><span class="check-box"></span> Buoyancy</span>
    <span class="check-item"><span class="check-box"></span> Navigation</span>
    <span class="check-item"><span class="check-box"></span> Photography</span>
    <span class="check-item"><span class="check-box"></span> SMB Deploy</span>
  </div>

  <!-- Dive Summary -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 4px;">Dive Summary</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;">
    <div class="stat-card" style="padding:6px;"><div class="stat-label">SAC Rate</div><div class="stat-value" style="font-size:11pt;"></div></div>
    <div class="stat-card" style="padding:6px;"><div class="stat-label">Rating</div><div class="stat-value" style="font-size:11pt;"></div></div>
    <div class="stat-card" style="padding:6px;"><div class="stat-label">Would Repeat</div><div class="stat-value" style="font-size:11pt;"></div></div>
  </div>

  <div class="page-footer">
    <span>Dive #{entry_num:03d} &mdash; Notes</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def quick_log(page_of, total_pages):
    """One-line-per-dive quick log"""
    rows = ""
    for i in range(1, 16):
        start = (page_of - 1) * 15 + i
        rows += f'''<tr><td style="font-weight:700;color:#C4A04A;">{start}</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>\n'''

    return f'''
<!-- Page {pn()}: Quick Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Quick Dive Log</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Quick Dive Log</div>
  <div class="page-subtitle">Every dive at a glance</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th style="width:42px;">Date</th>
      <th>Location</th>
      <th style="width:35px;">Depth</th>
      <th style="width:30px;">Time</th>
      <th style="width:35px;">Air</th>
      <th style="width:35px;">Temp</th>
    </tr>
    {rows}
  </table>

  <div class="page-footer">
    <span>Scuba Diving Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def dive_sites_tracker():
    """Best dive sites tracker"""
    rows = ""
    for i in range(1, 16):
        rows += f'<tr><td style="font-weight:700;color:#C4A04A;">{i}</td><td></td><td></td><td></td><td></td></tr>\n'

    return f'''
<!-- Page {pn()}: Dive Sites -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Dive Sites</span>
    <span class="sh-right">Favorite Spots</span>
  </div>

  <div class="page-title">Favorite Dive Sites</div>
  <div class="page-subtitle">Your personal map of underwater adventures</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Site Name / Location</th>
      <th style="width:45px;">Max Depth</th>
      <th style="width:45px;">Best Season</th>
      <th style="width:55px;">Highlights</th>
    </tr>
    {rows}
  </table>

  <div class="page-footer">
    <span>Scuba Diving Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def personal_records():
    """Personal diving records and milestones"""
    return f'''
<!-- Page {pn()}: Personal Records -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Personal Records</span>
    <span class="sh-right">Milestones</span>
  </div>

  <div class="page-title">Personal Records</div>
  <div class="page-subtitle">Your deepest, longest, and most memorable</div>

  <table class="data-table" style="font-size: 8pt;">
    <tr>
      <th style="width:100px;">Category</th>
      <th style="width:45px;">Value</th>
      <th style="width:55px;">Date</th>
      <th>Location</th>
    </tr>
    <tr><td style="font-weight:700;color:#161616;">Deepest Dive</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Longest Dive</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Coldest Water</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Visibility</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">First Night Dive</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">First Wreck</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Best Air Consumption</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Most Marine Life</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Rarest Creature</td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#161616;">Most Memorable</td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Certification Milestones</div>
    <table class="data-table" style="font-size: 7.5pt;">
      <tr><th>Certification</th><th style="width:55px;">Date</th><th style="width:55px;">Agency</th><th style="width:45px;">Instructor</th></tr>
      <tr><td style="font-weight:700;color:#161616;">Open Water</td><td></td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Advanced</td><td></td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Rescue</td><td></td><td></td><td></td></tr>
      <tr><td style="font-weight:700;color:#161616;">Specialty</td><td></td><td></td><td></td></tr>
    </table>
  </div>

  <div class="page-footer">
    <span>Scuba Diving Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def gear_inventory():
    """Gear inventory tracker"""
    categories = [
        ("Exposure Protection", ["Wetsuit / Drysuit", "Hood", "Gloves", "Boots", "Vest / Rash Guard"]),
        ("BCD &amp; Regulator", ["BCD", "Primary Regulator", "Octopus / Alternate", "Pressure Gauge (SPG)", "Depth Gauge / Computer"]),
        ("Cylinders &amp; Weights", ["Primary Cylinder", "Pony Bottle", "Weight Belt", "Integrated Weights", "Weight Amount"]),
        ("Accessories", ["Dive Mask", "Snorkel", "Fins", "Dive Light", "SMB / Surface Marker"]),
    ]

    sections = ""
    for cat_name, items in categories:
        item_rows = ""
        for item in items:
            item_rows += f'''
          <tr><td style="font-size:7.5pt;">{item}</td><td></td><td></td><td style="text-align:center;"></td></tr>'''
        sections += f'''
      <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 8px; margin-bottom: 4px;">{cat_name}</div>
      <table class="data-table" style="font-size: 7.5pt;">
        <tr><th>Item</th><th style="width:50px;">Brand / Model</th><th style="width:40px;">Size</th><th style="width:22px;">OK?</th></tr>
        {item_rows}
      </table>'''

    return f'''
<!-- Page {pn()}: Gear Inventory -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Gear Inventory</span>
    <span class="sh-right">Equipment Tracker</span>
  </div>

  <div class="page-title">Gear Inventory</div>
  <div class="page-subtitle">Know your kit and its condition</div>

  {sections}

  <div class="page-footer">
    <span>Scuba Diving Log Book</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def gear_service_log():
    """Gear maintenance and service log"""
    return f'''
<!-- Page {pn()}: Gear Service Log -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Gear Service Log</span>
    <span class="sh-right">Maintenance Record</span>
  </div>

  <div class="page-title">Gear Service Log</div>
  <div class="page-subtitle">Track maintenance and inspections</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Item</th>
      <th style="width:50px;">Service Type</th>
      <th style="width:40px;">Date</th>
      <th style="width:55px;">Technician</th>
      <th style="width:30px;">Next Due</th>
    </tr>
    <tr><td style="font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td style="font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>

  <div style="margin-top: 14px; padding: 6px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 7.5pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">Service Reminder:</strong> Regulators should be professionally serviced annually. BCDs and cylinders need visual inspections yearly and hydrostatic testing every five years.
  </div>

  <div class="page-footer">
    <span>Scuba Diving Log Book</span>
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

  <div class="page-title">Dive Notes</div>
  <div class="page-subtitle">Tips, patterns, and future dive plans</div>

  {lines}

  <div class="page-footer">
    <span>Scuba Diving Log Book</span>
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
    pages.append(cover_page())                          # 1
    pages.append(owner_page())                           # 2

    # ---- Reference Section ----
    pages.append(how_to_use())                           # 3
    pages.append(dive_safety_tips())                     # 4
    pages.append(dive_types_guide())                     # 5
    pages.append(hand_signals_reference())               # 6
    pages.append(gas_management_reference())             # 7

    # ---- Section 1: Dive Logs ----
    pages.append(divider_section(1, "Dive Logs", "50 dives &mdash; detailed records of every descent"))
    NUM_DIVES = 50
    for i in range(1, NUM_DIVES + 1):
        pages.append(dive_log_left(i))
        pages.append(dive_log_right(i))

    # ---- Section 2: Quick Dive Log ----
    pages.append(divider_section(2, "Quick Dive Log", "Every dive at a glance"))
    pages.append(quick_log(1, 4))
    pages.append(quick_log(2, 4))
    pages.append(quick_log(3, 4))
    pages.append(quick_log(4, 4))

    # ---- Section 3: Sites & Records ----
    pages.append(divider_section(3, "Sites &amp; Records", "Your best dive sites and personal milestones"))
    pages.append(dive_sites_tracker())
    pages.append(personal_records())

    # ---- Section 4: Gear ----
    pages.append(divider_section(4, "Gear &amp; Equipment", "Track your kit and its maintenance"))
    pages.append(gear_inventory())
    pages.append(gear_service_log())

    # ---- Section 5: Notes ----
    pages.append(divider_section(5, "Notes", "Tips, patterns, and future dive plans"))
    for i in range(4):
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
    print(f"  How to use: 1")
    print(f"  Dive safety: 1")
    print(f"  Dive types: 1")
    print(f"  Hand signals: 1")
    print(f"  Gas management: 1")
    print(f"  Section dividers: 5")
    print(f"  Dive logs ({NUM_DIVES} x 2): {NUM_DIVES * 2}")
    print(f"  Quick dive log: 4")
    print(f"  Dive sites: 1")
    print(f"  Personal records: 1")
    print(f"  Gear inventory: 1")
    print(f"  Gear service log: 1")
    print(f"  Notes pages: 4")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
