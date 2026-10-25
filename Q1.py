"""
problem_solver.py - one-file Python toolkit for solving common problems.

Run:  python problem_solver.py
Or import functions:  from problem_solver import is_prime, bfs, lcs ...

Sections:
  1. Math & number theory
  2. Strings
  3. Searching & sorting
  4. Dynamic programming
  5. Graphs
  6. Data helpers
  7. Interactive menu
  8. Blank template for a NEW problem (see `solve`)
"""

import heapq
import math
import sys
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, permutations


# MATH 
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primes_upto(n: int) -> list:
    """Sieve of Eratosthenes."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, p in enumerate(sieve) if p]


def prime_factors(n: int) -> list:
    out, d = [], 2
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def gcd(a: int, b: int) -> int:
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b) if a and b else 0


def factorial(n: int) -> int:
    return math.factorial(n)


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_armstrong(n: int) -> bool:
    digits = str(n)
    return n == sum(int(d) ** len(digits) for d in digits)


def to_base(n: int, base: int) -> str:
    if n == 0:
        return "0"
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out = []
    while n:
        n, r = divmod(n, base)
        out.append(chars[r])
    return "".join(reversed(out))


# STRINGS 
def is_palindrome(s: str) -> bool:
    t = "".join(c.lower() for c in s if c.isalnum())
    return t == t[::-1]


def is_anagram(a: str, b: str) -> bool:
    clean = lambda s: Counter(c.lower() for c in s if c.isalnum())
    return clean(a) == clean(b)


def char_frequency(s: str) -> dict:
    return dict(Counter(s))


def longest_common_prefix(words: list) -> str:
    if not words:
        return ""
    p = words[0]
    for w in words[1:]:
        while not w.startswith(p):
            p = p[:-1]
    return p


def balanced_brackets(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack


#  SEARCH & SORT 
def binary_search(arr: list, target) -> int:
    """Returns index or -1. arr must be sorted."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    return out + left[i:] + right[j:]


def two_sum(nums: list, target: int):
    """Indices of two numbers adding to target, or None."""
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return seen[target - n], i
        seen[n] = i
    return None


def max_subarray(nums: list) -> int:
    """Kadane's algorithm."""
    best = cur = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        best = max(best, cur)
    return best


# DYNAMIC PROGRAMMING 
def lcs(a: str, b: str) -> int:
    """Longest common subsequence length."""
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def edit_distance(a: str, b: str) -> int:
    dp = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        prev, dp[0] = dp[0], i
        for j in range(1, len(b) + 1):
            cur = dp[j]
            dp[j] = prev if a[i - 1] == b[j - 1] else 1 + min(prev, dp[j], dp[j - 1])
            prev = cur
    return dp[-1]


def knapsack(weights: list, values: list, cap: int) -> int:
    dp = [0] * (cap + 1)
    for w, v in zip(weights, values):
        for c in range(cap, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[cap]


def coin_change(coins: list, amount: int) -> int:
    """Fewest coins to make amount, or -1."""
    dp = [0] + [math.inf] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return -1 if dp[amount] == math.inf else dp[amount]


# GRAPHS 
def bfs(graph: dict, start) -> list:
    seen, order, q = {start}, [], deque([start])
    while q:
        node = q.popleft()
        order.append(node)
        for nb in graph.get(node, []):
            if nb not in seen:
                seen.add(nb)
                q.append(nb)
    return order


def dfs(graph: dict, start) -> list:
    seen, order = set(), []

    def go(node):
        seen.add(node)
        order.append(node)
        for nb in graph.get(node, []):
            if nb not in seen:
                go(nb)

    go(start)
    return order


def dijkstra(graph: dict, start) -> dict:
    """graph = {node: [(neighbor, weight), ...]}"""
    dist = {start: 0}
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, math.inf):
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, math.inf):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


# DATA HELPERS 
def read_ints(prompt: str = "") -> list:
    return list(map(int, input(prompt).split()))


def stats(nums: list) -> dict:
    s = sorted(nums)
    n = len(s)
    mean = sum(s) / n
    median = s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
    mode = Counter(s).most_common(1)[0][0]
    var = sum((x - mean) ** 2 for x in s) / n
    return {"min": s[0], "max": s[-1], "mean": mean, "median": median,
            "mode": mode, "std_dev": math.sqrt(var)}


def all_subsets(items: list) -> list:
    return [list(c) for r in range(len(items) + 1) for c in combinations(items, r)]


def all_permutations(items: list) -> list:
    return [list(p) for p in permutations(items)]


# MENU 
def menu():
    options = {
        "1": ("Is prime?", lambda: print(is_prime(int(input("n: "))))),
        "2": ("Primes up to n", lambda: print(primes_upto(int(input("n: "))))),
        "3": ("Prime factors", lambda: print(prime_factors(int(input("n: "))))),
        "4": ("GCD / LCM", lambda: (lambda a, b: print("GCD", gcd(a, b), "LCM", lcm(a, b)))(*read_ints("a b: "))),
        "5": ("Fibonacci(n)", lambda: print(fibonacci(int(input("n: "))))),
        "6": ("Factorial(n)", lambda: print(factorial(int(input("n: "))))),
        "7": ("Palindrome?", lambda: print(is_palindrome(input("text: ")))),
        "8": ("Anagram?", lambda: print(is_anagram(input("a: "), input("b: ")))),
        "9": ("Balanced brackets?", lambda: print(balanced_brackets(input("text: ")))),
        "10": ("Sort numbers", lambda: print(merge_sort(read_ints("numbers: ")))),
        "11": ("Binary search", lambda: print(binary_search(sorted(read_ints("numbers: ")), int(input("target: "))))),
        "12": ("Two-sum", lambda: print(two_sum(read_ints("numbers: "), int(input("target: "))))),
        "13": ("Max subarray sum", lambda: print(max_subarray(read_ints("numbers: ")))),
        "14": ("Statistics", lambda: print(stats(read_ints("numbers: ")))),
        "15": ("LCS length", lambda: print(lcs(input("a: "), input("b: ")))),
        "16": ("Edit distance", lambda: print(edit_distance(input("a: "), input("b: ")))),
        "17": ("Coin change", lambda: print(coin_change(read_ints("coins: "), int(input("amount: "))))),
        "18": ("Convert to base", lambda: print(to_base(int(input("n: ")), int(input("base: "))))),
        "19": ("Run my solve() template", lambda: solve()),
    }
    while True:
        print("\n=== Problem Solver ===")
        for k, (name, _) in options.items():
            print(f"{k:>3}. {name}")
        print("  0. Exit")
        choice = input("Choose: ").strip()
        if choice == "0":
            break
        if choice in options:
            try:
                options[choice][1]()
            except Exception as e:
                print("Error:", e)
        else:
            print("Invalid choice.")


# TEMPLATE FOR A NEW PROBLEM 
def solve():
    """
    Steps for ANY new problem:
      1. Read input      2. Pick the right tool above (or write logic here)
      3. Compute         4. Print the answer
    Edit the body below; option 19 in the menu runs it.
    """
    data = read_ints("Enter numbers separated by spaces: ")
    result = sum(data)
    print("Answer:", result)


if __name__ == "__main__":
    menu()
