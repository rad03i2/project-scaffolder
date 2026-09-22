from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from . import __version__
from .core import TEMPLATES, plan, scaffold


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="project-scaffolder", description="Generate safe, useful project foundations.")
    p.add_argument("name", nargs="?", help="project directory/name")
    p.add_argument("--template", "-t", choices=sorted(TEMPLATES), default="python")
    p.add_argument("--destination", "-d", default=".")
    p.add_argument("--author", default="Radwan Abdulhadi Ahmed")
    p.add_argument("--force", action="store_true", help="replace scaffold-managed files that already exist")
    p.add_argument("--dry-run", action="store_true", help="show planned paths without writing")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    p.add_argument("--list-templates", action="store_true")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__} — Radwan Abdulhadi Ahmed / @rad03i2")
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.list_templates:
        payload = sorted(TEMPLATES)
        print(json.dumps(payload) if args.json else "\n".join(payload))
        return 0
    if not args.name:
        parser().error("name is required unless --list-templates is used")
    try:
        result = scaffold(args.name, Path(args.destination), args.template, args.author, args.force, args.dry_run)
    except (ValueError, FileExistsError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    rels = [str(p.relative_to(result.root)) for p in result.created]
    if args.json:
        print(json.dumps({"project": str(result.root), "template": args.template, "dry_run": args.dry_run, "files": rels}, indent=2))
    else:
        verb = "Would create" if args.dry_run else "Created"
        print(f"{verb} {result.root} ({len(rels)} files)")
        for rel in rels:
            print(f"  {rel}")
    return 0
