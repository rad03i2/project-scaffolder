from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

_NAME = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{0,63}$")

@dataclass(frozen=True)
class ScaffoldResult:
    root: Path
    created: tuple[Path, ...]


def validate_name(name: str) -> str:
    name = name.strip()
    if not _NAME.fullmatch(name):
        raise ValueError("project name must start with a letter and contain only letters, numbers, '-' or '_'")
    return name


def _python_files(name: str, author: str) -> dict[str, str]:
    package = name.lower().replace("-", "_")
    return {
        "README.md": f"# {name}\n\nGenerated Python project foundation.\n\n## Run\n\n```bash\npython -m {package}\n```\n",
        ".gitignore": "__pycache__/\n*.py[cod]\n.venv/\ndist/\nbuild/\n*.egg-info/\n.pytest_cache/\n",
        "pyproject.toml": f'''[build-system]\nrequires = ["hatchling>=1.25"]\nbuild-backend = "hatchling.build"\n\n[project]\nname = "{name}"\nversion = "0.1.0"\ndescription = "Generated with project-scaffolder"\nrequires-python = ">=3.10"\nauthors = [{{name = "{author}"}}]\n\n[tool.hatch.build.targets.wheel]\npackages = ["src/{package}"]\n''',
        f"src/{package}/__init__.py": '__version__ = "0.1.0"\n',
        f"src/{package}/__main__.py": 'def main():\n    print("Project is ready.")\n\nif __name__ == "__main__":\n    main()\n',
        "tests/test_smoke.py": f'def test_import():\n    import {package}\n    assert {package}.__version__ == "0.1.0"\n',
    }


def _web_files(name: str, author: str) -> dict[str, str]:
    safe_title = name.replace("-", " ").replace("_", " ").title()
    return {
        "README.md": f"# {name}\n\nDependency-free static web project. Open `index.html` in a browser.\n",
        ".gitignore": ".DS_Store\nThumbs.db\n.vscode/\n",
        "index.html": f'''<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="author" content="{author}"><title>{safe_title}</title><link rel="stylesheet" href="styles.css"></head><body><main><h1>{safe_title}</h1><p>Your project is ready.</p><button id="action" type="button">Try it</button><p id="status" aria-live="polite"></p></main><script src="app.js"></script></body></html>\n''',
        "styles.css": "*{box-sizing:border-box}body{margin:0;font-family:system-ui,sans-serif;background:#f6f7fb;color:#172033}main{max-width:720px;margin:10vh auto;padding:2rem;background:white;border-radius:1rem;box-shadow:0 8px 30px #0001}button{padding:.7rem 1rem;font:inherit;cursor:pointer}\n",
        "app.js": "const button=document.querySelector('#action');const status=document.querySelector('#status');button.addEventListener('click',()=>{status.textContent='Everything is wired correctly.';});\n",
    }

TEMPLATES = {"python": _python_files, "web": _web_files}


def plan(name: str, template: str = "python", author: str = "Radwan Abdulhadi Ahmed") -> dict[str, str]:
    name = validate_name(name)
    if template not in TEMPLATES:
        raise ValueError(f"unknown template: {template}")
    return TEMPLATES[template](name, author.strip() or "Unknown")


def scaffold(name: str, destination: Path | str = ".", template: str = "python", author: str = "Radwan Abdulhadi Ahmed", force: bool = False, dry_run: bool = False) -> ScaffoldResult:
    files = plan(name, template, author)
    base = Path(destination).expanduser().resolve()
    root = (base / validate_name(name)).resolve()
    if root.parent != base:
        raise ValueError("project path escapes destination")
    conflicts = [root / rel for rel in files if (root / rel).exists()]
    if conflicts and not force:
        raise FileExistsError("refusing to overwrite existing files: " + ", ".join(str(p) for p in conflicts[:5]))
    created = tuple(root / rel for rel in files)
    if dry_run:
        return ScaffoldResult(root, created)
    root.mkdir(parents=True, exist_ok=True)
    for rel, content in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
    return ScaffoldResult(root, created)
