"""
    Functions: Functions is set of instructions that are written and that can be reused
        further in python file.
        - To create function we will use keyword called "def".
        - Functions can be pre defines.
        - Functions can be user defines based on his needs.
        - We can pass parameter inside a function.(parameter: can be given by user as input to function)
        - We can add multiple parameters into function by using "*param_name".
"""
def simple(parameter):
    print(parameter)
    return parameter
res = simple("Hello")
print(res)

def details(name, age):
   print(f"Name: {name} and Age: {age}")
print(details("ABD", 20))


def printname(*name): ## The * in *name means collect any number of positional arguments into a tuple.
    print(name)
    print(name[0])
print(printname("a", "b", "c"))



## functions
def fun():
    print("Function execution")
fun()

def val(v):
    v[0] = 1
value = [2, 3, 4, 5]
val(value)
print(value) ## [1, 3, 4, 5]


"""
    Modules: Module is also called library, this library contains 
        set of functions which can be used by programmer for further use.
        -To use function within library we need to import module.
        -Command used: import <lib_name>
"""
import math
print("sqrt")
print(math.sqrt(25))

print("factorial")
print(math.factorial(5))

print("gcd")
print(math.gcd(17, 30))

## pow(base, power)
print("pow")
print(pow(2, 3))


"""
    Methods:
"""

method = [1,2,3,1,2,3,1]
method1 = [4,5,6]
print(method.count(1))
method.extend(method1)
print(method)


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. print(details(...)) gotcha - functions with no explicit return give None
# -------------------------
# NOTE: `details()` in your code above has no `return` statement, so it
# implicitly returns None. `print(details("ABD", 20))` therefore prints the
# name/age line from INSIDE the function, followed by "None" from the
# print() wrapping the call. This is a common beginner confusion point.
def no_return_example():
    print("doing work")
    # no return statement here

output = no_return_example()
print(output)   # None -> every function returns None implicitly if no `return` is given

print(f"{'*' * 60}")

# -------------------------
# 2. Default arguments and keyword arguments
# -------------------------
def greet(name, greeting="Hello"):   # 'greeting' has a DEFAULT value
    return f"{greeting}, {name}!"

print(greet("Alice"))                  # Hello, Alice!  -> uses default
print(greet("Bob", "Hi"))               # Hi, Bob!        -> overrides default
print(greet(name="Carol", greeting="Hey"))   # Hey, Carol!  -> keyword arguments (order doesn't matter)
print(greet(greeting="Yo", name="Dave"))       # Yo, Dave!    -> can be in any order when using keywords

print(f"{'*' * 60}")

# -------------------------
# 3. Returning MULTIPLE values (really returns a tuple, unpacked by the caller)
# -------------------------
def min_max(numbers):
    return min(numbers), max(numbers)   # this is actually returning a TUPLE (min(numbers), max(numbers))

lo, hi = min_max([4, 1, 7, 3])   # tuple unpacking on the caller's side
print(lo, hi)                       # 1 7

result = min_max([4, 1, 7, 3])
print(type(result), result)          # <class 'tuple'> (1, 7)

print(f"{'*' * 60}")

# -------------------------
# 4. Variable scope: local vs global vs nonlocal (VERY common interview topic)
# -------------------------
x = "global value"

def read_global():
    print(x)   # can READ a global variable without any special keyword

def modify_global():
    global x    # needed to MODIFY (rebind) the global variable from inside a function
    x = "modified by function"

read_global()          # global value
modify_global()
read_global()            # modified by function

def outer():
    y = "outer value"
    def inner():
        nonlocal y   # needed to modify a variable from an ENCLOSING (non-global) scope
        y = "modified by inner"
    inner()
    print(y)   # modified by inner

outer()

# GOTCHA: without 'global'/'nonlocal', assigning to a name inside a function
# creates a NEW LOCAL variable, shadowing the outer one, instead of modifying it:
count = 0
def broken_increment():
    count = count + 1   # UnboundLocalError! Python sees `count = ...` in this
                          # function and treats `count` as local for the WHOLE
                          # function, so reading it on the right-hand side fails
try:
    broken_increment()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)

print(f"{'*' * 60}")

# -------------------------
# 5. Docstrings and accessing them
# -------------------------
def area_of_circle(radius):
    """Calculate the area of a circle given its radius.

    Args:
        radius (float): the radius of the circle

    Returns:
        float: the area of the circle
    """
    return 3.14159 * radius ** 2

print(area_of_circle.__doc__)   # prints the docstring text
help(area_of_circle)              # also displays the docstring, plus the function signature

print(f"{'*' * 60}")

# -------------------------
# 6. Type hints (annotations) - NOT enforced at runtime, but great for
#    readability, tooling, and static type checkers like mypy
# -------------------------
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))          # 5
print(add("x", "y"))        # 'xy' -> still works! type hints are NOT enforced by Python itself
print(add.__annotations__)   # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

print(f"{'*' * 60}")

# -------------------------
# 7. Lambda functions - small anonymous, single-expression functions
# -------------------------
square = lambda x: x ** 2
print(square(5))   # 25

# very common real-world use: as the 'key' argument for sorting
people = [("Alice", 30), ("Bob", 25), ("Carol", 35)]
sorted_by_age = sorted(people, key=lambda person: person[1])
print(sorted_by_age)   # [('Bob', 25), ('Alice', 30), ('Carol', 35)]

# lambda is limited to a SINGLE expression - no statements, no multiple lines
# (no assignments, no loops, no multiple return paths inside it)

print(f"{'*' * 60}")

# -------------------------
# 8. Functions are first-class objects - can be assigned, passed, returned
# -------------------------
def shout(text):
    return text.upper()

my_func = shout            # assign a function to a variable (no parentheses = don't call it!)
print(my_func("hello"))     # HELLO

def apply_twice(func, value):
    return func(func(value))

print(apply_twice(shout, "hi"))   # HI -> shout() applied twice (uppercase twice, same result)

def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier   # returning a FUNCTION - this is a closure

times3 = make_multiplier(3)
print(times3(10))   # 30 -> 'times3' "remembers" n=3 even after make_multiplier() has returned

print(f"{'*' * 60}")

# -------------------------
# 9. Recursion - a function calling itself
# -------------------------
def factorial(n):
    if n <= 1:              # BASE CASE - required to stop the recursion
        return 1
    return n * factorial(n - 1)   # RECURSIVE CASE

print(factorial(5))   # 120

# Python has a default recursion limit (usually 1000) to prevent stack
# overflow from infinite/runaway recursion:
import sys
print(sys.getrecursionlimit())   # 1000 (default, can be changed with setrecursionlimit())

print(f"{'*' * 60}")

# -------------------------
# 10. Mutable default arguments - the classic Python function gotcha (recap
#     since your file passes a mutable list to a function - related concept)
# -------------------------
def buggy_append(item, items=[]):   # DANGEROUS - default list created ONCE at def time
    items.append(item)
    return items

print(buggy_append(1))   # [1]
print(buggy_append(2))    # [1, 2] -> NOT [2]! same list object reused across calls

def fixed_append(item, items=None):   # SAFE fix
    if items is None:
        items = []
    items.append(item)
    return items

print(fixed_append(1))   # [1]
print(fixed_append(2))    # [2] -> correctly independent each time

print(f"{'*' * 60}")

# -------------------------
# 11. Modules - different import styles
# -------------------------
import math as m                     # import with an alias
print(m.pi)                            # 3.14159...

from math import sqrt, pi              # import SPECIFIC names directly into the namespace
print(sqrt(16), pi)                     # 4.0 3.14159... -> no 'math.' prefix needed now

# from math import *                   # AVOID this - imports everything into the current
                                          # namespace, risking naming collisions and making
                                          # it unclear WHERE a name came from when reading code

print(f"{'*' * 60}")

# -------------------------
# 12. __name__ == "__main__" - controlling what runs on direct execution vs import
# -------------------------
print(__name__)   # '__main__' when this file is run directly, or the MODULE NAME
                    # (e.g. 'functions_module_methods') if this file is imported elsewhere

# Standard pattern for making a file both runnable AND importable:
def main():
    print("Main logic here")

if __name__ == "__main__":
    main()   # only runs when the file is executed directly, NOT when imported

print(f"{'*' * 60}")

# -------------------------
# 13. Exploring a module - dir(), help(), and finding what's available
# -------------------------
print(dir(math)[:10])   # first 10 names available in the math module (functions, constants)
# help(math)              # opens full documentation for the module (verbose, commented out here)

print(f"{'*' * 60}")

# -------------------------
# 14. Difference between a function and a method (the actual terminology distinction)
# -------------------------
# A FUNCTION is standalone (e.g., `len(x)`, `sum(x)`, your own `def fun():`).
# A METHOD is a function that belongs to (is called ON) an object/class,
# using dot notation (e.g., `my_list.append(x)`, `my_string.upper()`).
my_list = [1, 2, 3]
print(my_list.append)         # <built-in method append of list object at ...> -> it's a METHOD
print(len)                      # <built-in function len> -> it's a FUNCTION

# Internally, calling an_object.method(args) is equivalent to
# TypeName.method(an_object, args) - similar to how 'self' works in your own classes.
print(list.count(method, 1))     # same effect as method.count(1) from your original code

print(f"{'*' * 60}")

# -------------------------
# 15. Built-in functions worth knowing beyond math/pow (quick reference)
# -------------------------
print(abs(-5))            # 5      -> absolute value
print(round(3.567, 2))      # 3.57   -> rounding to 2 decimal places
print(divmod(17, 5))          # (3, 2) -> (quotient, remainder) in one call
print(sum([1, 2, 3]))           # 6      -> sum of an iterable
print(max([3, 1, 4]), min([3, 1, 4]))   # 4 1 -> max/min of an iterable
print(sorted([3, 1, 2]))                   # [1, 2, 3] -> returns a NEW sorted list
print(enumerate)                             # class 'enumerate' -> pairs items with an index
print(list(enumerate(["a", "b", "c"])))       # [(0, 'a'), (1, 'b'), (2, 'c')]
print(list(zip([1, 2], ["a", "b"])))            # [(1, 'a'), (2, 'b')] -> combines iterables element-wise
print(list(map(lambda x: x * 2, [1, 2, 3])))      # [2, 4, 6] -> applies a function to every item
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))   # [2, 4] -> keeps items matching a condition


## ==========================================================
## INTERVIEW QUESTIONS ON FUNCTIONS, MODULES & METHODS
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What does a Python function return if there is no explicit `return`
#    statement? What would `print(my_function())` show in that case?
#
# 2. What is the difference between a positional argument, a keyword argument,
#    and a default argument?
#
# 3. If a function does `return a, b`, what is actually being returned? How
#    would you "receive" both values on the caller's side?
#
# 4. What is the difference between local, global, and nonlocal scope in
#    Python? What keyword is required to MODIFY (not just read) a variable
#    from an outer scope inside a function?
#
# 5. Why does assigning to a variable INSIDE a function (without declaring it
#    `global`) cause an UnboundLocalError if that same variable name exists
#    at the module level and you try to read it first?
#
# 6. What is a docstring, and how would you access a function's docstring
#    programmatically (without opening the source file)?
#
# 7. Are Python type hints (e.g., `def add(a: int, b: int) -> int:`) enforced
#    at runtime? What tool would you use to actually check type correctness
#    based on these hints?
#
# 8. What is a lambda function, and what are its limitations compared to a
#    regular `def` function?
#
# 9. What does it mean that "functions are first-class objects" in Python?
#    Give an example of passing a function as an argument to another
#    function.
#
# 10. What is a closure? How does the "times3" example (a function returning
#     another function that remembers a variable) work internally?
#
# 11. What is recursion, and what MUST every correct recursive function have
#     to avoid infinite recursion? What happens if you exceed Python's
#     recursion limit?
#
# 12. Why is using a mutable default argument (like `def f(x, items=[])`)
#     considered a common Python bug? Walk through why it happens.
#
# 13. What is the difference between `import module`, `import module as m`,
#     and `from module import name`? Why is `from module import *` generally
#     discouraged?
#
# 14. What is the purpose of `if __name__ == "__main__":`? What is `__name__`
#     set to when a file is run directly versus when it's imported as a
#     module?
#
# 15. What is the actual difference between a "function" and a "method" in
#     Python terminology? Give an example of each.
#
# 16. How would you list all the available names/functions inside an imported
#     module without checking documentation?
#
# 17. What is the difference between `map()`/`filter()` (which return
#     iterators) and using a list comprehension to achieve the same result?
#
# 18. If you pass a mutable object (like a list) into a function and mutate it
#     in place, does the caller see the change? Does this depend on whether
#     you use `global`?
#
# 19. What does `*args` mean in a function definition, and how is it
#     different from just naming a parameter `args` without the asterisk?
#
# 20. How would you write a function that memorizes/caches results of
#     expensive recursive calls (e.g., a faster Fibonacci) using a built-in
#     Python decorator?