import json
from project_scaffolder.cli import main


def test_list_templates(capsys):
    assert main(["--list-templates"]) == 0
    out = capsys.readouterr().out
    assert "python" in out and "web" in out


def test_dry_run_json(tmp_path, capsys):
    assert main(["demo", "-d", str(tmp_path), "--dry-run", "--json"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["dry_run"] is True
    assert payload["template"] == "python"
    assert not (tmp_path / "demo").exists()


def test_invalid_name_returns_two(capsys):
    assert main(["../bad"]) == 2
    assert "error:" in capsys.readouterr().err
