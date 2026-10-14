"""
1. lambda — Anonymous Functions
    A lambda lets you write a small function in one line, without using def or giving it a name.
    Syntax:
        lambda arguments: expression
"""
# Regular function
def add(x, y):
    return x + y
# Same thing as a lambda
add_lambda = lambda x, y: x + y
print(add(3, 4))            # 7
print(add_lambda(3, 4))     # 7

# Sorting a list of tuples by the second element
pairs = [(3, 'b'), (2, 'a'), (1, 'c')]
pairs.sort(key=lambda x: x[0])
print(pairs)   # [(1, 'c'), (2, 'a'), (3, 'b')]
pairs.sort(key=lambda x: x[1])
print(pairs)   # [(2, 'a'), (3, 'b'), (1, 'c')]

numbers = [1, 2, 3, 4, 5]



# Limitation: a lambda can only contain a single expression — no multiple statements, loops, or assignments.

# ==================================================================================================== #
"""
2. map() — Apply a Function to Every Item
    map(function, iterable) applies function to each element of iterable and returns a map
    object (a lazy iterator — values are computed only when you loop over it or convert it).
    Syntax:
        map(function, iterable)
"""
nums = [1, 2, 3, 4, 5]
# Square every number
squares = map((lambda x: x**2), nums)
print(list(squares))   # [1, 4, 9, 16, 25]


a = [1, 2, 3]
b = [10, 20, 30]
sums = map((lambda x, y: x + y), a, b)
print(list(sums))   # [11, 22, 33]

sums = map((lambda x, y: x * y), a, b)
print(list(sums))   # [10, 40, 90]

# ==================================================================================================== #
"""
3. filter() — Keep Only Items That Match a Condition
    filter(function, iterable) keeps only the elements for which function returns True. Also returns a lazy filter object.
    Syntax:
        filter(function, iterable)
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter((lambda x: x % 2 == 0), nums)
print(list(evens))   # [2, 4, 6, 8]
odd = filter((lambda x: x % 2 != 0), nums)
print(list(odd))   # [1, 3, 5, 7]


values = [0, 1, '', 'hello', None, 5]
print(list(filter(None, values))) # [1, 'hello', 5]
l = filter((lambda x: type(x) == int), values)
print(list(l)) # [0, 1, 5]

# ==================================================================================================== #
"""
4. reduce() — Combine All Items Into One Value
    reduce() is not built-in — you must import it from functools. It repeatedly applies a function to pairs 
    of elements, cumulatively reducing the iterable to a single value.
"""
from functools import reduce

nums = [1, 2, 3, 4]
total = reduce((lambda a, b: a + b), nums)
print(total)   # 10
'''
How it works step by step:
    step 1: a=1, b=2  → 1+2 = 3
    step 2: a=3, b=3  → 3+3 = 6
    step 3: a=6, b=4  → 6+4 = 10
'''

# You can also give it an initial starting value: that is 100
total = reduce((lambda a, b: a + b), nums, 100)
print(total)   # 110   (100 + 1 + 2 + 3 + 4)


# Another example — finding the maximum manually:
nums = [4, 9, 2, 7, 5]
maximum = reduce((lambda a, b: a if a > b else b), nums)
print(maximum)   # 9

# ============================================================================================================= #
from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Filter: keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# 2. Map: square each even number
squared = list(map(lambda x: x**2, evens))
print(squared)

# 3. Reduce: sum them all up
result = reduce(lambda a, b: a + b, squared)
print(result)   # 220  → (2²+4²+6²+8²+10²) = 4+16+36+64+100

"""
Summary Table
Tool	    Purpose	                            Returns	            Common Alternative
------      --------------------------------    --------------      ---------------------------
lambda	    Define small anonymous function	    function object	    def
map()	    Transform each item	                lazy iterator	    list comprehension [f(x) for x in iterable]
filter()	Select items matching a condition	lazy iterator	    list comprehension [x for x in iterable if cond]
reduce()	Combine all items into one result	single value	    for loop with accumulator, or built-ins like sum(), max()
"""

# ============================================================================================================= #

"""
sorted(): 
    sorted() is a built-in function that returns a new sorted list from any iterable (list, tuple, string, dict, set, etc.),
    without modifying the original.
    Basic Syntax:
        sorted(iterable, key=None, reverse=False)
    
            - iterable — the data you want to sort
            - key — a function that determines the sort order (optional)
            - reverse — if True, sorts in descending order (optional, default False)
"""
# 1. Simple Sorting
nums = [5, 2, 8, 1, 9]
print(sorted(nums))          # [1, 2, 5, 8, 9]
print(nums)                  # [5, 2, 8, 1, 9]  <- original unchanged

# Works on strings too (sorts characters):
print(sorted("python"))      # ['h', 'n', 'o', 'p', 't', 'y']

# And on tuples/sets — always returns a list, regardless of input type:
print(sorted((3, 1, 2)))     # [1, 2, 3]


# 2. Reverse Order
nums = [5, 2, 8, 1, 9]
print(sorted(nums, reverse=True))   # [9, 8, 5, 2, 1]


# 3. Sorting with key
# The key parameter lets you specify a function that transforms each element before comparing — very powerful for custom sorting logic.

words = ["mango", "banana", "kiwi", "apple", "fig"]
print(sorted(words, key=len))
# ['fig', 'kiwi', 'mango', 'apple', 'banana']


words = ["banana", "Banana", "apple", "Cherry"]
print(sorted(words))
# ['Banana', 'Cherry', 'apple']

# Case-insensitive sort:
print(sorted(words, key=str.lower))
# ['apple', 'banana', 'Banana', 'Cherry']

# Sort a list of tuples by the second element:
pairs = [(1, 'c'), (2, 'a'), (3, 'b')]
print(sorted(pairs, key=lambda x: x[1]))    # [(2, 'a'), (3, 'b'), (1, 'c')]

# Sort a list of dictionaries by a specific field:
people = [
    {"name": "alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "carol", "age": 15}
]
print(sorted(people, key=lambda p: p["age"]))   # [{'name': 'carol', 'age': 15}, {'name': 'Bob', 'age': 25}, {'name': 'alice', 'age': 30}]
print(sorted(people, key=lambda p: p["name"]))   # [{'name': 'Bob', 'age': 25}, {'name': 'alice', 'age': 30}, {'name': 'carol', 'age': 15}]


# 4. Combining key and reverse
words = ["banana", "kiwi", "apple", "fig"]
print(sorted(words, key=len, reverse=True))
# ['banana', 'apple', 'kiwi', 'fig']

# 5. Sorting by Multiple Criteria
people = [
    {"name": "Alice", "age": 35},
    {"name": "Bob", "age": 30},
    {"name": "Carol", "age": 25}
]
# Sort by age first, then by name
result = sorted(people, key=lambda p: (p["age"], p["name"]))
print(result)   # [{'name': 'Carol', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 30}]

# ============================================================================================================= #


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. map()/filter() vs list comprehensions - readability & performance recap
# -------------------------
nums = [1, 2, 3, 4, 5]

# map/filter style
squares_map = list(map(lambda x: x**2, nums))
# equivalent, generally more "Pythonic" for simple cases:
squares_comp = [x**2 for x in nums]
print(squares_map == squares_comp)   # True -> same result

evens_filter = list(filter(lambda x: x % 2 == 0, nums))
evens_comp = [x for x in nums if x % 2 == 0]
print(evens_filter == evens_comp)     # True

# Guideline commonly given in interviews: comprehensions are usually preferred
# for simple transforms/filters (more readable, avoids a lambda), while
# map()/filter() can be nicer when you already have a NAMED function (no
# lambda needed) and want a lazy iterator directly, e.g. map(str, nums).
print(list(map(str, nums)))   # ['1', '2', '3', '4', '5'] -> no lambda needed here at all

print(f"{'*' * 80}")

# -------------------------
# 2. reduce() edge cases - empty iterable and no initial value
# -------------------------
from functools import reduce
try:
    reduce(lambda a, b: a + b, [])          # no initial value + empty iterable
except TypeError as e:
    print("TypeError:", e)   # reduce() of empty iterable with no initial value

print(reduce(lambda a, b: a + b, [], 100))    # 100 -> WITH an initial value, empty iterable is fine,
                                                 # simply returns the initial value unchanged

print(f"{'*' * 80}")

# -------------------------
# 3. functools.partial - "pre-filling" some arguments of a function (a common
#    real-world HOF pattern, often paired with map/filter)
# -------------------------
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)   # exponent is now FIXED at 2
cube = partial(power, exponent=3)

print(square(5))   # 25
print(cube(5))       # 125

print(list(map(square, [1, 2, 3, 4])))   # [1, 4, 9, 16] -> partial works great with map()

print(f"{'*' * 80}")

# -------------------------
# 4. operator module - faster, more readable alternative to simple lambdas
# -------------------------
import operator

nums2 = [1, 2, 3, 4]
print(reduce(operator.add, nums2))         # 10 -> same as reduce(lambda a,b: a+b, nums2), but faster/clearer
print(reduce(operator.mul, nums2))          # 24 -> product of all elements

# operator.itemgetter / attrgetter - cleaner alternative to lambda for sort keys
pairs = [(3, 'b'), (2, 'a'), (1, 'c')]
print(sorted(pairs, key=operator.itemgetter(1)))   # [(2,'a'),(1,'c'),(3,'b')] -> same as key=lambda x: x[1]

people = [
    {"name": "Bob", "age": 25},
    {"name": "Alice", "age": 30},
]
print(sorted(people, key=operator.itemgetter("age")))   # works on dicts too, by key name

# itemgetter can also extract MULTIPLE fields at once, for multi-criteria sort:
data = [(1, 'b', 20), (1, 'a', 10), (2, 'a', 5)]
print(sorted(data, key=operator.itemgetter(0, 1)))   # sorts by field 0, THEN field 1

print(f"{'*' * 80}")

# -------------------------
# 5. sorted() is STABLE - equal elements keep their relative original order
#    (important for multi-pass/multi-key sorting strategies)
# -------------------------
students = [("Alice", "B"), ("Bob", "A"), ("Carol", "A"), ("Dave", "B")]
# sort by grade only - students with the SAME grade keep their ORIGINAL relative order
by_grade = sorted(students, key=lambda s: s[1])
print(by_grade)   # [('Bob', 'A'), ('Carol', 'A'), ('Alice', 'B'), ('Dave', 'B')]
# Bob still comes before Carol (original order preserved among the 'A' grades),
# and Alice still comes before Dave among the 'B' grades.
# Python's sort algorithm (Timsort) GUARANTEES this stability - it's not
# a coincidence, and interviewers often ask about it directly.

print(f"{'*' * 80}")

# -------------------------
# 6. sorted() vs list.sort() - the key practical difference
# -------------------------
nums3 = [3, 1, 2]
new_list = sorted(nums3)     # returns a NEW list, leaves original untouched
print(nums3, new_list)         # [3, 1, 2] [1, 2, 3]

nums3.sort()                    # sorts IN PLACE, returns None
print(nums3)                      # [1, 2, 3]
print(nums3.sort())                 # None -> common gotcha: `x = my_list.sort()` sets x to None!

# sorted() works on ANY iterable (tuples, sets, dicts, generators);
# .sort() is a LIST-ONLY method (tuples/sets don't even have .sort()).

print(f"{'*' * 80}")

# -------------------------
# 7. functools.cmp_to_key() - using an OLD-STYLE comparator function with sorted()
# -------------------------
from functools import cmp_to_key

def compare(a, b):
    """Old-style comparator: negative if a<b, zero if equal, positive if a>b."""
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0

print(sorted([3, 1, 2], key=cmp_to_key(compare)))   # [1, 2, 3]
# Useful when porting comparator-based sorting logic (common in other
# languages, or legacy Python 2 code using the old `cmp` parameter which was
# removed in Python 3).

print(f"{'*' * 80}")

# -------------------------
# 8. any() and all() - related "functional" built-ins that pair naturally with
#    map()/filter()-style thinking
# -------------------------
nums4 = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in nums4))    # True  -> every element satisfies the condition
print(any(n > 5 for n in nums4))           # True  -> at least one element satisfies the condition

# often used instead of filter() when you only care about a yes/no answer,
# not the actual matching items:
has_negative = any(x < 0 for x in [1, -2, 3])
print(has_negative)   # True

print(f"{'*' * 80}")

# -------------------------
# 9. Chaining map/filter and readability tradeoffs (real interview discussion point)
# -------------------------
# Chained map/filter (can get hard to read):
result_chained = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, range(10))))
print(result_chained)   # [0, 4, 8, 12, 16]

# Same logic as a single list comprehension (often considered more readable):
result_comp = [x * 2 for x in range(10) if x % 2 == 0]
print(result_comp)        # [0, 4, 8, 12, 16]
print(result_chained == result_comp)   # True

print(f"{'*' * 80}")

# -------------------------
# 10. Higher-order functions that RETURN functions (closures, decorators are
#     the other big example of this beyond simple sort/map/filter/reduce)
# -------------------------
def make_adder(n):
    def adder(x):
        return x + n
    return adder   # returns a FUNCTION - this makes make_adder() a higher-order function

add5 = make_adder(5)
print(add5(10))   # 15 -> add5 "remembers" n=5 via closure

# passing a HOF as an argument to another function (composition-style)
def compose(f, g):
    return lambda x: f(g(x))

double_then_square = compose(lambda x: x**2, lambda x: x*2)
print(double_then_square(3))   # 36 -> (3*2)^2 = 36


## ==========================================================
## INTERVIEW QUESTIONS ON HIGHER-ORDER FUNCTIONS (map, filter, reduce, sorted)
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is a "higher-order function"? Give examples of built-in Python
#    functions that qualify, and explain what makes them higher-order.
#
# 2. What is the key limitation of a lambda expression compared to a regular
#    function defined with `def`?
#
# 3. Do map() and filter() return a list directly? What do they actually
#    return, and why does this matter for memory usage with large datasets?
#
# 4. What happens if you call `reduce()` on an empty iterable without
#    providing an initial value? How does providing an initial value change
#    this behavior?
#
# 5. When would you prefer a list comprehension over map()/filter(), and vice
#    versa? Is there a meaningful performance difference between them?
#
# 6. What does functools.partial do? Give a practical example of using it
#    together with map() or filter().
#
# 7. What is operator.itemgetter(), and why might you prefer it over an
#    equivalent lambda (e.g., `key=operator.itemgetter(1)` vs
#    `key=lambda x: x[1]`)?
#
# 8. What does it mean for a sorting algorithm to be "stable"? Is Python's
#    sorted()/list.sort() stable? Why does this matter when sorting by
#    multiple keys in separate passes?
#
# 9. What is the difference between sorted() and list.sort()? Which one
#    returns None, and what common mistake does that lead to?
#
# 10. How would you sort a list of dictionaries by multiple fields (e.g., age
#     first, then name)? What would you pass as the `key` argument?
#
# 11. What does functools.cmp_to_key() do, and when would you need it instead
#     of a simple `key=` function?
#
# 12. How would you check if ALL elements in a list satisfy a condition, or if
#     AT LEAST ONE does, without writing a manual loop?
#
# 13. What is a closure, and how does it relate to a function like
#     `make_adder(n)` that returns another function?
#
# 14. Can you chain map() and filter() together? What are the readability
#     tradeoffs of doing so compared to using a single list comprehension
#     with a condition?
#
# 15. What does `key=str.lower` do when passed to sorted()? Why is this
#     useful for case-insensitive sorting, and how is it different from
#     sorting `[s.lower() for s in words]` directly?
#
# 16. What's the difference between `reduce(operator.add, nums)` and simply
#     using the built-in `sum(nums)`? Is there ever a reason to prefer
#     reduce() for summing numbers?
#
# 17. If you sort a list of tuples using `sorted(data, key=operator.itemgetter(0, 1))`,
#     what does passing multiple indices to itemgetter actually do?
#
# 18. Are lambda functions "first-class" in the same way regular functions
#     are (can they be stored in variables, passed as arguments, returned
#     from other functions)?
#
# 19. What is function composition (e.g., combining two functions f and g
#     into a single function that applies g then f)? How would you implement
#     a simple `compose()` helper in Python?
#
# 20. Why might overusing lambda expressions inside deeply chained
#     map/filter/reduce calls hurt code readability and debuggability
#     compared to named functions or list comprehensions?