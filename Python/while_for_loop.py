## while loop:

a = 1
while a <= 10:
    print(a)
    a += 1

## for loop:

l = ["a", "b", "c", "d"]
for i in l:
    print(i)

# # break
# for i in l:
#     if i == 3:
#         break
#     print(i)

# # continue
# for i in l:
#     if i == 2:
#         continue
#     print(i)

# for-else loop, else will execute after for

# for i in l:
#     print(i)
# else:
#     print("For else")

# # if we use break in for loop else will not execute
# for i in l:
#     if i == 3:
#         break
#     print(i)
# else:
#     print("for else")

# # for-else with continue
# for i in l:
#     if i == 3:
#         continue
#     print(i)
# else:
#     print("for-else")

# range()
for i in range(10):
    print(i)

## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. break and continue - actually demonstrated (your file has these commented
#    out, and with a bug - i == 3 never matches since l holds strings, not ints)
# -------------------------
l = ["a", "b", "c", "d"]

print("break demo:")
for i in l:
    if i == "c":       # fixed: comparing against the STRING "c", matching l's actual contents
        break
    print(i)             # a, b -> stops BEFORE printing 'c'

print("continue demo:")
for i in l:
    if i == "b":
        continue           # skips ONLY this iteration, loop continues
    print(i)                 # a, c, d -> 'b' is skipped, but loop doesn't stop

print(f"{'*' * 60}")

# -------------------------
# 2. for-else and while-else - a Python-specific feature many candidates have
#    never used correctly (your file's examples are commented out - here they
#    are actually running so you can see the real behavior)
# -------------------------
print("for-else with NO break:")
for i in l:
    print(i)
else:
    print("For-else: loop completed normally")   # ALWAYS runs if the loop finishes without 'break'

print(f"{'*' * 60}")

print("for-else WITH break:")
for i in l:
    if i == "c":
        break
    print(i)
else:
    print("This will NOT print")   # SKIPPED entirely, because 'break' occurred
print("(nothing printed after the loop above, confirming else was skipped)")

print(f"{'*' * 60}")

print("for-else WITH continue (but no break):")
for i in l:
    if i == "c":
        continue
    print(i)
else:
    print("for-else: STILL runs, because continue is not break")   # continue does NOT prevent else!

# KEY RULE: the `else` block on a loop runs if the loop completes WITHOUT
# hitting `break`. `continue` has NO effect on whether `else` runs - only
# `break` (or an exception) can skip the `else` block.

print(f"{'*' * 60}")

# -------------------------
# 3. Real-world use case for for-else: searching, without a "found" flag variable
# -------------------------
def find_first_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            print(f"Found even number: {n}")
            break
    else:
        print("No even number found")   # runs only if we never found one (no break)

find_first_even([1, 3, 5, 7])     # No even number found
find_first_even([1, 3, 4, 7])       # Found even number: 4

# WITHOUT for-else, this pattern usually needs an extra boolean flag:
def find_first_even_without_else(numbers):
    found = False
    for n in numbers:
        if n % 2 == 0:
            print(f"Found even number: {n}")
            found = True
            break
    if not found:
        print("No even number found")

print(f"{'*' * 60}")

# -------------------------
# 4. while-else works the SAME way as for-else
# -------------------------
count = 0
while count < 3:
    print("while iteration:", count)
    count += 1
else:
    print("while-else: loop finished normally (no break)")

count2 = 0
while count2 < 3:
    if count2 == 1:
        break
    print("while iteration (with break):", count2)
    count2 += 1
else:
    print("This will NOT print - break occurred")
print("(confirmed: while-else skipped after break)")

print(f"{'*' * 60}")

# -------------------------
# 5. enumerate() in loops - getting BOTH index and value cleanly (very common,
#    and missing from this file entirely)
# -------------------------
for index, value in enumerate(l):
    print(index, value)

for index, value in enumerate(l, start=1):    # can start counting from a custom number
    print(index, value)

print(f"{'*' * 60}")

# -------------------------
# 6. Looping with zip() - iterating MULTIPLE sequences in parallel
# -------------------------
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

print(f"{'*' * 60}")

# -------------------------
# 7. Nested loops and labeled-break workarounds (Python has NO 'break label',
#    unlike Java/C - this is a common interview follow-up)
# -------------------------
# Python does NOT support breaking out of multiple nested loops directly with
# a single break statement. Common workarounds:

# Workaround 1: use a flag variable
found = False
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            found = True
            break
    if found:
        break
print(f"Workaround 1 stopped at i={i}, j={j}")

# Workaround 2: wrap the nested loops in a function and use `return`
def search_nested():
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                return i, j    # immediately exits BOTH loops via return
    return None

print("Workaround 2 (function+return):", search_nested())

# Workaround 3: use itertools.product to FLATTEN the nested loop into one
import itertools
for i, j in itertools.product(range(3), range(3)):
    if i == 1 and j == 1:
        print(f"Workaround 3 (itertools.product) stopped at i={i}, j={j}")
        break

print(f"{'*' * 60}")

# -------------------------
# 8. Iterating and modifying a list AT THE SAME TIME - a classic bug source
# -------------------------
nums = [2, 4, 6, 8, 10]
# BUGGY: removing items while iterating over the SAME list skips elements!
for n in nums:
    if n % 2 == 0:
        nums.remove(n)   # mutating the list you're currently iterating over -
                            # indices shift underneath you, some elements get SKIPPED
print("Buggy result (notice 4 and 8 were skipped!):", nums)   # [4, 8] -> BUG! only removed every OTHER even number

# CORRECT: iterate over a COPY, or build a new list instead
nums2 = [2, 4, 6, 8, 10]
for n in nums2[:]:          # nums2[:] creates a shallow copy to iterate safely
    if n % 2 == 0:
        nums2.remove(n)
print("Fixed with a copy:", nums2)   # [] -> correct, all evens removed

nums3 = [2, 4, 6, 8, 10]
nums3 = [n for n in nums3 if n % 2 != 0]   # even better - build a NEW list instead of mutating
print("Fixed with list comprehension:", nums3)   # [] -> correct

print(f"{'*' * 60}")

# -------------------------
# 9. range() in depth - start, stop, step, and negative steps
# -------------------------
print(list(range(5)))          # [0, 1, 2, 3, 4] -> stop only (starts at 0 by default)
print(list(range(2, 8)))         # [2, 3, 4, 5, 6, 7] -> start, stop
print(list(range(0, 10, 2)))       # [0, 2, 4, 6, 8] -> start, stop, step
print(list(range(10, 0, -2)))        # [10, 8, 6, 4, 2] -> negative step, counts DOWN
print(list(range(5, 5)))               # [] -> empty, start equals stop

print(f"{'*' * 60}")

# -------------------------
# 10. pass vs continue vs break - a quick clarifying comparison (commonly
#     confused by less experienced candidates)
# -------------------------
"""
pass       -> does NOTHING - just a placeholder/no-op, loop continues normally
              (used when syntax REQUIRES a statement, but you have nothing to do yet)
continue   -> skips the REST of the current iteration, moves to the NEXT one
break      -> EXITS the loop entirely, no further iterations at all
"""
for i in range(5):
    if i == 2:
        pass          # does nothing special - execution just continues to the print() below
    print(f"pass demo: {i}")   # 0, 1, 2, 3, 4 -> ALL printed, pass has no effect on flow

print(f"{'*' * 60}")

# -------------------------
# 11. Infinite loop patterns beyond input() - common real-world uses
# -------------------------
"""
# Polling pattern - keep checking a condition until it's met
import time
while True:
    status = check_some_status()   # e.g. checking if a job finished
    if status == "done":
        break
    time.sleep(1)   # wait before checking again, avoid a tight busy-loop

# Event loop pattern (simplified) - servers often run something like this:
while True:
    request = get_next_request()   # blocks until a request arrives
    handle(request)
"""

## Infinite loops:
# break: will terminate the loop
# continue will skip the current iteration of loop

# while True:
#     print("Infinite")

while True:
    item = int(input("Enter number: "))
    if item == 3:
        break


## ==========================================================
## INTERVIEW QUESTIONS ON WHILE/FOR LOOPS, BREAK, CONTINUE, ELSE
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is the difference between `break` and `continue`? Give an example
#    where using the wrong one would produce a completely different result.
#
# 2. What does the `else` clause on a `for` or `while` loop actually do? Under
#    what specific condition does it get SKIPPED?
#
# 3. Does using `continue` inside a loop prevent its `else` clause from
#    running? Why or why not?
#
# 4. What is a practical, real-world use case for `for-else` that avoids
#    needing a separate boolean "found" flag variable?
#
# 5. Why is it dangerous to call `list.remove()` on a list while iterating
#    over that SAME list directly in a `for` loop? What actually goes wrong
#    internally (hint: think about how indices shift)?
#
# 6. What are two different ways to safely remove items from a list while
#    iterating over it, without skipping elements?
#
# 7. Does Python support breaking out of multiple nested loops with a single
#    `break` statement (like a labeled break in Java)? What are common
#    workarounds?
#
# 8. What is the difference between `pass`, `continue`, and `break`? In what
#    situation would you specifically need `pass` rather than just leaving
#    the block empty?
#
# 9. What does `range(start, stop, step)` do when `step` is negative? What
#    happens if `start` equals `stop`?
#
# 10. How would you iterate over two lists in PARALLEL (getting corresponding
#     elements from each at the same time) without using manual indexing?
#
# 11. What does `enumerate(iterable, start=1)` do differently from
#     `enumerate(iterable)`?
#
# 12. Why does a `while True:` loop need an explicit `break` (or a `return`)
#     to ever terminate? What real-world patterns commonly use `while True:`
#     intentionally (e.g., polling, event loops)?
#
# 13. If a `for` loop's iterable is empty (e.g., an empty list), does its
#     `else` clause still run?
#
# 14. What's the difference between iterating with `for item in my_list:`
#     versus `for i in range(len(my_list)): item = my_list[i]`? Which is
#     considered more "Pythonic," and why?
#
# 15. How would you modify a list's elements (transforming values) WHILE
#     iterating, without running into the same bug as removing elements
#     mid-iteration?
#
# 16. What is `itertools.product()`, and how can it help "flatten" nested
#     loops into a single loop structure?
#
# 17. Can the `else` clause on a loop be triggered by something OTHER than
#     the loop completing without a `break`? (Hint: think about exceptions
#     raised inside the loop body.)
#
# 18. Why might using a `while` loop with a manually incremented counter
#     (`i = 0; while i < n: ...; i += 1`) be more error-prone than using a
#     `for i in range(n):` loop for the same task?
#
# 19. What happens if you write `break` OUTSIDE of any loop (e.g., directly in
#     a function body with no enclosing for/while)? At what point is this
#     error caught?
#
# 20. Given the busy-polling pattern (`while True: check_status(); ...`), why
#     is it usually important to include a `time.sleep()` inside the loop
#     rather than checking as fast as possible in a tight loop?