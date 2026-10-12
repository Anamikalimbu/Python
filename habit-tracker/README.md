# Habit Tracker

A small command-line habit tracker written in pure Python (standard library only). Check in each day and watch your streaks grow.

## Features

- Check in a habit once per day (repeat check-ins are ignored)
- Current streak and best streak per habit
- Data stored in a simple JSON file (`~/.habit_tracker.json` by default)
- Unit tests with `pytest`

## Usage

```bash
python -m habit_tracker done "Study Python"
python -m habit_tracker done "Exercise"
python -m habit_tracker list
python -m habit_tracker remove "Exercise"
```

Use a custom data file with `--file`:

```bash
python -m habit_tracker --file my_habits.json list
```

Example output:

```
Habit               Today   Streak  Best
Study Python        yes     4       7
```

## Project structure

```
habit_tracker/
  __init__.py
  __main__.py     # python -m habit_tracker
  cli.py          # argparse commands
  storage.py      # JSON load/save
  tracker.py      # check-in + streak logic
tests/
  test_habit_tracker.py
```

## Run the tests

```bash
pip install pytest
pytest
```

## Ideas to extend

- Weekly goals and reminders
- Export to CSV
- A simple chart of check-ins with matplotlib
