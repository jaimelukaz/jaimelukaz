#!/usr/bin/env python3
"""Generates the MU Online–style GitHub profile: SVG assets + README in PT/EN/ES."""
from pathlib import Path

OUT = Path(__file__).parent
A = OUT / "assets"
A.mkdir(exist_ok=True)

GOLD = "#e8c170"
GOLD_D = "#a67c2e"
BG = "#0d0a07"
BG2 = "#1a120b"
BLOOD = "#8b1e1e"
TXT = "#f3e6c8"
FONT = "Cinzel, 'Trajan Pro', 'Palatino Linotype', Palatino, Georgia, serif"

DEFS = f"""
<defs>
  <linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#fff1c1"/><stop offset=".45" stop-color="{GOLD}"/>
    <stop offset=".55" stop-color="{GOLD_D}"/><stop offset="1" stop-color="#f6d27a"/>
  </linearGradient>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#20160d"/><stop offset="1" stop-color="{BG}"/>
  </linearGradient>
  <radialGradient id="glow" cx=".5" cy=".55" r=".6">
    <stop offset="0" stop-color="#7a2a0c" stop-opacity=".55"/><stop offset="1" stop-color="#000" stop-opacity="0"/>
  </radialGradient>
  <filter id="shine" x="-20%" y="-50%" width="140%" height="200%">
    <feGaussianBlur stdDeviation="3" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>"""


def frame(w, h, inset=14):
    """Ornamented double border with corner diamonds."""
    i, j = inset, inset + 6
    c = []
    c.append(f'<rect x="{i}" y="{i}" width="{w-2*i}" height="{h-2*i}" rx="4" fill="none" stroke="url(#gold)" stroke-width="2.5"/>')
    c.append(f'<rect x="{j}" y="{j}" width="{w-2*j}" height="{h-2*j}" rx="2" fill="none" stroke="{GOLD_D}" stroke-width="1" opacity=".7"/>')
    for x, y in [(i, i), (w - i, i), (i, h - i), (w - i, h - i)]:
        c.append(f'<path d="M{x} {y-11} L{x+11} {y} L{x} {y+11} L{x-11} {y} Z" fill="{BG}" stroke="url(#gold)" stroke-width="2"/>')
        c.append(f'<circle cx="{x}" cy="{y}" r="3" fill="{BLOOD}"/>')
    return "\n".join(c)


def embers(w, h, n=18, seed=7):
    import random
    r = random.Random(seed)
    out = []
    for _ in range(n):
        x = r.randint(30, w - 30)
        dur = r.uniform(4, 9)
        delay = r.uniform(0, 6)
        size = r.uniform(1, 2.6)
        out.append(
            f'<circle cx="{x}" cy="{h-20}" r="{size:.1f}" fill="#ffb347" opacity="0">'
            f'<animate attributeName="cy" from="{h-20}" to="{r.randint(20, h//2)}" dur="{dur:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0;.9;0" dur="{dur:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/>'
            f'</circle>')
    return "\n".join(out)


def sword(x, y, s=1, flip=False):
    t = f'translate({x},{y}) scale({-s if flip else s},{s}) rotate(-35)'
    return f"""<g transform="{t}" opacity=".9">
  <path d="M0 -70 L6 -58 L6 30 L0 38 L-6 30 L-6 -58 Z" fill="#cfd6dd" stroke="#6b7682" stroke-width="1"/>
  <path d="M0 -62 L0 30" stroke="#ffffff" stroke-width="1" opacity=".6"/>
  <rect x="-22" y="30" width="44" height="7" rx="3" fill="url(#gold)"/>
  <rect x="-3.5" y="37" width="7" height="24" fill="#5a3a1c"/>
  <circle cx="0" cy="65" r="6" fill="url(#gold)"/><circle cx="0" cy="65" r="2.5" fill="{BLOOD}"/>
</g>"""


# ---------------------------------------------------------------- banner
def banner():
    w, h = 900, 260
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{DEFS}
<style>
  .t{{font-family:{FONT};}}
  @keyframes pulse{{0%,100%{{opacity:.55}}50%{{opacity:1}}}}
  .p{{animation:pulse 3.5s ease-in-out infinite}}
</style>
<rect width="{w}" height="{h}" fill="url(#bg)"/>
<rect width="{w}" height="{h}" fill="url(#glow)" class="p"/>
<!-- castle silhouette -->
<path d="M0 {h} L0 205 L40 205 L40 190 L52 190 L52 200 L64 200 L64 190 L76 190 L76 205 L120 205 L120 170 L130 150 L140 170 L140 205
 L760 205 L760 170 L770 150 L780 170 L780 205 L824 205 L824 190 L836 190 L836 200 L848 200 L848 190 L860 190 L860 205 L{w} 205 L{w} {h} Z"
 fill="#000" opacity=".55"/>
{embers(w, h)}
{sword(95, 120, 1.15)}
{sword(805, 120, 1.15, flip=True)}
<text x="450" y="58" text-anchor="middle" class="t" font-size="15" letter-spacing="7" fill="{GOLD_D}">⚔ DN4CODE TECH SOLUTIONS ⚔</text>
<text x="450" y="128" text-anchor="middle" class="t" font-size="58" font-weight="700" letter-spacing="5"
 fill="url(#gold)" stroke="#3a2410" stroke-width="1.2" filter="url(#shine)">JAIME LUCAS</text>
<path d="M250 150 H420 L450 140 L480 150 H650" fill="none" stroke="url(#gold)" stroke-width="2"/>
<circle cx="450" cy="150" r="5" fill="{BLOOD}" stroke="url(#gold)" stroke-width="1.5"/>
<text x="450" y="185" text-anchor="middle" class="t" font-size="19" letter-spacing="4" fill="{TXT}">MAGIC GLADIATOR · FULL-STACK</text>
<text x="450" y="212" text-anchor="middle" class="t" font-size="13" letter-spacing="3" fill="{GOLD_D}">RUBY ON RAILS · REACT NATIVE · POSTGRESQL · AWS</text>
{frame(w, h)}
</svg>"""


# ---------------------------------------------------------------- character card
L = {
    "pt": dict(title="FICHA DO PERSONAGEM", cls="Classe", clsv="Magic Gladiator",
               lvl="Nível", guild="Guilda", realm="Servidor", realmv="Brasil 🇧🇷",
               hp="HP", mp="MP", hpv="Café", mpv="Foco", stats="ATRIBUTOS",
               pts="Pontos livres: 0 — tudo distribuído"),
    "en": dict(title="CHARACTER SHEET", cls="Class", clsv="Magic Gladiator",
               lvl="Level", guild="Guild", realm="Realm", realmv="Brazil 🇧🇷",
               hp="HP", mp="MP", hpv="Coffee", mpv="Focus", stats="ATTRIBUTES",
               pts="Free points: 0 — all distributed"),
    "es": dict(title="FICHA DEL PERSONAJE", cls="Clase", clsv="Magic Gladiator",
               lvl="Nivel", guild="Gremio", realm="Servidor", realmv="Brasil 🇧🇷",
               hp="HP", mp="MP", hpv="Café", mpv="Foco", stats="ATRIBUTOS",
               pts="Puntos libres: 0 — todo distribuido"),
}
STATS = [  # MU attribute, skill, value(out of 32767), color
    ("STR", "Ruby on Rails", 32767, "#cc342d"),
    ("AGI", "React Native", 28400, "#61dafb"),
    ("VIT", "PostgreSQL", 30100, "#6c9bd2"),
    ("ENE", "AWS", 24800, "#ff9900"),
    ("CMD", "UI/UX · Figma", 22500, "#a259ff"),
]


def card(lang):
    t = L[lang]
    w, h = 900, 330
    rows = []
    y0 = 128
    for i, (attr, skill, val, col) in enumerate(STATS):
        y = y0 + i * 34
        pct = val / 32767
        bw = 330
        rows.append(f"""
<text x="470" y="{y+5}" class="t" font-size="15" font-weight="700" fill="url(#gold)">{attr}</text>
<text x="520" y="{y+5}" class="s" font-size="13" fill="{TXT}">{skill}</text>
<rect x="520" y="{y+11}" width="{bw}" height="8" rx="2" fill="#2a1d12" stroke="{GOLD_D}" stroke-width=".6"/>
<rect x="520" y="{y+11}" width="0" height="8" rx="2" fill="{col}">
  <animate attributeName="width" from="0" to="{bw*pct:.0f}" dur="1.4s" begin="{0.2+i*0.15:.2f}s" fill="freeze"/>
</rect>
<text x="850" y="{y+5}" text-anchor="end" class="s" font-size="12" fill="{GOLD}">{val}</text>""")

    def kv(y, k, v):
        return (f'<text x="60" y="{y}" class="s" font-size="13" fill="{GOLD_D}">{k}</text>'
                f'<text x="170" y="{y}" class="t" font-size="16" fill="{TXT}">{v}</text>')

    def bar(y, k, label, col):
        return (f'<text x="60" y="{y}" class="t" font-size="13" font-weight="700" fill="{col}">{k}</text>'
                f'<rect x="100" y="{y-11}" width="300" height="14" rx="7" fill="#2a1d12" stroke="{GOLD_D}" stroke-width=".8"/>'
                f'<rect x="102" y="{y-9}" width="296" height="10" rx="5" fill="{col}" opacity=".85">'
                f'<animate attributeName="opacity" values=".6;1;.6" dur="2.4s" repeatCount="indefinite"/></rect>'
                f'<text x="250" y="{y}" text-anchor="middle" class="s" font-size="10" fill="#fff">{label} 100%</text>')

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{DEFS}
<style>.t{{font-family:{FONT};}}.s{{font-family:Georgia,'Times New Roman',serif;}}</style>
<rect width="{w}" height="{h}" fill="url(#bg)"/>
<text x="450" y="52" text-anchor="middle" class="t" font-size="20" font-weight="700" letter-spacing="6" fill="url(#gold)">{t['title']}</text>
<path d="M300 66 H600" stroke="{GOLD}" stroke-width="1.5"/>
<line x1="440" y1="95" x2="440" y2="300" stroke="{GOLD_D}" stroke-width="1" opacity=".5"/>
{kv(110, t['cls'], t['clsv'])}
{kv(140, t['lvl'], '400 <tspan fill="' + GOLD_D + '" font-size="12">· Master Reset</tspan>')}
{kv(170, t['guild'], 'DN4Code Tech Solutions')}
{kv(200, t['realm'], t['realmv'])}
{bar(245, t['hp'], t['hpv'], '#b22222')}
{bar(275, t['mp'], t['mpv'], '#2f5fd0')}
<text x="470" y="102" class="t" font-size="12" letter-spacing="4" fill="{GOLD_D}">{t['stats']}</text>
{''.join(rows)}
<text x="850" y="302" text-anchor="end" class="s" font-size="11" font-style="italic" fill="{GOLD_D}">{t['pts']}</text>
{frame(w, h)}
</svg>"""


def divider():
    w, h = 900, 30
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{DEFS}
<path d="M40 15 H420" stroke="{GOLD_D}" stroke-width="1.5"/><path d="M480 15 H860" stroke="{GOLD_D}" stroke-width="1.5"/>
<path d="M450 3 L462 15 L450 27 L438 15 Z" fill="{BLOOD}" stroke="url(#gold)" stroke-width="2"/>
<circle cx="420" cy="15" r="3" fill="{GOLD}"/><circle cx="480" cy="15" r="3" fill="{GOLD}"/>
</svg>"""


(A / "banner.svg").write_text(banner(), encoding="utf-8")
(A / "divider.svg").write_text(divider(), encoding="utf-8")
for lg in L:
    (A / f"card-{lg}.svg").write_text(card(lg), encoding="utf-8")

# ---------------------------------------------------------------- README
U = "jaimelukaz"
STATS_THEME = "bg_color=0d0a07&title_color=e8c170&text_color=f3e6c8&icon_color=a67c2e&border_color=a67c2e&ring_color=8b1e1e"

T = {
    "pt": dict(file="README.md",
               intro="> *Um Magic Gladiator do servidor Brasil: metade guerreiro do backend, metade mago do mobile. Forja sistemas em **Rails** e **PostgreSQL**, invoca apps em **React Native**, desenha interfaces no **Figma** e mantém tudo de pé nas muralhas da **AWS**. Co-fundador da guilda **DN4Code Tech Solutions**.*",
               quests="📜 Missões ativas", qh=("Missão", "Recompensa", "Status"),
               q=[("🎯 **OpinaKI**", "Rede social gamificada de previsões e opiniões — [opinaki.com](https://opinaki.com)", "⚔ Em batalha"),
                  ("🏰 **MU Online Server**", "Servidor privado de MU Online, do core ao client", "⚔ Em batalha"),
                  ("💰 **SisPag**", "Sistema de pagamentos — PIX, parcelamentos e operações com USDT", "⚔ Em batalha")],
               inv="🎒 Inventário", sk="🧪 Habilidades secundárias",
               skills="Hotkeys decoradas, commits atômicos, PRs com spec e um gosto suspeito por máscaras de input em centavos.",
               st="📊 Registro de batalha", party="🛡 Chamar para a party",
               foot="*“Quem não reseta, não evolui.”*"),
    "en": dict(file="README.en.md",
               intro="> *A Magic Gladiator from the Brazil realm: half backend warrior, half mobile mage. Forges systems in **Rails** and **PostgreSQL**, summons apps with **React Native**, designs interfaces in **Figma** and keeps it all standing on the **AWS** walls. Co-founder of the **DN4Code Tech Solutions** guild.*",
               quests="📜 Active quests", qh=("Quest", "Reward", "Status"),
               q=[("🎯 **OpinaKI**", "Gamified social network for predictions and opinions — [opinaki.com](https://opinaki.com)", "⚔ In battle"),
                  ("🏰 **MU Online Server**", "Private MU Online server, from core to client", "⚔ In battle"),
                  ("💰 **SisPag**", "Payments system — PIX, installments and USDT operations", "⚔ In battle")],
               inv="🎒 Inventory", sk="🧪 Secondary skills",
               skills="Memorized hotkeys, atomic commits, spec-driven PRs and a suspicious taste for cents-based input masks.",
               st="📊 Battle log", party="🛡 Invite to party",
               foot="*“No reset, no progress.”*"),
    "es": dict(file="README.es.md",
               intro="> *Un Magic Gladiator del servidor Brasil: mitad guerrero del backend, mitad mago del mobile. Forja sistemas en **Rails** y **PostgreSQL**, invoca apps con **React Native**, diseña interfaces en **Figma** y lo mantiene todo en pie sobre las murallas de **AWS**. Cofundador del gremio **DN4Code Tech Solutions**.*",
               quests="📜 Misiones activas", qh=("Misión", "Recompensa", "Estado"),
               q=[("🎯 **OpinaKI**", "Red social gamificada de predicciones y opiniones — [opinaki.com](https://opinaki.com)", "⚔ En batalla"),
                  ("🏰 **MU Online Server**", "Servidor privado de MU Online, del core al cliente", "⚔ En batalla"),
                  ("💰 **SisPag**", "Sistema de pagos — PIX, cuotas y operaciones con USDT", "⚔ En batalla")],
               inv="🎒 Inventario", sk="🧪 Habilidades secundarias",
               skills="Hotkeys memorizadas, commits atómicos, PRs guiados por spec y un gusto sospechoso por máscaras de input en centavos.",
               st="📊 Registro de batalla", party="🛡 Invitar a la party",
               foot="*“Quien no resetea, no evoluciona.”*"),
}

FLAGS = {"pt": ("🇧🇷", "Português", "009c3b"), "en": ("🇺🇸", "English", "3c3b6e"), "es": ("🇪🇸", "Español", "c60b1e")}


def badge(label, color, logo, logo_color="white"):
    from urllib.parse import quote
    return (f'<img src="https://img.shields.io/badge/{quote(label)}-{color}?style=for-the-badge&logo={logo}'
            f'&logoColor={logo_color}" alt="{label}"/>')


INVENTORY = [
    ("Ruby", "CC342D", "ruby"), ("Rails", "8B0000", "rubyonrails"),
    ("PostgreSQL", "336791", "postgresql"), ("React Native", "20232A", "react", "61DAFB"),
    ("TypeScript", "3178C6", "typescript"), ("AWS", "232F3E", "amazonwebservices", "FF9900"),
    ("Docker", "2496ED", "docker"), ("Redis", "DC382D", "redis"),
    ("Figma", "1E1E1E", "figma", "F24E1E"), ("C++", "00599C", "cplusplus"),
]


def selector(cur):
    parts = []
    for lg, (flag, name, col) in FLAGS.items():
        style = "for-the-badge" if lg == cur else "flat-square"
        c = "e8c170" if lg == cur else "1a120b"
        lc = "0d0a07" if lg == cur else "e8c170"
        from urllib.parse import quote
        img = f'<img src="https://img.shields.io/badge/{quote(flag + " " + name)}-{c}?style={style}&labelColor={c}&color={c}&logoColor={lc}" alt="{name}"/>'
        parts.append(f'<a href="{T[lg]["file"]}">{img}</a>')
    return " ".join(parts)


def readme(lg):
    t = T[lg]
    rows = "\n".join(f"| {a} | {b} | {c} |" for a, b, c in t["q"])
    inv = "\n  ".join(badge(*i[:3], *(i[3:] or ["white"])) for i in INVENTORY)
    div = '<p align="center"><img src="assets/divider.svg" width="100%"/></p>'
    return f"""<!-- MU Online style profile · generated by gen.py -->
<p align="center">
  {selector(lg)}
</p>

<p align="center">
  <img src="assets/banner.svg" width="100%" alt="Jaime Lucas — Magic Gladiator · Full-Stack"/>
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Cinzel&weight=700&size=20&duration=3200&pause=900&color=E8C170&center=true&vCenter=true&width=700&lines=Rails+%E2%9A%94+PostgreSQL+%E2%9A%94+React+Native;AWS+%C2%B7+Figma+%C2%B7+PIX;DN4Code+Tech+Solutions+%E2%80%94+Co-founder" alt="typing"/>
</p>

{t['intro']}

<p align="center"><img src="assets/card-{lg}.svg" width="100%" alt="{t['quests']}"/></p>

{div}

## {t['quests']}

| {t['qh'][0]} | {t['qh'][1]} | {t['qh'][2]} |
|:--|:--|:--:|
{rows}

{div}

## {t['inv']}

<p align="center">
  {inv}
</p>

**{t['sk']}:** {t['skills']}

{div}

## {t['party']}

<p align="center">
  <a href="https://www.linkedin.com/in/jaimelukaz"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://instagram.com/jaimelucaz"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/></a>
  <a href="https://facebook.com/jaimelucazz"><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white"/></a>
  <a href="https://github.com/DN4code"><img src="https://img.shields.io/badge/DN4code-1a120b?style=for-the-badge&logo=github&logoColor=e8c170"/></a>
</p>

<p align="center">{t['foot']}</p>
"""


for lg in T:
    (OUT / T[lg]["file"]).write_text(readme(lg), encoding="utf-8")
print("ok")
