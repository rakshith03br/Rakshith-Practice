'''
Levels of logging
DEBUG: This level gives detailed information, useful only when a problem is being diagnosed.
INFO: This is used to confirm that everything is working as expected.
WARNING: This level indicates that something unexpected has happened or it may happen.
ERROR: As it implies, an error has occurred. The software was unable to perform some function.
CRITICAL: A serious error has occurred. The program itself may shut down or not be able to continue running properly.
'''

import logging
log = logging.getLogger()

'''
# logging.basicConfig(level=logging.DEBUG) # setting the level of the log
# logging.basicConfig(filename='test.log', level=logging.DEBUG) # saving the log file to 'test.log'
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s') # saving the log file to 'test.log'


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


x = 30
y = 5

add_res = add(x, y)
logging.debug(f'Add {x} + {y} is: {add_res}')
sub_res = sub(x, y)
logging.debug(f'sub {x} - {y} is: {sub_res}')
mul_res = mul(x, y)
logging.debug(f'mul {x} * {y} is: {mul_res}')
div_res = div(x, y)
logging.debug(f'div {x} / {y} is: {div_res}')

'''

logging.basicConfig(filename='employee.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        log.info(f'Created Employee: {self.fullname}:{self.email}')
        # print(f'Created Employee: {self.fullname}{self.email}')

    @property
    def email(self):
        return f' {self.first}{self.last}@gmail.com'

    @property
    def fullname(self):
        return f'{self.first}{self.last}'


emp1 = Employee('Rakshith','B R')
n = emp1.fullname
log.info(f'Employee: {n}')
# logging.info(f'Created Employee: {emp1.fullname}{emp1.email}')


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. Logging levels have NUMERIC values under the hood - this determines what
#    gets shown when you set a level via basicConfig(level=...)
# -------------------------
print(logging.DEBUG)      # 10
print(logging.INFO)        # 20
print(logging.WARNING)      # 30
print(logging.ERROR)         # 40
print(logging.CRITICAL)       # 50

# Setting level=logging.INFO means: show INFO and ANYTHING with a HIGHER
# numeric value (WARNING, ERROR, CRITICAL) - but NOT DEBUG (which is lower).
# This is why your DEBUG-level logs are silent when the logger is set to INFO.

print(f"{'*' * 60}")

# -------------------------
# 2. print() vs logging - why professional code uses logging (very common
#    "why would you use X over Y" interview question)
# -------------------------
"""
print()                              logging
--------------------------------     --------------------------------------
Always goes to stdout only            Can go to console, file, network, etc.
No severity levels                      Has DEBUG/INFO/WARNING/ERROR/CRITICAL
No timestamps/context by default         Can auto-include timestamp, module, line number
Hard to disable across a whole app        Can globally raise/lower verbosity with one setting
No filtering                               Supports filters and per-module control
Not thread-safe by default in complex apps  Designed with thread-safety in mind
"""

print(f"{'*' * 60}")

# -------------------------
# 3. Root logger vs named loggers - logging.getLogger(__name__) is the
#    STANDARD/RECOMMENDED pattern (your file uses the bare root logger)
# -------------------------
# logging.getLogger() with NO argument -> returns the ROOT logger (what your
# file's `log = logging.getLogger()` does).
# logging.getLogger(__name__) -> returns a NAMED logger, using the module's
# own name (e.g. 'my_module') - this is the standard best practice because:
#   1. Log messages show WHICH module produced them
#   2. You can configure verbosity PER MODULE independently
#   3. It avoids libraries you import polluting/hijacking your root logger config
named_logger = logging.getLogger(__name__)
print(named_logger.name)   # '__main__' when run as a script directly

print(f"{'*' * 60}")

# -------------------------
# 4. Logger hierarchy and propagation - dotted names create parent-child relationships
# -------------------------
# A logger named "myapp.database" is a CHILD of "myapp", which is a child of
# the ROOT logger. By default, a log record propagates UP through all parent
# loggers' handlers too (unless propagate=False is set).
child_logger = logging.getLogger("myapp.database")
print(child_logger.parent.name if child_logger.parent else "no parent")   # 'myapp' (or 'root' if 'myapp' doesn't exist yet)

# child_logger.propagate = False   # would stop messages from also being
                                     # handled by ancestor loggers' handlers

print(f"{'*' * 60}")

# -------------------------
# 5. Handlers - WHERE the logs actually go (basicConfig only sets up ONE
#    handler; real apps often need multiple simultaneously)
# -------------------------
demo_logger = logging.getLogger("demo_logger")
demo_logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()             # sends logs to the console (stdout/stderr)
console_handler.setLevel(logging.WARNING)               # this handler only shows WARNING and above

file_handler = logging.FileHandler("demo_output.log")     # sends logs to a file
file_handler.setLevel(logging.DEBUG)                        # this handler shows EVERYTHING

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

demo_logger.addHandler(console_handler)
demo_logger.addHandler(file_handler)

demo_logger.debug("This only goes to the file (below console_handler's WARNING threshold)")
demo_logger.warning("This goes to BOTH console and file")
# Each handler can have its OWN level and formatter - very flexible for
# "show me warnings+ on screen, but log EVERYTHING to a file" setups.

print(f"{'*' * 60}")

# -------------------------
# 6. Logging exceptions properly - logging.exception() and exc_info=True
# -------------------------
def risky_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        log.exception("Division failed!")   # automatically includes the FULL traceback,
                                               # logged at ERROR level - very useful for debugging!
        return None

risky_divide(10, 0)
# log.exception(...) is shorthand for log.error(..., exc_info=True) - ALWAYS
# use one of these (not just log.error("Division failed")) when logging
# inside an except block, so you don't lose the traceback.

print(f"{'*' * 60}")

# -------------------------
# 7. Lazy (deferred) argument formatting - a subtle but real performance point
# -------------------------
user_id = 42
# PREFERRED in logging calls - the string formatting is DEFERRED and only
# happens if the log record actually gets emitted (i.e., passes the level check):
log.debug("User ID is %s", user_id)

# LESS preferred - the f-string is evaluated IMMEDIATELY, even if DEBUG logs
# are disabled and this message would be thrown away anyway:
log.debug(f"User ID is {user_id}")

# The difference matters mainly when the formatted value is EXPENSIVE to
# compute (e.g., serializing a large object) and DEBUG logging is usually off
# in production - the %-style avoids paying that cost needlessly.

print(f"{'*' * 60}")

# -------------------------
# 8. RotatingFileHandler / TimedRotatingFileHandler - preventing log files
#    from growing forever (a real production concern)
# -------------------------
from logging.handlers import RotatingFileHandler

rotating_handler = RotatingFileHandler(
    "app.log", maxBytes=1_000_000, backupCount=3   # rotates when file hits 1MB, keeps 3 old backups
)
# Once app.log hits maxBytes, it's renamed app.log.1, app.log.2, etc., and a
# fresh app.log is started - prevents disk space from growing unbounded.

print(f"{'*' * 60}")

# -------------------------
# 9. NullHandler - the recommended pattern for LIBRARY code (not application code)
# -------------------------
# If you're writing a REUSABLE LIBRARY (not a standalone script/app), you
# should NOT call basicConfig() or add real handlers yourself - that would
# force your logging configuration onto whoever imports your library!
library_logger = logging.getLogger("my_library")
library_logger.addHandler(logging.NullHandler())   # does nothing by default,
                                                       # but silences the "No handlers
                                                       # could be found" warning until
                                                       # the APPLICATION using the library
                                                       # configures its own handlers

print(f"{'*' * 60}")

# -------------------------
# 10. Common gotcha: calling basicConfig() more than once has NO EFFECT
# -------------------------
# basicConfig() only configures the root logger THE FIRST TIME it's called
# (unless you pass force=True). Calling it again later with different
# arguments silently does nothing if handlers already exist on the root logger.
logging.basicConfig(level=logging.WARNING)   # if root logger already has handlers,
                                                # from an earlier basicConfig() call,
                                                # this line has NO EFFECT
logging.basicConfig(level=logging.WARNING, force=True)   # force=True actually
                                                             # REMOVES existing handlers
                                                             # and reconfigures from scratch

print(f"{'*' * 60}")

# -------------------------
# 11. dictConfig - configuring logging declaratively (common in real
#     production apps/frameworks like Django, Flask)
# -------------------------
from logging.config import dictConfig

logging_config = {
    "version": 1,
    "formatters": {
        "simple": {"format": "%(levelname)s:%(name)s:%(message)s"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple", "level": "INFO"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}
# dictConfig(logging_config)   # would apply this entire config in one call -
                                  # much easier to manage/version-control than
                                  # many individual addHandler()/setFormatter() calls


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON LOGGING
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What are the five standard logging levels in Python, from least to most
#    severe? What numeric value does each correspond to?
#
# 2. Why would you use the logging module instead of print() statements in a
#    production application?
#
# 3. What is the difference between logging.getLogger() (no arguments) and
#    logging.getLogger(__name__)? Why is the latter considered best practice?
#
# 4. What is the logger hierarchy in Python's logging module? How does
#    "propagation" work between a child logger (e.g., "myapp.database") and
#    its parent ("myapp")?
#
# 5. What is the difference between a Logger, a Handler, and a Formatter in
#    the logging module? What role does each play?
#
# 6. Can a single logger have multiple handlers with DIFFERENT levels
#    attached to it? Give a practical scenario where this would be useful.
#
# 7. What does logging.exception() do differently from logging.error()? Why
#    is it important to use inside an except block?
#
# 8. What is "lazy" argument formatting in logging (e.g.,
#    `log.debug("value: %s", x)` vs `log.debug(f"value: {x}")`), and why does
#    it matter for performance?
#
# 9. What does basicConfig() do if the root logger already has handlers
#    configured? How would you force it to reconfigure anyway?
#
# 10. What is a RotatingFileHandler, and what real-world problem does it
#     solve for long-running applications?
#
# 11. Why should library code use a NullHandler instead of configuring real
#     handlers or calling basicConfig() itself?
#
# 12. What is the purpose of the format string tokens like %(asctime)s,
#     %(levelname)s, and %(message)s in a Formatter? How would you add the
#     module name or line number to a log format?
#
# 13. If you set a logger's level to WARNING, will DEBUG and INFO messages
#     sent to it be processed at all? What determines whether a log record is
#     actually emitted?
#
# 14. What is the difference between setting the LEVEL on a Logger versus
#     setting it on a Handler attached to that logger? Can they differ, and
#     what happens if they do?
#
# 15. How would you configure logging to write DEBUG-level (and above)
#     messages to a file, but only show WARNING-level (and above) messages on
#     the console, at the same time?
#
# 16. What is dictConfig(), and why might a larger application prefer it over
#     many individual addHandler()/setLevel() calls scattered through the
#     code?
#
# 17. What happens to a log record after it's created if propagate=False is
#     set on the logger that created it?
#
# 18. Why is it considered bad practice to configure logging (e.g., call
#     basicConfig()) inside a library that other people will import?
#
# 19. What information does log.exception() automatically capture that a
#     plain log.error("message") would NOT capture?
#
# 20. How would you rotate log files based on TIME (e.g., a new file every
#     midnight) instead of based on file SIZE? What class would you use
#     instead of RotatingFileHandler?