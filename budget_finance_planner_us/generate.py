#!/usr/bin/env python3
"""
Budget & Finance Planner — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Individuals, couples, and families who want to take control of their finances
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "budget_finance_planner_us_V1.0.html")

BOOK_TITLE = "Budget & Finance Planner"
BOOK_SUBTITLE = "Take Control of Your Money, One Month at a Time"

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

/* ---- Colors ---- */
/* Charcoal: #161616, #1E1E1E */
/* Gold: #C4A04A */
/* Warm cream: #FAF6F0, #F5EDE3 */
/* Text: #2A2A2A */

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

/* Coin / dollar symbol stylized */
.cover .icon-wrap {
  width: 120px; height: 120px;
  position: relative;
  margin: 0 auto 16px;
}

.cover .icon-circle {
  width: 100px; height: 100px;
  border: 2px solid rgba(196,160,74,0.5);
  border-radius: 50%;
  position: absolute;
  top: 10px; left: 10px;
  background: transparent;
}

.cover .icon-circle-inner {
  width: 80px; height: 80px;
  border: 1px solid rgba(196,160,74,0.3);
  border-radius: 50%;
  position: absolute;
  top: 20px; left: 20px;
}

.cover .icon-dollar {
  position: absolute;
  top: 30px; left: 0; right: 0;
  text-align: center;
  font-size: 42pt;
  font-weight: 700;
  color: rgba(196,160,74,0.6);
  font-family: Georgia, serif;
}

.cover .icon-arc {
  position: absolute;
  top: -5px; left: -5px;
  width: 130px; height: 130px;
  border: 1.5px dashed rgba(196,160,74,0.2);
  border-radius: 50%;
}

.cover .title-block {
  position: relative;
  z-index: 5;
  padding: 0 0.4in;
}

.cover .main-title {
  font-family: Georgia, serif;
  font-size: 30pt;
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
.section-header .sh-right {
  color: #aaa;
}

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

/* ---- Writing Lines ---- */
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

/* ---- Data Tables ---- */
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
table.data-table tr:nth-child(even) td {
  background: #FAF6F0;
}

/* ---- Money table (income/expense) ---- */
table.money-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
}
table.money-table th {
  background: #161616;
  color: #C4A04A;
  font-weight: 700;
  text-align: left;
  padding: 5px 6px;
  font-size: 7pt;
  letter-spacing: 0.3pt;
  text-transform: uppercase;
}
table.money-table th.amt {
  text-align: right;
}
table.money-table td {
  padding: 4px 6px;
  border-bottom: 0.5px solid #ddd;
  vertical-align: top;
}
table.money-table td.amt {
  text-align: right;
  font-family: 'Courier New', monospace;
  font-size: 8.5pt;
}
table.money-table tr:nth-child(even) td {
  background: #FAF6F0;
}
table.money-table .total-row td {
  background: #F0E6D0;
  font-weight: 700;
  border-top: 1.5px solid #C4A04A;
  border-bottom: 1.5px solid #C4A04A;
}
table.money-table .total-row td.amt {
  font-size: 9.5pt;
  color: #161616;
}

/* ---- Field Grid ---- */
.field-row {
  display: flex;
  gap: 8px;
  align-items: baseline;
}
.field-label {
  font-size: 7.5pt;
  font-weight: 700;
  color: #161616;
  text-transform: uppercase;
  letter-spacing: 0.4pt;
  white-space: nowrap;
  min-width: 60px;
}
.field-line {
  flex: 1;
  border-bottom: 0.5px solid #bbb;
  height: 16px;
}

/* ---- Checkbox Row ---- */
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

/* ---- Info Box ---- */
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

/* ---- Summary Card ---- */
.summary-card {
  background: #FAF6F0;
  border: 1px solid #E8DCC8;
  border-radius: 4px;
  padding: 8px 10px;
  margin-bottom: 6px;
}
.summary-card .sc-label {
  font-size: 7pt;
  font-weight: 700;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
}
.summary-card .sc-value {
  font-size: 11pt;
  font-weight: 700;
  color: #161616;
  font-family: 'Courier New', monospace;
}

/* ---- Progress Bar ---- */
.progress-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
}
.progress-label {
  font-size: 7pt;
  font-weight: 700;
  color: #161616;
  text-transform: uppercase;
  letter-spacing: 0.3pt;
  min-width: 80px;
}
.progress-track {
  flex: 1;
  height: 12px;
  background: #F0E6D0;
  border-radius: 2px;
  border: 0.5px solid #D4B896;
  position: relative;
}
.progress-fill-prompt {
  font-size: 6.5pt;
  color: #aaa;
  font-style: italic;
}
.progress-amt {
  font-size: 7pt;
  font-weight: 700;
  color: #161616;
  font-family: 'Courier New', monospace;
  min-width: 40px;
  text-align: right;
}

/* ---- Debt Snowball Item ---- */
.debt-item {
  border: 1px solid #E8DCC8;
  border-radius: 4px;
  padding: 8px 10px;
  margin-bottom: 8px;
  background: #FCFAF7;
}
.debt-item .di-name {
  font-size: 9pt;
  font-weight: 700;
  color: #161616;
  margin-bottom: 5px;
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
    <div class="icon-arc"></div>
    <div class="icon-circle"></div>
    <div class="icon-circle-inner"></div>
    <div class="icon-dollar">$</div>
  </div>
  <div class="title-block">
    <div class="main-title">{BOOK_TITLE}</div>
    <div class="accent-bar"></div>
    <div class="subtitle">{BOOK_SUBTITLE}</div>
    <div class="features">
      <span class="feature-badge">12 Monthly Budgets</span>
      <span class="feature-badge">Expense Tracker</span>
      <span class="feature-badge">Debt Payoff</span>
      <span class="feature-badge">Savings Goals</span>
    </div>
    <div class="tagline">For Individuals, Couples &amp; Families</div>
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
    <div style="font-size: 16pt; font-weight: 700; color: #161616; margin-bottom: 6px;">This Planner Belongs To</div>
    <div style="width: 3.5in; border-bottom: 1.5px solid #161616; height: 24px; margin: 0 auto 16px;"></div>
  </div>

  <div style="width: 3.5in; margin: 0 auto;">
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Budgeting Period</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Primary Financial Goal</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">Target Savings This Year</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
    <div style="margin-bottom: 14px;">
      <div style="font-size: 8pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 3px;">My Money Motto</div>
      <div style="border-bottom: 0.5px solid #bbb; height: 18px;"></div>
    </div>
  </div>

  <div class="page-footer">
    <span>Budget &amp; Finance Planner</span>
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

  <div class="page-title">How to Use This Planner</div>
  <div class="page-subtitle">Your roadmap to financial peace of mind</div>

  <div class="info-box">
    <div class="info-title">Why Budget?</div>
    A budget is not about restriction &mdash; it is about intention. When you tell your money where to go instead of wondering where it went, you gain control, reduce stress, and accelerate toward the things that matter most to you. This planner gives you the tools to do exactly that.
  </div>

  <div style="font-size: 9pt; line-height: 1.7; color: #333;">
    <div style="font-weight: 700; color: #161616; font-size: 10pt; margin-bottom: 6px;">Six Steps to Financial Control</div>

    <div style="margin-bottom: 10px;">
      <strong>1. Set your goals.</strong> Before the numbers, know your &quot;why.&quot; Write down your short-term, mid-term, and long-term financial goals. They will guide every budgeting decision.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>2. Track your income.</strong> List every source of income &mdash; salary, side hustles, investments, and anything else. Knowing your total inflow is the foundation of every budget.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>3. List your expenses.</strong> Start with fixed costs (rent, insurance, debt payments), then estimate variable costs (groceries, dining, entertainment). Track daily for the first month to get real numbers.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>4. Build your budget.</strong> Allocate every dollar. Prioritize needs first, then savings, then wants. The goal is to spend less than you earn &mdash; every month.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>5. Track and adjust.</strong> Record actual spending against your plan weekly. Adjust as needed. A budget that does not bend will break &mdash; flexibility is part of the process.
    </div>
    <div style="margin-bottom: 10px;">
      <strong>6. Review and celebrate.</strong> At month-end, review what worked. Celebrate wins, learn from misses, and refine your plan. Every month gets easier.
    </div>
  </div>

  <div style="margin-top: 14px; padding: 8px 10px; background: #FAF6E8; border: 1px solid #E8D5A0; border-radius: 3px; font-size: 8pt; color: #666; font-style: italic;">
    <strong style="color: #8B6914;">The 50/30/20 Rule:</strong> A popular starting point &mdash; allocate roughly 50% to needs, 30% to wants, and 20% to savings and debt repayment. Adjust based on your situation.
  </div>

  <div class="page-footer">
    <span>Budget &amp; Finance Planner</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def budgeting_methods():
    methods = [
        ("50/30/20 Rule", "The simplest framework. 50% of income goes to needs (housing, food, insurance, minimum debt payments). 30% to wants (dining, entertainment, hobbies). 20% to savings and extra debt payments. Best for beginners who want a quick, flexible guideline.", "Best for: Beginners"),
        ("Zero-Based Budget", "Every dollar is assigned a job before the month begins. Income minus expenses equals exactly zero. Forces you to be intentional with every dollar. More work but maximum control.", "Best for: Detail-oriented planners"),
        ("Envelope System", "Allocate cash into labeled envelopes for each spending category. When an envelope is empty, that category is done for the month. Prevents overspending. Can be adapted digitally.", "Best for: Overspenders"),
        ("Pay Yourself First", "Automatically route savings off the top, then budget with what remains. Treats savings as a non-negotiable expense rather than an afterthought.", "Best for: Savers who struggle to save"),
        ("Incremental Budget", "Start with last month's actual spending and adjust up or down. Easy to maintain once you have a few months of data. Works well for stable income.", "Best for: Steady income earners"),
    ]

    rows = ""
    for name, desc, best in methods:
        rows += f'''
      <div style="border: 1px solid #E8DCC8; border-radius: 3px; padding: 7px 9px; margin-bottom: 6px; background: #FCFAF7;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
          <div style="font-size: 9.5pt; font-weight: 700; color: #161616;">{name}</div>
          <div style="font-size: 6.5pt; color: #C4A04A; font-weight: 700; text-transform: uppercase; letter-spacing: 0.3pt;">{best}</div>
        </div>
        <div style="font-size: 8pt; color: #555; line-height: 1.5;">{desc}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Budgeting Methods -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Budgeting Methods</span>
  </div>

  <div class="page-title">Budgeting Methods</div>
  <div class="page-subtitle">Find the approach that works for you</div>

  {rows}

  <div style="margin-top: 8px; padding: 6px 8px; background: #FAF6F0; border-radius: 3px; font-size: 7pt; color: #888; font-style: italic;">
    There is no single &quot;right&quot; way to budget. The best method is the one you will actually stick with.
  </div>

  <div class="page-footer">
    <span>Budget &amp; Finance Planner</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def expense_categories_reference():
    categories = [
        ("Housing", "Rent/Mortgage &bull; Property Tax &bull; Home Insurance &bull; HOA &bull; Repairs &bull; Utilities (gas, electric, water, trash)"),
        ("Transportation", "Car Payment &bull; Auto Insurance &bull; Fuel &bull; Maintenance &bull; Registration &bull; Public Transit &bull; Parking &bull; Rideshare"),
        ("Food &amp; Groceries", "Groceries &bull; Dining Out &bull; Coffee &bull; Work Lunches &bull; Snacks &bull; Delivery &bull; Alcohol"),
        ("Insurance &amp; Health", "Health Insurance &bull; Life Insurance &bull; Dental &bull; Vision &bull; Co-pays &bull; Prescriptions &bull; Gym &bull; Therapy"),
        ("Debt Payments", "Credit Cards &bull; Student Loans &bull; Personal Loans &bull; Medical Debt &bull; IRS/ Tax Debt &bull; Buy-Now-Pay-Later"),
        ("Subscriptions", "Streaming &bull; Phone &bull; Internet &bull; Software &bull; Memberships &bull; Magazines &bull; Cloud Storage &bull; Apps"),
        ("Personal &amp; Lifestyle", "Clothing &bull; Haircut/Beauty &bull; Personal Care &bull; Education &bull; Hobbies &bull; Gifts &bull; Kids Activities"),
        ("Entertainment", "Movies &bull; Concerts &bull; Events &bull; Hobbies &bull; Books &bull; Games &bull; Sports &bull; Travel &bull; Nights Out"),
        ("Savings &amp; Investments", "Emergency Fund &bull; Retirement (401k/IRA) &bull; Brokerage &bull; College Fund &bull; Sinking Funds &bull; Vacation Fund"),
    ]

    rows = ""
    for cat, items in categories:
        rows += f'''
      <div style="display: flex; gap: 8px; margin-bottom: 5px; padding: 5px 8px; border-left: 2.5px solid #C4A04A; background: #FAF6F0; border-radius: 0 3px 3px 0;">
        <div style="min-width: 100px; font-size: 8pt; font-weight: 700; color: #161616;">{cat}</div>
        <div style="font-size: 7pt; color: #555; line-height: 1.4; flex: 1;">{items}</div>
      </div>'''

    return f'''
<!-- Page {pn()}: Expense Categories -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Reference</span>
    <span class="sh-right">Expense Categories</span>
  </div>

  <div class="page-title">Expense Category Guide</div>
  <div class="page-subtitle">Organize your spending for clarity</div>

  {rows}

  <div class="page-footer">
    <span>Budget &amp; Finance Planner</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def financial_goals():
    return f'''
<!-- Page {pn()}: Financial Goals -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Goal Setting</span>
    <span class="sh-right">Define Your &quot;Why&quot;</span>
  </div>

  <div class="page-title">Financial Goals</div>
  <div class="page-subtitle">Clear goals make every dollar purposeful</div>

  <div class="info-box">
    <div class="info-title">SMART Goals</div>
    Specific &bull; Measurable &bull; Achievable &bull; Relevant &bull; Time-bound. &quot;Save more&quot; is a wish. &quot;Save $5,000 for an emergency fund by December&quot; is a goal.
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Short-Term (This Year)</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 12px; margin-bottom: 6px;">Mid-Term (1&ndash;5 Years)</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 12px; margin-bottom: 6px;">Long-Term (5+ Years)</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 12px; margin-bottom: 4px;">My #1 Priority This Year</div>
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 6px;">
    <span style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; min-width: 50px;">Goal</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 6px;">
    <span style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; min-width: 50px;">Amount</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>
  <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 6px;">
    <span style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; min-width: 50px;">By When</span>
    <div style="flex:1; border-bottom: 0.5px solid #bbb; height: 16px;"></div>
  </div>

  <div class="page-footer">
    <span>Budget &amp; Finance Planner</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def annual_overview():
    return f'''
<!-- Page {pn()}: Annual Overview -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Annual Overview</span>
    <span class="sh-right">The Year at a Glance</span>
  </div>

  <div class="page-title">Annual Financial Overview</div>
  <div class="page-subtitle">Your roadmap for the year ahead</div>

  <table class="money-table" style="font-size: 7.5pt;">
    <tr>
      <th>Month</th>
      <th class="amt">Income</th>
      <th class="amt">Expenses</th>
      <th class="amt">Saved</th>
      <th class="amt">Net</th>
    </tr>
    <tr><td>January</td><td class="amt"></td><td class="amt"></td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>February</td><td class="amt"></td><td class="amt"></td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>March</td><td class="amt"></td><td class="amt"></td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>April</td><td class="amt"></td><td class="amt"></td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>May</td><td class="amt"></td><td class="amt"></td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>June</td><td class="amt"></td><td class="amt"></td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>July</td><td class="amt"></td><td class="amt"></td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>August</td><td class="amt"></td><td class="amt"></td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>September</td><td class="amt"></td><td class="amt"></td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>October</td><td class="amt"></td><td class="amt"></td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>November</td><td class="amt"></td><td class="amt"></td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>December</td><td class="amt"></td><td class="amt"></td><td class="amt"></td><td class="amt"></td></tr>
    <tr class="total-row"><td>TOTAL</td><td class="amt"></td><td class="amt"></td><td class="amt"></td><td class="amt"></td></tr>
  </table>

  <div style="margin-top: 14px;">
    <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Year's Focus</div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
    <div class="wline-sm"></div>
  </div>

  <div class="page-footer">
    <span>Budget &amp; Finance Planner</span>
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


def monthly_budget_left(month_name):
    """Left page: Income + Planned Expenses"""
    return f'''
<!-- Page {pn()}: {month_name} Budget Left -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">{month_name} &mdash; Income &amp; Planned Budget</span>
    <span class="sh-right">Budget &amp; Finance Planner</span>
  </div>

  <div class="page-title">{month_name} Budget</div>
  <div class="page-subtitle">Plan your income and allocate your spending</div>

  <!-- Income Section -->
  <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Income</div>
  <table class="money-table" style="font-size: 7.5pt; margin-bottom: 8px;">
    <tr>
      <th>Source</th>
      <th class="amt">Planned ($)</th>
      <th class="amt">Actual ($)</th>
    </tr>
    <tr><td>Primary Salary</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Secondary / Side</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Freelance / Bonus</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Investment / Other</td><td class="amt"></td><td class="amt"></td></tr>
    <tr class="total-row"><td>Total Income</td><td class="amt"></td><td class="amt"></td></tr>
  </table>

  <!-- Planned Expenses -->
  <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Planned Expenses</div>
  <table class="money-table" style="font-size: 7pt;">
    <tr>
      <th>Category</th>
      <th class="amt">Planned ($)</th>
    </tr>
    <tr><td>Housing / Rent</td><td class="amt"></td></tr>
    <tr><td>Utilities</td><td class="amt"></td></tr>
    <tr><td>Groceries</td><td class="amt"></td></tr>
    <tr><td>Dining Out</td><td class="amt"></td></tr>
    <tr><td>Transportation</td><td class="amt"></td></tr>
    <tr><td>Insurance</td><td class="amt"></td></tr>
    <tr><td>Debt Payments</td><td class="amt"></td></tr>
    <tr><td>Subscriptions</td><td class="amt"></td></tr>
    <tr><td>Personal / Lifestyle</td><td class="amt"></td></tr>
    <tr><td>Entertainment</td><td class="amt"></td></tr>
    <tr><td>Savings / Investment</td><td class="amt"></td></tr>
    <tr><td>Other</td><td class="amt"></td></tr>
    <tr class="total-row"><td>Total Expenses</td><td class="amt"></td></tr>
  </table>

  <div class="page-footer">
    <span>{month_name} &mdash; Budget Plan</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def monthly_budget_right(month_name):
    """Right page: Expense tracker + summary"""
    return f'''
<!-- Page {pn()}: {month_name} Budget Right -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">{month_name} &mdash; Tracker &amp; Summary</span>
    <span class="sh-right">Monthly Review</span>
  </div>

  <div class="page-title">{month_name} Tracker</div>
  <div class="page-subtitle">Record actual spending and review your month</div>

  <!-- Actual Expenses -->
  <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Actual Expenses</div>
  <table class="money-table" style="font-size: 7pt;">
    <tr>
      <th>Category</th>
      <th class="amt">Actual ($)</th>
      <th class="amt">Diff ($)</th>
    </tr>
    <tr><td>Housing / Rent</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Utilities</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Groceries</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Dining Out</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Transportation</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Insurance</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Debt Payments</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Subscriptions</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Personal / Lifestyle</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Entertainment</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Savings / Investment</td><td class="amt"></td><td class="amt"></td></tr>
    <tr><td>Other</td><td class="amt"></td><td class="amt"></td></tr>
    <tr class="total-row"><td>Total Actual</td><td class="amt"></td><td class="amt"></td></tr>
  </table>

  <!-- Summary -->
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-top: 10px;">
    <div class="summary-card">
      <div class="sc-label">Income</div>
      <div class="sc-value"></div>
    </div>
    <div class="summary-card">
      <div class="sc-label">Expenses</div>
      <div class="sc-value"></div>
    </div>
    <div class="summary-card">
      <div class="sc-label">Remaining</div>
      <div class="sc-value"></div>
    </div>
  </div>

  <!-- Reflection -->
  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 4px;">Month Reflection</div>
  <div style="font-size: 6.5pt; color: #aaa; font-style: italic; margin-bottom: 3px;">What went well?</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div style="font-size: 6.5pt; color: #aaa; font-style: italic; margin-top: 6px; margin-bottom: 3px;">What to improve next month?</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>{month_name} &mdash; Tracker &amp; Summary</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def weekly_expense_tracker(page_of, total_pages):
    """Weekly expense log — granular spending tracker"""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    rows = ""
    for day in days:
        rows += f'''
    <tr><td style="font-weight:700;color:#161616;">{day}</td><td></td><td></td><td class="amt"></td></tr>
    <tr><td style="font-size:6pt;color:#ccc;">&nbsp;</td><td></td><td></td><td class="amt"></td></tr>'''

    return f'''
<!-- Page {pn()}: Weekly Tracker -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Weekly Expense Tracker</span>
    <span class="sh-right">Page {page_of} of {total_pages}</span>
  </div>

  <div class="page-title">Weekly Expense Tracker</div>
  <div class="page-subtitle">Log every purchase to see where your money goes</div>

  <table class="money-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:62px;">Day</th>
      <th>Description</th>
      <th style="width:58px;">Category</th>
      <th class="amt" style="width:50px;">Amount</th>
    </tr>
    {rows}
    <tr class="total-row"><td>Total</td><td></td><td></td><td class="amt"></td></tr>
  </table>

  <div class="page-footer">
    <span>Budget &amp; Finance Planner</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def savings_goals():
    """Savings goals tracker with progress bars"""
    goals = [
        "Emergency Fund (3&ndash;6 months expenses)",
        "Vacation / Travel Fund",
        "Home Down Payment",
        "Vehicle / Car Fund",
        "Home Repair / Improvement",
        "Christmas / Holiday Gifts",
        "Education / Course Fund",
        "Retirement Supplement",
    ]

    goal_rows = ""
    for goal in goals:
        goal_rows += f'''
      <div class="debt-item">
        <div class="di-name">{goal}</div>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4px 10px; margin-bottom: 5px;">
          <div style="display:flex;align-items:baseline;gap:3px;">
            <span style="font-size:6pt;font-weight:700;color:#C4A04A;text-transform:uppercase;">Target</span>
            <div style="flex:1;border-bottom:0.5px solid #ddd;height:12px;"></div>
          </div>
          <div style="display:flex;align-items:baseline;gap:3px;">
            <span style="font-size:6pt;font-weight:700;color:#C4A04A;text-transform:uppercase;">Saved</span>
            <div style="flex:1;border-bottom:0.5px solid #ddd;height:12px;"></div>
          </div>
          <div style="display:flex;align-items:baseline;gap:3px;">
            <span style="font-size:6pt;font-weight:700;color:#C4A04A;text-transform:uppercase;">By Date</span>
            <div style="flex:1;border-bottom:0.5px solid #ddd;height:12px;"></div>
          </div>
        </div>
        <div class="progress-row">
          <span class="progress-label">Progress</span>
          <div class="progress-track"></div>
          <span class="progress-amt"></span>
        </div>
      </div>'''

    return f'''
<!-- Page {pn()}: Savings Goals -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Savings Goals</span>
    <span class="sh-right">Track Your Progress</span>
  </div>

  <div class="page-title">Savings Goals Tracker</div>
  <div class="page-subtitle">Visualize your path to each milestone</div>

  {goal_rows}

  <div class="page-footer">
    <span>Budget &amp; Finance Planner</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def debt_payoff():
    """Debt payoff tracker — snowball method"""
    debts = list(range(1, 9))

    debt_rows = ""
    for i in debts:
        debt_rows += f'''
      <div class="debt-item">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
          <div class="di-name">Debt #{i}</div>
          <div style="font-size:6pt;color:#C4A04A;font-weight:700;text-transform:uppercase;">Paid &#10063;</div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 4px 8px; margin-bottom: 5px;">
          <div style="display:flex;align-items:baseline;gap:3px;">
            <span style="font-size:6pt;font-weight:700;color:#C4A04A;text-transform:uppercase;">Creditor</span>
            <div style="flex:1;border-bottom:0.5px solid #ddd;height:12px;"></div>
          </div>
          <div style="display:flex;align-items:baseline;gap:3px;">
            <span style="font-size:6pt;font-weight:700;color:#C4A04A;text-transform:uppercase;">Balance</span>
            <div style="flex:1;border-bottom:0.5px solid #ddd;height:12px;"></div>
          </div>
          <div style="display:flex;align-items:baseline;gap:3px;">
            <span style="font-size:6pt;font-weight:700;color:#C4A04A;text-transform:uppercase;">Rate %</span>
            <div style="flex:1;border-bottom:0.5px solid #ddd;height:12px;"></div>
          </div>
          <div style="display:flex;align-items:baseline;gap:3px;">
            <span style="font-size:6pt;font-weight:700;color:#C4A04A;text-transform:uppercase;">Min Pay</span>
            <div style="flex:1;border-bottom:0.5px solid #ddd;height:12px;"></div>
          </div>
        </div>
        <div class="progress-row">
          <span class="progress-label">Payoff Progress</span>
          <div class="progress-track"></div>
          <span class="progress-amt"></span>
        </div>
      </div>'''

    return f'''
<!-- Page {pn()}: Debt Payoff -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Debt Payoff Tracker</span>
    <span class="sh-right">Snowball Method</span>
  </div>

  <div class="page-title">Debt Payoff Tracker</div>
  <div class="page-subtitle">List debts smallest to largest. Pay minimums on all, attack the smallest with everything extra.</div>

  {debt_rows}

  <div class="page-footer">
    <span>Budget &amp; Finance Planner</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def bills_tracker():
    """Recurring bills and subscription tracker"""
    return f'''
<!-- Page {pn()}: Bills Tracker -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Bills &amp; Subscriptions</span>
    <span class="sh-right">Recurring Payments</span>
  </div>

  <div class="page-title">Bills &amp; Subscription Tracker</div>
  <div class="page-subtitle">Never miss a payment or forget a subscription</div>

  <table class="data-table" style="font-size: 7.5pt;">
    <tr>
      <th style="width:18px;">#</th>
      <th>Bill / Subscription</th>
      <th style="width:42px;">Due Day</th>
      <th style="width:40px;">Amount</th>
      <th style="width:40px;">Freq.</th>
      <th style="width:30px;">Auto?</th>
      <th style="width:28px;">&#10003;</th>
    </tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">1</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">2</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">3</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">4</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">5</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">6</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">7</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">8</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">9</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">10</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">11</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">12</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">13</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">14</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">15</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">16</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">17</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
    <tr><td style="text-align:center;font-weight:700;color:#C4A04A;">18</td><td></td><td></td><td></td><td></td><td style="text-align:center;"></td><td style="text-align:center;"></td></tr>
  </table>

  <div style="font-size: 6pt; color: #aaa; margin-top: 3px;">Freq: M=Monthly, Q=Quarterly, A=Annually, W=Weekly | Auto: Y/N</div>

  <div class="page-footer">
    <span>Budget &amp; Finance Planner</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def net_worth_tracker():
    """Net worth summary — assets minus liabilities"""
    return f'''
<!-- Page {pn()}: Net Worth -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Net Worth Tracker</span>
    <span class="sh-right">Assets &minus; Liabilities</span>
  </div>

  <div class="page-title">Net Worth Statement</div>
  <div class="page-subtitle">Your financial snapshot</div>

  <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Assets (What You Own)</div>
  <table class="money-table" style="font-size: 7.5pt; margin-bottom: 8px;">
    <tr>
      <th>Asset</th>
      <th class="amt">Amount ($)</th>
    </tr>
    <tr><td>Cash / Checking</td><td class="amt"></td></tr>
    <tr><td>Savings Account</td><td class="amt"></td></tr>
    <tr><td>Investment / Brokerage</td><td class="amt"></td></tr>
    <tr><td>Retirement (401k / IRA)</td><td class="amt"></td></tr>
    <tr><td>Home Value</td><td class="amt"></td></tr>
    <tr><td>Vehicle(s)</td><td class="amt"></td></tr>
    <tr><td>Other Assets</td><td class="amt"></td></tr>
    <tr class="total-row"><td>Total Assets</td><td class="amt"></td></tr>
  </table>

  <div style="font-size: 7pt; font-weight: 700; color: #C4A04A; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 4px;">Liabilities (What You Owe)</div>
  <table class="money-table" style="font-size: 7.5pt; margin-bottom: 8px;">
    <tr>
      <th>Liability</th>
      <th class="amt">Amount ($)</th>
    </tr>
    <tr><td>Mortgage</td><td class="amt"></td></tr>
    <tr><td>Auto Loan</td><td class="amt"></td></tr>
    <tr><td>Credit Card Debt</td><td class="amt"></td></tr>
    <tr><td>Student Loans</td><td class="amt"></td></tr>
    <tr><td>Personal Loans</td><td class="amt"></td></tr>
    <tr><td>Medical Debt</td><td class="amt"></td></tr>
    <tr><td>Other Debt</td><td class="amt"></td></tr>
    <tr class="total-row"><td>Total Liabilities</td><td class="amt"></td></tr>
  </table>

  <div class="summary-card" style="display:flex;justify-content:space-between;align-items:center;">
    <div>
      <div class="sc-label">Net Worth (Assets &minus; Liabilities)</div>
    </div>
    <div class="sc-value" style="font-size: 14pt;">$</div>
  </div>

  <div class="page-footer">
    <span>Budget &amp; Finance Planner</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def year_review():
    """Year-end review and reflection"""
    return f'''
<!-- Page {pn()}: Year Review -->
<div class="page">
  <div class="section-header">
    <span class="sh-left">Year-End Review</span>
    <span class="sh-right">Reflect &amp; Plan Ahead</span>
  </div>

  <div class="page-title">Year-End Financial Review</div>
  <div class="page-subtitle">Celebrate progress and plan the year ahead</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 14px;">
    <div class="summary-card" style="text-align:center;">
      <div class="sc-label">Total Saved</div>
      <div class="sc-value" style="font-size: 16pt;"></div>
    </div>
    <div class="summary-card" style="text-align:center;">
      <div class="sc-label">Debt Paid Off</div>
      <div class="sc-value" style="font-size: 16pt;"></div>
    </div>
    <div class="summary-card" style="text-align:center;">
      <div class="sc-label">Net Worth Change</div>
      <div class="sc-value" style="font-size: 16pt;"></div>
    </div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-bottom: 6px;">Biggest Financial Win This Year</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 6px;">Biggest Lesson Learned</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div style="font-size: 7pt; font-weight: 700; color: #161616; text-transform: uppercase; letter-spacing: 0.4pt; margin-top: 10px; margin-bottom: 6px;">Goals for Next Year</div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>
  <div class="wline-sm"></div>

  <div class="page-footer">
    <span>Budget &amp; Finance Planner</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


def notes_page(page_num):
    """Blank lined notes page"""
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

  <div class="page-title">Financial Notes</div>
  <div class="page-subtitle">Ideas, reminders, and planning</div>

  {lines}

  <div class="page-footer">
    <span>Budget &amp; Finance Planner</span>
    <span>{page_no[0]}</span>
  </div>
</div>
'''


# ============================================================
# MAIN
# ============================================================
def main():
    pages = []

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    # ---- Front Matter ----
    pages.append(cover_page())                          # 1: Cover
    pages.append(owner_page())                           # 2: Owner page

    # ---- Reference Section ----
    pages.append(how_to_use())                           # 3: How to use
    pages.append(budgeting_methods())                    # 4: Budgeting methods
    pages.append(expense_categories_reference())         # 5: Expense categories
    pages.append(financial_goals())                      # 6: Financial goals
    pages.append(annual_overview())                      # 7: Annual overview

    # ---- Section 1: Monthly Budgets ----
    pages.append(divider_section(1, "One", "Monthly Budgets", "12 months &mdash; plan, track, and adjust"))
    for month in months:
        pages.append(monthly_budget_left(month))         # Left: income + planned
        pages.append(monthly_budget_right(month))        # Right: tracker + summary

    # ---- Section 2: Weekly Expense Tracking ----
    pages.append(divider_section(2, "Two", "Weekly Expense Tracking", "Log every purchase"))
    for i in range(6):
        pages.append(weekly_expense_tracker(i + 1, 6))   # 6 weekly trackers

    # ---- Section 3: Savings Goals ----
    pages.append(divider_section(3, "Three", "Savings Goals", "Watch your progress grow"))
    pages.append(savings_goals())                        # Goals tracker

    # ---- Section 4: Debt Payoff ----
    pages.append(divider_section(4, "Four", "Debt Payoff", "Snowball your way to freedom"))
    pages.append(debt_payoff())                          # Debt tracker

    # ---- Section 5: Bills & Net Worth ----
    pages.append(divider_section(5, "Five", "Bills &amp; Net Worth", "Stay on top of recurring payments"))
    pages.append(bills_tracker())                        # Bills tracker
    pages.append(net_worth_tracker())                    # Net worth

    # ---- Section 6: Year-End Review ----
    pages.append(divider_section(6, "Six", "Year-End Review", "Reflect and plan ahead"))
    pages.append(year_review())                          # Year review

    # ---- Section 7: Notes ----
    pages.append(divider_section(7, "Seven", "Notes", "Ideas, reminders, and planning"))
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
    print(f"  Reference (how-to, methods, categories, goals, overview): 5")
    print(f"  Section dividers: 7")
    print(f"  Monthly budgets (12 x 2): 24")
    print(f"  Weekly trackers: 6")
    print(f"  Savings goals: 1")
    print(f"  Debt payoff: 1")
    print(f"  Bills tracker: 1")
    print(f"  Net worth: 1")
    print(f"  Year review: 1")
    print(f"  Notes pages: 4")
    print(f"  TOTAL: {total_pages}")


if __name__ == "__main__":
    main()
