#!/usr/bin/env python3
"""Publish your sealed boot to YOUR public dist repo via the GitHub API (gh CLI).
1) Create a public repo (e.g. <you>/<instance>-dist), 2) set REPO below,
3) run after build_sealed_boot.py. Put the compact tier INSIDE your dist
README too — installers that can't fetch raw files must still get the real
text; never let a tool reconstruct your rules from a summary."""
import base64, json, pathlib, subprocess, sys

REPO = "[you]/[instance]-dist"   # ← set me
FILES = ["sealed-boot.md", "sealed-boot-compact.md"]
root = pathlib.Path(__file__).resolve().parent.parent

def gh(*args, ok404=False):
    r = subprocess.run(["gh", "api", *args], capture_output=True, text=True)
    if r.returncode != 0:
        if ok404 and "404" in r.stderr + r.stdout:
            return None
        sys.exit(f"gh api failed: {(r.stderr or r.stdout)[:300]}")
    return json.loads(r.stdout) if r.stdout.strip() else {}

if REPO.startswith("["):
    sys.exit("Set REPO at the top of this script first.")
for name in FILES:
    body = (root / name).read_text()
    existing = gh(f"repos/{REPO}/contents/{name}", ok404=True)
    args = ["-X", "PUT", f"repos/{REPO}/contents/{name}",
            "-f", f"message=publish {name}",
            "-f", f"content={base64.b64encode(body.encode()).decode()}"]
    if existing and existing.get("sha"):
        args += ["-f", f"sha={existing['sha']}"]
    gh(*args)
    print(f"published {name} → https://raw.githubusercontent.com/{REPO}/main/{name}")
