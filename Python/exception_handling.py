# ==============================================================================
# EXCEPTION HANDLING
# ==============================================================================
"""
NOTES:
- try/except/else/finally order: try -> except (if error) -> else (if NO error)
  -> finally (ALWAYS runs, even if return/break/continue happened above)
- Catch specific exceptions first, generic Exception last. Avoid bare 'except:'
  (it also catches KeyboardInterrupt, SystemExit).
- Custom exceptions: subclass Exception (or a more specific built-in exception).
- 'raise X from Y' chains exceptions, preserving the original traceback context
  (shows "The above exception was the direct cause of the following exception").
"""
class InsufficientFundsError(Exception):
    """Custom exception for bank withdrawal use-case."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}, balance is only {balance}")


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


def exception_handling_demo():
    print("\n--- 1. EXCEPTION HANDLING ---")

    # Basic try/except/else/finally
    try:
        result = 10 / 2
    except ZeroDivisionError as e:
        print("Error:", e)
    else:
        print("No error, result =", result)  # runs only if no exception
    finally:
        print("Finally always runs")

    # Multiple exceptions in one except
    try:
        int("abc")
    except (ValueError, TypeError) as e:
        print("Caught:", type(e).__name__, "-", e)

    # Custom exception in action
    try:
        withdraw(100, 500)
    except InsufficientFundsError as e:
        print("Custom exception caught:", e)

    # raise ... from ... (exception chaining)
    try:
        try:
            1 / 0
        except ZeroDivisionError as original:
            raise ValueError("Something went wrong upstream") from original
    except ValueError as e:
        print("Chained exception:", e, "| caused by:", e.__cause__)

    # finally still runs even with a return in try
    def weird_return():
        try:
            return "from try"
        finally:
            print("finally runs even though try returned")
    print(weird_return())


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. The built-in exception hierarchy - crucial for knowing WHAT to catch and in WHAT order
# -------------------------
"""
BaseException
 ├── SystemExit          -> raised by sys.exit()
 ├── KeyboardInterrupt    -> raised on Ctrl+C
 ├── GeneratorExit         -> raised when a generator is closed
 └── Exception              -> base for almost ALL user-facing exceptions
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── OverflowError
      ├── LookupError
      │    ├── IndexError      -> list index out of range
      │    └── KeyError         -> missing dict key
      ├── TypeError
      ├── ValueError
      ├── AttributeError
      ├── NameError
      ├── OSError (aka IOError)
      │    └── FileNotFoundError
      └── ... many more

NOTE: catch `Exception`, NOT `BaseException`, in almost all cases. Catching
BaseException (or a bare `except:`) also swallows SystemExit and
KeyboardInterrupt, which usually should be allowed to propagate (e.g. so
Ctrl+C actually stops your program).
"""
print(issubclass(ZeroDivisionError, ArithmeticError))   # True
print(issubclass(KeyError, LookupError))                  # True
print(issubclass(Exception, BaseException))                # True

print(f"{'*' * 70}")

# -------------------------
# 2. Order of except blocks MATTERS - most specific first, most general last
# -------------------------
def risky(x):
    try:
        return 10 / x
    except ZeroDivisionError:            # MOST specific first
        return "Cannot divide by zero"
    except ArithmeticError:                # broader (parent of ZeroDivisionError)
        return "Some arithmetic error"
    except Exception:                       # most general LAST - catch-all fallback
        return "Unknown error"

print(risky(0))    # Cannot divide by zero -> matches the FIRST matching except block

# GOTCHA: if you put a broader exception BEFORE a narrower one, the narrower
# block becomes UNREACHABLE (dead code) - Python matches top-to-bottom and
# stops at the first match.
def bad_order(x):
    try:
        return 10 / x
    except Exception:                 # this catches EVERYTHING first...
        return "generic"
    except ZeroDivisionError:           # ...so this is NEVER reached! (dead code)
        return "specific"

print(f"{'*' * 70}")

# -------------------------
# 3. else clause - purpose and why it's better than putting code in try
# -------------------------
# Code in 'else' runs ONLY if the try block succeeded with NO exception.
# Why not just put that code at the end of 'try'? Because then a bug in THAT
# code would be silently caught by the except block too, hiding real bugs.
try:
    x = 10 / 2          # only this risky operation is in try
except ZeroDivisionError:
    print("division failed")
else:
    print(f"Success, x = {x}")   # if this line itself had a bug, it would NOT
                                    # be mistakenly caught by the except above

print(f"{'*' * 70}")

# -------------------------
# 4. Bare 'raise' - re-raising the CURRENT exception without changing its traceback
# -------------------------
def log_and_reraise():
    try:
        1 / 0
    except ZeroDivisionError:
        print("Logging the error before re-raising...")
        raise    # bare 'raise' - re-raises the SAME exception with its ORIGINAL traceback intact

try:
    log_and_reraise()
except ZeroDivisionError as e:
    print("Caught re-raised exception:", e)

print(f"{'*' * 70}")

# -------------------------
# 5. raise ... from None - suppressing the exception chain entirely
# -------------------------
def validate(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Invalid input: {value}") from None   # hides the "During
        # handling of the above exception, another exception occurred" chain,
        # useful when the ORIGINAL low-level exception isn't useful to show

try:
    validate("abc")
except ValueError as e:
    print("Clean error (no chain shown):", e)

print(f"{'*' * 70}")

# -------------------------
# 6. Custom exception HIERARCHIES - grouping related errors (senior-level design)
# -------------------------
class ApplicationError(Exception):
    """Base exception for all custom errors in this application."""
    pass

class ValidationError(ApplicationError):
    """Raised when input validation fails."""
    pass

class DatabaseError(ApplicationError):
    """Raised when a database operation fails."""
    pass

def process(value):
    if value < 0:
        raise ValidationError("Value cannot be negative")
    # simulate more logic...

try:
    process(-5)
except ApplicationError as e:                   # catches ValidationError, DatabaseError, or ANY
    print(f"App error caught: {type(e).__name__}: {e}")   # future subclass of ApplicationError

# This pattern lets calling code catch `ApplicationError` broadly, OR catch
# `ValidationError` specifically, depending on how granular it needs to be.

print(f"{'*' * 70}")

# -------------------------
# 7. Context managers (with statement) vs try/finally for resource cleanup
# -------------------------
# 'with' is generally PREFERRED over manual try/finally for resource
# management (files, locks, connections) because it's shorter and less
# error-prone.
class ManagedResource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Releasing resource")
        if exc_type is not None:
            print(f"Handled exception: {exc_type.__name__}: {exc_value}")
        return True   # returning True SUPPRESSES the exception (it won't propagate further)

with ManagedResource() as r:
    print("Using resource")
    raise ValueError("Something broke inside the with block")
print("Program continues normally - exception was suppressed by __exit__")

# Equivalent manual version using try/finally (more verbose, more error-prone):
resource = None
try:
    print("Acquiring resource (manual)")
    resource = "some_resource"
    # ... use resource ...
finally:
    print("Releasing resource (manual)")

print(f"{'*' * 70}")

# -------------------------
# 8. assert statement - for debugging/invariants, NOT for input validation
# -------------------------
def calculate_discount(price, discount_percent):
    assert 0 <= discount_percent <= 100, "Discount must be between 0 and 100"
    return price * (1 - discount_percent / 100)

print(calculate_discount(100, 20))   # 80.0
try:
    calculate_discount(100, 150)
except AssertionError as e:
    print("AssertionError:", e)

# IMPORTANT: assert statements are STRIPPED OUT when Python runs with the -O
# (optimize) flag! Never use assert for security checks or real input
# validation in production code - use explicit if/raise instead for anything
# that MUST always be checked.

print(f"{'*' * 70}")

# -------------------------
# 9. Common gotcha: the exception variable is deleted after the except block ends
# -------------------------
try:
    raise ValueError("test")
except ValueError as e:
    print("Inside except:", e)
# print(e)   # NameError: name 'e' is not defined -> Python auto-deletes 'e'
              # at the end of the except block (to avoid keeping tracebacks
              # alive via a lingering reference, which can cause memory leaks)

print(f"{'*' * 70}")

# -------------------------
# 10. Exception groups - handling MULTIPLE unrelated exceptions at once (Python 3.11+)
# -------------------------
try:
    raise ExceptionGroup("multiple failures", [
        ValueError("bad value"),
        TypeError("bad type"),
    ])
except* ValueError as eg:
    print("Caught ValueErrors:", eg.exceptions)
except* TypeError as eg:
    print("Caught TypeErrors:", eg.exceptions)

# ExceptionGroup + 'except*' is useful for concurrent code (e.g., asyncio
# TaskGroups) where MULTIPLE tasks can fail independently and you want to
# handle all their errors together, rather than only seeing the first one.

print(f"{'*' * 70}")

# -------------------------
# 11. EAFP vs LBYL - a core Python design philosophy interview topic
# -------------------------
# EAFP = "Easier to Ask Forgiveness than Permission" - try the operation,
# catch the exception if it fails. This is the more PYTHONIC style.
d = {"a": 1}
# EAFP style:
try:
    value = d["b"]
except KeyError:
    value = None
print(value)   # None

# LBYL = "Look Before You Leap" - check conditions first, then act.
# LBYL style:
if "b" in d:
    value = d["b"]
else:
    value = None
print(value)   # None

# EAFP is generally preferred in Python because:
#   1. It avoids a race condition between the check and the action (e.g., a
#      file could be deleted between checking os.path.exists() and opening it)
#   2. It's often faster in the common/success case, since no upfront check
#      is needed - the cost of exceptions is mainly paid on the FAILURE path

print(f"{'*' * 70}")

# -------------------------
# 12. Multiple exception types with 'as' - accessing attributes across types
# -------------------------
def parse_number(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print(f"Failed to parse '{s}': {type(e).__name__}: {e}")
        return None

print(parse_number("abc"))    # ValueError
print(parse_number(None))      # TypeError
print(parse_number("42"))       # 42 -> success, no exception


## ==========================================================
## INTERVIEW QUESTIONS ON EXCEPTION HANDLING
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is the exact execution order of try/except/else/finally? Under what
#    circumstances does 'finally' NOT run (hint: think os._exit() or a killed
#    process)?
#
# 2. Why is a bare `except:` considered bad practice? What exceptions does it
#    catch that `except Exception:` would NOT catch?
#
# 3. Why does the order of multiple except blocks matter? What happens if you
#    put a broader exception class before a more specific one?
#
# 4. What is the purpose of the `else` clause in a try statement? Why not just
#    put that code inside the `try` block directly?
#
# 5. What is the difference between `raise` (bare) and `raise SomeException()`
#    inside an except block? What does bare `raise` preserve that creating a
#    new exception does not?
#
# 6. What does `raise NewException(...) from original_exception` do? How is
#    this different from `raise NewException(...) from None`?
#
# 7. How would you design a custom exception hierarchy for an application with
#    several different error categories (e.g., validation errors, database
#    errors, network errors)? What's the benefit of having a common base
#    exception class?
#
# 8. What is the difference between using a `with` statement (context
#    manager) versus a manual `try/finally` block for resource cleanup? What
#    methods must a class implement to work with `with`?
#
# 9. In a context manager's `__exit__` method, what does returning `True`
#    versus `False`/`None` do to an exception that occurred inside the `with`
#    block?
#
# 10. Why should `assert` statements not be used for input validation in
#     production code? What happens to assert statements when Python runs
#     with the `-O` flag?
#
# 11. Why does trying to access the exception variable from an `except X as e`
#     block AFTER the block has ended raise a NameError? What does Python do
#     to that variable automatically?
#
# 12. What are Exception Groups and the `except*` syntax (Python 3.11+)? What
#     problem do they solve that regular try/except couldn't handle before?
#
# 13. What is EAFP ("Easier to Ask Forgiveness than Permission") versus LBYL
#     ("Look Before You Leap")? Which style is more idiomatic in Python, and
#     why?
#
# 14. Give an example where LBYL-style code (checking a condition before
#     acting) could introduce a race condition, while EAFP-style code (try/
#     except) would not.
#
# 15. What is the difference between catching `LookupError` versus catching
#     `KeyError` and `IndexError` separately? When would you want the broader
#     catch?
#
# 16. How would you catch multiple different exception types in a single
#     except block, and still access which specific exception type was
#     raised?
#
# 17. What happens if an exception is raised INSIDE a `finally` block while
#     another exception is already propagating from the `try` block? Which
#     exception "wins" and gets raised to the caller?
#
# 18. Is it possible for a `return` statement inside a `finally` block to
#     silently swallow an exception or override a `return` value from the
#     `try` block? What would you warn a teammate about here?
#
# 19. What's the performance cost of using exceptions for control flow in a
#     hot loop, compared to checking a condition upfront? Does this change
#     your view on EAFP for performance-critical code?
#
# 20. How would you log a full exception traceback (not just the exception
#     message) when catching an exception, for debugging purposes in
#     production code?


# ==============================================================================
# MAIN
# ==============================================================================
"""
if __name__ == "__main__": controls whether a block of code runs only when the file is 
    executed directly, versus when it's imported as a module into another file.
"""
if __name__ == "__main__":
    exception_handling_demo()