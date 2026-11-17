#!/usr/bin/env python3
"""Conservative file-presence check only. NOT a Lens Studio/CLAD/LEAF validator."""
from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").expanduser().resolve()
print("Project folder:", root)
if not root.is_dir():
    print("ERROR: no project directory")
    raise SystemExit(2)

required = {
    "Lens Studio project (.esproj)": bool(list(root.glob("*.esproj"))),
    "MCP config (.mcp.json)": (root / ".mcp.json").is_file(),
    "Official Devpost skill brief": (root / "devpost/design-brief.md").is_file(),
}
for name, ok in required.items():
    print(("PRESENT" if ok else "MISSING") + ": " + name)

brief = root / "devpost/design-brief.md"
if brief.is_file():
    text = brief.read_text(encoding="utf-8", errors="replace")
    print(("MARKED APPROVED" if "status: approved" in text else "NOT MARKED APPROVED") + ": brief frontmatter")

print("\nThis does NOT verify whether plan-lens ran, CLAD built the Lens, LEAF tests executed, or SPECS preview works.")
raise SystemExit(0 if all(required.values()) else 1)
