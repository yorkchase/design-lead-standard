#!/usr/bin/env python3
"""Concatenate your instance's BOOT + RULES + PROCESS into sealed-boot.md —
the one-paste enablement file for any AI tool — plus a compact tier
(BOOT + RULES only) for knowledge fields with character caps.
Rerun after ANY change to the three sources; your retro checks freshness."""
import pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
T = root / "templates"
DIST_URL = "[SET AFTER CREATING YOUR DIST REPO — raw URL to sealed-boot.md]"

parts = [
    ("BOOT.md", "DOCUMENT 1 of 3 · BOOT — read this first"),
    ("RULES.md", "DOCUMENT 2 of 3 · RULES — the constitution (authoritative)"),
    ("PROCESS.md", "DOCUMENT 3 of 3 · PROCESS — the operating loop"),
]
m = re.search(r"\*(?:Instance version|Version) ([\d.]+) · (\S+)", (T / "RULES.md").read_text())
version, vdate = (m.group(1), m.group(2)) if m else ("0.1", "[date]")

def bundle(selected, name, note):
    header = (f"<!-- GENERATED — do not edit. Regenerate: python3 tools/build_sealed_boot.py -->\n\n"
              f"# sealed boot · {name} (v{version} · {vdate})\n\n{note}\n"
              f"Latest: {DIST_URL}\nTo check a pasted copy: ask the tool \"what version are you running?\"\n\n---\n")
    out = [header]
    for fname, title in selected:
        out.append(f"\n\n{'═' * 20} {title} {'═' * 20}\n\n{(T / fname).read_text()}")
    dest = root / f"sealed-boot{'' if name == 'full' else '-compact'}.md"
    dest.write_text("".join(out))
    print(f"wrote {dest.name} — {dest.stat().st_size:,} bytes")

bundle(parts, "full", "Paste into any AI tool's instructions/knowledge slot to enable this practice.")
bundle(parts[:2], "compact", "Compact tier for capped knowledge fields (constitution without the full loop — the loop's digest lives in BOOT).")
