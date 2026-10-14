"""
Counter is a specialized dictionary subclass in Python's built-in collections module, 
    designed for counting hashable objects (like elements in a list or characters in a string).
"""
from collections import Counter

# Count elements in a list
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count = Counter(fruits)
print(count)    # Counter({'apple': 3, 'banana': 2, 'orange': 1})


s = "strings"
c = Counter(s)
print(type(c))      # <class 'collections.Counter'>
print(c)    # Counter({'s': 2, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1})


# Ways to create a Counter
Counter(['a', 'b', 'a'])          # from a list
Counter('mississippi')            # from a string -> counts each character
Counter({'a': 3, 'b': 1})          # from a dict
Counter(a=3, b=1)                  # from keyword arguments


# Key features
# Accessing counts — works like a normal dict, but missing keys return 0 instead of raising KeyError:
count = Counter(['a', 'b', 'a'])
print(count['a'])   # 2
print(count['z'])   # 0 (no error!)


# most_common(n) — get the n most frequent elements:
count = Counter('mississippi')
print(count.most_common(2))     # [('i', 4), ('s', 4)]

# Updating counts:
count = Counter(['a', 'b'])
count.update(['a', 'c'])
print(count)    # Counter({'a': 2, 'b': 1, 'c': 1})

# Arithmetic operations — Counters support +, -, & (intersection), | (union):
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print(c1 + c2)   # Counter({'a': 4, 'b': 3})
print(c1 - c2)   # Counter({'a': 2})
print(c1 & c2)   # Counter({'a': 1, 'b': 1})  -> min of each
print(c1 | c2)   # Counter({'a': 3, 'b': 2})  -> max of each

# elements() — returns an iterator that repeats each element by its count:
count = Counter(a=2, b=1)
print(list(count.elements()))
# ['a', 'a', 'b']


# Quick example — word frequency
text = "the quick brown fox the lazy fox"
word_counts = Counter(text.split())
print(word_counts.most_common(2))
# [('the', 2), ('fox', 2)]
# ==============================================================================
#  COLLECTIONS MODULE
# ==============================================================================
"""
NOTES:
- Counter: dict subclass for counting hashable items - has .most_common(n).
- defaultdict: dict subclass that auto-creates a default value for missing
    keys (no more KeyError / manual "if key not in dict" checks).
- OrderedDict: preserves insertion order - since Python 3.7 regular dicts also
  preserve insertion order, so OrderedDict is mainly useful now for its extra
  methods like move_to_end() and for explicit "order matters" semantics.
- namedtuple: lightweight immutable object with named fields - like a mini
  class without writing __init__/etc.
- deque: double-ended queue - O(1) appends/pops from BOTH ends, unlike list
  where insert(0, x) is O(n) because everything shifts.
"""
from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

def collections_demo():
    print("\n--- COLLECTIONS MODULE ---")

    # Counter
    sentence = "the quick brown fox jumps over the lazy dog the fox runs"
    word_counts = Counter(sentence.split())
    print("word_counts:", word_counts)
    print("Most common word:", word_counts.most_common(1))

    # defaultdict - group items by key
    items = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana")]
    grouped = defaultdict(list)
    print(grouped)
    for category, item in items:
        grouped[category].append(item)
    print("Grouped with defaultdict:", dict(grouped))

    # OrderedDict
    od = OrderedDict()
    od["b"] = 2
    od["a"] = 1
    od.move_to_end("b")
    print("OrderedDict after move_to_end:", od)

    # namedtuple
    Point = namedtuple("Point", ["x", "y"])
    p = Point(3, 4)
    print("namedtuple Point:", p, "| p.x =", p.x, "| accessible like tuple:", p[0])

    # deque - O(1) from both ends
    dq = deque([1, 2, 3])
    dq.appendleft(0)  # O(1) - vs list.insert(0, x) which is O(n)
    dq.append(4)
    print("deque after appendleft/append:", dq)


if __name__ == "__main__":
    collections_demo()


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. Counter.subtract() vs the '-' operator (subtle difference!)
# -------------------------
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print(c1 - c2)          # Counter({'a': 2})  -> '-' operator DROPS non-positive counts
c1.subtract(c2)
print(c1)               # Counter({'a': 2, 'b': -1}) -> subtract() KEEPS negative/zero counts

print(f"{'*' * 60}")

# -------------------------
# 2. Counter with missing keys - accessing vs checking membership
# -------------------------
count = Counter(['a', 'b', 'a'])
print('z' in count)     # False -> 'in' still correctly reports absence
print(count['z'])       # 0     -> but indexing returns 0, NOT KeyError (this is the special part)
print(len(count))        # 2     -> only counts KEYS THAT EXIST, accessing count['z'] does NOT add it

print(f"{'*' * 60}")

# -------------------------
# 3. defaultdict - the "default factory" concept in depth
# -------------------------
# The argument to defaultdict must be a CALLABLE (a function/class with no args),
# not a value. It's called automatically whenever a missing key is accessed.
dd_list = defaultdict(list)      # calls list() -> [] for missing keys
dd_int = defaultdict(int)        # calls int()  -> 0 for missing keys
dd_set = defaultdict(set)        # calls set()  -> set() for missing keys
dd_custom = defaultdict(lambda: "N/A")  # any zero-arg callable works

print(dd_int['missing'])   # 0  -> auto-created via int()
dd_int['x'] += 1
dd_int['x'] += 1
print(dd_int)               # defaultdict(<class 'int'>, {'missing': 0, 'x': 2})

print(dd_custom['unknown'])  # 'N/A'

# IMPORTANT GOTCHA: simply ACCESSING a missing key (even just reading it,
# like in `if dd['x']:`) creates that key in the defaultdict as a side effect!
dd2 = defaultdict(int)
print('y' in dd2)     # False
_ = dd2['y']            # just reading it...
print('y' in dd2)      # True -> now it exists! reading created it.

# word frequency counter, the "manual" way defaultdict replaces:
text = "a b a c b a"
counts = {}
for word in text.split():
    if word not in counts:
        counts[word] = 0
    counts[word] += 1
print(counts)   # same result achievable in 2 lines with defaultdict(int)

print(f"{'*' * 60}")

# -------------------------
# 4. namedtuple - more useful methods (_asdict, _replace, _fields, defaults)
# -------------------------
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)

print(p._asdict())          # {'x': 3, 'y': 4} -> converts to an (ordered) dict
p2 = p._replace(x=10)        # creates a NEW namedtuple with x changed (immutable!)
print(p2)                     # Point(x=10, y=4)
print(p)                      # Point(x=3, y=4) -> original unchanged, since tuples are immutable
print(Point._fields)          # ('x', 'y') -> tuple of field names

# namedtuple with default values (Python 3.7+)
Config = namedtuple("Config", ["host", "port"], defaults=["localhost", 8080])
print(Config())               # Config(host='localhost', port=8080)
print(Config("example.com"))   # Config(host='example.com', port=8080)

# Why prefer namedtuple over a plain tuple:
plain = (3, 4)
print(plain[0])   # 3 -> works, but unclear WHAT 3 represents without context
print(p.x)          # 3 -> self-documenting, much more readable

print(f"{'*' * 60}")

# -------------------------
# 5. deque - additional operations beyond append/appendleft
# -------------------------
dq = deque([1, 2, 3, 4, 5])
dq.rotate(1)     # rotate right by 1
print(dq)          # deque([5, 1, 2, 3, 4])
dq.rotate(-2)     # rotate left by 2
print(dq)          # deque([2, 3, 4, 5, 1])

print(dq.pop())       # 1  -> removes and returns from the RIGHT end, O(1)
print(dq.popleft())    # 2  -> removes and returns from the LEFT end, O(1)
print(dq)                # deque([3, 4, 5])

# maxlen - very useful for "sliding window" / "last N items" / circular buffer problems
recent = deque(maxlen=3)
for i in range(6):
    recent.append(i)
    print(list(recent))
# Once full, adding a new item automatically DROPS the oldest from the other end:
# [0] [0, 1] [0, 1, 2] [1, 2, 3] [2, 3, 4] [3, 4, 5]

print(f"{'*' * 60}")

# -------------------------
# 6. deque vs list - performance comparison (important for coding interviews)
# -------------------------
# list.insert(0, x) / list.pop(0)   -> O(n) - every remaining element must shift
# deque.appendleft(x) / deque.popleft() -> O(1) - deque is a doubly linked list internally
# deque.append(x) / deque.pop()          -> O(1), same as list.append()/list.pop()
# list random access (lst[i])            -> O(1)
# deque random access (dq[i])            -> O(n) - must walk the linked list!
# RULE OF THUMB: use deque when you need fast operations at BOTH ends
# (e.g., BFS queues, sliding window, undo history); use list for fast
# random access and operations mainly at the end.

print(f"{'*' * 60}")

# -------------------------
# 7. ChainMap - search across multiple dicts as if they were one (often missed!)
# -------------------------
from collections import ChainMap

defaults = {"theme": "light", "language": "en"}
user_settings = {"theme": "dark"}

combined = ChainMap(user_settings, defaults)   # earlier dicts take priority
print(combined["theme"])       # 'dark' -> found in user_settings (first dict) first
print(combined["language"])    # 'en'   -> not in user_settings, falls back to defaults
print(dict(combined))           # {'language': 'en', 'theme': 'dark'} -> merged view

# useful for config layering: command-line args > env vars > config file > defaults
# Unlike {**dict1, **dict2}, ChainMap doesn't COPY the dicts - it's a live view,
# so changes to the underlying dicts are reflected automatically.
defaults["language"] = "fr"
print(combined["language"])     # 'fr' -> reflects the live update, no copy was made

print(f"{'*' * 60}")

# -------------------------
# 8. OrderedDict vs regular dict - what's ACTUALLY still different (post 3.7)
# -------------------------
od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
print(od1 == od2)     # False -> OrderedDict equality is ORDER-SENSITIVE

d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}
print(d1 == d2)        # True -> regular dict equality is NOT order-sensitive, only key/value pairs matter

# OrderedDict also has move_to_end(key, last=True/False) and pops in a
# well-defined order via popitem(last=True/False) - regular dict's popitem()
# always pops the LAST inserted item, no 'last' parameter.

print(f"{'*' * 60}")

# -------------------------
# 9. UserDict / UserList / UserString - for SAFELY subclassing built-ins
# -------------------------
# Subclassing dict/list/str directly can cause issues because built-in methods
# (implemented in C) don't always call your overridden methods internally.
# collections.UserDict/UserList/UserString wrap the built-in type in pure Python,
# so overrides are always respected.
from collections import UserDict

class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)   # always store keys lowercase

    def __getitem__(self, key):
        return super().__getitem__(key.lower())

cid = CaseInsensitiveDict()
cid["Name"] = "Alice"
print(cid["name"])    # 'Alice' -> works because keys are normalized to lowercase


## ==========================================================
## INTERVIEW QUESTIONS ON THE COLLECTIONS MODULE
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is Counter, and how is it different from a regular dict when accessing
#    a key that doesn't exist?
#
# 2. What is the difference between Counter's '-' operator and its subtract()
#    method?
#
# 3. What must you pass as the argument to defaultdict, and why does it need to
#    be callable rather than a plain value?
#
# 4. What is a subtle "gotcha" with defaultdict where simply READING a missing
#    key can have a side effect? Why does this matter in production code?
#
# 5. Since Python 3.7, regular dicts preserve insertion order. So what is
#    OrderedDict still useful for today?
#
# 6. How does equality comparison differ between OrderedDict and a regular dict?
#
# 7. What is a namedtuple, and what real-world problem does it solve compared to
#    using a plain tuple or a full class?
#
# 8. How would you create a modified copy of a namedtuple instance, given that
#    namedtuples (like all tuples) are immutable?
#
# 9. What is the time complexity of inserting/removing from the front of a
#    Python list versus a deque? Why the difference?
#
# 10. What is deque's maxlen parameter used for? Describe a real scenario
#     (e.g., sliding window, log buffer) where it's useful.
#
# 11. What is the time complexity of random access (dq[i]) on a deque compared
#     to a list? Why does this matter when choosing a data structure?
#
# 12. What is ChainMap used for? How is it different from merging dictionaries
#     with {**d1, **d2}?
#
# 13. If you update the underlying dictionary passed into a ChainMap, does the
#     ChainMap reflect the change? Why or why not?
#
# 14. Why might directly subclassing `dict` or `list` cause unexpected behavior
#     with overridden methods? How do UserDict/UserList/UserString solve this?
#
# 15. How would you find the top-N most frequent elements in a list efficiently?
#     What's the time complexity of Counter.most_common(n)?
#
# 16. What does elements() return on a Counter object, and what happens with
#     zero or negative counts when you call it?
#
# 17. How would you implement a fixed-size cache/rolling window of the last N
#     items seen? Which collections type is best suited for this and why?
#
# 18. What's the difference between deque.rotate(n) with a positive vs a
#     negative value of n?
#
# 19. Give an example of when you'd choose defaultdict(list) over a manual
#     `if key not in dict: dict[key] = []` pattern, and explain the readability/
#     performance benefit.
#
# 20. How would you merge two Counters such that overlapping keys take the
#     MINIMUM of the two counts? Which operator/method would you use?