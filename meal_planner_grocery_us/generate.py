#!/usr/bin/env python3
"""
Meal Planner & Grocery — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Busy families, home cooks, meal prep enthusiasts
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "meal_planner_grocery_us_V1.0.html")

BOOK_TITLE = "Meal Planner & Grocery"
BOOK_SUBTITLE = "52 Weeks of Healthy Eating Made Simple"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

def nl(n):
    return "\n".join('<div class="notes-line"></div>' for _ in range(n))

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
@media print  { .page { border: none; margin: 0; } }

/* ================ INTERIOR TITLE PAGE ================ */
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
  opacity: 0.05;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #C4A04A, transparent);
}

.cover .title-main {
  font-size: 30pt;
  font-weight: 700;
  color: #FAF6F0;
  line-height: 1.2;
  letter-spacing: 1pt;
  position: relative;
  z-index: 2;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 100px;
  height: 2px;
  background: #C4A04A;
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
  color: #161616;
  letter-spacing: 0.5pt;
  text-transform: uppercase;
}

.section-line {
  flex: 1;
  height: 1px;
  background: #C4A04A;
  margin: 0 12px;
  opacity: 0.5;
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
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 1pt;
  font-weight: 700;
}

.page-header .ph-right {
  font-size: 8pt;
  color: #999;
}

/* ================ WEEKLY SPREAD ================ */
.week-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1.5px solid #C4A04A;
  padding-bottom: 6px;
  margin-bottom: 12px;
}

.week-banner .wb-label {
  font-size: 9pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 1pt;
}

.week-banner .wb-line {
  flex: 1;
  height: 14px;
  border-bottom: 1px dotted #ccc;
}

.week-banner .wb-box {
  display: inline-block;
  border: 1.5px solid #C4A04A;
  border-radius: 4px;
  padding: 3px 10px;
  font-size: 8pt;
  color: #C4A04A;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

/* Day meal row */
.day-row {
  display: grid;
  grid-template-columns: 55px 1fr;
  gap: 0;
  border: 1px solid #ddd;
  border-radius: 3px;
  margin-bottom: 4px;
  overflow: hidden;
}

.day-label {
  background: #FAF6F0;
  border-right: 1px solid #ddd;
  padding: 4px 6px;
  font-size: 8pt;
  font-weight: 700;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

.day-meals {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 0;
}

.meal-cell {
  padding: 3px 5px;
  border-right: 1px solid #eee;
  font-size: 7.5pt;
  min-height: 32px;
}

.meal-cell:last-child { border-right: none; }

.meal-cell .mc-label {
  font-size: 6pt;
  color: #aaa;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  display: block;
  margin-bottom: 1px;
}

.meal-write {
  height: 18px;
}

/* Snacks & Water */
.snack-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-top: 6px;
}

.snack-box {
  border: 1px solid #C4A04A;
  border-radius: 3px;
  padding: 5px 8px;
  background: #FAF6F0;
}

.snack-box .sb-label {
  font-size: 7pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 2px;
}

.snack-box .sb-write {
  height: 14px;
}

.water-tracker {
  display: flex;
  gap: 3px;
  margin-top: 2px;
}

.water-circle {
  width: 12px;
  height: 12px;
  border: 1.5px solid #C4A04A;
  border-radius: 50%;
}

/* Notes / shopping list area */
.weekly-notes {
  border-left: 3px solid #C4A04A;
  padding: 6px 10px;
  margin-top: 6px;
  background: #FAF6F0;
  min-height: 30px;
}

.weekly-notes .wn-label {
  font-size: 7pt;
  color: #7A8B6F;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 2px;
}

/* ================ GROCERY LIST ================ */
.grocery-header {
  text-align: center;
  margin-bottom: 10px;
}

.grocery-title {
  font-size: 16pt;
  font-weight: 700;
  color: #161616;
}

.grocery-sub {
  font-size: 9pt;
  color: #999;
  font-style: italic;
  margin-top: 2px;
}

.grocery-cols {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.grocery-section {
  margin-bottom: 10px;
}

.grocery-cat {
  font-size: 8pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 1pt;
  font-weight: 700;
  border-bottom: 1px solid #C4A04A;
  padding-bottom: 2px;
  margin-bottom: 4px;
}

.grocery-item {
  display: flex;
  align-items: center;
  gap: 6px;
  height: 20px;
  border-bottom: 1px dotted #eee;
}

.grocery-check {
  width: 10px;
  height: 10px;
  border: 1px solid #C4A04A;
  border-radius: 2px;
  flex-shrink: 0;
}

.grocery-write {
  flex: 1;
  border-bottom: 1px dotted #ccc;
  height: 14px;
  font-size: 8pt;
}

/* ================ HOW TO USE ================ */
.howto-text {
  font-size: 10pt;
  line-height: 1.7;
  color: #2A2A2A;
}

.howto-text p {
  margin-bottom: 10px;
}

.howto-text .ht-title {
  font-size: 11pt;
  font-weight: 700;
  color: #161616;
  margin-bottom: 4px;
  margin-top: 6px;
}

.howto-text .ht-icon {
  color: #C4A04A;
  font-weight: 700;
  margin-right: 4px;
}

/* ================ NOTES ================ */
.notes-line {
  border-bottom: 1px solid #ddd;
  height: 22px;
}

/* ================ FINAL PAGE ================ */
.final-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100%;
}

.final-page .fp-text {
  font-size: 12pt;
  color: #999;
  font-style: italic;
  line-height: 1.8;
  margin-bottom: 20px;
}

.final-page .fp-logo {
  font-size: 11pt;
  color: #C4A04A;
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  font-weight: 700;
}

.final-page .fp-line {
  width: 60px;
  height: 1.5px;
  background: #C4A04A;
  margin: 12px auto;
  opacity: 0.5;
}
"""

# ============================================================
# PAGE GENERATORS
# ============================================================

def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- Plate -->
      <circle cx="50" cy="55" r="32" stroke="#C4A04A" stroke-width="1.5" fill="none"/>
      <circle cx="50" cy="55" r="26" stroke="#C4A04A" stroke-width="1" fill="none" opacity="0.5"/>
      <!-- Fork -->
      <line x1="18" y1="25" x2="18" y2="75" stroke="#C4A04A" stroke-width="1.5"/>
      <line x1="15" y1="25" x2="15" y2="35" stroke="#C4A04A" stroke-width="1"/>
      <line x1="18" y1="25" x2="18" y2="35" stroke="#C4A04A" stroke-width="1"/>
      <line x1="21" y1="25" x2="21" y2="35" stroke="#C4A04A" stroke-width="1"/>
      <!-- Knife -->
      <line x1="82" y1="25" x2="82" y2="75" stroke="#C4A04A" stroke-width="1.5"/>
      <path d="M 78 25 L 86 25 L 82 38 Z" stroke="#C4A04A" stroke-width="1" fill="none"/>
    </svg>
  </div>

  <div class="title-main">Meal Planner<br>&amp; Grocery</div>
  <div class="accent-bar"></div>
  <div class="subtitle">52 Weeks of Healthy Eating Made Simple</div>

  <div class="pub">More Shine Press</div>
</div>""" % pn()


def how_to_use_page():
    pg = pn()
    return """<!-- PAGE %d: How to Use -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">How to Use This Planner</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Plan Once, Eat Well All Week</div>
    <p>This planner is designed to make meal planning simple and stress-free.
    Each week, you get a <strong>weekly meal plan</strong> spread where you can
    map out breakfast, lunch, and dinner for all seven days, plus snacks and
    water intake tracking.</p>

    <p>On the facing page, you will find a <strong>grocery shopping list</strong>
    organized by section of the store &mdash; produce, meat and seafood, dairy,
    pantry, frozen, and more. Tear it out or take a photo before you shop.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Simple Steps Each Week</div>
    <p>&#9312; Check your calendar &mdash; note any busy nights or eating-out plans.</p>
    <p>&#9313; Plan meals based on what you already have and what is in season.</p>
    <p>&#9314; Write your grocery list from the meal plan.</p>
    <p>&#9315; Shop once, prep what you can, and enjoy a week of easy meals.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips for Success</div>
    <p>&#9679; Plan leftovers intentionally &mdash; cook once, eat twice.</p>
    <p>&#9679; Keep a well-stocked pantry with basics like rice, pasta, and canned goods.</p>
    <p>&#9679; Plan a mix of quick weeknight meals and bigger weekend projects.</p>
    <p>&#9679; Use the notes section for recipes to try next week.</p>
  </div>
</div>""" % (pg, pg)


def pantry_staples_page():
    pg = pn()
    categories = [
        ("Produce", ["Onions", "Garlic", "Potatoes", "Carrots", "Lettuce", "Tomatoes",
                      "Bananas", "Apples", "Lemons", "Avocados", "Broccoli", "Spinach"]),
        ("Meat & Seafood", ["Chicken breasts", "Ground beef", "Pork chops", "Salmon",
                             "Shrimp", "Bacon", "Sausage", "Turkey"]),
        ("Dairy & Eggs", ["Milk", "Eggs", "Butter", "Cheese", "Yogurt", "Cream",
                           "Sour cream", "Cottage cheese"]),
        ("Pantry", ["Rice", "Pasta", "Olive oil", "Flour", "Sugar", "Canned tomatoes",
                     "Broth", "Spices", "Bread", "Oats", "Peanut butter", "Coffee/Tea"]),
        ("Frozen", ["Frozen vegetables", "Frozen fruit", "Ice cream", "Frozen pizza",
                      "Frozen meals", "Frozen herbs"]),
        ("Other", ["Snacks", "Condiments", "Beverages", "Paper goods", "Cleaning supplies"]),
    ]

    cols_html = ""
    for cat_name, items in categories:
        items_html = "\n".join(
            '<div class="grocery-item"><div class="grocery-check"></div>'
            '<div class="grocery-write"></div></div>'
            for _ in items
        )
        cols_html += """<div class="grocery-section">
  <div class="grocery-cat">%s</div>
  %s
</div>
""" % (H.escape(cat_name), items_html)

    return """<!-- PAGE %d: Pantry Staples -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Pantry Staples Checklist</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Starter Pantry</div>
    <p>Check off the items you like to keep on hand. These staples form the
    foundation of countless quick and easy meals.</p>
  </div>

  <div class="grocery-cols">
    %s
  </div>
</div>""" % (pg, pg, cols_html)


def weekly_plan_spread():
    """Left page: weekly meal plan grid."""
    pg = pn()
    days = [
        ("Monday", "M"),
        ("Tuesday", "T"),
        ("Wednesday", "W"),
        ("Thursday", "T"),
        ("Friday", "F"),
        ("Saturday", "S"),
        ("Sunday", "S"),
    ]
    day_rows = ""
    for day_name, _abbrev in days:
        day_rows += """<div class="day-row">
    <div class="day-label">%s</div>
    <div class="day-meals">
      <div class="meal-cell"><span class="mc-label">Breakfast</span><div class="meal-write"></div></div>
      <div class="meal-cell"><span class="mc-label">Lunch</span><div class="meal-write"></div></div>
      <div class="meal-cell"><span class="mc-label">Dinner</span><div class="meal-write"></div></div>
    </div>
  </div>
""" % H.escape(day_name)

    return """<!-- PAGE %d: Weekly Plan -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Weekly Meal Plan</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="week-banner">
    <span class="wb-label">Week of:</span>
    <div class="wb-line"></div>
    <span class="wb-box">Plan</span>
  </div>

  %s

  <div class="snack-row">
    <div class="snack-box">
      <div class="sb-label">Snacks</div>
      <div class="sb-write"></div>
      <div class="sb-write"></div>
    </div>
    <div class="snack-box">
      <div class="sb-label">Water Intake</div>
      <div class="water-tracker">
        %s
      </div>
    </div>
  </div>

  <div class="weekly-notes">
    <div class="wn-label">Notes &amp; Recipes to Try</div>
    <div style="height: 30px;"></div>
  </div>
</div>""" % (pg, pg, day_rows, "".join('<div class="water-circle"></div>' for _ in range(8)))


def grocery_list_page():
    """Right page: grocery shopping list."""
    pg = pn()
    categories = [
        ("Produce", 6),
        ("Meat & Seafood", 4),
        ("Dairy & Eggs", 4),
        ("Pantry", 6),
        ("Frozen", 3),
        ("Bakery", 3),
        ("Beverages", 3),
        ("Other", 4),
    ]

    left_sections = ""
    right_sections = ""
    for i, (cat_name, n_items) in enumerate(categories):
        items_html = "\n".join(
            '<div class="grocery-item"><div class="grocery-check"></div>'
            '<div class="grocery-write"></div></div>'
            for _ in range(n_items)
        )
        section_html = """<div class="grocery-section">
  <div class="grocery-cat">%s</div>
  %s
</div>
""" % (H.escape(cat_name), items_html)
        if i % 2 == 0:
            left_sections += section_html
        else:
            right_sections += section_html

    return """<!-- PAGE %d: Grocery List -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Grocery Shopping List</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="grocery-header">
    <div class="grocery-title">Shopping List</div>
    <div class="grocery-sub">Check off as you shop</div>
  </div>

  <div class="grocery-cols">
    %s
    %s
  </div>

  <div style="margin-top: 10px; border-top: 1px solid #eee; padding-top: 8px;">
    <div class="grocery-cat" style="border: none; margin-bottom: 2px;">Budget Tracker</div>
    <div style="display: flex; gap: 16px; font-size: 8pt; color: #999;">
      <span>Estimated: $______</span>
      <span>Actual: $______</span>
    </div>
  </div>
</div>""" % (pg, pg, left_sections, right_sections)


def notes_page():
    pg = pn()
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes &amp; Favorite Recipes</span>
    <span class="ph-right">Page %d</span>
  </div>
  <div>
    %s
  </div>
</div>""" % (pg, pg, nl(28))


def final_page():
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="page">
  <div class="final-page">
    <div class="fp-text">
      Good food,<br>
      good planning,<br>
      good life.
    </div>
    <div class="fp-line"></div>
    <div class="fp-logo">More Shine Press</div>
    <div class="fp-line"></div>
  </div>
</div>""" % pg


# ============================================================
# MAIN
# ============================================================
def generate(output_path=HTML_FILE):
    pages = []

    # 1. Title page
    pages.append(interior_title_page())

    # 2. How to use
    pages.append(how_to_use_page())

    # 3. Pantry staples
    pages.append(pantry_staples_page())

    # 4-107. 52 weekly spreads (each = 2 pages: plan + grocery)
    for week in range(52):
        pages.append(weekly_plan_spread())
        pages.append(grocery_list_page())

    # Notes (3 pages)
    for _ in range(3):
        pages.append(notes_page())

    # Final
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
