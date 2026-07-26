#!/usr/bin/env python3
"""
Family Recipe Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: Home cooks, families, anyone preserving heirloom recipes
Publisher: More Shine Press
Zero-dependency: Python stdlib only, HTML + Chrome headless PDF export.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "family_recipe_journal_us_V1.0.html")

BOOK_TITLE = "Family Recipe Journal"
BOOK_SUBTITLE = "A Heirloom Cookbook to Write Down Your Best Recipes"

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
  font-size: 32pt;
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

/* ================ REFERENCE TABLES ================ */
.ref-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9pt;
  margin-bottom: 10px;
}

.ref-table th {
  background: #FAF6F0;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-size: 8pt;
  padding: 5px 8px;
  border-bottom: 1.5px solid #C4A04A;
  text-align: left;
}

.ref-table td {
  padding: 4px 8px;
  border-bottom: 0.5px solid #eee;
  color: #2A2A2A;
}

.ref-table tr:nth-child(even) td {
  background: #FCFAF7;
}

.ref-section {
  margin-bottom: 14px;
}

.ref-heading {
  font-size: 9pt;
  font-weight: 700;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 1pt;
  margin-bottom: 4px;
}

/* ================ RECIPE INDEX ================ */
.index-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9pt;
}

.index-table th {
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-size: 7.5pt;
  padding: 4px 6px;
  border-bottom: 1.5px solid #C4A04A;
  text-align: left;
}

.index-table td {
  padding: 3px 6px;
  border-bottom: 0.5px dotted #ddd;
  height: 24px;
  vertical-align: bottom;
}

.idx-letter {
  width: 20px;
  font-weight: 700;
  color: #C4A04A;
  font-size: 10pt;
}

.idx-name {
  width: auto;
}

.idx-page {
  width: 35px;
  text-align: right;
  color: #999;
  font-size: 8pt;
}

/* ================ RECIPE LEFT PAGE ================ */
.recipe-name-area {
  margin-bottom: 10px;
}

.rn-label {
  font-size: 7pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 1pt;
  font-weight: 700;
  margin-bottom: 2px;
}

.rn-line {
  border-bottom: 2px solid #161616;
  height: 28px;
}

.recipe-meta {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 6px;
  margin-bottom: 8px;
}

.meta-box {
  border: 1px solid #ddd;
  border-radius: 3px;
  padding: 4px 6px;
  text-align: center;
}

.meta-box .mb-label {
  font-size: 6pt;
  color: #aaa;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  display: block;
  margin-bottom: 1px;
}

.meta-box .mb-write {
  height: 16px;
  border-bottom: 1px dotted #ccc;
}

.recipe-meta2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
  margin-bottom: 8px;
}

.rating-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 10px;
  padding: 4px 0;
}

.rating-label {
  font-size: 7pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
}

.rating-stars {
  display: flex;
  gap: 4px;
}

.star {
  width: 14px;
  height: 14px;
  border: 1.5px solid #C4A04A;
  border-radius: 50%;
}

.difficulty-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-left: auto;
}

.diff-circle {
  display: inline-block;
  width: 14px;
  height: 14px;
  border: 1.5px solid #C4A04A;
  border-radius: 50%;
  vertical-align: middle;
  margin-right: 2px;
}

.diff-label {
  font-size: 7pt;
  color: #666;
}

.ingredients-header {
  display: flex;
  align-items: center;
  margin-bottom: 6px;
}

.ingredients-header .ih-text {
  font-size: 10pt;
  font-weight: 700;
  color: #161616;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.ingredients-header .ih-line {
  flex: 1;
  height: 1px;
  background: #C4A04A;
  margin-left: 8px;
  opacity: 0.4;
}

.ingredient-line {
  display: flex;
  align-items: center;
  gap: 6px;
  height: 21px;
  border-bottom: 0.5px dotted #ddd;
}

.ingredient-check {
  width: 10px;
  height: 10px;
  border: 1px solid #C4A04A;
  border-radius: 2px;
  flex-shrink: 0;
}

.ingredient-write {
  flex: 1;
  border-bottom: 1px dotted transparent;
  height: 14px;
}

/* ================ RECIPE RIGHT PAGE ================ */
.directions-header {
  display: flex;
  align-items: center;
  margin-bottom: 8px;
}

.directions-header .dh-text {
  font-size: 10pt;
  font-weight: 700;
  color: #161616;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
}

.directions-header .dh-line {
  flex: 1;
  height: 1px;
  background: #C4A04A;
  margin-left: 8px;
  opacity: 0.4;
}

.step-line {
  display: grid;
  grid-template-columns: 20px 1fr;
  gap: 4px;
  align-items: flex-start;
  height: 28px;
  border-bottom: 0.5px dotted #eee;
  margin-bottom: 1px;
}

.step-num {
  font-size: 8pt;
  color: #C4A04A;
  font-weight: 700;
  text-align: right;
  padding-top: 3px;
}

.step-write {
  border-bottom: 1px dotted transparent;
  height: 22px;
}

.notes-area {
  margin-top: 10px;
  border-left: 3px solid #C4A04A;
  padding: 6px 10px;
  background: #FAF6F0;
}

.notes-area .na-label {
  font-size: 7pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 4px;
}

.notes-area .na-line {
  border-bottom: 0.5px solid #ddd;
  height: 20px;
}

.date-made {
  margin-top: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.date-made .dm-label {
  font-size: 7pt;
  color: #C4A04A;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
}

.date-made .dm-line {
  flex: 1;
  border-bottom: 1px solid #ddd;
  height: 18px;
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
    <svg viewBox="0 0 100 100" width="90" height="90" xmlns="http://www.w3.org/2000/svg">
      <!-- Bowl -->
      <path d="M 15 50 Q 15 78 50 78 Q 85 78 85 50 Z" stroke="#C4A04A" stroke-width="1.5" fill="none"/>
      <!-- Steam -->
      <path d="M 38 38 Q 36 30 40 24 Q 44 18 40 12" stroke="#C4A04A" stroke-width="1" fill="none" opacity="0.5"/>
      <path d="M 50 36 Q 48 28 52 22 Q 56 16 52 10" stroke="#C4A04A" stroke-width="1" fill="none" opacity="0.4"/>
      <path d="M 62 38 Q 60 30 64 24 Q 68 18 64 12" stroke="#C4A04A" stroke-width="1" fill="none" opacity="0.5"/>
    </svg>
  </div>

  <div class="title-main">Family<br>Recipe Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">A Heirloom Cookbook to Write Down<br>Your Best Recipes</div>

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
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Your Kitchen Legacy</div>
    <p>This recipe journal is designed to preserve your family's
    most treasured recipes in one beautiful book. From Grandma's
    secret sauce to your own weeknight favorites, every dish
    deserves to be written down and passed on.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Each Recipe Gets Two Pages</div>
    <p>The <strong>left page</strong> is for the recipe name, who
    shared it with you, prep and cook times, servings, a difficulty
    rating, a star rating, and the full ingredients list with handy
    check boxes.</p>
    <p>The <strong>right page</strong> is for step-by-step directions,
    notes and tips, and the date you last made the dish.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Using the Index</div>
    <p>The recipe index at the front lets you list every recipe by
    name and page number, so you can find any dish in seconds.
    Fill it in as you add recipes.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Tips</div>
    <p>&#9679; Write the recipe name on the index page first, then note
    the page number where the recipe begins.</p>
    <p>&#9679; Use the check boxes next to each ingredient as you gather
    and measure &mdash; great for mise en place.</p>
    <p>&#9679; Note substitutions and variations in the notes section.</p>
    <p>&#9679; Pass this book on to the next generation someday.</p>
  </div>
</div>""" % (pg, pg)


def measurement_equivalents_page():
    pg = pn()
    return """<!-- PAGE %d: Measurement Equivalents -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Measurement Equivalents</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="ref-section">
    <div class="ref-heading">Dry &amp; Liquid Measures (US)</div>
    <table class="ref-table">
      <tr><th>Amount</th><th>Equivalent</th><th>Amount</th><th>Equivalent</th></tr>
      <tr><td>1/8 tsp</td><td>0.5 ml</td><td>1 cup</td><td>8 fl oz / 240 ml</td></tr>
      <tr><td>1/4 tsp</td><td>1.25 ml</td><td>2 cups</td><td>1 pint / 480 ml</td></tr>
      <tr><td>1/2 tsp</td><td>2.5 ml</td><td>4 cups</td><td>1 quart / 950 ml</td></tr>
      <tr><td>1 tsp</td><td>5 ml</td><td>2 pints</td><td>1 quart / 950 ml</td></tr>
      <tr><td>1 tbsp</td><td>3 tsp / 15 ml</td><td>4 quarts</td><td>1 gallon / 3.8 L</td></tr>
      <tr><td>1/4 cup</td><td>4 tbsp / 60 ml</td><td>1 fl oz</td><td>2 tbsp / 30 ml</td></tr>
      <tr><td>1/3 cup</td><td>5 tbsp + 1 tsp</td><td>1 stick butter</td><td>1/2 cup / 8 tbsp</td></tr>
      <tr><td>1/2 cup</td><td>8 tbsp / 120 ml</td><td>1 lb</td><td>16 oz / 454 g</td></tr>
    </table>
  </div>

  <div class="ref-section">
    <div class="ref-heading">Oven Temperatures</div>
    <table class="ref-table">
      <tr><th>Description</th><th>&deg;F</th><th>&deg;C</th><th>Gas Mark</th></tr>
      <tr><td>Very Slow</td><td>250&ndash;275</td><td>120&ndash;135</td><td>1/2&ndash;1</td></tr>
      <tr><td>Slow</td><td>300&ndash;325</td><td>150&ndash;165</td><td>2&ndash;3</td></tr>
      <tr><td>Moderate</td><td>350&ndash;375</td><td>175&ndash;190</td><td>4&ndash;5</td></tr>
      <tr><td>Hot</td><td>400&ndash;425</td><td>200&ndash;220</td><td>6&ndash;7</td></tr>
      <tr><td>Very Hot</td><td>450&ndash;475</td><td>230&ndash;245</td><td>8&ndash;9</td></tr>
      <tr><td>Broil</td><td>500+</td><td>260+</td><td>Broil</td></tr>
    </table>
  </div>

  <div class="ref-section">
    <div class="ref-heading">Common Pantry Weights</div>
    <table class="ref-table">
      <tr><th>Ingredient</th><th>1 Cup</th><th>Ingredient</th><th>1 Cup</th></tr>
      <tr><td>All-purpose flour</td><td>120 g / 4.2 oz</td><td>Granulated sugar</td><td>200 g / 7 oz</td></tr>
      <tr><td>Brown sugar (packed)</td><td>220 g / 7.75 oz</td><td>Powdered sugar</td><td>120 g / 4.2 oz</td></tr>
      <tr><td>Butter</td><td>227 g / 8 oz</td><td>Rolled oats</td><td>80 g / 2.8 oz</td></tr>
      <tr><td>Rice (uncooked)</td><td>185 g / 6.5 oz</td><td>Cocoa powder</td><td>85 g / 3 oz</td></tr>
    </table>
  </div>
</div>""" % (pg, pg)


def substitutions_page():
    pg = pn()
    return """<!-- PAGE %d: Common Substitutions -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Common Substitutions</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="ref-section">
    <div class="ref-heading">Emergency Substitutions</div>
    <table class="ref-table">
      <tr><th>You Need</th><th>Substitute With</th></tr>
      <tr><td>1 cup buttermilk</td><td>1 cup milk + 1 tbsp lemon juice (rest 5 min)</td></tr>
      <tr><td>1 egg</td><td>1 tbsp ground flax + 3 tbsp water, or 1/4 cup applesauce</td></tr>
      <tr><td>1 cup sour cream</td><td>1 cup plain yogurt (Greek works well)</td></tr>
      <tr><td>1 tbsp cornstarch</td><td>2 tbsp all-purpose flour</td></tr>
      <tr><td>1 cup brown sugar</td><td>1 cup white sugar + 1 tbsp molasses</td></tr>
      <tr><td>1 oz unsweetened chocolate</td><td>3 tbsp cocoa + 1 tbsp butter or oil</td></tr>
      <tr><td>1 cup heavy cream</td><td>3/4 cup milk + 1/3 cup butter (for cooking)</td></tr>
      <tr><td>1 tsp baking powder</td><td>1/4 tsp baking soda + 1/2 tsp cream of tartar</td></tr>
      <tr><td>1 cup honey</td><td>1-1/4 cups sugar + 1/4 cup water</td></tr>
      <tr><td>1 cup mayonnaise</td><td>1 cup sour cream or Greek yogurt</td></tr>
    </table>
  </div>

  <div class="ref-section">
    <div class="ref-heading">Cooking Abbreviations</div>
    <table class="ref-table">
      <tr><th>Abbrev</th><th>Meaning</th><th>Abbrev</th><th>Meaning</th></tr>
      <tr><td>tsp</td><td>teaspoon</td><td>lb</td><td>pound</td></tr>
      <tr><td>tbsp</td><td>tablespoon</td><td>oz</td><td>ounce</td></tr>
      <tr><td>c</td><td>cup</td><td>fl oz</td><td>fluid ounce</td></tr>
      <tr><td>pt</td><td>pint</td><td>qt</td><td>quart</td></tr>
      <tr><td>gal</td><td>gallon</td><td>g</td><td>gram</td></tr>
      <tr><td>kg</td><td>kilogram</td><td>ml</td><td>milliliter</td></tr>
    </table>
  </div>

  <div class="ref-section">
    <div class="ref-heading">Food Storage Guidelines</div>
    <table class="ref-table">
      <tr><th>Food</th><th>Refrigerator</th><th>Freezer</th></tr>
      <tr><td>Raw chicken</td><td>1&ndash;2 days</td><td>9 months</td></tr>
      <tr><td>Raw beef/pork</td><td>3&ndash;5 days</td><td>4&ndash;12 months</td></tr>
      <tr><td>Cooked meat</td><td>3&ndash;4 days</td><td>2&ndash;3 months</td></tr>
      <tr><td>Soups &amp; stews</td><td>3&ndash;4 days</td><td>2&ndash;3 months</td></tr>
      <tr><td>Eggs (in shell)</td><td>3&ndash;5 weeks</td><td>Do not freeze</td></tr>
    </table>
  </div>
</div>""" % (pg, pg)


def recipe_index_page(letter_start, letter_end):
    """Recipe index: one page with A-Z slots."""
    pg = pn()
    letters = [chr(c) for c in range(ord(letter_start), ord(letter_end) + 1)]
    rows_html = ""
    for letter in letters:
        # 2 entry slots per letter
        for _ in range(2):
            rows_html += """<tr>
  <td class="idx-letter">%s</td>
  <td class="idx-name"></td>
  <td class="idx-page"></td>
</tr>
""" % letter

    return """<!-- PAGE %d: Recipe Index -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Recipe Index</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="index-table">
    <tr>
      <th style="width:20px;"></th>
      <th>Recipe Name</th>
      <th style="text-align:right; width:35px;">Page</th>
    </tr>
    %s
  </table>
</div>""" % (pg, pg, rows_html)


def recipe_left_page():
    """Left page of recipe spread: name, meta, ingredients."""
    pg = pn()
    ingredient_lines = "\n".join(
        '<div class="ingredient-line"><div class="ingredient-check"></div>'
        '<div class="ingredient-write"></div></div>'
        for _ in range(16)
    )
    return """<!-- PAGE %d: Recipe Left -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Recipe</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="recipe-name-area">
    <div class="rn-label">Recipe Name</div>
    <div class="rn-line"></div>
  </div>

  <div class="recipe-meta">
    <div class="meta-box">
      <span class="mb-label">From / Source</span>
      <div class="mb-write"></div>
    </div>
    <div class="meta-box">
      <span class="mb-label">Category</span>
      <div class="mb-write"></div>
    </div>
    <div class="meta-box">
      <span class="mb-label">Serves</span>
      <div class="mb-write"></div>
    </div>
  </div>

  <div class="recipe-meta2">
    <div class="meta-box">
      <span class="mb-label">Prep Time</span>
      <div class="mb-write"></div>
    </div>
    <div class="meta-box">
      <span class="mb-label">Cook Time</span>
      <div class="mb-write"></div>
    </div>
  </div>

  <div class="rating-row">
    <span class="rating-label">Rating</span>
    <div class="rating-stars">
      <div class="star"></div><div class="star"></div><div class="star"></div>
      <div class="star"></div><div class="star"></div>
    </div>
    <div class="difficulty-row">
      <span class="rating-label">Difficulty</span>
      <span class="diff-circle"></span><span class="diff-label">Easy</span>
      <span class="diff-circle"></span><span class="diff-label">Med</span>
      <span class="diff-circle"></span><span class="diff-label">Hard</span>
    </div>
  </div>

  <div class="ingredients-header">
    <span class="ih-text">Ingredients</span>
    <div class="ih-line"></div>
  </div>

  %s
</div>""" % (pg, pg, ingredient_lines)


def recipe_right_page():
    """Right page of recipe spread: directions + notes."""
    pg = pn()
    step_lines = "\n".join(
        '<div class="step-line"><div class="step-num">%d</div>'
        '<div class="step-write"></div></div>'
        % (i + 1)
        for i in range(15)
    )
    note_lines = "\n".join(
        '<div class="na-line"></div>' for _ in range(3)
    )
    return """<!-- PAGE %d: Recipe Right -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Directions</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="directions-header">
    <span class="dh-text">Directions</span>
    <div class="dh-line"></div>
  </div>

  %s

  <div class="notes-area">
    <div class="na-label">Notes, Tips &amp; Variations</div>
    %s
  </div>

  <div class="date-made">
    <span class="dm-label">Date Made</span>
    <div class="dm-line"></div>
  </div>
</div>""" % (pg, pg, step_lines, note_lines)


def notes_page():
    pg = pn()
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes &amp; More Recipes</span>
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
      good family,<br>
      good memories.
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

    # 3. Measurement equivalents
    pages.append(measurement_equivalents_page())

    # 4. Substitutions & abbreviations
    pages.append(substitutions_page())

    # 5-9. Recipe index (5 pages, A-Z, 2 slots per letter)
    # A-E, F-J, K-O, P-T, U-Z
    index_ranges = [("A", "E"), ("F", "J"), ("K", "O"), ("P", "T"), ("U", "Z")]
    for ls, le in index_ranges:
        pages.append(recipe_index_page(ls, le))

    # 10-109. 50 recipe spreads (each = 2 pages: left + right)
    NUM_RECIPES = 50
    for _ in range(NUM_RECIPES):
        pages.append(recipe_left_page())
        pages.append(recipe_right_page())

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
