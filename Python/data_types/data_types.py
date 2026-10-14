"""
## Python Data Types

Data Type	    Example	            Ordered?	            Mutable?	        Duplicates?	        Indexed?
---------       -----------         --------                -----------         -----------         --------------
int	            10	                —	                    ❌ No	            —	                —
float	        3.14	            —	                    ❌ No	            —	                —
str	            "hello"	            ✅ Yes	                ❌ No	            ✅ Yes	            ✅ Yes
bool	        True, False	        —	                    ❌ No	            —	                —
list	        [1, 2, 3]	        ✅ Yes	                ✅ Yes	            ✅ Yes	            ✅ Yes
tuple	        (1, 2, 3)	        ✅ Yes	                ❌ No	            ✅ Yes	            ✅ Yes
set	            {1, 2, 3}	        ❌ No	                ✅ Yes	            ❌ No	            ❌ No
frozenset	    frozenset([1,2,3])	❌ No	                ❌ No	            ❌ No	            ❌ No
dict	        {"a": 1, "b": 2}	✅ Yes (insertion order)✅ Yes	            ❌ No (keys unique)	❌ No (accessed by key)
NoneType	    None	            —	                    —	                —	                —

## Grouped by category
    Numeric: `int`, `float`, `complex`
    Text: `str`
    Sequence: `list`, `tuple`, `range`
    Set: `set`, `frozenset`
    Mapping: `dict`
    Boolean: `bool`
    Binary: `bytes`, `bytearray`, `memoryview`
    None: `NoneType`

## Mutable vs Immutable — the key divide

Mutable ✅    | Immutable ❌
`list`        | `int`, `float`
`dict`        | `str`
`set`         | `tuple`
 -            | `frozenset`
 -            | `bool`

Key takeaway:
    When picking a data type, ask two questions —
        1. do I need order/position?
        2. will this data change after creation?
    That decision tree gets you to the right type almost every time:
        - Need key-based lookup → dict
        - Need order + changeable → list
        - Need order + fixed/safe → tuple
        - Need uniqueness + fast lookup → set
"""

## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION
## ==========================================================
# -------------------------
# 1. Checking type() and confirming the table's claims with code
# -------------------------
print(type(10))                 # <class 'int'>
print(type(3.14))               # <class 'float'>
print(type("hello"))            # <class 'str'>
print(type(True))               # <class 'bool'>
print(type([1, 2, 3]))          # <class 'list'>
print(type((1, 2, 3)))          # <class 'tuple'>
print(type({1, 2, 3}))          # <class 'set'>
print(type(frozenset([1, 2, 3])))  # <class 'frozenset'>
print(type({"a": 1, "b": 2}))    # <class 'dict'>
print(type(None))                 # <class 'NoneType'>

print(f"{'*' * 60}")

# -------------------------
# 2. Proving mutability vs immutability with id()
# -------------------------
# Immutable: any "change" actually creates a NEW object (id() changes)
s = "hello"
print(id(s))
s += " world"
print(id(s))     # DIFFERENT id -> a new string object was created, original untouched

# Mutable: changing in place keeps the SAME id()
lst = [1, 2, 3]
print(id(lst))
lst.append(4)
print(id(lst))    # SAME id -> modified in place, no new object created

print(f"{'*' * 60}")

# -------------------------
# 3. Ordered vs unordered - proving list/tuple/dict preserve order, set does not
# -------------------------
ordered_list = [3, 1, 2]
print(ordered_list)          # [3, 1, 2] -> insertion order preserved, always
ordered_dict = {"z": 1, "a": 2, "m": 3}
print(list(ordered_dict))     # ['z', 'a', 'm'] -> insertion order preserved (3.7+ guarantee)

unordered_set = {3, 1, 2}
print(unordered_set)           # order NOT guaranteed - may print in any order,
                                 # and should never be relied upon for sequence

print(f"{'*' * 60}")

# -------------------------
# 4. Duplicates - list/tuple allow, set/frozenset/dict-keys don't
# -------------------------
print([1, 1, 2, 2])         # [1, 1, 2, 2] -> duplicates kept
print({1, 1, 2, 2})          # {1, 2}       -> automatically deduplicated
d = {"a": 1, "a": 2}          # dict literal with duplicate key
print(d)                        # {'a': 2} -> LAST value wins, no error raised!

print(f"{'*' * 60}")

# -------------------------
# 5. Indexed vs not indexed - accessing elements by position vs key vs membership only
# -------------------------
lst = [10, 20, 30]
print(lst[0])          # 10 -> indexed access works

s = {10, 20, 30}
# print(s[0])            # TypeError: 'set' object is not subscriptable

d = {"a": 1}
print(d["a"])            # 1 -> accessed by KEY, not by integer position
# print(d[0])              # KeyError (unless 0 happens to be an actual key)

print(f"{'*' * 60}")

# -------------------------
# 6. Numeric types beyond int/float - complex (from the "grouped by category" list)
# -------------------------
c = 3 + 4j
print(type(c), c.real, c.imag)   # <class 'complex'> 3.0 4.0

print(f"{'*' * 60}")

# -------------------------
# 7. range - a memory-efficient sequence type (often forgotten in this list)
# -------------------------
r = range(5)
print(type(r))         # <class 'range'>
print(list(r))          # [0, 1, 2, 3, 4] -> materializes lazily, doesn't store all values upfront
print(r[2])              # 2 -> range IS indexed, despite being a lazy sequence
print(len(range(1_000_000_000)))   # instant! range doesn't actually build a billion-item list

print(f"{'*' * 60}")

# -------------------------
# 8. Binary types - bytes, bytearray, memoryview (also often forgotten)
# -------------------------
b = bytes([65, 66, 67])
print(b, type(b))            # b'ABC' <class 'bytes'> -> IMMUTABLE sequence of integers (0-255)

ba = bytearray([65, 66, 67])
print(ba, type(ba))            # bytearray(b'ABC') <class 'bytearray'> -> MUTABLE version of bytes
ba[0] = 90
print(ba)                        # bytearray(b'ZBC') -> can modify in place, unlike bytes

mv = memoryview(ba)
print(mv, type(mv))              # <memory at ...> <class 'memoryview'> -> view into the buffer
                                    # WITHOUT copying it - useful for large binary data / performance

print(f"{'*' * 60}")

# -------------------------
# 9. frozenset - the immutable counterpart to set (worth demonstrating directly)
# -------------------------
fs = frozenset([1, 2, 3])
# fs.add(4)          # AttributeError: 'frozenset' object has no attribute 'add'
print(fs)              # frozenset({1, 2, 3})

# frozenset is HASHABLE (regular set is NOT) - so it CAN be used as a dict key
# or nested inside another set, unlike a regular set:
d = {frozenset([1, 2]): "pair"}
print(d)                 # {frozenset({1, 2}): 'pair'}
# d2 = {set([1, 2]): "pair"}   # TypeError: unhashable type: 'set'

print(f"{'*' * 60}")

# -------------------------
# 10. NoneType and identity checks
# -------------------------
x = None
print(type(x))          # <class 'NoneType'>
print(x is None)         # True -> ALWAYS use 'is' for None comparisons, not =='
print(x == None)          # True, but considered bad practice (custom __eq__ could break this)

print(f"{'*' * 60}")

# -------------------------
# 11. Choosing the right type - practical decision-making examples
# -------------------------
# Need key-based lookup -> dict
user = {"name": "Alice", "age": 30}

# Need order + changeable -> list
shopping_cart = ["milk", "eggs", "bread"]
shopping_cart.append("butter")

# Need order + fixed/safe (e.g. coordinates that shouldn't change) -> tuple
coordinates = (12.9716, 77.5946)

# Need uniqueness + fast membership testing -> set
seen_ids = {101, 102, 103}
print(104 in seen_ids)   # O(1) average time -> much faster than `104 in [101,102,103]` for large data

print(f"{'*' * 60}")

# -------------------------
# 12. Type conversion between the major types (very common in real code/interviews)
# -------------------------
print(list((1, 2, 3)))        # [1, 2, 3] -> tuple to list
print(tuple([1, 2, 3]))        # (1, 2, 3) -> list to tuple
print(set([1, 1, 2, 3]))        # {1, 2, 3} -> list to set (dedupes)
print(list({1, 2, 3}))           # [1, 2, 3] -> set to list
print(dict([("a", 1), ("b", 2)]))  # {'a': 1, 'b': 2} -> list of pairs to dict
print(list({"a": 1, "b": 2}.items()))  # [('a', 1), ('b', 2)] -> dict to list of pairs


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON DATA TYPES (WITH ANSWERS)
## ==========================================================

# 1. What are Python's built-in data types, grouped by category (numeric, text,
#    sequence, set, mapping, boolean, binary, none)?
#
#    ANSWER:
#      Numeric  : int, float, complex
#      Text     : str
#      Sequence : list, tuple, range
#      Set      : set, frozenset
#      Mapping  : dict
#      Boolean  : bool (a subclass of int, see Q19)
#      Binary   : bytes, bytearray, memoryview
#      None     : NoneType (its only value is None)
#
# 2. What is the difference between a list and a tuple? Given that both are
#    ordered and allow duplicates, why would you choose one over the other?
#
#    ANSWER: The key difference is mutability: a list can be changed after
#    creation (append, remove, item assignment); a tuple cannot.
#    Choose a LIST when the collection will grow, shrink, or change, e.g. a
#    shopping cart or a queue of tasks.
#    Choose a TUPLE when the data is fixed and should not be changed by
#    accident, e.g. coordinates (lat, lon), RGB colours, or returning
#    several values from a function. Tuples are also hashable (if their
#    items are), so they can be dict keys or set members; lists cannot.
#    Tuples are also slightly lighter and faster (see Q3).
#
# 3. Why is a tuple generally faster to create and iterate over than a list of
#    the same elements?
#
#    ANSWER: Because a tuple is immutable and fixed-size:
#      - It is allocated ONCE with exactly the space it needs. A list
#        over-allocates extra room so append() is cheap, and keeps a
#        separate resizable array of item pointers.
#      - A tuple of constants like (1, 2, 3) is built once at compile time
#        and reused, while [1, 2, 3] must build a new list every time the
#        line runs.
#      - CPython keeps a cache of freed small tuples to reuse them.
#    So tuples use less memory and are noticeably faster to CREATE.
#    Iteration speed is almost identical; the difference there is tiny.
#        import sys
#        sys.getsizeof((1, 2, 3)) < sys.getsizeof([1, 2, 3])   -> True
#
# 4. What's the difference between a set and a frozenset? Why is frozenset
#    hashable while set is not, and what practical difference does that make?
#
#    ANSWER: A set is mutable (add, remove, update); a frozenset is
#    immutable. Since a frozenset's contents can never change, its hash can
#    be computed once and stays valid forever, so Python makes it hashable.
#    A set's contents (and therefore its hash) could change at any time, so
#    it is unhashable.
#    Practical difference: a frozenset can be used as a dict key or stored
#    inside another set; a regular set cannot:
#        {frozenset([1, 2]): "pair"}    # works
#        {{1, 2}: "pair"}               # TypeError: unhashable type: 'set'
#
# 5. Why does a dict allow duplicate VALUES but not duplicate KEYS? What
#    happens if you write a dict literal with the same key twice?
#
#    ANSWER: The key is the unique identifier used to look up a value: it
#    decides which hash-table slot is used, so each key can appear only
#    once. Values are just stored data and are never used for lookup, so any
#    number of keys can share the same value: {"a": 1, "b": 1} is fine.
#    With a duplicate key in a literal, no error is raised. The later value
#    simply overwrites the earlier one:
#        {"a": 1, "a": 2}   -> {'a': 2}
#
# 6. How would you prove, using id(), that strings are immutable and lists are
#    mutable in Python?
#
#    ANSWER: id() returns an object's identity. "Change" each and compare:
#        s = "hello"
#        before = id(s)
#        s += " world"
#        print(id(s) == before)     # False -> a NEW string object was made
#
#        lst = [1, 2, 3]
#        before = id(lst)
#        lst.append(4)
#        print(id(lst) == before)   # True  -> same object, changed in place
#    Also, trying s[0] = "H" raises TypeError: 'str' object does not
#    support item assignment, while lst[0] = 99 works.
#
# 7. What is the time complexity of membership testing (`x in y`) for a list
#    versus a set? Why the difference?
#
#    ANSWER: List: O(n). Set: O(1) on average.
#    A list has no index of its contents, so Python compares x with each
#    element in turn until it finds a match or reaches the end. A set is a
#    hash table: Python computes hash(x) and jumps straight to the slot
#    where x would be, so the time doesn't grow with the size of the set.
#
# 8. What is `range()`, and why is `range(10**9)` created instantly without
#    consuming huge memory? How is it different from a list of the same
#    numbers?
#
#    ANSWER: range is an immutable sequence type representing an arithmetic
#    progression. It stores only three numbers: start, stop, and step. Each
#    value is CALCULATED when needed (start + i * step), never stored, so
#    range(10**9) takes the same tiny memory as range(5).
#    A list stores every element, so list(range(10**9)) would need many GB.
#    range still supports len(), indexing r[i], slicing, and a fast
#    O(1) `in` check for integers, but you cannot modify it.
#        import sys
#        sys.getsizeof(range(10**9))   -> 48 bytes (approx.)
#
# 9. What are bytes, bytearray, and memoryview used for? Which one is mutable,
#    and when would you reach for memoryview specifically?
#
#    ANSWER: All three handle raw binary data (file contents, images,
#    network packets, encoded text):
#      - bytes     : IMMUTABLE sequence of integers 0-255, e.g. b"ABC" or
#                    "text".encode()
#      - bytearray : MUTABLE version of bytes; can be modified in place.
#      - memoryview: a view into another object's memory buffer (bytes,
#                    bytearray, arrays) WITHOUT copying it.
#    bytearray is the mutable one. Use memoryview when working with large
#    binary data where copying would waste memory and time, e.g. slicing a
#    large buffer, parsing parts of a big file, or network I/O. Slicing a
#    bytes object copies the data; slicing a memoryview does not.
#
# 10. Why can't you use a list or a set as a dictionary key, but you CAN use a
#     tuple or a frozenset?
#
#    ANSWER: Dict keys must be hashable, meaning their hash value must never
#    change. Lists and sets are mutable: if one were changed after being used
#    as a key, its hash would change and the dict could no longer find it.
#    So Python makes them unhashable. Tuples and frozensets are immutable,
#    so their hash stays fixed and they are safe as keys.
#    Note: a tuple is only hashable if ALL its items are hashable:
#        {(1, 2): "ok"}        # works
#        {(1, [2]): "fail"}    # TypeError: unhashable type: 'list'
#
# 11. Since Python 3.7, dict preserves insertion order. Does that mean dict is
#     now considered an "ordered" type in the same sense as list? What's the
#     nuance here?
#
#    ANSWER: Only partly. A dict REMEMBERS insertion order when you iterate
#    over it, but it is still not a sequence like a list:
#      - No positional indexing: d[0] looks up the KEY 0, not the first item.
#      - You cannot insert at a position or reorder items directly.
#      - Equality ignores order: {"a": 1, "b": 2} == {"b": 2, "a": 1} is True,
#        while [1, 2] == [2, 1] is False.
#    So a dict is "insertion-ordered" but not "positionally ordered".
#    (collections.OrderedDict adds move_to_end() and order-sensitive
#    equality between two OrderedDicts.)
#
# 12. Given a mix of data (e.g., needing uniqueness AND insertion order AND
#     mutability), how would you decide between list, set, and dict as your
#     underlying structure?
#
#    ANSWER: Check each requirement against each type:
#      - list: order + mutable, but allows duplicates and has O(n) lookup.
#      - set : unique + mutable + fast lookup, but NO order.
#      - dict: unique keys + insertion order + mutable + O(1) lookup.
#    So for uniqueness AND order AND mutability, use a dict, using its keys
#    as an "ordered set" (values can be None, or real data if you have it):
#        seen = dict.fromkeys([3, 1, 3, 2])   # keys: 3, 1, 2
#        seen[5] = None                       # add
#        del seen[1]                          # remove
#        list(seen)                           # [3, 2, 5]
#    General rule: start from what you must look things up BY and whether
#    order or duplicates matter, then pick the simplest type that fits.
#
# 13. What does `x == None` do differently from `x is None`? Why is `is`
#     preferred, and can `==` ever give a misleading answer here?
#
#    ANSWER: `x is None` checks IDENTITY: is x the exact same object as the
#    single None object? Since None is a singleton, this is always correct.
#    `x == None` checks EQUALITY by calling x's __eq__ method, which a class
#    can override to return anything. So yes, == can mislead:
#        class AlwaysEqual:
#            def __eq__(self, other):
#                return True
#        AlwaysEqual() == None   -> True   (wrong!)
#        AlwaysEqual() is None   -> False  (correct)
#    With NumPy arrays, arr == None compares element-wise and returns an
#    array instead of True/False. `is` is also slightly faster and is the
#    style recommended by PEP 8.
#
# 14. Why is `complex` considered a numeric type in Python but not commonly
#     used in typical business/backend code? Give a domain where it IS useful.
#
#    ANSWER: It's a numeric type because it supports arithmetic (+, -, *, /,
#    **, abs()) like int and float. It's rare in business code because money,
#    counts, and measurements are real numbers; nothing there needs the
#    square root of -1.
#    Domains where it IS useful:
#      - Electrical engineering: AC circuit analysis, impedance (Z = R + jX).
#        Python uses j for the same reason engineers do.
#      - Signal processing: Fourier transforms (FFT), audio and image
#        processing.
#      - Physics and quantum computing, control systems, and fractals such
#        as the Mandelbrot set.
#
# 15. What is the practical difference between deep equality (`==`) and
#     identity (`is`) when comparing two different data type instances that
#     look equal (e.g., two lists with the same elements)?
#
#    ANSWER: `==` asks "do they have the same VALUE?"; `is` asks "are they
#    the SAME OBJECT in memory?"
#        a = [1, 2, 3]
#        b = [1, 2, 3]
#        c = a
#        a == b   -> True   (same contents)
#        a is b   -> False  (two separate objects)
#        a is c   -> True   (c is just another name for a)
#    Practical impact: changing a also changes c, but not b.
#        a.append(4)  ->  c is [1, 2, 3, 4], b is still [1, 2, 3]
#    Use == to compare values; use `is` only for identity checks like
#    `is None`. Don't use `is` for numbers or strings: results like
#    `256 is 256` being True are CPython caching details, not guarantees.
#
# 16. How would you convert a list of (key, value) tuples into a dictionary,
#     and vice versa?
#
#    ANSWER:
#        pairs = [("a", 1), ("b", 2)]
#        d = dict(pairs)            -> {'a': 1, 'b': 2}
#        back = list(d.items())     -> [('a', 1), ('b', 2)]
#    If keys and values are in two separate lists, use zip():
#        dict(zip(["a", "b"], [1, 2]))   -> {'a': 1, 'b': 2}
#    Note: with duplicate keys in the pairs, the last value wins.
#
# 17. Why does converting a list to a set (e.g., `set(my_list)`) sometimes
#     change the order of elements when converted back to a list?
#
#    ANSWER: A set doesn't store items in insertion order. Each item goes
#    into a hash-table slot based on its hash value, and iterating over the
#    set walks those slots in table order. So list(set(my_list)) comes back
#    in hash order, not the original order.
#        list(set(["banana", "apple", "cherry"]))   # order can vary per run
#    (For small ints the result often LOOKS sorted, since an int's hash is
#    itself, but that is an implementation detail.) To dedupe while keeping
#    order: list(dict.fromkeys(my_list)).
#
# 18. If you need both fast lookups AND to preserve insertion order AND to
#     store key-value pairs, which built-in type do you reach for, and why?
#
#    ANSWER: A plain dict. It gives:
#      - key-value storage,
#      - O(1) average lookup, insert, and delete (hash table), and
#      - guaranteed insertion order since Python 3.7.
#    No other built-in type covers all three. OrderedDict is only needed for
#    extras like move_to_end() or order-sensitive equality.
#
# 19. Is `bool` considered a distinct data type, or is it more accurately
#     described as something else in Python's type system? What evidence
#     supports your answer?
#
#    ANSWER: bool is its own type, but it is a SUBCLASS OF int: True behaves
#    as 1 and False as 0. Evidence:
#        issubclass(bool, int)    -> True
#        isinstance(True, int)    -> True
#        True + True              -> 2
#        True == 1                -> True
#        sum([True, False, True]) -> 2    (handy for counting matches)
#    bool itself cannot be subclassed, and there are only two instances,
#    True and False.
#    Gotcha: since True == 1 and hash(True) == hash(1), they count as the
#    same dict key:
#        {1: "one", True: "yes"}   -> {1: 'yes'}
#
# 20. When would choosing a mutable type (like a list) for a function's
#     default argument value cause a bug? How does this connect back to the
#     mutable/immutable distinction in this table?
#
#    ANSWER: Default values are created ONCE, when the function is defined,
#    not each time it is called. With a mutable default, every call shares
#    the same object, so changes made in one call leak into the next:
#        def add_item(item, items=[]):
#            items.append(item)
#            return items
#        add_item("a")   -> ['a']
#        add_item("b")   -> ['a', 'b']   <- bug: expected ['b']
#    Fix: use None as the default and create a new list inside:
#        def add_item(item, items=None):
#            if items is None:
#                items = []
#            items.append(item)
#            return items
#    Connection to the table: immutable defaults (int, str, tuple, None) are
#    safe because they can't be modified in place; any "change" makes a new
#    object. Mutable defaults (list, dict, set) can be modified in place,
#    so the shared default object keeps the changes between calls.