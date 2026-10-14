# boolean data type

a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION
## ==========================================================

# -------------------------
# 1. bool is a SUBCLASS of int (classic interview gotcha)
# -------------------------
print(isinstance(True, int))    # True -> bool inherits from int
print(issubclass(bool, int))    # True

# Internally: True == 1 and False == 0
print(True == 1)     # True
print(False == 0)    # True
print(True + True)   # 2   -> arithmetic works because bool IS an int
print(True * 5)      # 5
print(sum([True, True, False, True]))  # 3 -> counts True values, common trick

print(f"{'*' * 50}")

# -------------------------
# 2. bool has only TWO instances: True and False (singletons)
# -------------------------
x = True
y = True
print(x is y)    # True -> always safe to use 'is' with True/False (unlike other objects)
print(x is True) # True -> preferred check is `if x:` not `if x is True:` (see gotcha below)

print(f"{'*' * 50}")

# -------------------------
# 3. Truthy and Falsy values (VERY common interview topic)
# -------------------------
# Everything in Python has an inherent truth value when used in a boolean context.
# FALSY values in Python (this is the complete list) :- False, None, 0, 0.0, 0j, '', [], (), {}, set(), range(0)
# Everything else is truthy.

print(bool(0))          # False
print(bool(0.0))        # False
print(bool(""))         # False -> empty string
print(bool([]))         # False -> empty list
print(bool({}))         # False -> empty dict
print(bool(set()))      # False -> empty set
print(bool(None))       # False

print(bool(1))           # True
print(bool(-1))          # True -> any nonzero number is truthy, including negatives
print(bool("False"))     # True -> non-empty string, even the word "False", is truthy!
print(bool([0]))         # True -> non-empty list (even containing falsy items) is truthy
print(bool(" "))         # True -> a single space is a non-empty string -> truthy

print(f"{'*' * 50}")

# -------------------------
# 4. bool() conversion / constructor
# -------------------------
print(bool("hello"))    # True
print(bool(3.14))       # True
print(bool(-0.0))       # False -> -0.0 is still considered zero

print(f"{'*' * 50}")

# -------------------------
# 5. Comparison operators ALWAYS return a bool
# -------------------------
print(type(5 > 3))       # <class 'bool'>
print(5 == 5)             # True
print(5 != 3)              # True
print(3 < 5 < 10)          # True -> CHAINED comparison: equivalent to (3 < 5) and (5 < 10) -> True and True
print(10 > 5 > 8)          # False -> equivalent to (10 > 5) and (5 > 8) -> True and False

print(f"{'*' * 50}")

# -------------------------
# 6. Logical operators: and, or, not (SHORT-CIRCUIT evaluation)
# -------------------------
# 'and'/'or' don't always return True/False - they return one of the OPERANDS.
print(True and False)   # False
print(1 and 2)           # 2   -> 'and' returns the SECOND operand if the first is truthy
print(0 and 2)           # 0   -> 'and' returns the FIRST operand if it's falsy (short-circuits)
print(1 or 2)             # 1   -> 'or' returns the FIRST operand if it's truthy (short-circuits)
print(0 or 2)             # 2   -> 'or' returns the SECOND operand if the first is falsy
print(not True)           # False
print(not 0)               # True -> not converts to bool first, then inverts

# Practical use: default values via 'or'
name = "" or "Anonymous"
print(name)   # 'Anonymous' -> common pattern, though `x if x else default` is more explicit

# Short-circuit avoids errors - second operand never evaluated if not needed
def risky():
    print("risky() was called")
    return True

print(False and risky())   # False -> risky() is NEVER called, avoids unnecessary/unsafe call
print(True or risky())      # True  -> risky() is NEVER called

print(f"{'*' * 50}")

# -------------------------
# 7. Logical (and/or/not) vs Bitwise (&, |, ~) operators - IMPORTANT distinction
# -------------------------
# and/or/not -> work on truthy/falsy values, short-circuit, meant for booleans/conditionals
# &, |, ~     -> work bit-by-bit on integers (or element-wise on things like numpy arrays/pandas Series)
#                do NOT short-circuit, both sides always evaluated

print(True & False)   # False -> works because bool is int under the hood (bitwise AND: 1 & 0)
print(True | False)   # True
print(~True)           # -2   -> bitwise NOT on int 1 -> -(x+1) --> -(1+1) = -2 (NOT a bool!)
# ~x == -(x + 1)
# ~True == ~1 == -(1 + 1) == -2
print(~False)           # # ~False == ~0 == -(0 + 1) == -1
print(type(~True))     # <class 'int'> -> ~ on a bool returns an int, not a bool

# common bug: using & instead of and for boolean logic in plain Python code
# a = 5
# if a > 0 & a < 10:   # WRONG! & has higher precedence than comparison operators,
#                       # this actually evaluates as: a > (0 & a) < 10 -> unexpected!
# Correct: if a > 0 and a < 10:

print(f"{'*' * 50}")

# -------------------------
# 8. all() and any() - built-ins that work great with booleans/iterables
# -------------------------
print(all([True, True, True]))     # True  -> True if ALL elements are truthy (or iterable is empty)
print(all([True, False, True]))    # False
print(all([]))                      # True  -> vacuously true for empty iterable
print(any([False, False, True]))    # True  -> True if AT LEAST ONE element is truthy
print(any([]))                       # False -> vacuously false for empty iterable

nums = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in nums))   # True -> works great with generator expressions

nums = [2, 3, 4, 6, 8]
print(any(n % 2 == 0 for n in nums))   # True

print(f"{'*' * 50}")

# -------------------------
# 9. Custom objects and truthiness: __bool__ and __len__
# -------------------------
# Python checks __bool__() first; if not defined, falls back to __len__() (0 = falsy);
# if neither is defined, the object is ALWAYS truthy.
class EmptyCart:
    def __len__(self):
        return 0    # no __bool__ defined, so Python uses __len__ to decide truthiness

cart = EmptyCart()
print(bool(cart))    # False -> because len(cart) == 0

class AlwaysTruthy:
    pass   # no __bool__, no __len__ -> defaults to True

print(bool(AlwaysTruthy()))   # True

class CustomBool:
    def __bool__(self):
        return False    # __bool__ takes priority over __len__ if both exist

print(bool(CustomBool()))   # False

print(f"{'*' * 50}")

# -------------------------
# 10. Common anti-pattern: comparing explicitly to True/False
# -------------------------
flag = True
# BAD (not Pythonic):
if flag == True:
    pass
# GOOD:
if flag:
    pass

# This matters MORE than it looks: if flag is something like 1 or "yes" (truthy but
# not literally True), `flag == True` can behave unexpectedly:
print(1 == True)      # True  -> because bool is a subclass of int
print("yes" == True)  # False -> non-bool truthy values are NOT == True!
if "yes":              # this works correctly (truthy check)
    print("this runs")

print(f"{'*' * 50}")

# -------------------------
# 11. Walrus operator (:=) often used alongside boolean conditions (Python 3.8+)
# -------------------------
data = [1, 2, 3, 4, 5]
# assign and test in one expression
if (n := len(data)) > 3:
    print(f"List is long, length = {n}")

print(f"{'*' * 50}")

# -------------------------
# 12. bool() on collections/containers - useful for "is empty" checks
# -------------------------
def process_items(items):
    if not items:              # Pythonic way to check for empty list/None
        print("No items to process")
        return
    print(f"Processing {len(items)} items")

process_items([])       # No items to process
process_items(None)     # No items to process
process_items([1, 2])   # Processing 2 items


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON BOOLEAN DATA TYPE
## ==========================================================
"""
1.  Is bool a separate primitive type in Python, or is it related to another type? What does `issubclass(bool, int)` 
    return, and what are the practical implications?
A:  bool is not a separate primitive type — it's a subclass of int.
        >>> issubclass(bool, int)
        True    
        >>> isinstance(True, int)
        True
-----------------------------------------------------------------------------------------------------------------------
2.  What are all the "falsy" values in Python? Name the complete list.
A:  Python considers the following values falsy (i.e., bool(x) evaluates to False):
        bool(False), bool(None), bool(0), bool(0.0), bool(0j), bool(""), bool([]), bool(()), bool({}), bool(set())
-----------------------------------------------------------------------------------------------------------------------
3.  Why is `bool("False")` True even though the string literally says "False"?
A:  bool("False") is True because Python's truthiness test for strings only cares about one thing: is the string empty
    or not? It doesn't look at what the string contains
-----------------------------------------------------------------------------------------------------------------------
4.  What do the `and` and `or` operators actually RETURN in Python? Do they always
    return True/False? Give an example showing otherwise.
A:  The rule is:
        x and y → returns x if x is falsy; otherwise returns y
        x or y → returns x if x is truthy; otherwise returns y
    >>> 5 and 10
    10
    >>> 0 and 10
    0
    >>> '' or 'default'
    'default'
    >>> 'hello' or 'default'
    'hello'
    >>> [] and [1, 2, 3]
    []
    >>> None or 0
    0
-----------------------------------------------------------------------------------------------------------------------
5.  What is short-circuit evaluation? Give a practical example where it prevents
    an error (e.g., checking `x is not None and x.value > 0`).
A:  Short-circuit evaluation means Python stops evaluating a boolean expression as soon as the overall result is 
        already determined, without evaluating the remaining operands.
    In x and y: if x is falsy, Python already knows the result is falsy — so y is never evaluated.
    In x or y: if x is truthy, Python already knows the result is truthy — so y is never evaluated.
    
    Example:
        class Item:
        def __init__(self, value=None):
            self.value = value
    
        x = None
        # Without short-circuiting, this would crash:
        if x is not None and x.value > 0:
            print("Positive value")
        else:
            print("Skipped safely")
    
    Proof it would otherwise crash:
        >>> x = None
        >>> x.value > 0
        AttributeError: 'NoneType' object has no attribute 'value'
-----------------------------------------------------------------------------------------------------------------------
6.  What is the difference between the logical operators (and, or, not) and the
    bitwise operators (&, |, ~) when used with booleans?
A:  Logical operators short-circuit — they may skip evaluating the right operand entirely.
    Bitwise operators always evaluate both operands — there's no shortcut.
    Example:    
        def noisy(val, label):
            print(f"evaluated {label}")
            return val
        # Logical: short-circuits, right side never runs
        False and noisy(True, "right")   # prints nothing, returns False
        # Bitwise: always evaluates both sides
        False & noisy(True, "right")     # prints "evaluated right", returns False
-----------------------------------------------------------------------------------------------------------------------
7.  Why does `~True` return -2 instead of False? Explain what's happening under the hood.
A:  ~x = ~True = ~1 = -(x+1) = -(1+1) = -2
-----------------------------------------------------------------------------------------------------------------------
8.  What's wrong with writing `if a > 0 & a < 10:` instead of `if a > 0 and a < 10:`? 
    (Hint: think about operator precedence.)
A:  Because '&' has higher precedence than '>' 'and' '<', Python evaluates 0 & a first, before either comparison:
        if a > (0 & a) < 10:
    Example:    
        a = 5
        print(a > 0 & a < 10)        # True — but for the WRONG reason
        print(a > 0 and a < 10)      # True — for the RIGHT reason
        
        a = -5
        print(a > 0 & a < 10)        # True  ❗ WRONG — a is not > 0, but this says True!
        print(a > 0 and a < 10)      # False — correct
-----------------------------------------------------------------------------------------------------------------------
9.  What do all() and any() return when called on an empty iterable? Why does that make logical sense (vacuous truth)?
A:  >>> all([])
    True
    >>> any([])
    False
    
    What all() and any() actually do:
        all(iterable) → True if every element is truthy (returns False on the first falsy element found, else True)
        any(iterable) → True if at least one element is truthy (returns True on the first truthy element found, else False)
        
    Why all([]) is True — vacuous truth
        all() is essentially asking: "Is there any element that fails the condition?" — if it can't find a single 
        counterexample, it says True.
    
    Why any([]) is False
        any() is asking: "Does at least one element satisfy the condition?" — it needs positive evidence, at least 
        one truthy element, to say True.
-----------------------------------------------------------------------------------------------------------------------
10. How does Python determine the truthiness of a custom object? Explain the role of __bool__ and __len__, 
    and which one takes priority.
A:  The lookup order:
        1. Look for __bool__. If the class defines it, Python calls obj.__bool__() and uses its return value directly 
            (it must return an actual bool, i.e. True or False).
        2. If __bool__ is not defined, look for __len__. Python calls obj.__len__(). If it returns 0, the object is 
            falsy; any other (non-negative) integer means truthy.
        3. If neither is defined, the object is always truthy — every instance of that class evaluates to True, no 
            matter its internal state.
    
    Demonstrating priority: __bool__ wins:
        class Weird:
            def __bool__(self):
                return False
            def __len__(self):
                return 100   # nonzero — would normally mean "truthy"
        
        w = Weird()
        print(bool(w))   # False — __bool__ wins, __len__ is ignored entirely
        print(len(w))    # 100 — len() itself still works fine
        
    Only __len__ defined: falls back to length:
        class Bag:
            def __init__(self, items):
                self.items = items
            def __len__(self):
                return len(self.items)
        
        b1 = Bag([])
        b2 = Bag([1, 2, 3])
        
        print(bool(b1))   # False — len() == 0
        print(bool(b2))   # True  — len() == 3
    
-----------------------------------------------------------------------------------------------------------------------
11. Why is `if flag == True:` considered bad practice compared to `if flag:`? Give a scenario where the two behave differently.
A:  Reason 1: Redundant style 
        if flag: already asks "is this truthy?" — which is exactly what you want when checking a boolean. 
        Writing == True adds a comparison that doesn't add any information if flag is a real bool, just extra characters
        
    if flag == True:   # works, but redundant
    if flag:           # idiomatic, same result — for actual booleans
        
    Reason 2: They actually behave differently — the real bug
        if flag: checks truthiness (is it non-zero / non-empty / not None, etc.). if flag == True: checks strict 
        equality to the boolean True. These are not the same test, and the gap shows up whenever flag isn't a "clean" boolean.
        
    flag = 2   # e.g., some API returns 0/1/2 as a "status" or count, not a strict bool
    if flag:
        print("A: truthy branch runs")      # ✅ prints — 2 is nonzero, so truthy
    
    if flag == True:
        print("B: equals True branch runs") # ❌ does NOT print!
-----------------------------------------------------------------------------------------------------------------------
12. What does chained comparison like `3 < 5 < 10` actually evaluate to internally? Is it the same as `(3 < 5) < 10`?
A: What it actually evaluates to:
    3 < 5 < 10 ==> (3 < 5) and (5 < 10)
    
-----------------------------------------------------------------------------------------------------------------------
13. Is `True is True` guaranteed to be True in every case? Why can you safely use 'is' with booleans, unlike with 
    most other objects (e.g., strings, ints > 256)?
A:  Yes — True is True (and False is False) is always guaranteed to be True, in every Python implementation, 
    every version, every time. This is one of the few is comparisons in Python that's actually part of the language 
    guarantee, not an implementation detail you're exploiting.

        >>> True is True
        True
        >>> False is False
        True
        >>> True is False
        False

    Why this differs from ints/strings
        For most objects, is checks memory identity, which is generally an implementation detail of how the 
        interpreter manages memory — not something the language promises:
    
        >>> a = 1000
        >>> b = 1000
        >>> a is b
        False        # two separate int objects, just happen to have equal value
        
        >>> x = "hello world!"
        >>> y = "hello world!"
        >>> x is y
        False  
-----------------------------------------------------------------------------------------------------------------------
14. What does `sum([True, False, True, True])` return, and why does this work?
A:  sum([True, False, True, True])
    3
    Why this works
        sum() adds up the elements of an iterable using the + operator. Since bool is a subclass of int, 
        True and False behave as 1 and 0 respectively in any arithmetic context — including addition:
            
    True + False + True + True
    = 1 + 0 + 1 + 1
    = 3
-----------------------------------------------------------------------------------------------------------------------
15. How would you check if a list, dict, or string is empty in a Pythonic way, without using `len(x) == 0`?
A:  The Pythonic way is to just rely on truthiness directly — since empty containers are falsy, you can write:
    # List
    my_list = []
    if not my_list:
        print("list is empty")     # prints
    
    # Dict
    my_dict = {}
    if not my_dict:
        print("dict is empty")     # prints
    
    # String
    my_str = ""
    if not my_str:
        print("string is empty")   # prints
-----------------------------------------------------------------------------------------------------------------------
16. What is the walrus operator (:=), and how can it be used to simplify a condition that both assigns and Test_Cases a value?
A:  The walrus operator (:=), officially called the assignment expression, was introduced in Python 3.8 (PEP 572). 
    It lets you assign a value to a variable and use that value in the same expression, instead of needing a separate 
    assignment statement beforehand.
    
    Basic syntax:
        (variable := expression)
        
    if (n := len(data)) > 10:
    print(f"Too long: {n}")
-----------------------------------------------------------------------------------------------------------------------
17. What's the difference in behavior between `0 and some_function()` and `0 & some_function()` in terms of whether 
    some_function() gets called?
A:  The key difference: and short-circuits and will never call some_function(), while & always evaluates both 
    operands, so it calls some_function() unconditionally — even though 0 alone already determines a falsy-ish result either way.
    
    0 and some_function() — function is NOT called:
    def some_function():
        print("called!")
        return True
    
    result = 0 and some_function()
    print(result)       # 0
    
    0 & some_function() — function IS called:
    def some_function():
        print("called!")
        return True
    result = 0 & some_function()
    print(result)
    
    Output:
        called!
        0
-----------------------------------------------------------------------------------------------------------------------
18. If a custom class defines neither __bool__ nor __len__, what is the truthiness of its instances by default?
A:  class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    p1 = Point(0, 0)
    p2 = Point(5, 10)
    
    print(bool(p1))   # True
    print(bool(p2))   # True
    
    if p1:
        print("p1 is truthy")   # prints — even though x and y are both 0!
        
    Why this happens:
        When Python evaluates bool(obj), it follows the lookup order covered earlier: check __bool__ first, then 
        fall back to __len__. If neither exists on the class (or is inherited from anywhere but object), Python 
        falls back to the default implementation from the base object class, which unconditionally returns True for every instance.
-----------------------------------------------------------------------------------------------------------------------
19. Why might using `or` for default values (e.g., `value = input_val or default`) be risky in certain cases? 
    (Hint: think about legitimate falsy inputs like 0.)
A:  value = input_val or default
    This returns default whenever input_val is falsy — but falsy includes 0, 0.0, '', [], {}, and False, all of which 
    can be completely legitimate, intentional values, not just "absence of a value."
-----------------------------------------------------------------------------------------------------------------------
20. What does `True + True + False` evaluate to, and what type is the result?
A: >>> True + True + False
    2
    >>> type(True + True + False)
    <class 'int'>
"""
