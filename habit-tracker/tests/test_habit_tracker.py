from datetime import date, timedelta

from habit_tracker import cli, storage, tracker

TODAY = date(2026, 10, 12)


def d(offset):
    return (TODAY - timedelta(days=offset)).isoformat()


def test_check_in_is_idempotent():
    data = {}
    assert tracker.check_in(data, "Study", TODAY) is True
    assert tracker.check_in(data, "Study", TODAY) is False
    assert data["Study"] == [TODAY.isoformat()]


def test_current_streak_counts_consecutive_days():
    assert tracker.current_streak([d(0), d(1), d(2)], TODAY) == 3


def test_streak_survives_until_end_of_today():
    assert tracker.current_streak([d(1), d(2)], TODAY) == 2


def test_streak_breaks_after_gap():
    assert tracker.current_streak([d(2), d(3)], TODAY) == 0


def test_longest_streak():
    assert tracker.longest_streak([d(10), d(9), d(8), d(5), d(4)]) == 3
    assert tracker.longest_streak([]) == 0


def test_remove_habit():
    data = {"Gym": [d(0)]}
    assert tracker.remove_habit(data, "Gym") is True
    assert tracker.remove_habit(data, "Gym") is False


def test_storage_roundtrip(tmp_path):
    path = tmp_path / "h.json"
    assert storage.load(path) == {}
    storage.save({"Read": [d(0)]}, path)
    assert storage.load(path) == {"Read": [d(0)]}


def test_storage_handles_corrupt_file(tmp_path):
    path = tmp_path / "h.json"
    path.write_text("not json")
    assert storage.load(path) == {}


def test_cli_done_and_list(tmp_path, capsys):
    f = str(tmp_path / "h.json")
    assert cli.main(["--file", f, "done", "Python"]) == 0
    assert cli.main(["--file", f, "done", "Python"]) == 0
    assert cli.main(["--file", f, "list"]) == 0
    out = capsys.readouterr().out
    assert "Current streak: 1" in out
    assert "already checked in" in out
    assert "Python" in out
