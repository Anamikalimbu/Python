"""Command-line interface for the habit tracker."""
import argparse
from datetime import date

from . import storage, tracker


def build_parser():
    p = argparse.ArgumentParser(prog="habit", description="Simple habit tracker with streaks.")
    p.add_argument("--file", default=str(storage.DEFAULT_PATH), help="Path to the data file")
    sub = p.add_subparsers(dest="command", required=True)

    add = sub.add_parser("done", help="Check in a habit for today")
    add.add_argument("habit")

    rm = sub.add_parser("remove", help="Delete a habit")
    rm.add_argument("habit")

    sub.add_parser("list", help="Show all habits and streaks")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    data = storage.load(args.file)

    if args.command == "done":
        if tracker.check_in(data, args.habit):
            storage.save(data, args.file)
            streak = tracker.current_streak(data[args.habit])
            print(f"Checked in '{args.habit}'. Current streak: {streak} day(s).")
        else:
            print(f"'{args.habit}' is already checked in for today.")
    elif args.command == "remove":
        if tracker.remove_habit(data, args.habit):
            storage.save(data, args.file)
            print(f"Removed '{args.habit}'.")
        else:
            print(f"No habit named '{args.habit}'.")
    elif args.command == "list":
        if not data:
            print("No habits yet. Try: python -m habit_tracker done \"Study\"")
            return 0
        today = date.today().isoformat()
        print(f"{'Habit':<20}{'Today':<8}{'Streak':<8}{'Best':<6}")
        for name, days in sorted(data.items()):
            mark = "yes" if today in days else "no"
            print(f"{name:<20}{mark:<8}{tracker.current_streak(days):<8}{tracker.longest_streak(days):<6}")
    return 0
