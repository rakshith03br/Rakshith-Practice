# ==============================================================================
# *ARGS, **KWARGS & UNPACKING
# ==============================================================================
"""
NOTES:
- *args:- collects extra positional args into a tuple.
- **kwargs:- collects extra keyword args into a dict.

- Order in function def: def f(pos, default=val, *args, kw_only, **kwargs)
- DANGER: mutable default arguments (e.g. def f(x, items=[])) are created ONCE
  when the function is DEFINED, not each call - so they persist/accumulate
  across calls! Fix: use items=None, then `items = items or []` inside.
- Unpacking with * and ** when CALLING a function spreads a list/dict into args.
"""

def log_call(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)


def buggy_append(x, items=[]):  # DANGEROUS - shared default!
    items.append(x)
    return items


def fixed_append(x, items=None):  # SAFE
    if items is None:
        items = []
    items.append(x)
    return items


def args_kwargs_demo():
    print("\n--- *ARGS, **KWARGS & UNPACKING ---")

    log_call(1, 2, 3, name="Alice", age=30)
    print(f"{'*' * 80}")

    # Mutable default argument bug
    print("buggy_append(1):", buggy_append(1))
    print("buggy_append(2):", buggy_append(2))  # [1, 2] NOT [2] - the bug!
    print(f"{'*' * 80}")

    print("fixed_append(1):", fixed_append(1))
    print("fixed_append(2):", fixed_append(2))  # correctly just [2]
    print(f"{'*' * 80}")

    # Unpacking when CALLING
    nums = [1, 2, 3]
    print("sum via unpacking:", sum(nums))

    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged = {**dict1, **dict2}  # unpack-merge two dicts
    print("Merged dicts:", merged)

    def keyword_only_example(a, *, b):
        """ '*' forces 'b' to be keyword-only - can't call as positional. """
        return a, b
    print("keyword-only call:", keyword_only_example(1, b=2))


if __name__ == "__main__":
    args_kwargs_demo()


# ==============================================================================
# ADDITIONAL NOTES FOR INTERVIEW PREPARATION
# ==============================================================================

# -------------------------
# 1. Full parameter ordering rules in a function definition
# -------------------------
# The ONLY valid order is:
#   def f(positional_only, /, positional_or_keyword, *args, keyword_only, **kwargs):
# Violating this order raises a SyntaxError at definition time.

def full_signature_demo(pos_only, /, normal, *args, kw_only, **kwargs):
    """
    pos_only  -> can ONLY be passed positionally (before the '/')
    normal    -> can be passed positionally OR by keyword
    *args     -> extra positional args, collected as a tuple
    kw_only   -> must be passed by keyword (after *args or bare '*')
    **kwargs  -> extra keyword args, collected as a dict
    """
    return pos_only, normal, args, kw_only, kwargs


print(full_signature_demo(1, 2, 3, 4, kw_only=5, extra="x"))
# (1, 2, (3, 4), 5, {'extra': 'x'})

print(f"{'*' * 80}")

# -------------------------
# 2. Positional-only parameters using '/' (Python 3.8+)
# -------------------------
def divide(a, b, /):
    """Everything before '/' MUST be passed positionally - cannot use a= or b=."""
    return a / b

print(divide(10, 2))     # 5.0
# divide(a=10, b=2)      # TypeError: divide() got some positional-only arguments
                          # passed as keyword arguments

# Why it exists: lets library authors rename parameters later without breaking
# callers (e.g. len(obj) - you can't call len(obj=x)).

print(f"{'*' * 80}")

# -------------------------
# 3. Keyword-only parameters using bare '*' (Python 3+, already partly shown above)
# -------------------------
def create_user(name, *, is_admin=False):
    """Bare '*' with no name - everything after it MUST be passed as keyword."""
    return {"name": name, "is_admin": is_admin}

print(create_user("Bob", is_admin=True))
# create_user("Bob", True)   # TypeError - is_admin can't be positional

# Why it's useful: prevents confusing calls like create_user("Bob", True)
# where the meaning of `True` isn't obvious at the call site.

print(f"{'*' * 80}")

# -------------------------
# 4. Unpacking with * and ** when CALLING (spreading), shown with more depth
# -------------------------
def add3(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add3(*nums))          # 6  -> list unpacked into 3 positional args

nums_dict = {"a": 1, "b": 2, "c": 3}
print(add3(**nums_dict))    # 6  -> dict unpacked into keyword args (keys must match param names)

# combining both in one call
def combo(a, b, *args, **kwargs):
    return a, b, args, kwargs

print(combo(*[1, 2, 3, 4], **{"x": 10}))
# (1, 2, (3, 4), {'x': 10})

print(f"{'*' * 80}")

# -------------------------
# 5. Extended iterable unpacking with * in assignments (NOT function-related,
#    but commonly asked alongside *args since it uses the same '*' syntax)
# -------------------------
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)   # 1 [2, 3, 4] 5

a, *rest = (10, 20, 30)
print(a, rest)                # 10 [20, 30]

*head, tail = "abcd"
print(head, tail)             # ['a', 'b', 'c'] 'd'

print(f"{'*' * 80}")

# -------------------------
# 6. Forwarding *args/**kwargs to another function - VERY common in real code
#    (decorators, subclassing, wrapper functions)
# -------------------------
def wrapper(*args, **kwargs):
    print("Before calling wrapped function")
    result = wrapped(*args, **kwargs)   # forward everything through unchanged
    print("After calling wrapped function")
    return result

def wrapped(x, y, z=0):
    return x + y + z

print(wrapper(1, 2, z=3))    # 6

# Same pattern shows up in class inheritance:
class Base:
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)

class Child(Base):
    def __init__(self, name, age, **kwargs):
        super().__init__(name, **kwargs)   # forward remaining kwargs up the chain
        self.age = age

print(f"{'*' * 80}")

# -------------------------
# 7. *args and **kwargs are just conventional NAMES, not keywords
# -------------------------
# The '*' and '**' are what matter; you could name them anything.
def flexible(*values, **options):
    print(values, options)

flexible(1, 2, key="val")   # (1, 2) {'key': 'val'}

print(f"{'*' * 80}")

# -------------------------
# 8. Real-world use case: decorators that work on ANY function signature
# -------------------------
import functools
import time

def timer(func):
    @functools.wraps(func)   # preserves func.__name__, __doc__, etc.
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f}s")
        return result
    return inner

@timer
def slow_add(a, b):
    return a + b

print(slow_add(2, 3))
print(slow_add.__name__)   # 'slow_add' -> preserved thanks to functools.wraps

print(f"{'*' * 80}")

# -------------------------
# 9. Other mutable default argument traps (not just lists)
# -------------------------
def buggy_dict_default(key, value, cache={}):   # DANGEROUS - same trap with dict
    cache[key] = value
    return cache

print(buggy_dict_default("a", 1))   # {'a': 1}
print(buggy_dict_default("b", 2))   # {'a': 1, 'b': 2}  -> leaked from previous call!

# Rule of thumb: NEVER use a mutable object (list, dict, set, or a custom mutable
# class instance) as a default argument value.

print(f"{'*' * 80}")

# -------------------------
# 10. TypeErrors you should recognize instantly (common interview trick questions)
# -------------------------
# def f(a, b): pass
# f(1, 2, 3)          # TypeError: f() takes 2 positional arguments but 3 were given
# f(a=1)              # TypeError: f() missing 1 required positional argument: 'b'
# f(1, a=2)           # TypeError: f() got multiple values for argument 'a'

# def g(*, a): pass
# g(1)                 # TypeError: g() takes 0 positional arguments but 1 was given

print(f"{'*' * 80}")

# -------------------------
# 11. Argument count/order sanity check with **kwargs and duplicate keys
# -------------------------
def show(**kwargs):
    print(kwargs)

d1 = {"a": 1}
d2 = {"a": 2}          # duplicate key 'a'
merged = {**d1, **d2}  # later dict's value WINS on key collision
print(merged)           # {'a': 2}
# show(**d1, **d2)      # works fine for merging, but show(a=1, **{"a": 2})
                         # would raise: TypeError: got multiple values for keyword argument 'a'

print(f"{'*' * 80}")

# -------------------------
# 12. Empty *args / **kwargs still work fine (no error if nothing extra is passed)
# -------------------------
log_call()   # Positional args: ()   Keyword args: {}


# ==============================================================================
# INTERVIEW QUESTIONS ON *ARGS, **KWARGS & UNPACKING
# ==============================================================================

# 1. What is the difference between *args and **kwargs? What data structures do they
#    collect their values into?
#
# 2. What is the correct order of parameters in a function definition when mixing
#    positional, default, *args, keyword-only, and **kwargs? What happens if you
#    get the order wrong?
#
# 3. Why is using a mutable object (like a list or dict) as a default argument value
#    considered dangerous? Walk through exactly when the default value gets created.
#
# 4. What is the fix for the mutable default argument problem, and why does that
#    fix work (i.e., why is `None` safe as a default)?
#
# 5. What do positional-only parameters (using '/') mean, and why would an API
#    designer want to use them?
#
# 6. What does a bare '*' (with no name) do in a function signature? How is it
#    different from *args?
#
# 7. How would you forward all arguments received by a wrapper function to another
#    function unchanged? Why is this pattern common in decorators?
#
# 8. What does functools.wraps do, and why is it important when writing decorators
#    that use *args, **kwargs?
#
# 9. If you unpack two dictionaries with overlapping keys into a single dict literal
#    (e.g., {**d1, **d2}), which value wins for a duplicate key?
#
# 10. What error do you get if you pass a keyword argument that collides with a
#     positional argument already provided (e.g., f(1, a=2) where 'a' is the first
#     parameter)?
#
# 11. Can you unpack a generator or other iterable (not just a list) using *? What
#     about unpacking a non-dict mapping using **?
#
# 12. What is extended iterable unpacking (e.g., `first, *rest = some_list`)? How
#     is this related to, or different from, *args in function definitions?
#
# 13. Is it mandatory to name your variadic parameters "args" and "kwargs"? What
#     actually makes them behave this way syntactically?
#
# 14. How would you write a function that accepts any number of positional
#     arguments but requires at least one? (Hint: think about signature design,
#     e.g. def f(first, *rest).)
#
# 15. What happens if you call a function with more positional arguments than it
#     defines and it has no *args to catch them?
#
# 16. In class inheritance, why do we often see `super().__init__(*args, **kwargs)`
#     in a subclass's __init__? What problem does this solve?
#
# 17. Can *args and **kwargs be empty when a function is called with no extra
#     arguments? What values do they hold in that case?
#
# 18. How would you dynamically call a function with arguments stored in a list
#     and a dict that were built at runtime (not known when writing the code)?
#
# 19. What's the difference between *args in a function DEFINITION versus * used
#     when CALLING a function? (i.e., "collecting" vs "unpacking")
#
# 20. Why might overusing **kwargs in a public API's function signatures be
#     considered bad practice from a readability/maintainability standpoint?

# ==============================================================================
# ANSWERS TO INTERVIEW QUESTIONS
# ==============================================================================

# A1. *args vs **kwargs
#     *args   -> collects extra POSITIONAL arguments into a TUPLE.
#     **kwargs -> collects extra KEYWORD arguments into a DICT (name -> value).
#     def f(*args, **kwargs): ...
#     f(1, 2, a=3)  ->  args = (1, 2), kwargs = {'a': 3}

# A2. Correct parameter order
#     def f(pos_only, /, normal, default=val, *args, kw_only, **kwargs)
#     Order: positional-only -> '/' -> positional-or-keyword (defaults after
#     non-defaults) -> *args (or bare '*') -> keyword-only -> **kwargs.
#     Wrong order (e.g. **kwargs before *args, or a non-default parameter after
#     a default one in the positional section) -> SyntaxError at DEFINITION time,
#     before any code runs.

# A3. Why mutable defaults are dangerous
#     Default values are evaluated ONCE, when the `def` statement executes (when
#     the function object is created), not on each call. The object is stored on
#     the function (see f.__defaults__) and reused for every call that omits the
#     argument. If it is a list/dict/set and the function mutates it, the changes
#     persist across calls:
#         def f(x, items=[]): items.append(x); return items
#         f(1) -> [1];  f(2) -> [1, 2]   # same list object each time
#     Proof: buggy_append.__defaults__ shows the accumulated list.

# A4. The fix, and why None is safe
#     def f(x, items=None):
#         if items is None:
#             items = []
#     The `[]` inside the body runs on EVERY call, so each call gets a fresh list.
#     None is safe because it is an immutable singleton - nobody can mutate it,
#     so sharing it across calls is harmless.
#     Prefer `if items is None` over `items = items or []`: the `or` version also
#     replaces a falsy value the caller passed on purpose (e.g. their own empty
#     list, which they may expect to be appended to), silently breaking that.

# A5. Positional-only parameters ('/')
#     Parameters before '/' can only be passed by position, never by name.
#         def divide(a, b, /): ...   ->  divide(10, 2) OK, divide(a=10, b=2) TypeError
#     Why designers use them:
#       - The parameter names are not part of the public API, so they can be
#         renamed later without breaking callers.
#       - Names are meaningless/obvious anyway (len(obj), divide(a, b)).
#       - Avoids clashes: a positional-only name can safely also appear as a
#         key in **kwargs.

# A6. Bare '*' in a signature
#     A bare '*' (no name) does NOT collect anything; it only marks that every
#     parameter after it is KEYWORD-ONLY.
#         def create_user(name, *, is_admin=False)
#         create_user("Bob", True)            # TypeError
#         create_user("Bob", is_admin=True)   # OK
#     Difference from *args: *args also marks the keyword-only boundary but
#     additionally captures extra positional arguments into a tuple. A bare '*'
#     captures nothing, so extra positional arguments raise TypeError.

# A7. Forwarding all arguments
#     def wrapper(*args, **kwargs):
#         return wrapped(*args, **kwargs)
#     Collect everything on the way in, spread it on the way out, so the arguments
#     reach the target unchanged. It is common in decorators because the decorator
#     doesn't know (or care) what signature the decorated function has - the same
#     wrapper works for ANY function, and it can add behaviour (timing, logging,
#     retries, auth checks) before/after the call.

# A8. functools.wraps
#     @functools.wraps(func) copies metadata from the original function onto the
#     wrapper: __name__, __doc__, __module__, __qualname__, __annotations__,
#     and sets __wrapped__ (so inspect.signature can see through the wrapper).
#     Without it, slow_add.__name__ would be 'inner' and the docstring would be
#     lost. That breaks debugging, logs, help(), introspection tools, and
#     frameworks that rely on function names (e.g. pytest fixtures/markers,
#     Flask route endpoints).

# A9. Duplicate keys in {**d1, **d2}
#     The LATER dictionary wins: {**{'a': 1}, **{'a': 2}} -> {'a': 2}.
#     Keys are processed left to right and later assignments overwrite earlier
#     ones. (Python 3.9+ has the same behaviour for d1 | d2.)

# A10. Keyword colliding with a positional argument
#      def f(a, b): ...
#      f(1, a=2)  ->  TypeError: f() got multiple values for argument 'a'
#      The first positional value 1 already filled 'a', and then a=2 tries to
#      fill it again.
#      Similarly, f(a=1, **{'a': 2}) -> TypeError: f() got multiple values for
#      keyword argument 'a'.

# A11. Unpacking generators / non-dict mappings
#      '*' works on ANY iterable (list, tuple, set, string, range, generator,
#      dict -> its keys, file object...). A generator is consumed in the process:
#          def gen(): yield 1; yield 2
#          print(*gen())        # 1 2
#      '**' requires a MAPPING (an object with keys() and __getitem__, not only
#      dict - e.g. collections.OrderedDict, ChainMap, MappingProxyType). Passing
#      a list of pairs fails: f(**[('a', 1)]) -> TypeError: argument after **
#      must be a mapping. Also, in a call the keys must be strings.

# A12. Extended iterable unpacking
#      first, *rest = [1, 2, 3, 4]   ->  first = 1, rest = [2, 3, 4]
#      The starred name soaks up "whatever is left" and is ALWAYS a list (even if
#      the source is a tuple or string). Only one starred target is allowed per
#      assignment. It is related to *args in that both use '*' to gather the
#      leftovers, but it is an ASSIGNMENT feature (Python 3.0+) - it has nothing
#      to do with function definitions, and *args gives a tuple while this gives
#      a list.

# A13. Must the names be "args" and "kwargs"?
#      No. They are only convention. The single '*' and double '**' prefixes are
#      what make a parameter variadic. def f(*values, **options) works
#      identically. Stick to args/kwargs anyway unless a more descriptive name
#      (e.g. *paths, **headers) genuinely improves readability.

# A14. At least one positional argument required
#      def f(first, *rest):
#          ...
#      `first` is a normal required parameter, so f() raises TypeError, while
#      f(1), f(1, 2, 3) all work. Better than checking len(args) manually: the
#      error is raised by Python itself and the signature documents the rule.

# A15. Too many positional arguments with no *args
#      Python raises TypeError at call time:
#          def f(a, b): ...
#          f(1, 2, 3)  ->  TypeError: f() takes 2 positional arguments but 3 were given
#      Likewise, unexpected keyword args with no **kwargs ->
#          TypeError: f() got an unexpected keyword argument 'x'

# A16. super().__init__(*args, **kwargs) in subclasses
#      The subclass often doesn't know (or want to care) which extra parameters
#      the parent - or other classes in a multiple-inheritance chain (the MRO) -
#      accept. Forwarding *args/**kwargs lets each class consume what it needs
#      and pass the rest up, which supports cooperative multiple inheritance and
#      means the child doesn't need updating when the parent gains a new
#      parameter.
#      Caveat: whatever remains at the top must be consumed. In the Base class
#      above, super().__init__(**kwargs) ends at object.__init__, which accepts
#      no extra arguments, so Child("x", 5, foo=1) would raise TypeError.

# A17. Empty *args / **kwargs
#      Yes. If nothing extra is passed, args == () (empty tuple) and
#      kwargs == {} (empty dict). No error. That is why log_call() prints
#      "Positional args: ()" and "Keyword args: {}".

# A18. Dynamically calling with runtime-built arguments
#      args = [1, 2]
#      kwargs = {"z": 3}
#      func(*args, **kwargs)
#      Works with any callable, and the list/dict can be built at runtime (from
#      config, JSON, test data, user input...). Typical use: data-driven tests,
#      dispatch tables, running a callback registered with its own arguments
#      (this is also what functools.partial does under the hood).

# A19. Collecting vs unpacking
#      In a DEFINITION, * / ** COLLECT: many separate arguments -> one tuple/dict.
#          def f(*args, **kwargs)     # gathers
#      In a CALL, * / ** UNPACK (spread): one container -> many separate
#      arguments.
#          f(*[1, 2, 3], **{"a": 1})  # spreads
#      Same symbols, opposite directions: pack on the way in, unpack on the way out.

# A20. Why overusing **kwargs in a public API is bad practice
#      - The real parameters are invisible: the signature, help(), IDE
#        autocomplete, and type checkers can't tell callers what is accepted.
#      - Typos are silently swallowed (e.g. timeuot=5 is accepted and ignored),
#        so bugs surface late or never.
#      - Documentation drifts, because valid options live only in the body or
#        in prose docs.
#      - It's harder to refactor and test, since the supported surface is
#        undefined, and defaults/validation have to be hand-written.
#      Prefer explicit named parameters (optionally keyword-only); keep **kwargs
#      for genuine pass-through cases (wrappers, decorators, forwarding to a
#      parent/other function) and document where they end up.