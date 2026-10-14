# # while loop
# # used to execute a set of statements until the condition is true
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# # break
# i = 0
# while i < 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# # continue
# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)

# while-else
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("while-else")


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. break, continue, and while-else - actually demonstrated (your file has
#    these commented out - here they're running so you see real behavior)
# -------------------------
print("break demo:")
i = 0
while i < 10:
    print(i)
    if i == 5:
        break            # exits the loop immediately once i == 5
    i += 1
# Output: 0 1 2 3 4 5 -> stops AFTER printing 5, never reaches 6-9

print(f"{'*' * 60}")

print("continue demo:")
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue          # skips the print() for this ONE iteration only
    print(i)
# Output: 1 2 3 4 6 7 8 9 10 -> 5 is the only value skipped, loop still runs fully

print(f"{'*' * 60}")

print("while-else WITH break (else is SKIPPED):")
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
else:
    print("This will NOT print - break occurred")
print("(confirmed: while-else skipped because of break)")
# Compare this to your ORIGINAL while-else example (no break) - the else DID
# run there. The presence of 'break' is the ONLY thing that skips 'else'.

print(f"{'*' * 60}")

# -------------------------
# 2. Classic while loop bug: forgetting to increment -> INFINITE loop
# -------------------------
"""
i = 0
while i < 10:
    print(i)
    # forgot i += 1 here!   -> this loop NEVER terminates, i stays 0 forever
    # In an interview, always double-check: does every code path through the
    # loop body actually move the loop TOWARD its exit condition?
"""

print(f"{'*' * 60}")

# -------------------------
# 3. while loop with a SENTINEL value - a very common real-world pattern
#    (reading input/data until a special "stop" value appears)
# -------------------------
data_stream = [10, 25, 30, -1, 40, 50]   # -1 acts as a SENTINEL meaning "stop"
idx = 0
while data_stream[idx] != -1:
    print("Processing:", data_stream[idx])
    idx += 1
print("Sentinel reached, stopping.")

print(f"{'*' * 60}")

# -------------------------
# 4. Simulating a do-while loop (Python has NO built-in do-while, unlike
#    C/Java - a common interview follow-up: "how would you simulate one?")
# -------------------------
# A do-while loop runs the body AT LEAST ONCE, checking the condition AFTER.
# Python's while loop checks the condition BEFORE the first run, so we
# simulate do-while using while True + a break at the end:
count = 0
while True:
    print("do-while style, iteration:", count)   # this body ALWAYS runs at least once
    count += 1
    if count >= 3:       # condition checked AFTER the body runs (like real do-while)
        break

print(f"{'*' * 60}")

# -------------------------
# 5. Nested while loops
# -------------------------
row = 0
while row < 3:
    col = 0
    while col < 3:
        print(f"({row},{col})", end=" ")
        col += 1
    print()   # newline after each row
    row += 1

print(f"{'*' * 60}")

# -------------------------
# 6. while with the walrus operator (:=) - assign AND test in the condition
#    itself (Python 3.8+), avoiding a common "duplicate initialization" pattern
# -------------------------
import random
random.seed(42)   # for reproducible output in this demo

# WITHOUT walrus - value has to be computed TWICE (once before the loop,
# once at the end of each iteration) to avoid duplicating logic:
value = random.randint(1, 5)
while value != 3:
    print("Got (no walrus):", value)
    value = random.randint(1, 5)   # duplicated call

random.seed(42)   # reset for a fair comparison
# WITH walrus - the assignment happens ONCE, right in the condition itself:
while (value := random.randint(1, 5)) != 3:
    print("Got (with walrus):", value)

print(f"{'*' * 60}")

# -------------------------
# 7. while loop for reading data until exhausted - a common real-world pattern
#    (e.g., reading a file, or paginated API results) using a sentinel/None check
# -------------------------
def get_next_item(items, index):
    """Simulates fetching the 'next' item, e.g. from a file or API page."""
    return items[index] if index < len(items) else None

items = ["a", "b", "c"]
index = 0
item = get_next_item(items, index)
while item is not None:
    print("Got item:", item)
    index += 1
    item = get_next_item(items, index)
print("No more items.")

print(f"{'*' * 60}")

# -------------------------
# 8. for vs while - when to choose each (a common "why not just always use
#    for" interview question)
# -------------------------
"""
Use a FOR loop when:
    - You're iterating over a KNOWN, FINITE collection/sequence
      (a list, string, range, dict, file object, etc.)
    - The number of iterations is determined by the DATA itself

Use a WHILE loop when:
    - The number of iterations is NOT known in advance
    - You're looping based on a CONDITION that may change unpredictably
      (e.g., "keep trying until successful", "keep reading until EOF",
      "keep polling until status changes")
    - You need a true "loop forever until explicitly told to stop" pattern
      (while True: ... break)
"""

print(f"{'*' * 60}")

# -------------------------
# 9. while loop condition is re-evaluated EVERY iteration - not cached
# -------------------------
class Countdown:
    def __init__(self, start):
        self.value = start
    def is_active(self):
        print("  (condition checked)")   # proves the condition function runs EVERY loop pass
        return self.value > 0

cd = Countdown(3)
while cd.is_active():
    print("Counting:", cd.value)
    cd.value -= 1
# Notice "(condition checked)" prints ONE MORE TIME than "Counting" lines -
# the condition is checked once more AFTER the last valid iteration, to
# discover the loop should now stop.


## ==========================================================
## INTERVIEW QUESTIONS ON THE WHILE LOOP
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is the fundamental difference in WHEN you'd choose a `while` loop
#    over a `for` loop? Give an example scenario where only a `while` loop
#    makes sense.
#
# 2. What is the most common cause of an accidental INFINITE while loop? How
#    would you review code to catch this bug before running it?
#
# 3. Does Python have a built-in `do-while` construct (like C or Java)? How
#    would you simulate "run the body at least once, then check the
#    condition" using a `while` loop?
#
# 4. What does the `else` clause on a `while` loop do? Under what specific
#    circumstance is it SKIPPED?
#
# 5. If a `while` loop's condition uses a function call (e.g.,
#    `while some_object.is_active():`), how many times is that function
#    actually called relative to the number of loop body executions?
#
# 6. What is a "sentinel value," and how would you use one to control when a
#    `while` loop should stop (e.g., reading values until a special marker is
#    found)?
#
# 7. How does the walrus operator (`:=`) help avoid duplicating an
#    initialization statement both BEFORE a while loop and at the END of its
#    body?
#
# 8. What's the difference between `break` and `continue` inside a `while`
#    loop, in terms of what happens to the loop's condition check afterward?
#
# 9. If you use `continue` inside a `while` loop, but forget to increment your
#    loop counter BEFORE the `continue` statement, what could go wrong?
#
# 10. How would you write a `while` loop that keeps prompting a user for
#     input until they provide a valid response (e.g., a number between 1 and
#     10)?
#
# 11. What's the risk of using a tight `while True:` polling loop (checking a
#     condition repeatedly with NO delay) in a real application? How would
#     you mitigate it?
#
# 12. Can a `while` loop's condition change based on something happening
#     INSIDE the loop body (as opposed to a simple counter)? Give an example.
#
# 13. What happens if a `while` loop's condition is `False` from the very
#     first check? Does the loop body run at all? Does the `else` clause
#     still run?
#
# 14. How would you write nested `while` loops to print a multiplication
#     table, and how would you track TWO separate counters correctly?
#
# 15. What's a real-world example of an appropriate use for `while True:`
#     combined with an internal `break` condition, rather than a `for` loop?
#
# 16. If you need to iterate over a data source of UNKNOWN length (e.g.,
#     reading from a network stream until it closes), why is `while` usually
#     more natural than `for`?
#
# 17. What does it mean that a `while` loop's condition is evaluated "lazily,"
#     right before each iteration, rather than being computed once upfront?
#
# 18. How would you convert a `for i in range(n):` loop into an equivalent
#     `while` loop? What extra bookkeeping does the `while` version require
#     that the `for` version handles automatically?
#
# 19. If an exception is raised inside a `while` loop's body (and not caught),
#     does the loop's `else` clause execute?
#
# 20. Why might overusing `while True:` with multiple scattered `break`
#     statements throughout the loop body make code harder to reason about,
#     compared to expressing the same logic with a clear condition in the
#     `while` statement itself?