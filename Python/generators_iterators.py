# ==============================================================================
# GENERATORS & ITERATORS
# ==============================================================================
"""
NOTES:
- Iterator protocol: an object needs __iter__ (returns itself) and __next__
    (returns next value, raises StopIteration when done).
- 'yield' pauses a function and remembers its state; 'return' ends it completely.

- Generator expressions (x for x in ...) are LAZY - don't build the whole list in
    memory, unlike list comprehensions [x for x in ...]. Huge memory savings for
    large/infinite sequences.
- 'yield from' delegates to a sub-generator/sub-iterable - useful for flattening
    or composing generators.
"""

def fibonacci_generator():
    """Infinite generator - only computes values as requested."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


class CountDown:
    """Custom iterator class (the manual, non-generator way)."""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # an iterator must return itself from __iter__

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def flatten(nested_list):
    """yield from - delegates to sub-iterables to flatten nested lists."""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)  # recursive delegation
        else:
            yield item


def generators_demo():
    print("\n--- GENERATORS & ITERATORS ---")

    fib = fibonacci_generator()
    first_10 = [next(fib) for _ in range(10)]
    print("First 10 Fibonacci:", first_10)
    print(f"{'*' * 80}")

    print("Custom iterator countdown:", list(CountDown(5)))
    print(f"{'*' * 80}")

    nested = [1, [2, 3, [4, 5]], [22], 6, [7, [8, [9, 10, 1]]]]
    print("Flattened:", list(flatten(nested)))
    print(f"{'*' * 80}")

    # Memory difference: list comp builds it all now, generator builds lazily
    list_comp = [x**2 for x in range(5)]       # fully in memory
    gen_expr = (x**2 for x in range(5))        # lazy, computed on demand
    print("List comprehension:", list_comp)
    print("Generator expression (consumed):", list(gen_expr))

## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. Iterable vs Iterator - the core distinction (VERY commonly confused)
# -------------------------
# ITERABLE: any object you can loop over (has __iter__). Examples: list, str,
#           dict, set, tuple, range, file objects.
# ITERATOR: an object with BOTH __iter__ AND __next__, that tracks its OWN
#           position/state and produces values one at a time via next().
# Every iterator is an iterable, but NOT every iterable is an iterator!

lst = [1, 2, 3]
print(hasattr(lst, '__iter__'))    # True  -> list IS iterable
print(hasattr(lst, '__next__'))     # False -> but list is NOT itself an iterator

it = iter(lst)                        # iter() converts an iterable INTO an iterator
print(hasattr(it, '__iter__'))         # True
print(hasattr(it, '__next__'))          # True -> now it's both

print(f"{'*' * 80}")

# -------------------------
# 2. Manually using next() and seeing StopIteration raised
# -------------------------
it = iter([10, 20])
print(next(it))    # 10
print(next(it))     # 20
try:
    print(next(it))   # nothing left!
except StopIteration:
    print("StopIteration raised - iterator exhausted")

# next() also accepts a DEFAULT value, avoiding the need for try/except:
it2 = iter([10])
print(next(it2, "no more items"))   # 10
print(next(it2, "no more items"))    # 'no more items' -> default returned instead of raising

print(f"{'*' * 80}")

# -------------------------
# 3. A 'for' loop is just syntactic sugar around iter() + next() + StopIteration
# -------------------------
# This:
for x in [1, 2, 3]:
    print(x)

# is roughly equivalent to:
_it = iter([1, 2, 3])
while True:
    try:
        x = next(_it)
    except StopIteration:
        break
    print(x)

print(f"{'*' * 80}")

# -------------------------
# 4. Generators are EXHAUSTED after one full pass - can't be reused/reset
# -------------------------
def small_gen():
    yield 1
    yield 2

g = small_gen()
print(list(g))   # [1, 2]
print(list(g))    # [] -> EMPTY! generator is already exhausted, must create a NEW one
                    #        to iterate again (g = small_gen())

print(f"{'*' * 80}")

# -------------------------
# 5. Memory comparison: generator expression vs list comprehension (PROVEN with sys.getsizeof)
# -------------------------
import sys
list_comp = [x for x in range(10000)]
gen_expr = (x for x in range(10000))

print(f"List comprehension size: {sys.getsizeof(list_comp)} bytes")   # large - stores ALL 10000 items
print(f"Generator expression size: {sys.getsizeof(gen_expr)} bytes")   # tiny - stores only generator STATE,
                                                                          # regardless of how many items it'll yield

print(f"{'*' * 80}")

# -------------------------
# 6. send() - sending a value INTO a generator (turns it into a basic coroutine)
# -------------------------
def running_total():
    total = 0
    while True:
        value = yield total   # pauses here, returns 'total', waits to RECEIVE a value via send()
        total += value

gen = running_total()
next(gen)              # PRIME the generator - must advance to the first yield before sending
print(gen.send(10))      # 10  -> sends 10 in, resumes, returns new total
print(gen.send(5))         # 15  -> sends 5 in, adds to running total

print(f"{'*' * 80}")

# -------------------------
# 7. throw() and close() - injecting exceptions / terminating a generator early
# -------------------------
def resilient_gen():
    try:
        while True:
            yield "running"
    except ValueError:
        yield "caught a ValueError inside the generator!"
    finally:
        print("Generator cleanup ran (finally block)")

g = resilient_gen()
print(next(g))              # running
print(g.throw(ValueError))    # caught a ValueError inside the generator! -> injects
                                # an exception AT the yield point inside the generator
g.close()                       # forcibly terminates the generator, triggers 'finally'

print(f"{'*' * 80}")

# -------------------------
# 8. Generators as lightweight, memory-efficient pipelines (real-world pattern)
# -------------------------
def read_lines(lines):
    for line in lines:
        yield line.strip()

def filter_non_empty(lines):
    for line in lines:
        if line:
            yield line

def uppercase_lines(lines):
    for line in lines:
        yield line.upper()

raw_lines = ["  hello  ", "", "  world  ", "   "]
pipeline = uppercase_lines(filter_non_empty(read_lines(raw_lines)))
print(list(pipeline))   # ['HELLO', 'WORLD']
# Each stage processes ONE item at a time and passes it along - nothing is
# fully materialized in memory at any stage, great for large data/log processing.

print(f"{'*' * 80}")

# -------------------------
# 9. itertools module - the standard toolkit for working with iterators
# -------------------------
import itertools

print(list(itertools.islice(fibonacci_generator(), 5)))   # [0, 1, 1, 2, 3] -> take first 5
                                                              # from an INFINITE generator safely

print(list(itertools.chain([1, 2], [3, 4])))                # [1, 2, 3, 4] -> chain multiple iterables

print(list(itertools.count(10, 2))[:5] if False else list(itertools.islice(itertools.count(10, 2), 5)))
# [10, 12, 14, 16, 18] -> count() is an INFINITE counter, must slice it with islice

print(list(itertools.cycle([1, 2, 3]))[:7] if False else list(itertools.islice(itertools.cycle([1, 2, 3]), 7)))
# [1, 2, 3, 1, 2, 3, 1] -> cycles through indefinitely, again needs islice to limit

print(list(itertools.permutations([1, 2, 3], 2)))    # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]
print(list(itertools.combinations([1, 2, 3], 2)))       # [(1,2),(1,3),(2,3)]

print(f"{'*' * 80}")

# -------------------------
# 10. Custom iterator class vs generator function - when to choose which
# -------------------------
# Your CountDown class shows the MANUAL way (implementing __iter__/__next__).
# A generator function does the SAME thing with much less code:
def countdown_gen(start):
    while start >= 0:
        yield start
        start -= 1

print(list(countdown_gen(5)))   # [5, 4, 3, 2, 1, 0] -> same result as CountDown(5), way less code

# WHEN to still use a class-based iterator instead of a generator function:
#   - you need extra methods/state beyond simple iteration (e.g. .reset(),
#     .peek(), custom attributes accessed from outside)
#   - you need the object to be iterated MULTIPLE times independently
#     (each call to __iter__ could return a fresh iterator, unlike a
#     generator object which is single-use/exhausted after one pass)

print(f"{'*' * 80}")

# -------------------------
# 11. Generators and 'yield' vs a normal function returning a list - laziness recap
# -------------------------
def eager_squares(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result             # returns the WHOLE list immediately, computed upfront

def lazy_squares(n):
    for i in range(n):
        yield i ** 2            # computes ONE value at a time, only when asked (via next())

print(eager_squares(5))          # [0, 1, 4, 9, 16] -> already fully computed
print(list(lazy_squares(5)))       # [0, 1, 4, 9, 16] -> same output, but computed lazily on demand

# Practical benefit: lazy_squares(10**9) creates the generator INSTANTLY,
# while eager_squares(10**9) would try to build a billion-item list right away
# (huge memory + time cost, possibly a MemoryError).


## ==========================================================
## INTERVIEW QUESTIONS ON GENERATORS & ITERATORS
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is the difference between an iterable and an iterator? Can you give
#    an example of something that is iterable but NOT itself an iterator?
#
# 2. What two dunder methods must an object implement to satisfy the iterator
#    protocol? What should __next__ do once there are no more items left?
#
# 3. What is the difference between `yield` and `return` inside a generator
#    function?
#
# 4. Why are generator expressions more memory-efficient than list
#    comprehensions? How would you PROVE this difference in code?
#
# 5. Can a generator be iterated over more than once? What happens if you
#    call list() on the same generator object twice?
#
# 6. What does `yield from` do, and what real problem does it solve when
#    working with nested/recursive generators (like flattening a nested
#    list)?
#
# 7. What is the purpose of a generator's `send()` method? Why must you call
#    `next()` once on a generator before you can `send()` a value into it?
#
# 8. What does calling `.throw()` on a generator do? What about `.close()`?
#    How would a `finally` block inside the generator react to `.close()`?
#
# 9. How would you safely take the first N values from an INFINITE generator
#    (like a Fibonacci sequence generator) without it looping forever?
#
# 10. What is `itertools.islice()`, and why is it necessary when working with
#     infinite iterators like `itertools.count()` or `itertools.cycle()`?
#
# 11. When would you choose to write a class-based iterator (with __iter__ and
#     __next__) instead of a simpler generator function? What can a class do
#     that a generator function can't as easily?
#
# 12. What is a generator pipeline? How does chaining several generator
#     functions together (each processing one item at a time) help with
#     memory usage when processing large files or datasets?
#
# 13. What exception does a `for` loop rely on internally to know when to
#     stop looping? Is this exception something you'd normally need to catch
#     yourself?
#
# 14. What does `next(iterator, default)` do differently from `next(iterator)`
#     when the iterator is exhausted?
#
# 15. What's the difference between `itertools.chain()` and simply
#     concatenating two lists with `+`? When would chain() be preferable?
#
# 16. Why is `fibonacci_generator()` in this file able to represent an
#     "infinite" sequence without ever running out of memory?
#
# 17. What is a "coroutine" in the context of a Python generator using
#     `send()`? How is this different from `async`/`await` coroutines
#     introduced later in Python (conceptually, at a high level)?
#
# 18. How would you write a generator function that flattens an arbitrarily
#     nested list (lists within lists within lists) using `yield from`?
#
# 19. Are generator objects thread-safe? What would happen if two threads
#     called `next()` on the SAME generator object concurrently?
#
# 20. What's the time and space complexity tradeoff between materializing a
#     full list upfront (`[x**2 for x in range(n)]`) versus using a generator
#     (`(x**2 for x in range(n))`) when you only need to iterate through the
#     values once?


if __name__ == "__main__":
    generators_demo()