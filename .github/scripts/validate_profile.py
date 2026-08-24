#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[2]
readme = root / "README.md"
errors = []

if not readme.is_file() or not readme.read_text(encoding="utf-8").strip():
    errors.append("README.md is missing or empty")
else:
    text = readme.read_text(encoding="utf-8")
    required = ["pine-script-portfolio", "pine-script-indicators", "pine-script-v6-course", "120"]
    for value in required:
        if value not in text:
            errors.append(f"README.md must mention {value}")
    forbidden = ["115 scripts", "5 scripts produced documented Pine compilation errors"]
    for value in forbidden:
        if value in text:
            errors.append(f"README.md contains stale validation text: {value}")
    for target in re.findall(r"!?\\[[^]]*\\]\\(([^)]+)\\)", text):
        target = target.split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (root / target).resolve().exists():
            errors.append(f"Broken relative Markdown link: {target}")
    secret_patterns = [
        r"ghp_[A-Za-z0-9]{20,}",
        r"github_pat_[A-Za-z0-9_]{20,}",
        r"sk-[A-Za-z0-9]{20,}",
        r"AKIA[0-9A-Z]{16}",
    ]
    for pattern in secret_patterns:
        if re.search(pattern, text):
            errors.append("README.md may contain a credential pattern")

if errors:
    print("\n".join(f"ERROR: {item}" for item in errors))
    sys.exit(1)

print("Profile validation passed")
