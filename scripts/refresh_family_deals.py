#!/usr/bin/env python3
"""Filter the public RFD Hot Deals Atom feed into family-relevant titles.

Does not invent editorial why-copy. Writes candidate titles so an editor
can keep or drop them. Curated picks in data/deals.json stay hand-written.
"""
from __future__ import annotations

import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FEED = "https://forums.redflagdeals.com/feed/forum/9"
KEYWORDS = (
    "kid", "kids", "child", "children", "family", "school", "lunch",
    "diaper", "toy", "lego", "hot wheels", "grape", "grocery", "no frills",
    "dollarama", "costco", "walmart", "amazon.ca", "boston pizza",
    "domino", "pizza", "winter", "jacket", "canada goose", "snack",
)
SKIP = ("refrigerator", "fridge")
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "candidates.json"
TITLE_RE = re.compile(r"<title type=\"html\"><!\[CDATA\[(.*?)\]\]></title>")
LINK_RE = re.compile(r"<link href=\"([^\"]+)\"")


def main() -> None:
    req = urllib.request.Request(FEED, headers={"User-Agent": "familydeals-ca/0.1"})
    xml = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    kept = []
    for entry in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        tm = TITLE_RE.search(entry)
        lm = LINK_RE.search(entry)
        if not tm or not lm:
            continue
        title = tm.group(1)
        low = title.lower()
        if any(s in low for s in SKIP):
            continue
        if any(k in low for k in KEYWORDS):
            kept.append({"title": title, "href": lm.group(1)})
    payload = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "source": FEED,
        "count": len(kept),
        "candidates": kept,
    }
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"wrote {len(kept)} candidates to {OUT}")


if __name__ == "__main__":
    main()
