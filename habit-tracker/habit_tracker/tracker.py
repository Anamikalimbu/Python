"""Core habit logic: check-ins and streak calculation."""
from datetime import date, timedelta


def check_in(data, habit, day=None):
    """Record a check-in. Returns True if added, False if already recorded."""
    day = (day or date.today()).isoformat()
    days = data.setdefault(habit, [])
    if day in days:
        return False
    days.append(day)
    days.sort()
    return True


def remove_habit(data, habit):
    return data.pop(habit, None) is not None


def current_streak(days, today=None):
    """Consecutive days ending today (or yesterday, so the streak isn't lost mid-day)."""
    today = today or date.today()
    done = {date.fromisoformat(d) for d in days}
    cursor = today if today in done else today - timedelta(days=1)
    streak = 0
    while cursor in done:
        streak += 1
        cursor -= timedelta(days=1)
    return streak


def longest_streak(days):
    best = run = 0
    prev = None
    for d in sorted(date.fromisoformat(x) for x in set(days)):
        run = run + 1 if prev and d - prev == timedelta(days=1) else 1
        best = max(best, run)
        prev = d
    return best
