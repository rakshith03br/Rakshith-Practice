"""
str (String) in Python:- str()

String: String is set of characters that are together and enclosed with single,double and triple quotes.
A string is a sequence of characters used to represent text. It's one of the most commonly used data types in Python.
    Immutable — once created, a string cannot be changed in place
    Ordered — characters have a fixed position (indexed)
    Iterable — you can loop through characters one by one
"""

# Creating strings
s1 = 'Hello'
s2 = "World"
s3 = '''This is a
multi-line string'''
s4 = """This also works
for multiple lines"""
# Single quotes, double quotes — both work the same way. Triple quotes (''' or """) let you span multiple lines.

# Indexing and slicing
# Strings are ordered, so each character has a position (index), starting at 0.
# s[start:stop:step]

s = "Python"
#    012345     # +ve index
#    654321     # -ve index
print(s[0])     # 'P'
print(s[-1])    # 'n'  (negative index counts from the end)
print(s[1:4])   # 'yth'  (slicing: start included, end excluded)
print(s[::-1])  # 'nohtyP'  (reverses the string using indexing)
print(s[0::2])  # pto
print(s[-7])    # IndexError: string index out of range


# Strings are immutable
# You cannot change a character in place:
# s = "Hello"
# s[0] = "J"   # ❌ TypeError — strings don't support item assignment
# # Instead, you create a new string:
# s = "Hello"
# s = "J" + s[1:]
# print(s)  # "Jello"

# Common string methods
s = "  Hello World  "

s.strip()        # "Hello World"        — removes leading/trailing spaces
s.lstrip()        # "Hello World  "        — removes leading spaces
s.rstrip()        # "  Hello World"        — removes trailing spaces
s.lower()        # "  hello world  "    — lowercase
s.upper()        # "  HELLO WORLD  "    — uppercase
s.replace("Hello", "Hi")  # "  Hi World  "
s.split()        # ['Hello', 'World']   — splits into a list
s.splitlines()    #  ['  Hello World  ']
s.find("World")  # index where "World" starts # 8
len(s)           # length of the string # 15

# Concatenation and repetition
a = "Hello"
b = "World"
print(a + " " + b)  # "Hello World"  — concatenation
print(a * 3)          # "HelloHelloHello"  — repetition

# String formatting
name = "Alice"
age = 25
# f-strings (recommended, Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# .format()
print("My name is {} and I am {} years old.".format(name, age))

# % operator (older style)
print("My name is %s and I am %d years old." % (name, age))

# Checking string content
"123".isdigit()     # True
"abc".isalpha()     # True
"abc123".isalnum()  # True
" ".isspace()       # True

# Iterating through a string
for ch in "Python":
    print(ch)

# Membership check
s = "Hello World"
print("World" in s)   # True
print("Bye" in s)     # False


# Joining strings
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)  # "Python is fun"

## escape character(\)
print('Hello\'world')
print("C:\\Users\\name\\Documents")


## raw string
path = r"C:\Users\name\Documents"
print(path)   # C:\Users\name\Documents  — backslashes stay literal

## concatination of str and int
a = "Hi "
b = 100
print(a + str(b))

"""
 Quick summary
Feature	                String
--------                ----------------------------------------
Ordered?	            ✅ Yes
Indexed?	            ✅ Yes
Mutable?	            ❌ No (immutable)
Duplicates allowed?	    ✅ Yes (characters can repeat)
Common use	            Text storage, manipulation, formatting
"""

## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION
## ==========================================================

# -------------------------
# 1. find() vs index() vs count()  (common confusion point)
# -------------------------
s = "Hello World"
print(s.find("Bye"))     # -1  -> returns -1 if not found, never raises
# print(s.index("Bye"))  # ValueError: substring not found -> raises exception
print(s.index("World"))  # 6   -> works like find() but raises on failure
print(s.count("o"))      # 2   -> counts non-overlapping occurrences

print(f"{'*' * 50}")

# -------------------------
# 2. startswith() / endswith() (better than slicing for prefix/suffix checks)
# -------------------------
filename = "report.pdf"
print(filename.startswith("report"))   # True
print(filename.endswith(".pdf"))       # True
print(filename.endswith((".pdf", ".doc")))  # True -> accepts a tuple of options

print(f"{'*' * 50}")

# -------------------------
# 3. split() vs rsplit() vs splitlines() vs partition()
# -------------------------
path = "a,b,c,d"
print(path.split(","))         # ['a', 'b', 'c', 'd']
print(path.split(",", 1))      # ['a', 'b,c,d']  -> maxsplit limits number of splits
print(path.rsplit(",", 1))     # ['a,b,c', 'd']  -> splits from the right

text = "line1\nline2\nline3"
print(text.splitlines())       # ['line1', 'line2', 'line3'] -> splits on line boundaries, no trailing empty string

# partition() splits into exactly 3 parts: (before, separator, after)
print("key=value".partition("="))   # ('key', '=', 'value')
print("no-sep-here".partition("="))  # ('no-sep-here', '', '') -> sep not found

print(f"{'*' * 50}")

# -------------------------
# 4. Padding and alignment methods (useful for formatted output, tables, reports)
# -------------------------
print("42".zfill(5))       # '00042'   -> zero-pads on the left, handles sign correctly e.g. "-42".zfill(5) -> '-0042'
print("hi".ljust(10, "-")) # 'hi--------'
print("hi".rjust(10, "-")) # '--------hi'
print("hi".center(10, "-"))# '----hi----'

print(f"{'*' * 50}")

# -------------------------
# 5. strip() variants
# -------------------------
s = "xxHelloxx"
print(s.strip("x"))    # 'Hello'      -> strips given characters from both ends
print(s.lstrip("x"))   # 'Helloxx'    -> strips from the left only
print(s.rstrip("x"))   # 'xxHello'    -> strips from the right only

print(f"{'*' * 50}")

# -------------------------
# 6. Advanced f-string features (Python 3.8+)
# -------------------------
value = 3.14159
name = "Bob"
print(f"{value:.2f}")        # '3.14'     -> format specifier: 2 decimal places
print(f"{value:>10.2f}")     # '      3.14' -> right-align in a width-10 field
print(f"{name=}")            # "name='Bob'" -> self-documenting expressions (3.8+), great for debugging
number = 1000000
print(f"{number:,}")         # '1,000,000' -> thousands separator

print(f"{'*' * 50}")

# -------------------------
# 7. Raw strings (r-strings) — important for regex and file paths
# -------------------------
path = r"C:\Users\name\Documents"   # backslashes are NOT treated as escape characters
print(path)                          # C:\Users\name\Documents
normal = "C:\\Users\\name\\Documents"  # without raw string, need to escape each backslash
print(normal)           # C:\Users\name\Documents

print(f"{'*' * 50}")

# -------------------------
# 8. String <-> character code conversions
# -------------------------
print(ord('A'))    # 65  -> character to its Unicode code point
print(chr(65))     # 'A' -> code point to character
print(ord('a'))    # 97

print(f"{'*' * 50}")

# -------------------------
# 9. Encoding / decoding (str vs bytes) — common interview topic
# -------------------------
s = "café"
encoded = s.encode("utf-8")       # str -> bytes
print(encoded)                     # b'caf\xc3\xa9'
decoded = encoded.decode("utf-8")  # bytes -> str
print(decoded)                     # 'café'
print(type(encoded))               # <class 'bytes'>

# NOTE: In Python 3, str is Unicode by default (unlike Python 2 where str was bytes).

print(f"{'*' * 50}")

# -------------------------
# 10. String immutability & efficient concatenation (performance gotcha)
# -------------------------
# BAD (in a loop): creates a new string object on every iteration -> O(n^2) time
result = ""
for word in ["Python", "is", "fun"]:
    result += word + " "
print(result)


# GOOD: build a list and join once at the end -> O(n) time
parts = []
for word in ["Python", "is", "fun"]:
    parts.append(word)
result = " ".join(parts)
print(result)       # "Python is fun"

print(f"{'*' * 50}")

# -------------------------
# 11. String interning (identity vs equality — similar to int caching)
# -------------------------
a = "hello"
b = "hello"
print(a is b)      # True -> CPython interns short, identifier-like string literals

c = "hello world!"
d = "hello world!"
print(c is d)      # may be False -> strings with spaces/special chars aren't always interned
print(c == d)       # True -> always use == to compare string VALUES, not 'is'

import sys
e = sys.intern("hello world!")
f = sys.intern("hello world!")
print(e is f)       # True -> sys.intern() forces interning manually

print(f"{'*' * 50}")

# -------------------------
# 12. String comparison rules (lexicographic, based on Unicode code points)
# -------------------------
print("apple" < "banana")   # True  -> compared character by character
print("Apple" < "apple")    # True  -> uppercase letters have smaller code points than lowercase
print("10" < "9")           # True  -> STRING comparison, not numeric! ("1" < "9")

print(f"{'*' * 50}")

# -------------------------
# 13. translate() and maketrans() — bulk character replacement (faster than chained replace())
# -------------------------
table = str.maketrans("abc", "xyz")
print("aabbcc".translate(table))   # 'xxyyzz'

# removing characters using translate
remove_table = str.maketrans("", "", "aeiou")
print("hello world".translate(remove_table))  # 'hll wrld'

print(f"{'*' * 50}")

# -------------------------
# 14. Checking content: additional is* methods
# -------------------------
print("Hello World".istitle())   # True  -> each word starts with uppercase
print("HELLO".isupper())          # True
print("hello".islower())          # True
print("123".isnumeric())          # True
print("  ".isspace())             # True
print("".isalpha())               # False -> empty string returns False for all is* checks

print(f"{'*' * 50}")

# -------------------------
# 15. String multiplication and repetition edge cases
# -------------------------
print("ab" * 0)     # ''  -> empty string
print("ab" * -1)    # ''  -> negative repeat also gives empty string (no error)

print(f"{'*' * 50}")

# -------------------------
# 16. Common interview coding patterns using strings
# -------------------------
def is_palindrome(text: str) -> bool:
    cleaned = text.lower().replace(" ", "")
    if cleaned == cleaned[::-1]:
        return True
    else:
        return False

print(is_palindrome("Nurses Run"))   # True


def is_anagram(s1: str, s2: str) -> bool:
    print(sorted(s1.lower()))
    print(sorted(s2.lower()))
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("listen", "silent"))  # True

def reverse_words(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])

print(reverse_words("Python is fun"))   # "fun is Python"

def count_vowels(text: str) -> int:
    return sum(1 for ch in text.lower() if ch in "aeiou")

print(count_vowels("Hello World"))   # 3

print(f"{'*' * 50}")

# -------------------------
# 17. String module (predefined character sets — handy for validation/generation tasks)
# -------------------------
import string
print(string.ascii_lowercase)   # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase)   # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)            # '0123456789'
print(string.punctuation)       # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


## ==========================================================
## INTERVIEW QUESTIONS & ANSWERS ON PYTHON STRING DATA TYPE
## ==========================================================

INTERVIEW_QA = """
1. Why are strings immutable in Python? What are the benefits and drawbacks
   of this design?

   ANSWER: Strings are immutable so they can be safely used as dict keys /
   set members (their hash never changes), shared across multiple
   references without risk of unexpected mutation, and safely cached /
   interned by CPython for performance. Drawback: any "modification"
   creates a brand-new string object, which can be inefficient if done
   repeatedly (e.g. += in a loop -> O(n^2) total cost).


2. What happens internally when you do `s += "text"` in a loop? Why is
   this considered inefficient, and what's the better alternative?

   ANSWER: Each `s += "text"` creates an entirely NEW string object
   (concatenating the old string with "text") and rebinds s to it -- the
   original string is discarded. Doing this n times means copying
   increasingly large strings repeatedly, giving O(n^2) total time.
   Better alternative: accumulate pieces in a list and call "".join(parts)
   once at the end -> O(n) time, since join() only allocates the final
   string once.


3. What is string interning in CPython? Why does `"hello" is "hello"`
   return True but `"hello world!" is "hello world!"` may return False?

   ANSWER: Interning is a CPython optimization that reuses a single
   shared object for certain strings instead of creating duplicates.
   Short, identifier-like literals (no spaces/special characters,
   resembling variable names) are automatically interned by the compiler,
   so two occurrences point to the SAME object -> "hello" is "hello"
   -> True. Strings with spaces or built dynamically (e.g. at runtime via
   concatenation) are not automatically interned, so they may be separate
   objects with equal VALUE but different IDENTITY -> "hello world!" is
   "hello world!" may be False. This is an implementation detail, not a
   language guarantee -- always use == for value comparison. You can force
   interning manually with sys.intern().


4. What is the difference between find(), index(), and count()? What
   happens when the substring is not found in each case?

   ANSWER: find() returns the index of the first occurrence, or -1 if not
   found (never raises). index() behaves like find() but RAISES
   ValueError if the substring isn't found. count() returns the number of
   non-overlapping occurrences of the substring (returns 0, not an error,
   if not found).


5. Explain the difference between split(), rsplit(), and partition(). When
   would you use partition() over split()?

   ANSWER: split() splits from the LEFT, with an optional maxsplit limit,
   returning a list of all pieces. rsplit() splits from the RIGHT --
   useful when you want to limit splits starting from the end (e.g.
   splitting off just the last segment of a path). partition() always
   splits into exactly a 3-tuple: (before, separator, after) on the FIRST
   occurrence of the separator -- use it when you specifically want the
   separator itself preserved and only care about one split point (e.g.
   parsing "key=value" into key/sep/value), which is often clearer and
   faster than split() with maxsplit=1 plus manual unpacking.


6. How would you reverse a string in Python? Can you do it without using
   slicing?

   ANSWER: Slicing: s[::-1] -- most idiomatic and fastest in practice.
   Without slicing: "".join(reversed(s)) using the built-in reversed()
   iterator, or a manual loop building a new string/list and reversing
   it, e.g.:
       result = []
       for ch in s:
           result.insert(0, ch)   # inefficient, O(n^2), for illustration only
       "".join(result)
   In practice, s[::-1] or "".join(reversed(s)) are the preferred
   approaches.


7. How do you check if two strings are anagrams of each other? What's the
   time complexity of your approach?

   ANSWER: Sort both strings (after normalizing case) and compare:
       sorted(s1.lower()) == sorted(s2.lower())
   Time complexity: O(n log n) due to sorting. A faster O(n) alternative
   uses character frequency counts (e.g. collections.Counter(s1) ==
   collections.Counter(s2)), which avoids the sort but uses extra space
   for the counters.


8. What's the difference between str and bytes in Python 3? When would you need to encode/decode between them?

   ANSWER: str represents Unicode TEXT (sequence of Unicode code points).
   bytes represents raw BINARY data (sequence of integers 0-255). You
   convert str -> bytes with .encode(encoding) (e.g. "utf-8"), and
   bytes -> str with .decode(encoding). You need this whenever text
   crosses a boundary that only understands raw bytes -- e.g. writing
   text to a file in binary mode, sending data over a network socket, or
   reading data from disk/network that must be decoded back into text.


9. What is a raw string (r"...")? Give a real-world scenario where you'd need one.

   ANSWER: A raw string tells Python to treat backslashes literally,
   NOT as escape-sequence introducers -- r"\\n" is the two characters
   backslash + n, not a newline. Real-world use cases: Windows file
   paths (r"C:\\Users\\name") where you'd otherwise need to double every
   backslash, and regular expressions (re.compile(r"\\d+")) where regex
   syntax itself uses lots of backslashes that would otherwise collide
   with Python's own escape sequences.


10. Explain Python's f-string formatting. How would you format a float
    to 2 decimal places, or add thousands separators to a large number?

    ANSWER: f-strings (f"...") let you embed expressions directly inside
    string literals using {expression}, evaluated at runtime, optionally
    with a format spec after a colon.
    2 decimal places: f"{value:.2f}"
    Thousands separator: f"{number:,}"
    You can combine specs too, e.g. f"{number:,.2f}" for both thousands
    separators and 2 decimal places.


11. Why does `"10" < "9"` evaluate to True? Explain how string comparison
    works under the hood.

    ANSWER: String comparison is LEXICOGRAPHIC (dictionary-order),
    comparing character by character based on each character's Unicode
    code point -- it is NOT numeric, even if the characters happen to be
    digits. "10" vs "9": the first characters are '1' and '9'. Since the
    code point of '1' (49) is less than '9' (57), "10" is considered
    "less than" "9" immediately, without ever looking at the second
    character. This is why numeric strings must be converted with int()
    before doing numeric comparisons.


12. What is the time complexity of string concatenation (+) vs "".join()
    when combining many strings? Why does the difference exist given
    strings are immutable?

    ANSWER: Repeated concatenation with + in a loop is O(n^2) in the
    worst case: since strings are immutable, EVERY += allocates a new
    string and copies all previous characters into it, and this cost
    grows with each iteration. "".join(list_of_strings) is O(n): it can
    calculate the total required length up front and allocate the final
    string buffer ONCE, copying each piece into it a single time. The
    difference exists precisely BECAUSE strings are immutable --
    join() avoids repeated reallocation by doing all the copying in one
    pass instead of n incremental ones.


13. How would you check if a string is a palindrome? How would you handle case-sensitivity and spaces?

    ANSWER: Normalize the string first (lowercase, remove spaces/
    punctuation as needed), then compare it to its reverse:
        def is_palindrome(text):
            cleaned = text.lower().replace(" ", "")
            return cleaned == cleaned[::-1]
    This handles case-insensitivity via .lower() and ignores spaces via
    .replace(" ", "") (you could extend this with a regex to also strip
    punctuation for phrases like "A man, a plan, a canal: Panama").


14. What does str.translate() do, and how is it different/faster than chaining multiple replace() calls?

    ANSWER: str.translate(table) performs BULK character-level
    replacement/removal in a single pass, using a mapping table (built
    with str.maketrans()) that maps character codes to replacement
    characters, other characters, or None (to delete them). It's faster
    than chaining multiple .replace() calls because each replace() call
    is a full separate O(n) scan of the string, so k chained replace()
    calls cost O(k*n); translate() does the equivalent work in a SINGLE
    O(n) pass, regardless of how many character mappings are involved.


15. What's the difference between isdigit(), isnumeric(), and isdecimal()? Give an example where they differ 
    (hint: think Unicode fraction characters or superscripts).

    ANSWER: 
    isdecimal() -> True only for characters that are decimal
    digits usable in base-10 numbers (e.g. '0'-'9'). isdigit() -> True
    for decimal digits AND some additional digit-like characters, such
    as superscripts (e.g. '\u00b2', the superscript '2'). 
    isnumeric() ->
    the broadest check, True for decimal digits, digit-like characters,
    AND numeric characters that aren't digits at all, such as Unicode
    fraction characters (e.g. '\u00bd', the character for "1/2") or
    number words in some scripts.
    Example: '\u00bd'.
    isdecimal() -> False, '\u00bd'.isdigit() -> False,
    '\u00bd'.isnumeric() -> True (the fraction character is "numeric"
    but not a "digit" or "decimal").


16. How is Unicode handled in Python 3 strings compared to Python 2?
    What was the "str vs unicode" split in Python 2 about?

    ANSWER: In Python 3, str is Unicode BY DEFAULT -- every str is a
    sequence of Unicode code points, and there's a separate bytes type
    for raw binary data. In Python 2, str was actually a sequence of
    BYTES (essentially what Python 3 calls bytes), and there was a
    SEPARATE unicode type for text. This caused constant confusion and
    bugs in Python 2 -- mixing str (bytes) and unicode (text) could
    silently work sometimes and raise UnicodeDecodeError/EncodeError
    other times, depending on the data. Python 3's unification (str =
    text, bytes = binary, with explicit encode/decode between them) was
    one of the biggest and most deliberate breaking changes from Python 2.


17. Given a string, how would you count the frequency of each character
    efficiently? What data structure would you use?

    ANSWER: Use collections.Counter, which is a dict subclass built
    exactly for this:
        from collections import Counter
        freq = Counter("hello world")
        # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    This is O(n) time (one pass over the string) and O(k) space, where k
    is the number of distinct characters. A plain dict with manual
    counting works too, but Counter is the idiomatic, optimized choice.


18. What does the `maxsplit` parameter do in split()? Give an example
    use case.

    ANSWER: maxsplit limits the NUMBER of splits performed -- after that
    many splits, the rest of the string is returned as-is in the final
    element, unsplit. Example use case: parsing a "key: value with:
    colons" string where you only want to split on the FIRST colon and
    keep the rest of the value intact:
        "key: value: with: colons".split(":", 1)
        # ['key', ' value: with: colons']


19. How would you remove all occurrences of specific characters from a string efficiently (e.g., removing all vowels)?

    ANSWER: Use str.translate() with a mapping table built via
    str.maketrans("", "", chars_to_remove) -- passing the characters to
    delete as the third argument:
        remove_table = str.maketrans("", "", "aeiou")
        "hello world".translate(remove_table)   # 'hll wrld'
    This does the removal in a single O(n) pass, and is more efficient
    than looping with multiple .replace() calls (one per character) or
    building a new string manually with a list comprehension filter
    (which also works, e.g. "".join(c for c in s if c not in "aeiou"),
    but translate() is typically faster for large strings/many
    characters).


20. What's the difference between `%` formatting, `.format()`, and f-strings? Which is preferred in modern Python and why?

    ANSWER: `%` formatting is the oldest, C-style printf-like syntax
    (e.g. "%s is %d" % (name, age)) -- less readable for complex cases
    and limited in features. .format() (Python 2.6+) is more flexible,
    supports named/positional placeholders and reordering (e.g.
    "{0} is {1}".format(name, age)), but is more verbose. f-strings
    (Python 3.6+) embed expressions DIRECTLY inside the string literal
    (f"{name} is {age}"), and are both the most readable AND the fastest
    at runtime, since the expressions are evaluated inline rather than
    passed as separate arguments. f-strings are the preferred, modern
    approach for nearly all use cases.


21. Can you slice a string with a step value? How would you get every 2nd character, or reverse a string using slicing?

    ANSWER: Yes -- the full slice syntax is s[start:stop:step]. Every
    2nd character: s[::2]. Reverse the whole string: s[::-1] (a negative
    step of -1 walks backward from the end to the start).


22. What happens when you try to do `s[0] = 'X'` on a string? Why does this fail, and how would you achieve 
    the same effect (replacing one character)?

    ANSWER: This raises TypeError: 'str' object does not support item
    assignment, because strings are IMMUTABLE -- there is no way to
    modify a character in place. To achieve the effect of "replacing one
    character," build a NEW string by slicing around the position and
    concatenating the desired character in:
        s = "Hello"
        s = "X" + s[1:]   # "Xello"
    or, for replacing a known character/substring anywhere in the
    string, use s.replace(old, new).


23. How would you check if a string contains only whitespace, or is
    empty vs contains only whitespace? What methods distinguish these
    cases?

    ANSWER: "".isspace() -> False for an EMPTY string (there are no
    characters to be whitespace, so isspace() returns False). " ".isspace()
    -> True for a non-empty, whitespace-only string. To distinguish
    "empty" from "whitespace-only" from "has content", check explicitly:
        if not s:               # True only for the empty string ''
            ...
        elif s.isspace():       # True only for whitespace-only, non-empty strings
            ...
        else:                    # has real content
            ...
    Note the common idiom `if not s.strip():` treats BOTH empty and
    whitespace-only strings the same way (both become falsy after
    stripping) -- use that when you want to treat them identically, and
    the explicit checks above when you need to tell them apart.


24. What's the difference between shallow copying and just reassigning a
    string variable, given strings are immutable? Does copy.copy() even
    make sense for strings?

    ANSWER: Reassigning a variable (b = a) just makes b point to the SAME
    string object as a -- no copy occurs, and none is needed, because
    strings can't be mutated in place anyway; there's no risk of one
    variable's changes affecting the other. copy.copy(a) technically
    works on strings but is essentially a NO-OP / wasted operation --
    since strings are immutable, Python's copy module typically just
    returns the SAME object (or an equal one) rather than allocating a
    genuine duplicate, because making a distinct copy of something that
    can never change would serve no purpose. In practice, you never need
    to explicitly copy a string -- immutability makes copying strings a
    non-issue, unlike mutable types (lists, dicts) where shallow vs deep
    copying is a real, meaningful distinction.
"""

if __name__ == "__main__":
    print(INTERVIEW_QA)