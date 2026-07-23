#!/usr/bin/env python3
"""
Dog Training & Puppy Journal — KDP Interior Generator
Trim: 6 x 9 in | Language: English
Target: New puppy owners, dog training enthusiasts
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "dog_training_journal_us_V1.0.html")

BOOK_TITLE = "Dog Training & Puppy Journal"
BOOK_SUBTITLE = "Your Companion from First Day to Best Friend"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

def nl(n):
    return "\n".join('<div class="notes-line"></div>' for _ in range(n))

def rc(n):
    """Rating circles 1-n."""
    return " ".join('<span class="rating-circle">%d</span>' % i for i in range(1, n + 1))

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
@media print { .page { border: none; margin: 0; } }

/* TITLE PAGE */
.cover {
  width: 6in; height: 9in; padding: 0;
  page-break-after: always;
  position: relative; overflow: hidden;
  background: linear-gradient(165deg, #161616 0%, #1E1E1E 30%, #161616 65%, #0D0D0D 100%);
  display: flex; flex-direction: column;
  justify-content: center; align-items: center; text-align: center;
}
.cover .glow-bg {
  position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.05;
  background-image:
    radial-gradient(ellipse 30px 18px at 15% 20%, #C4A04A, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #7A8B6F, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #C4A04A, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #7A8B6F, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #C4A04A, transparent);
}
.cover .title-main { font-size: 26pt; font-weight: 700; color: #FAF6F0; line-height: 1.2; letter-spacing: 0.5pt; position: relative; z-index: 2; text-shadow: 2px 2px 8px rgba(0,0,0,0.5); }
.cover .accent-bar { width: 100px; height: 2px; background: #C4A04A; margin: 20px auto; position: relative; z-index: 2; }
.cover .subtitle { font-size: 12pt; color: #D4B896; font-style: italic; line-height: 1.5; position: relative; z-index: 2; }
.cover .pub { position: absolute; bottom: 0.6in; left: 0; right: 0; text-align: center; font-size: 9pt; color: #C4A04A; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; }

/* PAGE HEADER */
.page-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; padding-bottom: 4px; border-bottom: 0.5px solid #eee; }
.page-header .ph-left { font-size: 8pt; color: #7A8B6F; text-transform: uppercase; letter-spacing: 1pt; font-weight: 700; }
.page-header .ph-right { font-size: 8pt; color: #999; }

/* SECTION */
.section-header { display: flex; align-items: center; justify-content: center; margin-bottom: 14px; }
.section-title { font-size: 14pt; font-weight: 700; color: #161616; letter-spacing: 0.5pt; text-transform: uppercase; }
.section-line { flex: 1; height: 1px; background: #7A8B6F; margin: 0 12px; opacity: 0.4; }

/* INFO FIELDS */
.info-row { display: grid; grid-template-columns: 1fr 1fr; gap: 6px 12px; margin-bottom: 8px; }
.info-field .if-label { font-size: 6.5pt; color: #7A8B6F; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; display: block; margin-bottom: 1px; }
.info-field .if-write { height: 16px; border-bottom: 1px dotted #ccc; }

/* WRITE BOX */
.write-box { border: 1px solid #C4A04A; border-radius: 3px; padding: 6px 8px; margin-bottom: 8px; }
.write-box .wb-label { font-size: 7pt; color: #7A8B6F; text-transform: uppercase; letter-spacing: 0.5pt; font-weight: 700; margin-bottom: 3px; }
.write-box .wb-area { height: 28px; }

/* CHECKBOX LISTS */
.check-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2px 12px; margin-bottom: 8px; }
.check-item { display: flex; align-items: center; gap: 4px; height: 18px; }
.check-box { width: 9px; height: 9px; border: 1px solid #7A8B6F; border-radius: 2px; flex-shrink: 0; }
.check-item span { font-size: 8pt; color: #2A2A2A; }

/* RATING CIRCLES */
.rating-row { display: flex; align-items: center; gap: 4px; margin-bottom: 5px; }
.rating-row .rr-label { font-size: 8pt; width: 110px; flex-shrink: 0; }
.rating-circle { width: 12px; height: 12px; border: 1.5px solid #7A8B6F; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 5pt; color: #7A8B6F; margin-right: 1px; }

/* HABIT TABLE */
.habit-table { width: 100%; border-collapse: collapse; margin-top: 4px; }
.habit-table th { font-size: 6.5pt; color: #7A8B6F; text-transform: uppercase; letter-spacing: 0.5pt; padding: 4px 3px; border-bottom: 1.5px solid #7A8B6F; text-align: center; }
.habit-table th:first-child { text-align: left; width: 100px; }
.habit-table td { padding: 4px 3px; border-bottom: 1px solid #eee; text-align: center; height: 18px; }
.habit-table td:first-child { text-align: left; font-size: 8pt; }
.habit-check { width: 11px; height: 11px; border: 1px solid #7A8B6F; border-radius: 50%; display: inline-block; }

/* HOW-TO */
.howto-text { font-size: 10pt; line-height: 1.7; }
.howto-text p { margin-bottom: 8px; }
.howto-text .ht-title { font-size: 11pt; font-weight: 700; color: #161616; margin-bottom: 4px; margin-top: 6px; }
.howto-text .ht-icon { color: #7A8B6F; font-weight: 700; margin-right: 4px; }

/* COMMANDS TABLE */
.cmd-table { width: 100%; border-collapse: collapse; margin-bottom: 8px; }
.cmd-table th { font-size: 6.5pt; color: #7A8B6F; text-transform: uppercase; padding: 4px 3px; border-bottom: 1.5px solid #7A8B6F; text-align: left; }
.cmd-table th:first-child { width: 90px; }
.cmd-table td { padding: 4px 3px; border-bottom: 1px solid #eee; height: 22px; font-size: 8.5pt; }
.cmd-table td:first-child { font-weight: 700; color: #161616; }

/* NOTES */
.notes-line { border-bottom: 1px solid #ddd; height: 22px; }

/* FINAL */
.final-page { display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; height: 100%; }
.final-page .fp-text { font-size: 12pt; color: #999; font-style: italic; line-height: 1.8; margin-bottom: 20px; }
.final-page .fp-logo { font-size: 11pt; color: #C4A04A; letter-spacing: 2.5pt; text-transform: uppercase; font-weight: 700; }
.final-page .fp-line { width: 60px; height: 1.5px; background: #7A8B6F; margin: 12px auto; opacity: 0.5; }

/* DAY BANNER */
.day-banner { display: flex; align-items: center; gap: 8px; border-bottom: 1.5px solid #7A8B6F; padding-bottom: 5px; margin-bottom: 10px; }
.day-banner .db-num { display: inline-block; border: 1.5px solid #7A8B6F; border-radius: 4px; padding: 3px 10px; font-size: 8pt; color: #7A8B6F; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5pt; }
.day-banner .db-label { font-size: 8pt; color: #999; text-transform: uppercase; letter-spacing: 0.5pt; }
.day-banner .db-line { flex: 1; height: 12px; border-bottom: 1px dotted #ccc; }
"""

def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <!-- Dog paw print -->
      <!-- Main pad -->
      <path d="M 30 55 Q 30 42 38 40 Q 50 36 62 40 Q 70 42 70 55 Q 70 72 50 72 Q 30 72 30 55 Z"
            stroke="#C4A04A" stroke-width="1.5" fill="none"/>
      <!-- Toe pads -->
      <ellipse cx="25" cy="32" rx="7" ry="10" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.7"/>
      <ellipse cx="40" cy="22" rx="7" ry="10" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.7"/>
      <ellipse cx="60" cy="22" rx="7" ry="10" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.7"/>
      <ellipse cx="75" cy="32" rx="7" ry="10" stroke="#C4A04A" stroke-width="1.2" fill="none" opacity="0.7"/>
    </svg>
  </div>

  <div class="title-main">Dog Training<br>&amp; Puppy Journal</div>
  <div class="accent-bar"></div>
  <div class="subtitle">Your Companion from First Day to Best Friend</div>

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
    <div class="ht-title"><span class="ht-icon">&#9758;</span> Welcome to Your Puppy Journey</div>
    <p>Bringing a new dog home is one of life's great joys. This journal helps
    you track training progress, milestones, health, and all the little moments
    that make the journey memorable.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> Training Philosophy</div>
    <p>Dogs learn through <strong>consistency, patience, and positive reinforcement</strong>.
    Keep training sessions short (5-10 minutes), reward good behavior immediately,
    and never punish a dog for not understanding. Every dog learns at their own pace.</p>

    <div class="ht-title"><span class="ht-icon">&#9758;</span> How to Use This Journal</div>
    <p>&#9679; Use the <strong>dog profile</strong> page to record your dog's details.</p>
    <p>&#9679; Log <strong>weekly training sessions</strong> with commands, progress, and notes.</p>
    <p>&#9679; Track <strong>milestones</strong> like first walk, first vet visit, house training.</p>
    <p>&#9679; Keep a <strong>health record</strong> for vaccinations, weight, and vet visits.</p>
    <p>&#9679; Use the <strong>command tracker</strong> to see which skills your dog has mastered.</p>
  </div>
</div>""" % (pg, pg)


def dog_profile_page():
    pg = pn()
    return """<!-- PAGE %d: Dog Profile -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">My Dog's Profile</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">All About My Dog</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Dog's Name</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Breed</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Date of Birth</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Date Adopted</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Sex / Spayed/Neutered</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Color / Markings</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Weight (at adoption)</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Microchip ID</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Veterinarian</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Insurance</span><div class="if-write"></div></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Personality &amp; Temperament</div>
    <div class="wb-area" style="height: 36px;"></div>
  </div>

  <div class="write-box" style="border-color: #7A8B6F;">
    <div class="wb-label">Likes &amp; Dislikes</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>
</div>""" % (pg, pg)


def milestones_page():
    pg = pn()
    milestones = [
        "Brought home", "First night", "First vet visit", "First vaccination",
        "First bath", "First walk outside", "Met another dog", "Met a child",
        "House training started", "House training complete", "First grooming",
        "Learned name", "Learned sit", "Learned stay", "Learned come",
        "Learned down", "Learned leave it", "Learned heel", "Crate trained",
        "First trip / travel", "Spayed/Neutered", "Off-leash trained",
        "Agility / sport started", "Canine Good Citizen", "Birthday #1",
    ]
    items_html = "\n".join(
        '<div class="check-item"><div class="check-box"></div><span>%s</span><div style="flex:1; height:10px; border-bottom: 1px dotted #ccc; margin-left: 6px;"></div></div>'
        % H.escape(m)
        for m in milestones
    )
    return """<!-- PAGE %d: Milestones -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Puppy Milestones</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Check Off Each Milestone</div>
    <div class="section-line"></div>
  </div>

  <div class="check-grid">%s</div>
</div>""" % (pg, pg, items_html)


def command_tracker_page():
    pg = pn()
    commands = [
        ("Sit", "Foundational"),
        ("Down", "Foundational"),
        ("Stay", "Foundational"),
        ("Come (Recall)", "Critical"),
        ("Heel / Loose Leash", "Foundational"),
        ("Leave It", "Safety"),
        ("Drop It", "Safety"),
        ("Wait", "Impulse control"),
        ("Place / Settle", "Calm"),
        ("Off", "Manners"),
        ("Quiet", "Manners"),
        ("Watch Me / Focus", "Attention"),
        ("Roll Over", "Fun trick"),
        ("Shake / Paw", "Fun trick"),
        ("Spin / Turn", "Fun trick"),
        ("Fetch", "Fun / exercise"),
        ("Speak / Bark", "Fun trick"),
        ("Crawl", "Advanced"),
    ]
    rows = ""
    for cmd, category in commands:
        rows += '<tr><td>%s</td><td>%s</td><td></td><td></td><td></td></tr>\n' % (
            H.escape(cmd), H.escape(category)
        )
    return """<!-- PAGE %d: Command Tracker -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Command Progress Tracker</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Training Progress</div>
    <div class="section-line"></div>
  </div>

  <table class="cmd-table">
    <thead>
      <tr>
        <th>Command</th>
        <th>Category</th>
        <th>Date Started</th>
        <th>Date Mastered</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      %s
    </tbody>
  </table>

  <div class="howto-text" style="font-size: 8.5pt; margin-top: 6px;">
    <p><strong>Stages of learning:</strong> Introduced &#8594; Practicing &#8594;
    Reliable &#8594; Mastered (works with distractions).</p>
  </div>
</div>""" % (pg, pg, rows)


def health_log_page():
    pg = pn()
    return """<!-- PAGE %d: Health Record -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Health &amp; Vaccination Record</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Vaccinations</div>
    <div class="section-line"></div>
  </div>

  <table class="cmd-table">
    <thead>
      <tr>
        <th>Vaccine / Treatment</th>
        <th>Date</th>
        <th>Next Due</th>
        <th>Vet / Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Distemper/Parvo (1st)</td><td></td><td></td><td></td></tr>
      <tr><td>Distemper/Parvo (2nd)</td><td></td><td></td><td></td></tr>
      <tr><td>Distemper/Parvo (3rd)</td><td></td><td></td><td></td></tr>
      <tr><td>Rabies</td><td></td><td></td><td></td></tr>
      <tr><td>Bordetella</td><td></td><td></td><td></td></tr>
      <tr><td>Leptospirosis</td><td></td><td></td><td></td></tr>
      <tr><td>Lyme</td><td></td><td></td><td></td></tr>
      <tr><td>Heartworm Test</td><td></td><td></td><td></td></tr>
      <tr><td>Flea/Tick Prevention</td><td></td><td></td><td></td></tr>
      <tr><td>Spay / Neuter</td><td></td><td></td><td></td></tr>
    </tbody>
  </table>
</div>""" % (pg, pg)


def weight_tracker_page():
    pg = pn()
    rows = ""
    for i in range(1, 13):
        rows += '<tr><td>Month %d</td><td></td><td></td></tr>\n' % i
    return """<!-- PAGE %d: Weight Tracker -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Weight Tracker</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Monthly Weight Log</div>
    <div class="section-line"></div>
  </div>

  <table class="cmd-table">
    <thead>
      <tr><th>Month</th><th>Date</th><th>Weight (lbs)</th></tr>
    </thead>
    <tbody>%s</tbody>
  </table>

  <div class="write-box" style="margin-top: 10px;">
    <div class="wb-label">Diet / Food Brand</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Feeding Schedule</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg, rows)


def training_session_page(week_num):
    pg = pn()
    skills = ["Sit", "Down", "Stay", "Come", "Heel", "Leave It", "Loose Leash", "Place", "Crate", "Socialization"]
    skill_checks = " ".join(
        '<span style="font-size: 7pt; color: #555; margin-right: 4px;"><span class="check-box" style="display:inline-block; width:8px; height:8px; border:1px solid #7A8B6F; border-radius:2px;"></span> %s</span>'
        % s for s in skills
    )
    return """<!-- PAGE %d: Training Week %d -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Training Journal</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="day-banner">
    <span class="db-num">Week %d</span>
    <span class="db-label">Date:</span>
    <div class="db-line"></div>
  </div>

  <div style="font-size: 7pt; font-weight: 700; color: #7A8B6F; text-transform: uppercase; letter-spacing: 0.5pt; margin-bottom: 4px;">
    Skills Practiced
  </div>
  <div style="margin-bottom: 8px;">%s</div>

  <table class="habit-table">
    <thead>
      <tr>
        <th>Activity</th>
        <th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th><th>Sun</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Training session</td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td></tr>
      <tr><td>Walk / exercise</td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td></tr>
      <tr><td>Socialization</td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td></tr>
      <tr><td>Crate time</td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td><td><span class="habit-check"></span></td></tr>
    </tbody>
  </table>

  <div class="rating-row" style="margin-top: 8px;">
    <span class="rr-label">Focus / Attention</span>
    %s
  </div>
  <div class="rating-row">
    <span class="rr-label">Energy Level</span>
    %s
  </div>
  <div class="rating-row">
    <span class="rr-label">Overall Progress</span>
    %s
  </div>

  <div class="write-box">
    <div class="wb-label">What Went Well This Week</div>
    <div class="wb-area"></div>
  </div>

  <div class="write-box" style="border-color: #7A8B6F;">
    <div class="wb-label">Challenges / To Work On</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, week_num, pg, week_num, skill_checks, rc(5), rc(5), rc(5))


def notes_page():
    pg = pn()
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes &amp; Memories</span>
    <span class="ph-right">Page %d</span>
  </div>
  <div>%s</div>
</div>""" % (pg, pg, nl(28))


def final_page():
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="page">
  <div class="final-page">
    <div class="fp-text">
      A dog is the only thing on earth<br>
      that loves you more than<br>
      he loves himself.
    </div>
    <div class="fp-line"></div>
    <div class="fp-logo">More Shine Press</div>
    <div class="fp-line"></div>
  </div>
</div>""" % pg


def generate(output_path=HTML_FILE):
    pages = []
    pages.append(interior_title_page())
    pages.append(how_to_use_page())
    pages.append(dog_profile_page())
    pages.append(milestones_page())
    pages.append(command_tracker_page())
    pages.append(health_log_page())
    pages.append(weight_tracker_page())

    # 16 weekly training sessions
    for week in range(1, 17):
        pages.append(training_session_page(week))

    for _ in range(3):
        pages.append(notes_page())
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
