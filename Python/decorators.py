# ==============================================================================
# DECORATORS
# ==============================================================================
"""
NOTES:
- Functions are first-class objects: can be passed as args, returned, stored in vars.
- A decorator is a function that takes a function and returns a wrapped function.
- functools.wraps preserves the original function's __name__/__doc__ (without it,
    introspection tools/debuggers see the wrapper's metadata instead of the original's).
- @staticmethod: no access to instance (self) or class (cls). Just a plain function
    namespaced inside a class.
- @classmethod: receives the class (cls) instead of instance -> used for alternate
    constructors (e.g. Class.from_string(...)).
- @property: lets you access a method like an attribute; @x.setter lets you validate
    on assignment.
"""
# ========================================================================
"""
A Python decorator is a function that takes another function as input, extends or modifies 
    its behavior, and returns a new function—all without changing the original function's 
    source code.
Decorators act as "wrappers". They allow you to execute code before and after the target 
    function runs, making them highly effective for keeping code clean, readable, and reusable.
"""
def my_decorator(func):
    def wrapper():
        print("Something is happening BEFORE the function is called.")
        func()  # This runs the original function
        print("Something is happening AFTER the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# ========================================================================

import functools
import time

def timer(func):
    """Decorator that prints how long a function takes."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper


def retry(times=3):
    """Decorator FACTORY - takes an argument, returns the actual decorator."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt} failed: {e}")
            raise last_exception
        return wrapper
    return decorator


@timer
def slow_square(n):
    time.sleep(0.1)
    return n * n


attempt_counter = {"count": 0}

@retry(times=10)
def flaky_function():
    attempt_counter["count"] += 1
    if attempt_counter["count"] < 10:
        raise ValueError("Simulated failure")
    return "Success!"


class Circle:
    def __init__(self, radius):
        self._radius = radius  # convention: "_" = internal/protected

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @staticmethod
    def is_valid_radius(value):
        """No access to self/cls - just a utility function grouped in the class."""
        return value > 0

    @classmethod
    def unit_circle(cls):
        """Alternate constructor - uses cls, not self."""
        return cls(radius=2)


def decorators_demo():
    print("\n--- DECORATORS ---")
    print(slow_square(5))
    print("Function name preserved by @wraps:", slow_square.__name__)
    print(f"{'*' * 80}")

    print(flaky_function())
    print(f"{'*' * 80}")

    c = Circle(5)
    print("Area:", c.area)
    c.radius = 10  # uses the setter (with validation)
    print("New area after setter:", c.area)
    try:
        c.radius = -5  # triggers validation error
    except ValueError as e:
        print("Validation caught:", e)
    print(f"{'*' * 80}")

    print("Static method check:", Circle.is_valid_radius(5))
    print(f"{'*' * 80}")

    unit = Circle.unit_circle()  # classmethod alternate constructor
    print("Unit circle radius:", unit.radius)

## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. What a decorator ACTUALLY is - manual application without @ syntax
# -------------------------
def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def greet(name):
    return f"hello, {name}"

# @shout above a function is just syntactic sugar for this:
greet = shout(greet)
print(greet("alice"))   # HELLO, ALICE

# So @shout\ndef greet(name): ... is EXACTLY equivalent to writing greet = shout(greet)
# right after the function definition.

print(f"{'*' * 80}")

# -------------------------
# 2. Why functools.wraps matters - proving the problem it solves
# -------------------------
def bad_decorator(func):
    def wrapper(*args, **kwargs):   # NOTE: no @functools.wraps here
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def my_function():
    """Original docstring."""
    pass

print(my_function.__name__)   # 'wrapper' -> WRONG! lost the original name
print(my_function.__doc__)     # None      -> WRONG! lost the original docstring

def good_decorator(func):
    @functools.wraps(func)     # copies __name__, __doc__, __module__, etc. from func
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def my_function2():
    """Original docstring, preserved!"""
    pass

print(my_function2.__name__)   # 'my_function2' -> correct
print(my_function2.__doc__)     # 'Original docstring, preserved!' -> correct

print(f"{'*' * 80}")

# -------------------------
# 3. Stacking multiple decorators - ORDER MATTERS (bottom-up application,
#    top-down execution) - a VERY common interview trick question
# -------------------------
def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def text():
    return "Hello"

print(text())   # <b><i>Hello</i></b>
# Decorators are APPLIED bottom-up: italic(text) first, then bold(...) wraps
# that result. So the closest decorator to the function runs FIRST when the
# function is called (its output becomes the input to the next one up).

print(f"{'*' * 80}")

# -------------------------
# 4. Decorators on functions WITH arguments and return values (recap using *args/**kwargs)
# -------------------------
def uppercase_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() if isinstance(result, str) else result
    return wrapper

@uppercase_result
def combine(a, b):
    return f"{a}-{b}"

print(combine("foo", "bar"))   # FOO-BAR
# Using *args, **kwargs in the wrapper makes the decorator work with ANY
# function signature, regardless of how many/what kind of arguments it takes.

print(f"{'*' * 80}")

# -------------------------
# 5. Class-based decorators - using __call__ instead of a nested function
# -------------------------
class CountCalls:
    """A decorator implemented as a class, using __call__ to make instances callable."""
    def __init__(self, func):
        functools.update_wrapper(self, func)   # class-based equivalent of functools.wraps
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"Call #{self.call_count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    return "hi!"

print(say_hi())   # Call #1 to say_hi -> hi!
print(say_hi())   # Call #2 to say_hi -> hi!
print(say_hi.call_count)   # 2 -> state persists across calls, since it's stored on the instance

print(f"{'*' * 80}")

# -------------------------
# 6. functools.lru_cache - a REAL, extremely common built-in decorator (caching/memoization)
# -------------------------
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(30))                     # fast, thanks to caching -> without @lru_cache this would be
                                     # exponential time; with it, it's linear (each n computed once)
print(fib.cache_info())              # CacheInfo(hits=..., misses=..., maxsize=None, currsize=...)
fib.cache_clear()                     # clears the cache manually if needed

print(f"{'*' * 80}")

# -------------------------
# 7. functools.singledispatch - decorator for function overloading based on argument TYPE
# -------------------------
@functools.singledispatch
def describe(value):
    return f"Some value: {value}"

@describe.register(int)
def _(value):
    return f"An integer: {value}"

@describe.register(str)
def _(value):
    return f"A string: '{value}'"

print(describe(42))       # An integer: 42
print(describe("hi"))       # A string: 'hi'
print(describe(3.14))        # Some value: 3.14 -> falls back to the default implementation

print(f"{'*' * 80}")

# -------------------------
# 8. contextlib.contextmanager - turning a generator into a `with`-statement context manager
#    (a decorator, but for a DIFFERENT purpose than wrapping function calls)
# -------------------------
from contextlib import contextmanager

@contextmanager
def timer_context(label):
    start = time.perf_counter()
    yield                 # code inside the 'with' block runs here
    elapsed = time.perf_counter() - start
    print(f"{label} took {elapsed:.4f} seconds")

with timer_context("sleep block"):
    time.sleep(0.05)

print(f"{'*' * 80}")

# -------------------------
# 9. Decorators that accept optional arguments (@deco vs @deco())
# -------------------------
# retry(times=3) above must ALWAYS be called with parentheses: @retry() or
# @retry(times=5) - it can't be used as bare @retry. To support BOTH styles,
# you need extra logic to detect whether the decorator was called directly on
# a function or with arguments first:
def flexible_decorator(func=None, *, label="default"):
    def actual_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print(f"[{label}] calling {f.__name__}")
            return f(*args, **kwargs)
        return wrapper
    if func is not None:
        return actual_decorator(func)   # used as @flexible_decorator (no parens)
    return actual_decorator               # used as @flexible_decorator(label="x") (with parens)

@flexible_decorator
def a():
    return "a called"

@flexible_decorator(label="custom")
def b():
    return "b called"

print(a())   # [default] calling a -> a called
print(b())    # [custom] calling b -> b called

print(f"{'*' * 80}")

# -------------------------
# 10. Common mistakes / gotchas with decorators
# -------------------------
# MISTAKE 1: forgetting to RETURN the wrapper from the decorator function
def broken_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    # forgot: return wrapper   <- without this, decorator returns None!
    # Applying @broken_decorator would make the decorated name become None.

# MISTAKE 2: forgetting *args, **kwargs in wrapper -> breaks for functions
# with any parameters other than exactly what you hardcoded.

# MISTAKE 3: mutable default arguments INSIDE a decorator's closure (same
# mutable-default trap as regular functions, just less obvious when nested).

# MISTAKE 4: applying a decorator meant for functions directly to a class
# method without accounting for 'self' being the first positional argument
# (usually fine since *args captures it, but easy to forget when debugging).

print("All common decorator gotchas noted above (see comments).")


## ==========================================================
## INTERVIEW QUESTIONS ON DECORATORS
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is a decorator in Python, conceptually? What does `@decorator` above
#    a function definition actually translate to under the hood?
#
# 2. Why is functools.wraps important when writing a decorator? What specific
#    problems occur if you omit it?
#
# 3. If you stack multiple decorators on top of a single function (e.g.,
#    @bold @italic def text(): ...), in what order are they applied, and in
#    what order do they execute when the function is called?
#
# 4. What is a "decorator factory" (a decorator that takes its own arguments,
#    like @retry(times=3))? How does its structure differ from a plain
#    decorator (an extra level of nesting)?
#
# 5. How would you write a decorator that works on ANY function, regardless of
#    how many positional or keyword arguments it takes?
#
# 6. How would you implement a decorator using a class instead of a nested
#    function? What dunder method makes a class instance callable?
#
# 7. What does functools.lru_cache do, and what problem does it solve? What
#    are the tradeoffs of using it (e.g., memory usage, mutable/unhashable
#    arguments)?
#
# 8. Can functools.lru_cache be used on a function with unhashable arguments
#    (like a list)? Why or why not?
#
# 9. What does functools.singledispatch do, and how is it different from
#    traditional method overloading in languages like Java?
#
# 10. What is the difference between a decorator used for wrapping function
#     calls versus @contextmanager, which is used to build a `with`-statement
#     context manager?
#
# 11. How would you design a decorator that can be used BOTH as `@my_decorator`
#     (no parentheses) AND `@my_decorator(option=True)` (with parentheses)?
#
# 12. What happens if you forget to return the wrapper function from inside
#     your decorator function? What would calling the decorated function do?
#
# 13. What's the difference between @staticmethod, @classmethod, and a regular
#     instance method decorator-wise? Which ones change what gets passed as
#     the first argument?
#
# 14. How does @property work internally? What is @x.setter actually doing,
#     and why must the setter method have the SAME NAME as the property?
#
# 15. Can you apply a decorator to a class itself (not just a function or
#     method)? What would that look like, and what's a real use case (hint:
#     dataclasses use a similar idea)?
#
# 16. What is the performance overhead of using decorators? Is there a
#     meaningful cost to wrapping a function, especially for something called
#     millions of times?
#
# 17. How would you write a decorator that only allows a function to run if a
#     certain condition is true (e.g., a feature flag), otherwise skips it?
#
# 18. What's the difference between decorating a function ONCE at definition
#     time (@decorator) versus applying it dynamically at runtime
#     (func = decorator(func))?
#
# 19. If a decorated function raises an exception, does the decorator's
#     wrapper automatically see/handle that exception? How would you add
#     custom exception handling inside a decorator (like the retry() example)?
#
# 20. Why can accessing `functools.wraps`-decorated function's __wrapped__
#     attribute be useful for introspection or testing?


# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == "__main__":
    decorators_demo()