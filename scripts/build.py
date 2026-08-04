#!/usr/bin/env python3
"""Build automation script for the project.

Developed and tested in an isolated Daytona sandbox environment.

Steps:
  1. clean   - remove previous build artifacts
  2. lint    - byte-compile all sources to catch syntax errors
  3. test    - run the test suite (if present)
  4. package - create a timestamped tar.gz artifact in dist/
"""
import compileall
import shutil
import subprocess
import sys
import tarfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
VERSION = "1.0.0"


def clean():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)
    print("[clean] dist/ ready")


def lint():
    src = SRC if SRC.exists() else ROOT
    ok = compileall.compile_dir(str(src), quiet=1)
    if not ok:
        raise SystemExit("[lint] compilation failed")
    print(f"[lint] OK - {src}")


def test():
    tests = ROOT / "tests"
    if tests.exists():
        subprocess.check_call([sys.executable, "-m", "pytest", str(tests), "-q"])
        print("[test] OK")
    else:
        print("[test] no tests/ directory - skipped")


def package():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    artifact = DIST / f"project-{VERSION}-{stamp}.tar.gz"
    with tarfile.open(artifact, "w:gz") as tar:
        for item in ("src", "scripts", "data", "README.md"):
            p = ROOT / item
            if p.exists():
                tar.add(p, arcname=item)
    print(f"[package] wrote {artifact}")
    return artifact


def main():
    print(f"=== build v{VERSION} ===")
    clean()
    lint()
    test()
    artifact = package()
    print(f"=== build OK -> {artifact} ===")


if __name__ == "__main__":
    main()
