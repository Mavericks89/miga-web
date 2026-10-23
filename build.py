import os, sys
ROOT = sys.argv[1]
SITE = "https://migaworldwide.com"
LEGAL = "NEXILON LLC"
ADDR = "1209 Mountain Road Pl NE, Ste N, Albuquerque, NM 87110, USA"
ADDR_HTML = "1209 Mountain Road Pl NE, Ste N<br>Albuquerque, NM 87110, USA"
PHONE = "+1 (505) 369-2676"  # número de empresa (Dingtone), el mismo que en Meta; nunca el personal
PHONE_TEL = "+15053692676"
EMAIL = "info@migaworldwide.com"
YEAR = "2026"
PHONE_FOOT = f'<a href="tel:{PHONE_TEL}">{PHONE}</a>' if PHONE else ""
PHONE_LINE = f'<a href="tel:{PHONE_TEL}">{PHONE}</a> · ' if PHONE else ""
DISCLAIMER = "MIGA Worldwide does not provide investment, legal or tax advice and is not a registered broker-dealer or investment adviser."

LOGO = '<svg class="logo" viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="12" fill="#0f2a44"/><path d="M14 46V18l18 16 18-16v28" fill="none" stroke="#c9a86a" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/></svg>'

def icon(name):
    paths = {
        "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
        "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>',
        "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
        "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
        "building": '<path d="M4 21V5l8-2v18M12 9h8v12M8 8h0M8 12h0M8 16h0M16 13h0M16 17h0"/><path d="M2 21h20"/>',
        "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
        "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
        "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8.2-8 9-4.6-.8-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
        "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
        "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
        "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
        "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    }
    return f'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true">{paths[name]}</svg>'

PHONE_DL = f'      <dt>{icon("phone")}Phone</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd>\n' if PHONE else ""

HERO_ART = '''<svg class="hero-art" viewBox="0 0 480 400" aria-hidden="true">
  <defs>
    <linearGradient id="arc" x1="0" x2="1"><stop offset="0" stop-color="#c9a86a" stop-opacity=".2"/><stop offset=".5" stop-color="#c9a86a"/><stop offset="1" stop-color="#c9a86a" stop-opacity=".2"/></linearGradient>
  </defs>
  <g fill="none" stroke="rgba(255,255,255,.10)">
    <circle cx="240" cy="200" r="170"/><circle cx="240" cy="200" r="120"/><circle cx="240" cy="200" r="70"/>
    <ellipse cx="240" cy="200" rx="60" ry="170"/><ellipse cx="240" cy="200" rx="120" ry="170"/>
    <path d="M70 200h340M90 120h300M90 280h300"/>
  </g>
  <path d="M115 226 C 160 70, 320 60, 367 140" fill="none" stroke="url(#arc)" stroke-width="2.5" stroke-dasharray="6 7"/>
  <g>
    <rect x="40" y="226" width="166" height="62" rx="10" fill="#fff"/>
    <circle cx="66" cy="257" r="12" fill="#e8eef5"/><path d="M60 263v-10l6 5 6-5v10" fill="none" stroke="#1d4e7a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="86" y="252" font-family="Inter,Arial,sans-serif" font-size="12" font-weight="600" fill="#0f2a44">Latin America</text>
    <text x="86" y="270" font-family="Inter,Arial,sans-serif" font-size="11" fill="#5b6675">Projects &amp; developers</text>
  </g>
  <g>
    <rect x="292" y="140" width="160" height="62" rx="10" fill="#fff"/>
    <circle cx="318" cy="171" r="12" fill="#f6efe1"/><path d="M312 177v-10l6 5 6-5v10" fill="none" stroke="#a8823e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="338" y="166" font-family="Inter,Arial,sans-serif" font-size="12" font-weight="600" fill="#0f2a44">Europe</text>
    <text x="338" y="184" font-family="Inter,Arial,sans-serif" font-size="11" fill="#5b6675">Investors &amp; projects</text>
  </g>
  <circle cx="115" cy="226" r="5" fill="#c9a86a"/><circle cx="367" cy="140" r="5" fill="#c9a86a"/>
</svg>'''

def page(path, title, desc, body, current, meta_comment=False):
    canon = SITE + ("/" if path == "" else f"/{path}/")
    nav = "".join(
        f'<a href="{href}"' + (' aria-current="page"' if key == current else "") + f">{label}</a>"
        for key, href, label in [("home","/","Home"),("about","/about/","About"),("contact","/contact/","Contact")])
    verif = ('\n  <meta name="facebook-domain-verification" content="yw71cjnn2fhqag37tvkx1z5cruil11" />'
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
  <meta name="theme-color" content="#0f2a44">
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
  <a class="brand" href="/">{LOGO}<span>MIGA <em>Worldwide</em></span></a>
  <nav aria-label="Main">{nav}<a class="nav-cta" href="/contact/">Get in touch</a></nav>
</div></header>
<main>
{body}
</main>
<footer class="site">
  <div class="wrap foot-grid">
    <div>
      <a class="brand brand-foot" href="/">{LOGO}<span>MIGA <em>Worldwide</em></span></a>
      <p class="foot-desc">B2B marketplace connecting investors and family offices with real estate developers and opportunities in Europe and Latin America.</p>
    </div>
    <div>
      <h4>Company</h4>
      <a href="/about/">About</a><a href="/contact/">Contact</a><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Use</a>
    </div>
    <div>
      <h4>Contact</h4>
      <address>{LEGAL}<br>{ADDR_HTML}</address>
      {PHONE_FOOT}<a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
  <div class="wrap foot-legal">
    <p>MIGA Worldwide is operated by {LEGAL} · {ADDR} · {PHONE_LINE}<a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p><a href="/privacy/">Privacy Policy</a> · <a href="/terms/">Terms of Use</a> · &copy; {YEAR} {LEGAL}. All rights reserved.</p>
    <p class="disclaimer">{DISCLAIMER}</p>
  </div>
</footer>
</body>
</html>
"""
    d = os.path.join(ROOT, path)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

def page_head(eyebrow, title, lead=""):
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<section class="page-head"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{title}</h1>{lead_html}</div></section>'

home = f"""<section class="hero"><div class="wrap hero-grid">
  <div>
    <span class="eyebrow eyebrow-light">Cross-border real estate · B2B</span>
    <h1>Connecting international investors with real estate opportunities</h1>
    <p>MIGA Worldwide is a B2B marketplace that connects investors and family offices with real estate developers and projects in Europe and Latin America.</p>
    <div class="actions"><a class="btn" href="/contact/">Contact us</a><a class="btn btn-ghost" href="#how-it-works">How it works</a></div>
  </div>
  {HERO_ART}
</div></section>

<section class="strip"><div class="wrap strip-grid">
  <div>{icon("globe")}<span><strong>Europe &amp; Latin America</strong>Cross-border focus</span></div>
  <div>{icon("users")}<span><strong>Investors &amp; family offices</strong>On one side</span></div>
  <div>{icon("building")}<span><strong>Developers &amp; projects</strong>On the other</span></div>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">What we do</span>
  <h2>A structured first step between investors and developers</h2>
  <p class="lead">We help qualified counterparties find each other across borders and give them the information they need to start a conversation.</p>
  <div class="grid three">
    <article class="card">{icon("search")}<h3>Project information overview</h3><p>We present the information developers provide in a clear format, without recommending any project.</p></article>
    <article class="card">{icon("doc")}<h3>Commercial information review</h3><p>We review the commercial information that developers share before an introduction is made. This is not an assessment or recommendation of any investment.</p></article>
    <article class="card">{icon("link")}<h3>Introductions</h3><p>We connect investors and developers whose objectives fit, so they can talk directly and decide independently.</p></article>
  </div>
</div></section>

<section class="alt" id="how-it-works"><div class="wrap">
  <span class="eyebrow">How it works</span>
  <h2>Three steps, from first contact to introduction</h2>
  <ol class="steps">
    <li><span class="num">01</span><h3>Tell us what you are looking for</h3><p>Investors share their criteria; developers share their project.</p></li>
    <li><span class="num">02</span><h3>We review and introduce</h3><p>We review the information and introduce parties with compatible interests.</p></li>
    <li><span class="num">03</span><h3>We make the introduction</h3><p>Both parties are introduced and continue the process with their own advisers.</p></li>
  </ol>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">Who it is for</span>
  <h2>Built for both sides of the table</h2>
  <div class="grid two">
    <article class="panel">
      <div class="panel-head">{icon("users")}<h3>Investors and family offices</h3></div>
      <p>Looking for real estate projects outside their home market, with a clear first point of contact.</p>
      <ul class="checks"><li>{icon("check")}Share your criteria once</li><li>{icon("check")}Receive project information in a clear format</li><li>{icon("check")}Talk directly with developers</li></ul>
    </article>
    <article class="panel">
      <div class="panel-head">{icon("building")}<h3>Developers</h3></div>
      <p>Looking to present their projects to international investors in a structured way.</p>
      <ul class="checks"><li>{icon("check")}Present your project in a structured format</li><li>{icon("check")}Reach investors outside your market</li><li>{icon("check")}Keep the negotiation in your hands</li></ul>
    </article>
  </div>
</div></section>

<section class="alt"><div class="wrap">
  <span class="eyebrow">How we work</span>
  <h2>Our principles</h2>
  <div class="grid three">
    <article class="card flat">{icon("doc")}<h3>Clear information</h3><p>Project information is presented as provided by developers, in a consistent and readable format.</p></article>
    <article class="card flat">{icon("chat")}<h3>Direct relationships</h3><p>Once introduced, investors and developers deal with each other directly.</p></article>
    <article class="card flat">{icon("shield")}<h3>Independent decisions</h3><p>{DISCLAIMER} Each party decides with its own advisers.</p></article>
  </div>
</div></section>

<section class="cta"><div class="wrap cta-inner">
  <div><h2>Looking for projects or investors?</h2><p>Write to us and tell us what you are looking for.</p></div>
  <a class="btn" href="/contact/">Contact us</a>
</div></section>"""

about = page_head("About us", "About MIGA Worldwide", "A B2B marketplace for international real estate investment.") + f"""
<section><div class="wrap two-col">
  <div class="prose">
    <h2>What we do</h2>
    <p>MIGA Worldwide is a B2B marketplace for international real estate investment. We connect investors and family offices with developers and real estate opportunities in Europe and Latin America, and we support the first stage of the process with a presentation and review of the commercial information provided by developers.</p>
    <h2>What we are not</h2>
    <p>{DISCLAIMER} Investors and developers make their own decisions and should rely on their own independent advisers.</p>
  </div>
  <aside class="info-card">
    <h3>Who operates MIGA Worldwide</h3>
    <p>MIGA Worldwide is a brand operated by <strong>{LEGAL}</strong>, a United States limited liability company.</p>
    <dl>
      <dt>{icon("pin")}Address</dt><dd><address>{LEGAL}<br>{ADDR_HTML}</address></dd>
{PHONE_DL}      <dt>{icon("mail")}Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
      <dt>{icon("users")}Management</dt><dd>Manuel Reina Blanco, CEO</dd>
    </dl>
  </aside>
</div></section>"""

contact = page_head("Contact", "Contact us", "Write to us or call us and we will get back to you.") + f"""
<section><div class="wrap two-col">
  <aside class="info-card">
    <h3>MIGA Worldwide</h3>
    <p>Operated by <strong>{LEGAL}</strong></p>
    <dl>
      <dt>{icon("pin")}Address</dt><dd><address>{ADDR}</address></dd>
{PHONE_DL}      <dt>{icon("mail")}Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
    </dl>
  </aside>
  <div class="prose">
    <h2>Tell us what you are looking for</h2>
    <p>If you are an investor or family office, tell us your criteria. If you are a developer, tell us about your project. We reply by email.</p>
    <p><a class="btn" href="mailto:{EMAIL}?subject=Enquiry%20MIGA%20Worldwide">Send us an email</a></p>
  </div>
</div></section>"""

privacy = f"""<div class="page"><div class="wrap prose">
  <h1>Privacy Policy</h1>
  <p>Last updated: 22 October 2026</p>
  <h2>1. Data controller</h2>
  <p>The controller of the personal data processed through this website is <strong>{LEGAL}</strong>, operator of the MIGA Worldwide brand, with address at {ADDR}. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <h2>2. Data we collect</h2>
  <p>This website has no forms and does not use advertising or analytics cookies. We only process the personal data you send us when you contact us by email: typically your name, contact details, company and the content of your message.</p>
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
  <p>This website (migaworldwide.com) is operated by <strong>{LEGAL}</strong>, a United States limited liability company with address at {ADDR}, under the brand MIGA Worldwide. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
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

D = "MIGA Worldwide is a B2B marketplace connecting investors and family offices with real estate developers and opportunities in Europe and Latin America. Operated by NEXILON LLC."
page("", "MIGA Worldwide | International Real Estate Investment Marketplace", D, home, "home", meta_comment=True)
page("about", "About | MIGA Worldwide", "MIGA Worldwide is a brand operated by NEXILON LLC, a United States limited liability company.", about, "about")
page("contact", "Contact | MIGA Worldwide", "Contact MIGA Worldwide (NEXILON LLC): address, phone and email.", contact, "contact")
page("privacy", "Privacy Policy | MIGA Worldwide", "Privacy Policy of MIGA Worldwide, operated by NEXILON LLC.", privacy, "")
page("terms", "Terms of Use | MIGA Worldwide", "Terms of Use of migaworldwide.com, operated by NEXILON LLC.", terms, "")
print("built")
