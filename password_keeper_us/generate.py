#!/usr/bin/env python3
"""
Password Keeper -- KDP Interior Generator
Trim: 8 x 10 in | Language: English
Publisher: More Shine Press
Zero-dependency: Python stdlib only.
"""

import html as H
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(OUTPUT_DIR, "password_keeper_us_V1.0.html")

BOOK_TITLE = "Password Keeper"
BOOK_SUBTITLE = "A Secure Logbook for All Your Online Accounts"

page_no = [0]

def pn():
    page_no[0] += 1
    return page_no[0]

def nl(n):
    return "\n".join('<div class="notes-line"></div>' for _ in range(n))

CSS = r"""
@page { size: 8in 10in; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: Georgia, "Iowan Old Style", "Palatino", serif;
  color: #2A2A2A;
  background: white;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

.page {
  width: 8in; height: 10in;
  padding: 0.6in 0.6in 0.5in 0.6in;
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
  width: 8in; height: 10in;
  padding: 0;
  page-break-after: always;
  position: relative;
  overflow: hidden;
  background: linear-gradient(165deg, #0F0E0C 0%, #1A1612 30%, #0F0E0C 65%, #080706 100%);
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
    radial-gradient(ellipse 30px 18px at 15% 20%, #B8860B, transparent),
    radial-gradient(ellipse 26px 16px at 80% 15%, #C4A04A, transparent),
    radial-gradient(ellipse 28px 17px at 70% 70%, #B8860B, transparent),
    radial-gradient(ellipse 22px 14px at 25% 80%, #C4A04A, transparent),
    radial-gradient(ellipse 20px 12px at 50% 45%, #B8860B, transparent);
}

.cover .title-main {
  font-size: 36pt;
  font-weight: 700;
  color: #FAF6F0;
  line-height: 1.2;
  letter-spacing: 0.5pt;
  position: relative;
  z-index: 2;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
}

.cover .accent-bar {
  width: 100px; height: 2px;
  background: #B8860B;
  margin: 20px auto;
  position: relative;
  z-index: 2;
}

.cover .subtitle {
  font-size: 13pt;
  color: #D4B896;
  font-style: italic;
  line-height: 1.5;
  position: relative;
  z-index: 2;
}

.cover .pub {
  position: absolute;
  bottom: 0.7in;
  left: 0; right: 0;
  text-align: center;
  font-size: 9pt;
  color: #C4A04A;
  letter-spacing: 2.5pt;
  text-transform: uppercase;
  font-weight: 700;
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
  color: #B8860B;
  text-transform: uppercase;
  letter-spacing: 1pt;
  font-weight: 700;
}

.page-header .ph-right {
  font-size: 8pt;
  color: #999;
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
  background: #B8860B;
  margin: 0 12px;
  opacity: 0.4;
}

/* ================ HOW TO USE ================ */
.howto-text { font-size: 10pt; line-height: 1.7; }
.howto-text p { margin-bottom: 8px; }
.howto-text .ht-title {
  font-size: 11pt; font-weight: 700; color: #161616;
  margin-bottom: 4px; margin-top: 6px;
}
.howto-text .ht-icon { color: #B8860B; font-weight: 700; margin-right: 4px; }

/* ================ WRITE BOX ================ */
.write-box {
  border: 1px solid #C4A04A;
  border-radius: 3px;
  padding: 6px 8px;
  margin-bottom: 8px;
}

.write-box .wb-label {
  font-size: 7pt;
  color: #B8860B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  margin-bottom: 3px;
}

.write-box .wb-area {
  height: 28px;
}

/* ================ ENTRY TABLE ================ */
.entry-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
}

.entry-table th {
  font-size: 7pt;
  color: #B8860B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  padding: 6px 4px;
  border-bottom: 1.5px solid #B8860B;
  text-align: left;
}

.entry-table td {
  padding: 6px 4px;
  border-bottom: 1px solid #eee;
  height: 30px;
  font-size: 9pt;
  vertical-align: middle;
}

.entry-table td:first-child {
  width: 0.3in;
  text-align: center;
  font-size: 7pt;
  color: #B8860B;
  font-weight: 700;
}

/* ================ TAB PAGE ================ */
.tab-page {
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  text-align: center; height: 100%;
}
.tab-page .tp-letter {
  font-size: 120pt; color: #B8860B; font-weight: 700;
  opacity: 0.15; line-height: 1;
}
.tab-page .tp-title {
  font-size: 16pt; color: #161616; font-weight: 700;
  letter-spacing: 1pt; text-transform: uppercase;
  margin-top: 10px;
}
.tab-page .tp-line {
  width: 80px; height: 2px; background: #B8860B;
  margin: 16px auto; opacity: 0.5;
}

/* ================ INFO FIELDS ================ */
.info-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 12px;
  margin-bottom: 8px;
}

.info-field .if-label {
  font-size: 6.5pt;
  color: #B8860B;
  text-transform: uppercase;
  letter-spacing: 0.5pt;
  font-weight: 700;
  display: block;
  margin-bottom: 1px;
}

.info-field .if-write {
  height: 16px;
  border-bottom: 1px dotted #ccc;
}

/* ================ CHECKLIST ================ */
.check-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4px 12px;
  margin-bottom: 8px;
}

.check-item {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 8pt;
  color: #555;
}

.check-box {
  width: 10px; height: 10px;
  border: 1.5px solid #B8860B;
  border-radius: 2px;
  flex-shrink: 0;
}

/* ================ NOTES ================ */
.notes-line { border-bottom: 1px solid #ddd; height: 22px; }

/* ================ FINAL PAGE ================ */
.final-page {
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  text-align: center; height: 100%;
}
.final-page .fp-text {
  font-size: 12pt; color: #999; font-style: italic;
  line-height: 1.8; margin-bottom: 20px;
}
.final-page .fp-logo {
  font-size: 11pt; color: #C4A04A;
  letter-spacing: 2.5pt; text-transform: uppercase;
  font-weight: 700;
}
.final-page .fp-line {
  width: 60px; height: 1.5px; background: #B8860B;
  margin: 12px auto; opacity: 0.5;
}
"""


def interior_title_page():
    return """<!-- PAGE %d: Interior Title -->
<div class="cover">
  <div class="glow-bg"></div>

  <div style="position: relative; z-index: 2; margin-bottom: 20px;">
    <svg viewBox="0 0 100 100" width="110" height="110" xmlns="http://www.w3.org/2000/svg">
      <!-- Padlock icon -->
      <g transform="translate(50,50)">
        <!-- Shackle -->
        <path d="M -14,-2 L -14,-14 C -14,-24 -6,-28 0,-28 C 6,-28 14,-24 14,-14 L 14,-2"
              stroke="#B8860B" stroke-width="2.5" fill="none"/>
        <!-- Body -->
        <rect x="-20" y="-2" width="40" height="30" rx="3" stroke="#B8860B" stroke-width="2.5" fill="none"/>
        <!-- Keyhole -->
        <circle cx="0" cy="10" r="3" fill="#C4A04A"/>
        <rect x="-1.5" y="10" width="3" height="8" fill="#C4A04A"/>
        <!-- Highlights -->
        <path d="M -16,-18 C -16,-24 -10,-26 -6,-26" stroke="#C4A04A" stroke-width="1" fill="none"/>
        <rect x="-17" y="1" width="3" height="10" rx="1" fill="none" stroke="#D4B896" stroke-width="0.8"/>
      </g>
    </svg>
  </div>

  <div class="title-main">Password<br>Keeper</div>
  <div class="accent-bar"></div>
  <div class="subtitle">A Secure Logbook for<br>All Your Online Accounts</div>

  <div class="pub">More Shine Press</div>
</div>""" % pn()


def how_to_use_page():
    pg = pn()
    return """<!-- PAGE %d: How to Use -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">How to Use This Book</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="howto-text">
    <div class="ht-title"><span class="ht-icon">&#10058;</span> Your Personal Password Vault</div>
    <p>This password keeper helps you organize every online account
    in one secure, offline location. No more forgotten passwords,
    no more risky password reuse -- just one reliable reference
    you can turn to anytime.</p>

    <div class="ht-title"><span class="ht-icon">&#10058;</span> A-Z Tabbed Organization</div>
    <p>Accounts are organized <strong>alphabetically from A to Z</strong>.
    Each letter has its own tab page followed by entry pages with
    spacious tables. Record the website name, username, password,
    email used, security questions, and notes for each account.</p>

    <div class="ht-title"><span class="ht-icon">&#10058;</span> Security Best Practices</div>
    <p>&#9679; Use a <strong>different password</strong> for every account.</p>
    <p>&#9679; Make passwords at least <strong>12 characters</strong> long
    with a mix of letters, numbers, and symbols.</p>
    <p>&#9679; Consider using a <strong>passphrase</strong> -- a sequence
    of random words is both strong and memorable.</p>
    <p>&#9679; Enable <strong>two-factor authentication</strong> whenever
    possible.</p>
    <p>&#9679; Update passwords <strong>every 6-12 months</strong>.</p>
    <p>&#9679; Store this book in a <strong>safe or locked drawer</strong> --
    treat it like the valuable document it is.</p>

    <div class="ht-title"><span class="ht-icon">&#10058;</span> What to Record</div>
    <p>For each account, note the <strong>website</strong>,
    <strong>username or email</strong>, <strong>password</strong>,
    <strong>recovery email</strong>, and any <strong>security
    questions</strong> with their answers. The notes column is for
    PINs, backup codes, subscription dates, or renewal reminders.</p>
  </div>
</div>""" % (pg, pg)


def security_info_page():
    pg = pn()
    return """<!-- PAGE %d: My Security Info -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">My Security Information</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Important Details</div>
    <div class="section-line"></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Owner Name</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Primary Email</span><div class="if-write"></div></div>
  </div>

  <div class="info-row">
    <div class="info-field"><span class="if-label">Recovery Email</span><div class="if-write"></div></div>
    <div class="info-field"><span class="if-label">Primary Phone</span><div class="if-write"></div></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Wi-Fi Network Name &amp; Password</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Home Alarm Code</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Router Admin Password</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Computer / Device Login</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">Email Account Recovery Codes</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Other Important PINs / Codes</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box">
    <div class="wb-label">In Case of Emergency (Trusted Contact)</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def tab_page(letter):
    pg = pn()
    return """<!-- PAGE %d: Tab %s -->
<div class="page">
  <div class="tab-page">
    <div class="tp-letter">%s</div>
    <div class="tp-title">%s</div>
    <div class="tp-line"></div>
  </div>
</div>""" % (pg, letter, letter, letter)


def entry_page(letter, entries=9):
    pg = pn()
    rows = "\n".join(
        '<tr><td>%s%d</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>'
        % (letter, i + 1)
        for i in range(entries)
    )
    return """<!-- PAGE %d: Entries %s -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">%s</span>
    <span class="ph-right">Page %d</span>
  </div>

  <table class="entry-table">
    <thead>
      <tr>
        <th>#</th>
        <th>Website / App</th>
        <th>Username</th>
        <th>Password</th>
        <th>Email Used</th>
        <th>Security Q &amp; A</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
%s
    </tbody>
  </table>
</div>""" % (pg, letter, letter, pg, rows)


def pin_reference_page():
    pg = pn()
    return """<!-- PAGE %d: PIN Reference -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">PIN &amp; Code Reference</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Quick Access</div>
    <div class="section-line"></div>
  </div>

  <table class="entry-table">
    <thead>
      <tr>
        <th>#</th>
        <th>Device / Service</th>
        <th>PIN / Code</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
%s
    </tbody>
  </table>
</div>""" % (pg, pg, "\n".join(
        '<tr><td>%d</td><td></td><td></td><td></td></tr>' % (i + 1)
        for i in range(18)
    ))


def subscription_page():
    pg = pn()
    return """<!-- PAGE %d: Subscriptions -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Subscriptions &amp; Bills</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Recurring Accounts</div>
    <div class="section-line"></div>
  </div>

  <table class="entry-table">
    <thead>
      <tr>
        <th>#</th>
        <th>Service</th>
        <th>Login</th>
        <th>Cost</th>
        <th>Billing Cycle</th>
        <th>Renewal Date</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
%s
    </tbody>
  </table>
</div>""" % (pg, pg, "\n".join(
        '<tr><td>%d</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>' % (i + 1)
        for i in range(14)
    ))


def security_checklist_page():
    pg = pn()
    return """<!-- PAGE %d: Security Checklist -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Security Audit Checklist</span>
    <span class="ph-right">Page %d</span>
  </div>

  <div class="section-header">
    <div class="section-line"></div>
    <div class="section-title">Best Practices</div>
    <div class="section-line"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Password Habits</div>
    <div class="check-grid">
      <span class="check-item"><span class="check-box"></span>No reused passwords</span>
      <span class="check-item"><span class="check-box"></span>12+ character passwords</span>
      <span class="check-item"><span class="check-box"></span>Mix of letters, numbers, symbols</span>
      <span class="check-item"><span class="check-box"></span>Passphrases for key accounts</span>
      <span class="check-item"><span class="check-box"></span>Last updated within 12 months</span>
      <span class="check-item"><span class="check-box"></span>No passwords written on sticky notes</span>
    </div>
  </div>

  <div class="write-box">
    <div class="wb-label">Account Security</div>
    <div class="check-grid">
      <span class="check-item"><span class="check-box"></span>2FA enabled on email</span>
      <span class="check-item"><span class="check-box"></span>2FA on banking</span>
      <span class="check-item"><span class="check-box"></span>2FA on social media</span>
      <span class="check-item"><span class="check-box"></span>Recovery email set on all accounts</span>
      <span class="check-item"><span class="check-box"></span>Recovery phone current</span>
      <span class="check-item"><span class="check-box"></span>Backup codes stored safely</span>
    </div>
  </div>

  <div class="write-box">
    <div class="wb-label">Device Security</div>
    <div class="check-grid">
      <span class="check-item"><span class="check-box"></span>Phone passcode set</span>
      <span class="check-item"><span class="check-box"></span>Computer password set</span>
      <span class="check-item"><span class="check-box"></span>Auto-lock enabled</span>
      <span class="check-item"><span class="check-box"></span>Disk encryption on</span>
      <span class="check-item"><span class="check-box"></span>Antivirus / firewall active</span>
      <span class="check-item"><span class="check-box"></span>Software updates current</span>
    </div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">This Book</div>
    <div class="check-grid">
      <span class="check-item"><span class="check-box"></span>Stored in a safe place</span>
      <span class="check-item"><span class="check-box"></span>Not shared with untrusted people</span>
      <span class="check-item"><span class="check-box"></span>Someone knows where to find it</span>
      <span class="check-item"><span class="check-box"></span>Updated regularly</span>
    </div>
  </div>

  <div class="write-box">
    <div class="wb-label">Last Audit Date &amp; Notes</div>
    <div class="wb-area" style="height: 28px;"></div>
  </div>

  <div class="write-box" style="border-color: #B8860B;">
    <div class="wb-label">Next Audit Due</div>
    <div class="wb-area"></div>
  </div>
</div>""" % (pg, pg)


def notes_page():
    pg = pn()
    return """<!-- PAGE %d: Notes -->
<div class="page">
  <div class="page-header">
    <span class="ph-left">Notes</span>
    <span class="ph-right">Page %d</span>
  </div>
  <div>%s</div>
</div>""" % (pg, pg, nl(34))


def final_page():
    pg = pn()
    return """<!-- PAGE %d: Final -->
<div class="page">
  <div class="final-page">
    <div class="fp-text">
      Security is not an accident.<br>
      It is a habit built one password at a time.<br>
      Stay safe. Stay organized.
    </div>
    <div class="fp-line"></div>
    <div class="fp-logo">More Shine Press</div>
    <div class="fp-line"></div>
  </div>
</div>""" % pg


def generate(output_path=HTML_FILE):
    pages = []
    # Front matter
    pages.append(interior_title_page())
    pages.append(how_to_use_page())
    pages.append(security_info_page())

    # A-Z entries
    # High-volume letters get 2 entry pages, others get 1
    import string
    two_pages = set("ABCEFGHIMPST")  # common starting letters
    for letter in string.ascii_uppercase:
        pages.append(tab_page(letter))
        if letter in two_pages:
            pages.append(entry_page(letter, 9))
            pages.append(entry_page(letter, 9))
        else:
            pages.append(entry_page(letter, 12))

    # PIN Reference (2 pages)
    for _ in range(2):
        pages.append(pin_reference_page())

    # Subscriptions (2 pages)
    for _ in range(2):
        pages.append(subscription_page())

    # Security Checklist
    pages.append(security_checklist_page())

    # Notes (3 pages)
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
