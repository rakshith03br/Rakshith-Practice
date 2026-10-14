"""
tuple in Python:- tuple()

A tuple is an ordered collection of items, similar to a list — but with one key difference: it's immutable.
    Once created, you can't change, add, or remove elements.
    Ordered — items have a fixed position (indexed)
    Indexed — accessed using [] like lists and strings
    Immutable — cannot be modified after creation
    Allows duplicates — same value can appear more than once
    Can hold mixed data types — ints, strings, other tuples, etc.

"""
# Creating tuples
t1 = (1, 2, 3)
t2 = 1, 2, 3          # parentheses are optional
t3 = ("apple", "banana", "cherry")
t4 = (1, "hello", 3.14, True)   # mixed types allowed

t5 = ()                # empty tuple
t6 = (5,)              # single-element tuple — comma is REQUIRED
t7 = (5)               # this is just an int, NOT a tuple!
print(type(t7))         # <class 'int'>

# Indexing and slicing (same as lists/strings)
t = (10, 20, 30, 40, 50)

print(t[0])     # 10
print(t[-1])    # 50
print(t[1:3])   # (20, 30)
print(t[::-1])  # (50, 40, 30, 20, 10)

# Immutability — the core feature
t = (1, 2, 3)
# t[0] = 100   # ❌ TypeError — tuples don't support item assignment (commented out so the file runs top-to-bottom)

# You cannot modify a tuple in place. If you need a changed version, you must create a new tuple:
t = (1, 2, 3)
t = (100,) + t[1:]
print(t)  # (100, 2, 3)


# Catch: if a tuple contains a mutable object (like a list), that inner object can still be changed — the tuple only
# locks its own references, not what those references point to:
t = (1, [2, 3], 4)
t[1].append(100)
print(t)  # (1, [2, 3, 100], 4)  ✅ works — the list itself is still mutable

# Common operations
t = (1, 2, 3, 2, 1)

len(t)          # 5
t.count(2)      # 2  — how many times 2 appears
t.index(3)      # 2  — position of first occurrence of 3
print(2 in t)          # True — membership check

# Concatenation and repetition
a = (1, 2, 3)
b = (4, 5)

print(a + b)    # (1, 2, 3, 4, 5)
print(a * 2)    # (1, 2, 3, 1, 2, 3)

# Tuple unpacking
t = (10, 20, 30)
x, y, z = t
print(x, y, z)  # 10 20 30
# This is used a lot for returning multiple values from a function:
def min_max(numbers):
    return min(numbers), max(numbers)
low, high = min_max([4, 7, 1, 9])
print(low, high)  # 1 9

"""
Why use a tuple instead of a list?
Reason	            Explanation
--------------      ------------------------------------------------------------------------------
Data integrity	    Immutability prevents accidental modification
Performance	        Tuples are slightly faster than lists
Hashable	        Tuples (with only immutable elements) can be used as dictionary keys or set elements — lists cannot
"""
d = {(1, 2): "point A", (3, 4): "point B"}  # ✅ works — tuple as dict key
# d = {[1, 2]: "point A"}                      # ❌ TypeError — list can't be a key (commented out so the file runs top-to-bottom)


"""
Tuple vs List — quick comparison
Feature	            Tuple	                                List
--------            -------------                           -------------------------------
Mutable?	        ❌ No	                                ✅ Yes
Syntax	            (1, 2, 3)	                            [1, 2, 3]
Speed	            Faster	                                Slower
Use as dict key?    ✅ Yes (if elements are immutable)	    ❌ No
Common use	        Fixed data, function returns	        Data that changes over time
"""
"""
Quick summary
Feature	                Tuple
-----------             ---------------
Ordered?	            ✅ Yes
Indexed?	            ✅ Yes
Mutable?	            ❌ No
Duplicates allowed?	    ✅ Yes
Common use	            Fixed collections, safe data passing, dictionary keys
"""


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. Why tuples are FASTER than lists - proving it, not just stating it
# -------------------------
import timeit
import sys

# Creation time comparison
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1_000_000)
list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1_000_000)
print(f"Tuple creation: {tuple_time:.4f}s")
print(f"List creation: {list_time:.4f}s")   # typically SLOWER than tuple creation

# Memory size comparison
t = (1, 2, 3, 4, 5)
l = [1, 2, 3, 4, 5]
print(f"Tuple size: {sys.getsizeof(t)} bytes")
print(f"List size: {sys.getsizeof(l)} bytes")   # typically LARGER than the tuple

# WHY: lists are designed to GROW/SHRINK, so Python allocates EXTRA capacity
# ("over-allocation") for future appends. Tuples have a FIXED size known at
# creation time, so there's no extra padding/capacity to allocate.

print(f"{'*' * 60}")

# -------------------------
# 2. Tuple packing and unpacking in depth - extended unpacking with *
# -------------------------
t = (1, 2, 3, 4, 5)
first, *middle, last = t
print(first, middle, last)   # 1 [2, 3, 4] 5 -> NOTE: 'middle' becomes a LIST, not a tuple!

a, b, *rest = t
print(a, b, rest)              # 1 2 [3, 4, 5]

# swapping variables - a classic tuple-packing trick, no temp variable needed
x, y = 10, 20
x, y = y, x            # this WORKS because Python packs (y, x) into a tuple,
                          # then unpacks it into (x, y) - all in one atomic step
print(x, y)               # 20 10

print(f"{'*' * 60}")

# -------------------------
# 3. Nested tuple unpacking - unpacking structures within structures
# -------------------------
point_data = (1, (2, 3))
a, (b, c) = point_data
print(a, b, c)   # 1 2 3 -> the inner tuple gets unpacked too, matching the nested structure

coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:            # unpacking each tuple directly in the for loop
    print(f"x={x}, y={y}")

print(f"{'*' * 60}")

# -------------------------
# 4. Named tuples - adding FIELD NAMES to tuples for readability (a VERY
#    common "how would you improve this" interview follow-up)
# -------------------------
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)          # 3 4 -> access by NAME, more readable than p[0], p[1]
print(p[0], p[1])          # 3 4 -> still works like a regular tuple too (backward compatible)
print(isinstance(p, tuple))  # True -> namedtuple IS a tuple subclass, all tuple operations still work

# Why prefer namedtuple over a plain tuple:
plain_point = (3, 4)
print(plain_point[0])   # 3 -> unclear what this represents without external context
print(p.x)                 # 3 -> self-documenting

print(f"{'*' * 60}")

# -------------------------
# 5. Tuples ARE hashable - but ONLY if every element inside is also hashable
# -------------------------
t1 = (1, 2, 3)
print(hash(t1))          # works fine - all elements are immutable/hashable

t2 = (1, [2, 3])            # contains a LIST - lists are unhashable
try:
    hash(t2)
except TypeError as e:
    print("TypeError:", e)   # unhashable type: 'list'

# This is WHY {(1, 2): "value"} works as a dict key, but {(1, [2, 3]): "value"}
# does NOT - the hashability of a tuple depends ENTIRELY on the hashability
# of everything inside it, recursively.

print(f"{'*' * 60}")

# -------------------------
# 6. Tuple as a return value for multiple values - the mechanics explained
# -------------------------
def divide_with_remainder(a, b):
    return a // b, a % b   # this is ACTUALLY building and returning a TUPLE (a//b, a%b)

result = divide_with_remainder(17, 5)
print(type(result), result)   # <class 'tuple'> (3, 2)

quotient, remainder = divide_with_remainder(17, 5)   # unpacked on the caller's side
print(quotient, remainder)                              # 3 2

print(f"{'*' * 60}")

# -------------------------
# 7. Single-element tuple gotcha, revisited with function calls specifically
# -------------------------
def returns_one_value():
    return (42)   # looks like a tuple, but the () here are just GROUPING parentheses, not a tuple!

print(type(returns_one_value()))   # <class 'int'> -> NOT a tuple, exactly like your t7 = (5) example

def returns_one_tuple():
    return (42,)   # the trailing comma is what ACTUALLY makes this a tuple

print(type(returns_one_tuple()))   # <class 'tuple'>

print(f"{'*' * 60}")

# -------------------------
# 8. Converting between tuple and other types
# -------------------------
print(tuple([1, 2, 3]))        # (1, 2, 3) -> list to tuple
print(list((1, 2, 3)))           # [1, 2, 3] -> tuple to list (needed if you want to MUTATE it)
print(tuple("hello"))              # ('h', 'e', 'l', 'l', 'o') -> string to tuple of characters
print(tuple({1, 2, 3}))              # (1, 2, 3) -> set to tuple (order not guaranteed)

print(f"{'*' * 60}")

# -------------------------
# 9. zip() with tuples - a VERY common real-world pairing/combination pattern
# -------------------------
names = ("Alice", "Bob", "Charlie")
ages = (30, 25, 35)
paired = tuple(zip(names, ages))
print(paired)   # (('Alice', 30), ('Bob', 25), ('Charlie', 35)) -> zip produces tuples by default

# unzipping - the REVERSE of zip, using the same zip() function with * unpacking
unzipped_names, unzipped_ages = zip(*paired)
print(unzipped_names, unzipped_ages)   # ('Alice', 'Bob', 'Charlie') (30, 25, 35)

print(f"{'*' * 60}")

# -------------------------
# 10. sorted() on a list of tuples - a common coding-interview pattern
# -------------------------
students = [("Bob", 85), ("Alice", 92), ("Carol", 78)]
by_score = sorted(students, key=lambda s: s[1], reverse=True)   # sort by 2nd element, descending
print(by_score)   # [('Alice', 92), ('Bob', 85), ('Carol', 78)]

# tuples also compare LEXICOGRAPHICALLY by default (element by element),
# which is why sorted() works even WITHOUT a key function on tuples of comparable types:
points = [(1, 5), (1, 2), (0, 9)]
print(sorted(points))   # [(0, 9), (1, 2), (1, 5)] -> compares first element first,
                           # only looks at 2nd element to break ties


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON TUPLES
## ==========================================================

# 1. Why are tuples generally faster and more memory-efficient than lists of
#    the same elements? What's the underlying reason (hint: think about how
#    each type handles resizing/growth)?
#
# ANSWER: Lists are designed to grow and shrink, so CPython over-allocates
# extra capacity beyond the current number of elements to make future
# append() calls cheap (amortized O(1)). That spare capacity costs memory
# even when unused. Tuples are fixed-size and immutable — the interpreter
# knows the exact size at creation time, so it allocates precisely that much
# space with zero padding. Tuple creation also skips the growth-management
# bookkeeping lists need, and because tuples are immutable, small tuples can
# be cached/reused by CPython, further reducing overhead.

# 2. What's the difference between `(5)` and `(5,)`? Why does the trailing
#    comma matter so much for single-element tuples?
#
# ANSWER: `(5)` is just the integer 5 in grouping parentheses — parentheses
# alone don't create a tuple. `(5,)` is a one-element tuple because it's the
# comma, not the parentheses, that actually builds a tuple in Python. The
# trailing comma is required for single-element tuples to distinguish them
# from a simple parenthesized expression.

# 3. Why can a tuple be used as a dictionary key, but a list cannot? Does
#    EVERY tuple qualify as a valid dictionary key?
#
# ANSWER: Dict keys must be hashable, and hashability generally requires
# immutability (so the hash value never changes while the object is stored).
# Tuples are immutable, so they support __hash__; lists are mutable, so
# Python disables __hash__ for them. However, not every tuple qualifies —
# a tuple is only hashable if every element inside it is also hashable. A
# tuple containing a list, e.g. `(1, [2, 3])`, will raise a TypeError when
# hashed, so it can't be used as a dict key either.

# 4. If a tuple contains a mutable object like a list (e.g., `(1, [2, 3])`),
#    can that inner list still be modified? Does this violate the tuple's
#    immutability?
#
# ANSWER: Yes, the inner list can still be modified (e.g., `.append()`,
# `.sort()`, item assignment). This doesn't violate the tuple's immutability
# because a tuple only guarantees that its own references/slots can't be
# reassigned — you can't make the tuple point to a different object at that
# index. But if that referenced object is itself mutable, its internal state
# is free to change. Immutability is shallow, not deep.

# 5. What does extended unpacking like `first, *middle, last = my_tuple` do?
#    What TYPE does the `middle` variable end up being?
#
# ANSWER: It assigns the first element to `first`, the last element to
# `last`, and collects everything in between into `middle`. Regardless of
# the fact that the source was a tuple, `middle` is always a LIST, not a
# tuple — the starred target in extended unpacking always produces a list.

# 6. How does the classic "swap two variables" trick (`x, y = y, x`) actually
#    work under the hood in terms of tuple packing and unpacking?
#
# ANSWER: Python first evaluates the entire right-hand side, packing the
# current values of `y` and `x` into a temporary tuple `(y, x)`. Only after
# that tuple is fully built does it unpack the tuple's elements into the
# left-hand targets `x` and `y` in order. Because the RHS is evaluated
# completely before any assignment happens, no temporary variable is needed
# and there's no risk of one assignment clobbering a value the other still
# needs.

# 7. What is a namedtuple, and what advantage does it offer over a plain
#    tuple? Is a namedtuple instance still considered a "true" tuple (e.g.,
#    does `isinstance(p, tuple)` return True)?
#
# ANSWER: A namedtuple (from collections.namedtuple) is a tuple subclass
# that lets you access elements by descriptive field names (p.x) as well as
# by index (p[0]), making code more self-documenting than a plain tuple
# while keeping the same performance and immutability characteristics. Since
# it's implemented as a genuine subclass of tuple, `isinstance(p, tuple)`
# returns True, and all normal tuple operations (indexing, iteration,
# unpacking, concatenation, etc.) still work on it.

# 8. When a function does `return a, b`, what data type is ACTUALLY being
#    returned? How would the caller receive both values?
#
# ANSWER: `return a, b` implicitly packs the two values into a tuple `(a, b)`
# and returns that single tuple object — Python doesn't have a special
# "multiple return values" mechanism, it's tuple packing under the hood. The
# caller can either capture the whole tuple in one variable (`result = f()`)
# or unpack it directly into two variables in one line (`x, y = f()`).

# 9. How would you "unzip" a list of paired tuples back into two separate
#    tuples/lists? What function and trick would you use?
#
# ANSWER: Reuse `zip()` itself combined with the `*` unpacking operator:
# `zip(*paired)`. The `*` unpacks each tuple in `paired` as a separate
# positional argument to zip, which then groups the first elements of each
# together, the second elements together, and so on — effectively
# transposing the pairs. The result is an iterator of tuples, which you can
# unpack directly (e.g., `names, ages = zip(*paired)`) or wrap in `list()`
# if you need mutable sequences.

# 10. Why does `sorted()` work on a list of tuples even without specifying a
#     `key` function? What determines the sort order in that case?
#
# ANSWER: Tuples support lexicographic ("dictionary order") comparison by
# default: Python compares the first elements of two tuples first; if
# they're equal, it moves on to compare the second elements, and so on,
# until a difference is found or one tuple runs out of elements. Since `<`,
# `>`, etc. are defined this way for tuples, `sorted()` can compare tuples
# directly without a custom key, as long as the corresponding elements at
# each position are themselves comparable.

# 11. What happens if you try to compute `hash((1, [2, 3]))`? Why does this
#     fail even though the OUTER object is a tuple?
#
# ANSWER: It raises `TypeError: unhashable type: 'list'`. A tuple's hash is
# computed by combining the hashes of all its elements, so hashability is
# inherited from its contents, not just the container type. Since the list
# `[2, 3]` inside the tuple is mutable and therefore unhashable, attempting
# to hash the whole tuple propagates that failure, even though the tuple
# itself is otherwise immutable.

# 12. How would you convert a list to a tuple, and why might you want to do
#     this (e.g., to use as a dict key, or to make data immutable/safe from
#     accidental modification)?
#
# ANSWER: Use the `tuple()` constructor, e.g. `tuple(my_list)`. Reasons to do
# this include: making the sequence hashable so it can be used as a dict key
# or set element; signaling/enforcing that the data shouldn't change further
# in the program (defensive copying at an API boundary); and getting the
# minor speed/memory benefits of tuples when the data is genuinely fixed.

# 13. What's the difference between `tuple.count(x)` and `list.count(x)`? Is
#     there any meaningful behavioral difference, or are they identical in
#     usage?
#
# ANSWER: Both methods do exactly the same conceptual thing — return the
# number of times `x` appears in the sequence — using the same equality-based
# comparison logic. There's no behavioral difference in what they compute;
# the only distinction is which underlying sequence type provides the
# method, and that a list's contents (and thus the count) can change over
# time while a tuple's cannot.

# 14. Given a tuple like `(1, (2, 3))`, how would you unpack it into three
#     separate variables (one for the first element, and two for the nested
#     tuple's elements)?
#
# ANSWER: Use nested unpacking that mirrors the structure:
# `a, (b, c) = (1, (2, 3))`. Python matches the shape of the target pattern
# against the shape of the value, so `a` gets 1, and `(b, c)` unpacks the
# inner tuple, giving `b = 2` and `c = 3`.

# 15. Why might a senior developer prefer a namedtuple (or a dataclass) over
#     a plain tuple when returning multiple values from a function, from a
#     code-maintainability perspective?
#
# ANSWER: Plain tuples force callers to remember the meaning of each
# position (e.g., "is index 0 the min or the max?"), which is error-prone
# and gets worse as more values are returned or as the function evolves.
# Named tuples (or dataclasses) attach explicit field names, making the
# return value self-documenting, safer against accidental reordering bugs,
# and easier to extend (adding a field doesn't break positional unpacking
# elsewhere) — all while dataclasses additionally offer mutability options,
# type hints, and default values that plain tuples/namedtuples don't.

# 16. What's the difference in mutability guarantees between `tuple(some_list)`
#     and simply keeping a reference to the original list? Does converting to
#     a tuple protect the ORIGINAL list from being mutated elsewhere?
#
# ANSWER: `tuple(some_list)` creates a brand-new tuple object containing
# copies of the references from `some_list` — it does not wrap or alias the
# original list. So the new tuple itself can never be mutated (no
# append/remove/item-assignment), but the original list variable is
# completely unaffected and can still be freely mutated elsewhere; the two
# objects are now independent. Converting to a tuple protects only the new
# tuple's structure, not the original list.

# 17. Can you concatenate a tuple and a list directly (e.g., `(1, 2) + [3, 4]`)?
#     What error would you get, and how would you fix it?
#
# ANSWER: No — this raises `TypeError: can only concatenate tuple (not
# "list") to tuple`, because `+` requires both operands to be the same
# sequence type. To fix it, convert one side to match the other, e.g.
# `(1, 2) + tuple([3, 4])` to get a tuple result, or `list((1, 2)) + [3, 4]`
# to get a list result.

# 18. What does `a, b = b, a` demonstrate about Python evaluating the
#     right-hand side of an assignment BEFORE performing any of the
#     left-hand-side bindings?
#
# ANSWER: It demonstrates that Python fully evaluates and packs the RHS
# tuple `(b, a)` using the values `a` and `b` had *before* the statement
# runs, and only afterward does it unpack that tuple into the LHS targets.
# Because none of the LHS assignments happen until the RHS tuple is
# complete, `a` and `b` swap correctly without either value being
# overwritten prematurely — no temporary variable is required.

# 19. If you have a tuple of tuples representing rows of data, how would you
#     sort them by the SECOND column instead of the first?
#
# ANSWER: Pass a `key` function to `sorted()` (or `.sort()`) that extracts
# the second element of each row, e.g.
# `sorted(rows, key=lambda row: row[1])`. This tells Python to compare rows
# based on index 1 instead of the default lexicographic (index-0-first)
# comparison.

# 20. Why does Python allow tuples to be created WITHOUT parentheses (e.g.,
#     `t = 1, 2, 3`)? What is technically doing the "tuple-making" here?
#
# ANSWER: It's the comma(s), not the parentheses, that create a tuple in
# Python — parentheses are just optional visual grouping (and are only
# mandatory in ambiguous contexts, like function calls or empty tuples).
# When Python's parser sees a comma-separated sequence of expressions on the
# right-hand side of an assignment (or in other expression contexts), it
# packs them into a tuple automatically, which is why `t = 1, 2, 3` and
# `t = (1, 2, 3)` produce the identical result.