"""
list in Python

A list is an ordered, mutable collection of items. It's probably the most commonly used data structure in
    Python — flexible enough to hold almost anything.

    - Ordered — items maintain a defined position (indexed)
    - Mutable — you can change, add, remove elements after creation
    - Allows duplicates — same value can appear multiple times
    - Can hold mixed data types — ints, strings, other lists, etc. all in one list
"""
l1 = [1, 2, 3, 4]
l2 = ["apple", "banana", "cherry"]
l3 = [1, "hello", 3.14, True]      # mixed types allowed
l4 = []                            # empty list
l5 = list()                        # also empty list
l6 = list((1, 2, 3))               # convert a tuple to a list

# list data type
l = ['India', 10, 20.33, "hello", 55, 66]

# +ve indexing numbers
#   [0        1  2         3       4   5]
# +ve indexing numbers
#   [-6        -5  -4         -3       -2   -1]
print(type(l))  # <class 'list'>

# slicing used to access particular elements in list
print(l[1:4])   # [10, 20.33, 'hello']
print(l[-1])    # 66
print(l[-3: -1])    # ['hello', 55]

## indexing
print(l[0])     # India
print(type(l[0]))   # <class 'str'>
# changing the value of the index
print(l)
l[1] = "changed"
print(l)    # ['India', 'changed', 20.33, "hello", 55, 66]

# inserting new item at specified index
l.insert(6, "new value")
print(l)    # ['India', 'changed', 20.33, "hello", 55, 66, 'new value']
'''
l = [1, 2, 3]
l.append(4)          # adds single item to the end
print(l)              # [1, 2, 3, 4]

l.insert(1, 99)       # inserts 99 at index 1
print(l)              # [1, 99, 2, 3, 4]

l.extend([5, 6])      # adds multiple items to the end
print(l)              # [1, 99, 2, 3, 4, 5, 6]

l = [1, 2, 3]
l.append([4, 5])      # adds the WHOLE list as a single item
print(l)               # [1, 2, 3, [4, 5]]

l = [1, 2, 3]
l.extend([4, 5])       # adds EACH item individually
print(l)                # [1, 2, 3, 4, 5]
'''
# removing item by item name
l.remove("hello")
print(l)

# remove item by index using pop()
l.pop(1)
print(l)

"""
l = [1, 2, 3, 4, 5]

l.remove(3)      # removes first occurrence of the VALUE 3
print(l)          # [1, 2, 4, 5]

l.pop()           # removes and returns the LAST item
print(l)          # [1, 2, 4]

l.pop(0)          # removes and returns item at index 0
print(l)          # [2, 4]

del l[0]          # deletes item at given index
l.clear()         # empties the entire list
"""

# Common methods
l = [3, 1, 4, 1, 5, 9, 2]

len(l)          # 7 — length
l.count(1)      # 2 — how many times 1 appears
l.index(4)      # 2 — position of first occurrence of 4
l.sort()        # sorts in place → [1, 1, 2, 3, 4, 5, 9] # modifies original list
l.reverse()     # reverses in place
sorted(l)       # returns a NEW sorted list, doesn't modify original


# Membership check
l = [1, 2, 3]
print(2 in l)    # True
print(10 in l)   # False


# iterating through list and print index and item
for value in range(len(l)):
    print(value, ':', l[value])

l1 = [(i, v) for i, v in enumerate(l)]
print(l1)

## concatination of sequences
a = [0, 1, 2, 3, 4]
b = [6, 7, 8, 9, 10]
print(a + b)

# TypeError: can only concatenate list (not "str") to list
#print(a + "Hello")


def fun():
    l = [n**2 for n in [1,2,3,4,5]]
    print(l) # [1, 4, 9, 14, 25]
fun()

def fun():
    l = [i for i in "python"]
    print(l) # ['p','y','t','h','o','n']
fun()

def fun():
    l = [n for n in range(30) if n % 2 != 0]    # odd numbers
    print(l) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
fun()

def fun():
    l = [n for n in range(30) if n % 2 == 0]    # even numbers
    print(l)
fun()

def fun():
    l = [[i+j for i in range(5)] for j in range(3)]
    print(l)    # [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
fun()
"""
l1 = []
for j in range(3):
    r = []
    for i in range(5):
        r.append(i+j)
    l1.append(r)
print(l1)
"""

print('---------')
d = []
for i in range(10):
    d.append(i)
    print(d)
print()
print(d)
"""
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
******************************
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

#-----------------------------------------------------------
# List comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
evens = [x for x in range(10) if x % 2 == 0]
print(evens)    # [0, 2, 4, 6, 8]

#-----------------------------------------------------------
# Nested lists (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # 6 — row 1, column 2

#-----------------------------------------------------------
# Copying a list — the classic pitfall
a = [1, 2, 3]
b = a              # b points to SAME list — not a copy!
b.append(4)
print(a)            # [1, 2, 3, 4] — a changed too!

# 1 - Shallow copy
# To make an actual copy:
c = a.copy()         # or a[:] or list(a)
c.append(5)
print(a)              # [1, 2, 3, 4] - unaffected

# 2 - Deep copy
# Use copy.deepcopy() to copy everything, including nested objects:
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)
print(a)   # [[1, 2], [3, 4]]      <- unaffected!
print(b)   # [[1, 2, 99], [3, 4]]

"""
Method	                    Type	                    Nested lists shared?
b = a	                    Reference (not a copy)	    Yes (same object)
b = a.copy()	            Shallow copy	            Yes
b = a[:]	                Shallow copy	            Yes
b = list(a)	                Shallow copy	            Yes
b = copy.deepcopy(a)	    Deep copy	                No
"""

"""
List vs Tuple — quick comparison
Feature	            List	            Tuple
---------           ----------          -----------
Mutable?	        ✅ Yes	            ❌ No
Syntax	            [1, 2, 3]	        (1, 2, 3)
Speed	            Slower	            Faster
Use as dict key?	❌ No	            ✅ Yes
Common use	        Data that changes	Fixed data
"""
"""
Quick summary
Feature	                List
---------------         --------------------------------
Ordered?	            ✅ Yes
Indexed?	            ✅ Yes
Mutable?	            ✅ Yes
Duplicates allowed?	    ✅ Yes
Common use	            General-purpose, dynamic collections that grow/shrink/change
"""


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION
## ==========================================================

# -------------------------
# 1. Slicing in depth - step, negative step, and slice assignment
# -------------------------
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[::2])       # [0, 2, 4, 6, 8] -> every 2nd element
print(nums[1::2])       # [1, 3, 5, 7, 9] -> every 2nd starting from index 1
print(nums[::-1])        # [9,8,7,6,5,4,3,2,1,0] -> reversed copy (doesn't mutate original)
print(nums[::-2])         # [9, 7, 5, 3, 1] -> reversed, every 2nd

# Slice ASSIGNMENT - can replace a chunk of the list (even with a different length!)
nums2 = [1, 2, 3, 4, 5]
nums2[1:3] = [99, 100, 101]   # replaces 2 elements with 3 -> list GROWS
print(nums2)                    # [1, 99, 100, 101, 4, 5]

nums3 = [1, 2, 3, 4, 5]
del nums3[1:3]                   # deletes a whole slice at once
print(nums3)                       # [1, 4, 5]

print(f"{'*' * 60}")

# -------------------------
# 2. List repetition (*) and the classic nested-list SHARED REFERENCE trap
# -------------------------
repeated = [0] * 5
print(repeated)          # [0, 0, 0, 0, 0] -> fine, ints are immutable, no sharing issue

# DANGER: repeating a MUTABLE object (like an inner list) shares ONE object!
grid_buggy = [[0] * 3] * 3     # creates 3 REFERENCES to the SAME inner list!
print(grid_buggy)       # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
grid_buggy[0][0] = 99
print(grid_buggy)                 # [[99,0,0],[99,0,0],[99,0,0]] -> BUG! all rows changed

# CORRECT way to build a 2D grid - a fresh list for each row:
grid_fixed = [[0] * 3 for _ in range(3)]   # list comprehension creates a NEW list each iteration
print(grid_fixed)       # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
grid_fixed[0][0] = 99
print(grid_fixed)                            # [[99,0,0],[0,0,0],[0,0,0]] -> only row 0 changed, correct!

print(f"{'*' * 60}")

# -------------------------
# 3. Sorting with key= and reverse= (recap, tailored to list.sort())
# -------------------------
words = ["banana", "kiwi", "apple", "fig"]
words.sort(key=len)                # sort in place by string length
print(words)                          # ['fig', 'kiwi', 'apple', 'banana']
words.sort(key=len, reverse=True)    # longest first
print(words)                            # ['banana', 'apple', 'kiwi', 'fig']

print(f"{'*' * 60}")

# -------------------------
# 4. List comprehension with MULTIPLE conditions, if-else, and nested loops
# -------------------------
# multiple 'if' conditions (acts like AND)
nums4 = [x for x in range(30) if x % 2 == 0 if x % 3 == 0]
print(nums4)   # [0, 6, 12, 18, 24] -> divisible by BOTH 2 and 3

# if-else INSIDE the expression (different from a filtering 'if' at the end!)
labeled = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labeled)   # ['even', 'odd', 'even', 'odd', 'even']

# nested loops in a single comprehension (flattening a matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"{'*' * 60}")

# -------------------------
# 5. Extended unpacking with * when assigning from a list
# -------------------------
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)   # 1 [2, 3, 4] 5

a, b, *rest = [10, 20, 30, 40]
print(a, b, rest)              # 10 20 [30, 40]

print(f"{'*' * 60}")

# -------------------------
# 6. List as a stack vs queue - performance implications (VERY common interview point)
# -------------------------
# STACK (LIFO) - list works great, both ends are O(1) at the END:
stack = []
stack.append(1)     # push -> O(1)
stack.append(2)
print(stack.pop())    # pop from end -> O(1)

# QUEUE (FIFO) - list is a BAD choice for this!
queue = [1, 2, 3]
# queue.pop(0)       # removes from the FRONT -> O(n)! every remaining item must shift left
# INSERT at the front is also O(n):
# queue.insert(0, 0)  # O(n)

# Use collections.deque instead for O(1) operations at BOTH ends:
from collections import deque
queue2 = deque([1, 2, 3])
queue2.popleft()   # O(1) -> deque is a doubly linked list internally

print(f"{'*' * 60}")

# -------------------------
# 7. Time complexity cheat-sheet for common list operations
# -------------------------
"""
Operation                  Time Complexity
------------------------   ------------------
index access lst[i]        O(1)
append(x)                  O(1) amortized
pop() (from end)            O(1)
pop(0) (from front)          O(n)
insert(0, x) (front)          O(n)
insert(i, x) (middle)          O(n)
remove(x)                       O(n) - must search for the value first
x in lst (membership test)       O(n)
len(lst)                           O(1) - length is cached, not recomputed
lst.sort()                          O(n log n) - Timsort
lst[a:b] (slicing)                    O(k) - k = size of the slice
"""

print(f"{'*' * 60}")

# -------------------------
# 8. copy() vs deepcopy() - recap specific to nested lists
# -------------------------
import copy
nested = [1, [2, 3], 4]
shallow = nested.copy()          # or nested[:] or list(nested)
deep = copy.deepcopy(nested)

nested[1].append(99)              # mutate the NESTED list
print(nested)                       # [1, [2, 3, 99], 4]
print(shallow)                        # [1, [2, 3, 99], 4] -> AFFECTED, shares the inner list
print(deep)                             # [1, [2, 3], 4]     -> NOT affected, fully independent

print(f"{'*' * 60}")

# -------------------------
# 9. enumerate() and zip() with lists - very common in real code and interviews
# -------------------------
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):        # gives (index, value) pairs
    print(index, fruit)
"""
0 apple
1 banana
2 cherry
"""

for i, fruit in enumerate(fruits, start=1):    # can start counting from a custom number
    print(i, fruit)

"""
1 apple
2 banana
3 cherry
"""

names = ["Alice", "Bob"]
ages = [30, 25]
for name, age in zip(names, ages):              # pairs elements from multiple lists together
    print(name, age)
"""
Alice 30
Bob 25
"""

# zip() stops at the SHORTEST iterable - no error, just truncates silently
print(list(zip([1, 2, 3], ["a", "b"])))            # [(1, 'a'), (2, 'b')] -> 3 is dropped, no error!

print(f"{'*' * 60}")

# -------------------------
# 10. bisect module - efficient insertion/search in an ALREADY SORTED list
# -------------------------
import bisect
sorted_list = [1, 3, 4, 4, 6, 8]
pos = bisect.bisect_left(sorted_list, 4)     # finds the LEFTMOST position to insert 4
print(pos)                                     # 2

bisect.insort(sorted_list, 5)                   # inserts 5 while KEEPING the list sorted
print(sorted_list)                                # [1, 3, 4, 4, 5, 6, 8]
# bisect operations are O(log n) for the SEARCH part (binary search), but the
# actual insertion is still O(n) because the rest of the list must shift.

print(f"{'*' * 60}")

# -------------------------
# 11. List equality vs identity (recap tailored to lists specifically)
# -------------------------
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)   # True  -> same VALUES
print(l1 is l2)    # False -> different OBJECTS in memory

# nested equality also works recursively:
print([1, [2, 3]] == [1, [2, 3]])   # True -> compares nested structures element by element


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON LISTS
## ==========================================================

# 1. What is the time complexity of appending to the END of a list versus
#    inserting/removing at the FRONT of a list? Why the difference?
#
# ANSWER:
# append() at the end is O(1) amortized because Python lists are backed by a
# dynamic array with extra pre-allocated capacity at the end, so most appends
# just place the item in existing free space. Inserting/removing at the FRONT
# (insert(0, x), pop(0)) is O(n) because every other element must be shifted
# one position to make room / fill the gap.
#
# 2. Why is `[[0] * 3] * 3` a common bug when trying to create a 2D grid/
#    matrix? What's the correct way to create an independent 2D list?
#
# ANSWER:
# `[[0]*3]*3` creates ONE inner list `[0,0,0]` and then repeats a REFERENCE to
# that same list 3 times, so all "rows" point to the same object — mutating
# one row mutates all of them. The correct way is to build a new inner list
# on each iteration: `[[0]*3 for _ in range(3)]`, which calls the list
# constructor fresh each time, producing independent objects.
#
# 3. What is the difference between list.sort() and sorted()? Which one
#    returns None, and what mistake does that commonly cause?
#
# ANSWER:
# list.sort() sorts the list IN PLACE and returns None; sorted() returns a
# NEW sorted list and leaves the original untouched (works on any iterable,
# not just lists). A common mistake is writing `my_list = my_list.sort()`,
# which sets my_list to None because sort() doesn't return the sorted list.
#
# 4. How would you reverse a list without using the built-in reverse() method
#    or [::-1] slicing?
#
# ANSWER:
# Swap elements from both ends toward the middle:
#     lst = [1, 2, 3, 4, 5]
#     left, right = 0, len(lst) - 1
#     while left < right:
#         lst[left], lst[right] = lst[right], lst[left]
#         left += 1
#         right -= 1
# This reverses the list in place in O(n) time using only index swaps.
# --- or ---
# def reverse_list(lst):
#     result = []
#     for item in lst:
#         result.insert(0, item)
#     return result
#
# 5. What does slice assignment do (e.g., `lst[1:3] = [10, 20, 30]`)? Can it
#    change the overall LENGTH of the list?
#
# ANSWER:
# Slice assignment replaces the elements in the given slice range with the
# elements of the assigned iterable. The number of items assigned does NOT
# need to match the number of items in the slice, so YES, it can grow or
# shrink the list. E.g. `lst[1:3] = [10, 20, 30]` replaces 2 elements with 3,
# so the list grows by one item.
#
# 6. Why is `collections.deque` generally preferred over a plain list when
#    implementing a queue (FIFO)? What specific list operation is the
#    bottleneck?
#
# ANSWER:
# A plain list is a dynamic array, so removing/inserting at the FRONT
# (pop(0) / insert(0, x)) is O(n) because all remaining elements must shift.
# deque is implemented as a doubly linked structure (blocks), giving O(1)
# operations at BOTH ends (appendleft/popleft as well as append/pop), making
# it the right choice for FIFO queues.
#
# 7. What is the difference between list.remove(x) and list.pop(i)? What
#    happens if the value passed to remove() doesn't exist in the list?
#
# ANSWER:
# remove(x) deletes the FIRST occurrence of the VALUE x (searches by value,
# returns None). pop(i) removes and RETURNS the item at index i (defaults to
# the last item if no index given). If the value passed to remove() isn't
# found in the list, it raises a ValueError.
#
# 8. How would you flatten a nested list of lists into a single flat list
#    using a list comprehension?
#
# ANSWER:
# Use a nested-loop comprehension:
#     flat = [num for row in matrix for num in row]
# The outer `for row in matrix` iterates rows first, then the inner
# `for num in row` iterates each element within that row.
#
# 9. What does zip() do when given lists of DIFFERENT lengths? Does it raise
#    an error?
#
# ANSWER:
# zip() stops as soon as the SHORTEST iterable is exhausted, silently
# truncating the extra elements from longer iterables — it does NOT raise an
# error. (Python 3.10+ offers `zip(..., strict=True)` if you want it to raise
# a ValueError on length mismatch instead.)
#
# 10. What is the difference between a shallow copy and a deep copy of a
#     nested list? Give an example where a shallow copy leads to unintended
#     shared mutation.
#
# ANSWER:
# A shallow copy (list.copy(), lst[:], list(lst)) creates a new OUTER list
# but the inner objects (e.g., nested lists) are still shared references. A
# deep copy (copy.deepcopy()) recursively copies every nested object so the
# result is fully independent. Example:
#     nested = [1, [2, 3], 4]
#     shallow = nested.copy()
#     nested[1].append(99)
#     print(shallow)   # [1, [2, 3, 99], 4] -> affected, shares inner list
#
# 11. What is the bisect module used for? Why would bisect.insort() be more
#     efficient than appending and then re-sorting the whole list?
#
# ANSWER:
# The bisect module provides binary-search-based utilities for efficiently
# finding insertion points in / inserting into an ALREADY SORTED list.
# bisect.insort() locates the correct position in O(log n) via binary search
# and inserts it there, keeping the list sorted, in roughly O(n) overall
# (due to the shift). Appending then re-sorting the whole list is O(n log n)
# every time, which is far more expensive for repeated insertions.
#
# 12. What's the time complexity of checking `x in my_list` for a list with n
#     elements? How does this compare to checking membership in a set?
#
# ANSWER:
# `x in my_list` is O(n) because Python must scan elements one by one until
# it finds a match (or reaches the end). Checking membership in a set (or
# dict) is O(1) average case because sets use hashing to locate elements
# directly, making sets/dicts much faster for frequent membership checks.
#
# 13. How would you remove duplicates from a list while preserving the
#     original order of first occurrence?
#
# ANSWER:
# Use a helper set to track seen items while building a new list:
#     def dedupe(lst):
#         seen = set()
#         result = []
#         for item in lst:
#             if item not in seen:
#                 seen.add(item)
#                 result.append(item)
#         return result
# (A plain `list(set(lst))` removes duplicates but does NOT preserve order.
# In Python 3.7+, `list(dict.fromkeys(lst))` also works and preserves order.)
#
# 14. What does extended unpacking like `first, *rest = my_list` do? What
#     type is `rest`?
#
# ANSWER:
# `first` is assigned the first element, and `*rest` captures ALL the
# remaining elements into a new list (the `*` can appear anywhere in the
# unpacking, e.g. `first, *middle, last`). `rest` is always of type `list`,
# even if it ends up empty.
#
# 15. What is the difference between list.append(x) and list.extend(iterable)?
#     What happens if you accidentally use append() when you meant extend()?
#
# ANSWER:
# append(x) adds x as a SINGLE item to the end of the list (even if x is
# itself a list). extend(iterable) adds EACH item of the iterable
# individually to the end. Using append() when you meant extend() results in
# a nested list instead of a flat one, e.g. `[1,2,3].append([4,5])` gives
# `[1, 2, 3, [4, 5]]` instead of the intended `[1, 2, 3, 4, 5]`.
#
# 16. Why does `my_list.sort()` return None instead of the sorted list? What
#     design principle does this follow (compare with sorted())?
#
# ANSWER:
# sort() mutates the list in place and returns None as a deliberate Python
# design convention: methods that mutate an object in place return None so
# it's clear (and hard to accidentally chain) that they don't produce a new
# object — the same convention applies to list.reverse(), list.sort(), and
# dict.update(). sorted(), in contrast, is a pure function that returns a
# brand-new sorted list/iterable without mutating the input.
#
# 17. How would you efficiently find the index of the first element in a
#     SORTED list that is greater than or equal to a target value?
#
# ANSWER:
# Use bisect.bisect_left(sorted_list, target). It performs a binary search
# in O(log n) and returns the leftmost insertion index where target could go
# to keep the list sorted — which is exactly the index of the first element
# >= target (or len(list) if all elements are smaller).
#
# 18. What happens internally when a Python list needs to grow beyond its
#     current allocated capacity (why is append() described as "O(1)
#     amortized" rather than strictly O(1))?
#
# ANSWER:
# Python lists over-allocate memory: when the underlying array is full,
# CPython allocates a NEW, larger block (growing by roughly ~1.125x, plus a
# small constant) and copies all existing elements over — an O(n) operation.
# But because this reallocation happens infrequently (geometric growth means
# it happens less and less often relative to the number of appends), the
# COST AVERAGED over many appends works out to O(1) per append — hence
# "amortized" O(1), even though any single append that triggers a resize is
# momentarily O(n).
#
# 19. How would you safely remove elements from a list WHILE iterating over
#     it, without skipping elements or causing unexpected behavior?
#
# ANSWER:
# Don't mutate the list you're iterating over directly (removing items while
# looping forward causes elements to be skipped, since indices shift). Safe
# approaches:
#   1. Iterate over a COPY: `for item in my_list[:]: ... my_list.remove(item)`
#   2. Build a NEW list with a list comprehension/filter instead of mutating:
#      `my_list = [x for x in my_list if not condition(x)]`
#   3. Iterate BACKWARDS by index if removing by index:
#      `for i in range(len(my_list)-1, -1, -1): ...`
#
# 20. Given two lists of equal length representing keys and values, how would
#     you combine them into a dictionary in one line?
#
# ANSWER:
# Use dict(zip(keys, values)):
#     keys = ["a", "b", "c"]
#     values = [1, 2, 3]
#     result = dict(zip(keys, values))   # {'a': 1, 'b': 2, 'c': 3}
# zip() pairs up corresponding elements, and dict() converts those pairs
# into key-value entries.
