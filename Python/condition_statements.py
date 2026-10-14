# if condition:
a, b = 10, 20
if a < b:
    print("true")

# if-else condition
a, b = 10, 20
if a > b:
    print("true")
else:
    print("false")

# if-elif-else condition
a, b = 10, 20
if a > b:
    print("if")
elif a == b:
    print("elif")
else:
    print("else")


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. Nested if statements
# -------------------------
age = 25
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry denied")

print(f"{'*' * 50}")

# -------------------------
# 2. Ternary / conditional expression (if-else in a single line)
# -------------------------
a, b = 10, 20
result = "a is bigger" if a > b else "b is bigger or equal"
print(result)   # b is bigger or equal

# nested ternary (use sparingly - hurts readability if overused)
x = 5
category = "positive" if x > 0 else "negative" if x < 0 else "zero"
print(category)   # positive

print(f"{'*' * 50}")

# -------------------------
# 3. Chained comparisons - Pythonic shortcut (already touched in boolean notes)
# -------------------------
x = 15
if 10 < x < 20:          # equivalent to: 10 < x and x < 20
    print("x is between 10 and 20")

print(f"{'*' * 50}")

# -------------------------
# 4. Using truthy/falsy values directly in conditions (no need for == True/False)
# -------------------------
items = [1, 2, 3]
if items:               # Pythonic - checks non-empty, not `if len(items) > 0:`
    print("List has items")

name = ""
if not name:             # Pythonic empty-string check
    print("Name is empty")

value = None
if value is None:         # ALWAYS use 'is' for None comparisons, not ==
    print("Value is None")

print(f"{'*' * 50}")

# -------------------------
# 5. Logical operators (and, or, not) combining multiple conditions
# -------------------------
age = 25
has_ticket = True
if age >= 18 and has_ticket:
    print("Can enter the concert")

is_weekend = False
is_holiday = True
if is_weekend or is_holiday:
    print("No work today")

print(f"{'*' * 50}")

# -------------------------
# 6. Membership (in / not in) inside conditions - very common in real code
# -------------------------
allowed_roles = ["admin", "editor"]
role = "editor"
if role in allowed_roles:
    print("Access granted")

banned_words = ["spam", "scam"]
message = "hello world"
if not any(word in message for word in banned_words):
    print("Message is clean")

print(f"{'*' * 50}")

# -------------------------
# 7. Guard clauses - early return pattern to avoid deep nesting (common in real
#    codebases and interview "clean code" questions)
# -------------------------
def process_order(order):
    if order is None:
        return "No order provided"
    if not order.get("items"):
        return "Order has no items"
    if order.get("total", 0) <= 0:
        return "Invalid order total"
    # main logic only runs once all guard checks pass - avoids nested if/else pyramids
    return "Order processed"

print(process_order(None))                                  # No order provided
print(process_order({"items": [], "total": 0}))               # Order has no items
print(process_order({"items": ["item1"], "total": 50}))        # Order processed

print(f"{'*' * 50}")

# -------------------------
# 8. Walrus operator (:=) inside an if condition (Python 3.8+)
# -------------------------
import re
text = "order id: 12345"
if (match := re.search(r"\d+", text)):
    print("Found number:", match.group())   # assigns AND Test_Cases in one expression

# without walrus, you'd need two lines:
match2 = re.search(r"\d+", text)
if match2:
    print("Found number (old way):", match2.group())

print(f"{'*' * 50}")

# -------------------------
# 9. match-case: structural pattern matching (Python 3.10+) - modern alternative
#    to long if-elif-else chains, similar to switch/case in other languages
# -------------------------
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:                      # '_' is the wildcard/default case
            return "Unknown status"

print(http_status(200))   # OK
print(http_status(999))   # Unknown status

# match-case can also match on structure/type, not just values (more powerful
# than a plain switch statement)
def describe(item):
    match item:
        case int() | float():
            return "It's a number"
        case str():
            return "It's a string"
        case [x, y]:                  # matches a list/sequence of exactly 2 elements
            return f"A pair: {x}, {y}"
        case {"name": name}:            # matches a dict with a 'name' key
            return f"Has a name: {name}"
        case _:
            return "Unknown type"

print(describe(42))              # It's a number
print(describe("hi"))             # It's a string
print(describe([1, 2]))            # A pair: 1, 2
print(describe({"name": "Bob"}))    # Has a name: Bob

print(f"{'*' * 50}")

# -------------------------
# 10. Dictionary dispatch as an alternative to long elif chains (common
#     "senior-level" refactoring answer)
# -------------------------
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b

operations = {
    "+": add,
    "-": sub,
    "*": mul,
}

op = "+"
if op in operations:
    print(operations[op](5, 3))   # 8 -> avoids a long if/elif chain checking each operator

print(f"{'*' * 50}")

# -------------------------
# 11. Common gotchas and mistakes
# -------------------------
# GOTCHA 1: using '=' (assignment) instead of '==' (comparison) - Python actually
# raises a SyntaxError for this in an if condition (unlike C), so this specific
# bug is caught early:
# if a = 5:   # SyntaxError: invalid syntax (Python protects you here!)

# GOTCHA 2: comparing floats for equality directly
price = 0.1 + 0.2
if price == 0.3:              # False! floating point precision issue
    print("Exact match")
else:
    print("Not an exact match due to float precision")   # this runs

# GOTCHA 3: mixing up 'is' and '==' for value comparison
a = [1, 2, 3]
b = [1, 2, 3]
if a == b:
    print("Equal values")     # True -> compares VALUES
if a is b:
    print("Same object")       # False -> different objects in memory, doesn't print

# GOTCHA 4: an empty if body (needs 'pass' as a placeholder, or code fails to parse)
flag = True
if flag:
    pass   # placeholder - TODO: implement later
else:
    print("flag is False")

# GOTCHA 5: elif vs separate if statements - elif short-circuits (only ONE
# branch runs), separate ifs are evaluated INDEPENDENTLY
x = 10
if x > 5:
    print("greater than 5")     # this runs
if x > 8:
    print("greater than 8")     # this ALSO runs - independent check, not elif!
# vs:
if x > 5:
    print("elif chain: greater than 5")
elif x > 8:
    print("elif chain: greater than 8")   # never reached - first condition already matched


## ==========================================================
## INTERVIEW QUESTIONS ON CONDITIONAL STATEMENTS
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is the difference between using multiple separate `if` statements
#    versus an `if-elif-else` chain? When would you choose one over the other?
#
# 2. What is a ternary (conditional) expression in Python? When does it improve
#    readability, and when does it hurt it?
#
# 3. Why does Python raise a SyntaxError if you accidentally write `if a = 5:`
#    instead of `if a == 5:`? How is this different from languages like C?
#
# 4. What is a "guard clause," and how does using early returns help avoid
#    deeply nested if-else blocks?
#
# 5. Why should you use `is None` instead of `== None` when checking for None?
#
# 6. What are truthy and falsy values, and how can you leverage them to
#    simplify a condition like `if len(my_list) > 0:`?
#
# 7. What is chained comparison (e.g., `10 < x < 20`)? How is it evaluated
#    internally, and is it equivalent to `10 < x and x < 20`?
#
# 8. What is the walrus operator (:=), and how can it simplify a conditional
#    that both assigns and checks a value (e.g., with regex matches)?
#
# 9. What is structural pattern matching (match-case), introduced in Python
#    3.10? How is it different from a simple switch/case statement in other
#    languages (e.g., can it match on structure/type)?
#
# 10. How would you refactor a long if-elif-else chain that dispatches based on
#     a string or enum value into something more maintainable?
#
# 11. Why might comparing two floating-point numbers with `==` inside an if
#     condition lead to unexpected/buggy behavior?
#
# 12. What is the difference between `if a == b:` and `if a is b:` when a and b
#     are both lists with the same values?
#
# 13. What does the wildcard pattern `case _:` do in a match statement, and
#     what happens if you omit it?
#
# 14. How would you check that a value belongs to a set of allowed options in a
#     clean, Pythonic way (instead of chaining many `or` conditions)?
#
# 15. Can you place a function call directly inside an if condition
#     (e.g., `if is_valid(data):`)? What are the pros/cons of this versus
#     assigning the result to a variable first?
#
# 16. What is short-circuit evaluation, and how does it affect the order in
#     which conditions in an `if a and b:` statement are evaluated?
#
# 17. What is the purpose of the `pass` statement, and when might you need it
#     inside an if block?
#
# 18. How would you write a one-line if statement in Python? Are there
#     readability trade-offs versus a full block?
#
# 19. In `match-case`, how would you match multiple possible values in a single
#     case (an "or" pattern)?
#
# 20. What is the risk of writing deeply nested if-else blocks (the "arrow
#     anti-pattern")? How would you refactor a 4-5 level nested if-else into
#     cleaner code?
