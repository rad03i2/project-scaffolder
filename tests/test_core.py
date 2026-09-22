from pathlib import Path
import pytest
from project_scaffolder import plan, scaffold, validate_name


def test_validate_name():
    assert validate_name("my-app") == "my-app"
    for bad in ("../oops", "two words", "", "/tmp/x", "9starts"):
        with pytest.raises(ValueError):
            validate_name(bad)


def test_python_plan_is_real_project():
    files = plan("hello-world", "python", "Example Author")
    assert "src/hello_world/__main__.py" in files
    assert "tests/test_smoke.py" in files
    assert 'name = "hello-world"' in files["pyproject.toml"]


def test_web_plan_has_accessible_foundation():
    files = plan("hello-web", "web")
    assert '<meta name="viewport"' in files["index.html"]
    assert 'aria-live="polite"' in files["index.html"]
    assert "addEventListener" in files["app.js"]


def test_scaffold_writes_and_refuses_overwrite(tmp_path: Path):
    result = scaffold("sample", tmp_path)
    assert result.root == tmp_path / "sample"
    assert (result.root / "src/sample/__init__.py").is_file()
    with pytest.raises(FileExistsError):
        scaffold("sample", tmp_path)


def test_force_preserves_unmanaged_file(tmp_path: Path):
    root = tmp_path / "sample"
    root.mkdir()
    extra = root / "notes.txt"
    extra.write_text("keep", encoding="utf-8")
    scaffold("sample", tmp_path, force=True)
    assert extra.read_text(encoding="utf-8") == "keep"


def test_dry_run_does_not_write(tmp_path: Path):
    result = scaffold("sample", tmp_path, dry_run=True)
    assert result.created
    assert not result.root.exists()
