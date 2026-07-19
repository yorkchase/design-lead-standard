#!/usr/bin/env python3
"""Cross-link checker for the design KB.

Validates every internal Markdown cross-link in the knowledge base:
  * file references resolve to a real file (tried file-relative, root-relative,
    then by unique basename so prose mentions of an existing file pass)
  * `#anchor` fragments resolve to a real heading (GitHub slug rules)

Usage:
    python3 tools/linkcheck.py          # human-readable report
    python3 tools/linkcheck.py --quiet  # only print problems

Exit code is 1 if any ERROR is found (broken path-link or bad anchor), else 0
— so it can gate a pre-commit hook or CI. WARNINGS (bare filename mentions that
don't resolve — usually roadmap files not yet built) never fail the run.

Not checked: external URLs, and bare `#anchor` continuation refs that inherit
their file from a preceding token (rare; verify those by hand).
"""
import os, re, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUIET = "--quiet" in sys.argv

EXTERNAL_BASENAMES = {"AGENT.md", "SKILL.md", "LICENSE.txt"}
DOMAIN_RE = re.compile(r'[a-z0-9]\.(com|org|io|dev|net|ai)/')

def is_external(token):
    if "://" in token or DOMAIN_RE.search(token):
        return True
    if token.startswith(("claude/", "memory/")) or "/memory/" in token:
        return True
    return os.path.basename(token) in EXTERNAL_BASENAMES

def slugify(text):
    text = text.strip().lower()
    text = re.sub(r'[^\w\s-]', '', text, flags=re.UNICODE)
    text = re.sub(r'\s+', '-', text)
    return text

# ---- inventory ----
real_files, md_files = set(), []
for dp, dn, fn in os.walk(ROOT):
    if os.sep + ".git" in dp:
        continue
    for f in fn:
        rel = os.path.relpath(os.path.join(dp, f), ROOT)
        real_files.add(rel)
        if f.endswith(".md") and not rel.startswith("_sources" + os.sep):
            md_files.append(rel)

basename_index = defaultdict(list)
for rel in real_files:
    basename_index[os.path.basename(rel)].append(rel)

# ---- heading slugs per file ----
heading_slugs = {}
for rel in (r for r in real_files if r.endswith(".md")):
    slugs, counts, in_fence = set(), defaultdict(int), False
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        for ln in fh:
            if ln.lstrip().startswith("```"):
                in_fence = not in_fence; continue
            if in_fence:
                continue
            m = re.match(r'^(#{1,6})\s+(.*?)\s*#*\s*$', ln)
            if m:
                base = slugify(m.group(2))
                if not base:
                    continue
                n = counts[base]; counts[base] += 1
                slugs.add(base if n == 0 else f"{base}-{n}")
    heading_slugs[rel] = slugs

def resolve(src, path):
    for c in (os.path.normpath(os.path.join(os.path.dirname(src), path)),
              os.path.normpath(path)):
        if c in real_files:
            return c
    hits = basename_index.get(os.path.basename(path), [])
    return hits[0] if len(hits) == 1 else None

# ---- scan ----
path_re = re.compile(r'([A-Za-z0-9_][A-Za-z0-9_./-]*\.md)(#[A-Za-z0-9_-]+)?')
mdlink_re = re.compile(r'\[[^\]]*\]\(([^)]+)\)')

errors, warnings, ok = [], [], 0
for src in sorted(md_files):
    with open(os.path.join(ROOT, src), encoding="utf-8") as fh:
        text = fh.read()
    mdlink_targets = {m.group(1).split("#")[0] for m in mdlink_re.finditer(text)
                      if not m.group(1).startswith(("http", "mailto:", "#"))}
    seen = set()
    for m in path_re.finditer(text):
        if "://" in text[max(0, m.start()-4):m.start()]:
            continue
        path, anchor = m.group(1), (m.group(2) or "")[1:]
        if (path, anchor) in seen:
            continue
        seen.add((path, anchor))
        if is_external(path):
            continue
        resolved = resolve(src, path)
        # a reference is a hard LINK if it's a real md-link, has an anchor,
        # or is a real path (contains a slash); otherwise it's a soft MENTION.
        hard = path in mdlink_targets or bool(anchor) or "/" in path
        if resolved is None:
            (errors if hard else warnings).append(
                (src, path + ("#" + anchor if anchor else ""),
                 "unresolved path"))
        elif anchor and anchor not in heading_slugs.get(resolved, set()):
            errors.append((src, f"{path}#{anchor}",
                           f"no heading '#{anchor}' in {resolved}"))
        else:
            ok += 1

# ---- report ----
if not QUIET:
    print(f"Scanned {len(md_files)} Markdown files — {ok} internal links OK\n")
if errors:
    print(f"ERRORS ({len(errors)}):")
    for src, ref, why in errors:
        print(f"  {src}\n     {ref}  —  {why}")
elif not QUIET:
    print("No broken links or anchors. ✓")
if warnings:
    print(f"\nWARNINGS ({len(warnings)}) — bare filename mentions that don't "
          f"resolve (roadmap files not yet built, or prose):")
    for src, ref, why in sorted(warnings):
        print(f"  {src}  ->  {ref}")

sys.exit(1 if errors else 0)
