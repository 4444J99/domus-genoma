#!/usr/bin/env python3
"""Check this edition's exact file boundary and example shell syntax."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "README.md", "LICENSE", ".chezmoiignore", ".gitignore", "form-manifest.yaml",
    "docs/architecture.md", "docs/public-private-boundary.md",
    "examples/chezmoi/README.md", "examples/chezmoi/dot_editorconfig",
    "examples/chezmoi/dot_zshenv", "examples/chezmoi/dot_config/zsh/00-init.zsh",
    "examples/chezmoi/dot_config/zsh/01-history.zsh",
    "examples/chezmoi/dot_config/zsh/dot_zshrc", "tools/check_public.py",
}


def main() -> int:
    files = set()
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if rel.parts[0] == ".git" or "__pycache__" in rel.parts:
            continue
        if path.is_symlink():
            raise ValueError(f"symlink is not admitted: {rel}")
        if path.is_file():
            files.add(rel.as_posix())
    if files != EXPECTED:
        raise ValueError(f"file boundary differs: {sorted(files ^ EXPECTED)}")
    # The manifest has a deliberately simple, explicit paths section.
    text = (ROOT / "form-manifest.yaml").read_text()
    section = text.split("paths:\n", 1)[1].split("exact_sources:", 1)[0]
    declared = {line.removeprefix("  - ").strip() for line in section.splitlines() if line.startswith("  - ")}
    if declared | {"form-manifest.yaml"} != EXPECTED:
        raise ValueError("manifest and admitted files differ")
    shells = [p for p in files if p.endswith(".zsh") or p.endswith(("dot_zshenv", "dot_zshrc"))]
    for path in sorted(shells):
        subprocess.run(["zsh", "-n", str(ROOT / path)], check=True, timeout=10)
    print(f"PASS: {len(files)} admitted files; {len(shells)} shell syntax checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
