"""
'set' in Python:- set()

A set is a collection that is:
    Unordered — no guaranteed order of elements
    Unindexed — no accessing elements by position (s[0] doesn't work)
    Mutable — you can add/remove elements
    Unique — no duplicate elements allowed
"""

# Creating a set
s1 = {1, 2, 3, 4}
print(s1)  # {1, 2, 3, 4}

s2 = set([1, 2, 2, 3, 3, 3])  # duplicates automatically removed
print(s2)  # {1, 2, 3}

s3 = set()  # empty set — note: {} creates an empty DICT, not a set!
# Important gotcha: {} creates an empty dictionary, not an empty set. You must use set() for an empty set.

# Duplicates are removed automatically
s = {1, 2, 2, 3, 3, 3, 4}
print(s)  # {1, 2, 3, 4}

lst = [1, 2, 2, 3, 4, 4, 5]
unique = set(lst)
print(unique)  # {1, 2, 3, 4, 5}

# No indexing
s = {10, 20, 30}
# print(s[0])  # ❌ TypeError — sets don't support indexing (commented out so the file runs top-to-bottom)

# Common operations:
# 1.Adding elements: add()
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}

# 2. Removing elements: remove(), discard(), pop()
s.remove(2)     # raises error if 2 not present
s.discard(10)   # does NOT raise error if 10 not present
s.pop()         # removes a random element (sets are unordered)

# Checking membership (very fast)
s = {1, 2, 3}
print(2 in s)   # True

# Set operations (math-style)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # Union → {1, 2, 3, 4, 5, 6}
print(a & b)   # Intersection → {3, 4}
print(a - b)   # Difference → {1, 2}
print(a ^ b)   # Symmetric difference → {1, 2, 5, 6}

'''
Operator	    Method	                    Meaning
|	            .union()	                Combine both sets
&	            .intersection()	            Common elements
-	            .difference()	            In a but not b
^	            .symmetric_difference()	    In either, but not both
'''
# Practical example
students_math = {"Alice", "Bob", "Charlie"}
students_science = {"Bob", "Charlie", "David"}

# Students in both classes
print(students_math & students_science)  # {'Bob', 'Charlie'}

# Students only in math
print(students_math - students_science)  # {'Alice'}

# All students (no duplicates)
print(students_math | students_science)  # {'Alice', 'Bob', 'Charlie', 'David'}

print(students_math ^ students_science) # {'Alice', 'David'}

#--------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------#
"""
Frozenset — the immutable version of 'set' is 'frozenset' :- frozenset()

If you need a set that can't be changed after creation (e.g., to use as a dictionary key, 
    since regular sets aren't hashable):
"""
fs = frozenset([1, 2, 3])
# fs.add(4)  # ❌ AttributeError — frozensets are immutable (commented out so the file runs top-to-bottom)

"""
Quick summary

Feature	    Set
Ordered?	❌ No
Indexed?	❌ No
Duplicates?	❌ Not allowed
Mutable?	✅ Yes
Common use	Removing duplicates, fast membership checks, math-style set operations
"""


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION
## ==========================================================

# -------------------------
# 1. Time complexity - WHY sets are used for fast membership checks
#    (the #1 practical reason sets exist, worth stating explicitly)
# -------------------------
# Sets are implemented as HASH TABLES (same underlying structure as dict),
# so:
#   x in my_set        -> O(1) average case
#   my_set.add(x)        -> O(1) average case
#   my_set.remove(x)       -> O(1) average case
# Compare with a LIST, where `x in my_list` is O(n) - must scan every element.
import time
big_list = list(range(1_000_000))
big_set = set(big_list)

start = time.perf_counter()
999_999 in big_list      # O(n) - scans up to the whole list
print(f"list membership check: {time.perf_counter() - start:.6f}s")

start = time.perf_counter()
999_999 in big_set         # O(1) - direct hash lookup
print(f"set membership check: {time.perf_counter() - start:.6f}s")
# The set lookup should be dramatically faster, especially as the collection grows.

print(f"{'*' * 60}")

# -------------------------
# 2. remove() vs discard() vs pop() - precise behavior differences
# -------------------------
s = {1, 2, 3}
try:
    s.remove(99)          # raises KeyError if the element doesn't exist
except KeyError as e:
    print("KeyError from remove():", e)

s.discard(99)                # does NOT raise, silently does nothing if 99 isn't present
print(s)                       # {1, 2, 3} -> unchanged, no error

popped = s.pop()                 # removes and RETURNS an ARBITRARY element (not necessarily "random"
                                   # in the statistical sense - just unspecified/implementation-defined)
print(popped, s)                    # e.g. 1 {2, 3}

empty_set = set()
try:
    empty_set.pop()                   # raises KeyError if the set is EMPTY
except KeyError as e:
    print("KeyError from pop() on empty set:", e)

print(f"{'*' * 60}")

# -------------------------
# 3. Why sets require HASHABLE (and therefore typically immutable) elements
# -------------------------
s = {1, 2, (3, 4)}       # tuple works fine - it's hashable (as long as its own contents are hashable)
print(s)
try:
    s.add([5, 6])           # TypeError: lists are UNHASHABLE - can't be a set element
except TypeError as e:
    print("TypeError:", e)   # unhashable type: 'list'

# This is the SAME underlying reason dict keys must be hashable - sets and
# dict keys are both implemented using the same hash-table mechanism.

print(f"{'*' * 60}")

# -------------------------
# 4. Set comprehensions - the set equivalent of list/dict comprehensions
# -------------------------
squares_set = {x**2 for x in range(10)}
print(squares_set)   # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# useful for deduplicating WHILE transforming in one step:
words = ["Hello", "hello", "WORLD", "world"]
unique_lower = {w.lower() for w in words}
print(unique_lower)   # {'hello', 'world'} -> deduplicated AND lowercased in one comprehension

print(f"{'*' * 60}")

# -------------------------
# 5. Comparison operators between sets - subset, superset, disjoint checks
# -------------------------
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a <= b)          # True  -> a is a SUBSET of b (a.issubset(b))
print(a < b)             # True  -> a is a PROPER subset (subset AND not equal)
print(b >= a)              # True  -> b is a SUPERSET of a (b.issuperset(a))
print(b > a)                 # True  -> b is a PROPER superset
print(a == {3, 2, 1})           # True  -> set equality ignores ORDER entirely (sets are unordered anyway)

c = {10, 20}
print(a.isdisjoint(c))    # True -> a and c share NO common elements at all

print(f"{'*' * 60}")

# -------------------------
# 6. In-place set operations - the *_update() methods (mutate the set directly,
#    vs the operators | & - ^ which return a NEW set)
# -------------------------
x = {1, 2, 3}
y = {3, 4, 5}

x_copy = x.copy()
x_copy.update(y)                    # equivalent to x_copy |= y -> mutates IN PLACE, adds all of y's elements
print(x_copy)                          # {1, 2, 3, 4, 5}

x_copy2 = x.copy()
x_copy2.intersection_update(y)          # equivalent to x_copy2 &= y -> keeps only common elements, IN PLACE
print(x_copy2)                             # {3}

x_copy3 = x.copy()
x_copy3.difference_update(y)                 # equivalent to x_copy3 -= y -> removes y's elements, IN PLACE
print(x_copy3)                                  # {1, 2}

x_copy4 = x.copy()
x_copy4.symmetric_difference_update(y)             # equivalent to x_copy4 ^= y -> IN PLACE
print(x_copy4)                                        # {1, 2, 4, 5}

# KEY DIFFERENCE: `x | y` creates and returns a NEW set (x unchanged);
# `x.update(y)` (or `x |= y`) MODIFIES x directly, in place.

print(f"{'*' * 60}")

# -------------------------
# 7. Removing duplicates from a list WHILE preserving original order
#    (a very common real interview coding question - plain set() loses order!)
# -------------------------
original = [3, 1, 2, 3, 1, 4, 2]
deduped_unordered = list(set(original))
print(deduped_unordered)   # order NOT guaranteed to match original - e.g. [1, 2, 3, 4]

# To preserve insertion order while removing duplicates, use dict.fromkeys()
# (dicts preserve insertion order since Python 3.7):
deduped_ordered = list(dict.fromkeys(original))
print(deduped_ordered)   # [3, 1, 2, 4] -> preserves the ORIGINAL first-seen order

print(f"{'*' * 60}")

# -------------------------
# 8. frozenset - being hashable, and its role as a dict key / set member
# -------------------------
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 2, 1])
print(fs1 == fs2)   # True -> order doesn't matter for equality, just like regular sets

# frozenset supports the SAME set operations (|, &, -, ^) as a regular set,
# just returns a NEW frozenset instead of mutating (since it CAN'T mutate):
print(fs1 | frozenset([4, 5]))   # frozenset({1, 2, 3, 4, 5})

# frozenset IS hashable -> can be used as a dict key or nested inside another set:
d = {frozenset([1, 2]): "pair one-two"}
print(d)                             # {frozenset({1, 2}): 'pair one-two'}
nested = {frozenset([1, 2]), frozenset([3, 4])}   # a set OF frozensets - impossible with regular sets!
print(nested)

print(f"{'*' * 60}")

# -------------------------
# 9. Sets are UNORDERED - never rely on iteration order (even though small
#    int sets often APPEAR sorted due to CPython implementation details)
# -------------------------
s = {5, 3, 1, 4, 2}
print(s)   # may print in what LOOKS like sorted order for small ints, but this
             # is an implementation detail of CPython's hash table, NOT a guarantee -
             # never write code that depends on set iteration order

print(f"{'*' * 60}")

# -------------------------
# 10. Practical use case: finding common/unique elements across MULTIPLE lists
#     (a common coding-round style problem, using set operations cleanly)
# -------------------------
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]

common_to_all = set(list1) & set(list2) & set(list3)
print(common_to_all)   # {4} -> only element present in ALL three lists

all_unique = set(list1) | set(list2) | set(list3)
print(all_unique)         # {1, 2, 3, 4, 5, 6, 7} -> union of everything, no duplicates


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON SETS (WITH ANSWERS)
## ==========================================================

# 1. Why is checking membership (`x in my_set`) much faster than checking
#    membership in a list, for large collections? What data structure is a
#    set built on top of internally?
#
#    ANSWER: A set is built on a HASH TABLE. To check `x in my_set`, Python
#    computes hash(x) and jumps directly to the slot where x would be stored,
#    so the check is O(1) on average no matter how big the set is. A list has
#    no such index, so `x in my_list` must compare x against each element one
#    by one, which is O(n). For a million elements, that is the difference
#    between one lookup and up to a million comparisons.
#
# 2. What is the difference between set.remove(x) and set.discard(x)? Which
#    one raises an error if x isn't present?
#
#    ANSWER: Both delete x if it exists. The difference is only when x is
#    missing: remove(x) raises a KeyError, while discard(x) silently does
#    nothing. Use remove() when a missing element indicates a bug you want to
#    catch, and discard() when "remove it if it's there" is all you need.
#
# 3. What does set.pop() do, and what happens if you call it on an empty
#    set? Does it remove a "random" element in the statistical sense?
#
#    ANSWER: pop() removes and RETURNS one element from the set. On an empty
#    set it raises KeyError: 'pop from an empty set'. The element is
#    ARBITRARY, not random: which one comes out depends on the internal
#    hash-table layout, so it is unspecified but not statistically random.
#    For small ints in CPython it is often the smallest value, but you must
#    never rely on that. If you need true randomness, use
#    random.choice(list(s)).
#
# 4. Why must elements added to a set be hashable? What types can and cannot
#    be added to a set, and why?
#
#    ANSWER: The set stores each element in a slot determined by its hash. If
#    an element could change after being added, its hash would change and the
#    set could no longer find it. So elements must be hashable, meaning their
#    hash never changes during their lifetime.
#      CAN be added:    int, float, str, bool, None, tuple (if all its items
#                       are hashable), frozenset
#      CANNOT be added: list, dict, set (all mutable, therefore unhashable)
#    e.g. s.add([1, 2]) -> TypeError: unhashable type: 'list'
#
# 5. What is the difference between a set and a frozenset? Why is frozenset
#    hashable while a regular set is not?
#
#    ANSWER: A set is mutable (add, remove, update, etc.), while a frozenset is
#    immutable: once created, its contents can never change. Both support the
#    same read-only operations (in, |, &, -, ^, subset checks). Because a
#    frozenset's contents are fixed, its hash can be computed once and will
#    always stay valid, so Python makes it hashable. A regular set's
#    contents (and so its hash) could change at any time, so it is
#    deliberately unhashable.
#
# 6. How would you remove duplicates from a list while PRESERVING the
#    original order of first occurrence? Why doesn't simply calling
#    list(set(my_list)) achieve this?
#
#    ANSWER: Use list(dict.fromkeys(my_list)). Dict keys are unique AND
#    dicts preserve insertion order (guaranteed since Python 3.7), so the
#    first occurrence of each value is kept in its original position:
#        list(dict.fromkeys([3, 1, 3, 2, 1]))  -> [3, 1, 2]
#    list(set(my_list)) removes duplicates too, but sets are unordered, so
#    the resulting order follows the hash table, not the original list.
#    An alternative is a loop with a "seen" set:
#        seen, result = set(), []
#        for x in my_list:
#            if x not in seen:
#                seen.add(x)
#                result.append(x)
#
# 7. What is the difference between the `|` operator and the `.update()`
#    method when combining two sets? Which one mutates the original set?
#
#    ANSWER: `a | b` creates and returns a NEW set; a and b are unchanged.
#    `a.update(b)` (same as `a |= b`) adds b's elements INTO a, modifying a
#    in place and returning None. So update() mutates the original.
#    Extra detail: `|` requires both operands to be sets, while update()
#    (and union()) accept any iterable, e.g. a.update([4, 5]).
#
# 8. What do the `<=`, `<`, `>=`, and `>` operators mean when used between
#    two sets? How are they different from numeric comparison?
#
#    ANSWER: Between sets they test containment, not size or value:
#      a <= b  -> a is a SUBSET of b (every element of a is in b)
#      a <  b  -> a is a PROPER subset (subset, and a != b)
#      a >= b  -> a is a SUPERSET of b
#      a >  b  -> a is a PROPER superset
#    Unlike numbers, sets are only PARTIALLY ordered: for {1, 2} and {3, 4},
#    a <= b, a >= b, and a == b are ALL False, because neither contains
#    the other. With numbers, one of <, ==, > is always True.
#
# 9. What does `a.isdisjoint(b)` check for two sets a and b?
#
#    ANSWER: It returns True if a and b have NO elements in common, i.e.
#    their intersection is empty. {1, 2}.isdisjoint({3, 4}) -> True,
#    {1, 2}.isdisjoint({2, 3}) -> False.
#
# 10. Can you use a set as a dictionary key? Can you use a frozenset as a
#     dictionary key? Explain the difference.
#
#    ANSWER: A set CANNOT be a dict key, because dict keys must be hashable
#    and sets are mutable/unhashable (TypeError: unhashable type: 'set').
#    A frozenset CAN be a dict key, because it is immutable and hashable.
#        d = {frozenset([1, 2]): "pair"}   # works
#        d = {{1, 2}: "pair"}              # TypeError
#
# 11. Is it safe to rely on the iteration order of a set staying consistent
#     across Python versions or runs? Why or why not?
#
#    ANSWER: No. Set order is an implementation detail of the hash table and
#    is not guaranteed by the language. It can change between Python
#    versions, after elements are added/removed, and even between runs of
#    the same program: string hashes are randomized per process (hash
#    randomization, controlled by PYTHONHASHSEED), so a set of strings can
#    print in a different order every time you run the script. If order
#    matters, use sorted(s), a list, or dict.fromkeys().
#
# 12. How would you find all elements common to THREE different lists using
#     set operations, in a single expression?
#
#    ANSWER:
#        common = set(list1) & set(list2) & set(list3)
#    or equivalently:
#        common = set(list1).intersection(list2, list3)
#    (intersection() accepts any iterables, so list2/list3 don't need
#    converting first.)
#
# 13. What is a set comprehension, and how is its syntax different from a
#     list comprehension?
#
#    ANSWER: A set comprehension builds a set from an expression in one line,
#    automatically removing duplicates. The only syntax difference is the
#    brackets: curly braces {} instead of square brackets [].
#        [x % 3 for x in range(6)]  -> [0, 1, 2, 0, 1, 2]   (list)
#        {x % 3 for x in range(6)}  -> {0, 1, 2}            (set)
#    A dict comprehension also uses {}, but has a key: value pair:
#        {x: x**2 for x in range(3)}
#
# 14. What happens if you try to create an "empty set" using `{}`? What does
#     `{}` actually create in Python?
#
#    ANSWER: {} creates an empty DICTIONARY, not a set; type({}) is dict.
#    This is because dicts were in Python before sets, so {} was already
#    taken. To create an empty set you must use set().
#
# 15. What is the time complexity of adding an element to a set versus
#     inserting into a sorted list while maintaining sort order?
#
#    ANSWER: set.add(x) is O(1) on average (hash and place it).
#    Inserting into a sorted list is O(n): finding the position with
#    bisect is O(log n), but list.insert() must then shift every later
#    element one place to the right, which is O(n). The trade-off is that
#    the set has no order, while the list stays sorted.
#
# 16. Given two sets representing "students in class A" and "students in
#     class B", how would you find students in EITHER class but NOT both
#     (i.e., exactly one of the two)?
#
#    ANSWER: Use symmetric difference:
#        only_one = class_a ^ class_b
#    or class_a.symmetric_difference(class_b). It's equivalent to
#    (class_a | class_b) - (class_a & class_b).
#    e.g. {"Alice","Bob","Charlie"} ^ {"Bob","Charlie","David"}
#         -> {'Alice', 'David'}
#
# 17. Why can't a set contain another (mutable) set as an element, but it CAN
#     contain a frozenset?
#
#    ANSWER: Set elements must be hashable. A regular set is mutable, so its
#    hash could change after being stored, which would make the outer set
#    unable to locate it; Python therefore makes sets unhashable and
#    {{1, 2}} raises TypeError. A frozenset is immutable, so its hash is
#    fixed and it can safely be stored: {frozenset([1, 2])} works.
#
# 18. What's the difference between set.intersection_update(other) and
#     set.intersection(other)? Which one modifies the original set?
#
#    ANSWER: a.intersection(b) returns a NEW set with the common elements;
#    a is unchanged. a.intersection_update(b) (same as a &= b) modifies a
#    IN PLACE so that it keeps only the common elements, and returns None.
#    So intersection_update() modifies the original.
#
# 19. How would you check if two sets share NO elements in common, without
#     manually computing their intersection first?
#
#    ANSWER: Use a.isdisjoint(b). It returns True if there's no overlap,
#    and it is more efficient than `not (a & b)` because it doesn't build a
#    new intersection set and can stop as soon as it finds one shared
#    element. It also accepts any iterable: a.isdisjoint([5, 6]).
#
# 20. Why are sets generally preferred over lists for tasks like removing
#     duplicates or checking "does this exist" in performance-sensitive code?
#
#    ANSWER:
#      - Membership checks: O(1) average for a set vs O(n) for a list.
#        Doing this inside a loop turns an O(n^2) list algorithm into O(n).
#      - Duplicates: a set rejects them automatically, so set(my_list) is a
#        one-step, O(n) dedupe.
#      - Set algebra (|, &, -, ^) expresses "common", "missing", and
#        "combined" logic clearly and efficiently.
#    Use a list instead when you need order, indexing, or duplicates.