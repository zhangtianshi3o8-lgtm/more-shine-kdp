#!/usr/bin/env python3
"""
Prayer Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English | Pages: ~128
Target: American Christians (all genders, all denominations)
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.

Design philosophy:
  - ACTS prayer model (Adoration, Confession, Thanksgiving, Supplication)
  - 52 undated weekly spreads — evergreen, works any year
  - Generous writing space (addresses #1 complaint: "not enough room")
  - Answered Prayers section (tracks God's faithfulness over time)
  - Gender-neutral, elegant, timeless aesthetic
  - Scripture from the World English Bible (WEB) — public domain
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "prayer_journal_us_V1.0.html")

BOOK_TITLE = "Prayer Journal"
BOOK_SUBTITLE = "A 52-Week Guided Journal for Prayer, Scripture & Gratitude"
PUBLISHER = "More Shine Press"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

# ============================================================
# 52 SCRIPTURE VERSES (World English Bible — public domain)
# One per week, flowing through themes of the Christian life
# ============================================================
SCRIPTURES = [
    ("Philippians 4:6-7", "In nothing be anxious, but in everything, by prayer and petition with thanksgiving, let your requests be made known to God. And the peace of God, which surpasses all understanding, will guard your hearts and your thoughts in Christ Jesus."),
    ("Jeremiah 33:3", "Call to me, and I will answer you, and will show you great things, and difficult, which you don't know."),
    ("Matthew 7:7-8", "Ask, and it will be given you. Seek, and you will find. Knock, and it will be opened for you. For everyone who asks receives. He who seeks finds. To him who knocks it will be opened."),
    ("1 Thessalonians 5:16-18", "Rejoice always. Pray without ceasing. In everything give thanks, for this is the will of God in Christ Jesus toward you."),
    ("James 5:16", "Confess your offenses to one another, and pray for one another, that you may be healed. The insistent prayer of a righteous person is powerfully effective."),
    ("Psalm 34:17", "The righteous cry, and the LORD hears, and delivers them out of all their troubles."),
    ("John 15:7", "If you remain in me, and my words remain in you, you will ask whatever you desire, and it will be done for you."),
    ("Proverbs 3:5-6", "Trust in the LORD with all your heart, and don't lean on your own understanding. In all your ways acknowledge him, and he will make your paths straight."),
    ("Psalm 46:10", "Be still, and know that I am God. I will be exalted among the nations. I will be exalted in the earth."),
    ("Ephesians 6:18", "With all prayer and requests, praying at all times in the Spirit, and being watchful to this end in all perseverance and requests for all the saints."),
    ("Hebrews 4:16", "Let's therefore draw near with boldness to the throne of grace, that we may receive mercy, and may find grace for help in time of need."),
    ("Psalm 145:18-19", "The LORD is near to all those who call on him, to all who call on him in truth. He will fulfill the desire of those who fear him. He also will hear their cry, and will save them."),
    ("Matthew 6:6", "But you, when you pray, enter into your inner chamber, and having shut your door, pray to your Father who is in secret; and your Father who sees in secret will reward you openly."),
    ("Romans 8:26", "In the same way, the Spirit also helps our weaknesses, for we don't know how to pray as we ought. But the Spirit himself makes intercession for us with groanings which can't be uttered."),
    ("1 John 5:14", "This is the boldness which we have toward him, that, if we ask anything according to his will, he listens to us."),
    ("Psalm 5:3", "The LORD, in the morning I will direct my prayer to you, and will look up."),
    ("Mark 11:24", "Therefore I tell you, all things whatever you pray and ask for, believe that you have received them, and you shall have them."),
    ("Colossians 4:2", "Continue steadfastly in prayer, watching in it with thanksgiving."),
    ("Psalm 121:1-2", "I will lift up my eyes to the hills. Where does my help come from? My help comes from the LORD, who made heaven and earth."),
    ("Isaiah 40:31", "But those who wait for the LORD will renew their strength. They will mount up with wings like eagles. They will run, and not be weary. They will walk, and not faint."),
    ("Lamentations 3:22-23", "It is of the LORD's loving kindnesses that we are not consumed, because his compassion doesn't fail. They are new every morning; great is your faithfulness."),
    ("Psalm 23:1-3", "The LORD is my shepherd; I shall lack nothing. He makes me lie down in green pastures. He leads me beside still waters. He restores my soul."),
    ("Matthew 11:28", "Come to me, all you who labor and are heavily burdened, and I will give you rest."),
    ("James 1:5", "But if any of you lacks wisdom, let him ask of God, who gives to all liberally and without reproach; and it will be given to him."),
    ("Psalm 37:4-5", "Also delight yourself in the LORD, and he will give you the desires of your heart. Commit your way to the LORD; trust also in him, and he will do this."),
    ("2 Chronicles 7:14", "If my people, who are called by my name, will humble themselves and pray, and seek my face, and turn from their wicked ways; then I will hear from heaven, will forgive their sin, and will heal their land."),
    ("John 14:13-14", "Whatever you will ask in my name, that will I do, that the Father may be glorified in the Son. If you will ask anything in my name, I will do it."),
    ("Psalm 91:1-2", "He who dwells in the secret place of the Most High will rest in the shadow of the Almighty. I will say of the LORD, 'He is my refuge and my fortress; my God, in whom I trust.'"),
    ("1 Peter 5:6-7", "Humble yourselves therefore under the mighty hand of God, that he may exalt you in due time; casting all your worries on him, because he cares for you."),
    ("Psalm 139:23-24", "Search me, God, and know my heart. Try me, and know my thoughts. See if there is any wicked way in me, and lead me in the everlasting way."),
    ("Zephaniah 3:17", "The LORD, your God, is among you, a mighty one who will save. He will rejoice over you with joy. He will calm you in his love. He will rejoice over you with singing."),
    ("Matthew 6:33", "But seek first God's Kingdom, and his righteousness; and all these things will be given to you as well."),
    ("2 Corinthians 12:9", "He has said to me, 'My grace is sufficient for you, for my power is made perfect in weakness.' Most gladly therefore I will rather glory in my weaknesses, that the power of Christ may rest on me."),
    ("Psalm 16:11", "You will show me the path of life. In your presence is fullness of joy. In your right hand there are pleasures for evermore."),
    ("Galatians 5:22-23", "But the fruit of the Spirit is love, joy, peace, patience, kindness, goodness, faith, gentleness, and self-control. Against such things there is no law."),
    ("Isaiah 41:10", "Don't be afraid, for I am with you. Don't be dismayed, for I am your God. I will strengthen you. Yes, I will help you. Yes, I will uphold you with the right hand of my righteousness."),
    ("Psalm 27:14", "Wait for the LORD. Be strong, and let your heart take courage. Yes, wait for the LORD."),
    ("Romans 12:12", "rejoicing in hope; enduring in troubles; continuing steadfastly in prayer."),
    ("Joshua 1:9", "Haven't I commanded you? Be strong and courageous. Don't be afraid, neither be dismayed: for the LORD your God is with you wherever you go."),
    ("Psalm 63:1", "God, you are my God. I will earnestly seek you. My soul thirsts for you. My flesh longs for you, in a dry and weary land, where there is no water."),
    ("1 Chronicles 16:11", "Seek the LORD and his strength. Seek his face forever more."),
    ("Matthew 21:22", "All things, whatever you ask in prayer, believing, you will receive."),
    ("Psalm 9:10", "Those who know your name will put their trust in you, for you, LORD, have not forsaken those who seek you."),
    ("Philippians 4:19", "My God will supply every need of yours according to his riches in glory in Christ Jesus."),
    ("Deuteronomy 31:6", "Be strong and courageous. Don't be afraid or scared of them; for the LORD your God, he it is who goes with you. He will not fail you nor forsake you."),
    ("Psalm 40:1", "I waited patiently for the LORD. He turned to me, and heard my cry."),
    ("2 Timothy 1:7", "For God didn't give us a spirit of fear, but of power, love, and self-control."),
    ("Psalm 118:24", "This is the day that the LORD has made. We will rejoice and be glad in it."),
    ("Romans 8:28", "We know that all things work together for good for those who love God, for those who are called according to his purpose."),
    ("Psalm 46:1", "God is our refuge and strength, a very present help in trouble."),
    ("Jude 1:20", "But you, beloved, keep building up yourselves on your most holy faith, praying in the Holy Spirit."),
    ("1 Corinthians 16:13-14", "Watch! Stand firm in the faith! Be courageous! Be strong! Let all that you do be done in love."),
]

assert len(SCRIPTURES) == 52, f"Expected 52 scriptures, got {len(SCRIPTURES)}"

# ============================================================
# CSS
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

/* ---- Color Palette ---- */
/* Navy:   #1B2A4A, #0F1B33, #2D3E5F */
/* Gold:   #C9A84C, #D4B968, #B8941C */
/* Cream:  #FAF8F3, #F5F0E6 */
/* Slate:  #4A5568, #718096 */
/* Lines:  #D0CCBE (warm light gray for writing lines) */

.page {
  width: 6in; height: 9in;
  page-break-after: always;
  position: relative;
  background: white;
  overflow: hidden;
}
.page:last-child { page-break-after: auto; }

/* Alternating gutter margins for perfect binding */
.page.recto { padding: 0.50in 0.50in 0.40in 0.75in; }  /* gutter on left */
.page.verso { padding: 0.50in 0.75in 0.40in 0.50in; }  /* gutter on right */

@media screen { .page { border: 1px dashed #ccc; margin: 8px auto; } }
@media print  { .page { border: none; margin: 0; } }

/* ================ TITLE PAGE ================ */
.title-page {
  width: 6in; height: 9in;
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  text-align: center;
  background: linear-gradient(160deg, #0F1B33 0%, #1B2A4A 40%, #1B2A4A 60%, #0F1B33 100%);
  color: white;
  position: relative; overflow: hidden;
  padding: 0;
}
.title-page .tp-ornament {
  width: 1.5in; height: 2px;
  background: linear-gradient(90deg, transparent, #C9A84C, transparent);
  margin: 0.2in 0;
}
.title-page .tp-title {
  font-size: 36pt; font-weight: 700;
  letter-spacing: 2pt;
  margin-bottom: 0.12in;
  text-shadow: 0 2px 8px rgba(0,0,0,0.3);
}
.title-page .tp-subtitle {
  font-size: 12pt; font-style: italic;
  color: #D4B968;
  max-width: 3.8in; line-height: 1.5;
  margin-bottom: 0.15in;
}
.title-page .tp-pub {
  font-size: 9pt; color: #C9A84C;
  letter-spacing: 3pt; text-transform: uppercase;
  position: absolute; bottom: 0.6in;
}
/* Cross + light rays on title page */
.title-page .cross-wrap {
  position: relative;
  width: 60px; height: 100px;
  margin-bottom: 0.25in;
}
.title-page .cross-vert {
  position: absolute;
  left: 50%; top: 0;
  transform: translateX(-50%);
  width: 14px; height: 100px;
  background: #C9A84C;
  border-radius: 2px;
}
.title-page .cross-horiz {
  position: absolute;
  left: 50%; top: 28px;
  transform: translateX(-50%);
  width: 46px; height: 14px;
  background: #C9A84C;
  border-radius: 2px;
}
.title-page .cross-glow {
  position: absolute;
  left: 50%; top: 50%;
  transform: translate(-50%, -50%);
  width: 160px; height: 160px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(201,168,76,0.12), transparent 70%);
}

/* ================ BELONGS TO PAGE ================ */
.belongs-page {
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  text-align: center;
}
.belongs-page .bt-label {
  font-size: 18pt; color: #1B2A4A; font-weight: 700;
  margin-bottom: 0.5in;
}
.belongs-page .bt-line {
  width: 4in; height: 0;
  border-bottom: 1px solid #B8941C;
  margin: 0.18in 0;
}
.belongs-page .bt-hint {
  font-size: 8pt; color: #718096;
  text-transform: uppercase; letter-spacing: 1.5pt;
}

/* ================ HOW TO USE PAGE ================ */
.howto-page h2 {
  font-size: 14pt; color: #1B2A4A;
  text-align: center; margin-bottom: 0.25in;
  font-weight: 700;
}
.howto-page .ht-intro {
  font-size: 9.5pt; color: #4A5568; font-style: italic;
  text-align: center; margin-bottom: 0.25in;
  line-height: 1.6;
}
.howto-page .ht-step {
  display: flex; margin-bottom: 0.18in;
}
.howto-page .ht-num {
  flex-shrink: 0;
  width: 22px; height: 22px;
  background: #1B2A4A; color: white;
  border-radius: 50%;
  font-size: 9pt; font-weight: 700;
  display: flex; align-items: center; justify-content: center;
  margin-right: 0.12in;
}
.howto-page .ht-text {
  font-size: 9pt; line-height: 1.55; color: #2A2A2A;
  flex: 1;
}
.howto-page .ht-text strong { color: #1B2A4A; }

/* ================ ACTS MODEL PAGE ================ */
.acts-page h2 {
  font-size: 14pt; color: #1B2A4A;
  text-align: center; margin-bottom: 0.12in;
  font-weight: 700;
}
.acts-page .acts-sub {
  font-size: 9pt; color: #718096; font-style: italic;
  text-align: center; margin-bottom: 0.25in;
}
.acts-card {
  border-left: 3px solid #C9A84C;
  padding: 0.1in 0.18in;
  margin-bottom: 0.15in;
  background: #FAF8F3;
}
.acts-card .ac-letter {
  font-size: 14pt; font-weight: 700; color: #C9A84C;
  display: inline-block; width: 18px;
}
.acts-card .ac-word {
  font-size: 10pt; font-weight: 700; color: #1B2A4A;
  text-transform: uppercase; letter-spacing: 1pt;
}
.acts-card .ac-desc {
  font-size: 8.5pt; color: #4A5568; line-height: 1.5;
  margin-top: 0.03in;
}

/* ================ OVERVIEW PAGE ================ */
.overview-page h2 {
  font-size: 14pt; color: #1B2A4A;
  text-align: center; margin-bottom: 0.2in;
  font-weight: 700;
}
.overview-page .ov-text {
  font-size: 9.5pt; color: #2A2A2A; line-height: 1.7;
  text-align: justify; margin-bottom: 0.15in;
}
.overview-page .ov-quote {
  font-size: 11pt; color: #1B2A4A; font-style: italic;
  text-align: center; margin: 0.2in 0;
  line-height: 1.6;
}
.overview-page .ov-attr {
  font-size: 8pt; color: #C9A84C;
  text-align: center;
  text-transform: uppercase; letter-spacing: 2pt;
}

/* ================ SECTION DIVIDER ================ */
.divider {
  width: 6in; height: 9in;
  padding: 0;
  page-break-after: always;
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  text-align: center;
  background: linear-gradient(165deg, #0F1B33 0%, #1B2A4A 50%, #0F1B33 100%);
  position: relative; overflow: hidden;
}
.divider .div-num {
  font-size: 56pt; font-weight: 700;
  color: rgba(201,168,76,0.10);
  position: absolute; top: 0.8in;
  line-height: 1;
}
.divider .div-label {
  font-size: 9pt; color: #C9A84C;
  letter-spacing: 4pt; text-transform: uppercase;
  margin-bottom: 0.15in;
}
.divider .div-title {
  font-size: 24pt; color: white; font-weight: 700;
  max-width: 4.2in; line-height: 1.3;
  margin-bottom: 0.15in;
}
.divider .div-sub {
  font-size: 10pt; color: #D4B968; font-style: italic;
  max-width: 3.5in; line-height: 1.5;
}
.divider .div-orn {
  width: 1.2in; height: 1px;
  background: #C9A84C;
  margin: 0.2in 0;
}
.divider .div-deco {
  width: 50px; height: 50px;
  border: 2px solid #C9A84C;
  border-radius: 50%;
  margin: 0.15in 0;
  position: relative;
}
.divider .div-deco::before {
  content: ""; position: absolute;
  left: 50%; top: 50%; transform: translate(-50%, -50%);
  width: 6px; height: 30px; background: #C9A84C;
  border-radius: 1px;
}
.divider .div-deco::after {
  content: ""; position: absolute;
  left: 50%; top: 60%; transform: translate(-50%, 0);
  width: 20px; height: 6px; background: #C9A84C;
  border-radius: 1px;
}

/* ================ WEEKLY SPREAD PAGES ================ */
.week-page {
  position: relative;
}

/* Week header */
.week-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  border-bottom: 1.5px solid #C9A84C;
  padding-bottom: 0.06in;
  margin-bottom: 0.12in;
}
.week-header .wh-week {
  font-size: 11pt; font-weight: 700; color: #1B2A4A;
  letter-spacing: 1pt;
}
.week-header .wh-date {
  font-size: 8pt; color: #718096;
}

/* Scripture verse box */
.scripture-box {
  background: #FAF8F3;
  border-left: 3px solid #C9A84C;
  padding: 0.1in 0.15in;
  margin-bottom: 0.15in;
}
.scripture-box .sb-text {
  font-size: 8.5pt; font-style: italic; color: #2A2A2A;
  line-height: 1.55;
}
.scripture-box .sb-ref {
  font-size: 7.5pt; color: #C9A84C; font-weight: 700;
  text-align: right; margin-top: 0.04in;
  letter-spacing: 0.5pt;
}

/* Prayer section label */
.prayer-section {
  margin-bottom: 0.12in;
}
.prayer-section .ps-label {
  font-size: 8pt; font-weight: 700; color: #1B2A4A;
  text-transform: uppercase; letter-spacing: 1.5pt;
  margin-bottom: 0.04in;
}
.prayer-section .ps-hint {
  font-size: 6.5pt; color: #A0A0A0; font-style: italic;
  margin-bottom: 0.03in;
}

/* Writing lines */
.write-lines .wl {
  border-bottom: 1px solid #D0CCBE;
  height: 22px;
}

/* Compact writing lines (for smaller sections) */
.write-lines-compact .wl {
  border-bottom: 1px solid #D0CCBE;
  height: 19px;
}

/* Answered prayer mini-box */
.answered-mini {
  border: 1px solid #C9A84C;
  border-radius: 3px;
  padding: 0.06in 0.1in;
  margin-top: 0.08in;
  background: #FFFCF5;
}
.answered-mini .am-label {
  font-size: 7pt; font-weight: 700; color: #C9A84C;
  text-transform: uppercase; letter-spacing: 1pt;
  margin-bottom: 0.03in;
}
.answered-mini .am-line {
  border-bottom: 1px dashed #D0CCBE;
  height: 16px;
  margin-bottom: 0;
}

/* ================ ANSWERED PRAYERS LOG ================ */
.ap-page h2 {
  font-size: 13pt; color: #1B2A4A;
  text-align: center; margin-bottom: 0.04in;
  font-weight: 700;
}
.ap-page .ap-sub {
  font-size: 8pt; color: #718096; font-style: italic;
  text-align: center; margin-bottom: 0.18in;
}
.ap-table {
  width: 100%; border-collapse: collapse;
}
.ap-table th {
  font-size: 7pt; font-weight: 700; color: #1B2A4A;
  text-transform: uppercase; letter-spacing: 0.5pt;
  border-bottom: 2px solid #C9A84C;
  padding: 0.04in 0.03in;
  text-align: left;
}
.ap-table td {
  border-bottom: 1px solid #E5E0D0;
  padding: 0;
  height: 40px;
  vertical-align: top;
  font-size: 8pt;
  color: #2A2A2A;
}
.ap-table .col-date { width: 0.8in; }
.ap-table .col-req { width: auto; }
.ap-table .col-date2 { width: 0.8in; }
.ap-table .col-how { width: 1.4in; }

/* ================ GRATITUDE PAGE ================ */
.grat-page h2 {
  font-size: 13pt; color: #1B2A4A;
  text-align: center; margin-bottom: 0.04in;
  font-weight: 700;
}
.grat-page .gp-sub {
  font-size: 8pt; color: #718096; font-style: italic;
  text-align: center; margin-bottom: 0.15in;
}
.grat-prompt {
  font-size: 9pt; color: #1B2A4A; font-weight: 700;
  margin-bottom: 0.08in;
  border-bottom: 1px solid #C9A84C;
  padding-bottom: 0.04in;
}
.grat-prompt .gp-count {
  font-size: 7pt; color: #C9A84C; font-weight: 400;
}
.grat-lines .wl {
  border-bottom: 1px solid #D0CCBE;
  height: 24px;
  display: flex; align-items: center;
}
.grat-lines .wl .wl-num {
  font-size: 8pt; color: #C9A84C; font-weight: 700;
  width: 20px; flex-shrink: 0;
}

/* ================ NOTES PAGE ================ */
.notes-page h2 {
  font-size: 12pt; color: #1B2A4A;
  text-align: center; margin-bottom: 0.2in;
  font-weight: 700;
}
.notes-lines .wl {
  border-bottom: 1px solid #D0CCBE;
  height: 26px;
}

/* ================ FOOTER ================ */
.page-footer {
  position: absolute;
  bottom: 0.18in;
  left: 0; right: 0;
  text-align: center;
}
.page-footer .pf-text {
  font-size: 6.5pt; color: #C0C0C0;
  letter-spacing: 1pt;
}

/* ================ LAST PAGE ================ */
.last-page {
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  text-align: center;
}
.last-page .lp-text {
  font-size: 12pt; color: #1B2A4A; font-style: italic;
  line-height: 1.8; max-width: 4in;
  margin-bottom: 0.3in;
}
.last-page .lp-ref {
  font-size: 9pt; color: #C9A84C; font-weight: 700;
}
.last-page .lp-pub {
  font-size: 8pt; color: #718096;
  letter-spacing: 2pt; text-transform: uppercase;
  position: absolute; bottom: 0.5in;
}
"""

# ============================================================
# PAGE BUILDERS
# ============================================================

def page_title():
    """Title page"""
    return f'''<div class="page title-page">
  <div class="cross-glow"></div>
  <div class="cross-wrap">
    <div class="cross-vert"></div>
    <div class="cross-horiz"></div>
  </div>
  <div class="tp-title">{H.escape(BOOK_TITLE)}</div>
  <div class="tp-ornament"></div>
  <div class="tp-subtitle">{H.escape(BOOK_SUBTITLE)}</div>
  <div class="tp-ornament"></div>
  <div class="tp-pub">{H.escape(PUBLISHER)}</div>
</div>'''


def page_belongs():
    """This Journal Belongs To"""
    return f'''<div class="page belongs-page recto">
  <div class="bt-label">This Journal Belongs To</div>
  <div class="bt-line"></div>
  <div class="bt-hint">Name</div>
  <div style="height:0.3in;"></div>
  <div class="bt-line"></div>
  <div class="bt-hint">Date Started</div>
  <div style="height:0.3in;"></div>
  <div class="bt-line"></div>
  <div class="bt-hint">Date Completed</div>
  <div style="height:0.5in;"></div>
  <div style="font-size:8pt;color:#C9A84C;font-style:italic;max-width:3.5in;">
    "Commit your way to the LORD; trust in him, and he will act."
    &mdash; Psalm 37:5 (WEB)
  </div>
</div>'''


def page_howto():
    """How to Use This Journal"""
    return f'''<div class="page howto-page verso">
  <h2>How to Use This Journal</h2>
  <p class="ht-intro">This journal is designed to guide you through a year of intentional prayer.
  Each week offers a fresh Scripture passage and space to pray using the ACTS model.</p>

  <div class="ht-step">
    <div class="ht-num">1</div>
    <div class="ht-text"><strong>Find a quiet moment.</strong> Set aside a regular time each week — morning, evening, or whenever you can be still before God. Even five minutes is enough to begin.</div>
  </div>
  <div class="ht-step">
    <div class="ht-num">2</div>
    <div class="ht-text"><strong>Read the weekly Scripture.</strong> Let the verse settle in your heart before you start writing. Read it slowly, perhaps more than once.</div>
  </div>
  <div class="ht-step">
    <div class="ht-num">3</div>
    <div class="ht-text"><strong>Pray through the ACTS sections.</strong> Write your prayers using the four guided categories on the left page. There are no right answers — be honest with God.</div>
  </div>
  <div class="ht-step">
    <div class="ht-num">4</div>
    <div class="ht-text"><strong>Reflect on the right page.</strong> Use the space for personal prayers, people you are praying for, and what God is teaching you.</div>
  </div>
  <div class="ht-step">
    <div class="ht-num">5</div>
    <div class="ht-text"><strong>Record answered prayers.</strong> Use the special section in the back of this journal to track how God has responded. Looking back builds faith.</div>
  </div>
  <div class="ht-step">
    <div class="ht-num">6</div>
    <div class="ht-text"><strong>Don't worry about perfect weeks.</strong> If you miss a week, simply pick up where you left off. Prayer is a relationship, not a checklist.</div>
  </div>

  <div style="margin-top:0.2in;padding:0.08in;background:#FAF8F3;border-left:3px solid #C9A84C;">
    <div style="font-size:8.5pt;color:#1B2A4A;font-style:italic;line-height:1.5;text-align:center;">
      "The Lord is near to all who call on him, to all who call on him in truth."
      &mdash; Psalm 145:18 (WEB)
    </div>
  </div>
</div>'''


def page_acts():
    """The ACTS Prayer Model"""
    return f'''<div class="page acts-page recto">
  <h2>The ACTS Prayer Model</h2>
  <div class="acts-sub">A simple framework used by Christians for centuries</div>

  <div class="acts-card">
    <span class="ac-letter">A</span>
    <span class="ac-word">Adoration</span>
    <div class="ac-desc">Praise God for who He is. Reflect on His character — His love, holiness, power, mercy, and faithfulness. Tell Him what you admire about Him.</div>
  </div>

  <div class="acts-card">
    <span class="ac-letter">C</span>
    <span class="ac-word">Confession</span>
    <div class="ac-desc">Be honest about where you have fallen short. Ask for forgiveness, knowing that God is faithful and just to forgive. Release anything weighing on your conscience.</div>
  </div>

  <div class="acts-card">
    <span class="ac-letter">T</span>
    <span class="ac-word">Thanksgiving</span>
    <div class="ac-desc">Express gratitude for God's blessings — both big and small. Thank Him for His provision, protection, people in your life, and above all, for His grace.</div>
  </div>

  <div class="acts-card">
    <span class="ac-letter">S</span>
    <span class="ac-word">Supplication</span>
    <div class="ac-desc">Bring your requests to God. Pray for others first — family, friends, leaders, those in need. Then bring your own needs, trusting that He hears and cares.</div>
  </div>

  <div style="margin-top:0.15in;padding:0.1in 0.15in;background:#FAF8F3;border-radius:3px;">
    <div style="font-size:8pt;color:#4A5568;line-height:1.6;text-align:center;">
      ACTS is a guide, not a rule. You may spend more time in one area on some weeks
      and less in others. The goal is simply to draw near to God with an open heart.
    </div>
  </div>
</div>'''


def page_overview():
    """A Year of Prayer overview"""
    return f'''<div class="page overview-page verso">
  <h2>A Year of Prayer</h2>

  <p class="ov-text">Prayer is one of the greatest privileges of the Christian life — the invitation to speak with the Creator of the universe and to listen for His voice. Yet for many, prayer can feel difficult, distracted, or dry.</p>

  <p class="ov-text">This journal exists to help you build a consistent, meaningful prayer life over the course of fifty-two weeks. Each week, a Scripture passage will anchor your prayers. Guided sections will help you move beyond routine requests into deeper conversation with God.</p>

  <p class="ov-text">As you write, you will create a record of your spiritual journey — the struggles, the breakthroughs, and the quiet faithfulness of God. When you look back, you will see a story of grace that you may have missed in the moment.</p>

  <div class="ov-quote">
    "He will rejoice over you with gladness.<br/>
    He will calm you in his love.<br/>
    He will rejoice over you with singing."
  </div>
  <div class="ov-attr">Zephaniah 3:17 (WEB)</div>

  <div style="margin-top:0.3in;text-align:center;">
    <div style="font-size:8pt;color:#C9A84C;font-weight:700;letter-spacing:2pt;">
      FIFTY-TWO WEEKS &bull; ONE VERSE EACH WEEK &bull; A LIFETIME OF FAITH
    </div>
  </div>
</div>'''


def divider(title, subtitle, label, part_num):
    """Section divider page"""
    return f'''<div class="page divider">
  <div class="div-num">{part_num}</div>
  <div class="div-label">{H.escape(label)}</div>
  <div class="div-orn"></div>
  <div class="div-deco"></div>
  <div class="div-title">{H.escape(title)}</div>
  <div class="div-sub">{H.escape(subtitle)}</div>
  <div class="div-orn"></div>
</div>'''


def page_week_left(week_num, ref, verse):
    """Left page of weekly spread (recto/odd) — structured ACTS prayer"""
    lines_adore = '<div class="wl"></div>' * 4
    lines_confess = '<div class="wl"></div>' * 3
    lines_thanks = '<div class="wl"></div>' * 4
    lines_focus = '<div class="wl"></div>' * 3
    return f'''<div class="page week-page recto">
  <div class="week-header">
    <div class="wh-week">WEEK {week_num} of 52</div>
    <div class="wh-date">Week of: ____________________</div>
  </div>

  <div class="scripture-box">
    <div class="sb-text">{H.escape(verse)}</div>
    <div class="sb-ref">{H.escape(ref)} (WEB)</div>
  </div>

  <div class="prayer-section">
    <div class="ps-label">Adoration &mdash; Praising God</div>
    <div class="ps-hint">Who God is &mdash; His love, power, holiness, faithfulness</div>
    <div class="write-lines">
      {lines_adore}
    </div>
  </div>

  <div class="prayer-section">
    <div class="ps-label">Confession &mdash; Seeking Forgiveness</div>
    <div class="write-lines-compact">
      {lines_confess}
    </div>
  </div>

  <div class="prayer-section">
    <div class="ps-label">Thanksgiving &mdash; Counting Blessings</div>
    <div class="ps-hint">Specific things God has done this week</div>
    <div class="write-lines">
      {lines_thanks}
    </div>
  </div>

  <div class="prayer-section">
    <div class="ps-label">Prayer Focus This Week</div>
    <div class="write-lines-compact">
      {lines_focus}
    </div>
  </div>
</div>'''


def page_week_right(week_num):
    """Right page of weekly spread (verso/even) — supplication, personal, reflection"""
    lines_others = '<div class="wl"></div>' * 5
    lines_personal = '<div class="wl"></div>' * 4
    lines_learning = '<div class="wl"></div>' * 4
    return f'''<div class="page week-page verso">
  <div class="week-header">
    <div class="wh-week">WEEK {week_num} &mdash; Continued</div>
    <div class="wh-date">Page 2</div>
  </div>

  <div class="prayer-section">
    <div class="ps-label">Supplication &mdash; Praying for Others</div>
    <div class="ps-hint">Family, friends, church, leaders, those in need</div>
    <div class="write-lines">
      {lines_others}
    </div>
  </div>

  <div class="prayer-section">
    <div class="ps-label">Personal Prayers</div>
    <div class="ps-hint">Your own needs, hopes, and requests</div>
    <div class="write-lines">
      {lines_personal}
    </div>
  </div>

  <div class="prayer-section">
    <div class="ps-label">What God Is Teaching Me</div>
    <div class="ps-hint">Reflections, impressions, Scripture insights</div>
    <div class="write-lines-compact">
      {lines_learning}
    </div>
  </div>

  <div class="answered-mini">
    <div class="am-label">&#10022; Answered Prayers This Week</div>
    <div class="am-line"></div>
    <div class="am-line"></div>
  </div>
</div>'''


def page_answered_prayers(page_label):
    """Answered Prayers log page"""
    rows = ""
    for i in range(1, 9):
        rows += f'''<tr>
          <td class="col-date"></td>
          <td class="col-req"></td>
          <td class="col-date2"></td>
          <td class="col-how"></td>
        </tr>'''
    return f'''<div class="page ap-page recto">
  <h2>Answered Prayers</h2>
  <div class="ap-sub">{H.escape(page_label)}</div>
  <table class="ap-table">
    <tr>
      <th class="col-date">Date Asked</th>
      <th class="col-req">Prayer Request</th>
      <th class="col-date2">Date Answered</th>
      <th class="col-how">How God Answered</th>
    </tr>
    {rows}
  </table>
  <div class="page-footer">
    <div class="pf-text">More Shine Press</div>
  </div>
</div>'''


def page_gratitude(page_label, start_num, prompts):
    """Gratitude page with themed prompts"""
    sections = ""
    for prompt, count_hint in prompts:
        lines = ""
        for j in range(1, 6):
            lines += f'<div class="wl"><span class="wl-num">{j}.</span></div>'
        sections += f'''<div class="grat-prompt">{H.escape(prompt)} <span class="gp-count">{H.escape(count_hint)}</span></div>
        <div class="grat-lines">{lines}</div>'''
    return f'''<div class="page grat-page verso">
  <h2>Gratitude & Thanksgiving</h2>
  <div class="gp-sub">{H.escape(page_label)}</div>
  {sections}
  <div class="page-footer">
    <div class="pf-text">More Shine Press</div>
  </div>
</div>'''


def page_notes():
    """Blank notes page"""
    lines = '<div class="wl"></div>' * 22
    return f'''<div class="page notes-page recto">
  <h2>Notes & Reflections</h2>
  <div class="notes-lines">
    {lines}
  </div>
</div>'''


def page_last():
    """Closing page"""
    return f'''<div class="page last-page verso">
  <div class="lp-text">
    "Now to him who is able to do far more abundantly<br/>
    than all that we ask or think,<br/>
    according to the power that works in us,<br/>
    to him be the glory in the assembly and in Christ Jesus<br/>
    to all generations forever and ever."
  </div>
  <div class="lp-ref">Ephesians 3:20-21 (WEB)</div>
  <div class="lp-pub">{H.escape(PUBLISHER)}</div>
</div>'''


# ============================================================
# MAIN
# ============================================================
def main():
    pages = []

    # ---- FRONT MATTER ----
    pages.append(page_title())                    # 1: title
    pages.append(page_belongs())                  # 2: belongs to
    pages.append(page_howto())                    # 3: how to use
    pages.append(page_acts())                     # 4: ACTS model
    pages.append(page_overview())                 # 5: a year of prayer

    # ---- DIVIDER: Weekly Prayers ----
    pages.append(divider(
        "Fifty-Two Weeks of Prayer",
        "One verse, one week, one step closer to God",
        "Part One", "01"
    ))                                           # 6: divider

    # ---- 52 WEEKLY SPREADS (104 pages) ----
    for i in range(52):
        ref, verse = SCRIPTURES[i]
        pages.append(page_week_left(i + 1, ref, verse))   # recto (odd)
        pages.append(page_week_right(i + 1))               # verso (even)

    # ---- DIVIDER: Answered Prayers ----
    pages.append(divider(
        "Answered Prayers",
        "A record of God's faithfulness",
        "Part Two", "02"
    ))                                           # 111: divider

    # ---- ANSWERED PRAYERS LOG (4 pages) ----
    for label in ["Page 1 of 4", "Page 2 of 4", "Page 3 of 4", "Page 4 of 4"]:
        pages.append(page_answered_prayers(label))

    # ---- DIVIDER: Gratitude ----
    pages.append(divider(
        "Gratitude & Thanksgiving",
        "Count your blessings, name them one by one",
        "Part Three", "03"
    ))                                           # 116: divider

    # ---- GRATITUDE PAGES (4 pages) ----
    gratitude_prompts_sets = [
        [("People I am grateful for", "(family, friends, mentors)"),
         ("God's provision in my life", "(food, shelter, work)")],
        [("Moments that brought me joy", "(big and small)"),
         ("Answered prayers I have seen", "(recent and past)")],
        [("Ways God has grown me", "(patience, faith, love)"),
         ("Scriptures that spoke to me", "(verses, passages)")],
        [("Beauty in everyday life", "(nature, kindness, grace)"),
         ("My hopes and dreams for the future", "(trusting God's plan)")],
    ]
    for i, prompts in enumerate(gratitude_prompts_sets):
        pages.append(page_gratitude(f"Page {i+1} of 4", 1, prompts))

    # ---- DIVIDER: Notes ----
    pages.append(divider(
        "Notes & Reflections",
        "Space for your thoughts, prayers, and reflections",
        "Part Four", "04"
    ))                                           # 121: divider

    # ---- NOTES PAGES (6 pages) ----
    for _ in range(6):
        pages.append(page_notes())

    # ---- CLOSING PAGE ----
    pages.append(page_last())

    # ---- ASSEMBLE HTML ----
    body_content = "\n".join(pages)
    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{H.escape(BOOK_TITLE)} — {H.escape(BOOK_SUBTITLE)}</title>
<style>{CSS}</style>
</head>
<body>
{body_content}
</body>
</html>'''

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)

    total_pages = len(pages)
    print(f"Generated: {HTML_FILE}")
    print(f"Total pages: {total_pages}")
    return total_pages


if __name__ == "__main__":
    main()
