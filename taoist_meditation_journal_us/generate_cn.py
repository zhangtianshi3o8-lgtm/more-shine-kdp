#!/usr/bin/env python3
"""
道教冥想日记（中文对照版）-- KDP Interior Generator
Trim: 6 x 9 in | Language: Chinese
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "taoist_meditation_journal_cn_V1.0.html")

BOOK_TITLE = "道教冥想日记"
BOOK_SUBTITLE = "致虚极 守静笃"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

from tao_quotes import TAO_QUOTES  # Shared 30-quote list (chapter, english, chinese)

CSS = r"""
@page { size: 6in 9in; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: "Songti SC", "STSong", "SimSun", "PingFang SC", Georgia, serif;
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
  background: linear-gradient(165deg, #161616 0%, #232323 30%, #161616 65%, #0E0E0E 100%);
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #C4A04A, transparent);
}

.cover .taiji { position: relative; z-index: 2; margin-bottom: 20px; }

.cover .title-main {
  font-size: 32pt;
  font-weight: 700;
  color: #FAF6F0;
  line-height: 1.3;
  letter-spacing: 4pt;
  position: relative;
  z-index: 2;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 100px; height: 2px;
  background: #C4A04A;
  margin: 20px auto;
  position: relative;
  z-index: 2;
}

.cover .subtitle {
  font-size: 13pt;
  color: #D4B896;
  line-height: 1.5;
  letter-spacing: 3pt;
  position: relative;
  z-index: 2;
}

.cover .pub {
  font-size: 8.5pt;
  color: #888;
  letter-spacing: 2pt;
  text-transform: uppercase;
  margin-top: 50px;
  position: relative;
  z-index: 2;
}

/* ================ PAGE HEADER ================ */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  border-bottom: 1.5px solid #C4A04A;
  padding-bottom: 5px;
  margin-bottom: 12px;
}

.ph-left { font-size: 10pt; font-weight: 700; color: #333; letter-spacing: 1pt; }
.ph-right { font-size: 7.5pt; color: #999; }

/* ================ HOW TO USE ================ */
.howto-text { font-size: 9pt; line-height: 1.8; color: #444; }
.howto-text .ht-title { font-size: 13pt; font-weight: 700; color: #333; margin-bottom: 8px; }
.howto-text p { margin-bottom: 8px; }
.howto-text .ht-section { margin-bottom: 12px; }
.howto-text .ht-heading { font-size: 10pt; font-weight: 700; color: #C4A04A; margin-bottom: 4px; }

/* ================ QUOTE BOX ================ */
.quote-box {
  border: 1px solid #C4A04A;
  border-radius: 4px;
  padding: 10px 14px;
  margin-bottom: 10px;
  background: #FFFCF5;
  text-align: center;
}

.quote-box .qb-text { font-size: 9.5pt; color: #555; line-height: 1.6; letter-spacing: 1pt; }

.quote-box .qb-source {
  font-size: 7pt; color: #999; margin-top: 4px;
  text-transform: uppercase; letter-spacing: 0.5pt;
}

/* ================ SESSION BANNER ================ */
.session-banner { display: flex; align-items: center; gap: 8px; margin-bottom: 10px; }

.session-banner .sb-num { font-size: 13pt; font-weight: 700; color: #C4A04A; }

.session-banner .sb-label { font-size: 8pt; color: #999; letter-spacing: 0.5pt; }

.session-banner .sb-line { flex: 1; height: 12px; border-bottom: 1px dotted #ccc; }

/* ================ INFO ROW ================ */
.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 6px 10px;
  margin-bottom: 10px;
}

.info-field .if-label {
  font-size: 7pt; color: #C4A04A;
  letter-spacing: 0.5pt; font-weight: 700;
  display: block; margin-bottom: 1px;
}

.info-field .if-write { height: 18px; border-bottom: 1px dotted #ccc; }

/* ================ TYPE CHECKBOXES ================ */
.type-row { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 8px; }

.type-check { display: inline-flex; align-items: center; gap: 3px; font-size: 8pt; color: #555; }

.type-box { width: 10px; height: 10px; border: 1.5px solid #C4A04A; border-radius: 2px; }

/* ================ WRITE BOX ================ */
.write-box { border: 1px solid #C4A04A; border-radius: 3px; padding: 6px 8px; margin-bottom: 8px; }

.write-box .wb-label {
  font-size: 7.5pt; color: #C4A04A;
  letter-spacing: 0.5pt; font-weight: 700;
  margin-bottom: 3px;
}

.write-box .wb-area { height: 28px; }

/* ================ METRIC ROWS ================ */
.metric-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px 10px; margin-bottom: 8px; }

.metric-field .mf-label {
  font-size: 7pt; color: #C4A04A;
  letter-spacing: 0.5pt; font-weight: 700;
  display: block; margin-bottom: 1px;
}

.metric-field .mf-write { height: 18px; border-bottom: 1px dotted #ccc; }

/* ================ SCORE DOTS ================ */
.score-dots { display: flex; gap: 4px; margin-top: 2px; }

.score-dot { width: 12px; height: 12px; border: 1.5px solid #C4A04A; border-radius: 50%; }

/* ================ NOTES ================ */
.notes-line { border-bottom: 1px solid #ddd; height: 22px; }

/* ================ FINAL PAGE ================ */
.final-page {
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  text-align: center; height: 100%;
}

.final-page .fp-text { font-size: 14pt; color: #999; line-height: 1.8; margin-bottom: 20px; letter-spacing: 2pt; }

.final-page .fp-logo {
  font-size: 11pt; color: #C4A04A;
  letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700;
}

.final-page .fp-line { width: 60px; height: 1.5px; background: #C4A04A; margin: 12px auto; opacity: 0.5; }

/* ================ WEEKLY REFLECTION ================ */
.weekly-banner {
  font-size: 11pt; font-weight: 700; color: #C4A04A;
  border-bottom: 1px solid #ddd; padding-bottom: 4px; margin-bottom: 10px;
}

/* ================ MEDITATION TYPES ================ */
.med-type { margin-bottom: 8px; }
.med-type .mt-name { font-size: 9pt; font-weight: 700; color: #333; }
.med-type .mt-desc { font-size: 8pt; color: #777; line-height: 1.6; }
"""


# ============================================================
# PAGE GENERATORS
# ============================================================

def taiji_svg(size=90):
    return f'''<svg viewBox="0 0 100 100" width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">
  <defs><clipPath id="tjclip_cn"><circle cx="50" cy="50" r="48"/></clipPath></defs>
  <g clip-path="url(#tjclip_cn)">
    <circle cx="50" cy="50" r="48" fill="none" stroke="#C4A04A" stroke-width="1.5"/>
    <path d="M50,2 A24,24 0 0,1 50,50 A24,24 0 0,0 50,98 A48,48 0 0,1 50,2 Z" fill="#C4A04A" opacity="0.12"/>
    <path d="M50,2 A48,48 0 0,1 50,98 A24,24 0 0,1 50,50 A24,24 0 0,0 50,2 Z" fill="none" stroke="#C4A04A" stroke-width="1.2"/>
    <circle cx="50" cy="26" r="6.5" fill="none" stroke="#C4A04A" stroke-width="1"/>
    <circle cx="50" cy="74" r="6.5" fill="none" stroke="#C4A04A" stroke-width="1"/>
    <circle cx="50" cy="26" r="2" fill="#C4A04A" opacity="0.4"/>
    <circle cx="50" cy="74" r="2" fill="#C4A04A"/>
  </g>
</svg>'''


def interior_title_page():
    return f'''
<!-- PAGE 1: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>
  <div class="taiji">{taiji_svg(95)}</div>
  <div class="title-main">道教<br>冥想日记</div>
  <div class="accent-bar"></div>
  <div class="subtitle">致虚极 守静笃</div>
  <div class="pub">More Shine Press</div>
</div>'''


def how_to_use_page():
    return f'''
<!-- PAGE 2: How to Use -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">使用指南</span>
    <span class="ph-right">第 {pn()} 页</span>
  </div>

  <div class="howto-text">
    <div class="ht-title">修道之门</div>

    <p>两千余年来，道教冥想为无数修行者提供了一条通往内在宁静、天人合一、自我觉知的道路。这本日记是你修行路上的同伴——记录、反思、成长。</p>

    <div class="ht-section">
      <div class="ht-heading">两页式练习记录</div>
      <p>每次练习使用一组两页的记录版面。左页记录基本信息：日期、练习类型、时长、姿势、环境。右页记录你的内在体验：呼吸观察、身体感受、情绪起伏、灵感洞见，以及一则道德经智慧供你参悟。</p>
    </div>

    <div class="ht-section">
      <div class="ht-heading">练习类型</div>
      <p>本日记支持六种道教核心冥想修法：坐忘、内观、坐禅、吐纳、内笑、动功。后续参考页对每种修法有详细说明。</p>
    </div>

    <div class="ht-section">
      <div class="ht-heading">五次一回顾</div>
      <p>每完成五次练习后设有一页回顾，帮助你审视进展、发现规律、深化修行。善用这些时刻来肯定进步、调整方向。</p>
    </div>

    <p style="margin-top: 14px; font-style: italic; color: #888; text-align: center; border-top: 1px solid #eee; padding-top: 8px;">
    道可道，非常道。<br>名可名，非常名。</p>
  </div>
</div>'''


def meditation_types_ref():
    types = [
        ("坐忘", "道教冥想的标志性修法。「堕肢体，黜聪明，离形去知，同于大通。」端坐舒适，双目微闭，放下一切概念、身份与杂念。不必抗拒——只需如观云般任其来去。安住于开放的觉知之中。"),
        ("内观（观）", "向内看的修行。将注意力轻柔地转向内，观察身体、呼吸与心念，不加评判。觉察当下的一切。培养如镜的品质：映照而不执取。"),
        ("坐禅", "基础静坐修法。脊柱正直，肩背放松，双目半闭，双手置于膝上。专注于呼吸的自然节律。心若游离，轻轻带回。"),
        ("吐纳", "吐故纳新的古老功法。自腹部缓慢深长地呼吸。每次呼气释放紧张，每次吸气采集清气。呼吸应柔和、绵长、深沉。"),
        ("内笑", "培养内在温润与慈悲的修法。向身体每个部位微笑——从面部开始，依次向下至五脏六腑。此法化解郁结，聚养精气。"),
        ("动功", "太极、气功与经行（步行冥想）。当以全然觉知、柔和呼吸、安定心神去做时，行动便成为冥想。练习缓慢、圆融的动作，顺应气之自然流转。"),
    ]

    html = '<!-- PAGE 3: Meditation Types Reference -->\n'
    html += f'''<div class="page">
  <div class="page-header">
    <span class="ph-left">道教冥想修法</span>
    <span class="ph-right">第 {pn()} 页</span>
  </div>'''
    for name, desc in types[:3]:
        html += f'''
  <div class="med-type">
    <div class="mt-name">{name}</div>
    <div class="mt-desc">{desc}</div>
  </div>'''
    html += '\n</div>'

    html += '\n<!-- PAGE 4: Meditation Types Reference (cont.) -->\n'
    html += f'''<div class="page">
  <div class="page-header">
    <span class="ph-left">道教冥想修法（续）</span>
    <span class="ph-right">第 {pn()} 页</span>
  </div>'''
    for name, desc in types[3:]:
        html += f'''
  <div class="med-type">
    <div class="mt-name">{name}</div>
    <div class="mt-desc">{desc}</div>
  </div>'''

    html += f'''
  <div class="quote-box" style="margin-top: 10px;">
    <div class="qb-text">致虚极，守静笃。<br>万物并作，吾以观复。</div>
    <div class="qb-source">道德经 第十六章</div>
  </div>
</div>'''
    return html


def intention_page():
    return f'''
<!-- PAGE 5: Intention Setting -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">立愿发心</span>
    <span class="ph-right">第 {pn()} 页</span>
  </div>

  <div class="howto-text" style="margin-bottom: 12px;">
    <div class="ht-heading" style="color: #333; font-size: 10pt;">先定其心，后行其道</div>
    <p style="font-size: 8.5pt; color: #777;">动笔之前，先静下来问问自己：是什么吸引你走上这条路？你希望修习什么？此刻，「道」对你意味着什么？</p>
  </div>

  <div class="write-box" style="height: auto;">
    <div class="wb-label">我的修行本愿</div>
    <div class="wb-area" style="height: 50px;"></div>
  </div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">每周练习次数</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">目标时长</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">偏好时段</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box">
    <div class="wb-label">我希望修习的方向</div>
    <div class="type-row">
      <span class="type-check"><span class="type-box"></span>静定</span>
      <span class="type-check"><span class="type-box"></span>觉知</span>
      <span class="type-check"><span class="type-box"></span>放下</span>
      <span class="type-check"><span class="type-box"></span>行气</span>
      <span class="type-check"><span class="type-box"></span>情绪调和</span>
      <span class="type-check"><span class="type-box"></span>自知</span>
      <span class="type-check"><span class="type-box"></span>简朴</span>
      <span class="type-check"><span class="type-box"></span>慈悲</span>
      <span class="type-check"><span class="type-box"></span>天人合一</span>
      <span class="type-check"><span class="type-box"></span>内外和谐</span>
    </div>
  </div>

  <div class="write-box" style="height: auto;">
    <div class="wb-label">我希望放下什么</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box" style="height: auto; border-color: #C4A04A;">
    <div class="wb-label">引路箴言</div>
    <div class="quote-box" style="border: none; padding: 6px 0; margin: 0; background: none; text-align: left;">
      <div class="qb-text" style="font-size: 10pt;">千里之行，始于足下。</div>
      <div class="qb-source" style="text-align: left;">道德经 第六十四章</div>
    </div>
  </div>
</div>'''


def practice_log_left(session_num):
    return f'''
<!-- Practice Log Left -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">练习记录</span>
    <span class="ph-right">第 {pn()} 页</span>
  </div>

  <div class="session-banner">
    <span class="sb-num">第 {session_num:03d} 次</span>
    <span class="sb-label">日期：</span>
    <div class="sb-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">日期</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">星期</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">时长（分钟）</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">时段</span><div class="if-write"></div></div>
  </div>

  <div style="font-size: 7.5pt; font-weight: 700; color: #C4A04A; letter-spacing: 0.5pt; margin-bottom: 3px;">练习类型</div>
  <div class="type-row">
    <span class="type-check"><span class="type-box"></span>坐忘</span>
    <span class="type-check"><span class="type-box"></span>内观</span>
    <span class="type-check"><span class="type-box"></span>坐禅</span>
    <span class="type-check"><span class="type-box"></span>吐纳</span>
    <span class="type-check"><span class="type-box"></span>内笑</span>
    <span class="type-check"><span class="type-box"></span>动功</span>
    <span class="type-check"><span class="type-box"></span>其他</span>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px 12px; margin-bottom: 8px;">
    <div>
      <div style="font-size: 7.5pt; font-weight: 700; color: #C4A04A; letter-spacing: 0.5pt; margin-bottom: 3px;">姿势</div>
      <div class="type-row" style="margin-bottom: 0;">
        <span class="type-check"><span class="type-box"></span>坐</span>
        <span class="type-check"><span class="type-box"></span>站</span>
        <span class="type-check"><span class="type-box"></span>卧</span>
        <span class="type-check"><span class="type-box"></span>行</span>
      </div>
    </div>
    <div>
      <div style="font-size: 7.5pt; font-weight: 700; color: #C4A04A; letter-spacing: 0.5pt; margin-bottom: 3px;">环境</div>
      <div class="type-row" style="margin-bottom: 0;">
        <span class="type-check"><span class="type-box"></span>室内</span>
        <span class="type-check"><span class="type-box"></span>户外</span>
        <span class="type-check"><span class="type-box"></span>静室</span>
      </div>
    </div>
  </div>

  <div class="write-box" style="border-color: #C4A04A;">
    <div class="wb-label">练习前的身心状态</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">环境布置（烛火、线香、音乐、方位）</div>
    <div class="wb-area" style="height: 32px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">呼吸观察（节奏、深浅、品质）</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>
</div>'''


def practice_reflection_right(session_num, quote_text, quote_ch):
    src = f"道德经 第{quote_ch}章" if isinstance(quote_ch, int) else "道家箴言"
    return f'''
<!-- Practice Reflection Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">练习心得</span>
    <span class="ph-right">第 {pn()} 页</span>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px 12px; margin-top: 4px; margin-bottom: 8px;">
    <div>
      <div style="font-size: 7.5pt; font-weight: 700; color: #C4A04A; letter-spacing: 0.5pt; margin-bottom: 4px;">静定程度（1-5）</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 6pt; color: #999; margin-top: 2px;">1 = 烦躁&#160;&#160;&#160;5 = 深度静定</div>
    </div>
    <div>
      <div style="font-size: 7.5pt; font-weight: 700; color: #C4A04A; letter-spacing: 0.5pt; margin-bottom: 4px;">精气充沛（1-5）</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 6pt; color: #999; margin-top: 2px;">1 = 倦怠&#160;&#160;&#160;5 = 气足神旺</div>
    </div>
    <div>
      <div style="font-size: 7.5pt; font-weight: 700; color: #C4A04A; letter-spacing: 0.5pt; margin-bottom: 4px;">心念清明（1-5）</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 6pt; color: #999; margin-top: 2px;">1 = 浑浊&#160;&#160;&#160;5 = 湛然澄明</div>
    </div>
    <div>
      <div style="font-size: 7.5pt; font-weight: 700; color: #C4A04A; letter-spacing: 0.5pt; margin-bottom: 4px;">身体松弛（1-5）</div>
      <div class="score-dots">
        <div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div><div class="score-dot"></div>
      </div>
      <div style="font-size: 6pt; color: #999; margin-top: 2px;">1 = 紧绷&#160;&#160;&#160;5 = 浑然松弛</div>
    </div>
  </div>

  <div class="write-box">
    <div class="wb-label">身体感受与气机观察</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">浮现的情绪</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">灵感与直觉洞见</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #C4A04A;">
    <div class="wb-label">练习后的身心状态</div>
    <div class="wb-area"></div>
  </div>

  <div class="quote-box">
    <div class="qb-text">{quote_text}</div>
    <div class="qb-source">{src}</div>
  </div>
</div>'''


def weekly_reflection(week_num):
    return f'''
<!-- Weekly Reflection -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">每周回顾</span>
    <span class="ph-right">第 {pn()} 页</span>
  </div>

  <div class="weekly-banner">第 {week_num} 周 —— 回顾与展望</div>

  <div class="metric-row">
    <div class="metric-field"><span class="mf-label">已完成次数</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">累计时长</span><div class="mf-write"></div></div>
    <div class="metric-field"><span class="mf-label">平均静定度</span><div class="mf-write"></div></div>
  </div>

  <div class="write-box" style="height: auto;">
    <div class="wb-label">本周做得好的地方</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="height: auto;">
    <div class="wb-label">遇到的困难与阻力</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="height: auto;">
    <div class="wb-label">最重要的时刻或洞见</div>
    <div class="wb-area" style="height: 40px;"></div>
  </div>

  <div class="write-box" style="height: auto;">
    <div class="wb-label">下周想要修习的方向</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="quote-box">
    <div class="qb-text">孰能浊以静之徐清？孰能安以动之徐生？</div>
    <div class="qb-source">道德经 第十五章</div>
  </div>
</div>'''


def tao_wisdom_ref_pages():
    passages = [
        (1, "道可道，非常道。名可名，非常名。无名，天地之始；有名，万物之母。"),
        (8, "上善若水。水善利万物而不争，处众人之所恶，故几于道。"),
        (11, "三十辐共一毂，当其无，有车之用。埏埴以为器，当其无，有器之用。凿户牖以为室，当其无，有室之用。故有之以为利，无之以为用。"),
        (16, "致虚极，守静笃。万物并作，吾以观复。"),
        (22, "曲则全，枉则直，洼则盈，敝则新，少则得，多则惑。"),
        (33, "知人者智，自知者明。胜人者有力，自胜者强。"),
        (40, "反者道之动，弱者道之用。天下万物生于有，有生于无。"),
        (47, "不出户，知天下。不窥牖，见天道。"),
        (63, "为无为，事无事，味无味。图难于其易，为大于其细。"),
        (76, "人之生也柔弱，其死也坚强。草木之生也柔脆，其死也枯槁。故坚强者死之徒，柔弱者生之徒。"),
    ]

    html = '<!-- Tao Wisdom Reference Page 1 -->\n'
    html += f'''<div class="page">
  <div class="page-header">
    <span class="ph-left">道德经智慧选读</span>
    <span class="ph-right">第 {pn()} 页</span>
  </div>'''
    for ch, text in passages[:5]:
        html += f'''
  <div class="quote-box" style="text-align: left; margin-bottom: 8px;">
    <div class="qb-text" style="text-align: left;">{text}</div>
    <div class="qb-source" style="text-align: left;">道德经 第{ch}章</div>
  </div>'''
    html += '\n</div>'

    html += '\n<!-- Tao Wisdom Reference Page 2 -->\n'
    html += f'''<div class="page">
  <div class="page-header">
    <span class="ph-left">道德经智慧选读（续）</span>
    <span class="ph-right">第 {pn()} 页</span>
  </div>'''
    for ch, text in passages[5:]:
        html += f'''
  <div class="quote-box" style="text-align: left; margin-bottom: 8px;">
    <div class="qb-text" style="text-align: left;">{text}</div>
    <div class="qb-source" style="text-align: left;">道德经 第{ch}章</div>
  </div>'''
    html += '\n</div>'
    return html


def final_page():
    return f'''
<!-- FINAL PAGE -->
<div class="page">
  <div class="final-page">
    <div class="fp-text">道常无为<br>而无不为</div>
    <div class="fp-line"></div>
    <div class="fp-logo">More Shine Press</div>
  </div>
</div>'''


# ============================================================
# BUILD THE BOOK
# ============================================================

def build():
    pages = []
    pages.append('<!DOCTYPE html>')
    pages.append('<html lang="zh"><head>')
    pages.append('<meta charset="UTF-8">')
    pages.append(f'<title>{BOOK_TITLE}</title>')
    pages.append(f'<style>{CSS}</style>')
    pages.append('</head><body>')

    pages.append(interior_title_page())
    pages.append(how_to_use_page())
    pages.append(meditation_types_ref())
    pages.append(intention_page())

    session = 0
    week = 0
    quote_idx = 0
    for i in range(30):
        session += 1
        q_ch, q_text = TAO_QUOTES[quote_idx % len(TAO_QUOTES)][0], TAO_QUOTES[quote_idx % len(TAO_QUOTES)][2]
        quote_idx += 1
        pages.append(practice_log_left(session))
        pages.append(practice_reflection_right(session, q_text, q_ch))
        if session % 5 == 0 and session < 30:
            week += 1
            pages.append(weekly_reflection(week))

    pages.append(tao_wisdom_ref_pages())
    pages.append(final_page())

    pages.append('</body></html>')

    html_content = "\n".join(pages)
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)

    total_pages = page_no[0] + 2  # +1 interior title (no pn), +1 final page (no pn)
    print(f"Generated: {HTML_FILE}")
    print(f"Total pages: {total_pages}")


if __name__ == "__main__":
    build()
