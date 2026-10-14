# ==============================================================================
#  COPY SEMANTICS, IDENTITY & MUTABILITY
# ==============================================================================
"""
NOTES:
- Mutable: list, dict, set (can change in place). Immutable: int, str, tuple,
  frozenset (any "change" creates a new object).
- '==' checks VALUE equality. 'is' checks IDENTITY (same object in memory,
  same id()).
- Shallow copy (copy.copy): copies the outer object, but nested objects are
  still SHARED references. Deep copy (copy.deepcopy): recursively copies
  everything, fully independent.
- Small int caching: Python caches ints -5 to 256 and short strings, so
  `a = 5; b = 5; a is b` is True due to this internal optimization - not
  something to rely on for larger numbers.
"""
import copy
def copy_semantics_demo():
    print("\n--- COPY SEMANTICS, IDENTITY & MUTABILITY ---")

    a = [1, 2, 3]
    b = [1, 2, 3]
    print("a == b:", a == b, "| a is b:", a is b)  # True, False (different objects)
     # a == b: True | a is b: False

    c = a
    print("c = a; c is a:", c is a)  # True (same object, just another reference)
    # c = a; c is a: True

    original = [1, [2, 3], 4]
    # Shallow copy
    shallow = copy.copy(original)
    # deep copy
    deep = copy.deepcopy(original)

    original[1].append(99)  # mutate the nested list
    print("original:", original) # [1, [2, 3, 99], 4]
    print("shallow (nested list AFFECTED - shared reference):", shallow) # [1, [2, 3, 99], 4]
    print("deep (nested list NOT affected - fully independent):", deep) # [1, [2, 3], 4]

    # Small int caching example
    x, y = 5, 5
    print("small int caching: x is y ->", x is y)  # True
    big1, big2 = 1000, 1000
    print("big int (may or may not be cached, don't rely on it): big1 is big2 ->", big1 is big2) # True


if __name__ == "__main__":
    copy_semantics_demo()


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. id() - the actual identity behind 'is'
# -------------------------
# 'is' compares the result of id() under the hood - id() returns a unique
# integer that represents the object's identity (in CPython, this is the
# object's memory address, though that's an implementation detail).
a = [1, 2, 3]
b = a
print(id(a), id(b), id(a) == id(b))   # same id -> a is b would be True
print(a is b)                           # True -> equivalent to id(a) == id(b)

print(f"{'*' * 60}")

# -------------------------
# 2. Ways to copy a list/dict WITHOUT the copy module (common shortcuts)
# -------------------------
original = [1, 2, 3]
copy1 = original[:]           # full slice - creates a shallow copy
copy2 = list(original)        # constructor call - also a shallow copy
copy3 = original.copy()       # .copy() method (lists, dicts, sets all have this) - shallow copy

original.append(4)
print(original)   # [1, 2, 3, 4]
print(copy1)        # [1, 2, 3] -> unaffected, since it's a NEW top-level list

# same idea for dict:
d1 = {"a": 1, "b": 2}
d2 = d1.copy()          # shallow copy
d3 = dict(d1)             # also shallow copy
d1["a"] = 999
print(d2)                 # {'a': 1, 'b': 2} -> unaffected at the top level

print(f"{'*' * 60}")

# -------------------------
# 3. Shallow copy STILL shares nested mutable objects - proven with a dict of lists
# -------------------------
nested = {"fruits": ["apple", "banana"]}
shallow_dict = nested.copy()
shallow_dict["fruits"].append("cherry")   # mutates the SHARED inner list
print(nested)          # {'fruits': ['apple', 'banana', 'cherry']} -> also changed!
print(shallow_dict)     # {'fruits': ['apple', 'banana', 'cherry']}
# This is the #1 real-world bug caused by misunderstanding shallow copy.

print(f"{'*' * 60}")

# -------------------------
# 4. Tuples containing mutable objects - a subtle immutability nuance
# -------------------------
# A tuple is immutable, meaning you can't REASSIGN its slots - but if a slot
# holds a mutable object, THAT object can still be mutated in place!
t = (1, [2, 3], 4)
# t[1] = [99]      # TypeError: 'tuple' object does not support item assignment
t[1].append(100)    # this works! we're mutating the LIST inside the tuple, not the tuple itself
print(t)              # (1, [2, 3, 100], 4)

print(f"{'*' * 60}")

# -------------------------
# 5. Mutability affects hashability - a common dict/set key interview question
# -------------------------
# Mutable objects (list, dict, set) are UNHASHABLE - they can't be dict keys
# or set members, because their hash would change if their content changes.
d = {}
# d[[1, 2, 3]] = "value"      # TypeError: unhashable type: 'list'
d[(1, 2, 3)] = "value"          # tuple works fine - it's immutable (as long as its
                                  # contents are also immutable/hashable)
print(d)                          # {(1, 2, 3): 'value'}

# a tuple CONTAINING a mutable object is still unhashable!
# d[(1, [2, 3])] = "value"       # TypeError: unhashable type: 'list'
print(hash((1, 2, 3)))             # works - all elements are immutable
# print(hash((1, [2, 3])))         # TypeError - fails because of the nested list

print(f"{'*' * 60}")

# -------------------------
# 6. Function arguments and mutability - "pass by object reference" (not
#    strictly pass-by-value or pass-by-reference, a very common interview
#    theory question)
# -------------------------
def modify_list(lst):
    lst.append(100)     # mutates the SAME object the caller passed in

def reassign_list(lst):
    lst = [999]           # REBINDS the local name 'lst' to a new object -
                            # does NOT affect the caller's variable at all

nums = [1, 2, 3]
modify_list(nums)
print(nums)     # [1, 2, 3, 100] -> caller sees the mutation

nums2 = [1, 2, 3]
reassign_list(nums2)
print(nums2)     # [1, 2, 3] -> unaffected, because reassignment inside the
                   # function only rebinds the LOCAL name, not the caller's variable

print(f"{'*' * 60}")

# -------------------------
# 7. copy.deepcopy() with custom objects and circular references
# -------------------------
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

n1 = Node(1)
n2 = Node(2, n1)
n1.next = n2   # create a CIRCULAR reference: n1 -> n2 -> n1

deep_copied = copy.deepcopy(n1)   # deepcopy correctly handles cycles internally
                                    # (it keeps a memo dict of already-copied objects)
print(deep_copied.value, deep_copied.next.value)   # 1 2
print(deep_copied is n1)                              # False -> fully independent copy

print(f"{'*' * 60}")

# -------------------------
# 8. Customizing copy behavior with __copy__ and __deepcopy__ dunders
# -------------------------
class Config:
    def __init__(self, settings):
        self.settings = settings

    def __copy__(self):
        print("Custom __copy__ called")
        new_obj = Config(self.settings)   # custom shallow-copy logic
        return new_obj

    def __deepcopy__(self, memo):
        print("Custom __deepcopy__ called")
        new_obj = Config(copy.deepcopy(self.settings, memo))
        return new_obj

cfg = Config({"debug": True})
cfg_shallow = copy.copy(cfg)         # uses our __copy__ override
cfg_deep = copy.deepcopy(cfg)         # uses our __deepcopy__ override

print(f"{'*' * 60}")

# -------------------------
# 9. Reference counting and garbage collection (relevant to "why does Python
#    manage memory the way it does")
# -------------------------
import sys
x = []
print(sys.getrefcount(x))   # includes +1 for the temporary reference passed to getrefcount() itself
y = x
print(sys.getrefcount(x))   # increased by 1, since 'y' is now also referencing the same object
del y
print(sys.getrefcount(x))   # back down - one less reference

# CPython uses reference counting as its primary memory management strategy,
# plus a generational garbage collector to catch reference CYCLES (like the
# Node example above) that reference counting alone can't clean up.

print(f"{'*' * 60}")

# -------------------------
# 10. weakref - references that DON'T increase the reference count (advanced,
#     but a good "I know this" answer for senior-level interviews)
# -------------------------
import weakref

class Resource:
    pass

res = Resource()
weak_ref = weakref.ref(res)     # doesn't keep 'res' alive on its own
print(weak_ref())                 # <__main__.Resource object at ...> -> still alive, strong ref exists
del res
print(weak_ref())                  # None -> object was garbage collected once the only strong ref was deleted

print(f"{'*' * 60}")

# -------------------------
# 11. == vs is - practical guidance recap
# -------------------------
# Use '==' to compare VALUES (almost always what you want).
# Use 'is' ONLY for:
#   - comparing to None / True / False (singletons)
#   - checking if two variables reference the EXACT SAME object (rare, intentional)
value = None
if value is None:      # correct
    print("value is None")

a = [1, 2]
b = [1, 2]
print(a == b)   # True  -> use this to compare contents
print(a is b)    # False -> different objects, would be wrong to rely on this for equality


## ==========================================================
## INTERVIEW QUESTIONS ON COPY SEMANTICS, IDENTITY & MUTABILITY
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is the difference between '==' and 'is' in Python? Give an example
#    where they produce different results for two "equal-looking" objects.
#
# 2. What is the difference between a shallow copy and a deep copy? Give an
#    example where a shallow copy leads to an unintended shared mutation.
#
# 3. What are three different ways to create a shallow copy of a list in
#    Python?
#
# 4. Why can a tuple contain a list, yet still be considered "immutable"?
#    Doesn't mutating that inner list violate immutability?
#
# 5. Why are lists and dicts unhashable, and why does that matter for using
#    them as dictionary keys or set members?
#
# 6. Is Python "pass by value" or "pass by reference"? What is the more
#    accurate description of Python's argument-passing model?
#
# 7. If you mutate a list inside a function (e.g., lst.append(x)), does the
#    caller see the change? What if you reassign the parameter instead
#    (e.g., lst = [])? Why the difference?
#
# 8. How does copy.deepcopy() handle objects with circular references (e.g., a
#    linked list node that points back to itself)? What would happen with a
#    naive recursive copy implementation instead?
#
# 9. How would you customize what copy.copy() or copy.deepcopy() does for your
#    own class? What dunder methods would you implement?
#
# 10. What is reference counting, and how does CPython use it for memory
#     management? What kind of memory leak can reference counting alone NOT
#     detect?
#
# 11. What is a weak reference (weakref), and when would you use one instead
#     of a normal (strong) reference?
#
# 12. Why does Python cache small integers (-5 to 256)? What could go wrong if
#     you relied on 'is' to compare two larger integers for equality?
#
# 13. What does id() return, and how is it related to the 'is' operator?
#
# 14. If a and b are two lists with identical contents, what does a == b
#     return, and what does a is b return? Explain the difference in what
#     each operator checks.
#
# 15. What's the difference between list.copy(), list(original), and
#     original[:]? Are they functionally equivalent?
#
# 16. Give a real-world example of a bug caused by using a shallow copy when a
#     deep copy was needed (e.g., copying a config dict containing nested
#     lists/dicts).
#
# 17. What happens when you do `b = a` for two mutable objects like lists?
#     Does this create a copy? How would you verify your answer using id()?
#
# 18. Why must dictionary keys be hashable (and therefore typically immutable)?
#     What would break if Python allowed mutable dict keys?
#
# 19. What is the performance cost of copy.deepcopy() on a very large, deeply
#     nested data structure? When might a shallow copy or no copy at all be a
#     better choice?
#
# 20. How does the `del` statement relate to reference counting and garbage
#     collection? Does `del x` guarantee the object is immediately destroyed?