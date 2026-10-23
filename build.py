import os, sys
ROOT = sys.argv[1]
SITE = "https://migaworldwide.com"
LEGAL = "DIGITAL BUSINESS CLUB LLC"
ADDR = "1209 Mountain Road Pl NE, Ste N, Albuquerque, NM 87110, USA"
PHONE = "+34 643 41 10 43"
PHONE_TEL = "+34643411043"
EMAIL = "info@migaworldwide.com"
YEAR = "2026"
DISCLAIMER = "MIGA Worldwide does not provide investment, legal or tax advice and is not a registered broker-dealer or investment adviser."

def page(path, title, desc, body, current, meta_comment=False):
    canon = SITE + ("/" if path == "" else f"/{path}/")
    nav = "".join(
        f'<a href="{href}"' + (' aria-current="page"' if key == current else "") + f">{label}</a>"
        for key, href, label in [("home","/","Home"),("about","/about/","About"),("contact","/contact/","Contact")])
    verif = ('\n  <!-- META DOMAIN VERIFICATION: <meta name="facebook-domain-verification" content="PEGAR_CODIGO_AQUI" /> -->'
             if meta_comment else "")
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">{verif}
  <link rel="canonical" href="{canon}">
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="MIGA Worldwide">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{SITE}/assets/og.png">
  <meta property="og:image:alt" content="MIGA Worldwide">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<header class="site"><div class="wrap">
  <a class="brand" href="/"><img src="/assets/favicon.svg" alt="" width="32" height="32">MIGA Worldwide</a>
  <nav aria-label="Main">{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer class="site"><div class="wrap">
  <p>MIGA Worldwide is operated by {LEGAL} · {ADDR} · <a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p><a href="/privacy/">Privacy Policy</a> · <a href="/terms/">Terms of Use</a> · &copy; {YEAR} {LEGAL}. All rights reserved.</p>
  <p class="disclaimer">{DISCLAIMER}</p>
</div></footer>
</body>
</html>
"""
    d = os.path.join(ROOT, path)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

home = f"""<section class="hero"><div class="wrap">
  <h1>Connecting international investors with real estate opportunities</h1>
  <p>MIGA Worldwide is a B2B marketplace that connects investors and family offices with real estate developers and projects in Europe and Latin America.</p>
  <a class="btn" href="/contact/">Contact us</a>
</div></section>
<section><div class="wrap">
  <h2>What we do</h2>
  <p class="lead">We help qualified counterparties find each other across borders and give them the information they need to start a conversation.</p>
  <div class="grid">
    <div class="card"><h3>Opportunity analysis</h3><p>We present the information developers provide in a clear format, without recommending any project.</p></div>
    <div class="card"><h3>Commercial due diligence</h3><p>We review the commercial information that developers share before an introduction is made. This is not an assessment or recommendation of any investment.</p></div>
    <div class="card"><h3>Introductions</h3><p>We connect investors and developers whose objectives fit, so they can talk directly and decide independently.</p></div>
  </div>
</div></section>
<section class="alt"><div class="wrap">
  <h2>How it works</h2>
  <div class="grid">
    <div class="card"><span class="step">01</span><h3>Tell us what you are looking for</h3><p>Investors share their criteria; developers share their project.</p></div>
    <div class="card"><span class="step">02</span><h3>We analyse and match</h3><p>We review the information and identify counterparties that fit.</p></div>
    <div class="card"><span class="step">03</span><h3>We make the introduction</h3><p>Both parties are introduced and continue the process with their own advisers.</p></div>
  </div>
</div></section>
<section><div class="wrap">
  <h2>Who it is for</h2>
  <div class="grid">
    <div class="card"><h3>Investors and family offices</h3><p>Looking for real estate projects outside their home market, with a clear first point of contact.</p></div>
    <div class="card"><h3>Developers</h3><p>Looking to present their projects to international investors in a structured way.</p></div>
  </div>
  <p style="margin-top:32px"><a class="btn" href="/contact/">Get in touch</a></p>
</div></section>"""

about = f"""<div class="page"><div class="wrap prose">
  <h1>About us</h1>
  <p>MIGA Worldwide is a B2B marketplace for international real estate investment. We connect investors and family offices with developers and real estate opportunities in Europe and Latin America, and we support the first stage of the process with opportunity analysis and a review of the commercial information provided by developers.</p>
  <h2>Who operates MIGA Worldwide</h2>
  <p>MIGA Worldwide is a brand operated by <strong>{LEGAL}</strong>, a Limited Liability Company registered in the State of New Mexico, USA.</p>
  <address>
    <strong>{LEGAL}</strong><br>
    {ADDR}<br>
    Phone: <a href="tel:{PHONE_TEL}">{PHONE}</a><br>
    Email: <a href="mailto:{EMAIL}">{EMAIL}</a>
  </address>
  <p>Manuel Reina Blanco, CEO.</p>
  <h2>What we are not</h2>
  <p>{DISCLAIMER} Investors and developers make their own decisions and should rely on their own independent advisers.</p>
</div></div>"""

contact = f"""<div class="page"><div class="wrap prose">
  <h1>Contact</h1>
  <p>Write to us or call us and we will get back to you.</p>
  <dl class="contact-box">
    <dt>Company</dt><dd>MIGA Worldwide, operated by {LEGAL}</dd>
    <dt>Address</dt><dd><address>{ADDR}</address></dd>
    <dt>Phone</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd>
    <dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
    <dt>General enquiries</dt><dd><a href="mailto:contact@migaworldwide.com">contact@migaworldwide.com</a></dd>
  </dl>
  <p style="margin-top:28px"><a class="btn" href="mailto:{EMAIL}?subject=Enquiry%20MIGA%20Worldwide">Send us an email</a></p>
</div></div>"""

privacy = f"""<div class="page"><div class="wrap prose">
  <h1>Privacy Policy</h1>
  <p>Last updated: 22 October 2026</p>
  <h2>1. Data controller</h2>
  <p>The controller of the personal data processed through this website is <strong>{LEGAL}</strong>, operator of the MIGA Worldwide brand, with address at {ADDR}. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <h2>2. Data we collect</h2>
  <p>This website has no forms and does not use advertising or analytics cookies. We only process the personal data you send us when you contact us by email or phone: typically your name, contact details, company and the content of your message.</p>
  <p>Our hosting provider may automatically record technical data (such as IP address, browser type and date and time of access) in server logs for security and operational purposes.</p>
  <h2>3. Purposes and legal basis</h2>
  <p>We use your data to answer your enquiries and, where applicable, to manage a business relationship with you. The legal basis is your request and our legitimate interest in responding to it, or the performance of pre-contractual or contractual measures.</p>
  <h2>4. Retention</h2>
  <p>We keep your data for as long as necessary to handle your enquiry or business relationship and, afterwards, for the periods required by applicable law.</p>
  <h2>5. Recipients and international transfers</h2>
  <p>We do not sell your personal data. We may share it with service providers that support our operations (such as email and hosting providers), bound by appropriate confidentiality obligations. Some of these providers may be located outside your country, including in the United States; where required, we rely on appropriate safeguards for such transfers.</p>
  <h2>6. Your rights</h2>
  <p>Depending on applicable law, you may request access to, rectification or erasure of your data, object to or restrict its processing, and request data portability, by writing to <a href="mailto:{EMAIL}">{EMAIL}</a>. If you are in the European Economic Area, you may also lodge a complaint with your local data protection authority.</p>
  <h2>7. Changes</h2>
  <p>We may update this policy. The current version is always available on this page.</p>
</div></div>"""

terms = f"""<div class="page"><div class="wrap prose">
  <h1>Terms of Use</h1>
  <p>Last updated: 22 October 2026</p>
  <h2>1. Operator</h2>
  <p>This website (migaworldwide.com) is operated by <strong>{LEGAL}</strong>, a Limited Liability Company registered in New Mexico, USA, with address at {ADDR}, under the brand MIGA Worldwide. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <h2>2. Purpose of the website</h2>
  <p>This website provides general information about MIGA Worldwide, a B2B service that connects investors and developers in the real estate sector. Nothing on this website is an offer to sell, a solicitation of an offer to buy, or a recommendation regarding any security, investment or property.</p>
  <h2>3. No advice</h2>
  <p>{DISCLAIMER} Any decision you make is your own responsibility, and you should obtain independent professional advice before entering into any transaction.</p>
  <h2>4. Intellectual property</h2>
  <p>The content and design of this website belong to {LEGAL} unless otherwise stated. You may not copy or reuse them for commercial purposes without our prior written permission.</p>
  <h2>5. Limitation of liability</h2>
  <p>The information on this website is provided "as is" for general purposes. To the extent permitted by law, {LEGAL} is not liable for decisions made on the basis of this information or for interruptions or errors in the website.</p>
  <h2>6. Links</h2>
  <p>This website may contain links to third-party websites. We are not responsible for their content or policies.</p>
  <h2>7. Governing law</h2>
  <p>These terms are governed by the laws of the State of New Mexico, USA, without prejudice to any mandatory consumer protection rights you may have under the law of your country of residence.</p>
  <h2>8. Contact</h2>
  <p>For any question about these terms, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div></div>"""

D = "MIGA Worldwide is a B2B marketplace connecting investors and family offices with real estate developers and opportunities in Europe and Latin America. Operated by DIGITAL BUSINESS CLUB LLC."
page("", "MIGA Worldwide | International Real Estate Investment Marketplace", D, home, "home", meta_comment=True)
page("about", "About | MIGA Worldwide", "MIGA Worldwide is a brand operated by DIGITAL BUSINESS CLUB LLC, a New Mexico (USA) limited liability company.", about, "about")
page("contact", "Contact | MIGA Worldwide", "Contact MIGA Worldwide (DIGITAL BUSINESS CLUB LLC): address, phone and email.", contact, "contact")
page("privacy", "Privacy Policy | MIGA Worldwide", "Privacy Policy of MIGA Worldwide, operated by DIGITAL BUSINESS CLUB LLC.", privacy, "")
page("terms", "Terms of Use | MIGA Worldwide", "Terms of Use of migaworldwide.com, operated by DIGITAL BUSINESS CLUB LLC.", terms, "")
print("built")
