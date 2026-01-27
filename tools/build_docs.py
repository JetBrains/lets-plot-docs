#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent  # tools/build_docs.py -> repo root

SPHINX_SRC_DIR = ROOT / "source"
DOCS_OUT_DIR = ROOT / "docs"

API_STUB_DIR = ROOT / "source/python/pages/api"   # generated stub pages dir
JUPYTER_EXECUTE_DIR = ROOT / "jupyter_execute"    # generated notebooks execution output

KEEP_IN_DOCS = {"kotlin"}


PROFILES = {
    "dev": {"execute_notebooks": 0, "clean": 1},
    "prod": {"execute_notebooks": 1, "clean": 1},
}


def rm_any(path: Path) -> None:
    if not path.exists():
        return
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink()


def clean_docs_dir() -> None:
    DOCS_OUT_DIR.mkdir(parents=True, exist_ok=True)
    for p in DOCS_OUT_DIR.iterdir():
        if p.name in KEEP_IN_DOCS:
            continue
        rm_any(p)


def parse_pre(values) -> list[Path]:
    # --pre a.py b.py  OR  --pre a.py,b.py  OR mixed
    if not values:
        return []
    parts = []
    for v in values:
        parts.extend([x.strip() for x in v.split(",") if x.strip()])

    out = []
    for s in parts:
        p = Path(s).expanduser()
        if not p.is_absolute():
            p = ROOT / p
        out.append(p.resolve())
    return out


def main() -> int:
    p = argparse.ArgumentParser("build_docs.py")

    p.add_argument("-t", "--type", choices=("dev", "prod"), default="dev")

    p.add_argument("-p", "--pre", nargs="*", default=None,
                   help="Python scripts to run before build (space and/or commas)")

    p.add_argument("-v", "--version", default=None,
                   help="Adds -D version=V -D release=V")

    p.add_argument("-s", "--switch-lets-plot", action="store_true",
                   help="Adds -D switch_lets_plot=True")

    # Single toggles, 0/1, default comes from profile
    p.add_argument("-e", "--execute-notebooks", type=int, choices=(0, 1), default=None,
                   help="Override execute_notebooks (0/1). Default depends on --type")

    p.add_argument("-c", "--clean", type=int, choices=(0, 1), default=None,
                   help="Clean generated dirs before build (0/1). Default depends on --type")

    mx = p.add_mutually_exclusive_group()
    mx.add_argument("-l", "--log-file", default=None,
                    help="Write sphinx output to file (stdout+stderr). No --quiet.")
    mx.add_argument("-L", "--console-log", action="store_true",
                    help="Show sphinx output in console. No --quiet.")

    args = p.parse_args()

    prof = PROFILES[args.type]
    execute_notebooks = prof["execute_notebooks"] if args.execute_notebooks is None else args.execute_notebooks
    clean = prof["clean"] if args.clean is None else args.clean

    # ---- profile restrictions ----
    if args.type == "prod" and clean == 0:
        raise SystemExit("prod build forbids --clean 0 (clean is always enabled in prod)")

    # ---- cleaning ----
    if clean == 1:
        print(f"Clean: {DOCS_OUT_DIR}/ (keep: {', '.join(sorted(KEEP_IN_DOCS))})")
        clean_docs_dir()

        print(f"Remove: {API_STUB_DIR}/")
        rm_any(API_STUB_DIR)

        print(f"Remove: {JUPYTER_EXECUTE_DIR}/")
        rm_any(JUPYTER_EXECUTE_DIR)

    # ---- pre scripts ----
    pre_scripts = parse_pre(args.pre)
    if pre_scripts:
        print("Pre-scripts:")
        for s in pre_scripts:
            print(f"  - {s}")
        for s in pre_scripts:
            if not s.exists():
                raise SystemExit(f"Pre-script not found: {s}")
            subprocess.run([sys.executable, "-m", "IPython", str(s)], cwd=str(ROOT), check=True)

    # ---- build cmd ----
    cmd = ["sphinx-build", "-b", "html"]

    log_file = Path(args.log_file).expanduser().resolve() if args.log_file else None

    # Quiet policy:
    # - default: --quiet (no console noise)
    # - if --log-file OR --console-log: no --quiet
    if (log_file is None) and (not args.console_log):
        cmd.append("--quiet")

    cmd.append("--fail-on-warning")
    cmd += ["-D", f"execute_notebooks={execute_notebooks}"]

    if args.version:
        cmd += ["-D", f"version={args.version}", "-D", f"release={args.version}"]

    if args.switch_lets_plot:
        cmd += ["-D", "switch_lets_plot=True"]

    cmd += [str(SPHINX_SRC_DIR), str(DOCS_OUT_DIR)]

    print("$", " ".join(cmd))

    if log_file is not None:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        with log_file.open("w", encoding="utf-8") as f:
            subprocess.run(cmd, cwd=str(ROOT), check=True, stdout=f, stderr=subprocess.STDOUT)
    else:
        subprocess.run(cmd, cwd=str(ROOT), check=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
