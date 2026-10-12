"""JSON file storage for the habit tracker."""
import json
from pathlib import Path

DEFAULT_PATH = Path.home() / ".habit_tracker.json"


def load(path=DEFAULT_PATH):
    """Return {habit_name: [ISO date strings]}."""
    path = Path(path)
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save(data, path=DEFAULT_PATH):
    Path(path).write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
