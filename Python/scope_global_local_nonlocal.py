# ==============================================================================
#  SCOPE: GLOBAL, LOCAL, NONLOCAL (LEGB)
# ==============================================================================
"""
- Python Scopes: local, global, nonlocal
    Python looks up variable names using the LEGB rule (Local → Enclosing → Global → Built-in).
    The keywords global and nonlocal let you override where an assignment goes.
Local scope:
    Any variable assigned inside a function is local by default — it exists only while that function
     runs, and it doesn't affect anything outside it.
global:
    Use global inside a function to tell Python "don't create a local variable — reassign the one in
    the module's global scope."
nonlocal:
    Used in nested functions. It tells Python "don't create a local variable here, and don't go all
    the way to global either — look in the nearest enclosing (non-global) function's scope."

"""
# Local scope
x = 10
def foo():
    x = 5   # this creates a NEW local x, separate from the global one
    print(x)  # 5
foo()
print(x)  # 10, unchanged

# --------------------------------------------------------------------------------------------
# global scope
x = 10
def foo():
    global x
    x = 5
    print(x)    # 5
foo()
print(x)  # 5, the global was actually changed
# --------------------------------------------------------------------------------------------
# nonlocal scope
print("nonlocal")
x = 20
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 5        # modifies outer's x
        print(x)     # 5
    inner()
    print(x)  # 5
outer()
print(x) # 20
# --------------------------------------------------------------------------------------------
# A classic use of nonlocal is building a stateful closure, like a counter:
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
# --------------------------------------------------------------------------------------------
counter_global = 0
def increment_global():
    global counter_global
    counter_global += 1


def make_counter():
    """Closure-based counter using nonlocal."""
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment


def legb_demo():
    print("\n--- SCOPE: GLOBAL, LOCAL, NONLOCAL (LEGB) ---")

    increment_global()
    increment_global()
    print("counter_global after 2 increments:", counter_global)

    counter = make_counter()
    print("closure counter calls:", counter(), counter(), counter())

    # LEGB demonstration
    x = "global x"
    def outer():
        x = "enclosing x"
        def inner():
            x = "local x"
            print("inner sees:", x)  # Local: "local x"
        inner()
        print("outer sees:", x)  # Enclosing: "enclosing x"
    outer()
    print("module level sees:", x)  # Global: "global x"


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. The classic UnboundLocalError gotcha - assignment ANYWHERE in a function
#    makes that name LOCAL for the ENTIRE function body (Python decides this
#    at COMPILE time, by scanning the function for assignments, before it
#    ever runs)
# -------------------------
y = 100
def broken():
    print(y)     # you might expect this to print the global y = 100...
    y = 5          # ...but because 'y' is assigned SOMEWHERE in this function,
                     # Python treats 'y' as LOCAL for the WHOLE function body,
                     # so the print() above actually fails!
try:
    broken()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)   # local variable 'y' referenced before assignment

# Fix: either don't assign to 'y' locally, OR declare 'global y' explicitly
# if you intend to reassign the module-level variable.

print(f"{'*' * 70}")

# -------------------------
# 2. Reading vs writing a global - reading needs NO keyword, only reassignment does
# -------------------------
z = 50
def read_only():
    print(z)   # perfectly fine - READING a global needs no 'global' declaration at all
read_only()      # 50

def mutate_global_object():
    # if z were a LIST instead of an int, you could MUTATE it without 'global':
    pass

shared_list = [1, 2, 3]
def append_without_global():
    shared_list.append(4)   # no 'global' needed! we're MUTATING, not REBINDING the name
append_without_global()
print(shared_list)             # [1, 2, 3, 4] -> worked without declaring 'global shared_list'

def reassign_needs_global():
    global shared_list
    shared_list = ["completely", "new", "list"]   # REBINDING needs 'global'
reassign_needs_global()
print(shared_list)   # ['completely', 'new', 'list']

# KEY DISTINCTION: 'global'/'nonlocal' are only needed when REBINDING
# (assigning a new object to) a name - NOT when merely reading it or
# mutating an existing mutable object it points to.

print(f"{'*' * 70}")

# -------------------------
# 3. nonlocal has NO effect on the global scope - it specifically skips global
#    and only searches ENCLOSING function scopes
# -------------------------
g = "I am global"
def outer_no_enclosing():
    def inner():
        # nonlocal g   # SyntaxError! there's no ENCLOSING function-scope 'g' to bind to -
        #                 nonlocal explicitly does NOT fall back to the global scope, even
        #                 though a module-level 'g' exists. This line is commented out because
        #                 it's a SyntaxError caught at COMPILE time (before the function even runs),
        #                 so it can't be wrapped in a try/except like a normal runtime error.
        pass
    inner()

# nonlocal ALWAYS requires an enclosing (non-global) scope with that variable
# already assigned - if there isn't one, Python raises a SyntaxError immediately.

print(f"{'*' * 70}")

# -------------------------
# 4. The LEGB rule spelled out explicitly with the BUILT-IN scope included
#    (your demo covers Local/Enclosing/Global well - Built-in is the missing piece)
# -------------------------
# LEGB = Local -> Enclosing -> Global -> Built-in
# 'Built-in' scope holds names like len, print, sum, str, list, etc. - always
# available UNLESS you've shadowed them at a closer scope.
print(len([1, 2, 3]))   # 3 -> 'len' is found in the BUILT-IN scope (nothing closer defines it)

def shadow_builtin_demo():
    len = "oops, I shadowed the built-in function!"   # creates a LOCAL 'len', shadowing the built-in
    print(len)          # prints the STRING, not the function - 'len' here refers to the local variable
    # print(len([1,2,3]))   # would raise TypeError: 'str' object is not callable

shadow_builtin_demo()
print(len([1, 2, 3]))   # 3 -> outside the function, the built-in 'len' is unaffected

print(f"{'*' * 70}")

# -------------------------
# 5. Comprehensions have their OWN scope in Python 3 (a common surprise
#    for people coming from Python 2, and a real interview gotcha)
# -------------------------
i = "outer i"
squares = [i**2 for i in range(5)]   # the 'i' inside the comprehension is LOCAL to the comprehension
print(squares)                          # [0, 1, 4, 9, 16]
print(i)                                  # 'outer i' -> UNCHANGED! comprehension's 'i' did NOT leak out
                                             # (this is DIFFERENT from a regular for-loop, which DOES leak its variable)

j = "outer j"
for j in range(3):
    pass
print(j)   # 2 -> a regular for-loop's variable DOES leak into the enclosing scope, unlike a comprehension!

print(f"{'*' * 70}")

# -------------------------
# 6. Class body scope - a special, often-overlooked scope quirk
# -------------------------
# Class bodies have their OWN local-like scope during class DEFINITION, but
# methods defined inside the class do NOT automatically see class-level
# names the way nested functions see enclosing function variables!
class Example:
    class_var = "I'm a class attribute"

    def method(self):
        # print(class_var)     # NameError! methods do NOT implicitly see
                                   # the class body's namespace as an enclosing scope
        print(self.class_var)    # CORRECT way - must go through self/ClassName
        print(Example.class_var)   # also correct

Example().method()

print(f"{'*' * 70}")

# -------------------------
# 7. Multiple levels of nesting - nonlocal searches the NEAREST enclosing
#    scope that has the variable, skipping levels that don't
# -------------------------
def level1():
    val = "level1 value"
    def level2():
        # no 'val' defined at level2 - nonlocal will search UP through level2's
        # enclosing scopes until it finds one that HAS 'val'
        def level3():
            nonlocal val   # found in level1 (skips level2, since level2 never assigns 'val')
            val = "modified by level3"
        level3()
        print("level2 sees:", val)   # 'modified by level3'
    level2()
    print("level1 sees:", val)         # 'modified by level3' -> level1's own 'val' was changed

level1()

print(f"{'*' * 70}")

# -------------------------
# 8. globals() and locals() - inspecting scope dictionaries directly
# -------------------------
sample_global = "hello"
print('sample_global' in globals())   # True -> globals() returns a dict of the module's global namespace

def check_locals():
    local_var = 42
    print(locals())   # {'local_var': 42} -> locals() returns a dict of the CURRENT local namespace
check_locals()

# NOTE: modifying the dict returned by locals() does NOT reliably affect the
# actual local variables (implementation-defined behavior) - it's meant for
# INSPECTION/debugging, not as a way to dynamically create local variables.

print(f"{'*' * 70}")

# -------------------------
# 9. Default argument values are evaluated ONCE, at function DEFINITION time,
#    in the ENCLOSING scope at that moment - not at call time (ties scope
#    rules together with the classic mutable-default-argument gotcha)
# -------------------------
default_val = 10
def uses_default(x=default_val):   # 'default_val' is looked up and BOUND to
                                       # the parameter's default ONCE, right now
    return x

default_val = 999   # changing the variable AFTER the function is defined...
print(uses_default())   # ...still prints 10! the default was captured at DEFINITION time, not call time


## ==========================================================
## INTERVIEW QUESTIONS ON SCOPE (LOCAL, GLOBAL, NONLOCAL, LEGB)
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What does the LEGB rule stand for, and in what order does Python search
#    for a variable name?
#
# 2. Why does assigning to a variable ANYWHERE inside a function make Python
#    treat that name as LOCAL for the function's ENTIRE body - even for lines
#    that appear BEFORE the assignment? What error does this cause if you try
#    to read the variable before that assignment?
#
# 3. Do you need the `global` keyword to simply READ a global variable inside
#    a function? When do you actually need it?
#
# 4. If a global variable holds a mutable object (like a list), can you
#    modify its CONTENTS inside a function without declaring `global`? Why or
#    why not?
#
# 5. What is the difference between `global` and `nonlocal`? Can `nonlocal`
#    ever reach all the way up to the module-level (global) scope?
#
# 6. What happens if you use `nonlocal x` inside a function, but no enclosing
#    function has a variable named `x`? Is this caught at compile time or
#    runtime?
#
# 7. Does the loop variable in a regular `for` loop leak into the enclosing
#    scope after the loop finishes? Does this also happen with a list
#    comprehension's loop variable? Why or why not?
#
# 8. Why can't a method inside a class body directly reference a class-level
#    variable by its bare name (e.g., `class_var` instead of
#    `self.class_var` or `ClassName.class_var`)? What does this tell you
#    about how class bodies behave as a scope?
#
# 9. If you shadow a built-in function name (like `len`) with a local
#    variable inside a function, what happens if you then try to call
#    `len(...)` later in that SAME function?
#
# 10. What is a closure? How does `nonlocal` enable a closure (like the
#     `make_counter()` example) to maintain state across multiple calls?
#
# 11. In a triple-nested function (level1 -> level2 -> level3), if level3
#     declares `nonlocal val` but level2 never assigns `val`, where does
#     Python find the variable to bind to?
#
# 12. What do the built-in `globals()` and `locals()` functions return? Is it
#     safe to rely on modifying the dictionary returned by `locals()` to
#     change actual local variables?
#
# 13. When is a function's default argument value evaluated - every time the
#     function is called, or once at function definition time? How does this
#     relate to the classic "mutable default argument" bug?
#
# 14. Given a variable assigned at the module level and a same-named variable
#     assigned inside a function (with no `global` keyword), are these the
#     same variable or two independent ones?
#
# 15. Why does Python need explicit `global`/`nonlocal` declarations at all,
#     instead of just always searching outward through LEGB for
#     ASSIGNMENTS the same way it does for READS?
#
# 16. What's the difference in scoping behavior between Python 2 and Python 3
#     when it comes to list comprehensions leaking their loop variable into
#     the enclosing scope?
#
# 17. If two nested functions both use `nonlocal count` for the SAME
#     enclosing variable, and both are called, do they share the same
#     underlying value, or does each get an independent copy?
#
# 18. How would you write a simple stateful counter using closures and
#     `nonlocal`, without using a class or a global variable?
#
# 19. What scope does an exception variable belong to in `except Exception as
#     e:` - is `e` still accessible after the except block ends?
#
# 20. If a function parameter has the SAME name as a global variable, does
#     the function ever "see" the global variable at all in the sections of
#     code where the parameter is in scope?



if __name__ == "__main__":
    legb_demo()