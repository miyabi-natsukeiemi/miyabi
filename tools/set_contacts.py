#!/usr/bin/env python3
"""Fill in the site's contacts and, optionally, the footer legal line.

Contacts live in one place: assets/contacts.js (used by the homepage #ask,
/services/ and /search/; article pages link to /#ask). Any value left out
keeps its current value, so contacts can be added one at a time.

Usage (from the repo root):
  python3 tools/set_contacts.py --telegram omamori_concierge --whatsapp "+7 999 123-45-67" --email hello@omamori-concierge.com
  python3 tools/set_contacts.py --legal "ИП Майструк Дарья Петровна · ОГРНИП … · ИНН …"
  python3 tools/set_contacts.py --check      # show what is set, change nothing
"""
import argparse, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
JS = ROOT / "assets" / "contacts.js"
FOOTER_PAGES = ["index.html", "services/index.html", "search/index.html", "404.html"]
LEGAL_PLACEHOLDER = "[ЮРЛИЦО, ИНН, РЕЕСТРОВЫЙ НОМЕР]"
KEYS = ("telegram", "whatsapp", "email")


def norm(key, v):
    v = v.strip()
    if key == "telegram":
        v = re.sub(r"^(https?://)?(t\.me|telegram\.me)/", "", v).lstrip("@")
        if not re.fullmatch(r"[A-Za-z0-9_]{5,32}", v):
            sys.exit(f"Telegram: «{v}» is not a valid user name (5–32 letters, digits, _)")
    elif key == "whatsapp":
        v = re.sub(r"\D", "", re.sub(r"^(https?://)?wa\.me/", "", v))
        if v.startswith("8") and len(v) == 11:  # Russian 8-xxx → 7-xxx
            v = "7" + v[1:]
        if not 10 <= len(v) <= 15:
            sys.exit(f"WhatsApp: «{v}» must be an international number with country code")
    elif key == "email":
        v = v.removeprefix("mailto:")
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", v):
            sys.exit(f"Email: «{v}» is not a valid address")
    return v


def current(js):
    return {k: re.search(rf"{k}: '([^']*)'", js).group(1) for k in KEYS}


def main():
    ap = argparse.ArgumentParser()
    for k in KEYS:
        ap.add_argument(f"--{k}")
    ap.add_argument("--legal", help="footer legal line (replaces the placeholder)")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    js = JS.read_text(encoding="utf-8")
    if not a.check:
        for k in KEYS:
            v = getattr(a, k)
            if v:
                js = re.sub(rf"({k}: ')[^']*(')", lambda m: m.group(1) + norm(k, v) + m.group(2), js, count=1)
        JS.write_text(js, encoding="utf-8")
        if a.legal:
            for p in FOOTER_PAGES:
                f = ROOT / p
                t = f.read_text(encoding="utf-8")
                if LEGAL_PLACEHOLDER not in t:
                    print(f"  ! {p}: placeholder not found (already filled?) — skipped")
                    continue
                f.write_text(t.replace(LEGAL_PLACEHOLDER, a.legal.replace("<", "&lt;")), encoding="utf-8")
                print(f"  footer updated: {p}")

    for k, v in current(js).items():
        print(f"  {k:9} {'— not set' if v.startswith('TODO') else v}")
    left = [p for p in FOOTER_PAGES if LEGAL_PLACEHOLDER in (ROOT / p).read_text(encoding="utf-8")]
    print(f"  legal     {'— placeholder in ' + ', '.join(left) if left else 'filled'}")


if __name__ == "__main__":
    main()
