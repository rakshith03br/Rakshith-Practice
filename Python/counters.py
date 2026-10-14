from collections import Counter

"""
Counter: Is used to count how many times each value appears in a list?
        return type is dictionary
"""
def fun():
    w='aabcdeff'
    print(Counter(w))
fun()


def fun():
    l=[1,2,3,4,1,2,3,1,2]
    print(Counter(l))
fun()


arg = Counter(a=10,b=20,c=30)
print(arg)
arg.update(a=5,b=5,c=5)
print(arg)


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. Counter is a subclass of dict - inherits all normal dict behavior
# -------------------------
print(isinstance(Counter(), dict))   # True

print(f"{'*' * 50}")

# -------------------------
# 2. Accessing a missing key -> returns 0 instead of raising KeyError
#    (this is the SINGLE most important thing that separates Counter from dict)
# -------------------------
c = Counter("aab")
print(c['a'])    # 2
print(c['z'])    # 0 -> normal dict would raise KeyError here!
print('z' in c)  # False -> the missing-key lookup does NOT add 'z' to the Counter
print(len(c))     # 2 -> only counts keys that actually exist

print(f"{'*' * 50}")

# -------------------------
# 3. most_common(n) - the most frequently asked Counter method in interviews
# -------------------------
word_list = ['apple', 'banana', 'apple', 'orange', 'apple', 'banana']
count = Counter(word_list)
print(count.most_common())      # [('apple', 3), ('banana', 2), ('orange', 1)] -> ALL items, sorted by count desc
print(count.most_common(1))      # [('apple', 3)] -> top 1
print(count.most_common(2))       # top 2

# Ties are broken by INSERTION ORDER (first-seen order), not alphabetically
tie_example = Counter(['b', 'a', 'a', 'b'])
print(tie_example.most_common())   # [('b', 2), ('a', 2)] -> 'b' seen first, so it comes first on tie

print(f"{'*' * 50}")

# -------------------------
# 4. update() vs directly re-assigning - update() ADDS to existing counts
# -------------------------
c = Counter(a=1, b=2)
c.update(a=10)     # ADDS 10 to existing count of 'a', doesn't replace it
print(c)             # Counter({'a': 11, 'b': 2})

c.update(['a', 'a', 'c'])   # can also update from an iterable, not just kwargs
print(c)                      # Counter({'a': 13, 'b': 2, 'c': 1})

# common mistake: thinking update() REPLACES counts (it doesn't - it ADDS)
print(f"{'*' * 50}")

# -------------------------
# 5. subtract() - decreases counts, allows negative results (unlike '-' operator)
# -------------------------
c1 = Counter(a=3, b=1, c=5)
c2 = Counter(a=1, b=2)
c1.subtract(c2)
print(c1)   # Counter({'c': 5, 'a': 2, 'b': -1}) -> 'b' went negative, subtract() allows this

print(f"{'*' * 50}")

# -------------------------
# 6. Arithmetic operators: +, -, &, | (these DROP non-positive results, unlike subtract())
# -------------------------
a = Counter(x=3, y=1)
b = Counter(x=1, y=2, z=5)

print(a + b)    # Counter({'y': 3, 'x': 4, 'z': 5}) -> adds counts
print(a - b)    # Counter({'x': 2}) -> only keeps POSITIVE results; 'y' (1-2=-1) is dropped entirely!
print(a & b)    # Counter({'x': 1, 'y': 1}) -> intersection: takes the MIN of each shared key
print(a | b)    # Counter({'z': 5, 'x': 3, 'y': 2}) -> union: takes the MAX of each key

print(f"{'*' * 50}")

# -------------------------
# 7. elements() - expands the Counter back into individual items
# -------------------------
c = Counter(a=3, b=2, c=0, d=-1)
print(list(c.elements()))   # ['a', 'a', 'a', 'b', 'b'] -> zero and negative counts are SKIPPED

print(f"{'*' * 50}")

# -------------------------
# 8. total() - sum of all counts (Python 3.10+)
# -------------------------
c = Counter(a=3, b=2, c=1)
print(c.total())   # 6 -> sum of all the values (equivalent to sum(c.values()))

print(f"{'*' * 50}")

# -------------------------
# 9. Converting Counter to other structures
# -------------------------
c = Counter(a=3, b=1)
print(dict(c))          # {'a': 3, 'b': 1} -> plain dict (loses most_common/Counter-specific methods)
print(list(c))           # ['a', 'b'] -> just the keys, like iterating a normal dict
print(sorted(c))          # ['a', 'b'] -> sorted keys
print(sorted(c.items()))   # [('a', 3), ('b', 1)] -> sorted (key, count) pairs

print(f"{'*' * 50}")

# -------------------------
# 10. Practical interview-style problems using Counter
# -------------------------
# Problem: find the most frequent character in a string
def most_frequent_char(s):
    return Counter(s).most_common(1)[0]

print(most_frequent_char("mississippi"))   # ('i', 4)

# Problem: check if two strings are anagrams using Counter
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)     # Counter equality compares counts, ignores order

print(is_anagram("listen", "silent"))     # True
print(is_anagram("hello", "world"))         # False

# Problem: find all unique elements that appear more than once
def find_duplicates(items):
    counts = Counter(items)
    return [item for item, cnt in counts.items() if cnt > 1]

print(find_duplicates([1, 2, 2, 3, 3, 3, 4]))   # [2, 3]

# Problem: word frequency from a sentence, ignoring case
def word_frequency(sentence):
    return Counter(sentence.lower().split())

print(word_frequency("The Cat sat on the mat the CAT ran"))
# Counter({'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1, 'ran': 1})


## ==========================================================
## INTERVIEW QUESTIONS ON collections.Counter
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is Counter, and what does it return when you access a key that
#    doesn't exist? How is this different from a regular dict?
#
# 2. Does accessing a missing key in a Counter (e.g., counter['missing']) add
#    that key to the Counter? How would you verify this?
#
# 3. What does most_common(n) return, and what is its time complexity for
#    large Counters? How are ties between equal counts broken?
#
# 4. What is the difference between Counter.update() and simply reassigning a
#    key's count (e.g., counter['a'] = 5)?
#
# 5. What is the difference between the '-' operator and the subtract() method
#    on two Counters? Which one allows negative results?
#
# 6. What do the '&' and '|' operators do when applied to two Counters? What
#    real-world problem could these solve (hint: think inventory/set-like
#    counting problems)?
#
# 7. What does elements() return, and what happens to keys with a zero or
#    negative count when you call it?
#
# 8. How would you use Counter to check if two strings are anagrams of each
#    other? What's the time complexity of this approach compared to sorting
#    both strings?
#
# 9. How would you find the top-K most frequent elements in a very large
#    dataset (e.g., millions of log lines) efficiently using Counter?
#
# 10. What does Counter.total() do (Python 3.10+), and how would you compute
#     the same thing on an older Python version?
#
# 11. Can you initialize a Counter directly from keyword arguments (like
#     Counter(a=1, b=2)) as well as from an iterable? What are all the valid
#     ways to construct one?
#
# 12. If you convert a Counter to a plain dict using dict(counter), what
#     functionality do you lose?
#
# 13. How does Counter equality (==) work? Does it care about the order items
#     were counted in?
#
# 14. How would you merge counts from two different Counters representing,
#     say, word counts from two different documents?
#
# 15. What's the underlying data structure/time complexity for looking up a
#     count in a Counter? (Hint: think about what Counter is built on top of.)
#
# 16. Given a list of numbers, how would you find all elements that appear
#     exactly once (as opposed to more than once) using Counter?
#
# 17. Is Counter hashable itself? Could you use a Counter object as a
#     dictionary key or a set member?
#
# 18. How would you sort a Counter's items by count in ascending order instead
#     of the default descending order that most_common() gives you?
#
# 19. What happens if you call most_common() with n greater than the number of
#     unique keys in the Counter? Does it raise an error?
#
# 20. How would you use Counter to efficiently detect if one string can be
#     formed by rearranging the letters of another (permutation check), and
#     what's the time and space complexity of that approach?