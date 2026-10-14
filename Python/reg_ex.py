"""
Regular Expressions in Python

    Python's re module lets you search, match, and manipulate strings using patterns. Here's a practical rundown.
"""

import re
my_str = 'I am from bangalore and I am from karnataka'

#---------------------------------------------------------------------------------
# match() will find the element only if it is at the beginning of the string
# re.match() — checks for a match only at the start of the string
p = 'I'
match_obj = re.match(p, my_str)
print(match_obj.group(0))       # I

#---------------------------------------------------------------------------------
# search() will return only the first occurrence of the string
# re.search() — finds first match anywhere in the string
a = 'from'
search_obj = re.search(a, my_str)
print(search_obj.group())       # from

#---------------------------------------------------------------------------------
# findall() will return the list of number of times the pattern repeated in the string
# re.findall() — returns all matches as a list
findall_obj = re.findall(a, my_str)
print(findall_obj)      # ['from', 'from']

#---------------------------------------------------------------------------------
# finditer() will return the matched object( combination of search() and findall() )
for match in re.finditer(a, my_str):
    print(match.group())  # .group() will print the matched object

#--------------------------------------------------------------------------------
# re.findall() — returns all matches as a list
out = re.findall(r'\d+', 'I have 42 apples and 7 oranges')
print(out) # ['42', '7']

#---------------------------------------------------------------------------------
# re.compile()
pattern_obj = re.compile("from")
match = pattern_obj.search(my_str)
# match = re.search("from", my_str)
if match:
    print("Found")
else:
    print("Not found")

#---------------------------------------------------------------------------------
# re.sub() — find and replace
re.sub(r'\d+', '#', 'a1 b22 c333')
# 'a# b# c#'

#---------------------------------------------------------------------------------
# re.split() — split a string by a pattern
re.split(r'[,;]', 'a,b;c,d')
# ['a', 'b', 'c', 'd']

#---------------------------------------------------------------------------------
"""
Pattern Syntax Cheat Sheet

Symbol	    Meaning
------      ---------------------------------------------
.	        any character except newline
\d	        digit (0-9)
\D	        non-digit
\w	        word character (letters, digits, underscore)
\W	        non-word character
\s	        whitespace
\S	        non-whitespace
^	        start of string
$	        end of string
*	        0 or more repetitions
+	        1 or more repetitions
?	        0 or 1 repetition (optional)
{n,m}	    between n and m repetitions
[]	        character set, e.g. [aeiou]
[^]	        negated set, e.g. [^0-9]
|	        OR, e.g. cat|dog
()	        grouping / capturing
(?:)	    non-capturing group
"""
'''
# Identifiers
1) \d ->A digit
    ex: file_\d\d -> file_10

2) \w ->Alphanumeric and underscore
    ex: A-B_1 -> \w-\w\w\w

3) \s ->Whitespace character
    ex: a b c -> a\sb\sc

4) \D ->Will matches any non-digit character
    ex: ABC*-+ -> \D\D\D\D\D\D

5) \W -> Will match any special characters that is not digit and alphabet
    ex: *-+& ->\W\W\W\W

6) \S -> Will matches non_whitespace characters
    ex: abc5 -> \S\S\S\S
'''
#---------------------------------------------------------------------------------
# Groups (Capturing Parts of a Match)
m = re.search(r'(\w+)@(\w+)\.com', 'contact: john@example.com')
m.group(0)  # 'john@example.com' (whole match)
m.group(1)  # 'john'
m.group(2)  # 'example'

# Named groups make this more readable:
m = re.search(r'(?P<user>\w+)@(?P<domain>\w+)\.com', 'john@example.com')
m.group('user')    # 'john'
m.group('domain')  # 'example'

#---------------------------------------------------------------------------------
# Compiling Patterns (for reuse/performance)
pattern = re.compile(r'\d+')
pattern.findall('a1 b22')  # ['1', '22']

#---------------------------------------------------------------------------------
# Common Flags
re.search(r'hello', 'HELLO WORLD', re.IGNORECASE)  # matches
re.findall(r'^\w+', 'line1\nline2', re.MULTILINE)  # matches at each line start
re.search(r'a.b', 'a\nb', re.DOTALL)  # . also matches newline

#---------------------------------------------------------------------------------
"""
Raw Strings Matter

    Always use r'...' for regex patterns in Python. Without it, \d, \s, etc. can be misinterpreted as 
    escape sequences (though Python often warns you). r'\d+' is safer and clearer than '\\d+'.
"""
# Quick Real-World Example: Validating an Email
pattern = r'^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$'
re.match(pattern, 'user@example.com')  # matches
re.match(pattern, 'not-an-email')      # None
"""
pattern = r'^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$'
----------------------------------------------------------------------------------
| Part           | Meaning                                  | Example            |
| -------------- | ---------------------------------------- | ------------------ |
| `^`            | Start of the string                      | —                  |
| `[\w.+-]+`     | One or more word chars, `.`, `+`, or `-` | `john.doe+test`    |
| `@`            | Literal `@`                              | `@`                |
| `[\w-]+`       | One or more word chars or `-`            | `gmail`            |
| `\.`           | Literal dot `.`                          | `.`                |
| `[a-zA-Z]{2,}` | At least 2 letters for the ending/TLD    | `com`, `in`, `org` |
| `$`            | End of the string                        | —                  |
----------------------------------------------------------------------------------
john.doe+test@gmail.com
│             │ │    │
│             │ │    └─ [a-zA-Z]{2,} → "com"
│             │ └────── \. → "."
│             └──────── [\w-]+ → "gmail"
└────────────────────── [\w.+-]+ → "john.doe+test"
              @ → literal "@"
              
few important details:

\w generally means word characters: letters, digits, and underscore (_). In Python, it can also match many Unicode letters.
The + after a character class means "one or more":
    [\w.+-]+
So the part before @ cannot be empty.
{2,} means "at least 2", which is why:
    user@example.com   ✅
    user@example.in    ✅
    user@example.c     ❌
The ^ and $ anchors make the regex apply to the whole string, rather than finding an email-like substring inside other text.
"""

#---------------------------------------------------------------------------------------------------------------------
"""
A Few Gotchas
    1. * and + are greedy by default — they'll match as much as possible. Add ? after them (*?, +?) for non-greedy matching.
    2. re.match only checks the beginning, not the whole string — use re.fullmatch if you want the entire string to match.
    3. Special characters like ., *, (, ) need to be escaped with \ if you want them literally, e.g. \. for a literal period.
"""
#---------------------------------------------------------------------------------

'''
# Quantifiers-> Are always used in combination with Identifiers

1) + -> This will matches if the character will occurs one or more time
    ex: A-b12 -> \w-\w+

2) {3} ->This will match the number of characters in the {}
    ex: aaa -> \D{3}
    ex: 1234 -> \d{4}
    
3) {2,4} -> This will match the character in the range specified here in the { , }
    ex: 123 -> \d{2,4}
    ex: 12 -> \d{2,4}
    3x: 1234 -> \d{2,4}
    
4) {3,} -> This will match the character 3 or more times
    ex: 123 -> \w{3,}
    ex: abcder -> \w{3,}
    ex: abc_123 -> \w{3,}
    
5) * -> Matches if it occurs Zero or more times
    ex: AAACC -> A*B*C
    
6) ? -> Matches Zero or None times
    ex: Bikes? -> Bikes/Bike
'''
#----------------------------------------------------------------------------
"""
# Implementation of Identifiers and Quantifiers

Identifiers (special sequences / character classes)
    These are shorthand codes that match specific types of characters.
    example: \d, \w, \s
    
Quantifiers
    These specify how many times the preceding element should repeat
    example: *, +, ?, {n}, {n,}, {n,m}
"""
my_string = "His phone number is 91-080-12948635"

# match = re.search('\d\d-\d\d\d-\d\d\d\d\d\d\d\d',my_string)
match = re.search(r'\d{2}-\d{3}-\d{8}', my_string)
if match:
    print("Found")
    print(match.group())
else:
    print("Not Found")


# Grouping -> is done using: (..) in the search pattern and is used for extracting the specific index
#          -> r'...' raw string is used in the search pattern, this will tell that '\' is not a escape sequence
match = re.search(r'(\d{2})-(\d{3})-(\d{8})', my_string)
if match:
    print(match.group())
    print(match.group(1)) # this will print the first group
    print(match.group(2)) # this will print the second group
    print(match.group(3)) # this will print the third group
else:
    print("Not Found")



# Use of '|' pipe operator, this is used to match the string with multiple names in the same index of the string
match = re.search(r'BMW|KTM','He has KTM')
print(match)
print(match.group())



# '.' operator: will match any character in the string
match1 = re.findall(r'.at', 'The cat here is wearing a hat and sat on splat')
print(match1) # ['cat', 'hat', 'sat', 'lat']

match2 = re.findall(r'..at', 'The cat here is wearing a hat and sat on splat')
print(match2) # [' cat', ' hat', ' sat', 'plat']

match3 = re.findall(r'...at', 'The cat here is wearing a hat and sat on splat')
print(match3) # ['e cat', 'a hat', 'd sat', 'splat']

match4 = re.findall(r'....at', 'The cat here is wearing a hat and sat on splat')
print(match4) # ['he cat', ' a hat', 'nd sat', ' splat']



# '^' will match the string at the beginning
match = re.search(r'^He', 'He works hard')
print(match)



# '$' will match the pattern is occur at the end of the string
match = re.search(r'hard$', 'He works hard')
print(match)



# [] -> Character class: -> will return list of characters
text = 'Finds only huper-words in the sentence. But you do not know how ling-is they are. They can be 2 long'
result1 = re.findall(r'[a-zA-Z]', text)
print(result1)
# ['F', 'i', 'n', 'd', 's', 'o', 'n', 'l', 'y', 'h', 'u', 'p', 'e', 'r', 'w', 'o', 'r', 'd', 's', 'i', 'n', 't', 'h', 'e', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', 'B', 'u', 't', 'y', 'o', 'u', 'd', 'o', 'n', 'o', 't', 'k', 'n', 'o', 'w', 'h', 'o', 'w', 'l', 'i', 'n', 'g', 'i', 's', 't', 'h', 'e', 'y', 'a', 'r', 'e', 'T', 'h', 'e', 'y', 'c', 'a', 'n', 'b', 'e', 'l', 'o', 'n', 'g']

result2 = re.findall(r'[a-zA-Z0-9]+',text)
print(result2)
# ['Finds', 'only', 'huper', 'words', 'in', 'the', 'sentence', 'But', 'you', 'do', 'not', 'know', 'how', 'ling', 'is', 'they', 'are', 'They', 'can', 'be', '2', 'long']

result3 = re.findall(r'[a-zA-Z0-9 ]+',text)
print(result3)
# ['Finds only huper', 'words in the sentence', ' But you do not know how ling', 'is they are', ' They can be 2 long']

result4 = re.findall(r'[a-z]+-[a-z]+',text)
print(result4)
# ['huper-words', 'ling-is']

result4 = re.findall(r'\w+-\w+',text)
print(result4)
# ['huper-words', 'ling-is']

result = re.split(r'\.\s*', text, maxsplit=1)
print(result)
# output: ['Finds only huper-words in the sentence', 'But you do not know how ling-is they are. They can be 2 long']

re.split(r'\.\s*', text)
# Output: ['Finds only huper-words in the sentence', 'But you do not know how ling-is they are', 'They can be 2 long']

text = 'This is a string! But it has. How to remove it?'
res1 = re.findall(r'[!.?]+', text)
res2 = re.findall(r'[^!.?]+',text)
res3 = " ".join(res2)
print(res1) # ['!', '.', '?']
print(res2) # ['This is a string', ' But it has', ' How to remove it']
print(res3) # This is a string  But it has  How to remove it


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. Greedy vs Non-greedy (lazy) quantifiers - a VERY common interview trap
# -------------------------
html = "<b>bold</b> and <i>italic</i>"
greedy = re.findall(r'<.*>', html)         # GREEDY - matches as MUCH as possible
print(greedy)                                # ['<b>bold</b> and <i>italic</i>'] -> matched from FIRST < to LAST >

lazy = re.findall(r'<.*?>', html)             # LAZY (non-greedy) - the '?' after * makes it match as LITTLE as possible
print(lazy)                                     # ['<b>', '</b>', '<i>', '</i>'] -> matches each tag individually

# Same idea applies to +? and {n,m}? - add '?' after ANY quantifier to make it lazy.

print(f"{'*' * 70}")

# -------------------------
# 2. match() vs fullmatch() vs search() - the three entry points, precisely compared
# -------------------------
s = "hello world"
print(re.match(r'hello', s))       # matches -> match() only checks from the START, doesn't need to consume the WHOLE string
print(re.match(r'hello world!', s))  # None -> pattern longer than what's there doesn't match anyway
print(re.fullmatch(r'hello', s))      # None -> fullmatch() requires the ENTIRE string to match the pattern, not just the start
print(re.fullmatch(r'hello world', s)) # matches -> now the WHOLE string matches
print(re.search(r'world', s))            # matches -> search() looks ANYWHERE in the string, not just the start

print(f"{'*' * 70}")

# -------------------------
# 3. Match object methods beyond .group() - span(), start(), end()
# -------------------------
m = re.search(r'from', my_str)
print(m.group())    # 'from' -> the matched text
print(m.start())      # index where the match STARTS
print(m.end())          # index where the match ENDS
print(m.span())           # (start, end) tuple - useful for slicing the original string
print(my_str[m.start():m.end()])   # 'from' -> proves span() gives you exact slice boundaries

print(f"{'*' * 70}")

# -------------------------
# 4. re.sub() with a FUNCTION as the replacement (not just a static string)
# -------------------------
def double_number(match):
    return str(int(match.group()) * 2)

result = re.sub(r'\d+', double_number, 'I have 3 apples and 5 oranges')
print(result)   # 'I have 6 apples and 10 oranges' -> each match is passed to the function individually

# re.sub() also supports BACKREFERENCES in the replacement string, reusing captured groups:
swapped = re.sub(r'(\w+)@(\w+)', r'\2@\1', 'john@example')
print(swapped)   # 'example@john' -> \1 and \2 refer to the captured groups

print(f"{'*' * 70}")

# -------------------------
# 5. re.subn() - like sub(), but ALSO tells you how many replacements were made
# -------------------------
result, count = re.subn(r'\d+', '#', 'a1 b22 c333')
print(result, count)   # 'a# b# c#' 3 -> 3 substitutions were made

print(f"{'*' * 70}")

# -------------------------
# 6. re.split() with CAPTURING groups - the delimiter itself gets INCLUDED in the output
# -------------------------
no_capture = re.split(r'[,;]', 'a,b;c,d')
print(no_capture)     # ['a', 'b', 'c', 'd'] -> delimiters DISCARDED (no capturing group)

with_capture = re.split(r'([,;])', 'a,b;c,d')
print(with_capture)     # ['a', ',', 'b', ';', 'c', ',', 'd'] -> delimiters KEPT in the result,
                           # because the pattern has a capturing group around them

print(f"{'*' * 70}")

# -------------------------
# 7. Lookahead and lookbehind assertions - check context WITHOUT consuming characters
# -------------------------
# Positive lookahead (?=...) - match only if FOLLOWED by something
print(re.findall(r'\d+(?=px)', '10px 20em 30px'))     # ['10', '30'] -> only numbers followed by "px"

# Negative lookahead (?!...) - match only if NOT followed by something
print(re.findall(r'\d+(?!px)', '10px 20em 30px'))       # ['1', '20', '3'] -> tricky! "10" fails (followed by
                                                            # "px"), backtracks to try "1" (followed by "0", not "px" -
                                                            # matches); "20em" fully matches since not followed by "px";
                                                            # "30px" fails, backtracks to "3". Classic gotcha showing
                                                            # \d+ backtracks character-by-character against the lookahead.

# Positive lookbehind (?<=...) - match only if PRECEDED by something
print(re.findall(r'(?<=\$)\d+', 'Price: $100, Discount: 20'))   # ['100'] -> only numbers preceded by '$'

# Negative lookbehind (?<!...) - match only if NOT preceded by something
print(re.findall(r'(?<!\$)\b\d+\b', 'Price: $100, Discount: 20'))   # ['20'] -> numbers NOT preceded by '$'

print(f"{'*' * 70}")

# -------------------------
# 8. Backreferences WITHIN the pattern itself (not just in re.sub replacement)
# -------------------------
# \1 inside the PATTERN refers back to whatever group 1 actually matched -
# useful for finding REPEATED words/values
text_dup = "hello hello world world foo bar"
print(re.findall(r'\b(\w+)\s+\1\b', text_dup))   # ['hello', 'world'] -> finds consecutively DUPLICATED words

print(f"{'*' * 70}")

# -------------------------
# 9. re.VERBOSE flag - writing readable, commented, multi-line regex patterns
# -------------------------
pattern_verbose = re.compile(r"""
    ^(\d{3})    # area code
    -
    (\d{3})     # first 3 digits
    -
    (\d{4})$    # last 4 digits
""", re.VERBOSE)
m = pattern_verbose.match("123-456-7890")
print(m.groups())   # ('123', '456', '7890')
# re.VERBOSE lets you add whitespace and comments INSIDE the pattern for
# readability - whitespace is ignored unless escaped or inside a character class.

print(f"{'*' * 70}")

# -------------------------
# 10. re.escape() - safely treating user input as a LITERAL pattern
# -------------------------
user_input = "3.14 (pi)"    # contains regex special characters: '.' and '(' ')'
escaped_pattern = re.escape(user_input)
print(escaped_pattern)        # '3\\.14\\ \\(pi\\)' -> every special character is escaped
print(re.findall(escaped_pattern, "the value of pi is 3.14 (pi) exactly"))
# ['3.14 (pi)'] -> matches the LITERAL text, instead of '.' meaning "any character"
# CRUCIAL when building a pattern dynamically from user-provided text - without
# re.escape(), special characters in the input could break the regex or cause
# unintended matches.

print(f"{'*' * 70}")

# -------------------------
# 11. Performance: compiling a pattern ONCE vs recompiling on every call
# -------------------------
import time

# Uncompiled - re.search() internally compiles AND CACHES the pattern anyway
# (Python has an internal regex cache), so for a SMALL number of distinct
# patterns, there's little practical difference. But explicitly compiling is
# clearer and avoids relying on the internal cache, especially in a tight
# loop with the SAME pattern used many times:
compiled = re.compile(r'\d+')
start = time.perf_counter()
for _ in range(100000):
    compiled.findall("abc 123 def 456")
print(f"Compiled: {time.perf_counter() - start:.4f}s")

start = time.perf_counter()
for _ in range(100000):
    re.findall(r'\d+', "abc 123 def 456")
print(f"Uncompiled (relies on internal cache): {time.perf_counter() - start:.4f}s")

print(f"{'*' * 70}")

# -------------------------
# 12. Common gotcha: forgetting that match objects are TRUTHY/FALSY, and the
#     "check before calling .group()" pattern (real-world defensive code)
# -------------------------
def safe_extract(pattern, text):
    match = re.search(pattern, text)
    if match:                       # ALWAYS check before calling .group() - avoids AttributeError
        return match.group()
    return None                       # if no match, .group() on None would raise AttributeError

print(safe_extract(r'\d+', 'no numbers here'))   # None -> handled safely
# match_obj.group(0) directly (without the `if match:` check) would raise:
# AttributeError: 'NoneType' object has no attribute 'group'


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON REGULAR EXPRESSIONS (re module)
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is the difference between re.match(), re.search(), and
#    re.fullmatch()? Give a concrete example where each would return a
#    different result for the same string.
#
# 2. What does it mean for a quantifier to be "greedy"? How would you make
#    `.*` lazy/non-greedy instead, and why does this matter when matching
#    HTML-like tags?
#
# 3. What is the difference between re.findall() and re.finditer()? When
#    would you prefer one over the other (hint: think about memory and
#    access to match position information)?
#
# 4. What information do a match object's .start(), .end(), and .span()
#    methods give you, beyond just .group()?
#
# 5. How would you replace matched text using a FUNCTION instead of a static
#    replacement string in re.sub()? Give a use case where this is necessary.
#
# 6. What is the difference between re.sub() and re.subn()?
#
# 7. If your regex pattern in re.split() contains a capturing group around
#    the delimiter, how does the output list change compared to a pattern
#    with no capturing group?
#
# 8. What are lookahead ((?=...), (?!...)) and lookbehind ((?<=...), (?<!...))
#    assertions? How are they different from normal groups in terms of what
#    gets "consumed" in the match?
#
# 9. What is a backreference (\1, \2, etc.) WITHIN a regex pattern (not in the
#    replacement string)? Give an example of using one to detect duplicated
#    consecutive words.
#
# 10. What does the re.IGNORECASE flag do? What about re.MULTILINE and
#     re.DOTALL - how does each change the default matching behavior?
#
# 11. What is re.VERBOSE used for, and why would you use it when writing a
#     complex regex pattern?
#
# 12. Why should you always use raw strings (r'...') when writing regex
#     patterns in Python, instead of normal strings?
#
# 13. What does re.escape() do, and why is it important when building a regex
#     pattern dynamically from user-provided input?
#
# 14. Why does calling .group() on the result of re.search() raise an
#     AttributeError sometimes? What defensive coding pattern avoids this?
#
# 15. What is the practical benefit of using re.compile() to pre-compile a
#     pattern, especially when the SAME pattern is used repeatedly (e.g.,
#     inside a loop processing many lines)?
#
# 16. How would you write a regex to validate an email address? What are the
#     limitations of using a single regex for FULL email validation (hint:
#     think about the full RFC 5322 spec vs a "good enough" practical regex)?
#
# 17. What's the difference between a capturing group `(...)` and a
#     non-capturing group `(?:...)`? Why would you use a non-capturing group?
#
# 18. Given the pattern `r'\d+(?!px)'` matched against `'30px'`, why does it
#     return `['3', '0']` instead of matching nothing at all? What does this
#     reveal about how lookahead assertions actually work character by
#     character?
#
# 19. How would you extract named groups from a match (e.g.,
#     `(?P<user>\w+)@(?P<domain>\w+)`), and why might named groups be
#     preferable to numbered groups `.group(1)`, `.group(2)` in more complex
#     patterns?
#
# 20. What is catastrophic backtracking in regex, and what kind of pattern
#     structure (e.g., nested quantifiers) tends to cause it? Why can this be
#     a real security concern (ReDoS - Regex Denial of Service)?