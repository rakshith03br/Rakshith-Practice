"""
Variables in Python

A variable is a name that refers to a value stored in memory. Think of it as a label you
    attach to some piece of data so you can use and refer to it later.
"""
x = 10
name = "Alice"
price = 99.99

# Here, x, name, and price are variables pointing to the values 10, "Alice", and 99.99.
#-------------------------------------------------------------------
"""
No need to declare a type

Unlike languages like Java or C++, Python is dynamically typed — you don't declare a variable's 
    type upfront. Python figures it out automatically based on the value assigned.
"""
x1 = 10        # int
x2 = "hello"   # now x2 refers to a string — totally fine
x3 = 3.14      # now a float

#-------------------------------------------------------------------
a = [1, 2, 3]
b = a          # b points to the SAME list object as a
b.append(4)
print(a)       # [1, 2, 3, 4] — a is affected too!

"""
Naming rules
    - Must start with a letter or underscore (_), not a number
    - Can contain letters, numbers, and underscores
    - Case-sensitive (age and Age are different variables)
    - Cannot use Python reserved keywords (class, for, if, return, etc.)
"""
# age = 25          # ✅ valid
# _age = 25         # ✅ valid
# age2 = 25         # ✅ valid
# 2age = 25         # ❌ SyntaxError — can't start with a number
# class = 25        # ❌ SyntaxError — 'class' is a reserved keyword
# -------------------------------------------------------------------
# Multiple assignment

# Assign same value to multiple variables
x = y = z = 10
print(x, y, z)  # 10 10 10

# Assign different values in one line
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Swapping values — no temp variable needed!
a, b = b, a
print(a, b)  # 2 1
# -------------------------------------------------------------------
# Checking type and identity
x = 10
print(type(x))   # <class 'int'>
print(id(x))     # memory address the variable currently points to
# -------------------------------------------------------------------
# Reassignment doesn't modify the original object (for immutables)
x = 10
y = x       # y also points to 10

x = 20      # x now points to a NEW object (20)
print(y)    # 10 — y is unaffected, still points to the original object
# -------------------------------------------------------------------
"""
Variable scope (brief overview)
    Where a variable is defined affects where it can be accessed:
"""
x = 100  # global variable
def my_func():
    y = 50  # local variable, only exists inside this function
    print(x)  # can still read the global x
    print(y)
my_func()
# print(y)  # ❌ NameError — y doesn't exist outside the function (commented out so the file runs top-to-bottom)

"""
Quick summary

Concept	                        Behavior in Python
----------------                -----------------------------
Type declaration	            Not required — dynamically typed
What a variable is	            A name pointing to an object in memory
Reassignment	                Points to a new object, doesn't "edit" old one (for immutables)
Naming rule	                    Letters, digits, underscores; can't start with a digit
Convention	                    snake_case for variables, UPPER_CASE for constants
"""


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. Variables are just NAMES bound to OBJECTS - Python has NO "variable
#    boxes" like C/Java; understanding this reframes almost every other topic
# -------------------------
a = [1, 2, 3]
b = a
print(id(a), id(b), a is b)   # SAME id -> 'a' and 'b' are just two NAMES for the ONE SAME object
# There is no "copy" happening in `b = a` - both names simply point to the
# SAME object in memory. This is why b.append(4) affects what 'a' sees too
# (as your file's example already correctly shows).

print(f"{'*' * 60}")

# -------------------------
# 2. Dynamic typing vs dynamic BINDING - a common misconception to clarify
# -------------------------
# "Dynamically typed" does NOT mean "no types" - every OBJECT still has a
# very definite type. What's dynamic is that a given NAME (variable) can be
# REBOUND to point to objects of DIFFERENT types over its lifetime:
x = 10          # x is bound to an int object
print(type(x))    # <class 'int'>
x = "now a string"   # x is REBOUND to a completely different object (a str)
print(type(x))         # <class 'str'>
# The INT object (10) still exists with type int; 'x' just no longer points
# to it. This is different from "weak typing" (where VALUES change type
# implicitly during operations) - Python's objects always know their own type.

print(f"{'*' * 60}")

# -------------------------
# 3. Constants - Python has NO true constants (unlike Java's `final` or C's `const`)
# -------------------------
MAX_CONNECTIONS = 100   # UPPER_CASE is purely a NAMING CONVENTION signaling
                           # "please treat this as a constant" - Python does
                           # NOT actually prevent reassignment
MAX_CONNECTIONS = 200      # perfectly legal, no error - the convention is
                              # a social contract between developers, not
                              # enforced by the language
print(MAX_CONNECTIONS)        # 200

# For TRUE immutability/enforcement, you'd need something like:
from typing import Final
MAX_RETRIES: Final = 5   # signals intent to type checkers (mypy), but STILL
                            # doesn't prevent reassignment at runtime in plain Python

print(f"{'*' * 60}")

# -------------------------
# 4. Augmented assignment (+=, -=, etc.) and how it differs for mutable vs
#    immutable objects (ties directly into "variables are just names")
# -------------------------
num = 5
print(id(num))
num += 1          # for an IMMUTABLE int, this creates a NEW object and rebinds 'num'
print(id(num))      # DIFFERENT id

lst = [1, 2, 3]
print(id(lst))
lst += [4]           # for a MUTABLE list, += calls __iadd__ and mutates IN PLACE
print(id(lst))         # SAME id! -> this is why 'lst += [4]' is NOT equivalent
                          # to 'lst = lst + [4]' (which WOULD create a new object)

print(f"{'*' * 60}")

# -------------------------
# 5. Multiple assignment with SHARED mutable objects - a real gotcha, not
#    just an academic point
# -------------------------
p = q = []          # DANGER: p and q are the SAME list object, not two independent empty lists!
p.append(1)
print(p, q)            # [1] [1] -> modifying p ALSO changed q, since they're literally the same object

# CORRECT way to get two INDEPENDENT empty lists:
p2, q2 = [], []       # two SEPARATE list literals -> two SEPARATE objects
p2.append(1)
print(p2, q2)            # [1] []  -> q2 correctly unaffected

print(f"{'*' * 60}")

# -------------------------
# 6. Chained comparisons vs chained assignment - don't confuse the two syntaxes
# -------------------------
x = y = z = 0        # chained ASSIGNMENT - all three names bound to the SAME initial object (0)
print(x, y, z)          # 0 0 0
x = 5
print(x, y, z)             # 5 0 0 -> since 0 is immutable, reassigning x doesn't affect y or z at all
                              # (this is SAFE for immutables, unlike the mutable list example above)

print(f"{'*' * 60}")

# -------------------------
# 7. Reserved keywords - checking programmatically instead of memorizing
# -------------------------
import keyword
print(keyword.iskeyword("class"))    # True
print(keyword.iskeyword("age"))        # False
print(keyword.kwlist[:10])               # shows the first 10 reserved keywords directly from Python itself

# Python also has "soft keywords" (context-dependent, usable as variable
# names in most contexts) like 'match', 'case', '_', and 'type':
print(keyword.softkwlist)   # ['_', 'case', 'match', 'type'] (may vary slightly by Python version)

print(f"{'*' * 60}")

# -------------------------
# 8. Variable annotations (type hints) - NOT enforced, but useful metadata
# -------------------------
age: int = 25              # type hint says "int", but Python does NOT enforce this at runtime
age = "twenty-five"           # perfectly legal! no error, even though the hint says int
print(age)                      # 'twenty-five'
print(__annotations__)            # {'age': <class 'int'>} -> the hint is just STORED as metadata,
                                     # for tools like mypy to check STATICALLY, not enforced at runtime

print(f"{'*' * 60}")

# -------------------------
# 9. del statement - unbinding a name (NOT necessarily destroying the object
#    immediately - depends on reference counting)
# -------------------------
temp_var = [1, 2, 3]
del temp_var          # removes the NAME 'temp_var' from the current namespace
try:
    print(temp_var)     # NameError! the name no longer exists
except NameError as e:
    print("NameError:", e)

# The underlying LIST object itself is only actually garbage-collected if NO
# other names/references still point to it - del just removes ONE reference/name.
shared = [1, 2, 3]
other_ref = shared      # a second name pointing to the SAME list
del shared                 # removes 'shared', but the list is STILL ALIVE via 'other_ref'
print(other_ref)             # [1, 2, 3] -> the list object survived, because 'other_ref' still points to it

print(f"{'*' * 60}")

# -------------------------
# 10. Global vs local variable naming COLLISION - variables at different
#     scope levels are entirely independent, even with the SAME name
# -------------------------
count = "I'm global"
def local_shadow():
    count = "I'm local"   # creates a COMPLETELY SEPARATE local variable,
                             # does NOT touch/overwrite the global 'count'
    print("Inside function:", count)
local_shadow()
print("Outside function:", count)   # 'I'm global' -> completely unaffected by the function's local variable

print(f"{'*' * 60}")

# -------------------------
# 11. Walrus operator (:=) - assignment as part of a larger EXPRESSION
#     (Python 3.8+), useful to know as a "variable assignment" edge case
# -------------------------
data = [1, 2, 3, 4, 5]
if (n := len(data)) > 3:          # assigns AND Test_Cases n in a single expression
    print(f"List has {n} items, which is more than 3")
# equivalent WITHOUT walrus would need two separate lines:
# n = len(data)
# if n > 3: ...


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON VARIABLES
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What does it actually mean that "a variable in Python is a name bound to
#    an object," rather than a labeled memory box holding a value directly
#    (as in C)?
#
# 2. What is the difference between "dynamically typed" and "weakly typed"?
#    Is Python one, both, or neither? Justify your answer with an example.
#
# 3. Does Python have TRUE constants (like Java's `final` or C's `const`)?
#    What does the UPPER_CASE naming convention actually enforce, if
#    anything?
#
# 4. If `b = a` for two variables pointing to the SAME mutable list, and you
#    then do `b.append(x)`, does `a` see the change? Why?
#
# 5. What's the difference between `p = q = []` and `p, q = [], []`? Which
#    one creates TWO independent list objects, and which creates just ONE
#    shared object referenced by two names?
#
# 6. Why does `num += 1` behave differently from `lst += [4]` in terms of
#    whether the underlying object's `id()` changes?
#
# 7. What are Python's naming rules for identifiers? Can a variable name
#    start with a digit or contain a hyphen?
#
# 8. How would you programmatically check whether a given string is a
#    reserved Python keyword, without hardcoding a list yourself?
#
# 9. What is a "soft keyword" in Python (e.g., `match`, `case`, `type`)? How
#    is it different from a regular reserved keyword like `class` or `for`?
#
# 10. Are Python's variable type annotations (e.g., `age: int = 25`) enforced
#     at runtime? What happens if you later assign a string to a variable
#     annotated as `int`?
#
# 11. What does the `del` statement actually do to a variable? Does it always
#     immediately destroy the underlying object in memory?
#
# 12. If two different names both reference the SAME object, and you `del`
#     one of those names, does the object get garbage collected right away?
#
# 13. If a global variable and a local variable inside a function share the
#     EXACT same name, does assigning to the local one inside the function
#     affect the global variable at all (assuming no `global` keyword is
#     used)?
#
# 14. What is the walrus operator (:=), and how is it different from a
#     regular assignment statement (`=`) in terms of where it can be used
#     (e.g., inside an `if` condition)?
#
# 15. Why does chained assignment like `x = y = z = 0` behave "safely" (no
#     shared-mutation surprises) when 0 is an int, but chained assignment
#     with a mutable default like `x = y = z = []` can lead to bugs?
#
# 16. What does `id()` return for a variable, and how would you use it to
#     PROVE whether two variable names refer to the same underlying object?
#
# 17. Can a Python variable change its type over its lifetime (e.g., first
#     hold an int, later hold a string)? Does this mean the underlying
#     OBJECTS themselves can change type, or just what the NAME points to?
#
# 18. What naming convention does PEP 8 recommend for regular variables
#     versus constants versus class names?
#
# 19. If you swap two variables using `a, b = b, a`, does Python create any
#     temporary variable behind the scenes? What data structure is briefly
#     involved in this operation?
#
# 20. What would happen if you tried to use a Python reserved keyword (like
#     `class` or `def`) as a variable name? At what stage would this fail -
#     parse time, compile time, or runtime?