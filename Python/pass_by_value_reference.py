"""
How Python actually works: Pass by Object Reference
    In Python, when you pass a variable to a function, you're passing a reference to the object
    that variable points to — not a copy of the value, and not the variable itself.

What happens depends on whether the object is mutable or immutable.
-----------------------------------------------------------------------------------------------------
Case 1: Immutable objects (int, float, str, tuple) — behaves like "pass by value"
def change(x):
    x = 100        # creates a NEW object, rebinds local x to it
    print("Inside:", x)
a = 10
change(a)
print("Outside:", a)

Output:
Inside: 100
Outside: 10

    Why? x = 100 doesn't modify the original integer object — integers can't be modified.
    It just makes x point to a new object. a still points to the original 10.
-----------------------------------------------------------------------------------------------------
Case 2: Mutable objects (list, dict, set) — behaves like "pass by reference"
def change(lst):
    lst.append(100)   # modifies the SAME object

a = [1, 2, 3]
change(a)
print(a)

Output:
[1, 2, 3, 100]

    Here, lst and a both point to the same list object in memory. lst.append(100) mutates that shared object,
    so the change is visible outside the function too.

"""


# pass by reference is passing the object itself to the function
a = 100
print(a)
def fun(n):
    print(n)
    n = 0
    print(n)
fun(a)
print(a)

'''
Output:
100
100
0
100
'''

lst = [1,2,3]
def pass_by_ref(l,value):
    l.append(value)

pass_by_ref(lst,10)
print(lst) # [1,2,3,10]


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. The correct terminology: Python is neither "pass by value" NOR "pass by
#    reference" - it's "PASS BY OBJECT REFERENCE" (also called "pass by
#    assignment"). This is the single most important clarification interviewers
#    look for - many candidates just say "pass by reference" and stop there,
#    which is technically INCORRECT.
# -------------------------
# - In true "pass by value" (like C), the function gets a full COPY - changes
#   inside never affect the caller, period.
# - In true "pass by reference" (like C++ references, or `ref` in C#), the
#   function can REBIND the caller's variable itself to point elsewhere.
# - Python does NEITHER exactly: the function parameter is a NEW local name
#   that refers to the SAME object as the caller's variable. You can MUTATE
#   the shared object (if mutable), but REBINDING the parameter inside the
#   function does NOT affect what the caller's variable points to.
print("See point 2 and 3 below for proof of each half of this claim.")

print(f"{'*' * 70}")

# -------------------------
# 2. Proving "rebinding doesn't affect the caller" with id()
# -------------------------
def rebind_demo(x):
    print("id before rebind:", id(x))
    x = 999          # REBINDS the local name 'x' to a NEW object
    print("id after rebind:", id(x))

a = 10
print("caller id:", id(a))
rebind_demo(a)
print("caller value after call:", a)   # 10 -> completely unaffected by the rebind inside the function

print(f"{'*' * 70}")

# -------------------------
# 3. Proving "mutation DOES affect the caller" with id() (same object, changed content)
# -------------------------
def mutate_demo(lst):
    print("id before mutation:", id(lst))
    lst.append(999)    # MUTATES the SAME object in place
    print("id after mutation:", id(lst))    # SAME id - proves it's the same object!

b = [1, 2, 3]
print("caller id:", id(b))
mutate_demo(b)
print("caller value after call:", b)   # [1, 2, 3, 999] -> caller SEES the mutation

print(f"{'*' * 70}")

# -------------------------
# 4. All immutable types behave like the int example - str, tuple, float, bool
# -------------------------
def modify_string(s):
    s += " world"    # creates a NEW string, rebinds local 's' - doesn't touch original
    print("Inside:", s)

text = "hello"
modify_string(text)
print("Outside:", text)   # 'hello' -> unaffected, strings are immutable

def modify_tuple(t):
    t = t + (4,)       # creates a NEW tuple, rebinds local 't'
    print("Inside:", t)

tup = (1, 2, 3)
modify_tuple(tup)
print("Outside:", tup)     # (1, 2, 3) -> unaffected, tuples are immutable

print(f"{'*' * 70}")

# -------------------------
# 5. All mutable types behave like the list example - dict, set also mutate in place
# -------------------------
def modify_dict(d):
    d["new_key"] = "new_value"    # mutates the SAME dict object

data = {"a": 1}
modify_dict(data)
print(data)   # {'a': 1, 'new_key': 'new_value'} -> caller sees the change

def modify_set(s):
    s.add(99)    # mutates the SAME set object

my_set = {1, 2, 3}
modify_set(my_set)
print(my_set)   # {1, 2, 3, 99} -> caller sees the change

print(f"{'*' * 70}")

# -------------------------
# 6. CRITICAL gotcha: += behaves DIFFERENTLY for mutable vs immutable, even
#    though it LOOKS like the same operator each time
# -------------------------
def append_with_plus_equals(lst):
    lst += [999]    # for a LIST, += calls __iadd__ which mutates IN PLACE
                      # (equivalent to lst.extend([999])) - NOT the same as lst = lst + [999]!

my_list = [1, 2, 3]
append_with_plus_equals(my_list)
print(my_list)   # [1, 2, 3, 999] -> caller SEES this change! (unlike the int/str += examples above)

# WHY the difference: for mutable types with an __iadd__ method (list, etc.),
# `x += y` mutates x in place and rebinds x to itself (same object). For
# immutable types (int, str, tuple - no __iadd__), `x += y` is just shorthand
# for `x = x + y`, which creates a brand new object and rebinds x to it.

print(f"{'*' * 70}")

# -------------------------
# 7. Tuple containing a mutable object - a nuance that trips people up
# -------------------------
def modify_tuple_with_list(t):
    t[0].append(999)    # the TUPLE itself is immutable, but if a slot HOLDS
                            # a mutable object (like a list), THAT object can still be mutated!

mixed = ([1, 2], "fixed")
modify_tuple_with_list(mixed)
print(mixed)   # ([1, 2, 999], 'fixed') -> the inner list WAS mutated, even though
                  # the outer tuple itself cannot be reassigned/resized

print(f"{'*' * 70}")

# -------------------------
# 8. How to "simulate" pass-by-reference for an immutable value (a common
#    interview follow-up: "how would you work around this?")
# -------------------------
# Workaround 1: wrap the value in a mutable container (list, dict) and mutate
# the CONTAINER instead of the value directly:
def increment_workaround(container):
    container[0] += 1    # mutating INDEX 0 of the list, not rebinding the list itself

value_holder = [10]
increment_workaround(value_holder)
print(value_holder[0])   # 11 -> "by reference" effect achieved via a mutable wrapper

# Workaround 2: use a simple class/object as a mutable "box"
class Box:
    def __init__(self, value):
        self.value = value

def increment_box(box):
    box.value += 1   # mutating an ATTRIBUTE, not rebinding the box object itself

b = Box(10)
increment_box(b)
print(b.value)   # 11

# Workaround 3 (most Pythonic): just RETURN the new value instead of trying
# to mutate the caller's variable at all:
def increment(x):
    return x + 1

value = 10
value = increment(value)   # caller explicitly re-assigns
print(value)                 # 11

print(f"{'*' * 70}")

# -------------------------
# 9. Multiple "output parameters" - Python doesn't have true output/ref
#    parameters like C#'s `out`/`ref`; the idiomatic solution is to return a
#    tuple and unpack it
# -------------------------
def divide_with_remainder(a, b):
    return a // b, a % b     # return MULTIPLE values as a tuple

quotient, remainder = divide_with_remainder(17, 5)
print(quotient, remainder)   # 3 2

print(f"{'*' * 70}")

# -------------------------
# 10. Default arguments interact with this same mutability concept - the
#     classic "mutable default argument" bug is a DIRECT consequence of
#     pass-by-object-reference semantics
# -------------------------
def buggy_append(item, items=[]):   # the default list is created ONCE, at
                                       # function DEFINITION time, not per call!
    items.append(item)
    return items

print(buggy_append(1))   # [1]
print(buggy_append(2))    # [1, 2] -> NOT [2]! same shared default list object across calls,
                             # exactly because Python passes/binds by object reference

def fixed_append(item, items=None):   # SAFE fix - create a fresh list each call
    if items is None:
        items = []
    items.append(item)
    return items

print(fixed_append(1))   # [1]
print(fixed_append(2))    # [2] -> correctly independent


## ==========================================================
## INTERVIEW QUESTIONS ON PASS BY VALUE / REFERENCE IN PYTHON
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. Is Python "pass by value" or "pass by reference"? What is the technically
#    correct term, and why do both simpler answers fall short?
#
# 2. If you reassign a function parameter inside the function body (e.g.,
#    `x = 100`), does that affect the caller's variable? Why or why not?
#
# 3. If you mutate a function parameter in place (e.g., `lst.append(x)`), does
#    that affect the caller's variable? Why is this different from question 2?
#
# 4. Why does `x += [1]` behave differently from `x = x + [1]` when x is a
#    list, even though they look equivalent at first glance?
#
# 5. Does the answer to "does mutation inside a function affect the caller"
#    depend on whether the argument passed in is mutable or immutable? Give
#    an example of each.
#
# 6. If a tuple contains a list, can that inner list still be mutated even
#    though the tuple itself is immutable? What does this reveal about what
#    "immutable" actually means for a tuple?
#
# 7. How would you use id() to PROVE whether a function parameter and the
#    caller's original variable refer to the same object at various points
#    in the function's execution?
#
# 8. Since Python has no `out` or `ref` parameters (like C#), how would you
#    write a function that needs to "return" multiple values to the caller?
#
# 9. How is the classic "mutable default argument" bug
#    (`def f(x, items=[])`) a direct consequence of Python's pass-by-object-
#    reference semantics?
#
# 10. If you wanted to simulate "pass by reference" for a single immutable
#     value (like an int) so a function COULD modify the caller's value,
#     what workaround(s) would you use?
#
# 11. What is the difference between the __iadd__ dunder method and simply
#     having no __iadd__ defined, in terms of how `+=` behaves for a custom
#     class?
#
# 12. In Java, primitives are passed by value and objects are passed by
#     reference to the object (similar to Python). How is this comparable to,
#     or different from, Python's argument-passing model?
#
# 13. If two function parameters (from two different arguments) happen to
#     point to the SAME mutable object, and you mutate one of them inside the
#     function, does the other one also reflect the change?
#
# 14. Why does printing `id(x)` before and after `x = new_value` inside a
#     function show DIFFERENT ids, but printing `id(x)` before and after
#     `x.append(new_value)` shows the SAME id?
#
# 15. What would happen if a function parameter default value were a mutable
#     object created fresh INSIDE the function body (like the `fixed_append`
#     example) versus specified directly in the function signature (like
#     `buggy_append`)? Why does WHERE the object is created matter so much?