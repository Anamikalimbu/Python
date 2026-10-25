# 30-Day Python Challenge (No AI)

## Rules
1. Try each question for at least 20 minutes before looking anything up.
2. Allowed help: docs.python.org, your class notes, your own old code. Not allowed: AI, copy-pasted solutions.
3. Write the logic on paper (steps or pseudocode) before typing.
4. Test each solution with at least 3 inputs, including an edge case (0, empty, negative).
5. Save one file per question (day01_q1.py ...) and push to GitHub daily.
6. If stuck after 45 minutes, write down exactly where you are stuck, take a break, and come back. Look at hints only as a last resort.
7. Every 7th day is a review day plus a mini project.

---

## WEEK 1: Basics, Conditions, Loops

### Day 1: Input, Output, Variables
1. Take name, age, city as input and print a formatted sentence using an f-string.
2. Swap two numbers without using a third variable.
3. Take length and width, print area and perimeter of a rectangle.
4. (Bonus) Convert Celsius to Fahrenheit and Kelvin.

### Day 2: Operators and Arithmetic
1. Simple interest calculator (principal, rate, time).
2. Convert total seconds into hours, minutes, seconds.
3. Take a 3-digit number and print the sum of its digits using only arithmetic (// and %).
4. (Bonus) Take two numbers and print quotient, remainder, and power.

### Day 3: Conditionals
1. Check whether a number is positive, negative, or zero.
2. Find the largest of three numbers without using max().
3. Check if a year is a leap year.
4. Grade calculator: marks to A/B/C/D/F.

### Day 4: Conditionals 2
1. Classify a triangle (equilateral, isosceles, scalene) from three sides, and check validity first.
2. BMI calculator with category (underweight, normal, overweight, obese).
3. Simple calculator using if/elif for + - * / (handle division by zero).
4. ATM PIN check: 3 attempts allowed, then "card blocked".

### Day 5: for Loops
1. Sum of numbers from 1 to n.
2. Print the multiplication table of any number up to 10.
3. Factorial of n using a loop.
4. Count the digits of a number.

### Day 6: while Loops
1. Reverse a number (1234 becomes 4321).
2. Check if a number is a palindrome.
3. Check if a number is an Armstrong number.
4. GCD and LCM of two numbers.

### Day 7: Patterns + Review + Mini Project
1. Print a right-angled triangle of stars.
2. Print a centered pyramid.
3. Print a diamond.
4. **Mini project:** Number guessing game (random number 1-100, hints "higher/lower", count attempts).

---

## WEEK 2: Strings, Lists, Tuples, Sets, Dictionaries

### Day 8: Strings
1. Count vowels and consonants in a string.
2. Check if a string is a palindrome (ignore case and spaces).
3. Capitalize the first letter of every word without using .title().
4. (Bonus) Find the longest word in a sentence.

### Day 9: Strings 2
1. Check if two strings are anagrams.
2. Remove duplicate characters, keeping the original order.
3. Count the frequency of each character.
4. Compress a string: "aaabbc" becomes "a3b2c1".

### Day 10: Lists
1. Find the second largest number in a list (no sorting shortcut allowed first, then try with sorted()).
2. Remove duplicates from a list.
3. Rotate a list by k positions.
4. Merge two sorted lists into one sorted list.

### Day 11: Lists 2
1. Two Sum: find a pair that adds to a target (brute force first).
2. Find the missing number in a list containing 1..n.
3. Move all zeros to the end, keeping the order of the others.
4. Use list comprehensions: squares of even numbers, and words longer than 4 letters.

### Day 12: Tuples and Sets
1. Given two lists, find common, unique, and symmetric-difference elements using sets.
2. Sort a list of tuples by the second element.
3. Check if a list has duplicates using a set.
4. Unpack a tuple of (name, age, marks) and print it neatly.

### Day 13: Dictionaries
1. Word frequency counter for a sentence.
2. Invert a dictionary (keys become values).
3. Merge two dictionaries, summing values for common keys.
4. Group words by their first letter.

### Day 14: Review + Mini Project
1. Find the most frequent element in a list.
2. Flatten a nested list ([1,[2,3],[4,[5]]] becomes [1,2,3,4,5]).
3. Transpose a matrix (list of lists).
4. **Mini project:** Student marks manager (dictionary): add student, update marks, show average, show topper.

---

## WEEK 3: Functions, Recursion, Sorting, Files, Errors

### Day 15: Functions
1. is_prime(n) function.
2. Print all primes in a range.
3. Function using *args that returns the sum and average.
4. Function with default and keyword arguments (greet(name, greeting="Hello")).

### Day 16: Functional Tools
1. Sort a list of dictionaries by a key using lambda.
2. Use map() to convert a list of strings to ints.
3. Use filter() to keep only prime numbers from a list.
4. Use reduce() to find the product of a list.

### Day 17: Recursion
1. Factorial using recursion.
2. Fibonacci using recursion, then add memoization with a dictionary.
3. Sum of digits using recursion.
4. Power function x^n using recursion.

### Day 18: Sorting and Searching
1. Implement bubble sort.
2. Implement selection sort.
3. Implement insertion sort.
4. Implement binary search (iterative), then recursive.

### Day 19: File Handling
1. Read a text file and count lines, words, characters.
2. Write user input into a file, then append more lines.
3. Read a CSV of marks and print each student's average.
4. Copy a file's content into a new file with lines reversed.

### Day 20: Exception Handling
1. Safe division: handle ZeroDivisionError and ValueError.
2. Keep asking for an integer until the user enters a valid one.
3. Create a custom exception InvalidAgeError and raise it for age < 0 or > 120.
4. Read a file that may not exist, using try/except/finally.

### Day 21: Review + Mini Project
1. Check if brackets are balanced in a string ("{[()]}" is valid).
2. Find the longest word in a text file.
3. Print the first n Fibonacci numbers using a generator-style loop.
4. **Mini project:** Expense tracker (add, list, total by category) that saves to a JSON file.

---

## WEEK 4: OOP, Data Structures, Advanced Python, Capstone

### Day 22: Classes and Objects
1. Rectangle class with area() and perimeter().
2. BankAccount class with deposit, withdraw, balance (no overdraft).
3. Student class with __init__ and __str__.
4. Create 3 objects and keep them in a list; print the topper.

### Day 23: Inheritance and Polymorphism
1. Shape parent class with Circle and Rectangle children overriding area().
2. Animal / Dog / Cat with an overridden speak().
3. Use @classmethod and @staticmethod in a class (e.g., a Date helper).
4. Encapsulation: private attribute with getter/setter using @property.

### Day 24: Dunder Methods and Composition
1. Vector class with __add__, __sub__, __str__, __eq__.
2. Library class that holds Book objects (add, remove, search).
3. Implement a Stack class (push, pop, peek, is_empty).
4. Implement a Queue class using collections.deque.

### Day 25: Data Structures
1. Build a singly linked list (insert at head/tail, delete, print).
2. Reverse a linked list.
3. Evaluate a postfix expression using a stack.
4. Binary tree: insert nodes and do inorder traversal.

### Day 26: Generators, Iterators, Decorators
1. Generator that yields Fibonacci numbers forever; take the first 10.
2. Custom iterator class that counts down from n.
3. Write a @timer decorator that prints function run time.
4. Write a context manager (with statement) that opens and closes a file.

### Day 27: Algorithm Practice
1. Maximum sum of k consecutive elements (sliding window).
2. Check if a sorted list has a pair summing to target (two pointers).
3. Pascal's triangle up to n rows.
4. Rotate a matrix 90 degrees.

### Day 28: Standard Library
1. Use collections.Counter to find the top 3 most common words in a file.
2. Calculate someone's exact age in years, months, days using datetime.
3. Random password generator (length, with letters, digits, symbols).
4. Validate an email address and a phone number using the re module.

### Day 29: Interview-Style Problems
1. Longest substring without repeating characters.
2. Longest common prefix of a list of strings.
3. Convert Roman numerals to integer.
4. Merge overlapping intervals.

### Day 30: Capstone
Pick ONE project: Library Management CLI, Quiz Game, or To-Do Manager.
1. Build it using classes, file/JSON storage, and exception handling.
2. Write at least 5 tests for it using unittest.
3. Write a README: what it does, how to run it, what you learned in 30 days.

---

## Daily Routine (suggested ~1.5 to 2 hours)
- 10 min: read the day's topic in docs or your notes
- 60-90 min: solve the questions
- 10 min: clean up code (good names, comments) and push to GitHub
- 5 min: write 2 lines in a journal: what was hard, what you learned

## Weekly Checkpoint
At the end of each week, redo one question from memory, with no looking at your old code. If you can't, revisit that topic.
