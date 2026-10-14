## ==========================================================
## NUMBERS AND MATH OPERATIONS IN PYTHON
## ==========================================================

# -------------------------
# 1. Basic arithmetic operators
# -------------------------
# add
print(2 + 2)          # 4
# sub
print(4 - 2)          # 2
# multiply
print(4 * 2)          # 8
# exponent
print(5 ** 2)         # 25  -> 5 raised to power 2
# divide (true division) -> ALWAYS returns a float
print(10 / 3)         # 3.3333333333333335
# floor division -> returns the quotient, rounded DOWN (towards -infinity)
print(10 // 3)        # 3
print(-10 // 3)       # -4  (NOTE: rounds towards -infinity, not towards zero)
# modulus -> gives remainder
print(10 % 4)         # 2
print(-10 % 4)        # 2  (Python's % result always has the sign of the divisor)

# NOTE (interview point): a // b and a % b always satisfy:
#   a = (a // b) * b + (a % b)

print(f"{'*' * 50}")

# -------------------------
# 2. Core numeric types: int, float, complex
# -------------------------
# int -> whole numbers, arbitrary precision (limited only by memory, no overflow like C/Java)
a = 10
# float -> IEEE-754 double precision (64-bit) floating point number
b = 2.43
# complex -> has a real and imaginary part, imaginary part suffixed with 'j'
c = 6j

print(type(a))   # <class 'int'>
print(type(b))   # <class 'float'>
print(type(c))   # <class 'complex'>

# checking types the "pythonic" way (works with inheritance too)
print(isinstance(a, int))       # True
print(isinstance(b, (int, float)))  # True - checks against a tuple of types

print(f"{'*' * 50}")

# -------------------------
# 3. Arbitrary precision of int (very common interview talking point)
# -------------------------
# Unlike languages like Java/C++ where int overflows at a fixed bit width,
# Python's int automatically grows to hold arbitrarily large numbers.
big_num = 2 ** 200
print(big_num)
print(type(big_num))   # still <class 'int'>

print(f"{'*' * 50}")

# -------------------------
# 4. Float precision issues (VERY common interview question)
# -------------------------
print(0.1 + 0.2)                 # 0.30000000000000004  (NOT 0.3!)
print(0.1 + 0.2 == 0.3)          # False

# Why? Floats are stored in binary (IEEE-754), and 0.1 / 0.2 cannot be
# represented exactly in binary, similar to how 1/3 cannot be represented
# exactly in decimal.

# How to compare floats safely:
import math
print(math.isclose(0.1 + 0.2, 0.3))   # True

# rounding
print(round(2.5))     # 2  -> Python uses "banker's rounding" (round half to even)
print(round(3.5))     # 4
print(round(3.14159, 2))  # 3.14
# First argument: 3.14159 — the number to round
# Second argument: 2 — the number of decimal places to round to

# For exact decimal arithmetic (money, billing, etc.) use the decimal module
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))   # Decimal('0.3')  -> exact

# For exact rational numbers, use the fractions module
from fractions import Fraction
print(Fraction(1, 3) + Fraction(1, 6))   # Fraction(1, 2)

print(f"{'*' * 50}")

# -------------------------
# 5. Type conversion (casting) between numeric types
# -------------------------
print(int(3.99))     # 3  -> truncates towards zero, does NOT round
print(int(-3.99))    # -3
print(float(5))      # 5.0
print(complex(3))    # (3+0j)
print(complex(2, 5)) # (2+5j)

# converting string to number (common source of ValueError in interviews)
print(int("42"))
print(float("3.14"))
# int("3.14")        # would raise ValueError -> int() can't parse decimal strings directly
print(int(float("3.14")))  # 3 -> convert to float first, then int

print(f"{'*' * 50}")

# -------------------------
# 6. Underscores in numeric literals (Python 3.6+) for readability
# -------------------------
million = 1_000_000
print(million)          # 1000000
hex_val = 0x_FF_FF
print(hex_val)           # 65535

print(f"{'*' * 50}")

# -------------------------
# 7. Number systems: binary, octal, hexadecimal
# -------------------------
print(bin(10))     # '0b1010'
print(oct(10))     # '0o12'
print(hex(255))    # '0xff'

# literals directly in other bases
binary_literal = 0b1010      # 10
octal_literal = 0o12         # 10
hex_literal = 0xFF           # 255
print(binary_literal, octal_literal, hex_literal)

# converting a base-N string back to int
print(int('1010', 2))   # 10 (parse as binary)
print(int('ff', 16))    # 255 (parse as hex)

print(f"{'*' * 50}")

# -------------------------
# 8. Complex numbers in depth
# -------------------------
c1 = 3 + 4j
print(c1.real)        # 3.0  -> always returned as float
print(c1.imag)        # 4.0
print(abs(c1))         # 5.0 -> magnitude: sqrt(real**2 + imag**2)
print(c1.conjugate())  # (3-4j)

c2 = 1 + 2j
print(c1 + c2)   # (4+6j)
print(c1 * c2)   # complex multiplication (-5+10j)
"""
(1 + 2j) × (3 + 4j)
1×3  +  1×4j  +  2j×3  +  2j×4j
3    +  4j    +  6j    +  8j²
3 + 4j + 6j - 8
-5+10j
"""

print(f"{'*' * 50}")

# -------------------------
# 9. Useful math module functions (frequently used in interviews / DSA)
# -------------------------
print(math.sqrt(16))     # 4.0
print(math.floor(4.7))   # 4
print(math.ceil(4.1))    # 5
print(math.trunc(4.7))   # 4 -> truncates decimal part (towards zero)
print(math.pow(2, 3))    # 8.0 -> always returns float (unlike ** which can return int)
print(math.factorial(5)) # 120
print(math.gcd(12, 18))  # 6
print(math.inf)          # infinity
print(math.nan)          # "Not a Number"
print(math.nan == math.nan)   # False -> NaN is never equal to itself (special IEEE-754 rule)
print(math.isnan(math.nan))   # True -> correct way to check for NaN

print(f"{'*' * 50}")

# -------------------------
# 10. int caching / identity vs equality (classic "gotcha" interview question)
# -------------------------
# CPython caches small integers in range [-5, 256] for performance.
x = 100
y = 100
print(x is y)   # True -> same cached object

x = 300
y = 300
print(x is y)   # False (usually) -> different objects, outside the cached range
print(x == y)   # True -> values are equal even though identities differ

# LESSON: always use == to compare values; only use 'is' to check identity
# (e.g., comparing to None: `if x is None`)

print(f"{'*' * 50}")

# -------------------------
# 11. Numbers are immutable in Python
# -------------------------
n = 5
print(id(n))
n += 1          # this does NOT modify the int object in place;
                # it creates a NEW int object and rebinds the name 'n' to it
print(id(n))    # different id

print(f"{'*' * 50}")

# -------------------------
# 12. Bitwise operators (work on the integer type)
# -------------------------
p, q = 12, 10
print(p & q)    # AND  -> 8
print(p | q)    # OR   -> 14
print(p ^ q)    # XOR  -> 6
print(~p)       # NOT  -> -13 (two's complement: ~p == -(p+1))
print(p << 2)   # left shift  -> 48 (multiply by 2**2)
print(p >> 2)   # right shift -> 3  (divide by 2**2, floor)

print(f"{'*' * 50}")

# -------------------------
# 13. Boolean is a subclass of int (another classic gotcha)
# -------------------------
print(isinstance(True, int))   # True
print(True + True)             # 2
print(True == 1)               # True
print(False == 0)              # True

print(f"{'*' * 50}")

# -------------------------
# 14. The 'numbers' module - abstract base class hierarchy (good for senior-level answers)
# -------------------------
# numbers.Complex -> numbers.Real -> numbers.Rational -> numbers.Integral
# int is Integral, float is Real, complex is Complex, Fraction is Rational.
import numbers
print(isinstance(5, numbers.Integral))   # True
print(isinstance(5.0, numbers.Real))     # True
print(isinstance(5 + 0j, numbers.Complex))  # True


## ==========================================================
## INTERVIEW QUESTIONS & ANSWERS ON PYTHON NUMERIC DATA TYPES
## ==========================================================

INTERVIEW_QA = """
1. What are the built-in numeric types in Python? How are they related to
   each other (e.g., is bool related to int)?

   ANSWER: Python has three built-in numeric types: int, float, and complex.
   bool is a SUBCLASS of int (not a separate primitive) -> True/False behave
   as 1/0 in arithmetic. Decimal and Fraction are standard-library
   additions, not core built-ins. isinstance(True, int) -> True


2. Why does 0.1 + 0.2 not equal 0.3 in Python? Explain how floats are
   stored internally.

   ANSWER: Floats use IEEE-754 binary representation, and 0.1 / 0.2 cannot
   be represented exactly in binary (just like 1/3 cannot be represented
   exactly in decimal). Tiny approximation errors compound when added,
   giving 0.30000000000000004 instead of exactly 0.3.


3. How would you safely compare two floating point numbers for "equality"?

   ANSWER: Use math.isclose(a, b) -> compares within a tolerance (rel_tol /
   abs_tol) instead of requiring exact bit equality.
   math.isclose(0.1 + 0.2, 0.3)  # True


4. What is the difference between / and // in Python? What happens with
   negative numbers, e.g. -7 // 2?

   ANSWER: '/' is true division -> always returns a float.
   '//' is floor division -> rounds DOWN, toward -infinity (not toward zero).
   -7 // 2   # -4, NOT -3


5. Explain Python's modulus(%) operator behavior with negative numbers,
   e.g. -7 % 3.

   ANSWER: Python's '%' result always takes the SIGN OF THE DIVISOR, it returns remainder
   (unlike C/Java, which takes the sign of the dividend).
   -7 % 3    # 2
   Invariant: a == (a // b) * b + (a % b)
            a == (a // b) * b + (a % b)
            -7 == (-3) * 3 + (a % b)
            -7 == -9 + (a % b)
            a % b == -7 - (-9)
            a % b == 2


6. Does Python's int type ever overflow? How is this different from
   languages like Java or C?

   ANSWER: Python's int NEVER overflows -> arbitrary precision, limited
   only by available memory. Java/C++ use fixed-width ints (e.g. 32/64-bit)
   that wrap around or throw on overflow.


7. What is int caching (small integer interning) in CPython? What range
   does it cover, and why does it exist?

   ANSWER: CPython caches small integers in the range [-5, 256] as a
   performance optimization (these values are extremely common, e.g. loop
   counters). This is a CPython IMPLEMENTATION DETAIL, not a language
   guarantee.
   x = 100; y = 100; x is y   # True (cached)
   x = 300; y = 300; x is y   # False (usually, outside cache range)


8. What is the difference between 'is' and '==' when comparing numbers?
   When should you use each?

   ANSWER: '==' compares VALUE equality. 'is' compares OBJECT IDENTITY.
   Always use '==' to compare numbers. Only use 'is' for identity checks,
   e.g. singleton comparisons like `if x is None`.


9. How would you convert a string like "101" to an integer using base 2?
   How about converting an integer to its binary/octal/hex string
   representation?

   ANSWER: String (base N) -> int:  int('101', 2)  # 5   int('ff', 16)  # 255
   Int -> string in other base: bin(10)  # '0b1010'
                                 oct(10)  # '0o12'
                                 hex(255) # '0xff'


10. What module would you use for precise decimal arithmetic (e.g., for
    currency calculations), and why shouldn't you use float for money?

    ANSWER: Use the 'decimal' module (Decimal) for currency/billing.
    Decimal('0.1') + Decimal('0.2')   # Decimal('0.3') -> exact
    float shouldn't be used for money because binary floating-point can't
    represent most decimal fractions exactly, and rounding errors compound
    across many transactions -> unacceptable for financial calculations.


11. What is the Fraction class used for? Give a scenario where you'd
    prefer it over float.

    ANSWER: Fraction represents EXACT rational numbers
    (numerator/denominator), with no rounding at all.
    Fraction(1, 3) + Fraction(1, 6)   # Fraction(1, 2)
    Prefer it over float when you need exact ratio arithmetic, e.g. exact
    probabilities or scaling recipe measurements without accumulated
    error.


12. Explain how complex numbers are represented in Python. How do you
    access the real and imaginary parts, and how do you get the
    magnitude of a complex number?

    ANSWER: Complex numbers: c = 3 + 4j
    c.real           # 3.0 -> always returned as a float
    c.imag           # 4.0
    abs(c)           # 5.0 -> magnitude: sqrt(real**2 + imag**2)
    c.conjugate()    # (3-4j)


13. What does math.isclose() do, and what parameters control its tolerance?

    ANSWER: math.isclose(a, b, rel_tol=1e-9, abs_tol=0.0)
    rel_tol -> relative tolerance, scales with the magnitude of the numbers
    abs_tol -> absolute tolerance, useful for comparisons near zero


14. What is the difference between round(2.5) and round(3.5) in Python?
    Why does this happen (banker's rounding)?

    ANSWER: round(2.5) -> 2 ; round(3.5) -> 4
    Python uses "banker's rounding" (round-half-to-even): exact halfway
    values round to the nearest EVEN neighbor. This reduces cumulative
    statistical bias compared to always rounding 0.5 up.


15. Are Python numbers mutable or immutable? What are the implications
    of this when you do something like `x += 1`?

    ANSWER: Python numbers are IMMUTABLE. `n += 1` does NOT modify n in
    place; it creates a brand NEW int object and rebinds the name n to it.
    n = 5; id(n)   # some address
    n += 1; id(n)  # different address -> new object


16. What is the difference between math.floor(), math.ceil(),
    math.trunc(), and int() when applied to a negative float like -3.7?

    ANSWER: 
    math.floor(-3.7)   # -4  -> rounds down (toward -infinity)
    math.ceil(-3.7)    # -3  -> rounds up (toward +infinity)
    math.trunc(-3.7)   # -3  -> chops decimal part (toward zero)
    int(-3.7)          # -3  -> same as trunc for floats (toward zero)
    floor/ceil differ from truncation specifically for negative numbers.


17. Explain Python's bitwise operators (&, |, ^, ~, <<, >>). What does
    ~x evaluate to for a given integer x?

    ANSWER: 
    & -> AND (bit set only if both bits are 1)
    | -> OR  (bit set if either bit is 1)
    ^ -> XOR (bit set if bits differ)
    ~ -> NOT/invert -> flips every bit; ~x == -(x + 1) (two's complement)
    << -> left shift  (multiply by 2**n)
    >> -> right shift (floor-divide by 2**n)


18. Why is `True + True` valid in Python and what does it evaluate to?
    What does this tell you about the bool type?

    ANSWER: True + True is valid because bool is a SUBCLASS of int ->
    True/False are literally 1/0 under the hood, so arithmetic operators treat them as integers.
    True + True   # 2
    This shows bool has no separate arithmetic; it inherits int's rules.


19. What is NaN? Why does `float('nan') == float('nan')` return False,
    and how do you correctly check whether a value is NaN?

    ANSWER: NaN ("Not a Number") represents an undefined/unrepresentable
    float result. Per the IEEE-754 standard, NaN is defined to be UNEQUAL
    to everything, including itself -> float('nan') == float('nan')  #
    False
    Correct check: math.isnan(x)  -> True only if x is NaN
    (never compare with == to detect NaN)


20. What are the abstract base classes defined in the `numbers` module
    (Complex, Real, Rational, Integral), and why might you use
    isinstance() checks against them instead of concrete types like
    int/float?

    ANSWER: Hierarchy: numbers.Complex -> numbers.Real -> numbers.Rational -> numbers.Integral
    int -> Integral, float -> Real, complex -> Complex, Fraction -> Rational
    Using isinstance(x, numbers.Real) instead of isinstance(x, (int,float)) 
    is more general/extensible -> it also matches custom numeric
    types (e.g. NumPy scalars) that register as ABC subclasses.


21. How does Python decide the result type of an operation between an
    int and a float (i.e., implicit type coercion / promotion rules)?

    ANSWER: When mixing int and float in an operation, Python PROMOTES
    the result to float (the "wider" type), so no precision from the
    wider type is lost.
    type(1 + 2.0)   # <class 'float'>


22. What's the maximum value of an integer in Python? (Trick question - think about it.)

    ANSWER: TRICK QUESTION: there is NO maximum -> Python's int has
    arbitrary precision (see Q6), unlike C/Java's fixed-width integers
    with a hard ceiling. (sys.maxsize reflects platform pointer size,
    not an int cap.)


23. How would you generate a large random integer or float in Python, and which module would you use?

    ANSWER: Use the 'random' module:
    random.randint(1, 100)     # random int in an inclusive range
    random.random()             # random float in [0.0, 1.0)
    random.uniform(1.5, 9.5)    # random float in a custom range
    For cryptographically secure randomness, use the 'secrets' module
    instead (random is NOT secure for tokens/passwords).


24. What happens when you divide a number by zero in Python for int vs float (e.g., 5 / 0 vs 5.0 / 0.0 vs 5 // 0)?

    ANSWER: 5 / 0     # ZeroDivisionError: division by zero
    5.0 / 0.0 # ZeroDivisionError: float division by zero
    5 // 0    # ZeroDivisionError: integer division or modulo by zero
    All THREE raise ZeroDivisionError -> Python does NOT silently return
    inf/nan like some languages/IEEE-754 float semantics might suggest.
"""

if __name__ == "__main__":
    print(INTERVIEW_QA)