"""
https://www.shashiworks.com/code-race.html

========= Python ==========
1. Factorial of a number.
2. Write a program in python which returns the gcd of two numbers?
3. Write a program in python which calculates the LCM of two numbers?
4. Write a program in python which finds a letter in a string?
    Example: String = "Example String", letter = "S" returns True.
5. Write a program in python to reverse a string using slicing method?
    Example: String = "helloworld", Returns reversed string = "dlrowolleh"
6. A Caesar Cipher (or Cipher Wheel) is an ancient mechanism for encrypting text and a popular children's toy. It encrypts a message by shifting each alphabetic character in the text by a fixed amount. For example, a Caesar cipher with a shift of 4 translates a to e, b to f etc.
            abcdefghijklmnopqrstuvwxyz
            efghijklmnopqrstuvwxyzabcd
    and would encrypt helloworld as lippsasvph.
    Write a program in python that would, covert a string into Caesar cipher.

7. Return True if the string "cat" and "dog" appear the same number of times in the given string.
8. What's the use of if __name__ == "__main__": in python
9. Fibonacci of 2 numbers using generator
10. Write a program in python which calculates the LCM of two numbers?
11. Program to find square root of a number
12. Program to find factorial of a number
13. Program to find gcd of 2 numbers
14. Program to find lcm of 2 numbers

========== Selenium ===========
1. What are the differences between `findElement()` and `findElements()`?
2. How do you handle dynamic web elements in Selenium?
3. Explain different types of waits used in Selenium.
4. What’s the difference between XPath and CSS Selector?
5. How do you handle multiple windows/tabs in Selenium?
6. How do you design a Page Object Model (POM) framework?

1. Walk me through your automation framework architecture.
2. How do you manage test data and environment configurations?
3. What are your best practices to make automation scripts more maintainable?
4. How do you handle failed test cases in Jenkins or CI/CD pipelines?
5. What’s your strategy for flaky test handling?
6. How do you decide which test cases to automate?
7. Explain your Git-Notes branching strategy or version control workflow.
8. How do you integrate API testing in your automation framework?
9. What are common challenges you faced in automation and how did you resolve them?
10. Have you worked with parallel execution or cross-browser testing tools?
"""

##1.
class A:
    pass
a = A()
print(type(a))
# Output: <class '__main__.A'>
#-----------------------------------------------------------
##2.
class Counter:
	count = 0
	def __init__(self):
		Counter.count += 1
c1 = Counter()
c2 = Counter()
print(Counter.count)
## Output:  2
#-----------------------------------------------------------
## 3.
t = (1, 2, 3)
t[0] = 4
print(t)
# Output: TypeError: 'tuple' object does not support item assignment
#-----------------------------------------------------------
## 4.
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        return x
    return inner()
print(outer())

# Output: 11
#-----------------------------------------------------------
## 5.
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def greet():
    print("Hello")
greet()
'''Output:
Before
Hello
After
'''
#-----------------------------------------------------------
## 6.
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(next(g))

'''
Output:
1
2
'''
#-----------------------------------------------------------
## 7.
class A:
    def __init__(self):
        self.val = 5
    def __str__(self):
        return str(self.val)
a = A()
print(a)

#Output: 5
#-----------------------------------------------------------
## 8.
try:
    raise ValueError("Invalid")
except ValueError as e:
    print(e)

#Output: Invalid
#-----------------------------------------------------------
## 9.
r = lambda q: q * 2
s = lambda q: q * 3
x = 2
x = r(x)
x = s(x)
x = r(x)
print (x)

# Output: 24
#-----------------------------------------------------------
## 10.
class A(object):
    val = 1

class B(A):
    pass

class C(A):
    pass

print (A.val, B.val, C.val)
B.val = 2
print (A.val, B.val, C.val)
A.val = 3
print (A.val, B.val, C.val)
'''
Output:
1 1 1
1 2 1
3 2 3
'''
#-----------------------------------------------------------
## 11.
#Write a function that prints the first N Fibonacci numbers.
#Input: fibonacci(6)
'''
Expected Output:
0 1 1 2 3 5
'''
#-----------------------------------------------------------
## 12.
#Given a sentence, print how many times each word occurs.
#Input:
"the cat and the dog"
'''
Output:
{'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
'''
#-----------------------------------------------------------
## 13.
#Find the most frequent character in a string.
#Input: 'success'

# Expected Output: 's'
#-----------------------------------------------------------
## 14.
#Find all permutations of a given string.
#Input: 'abc'

#Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
#-----------------------------------------------------------
## 15.
#Invert keys and values in a dictionary.
#Input: {'a': 1, 'b': 2}

#Expected Output: {1: 'a', 2: 'b'}
#-----------------------------------------------------------
## 16
String = "Example String"
letter = "S"

if letter in String:
    print("True")
else:
    print("False")

print(String[::-1])

#-----------------------------------------------------------
## 17
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += shifted_char
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged

    return encrypted_text


# Input from the user
message = input("Enter the message to encrypt: ")
shift_amount = int(input("Enter the shift amount: "))

# Encrypting the message
encrypted_message = caesar_cipher_encrypt(message, shift_amount)

print(f"Encrypted Message: {encrypted_message}")

#-----------------------------------------------------------
## 18
def cat_dog_equal_count(text):
    cat_count = text.count("cat")
    dog_count = text.count("dog")
    return cat_count == dog_count

# Input from the user
message = input("Enter a string: ")

# Check if 'cat' and 'dog' appear the same number of times
result = cat_dog_equal_count(message)

print(f"'cat' and 'dog' appear the same number of times: {result}")
#-----------------------------------------------------------
## 19
class B:
    def __init__(self):
        self.x = 1
b = B()
print(b.x)

# Output: 1
#---------------------------------------------------------
##20.
class A:
    def __init__(self):
        print("A init")
class B(A):
    def __init__(self):
	super().__init__()
	print("B init")
b = B()
'''
Output:
A init
B init
'''
#---------------------------------------------------------
##21
s = 'hello'
s[0] = 'H'

#Output: TypeError: 'str' object does not support item assignment

#---------------------------------------------------------
##22.
def f():
    x = 10
    def g():
        print(x)
    x = 20
    return g
f()()

#Output: 20
#---------------------------------------------------------
## 23.
def make_adder(x):
    return lambda y: x + y
add5 = make_adder(5)
print(add5(10))

#Output: 15
#---------------------------------------------------------
## 24.
'''
it = iter([1, 2, 3])
while True:
    print(next(it))

Output:
1
2
3
'''
#---------------------------------------------------------
## 25.
class B:
    def __init__(self):
        self.__val = 10

b = B()
print(b.__val)

#Output: AttributeError: 'B' object has no attribute '__val'. Did you mean: '_B__val'?
#---------------------------------------------------------
## 26.
with 5 as f:
    print(f)

#Output: TypeError: 'int' object does not support the context manager protocol
#---------------------------------------------------------
## 27.
from collections import Counter
print(Counter('aabcc'))

#Output: Counter({'a': 2, 'c': 2, 'b': 1})
#---------------------------------------------------------
## 28.
count = 1
def doThis():

    global count

    for i in (1, 2, 3):
        count += 1
doThis()
print (count)

#Output: 4
#---------------------------------------------------------
## 29.
#Count the number of vowels in a given string. Assume lowercase only.
#Input:
"hello world"

#Output: 3
#---------------------------------------------------------
## 30.
#Given a sentence, print how many times each word occurs.
#Input:
"the cat and the dog"

#Output: {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
#---------------------------------------------------------
## 31.
#Find the longest substring without repeating characters.
#Input: 'abcabcbb'

#Expected Output: 'abc'
#---------------------------------------------------------
## 32.
##Rotate a list to the right by k steps.
#Input: [1,2,3,4,5], k=2

#Expected Output: [4,5,1,2,3]
#---------------------------------------------------------
## 33.
#Find the longest increasing subsequence in a list.
#Input: [10, 9, 2, 5, 3, 7, 101, 18]

#Expected Output: 4
#---------------------------------------------------------

##34.
check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
check2 = check1
check3 = check1[:]

check2[0] = 'Code'
check3[1] = 'Mcq'

count = 0
for c in (check1, check2, check3):
    if c[0] == 'Code':
        count += 1
    if c[1] == 'Mcq':
        count += 10
print (count)

#Output: 12
#---------------------------------------------------------------
## 35.
class A:
    def __init__(self):
        self.val = 1

    def change(self, obj):
        obj.val = 2
a = A()
b = A()
a.change(b)
print(b.val)

#Output: 2
#---------------------------------------------------------------
## 36.

d = {['key']: 'value'}
print(d)

#Output: TypeError: unhashable type: 'list'
#---------------------------------------------------------------
## 4.
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        return x
    return inner()
print(outer())

#Output: 11
#---------------------------------------------------------------
## 37.
def outer():
    x = 1
    def inner():
        return x
    return inner
print(outer()())

#Output: 1
#---------------------------------------------------------------
## 38.
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for i in countdown(3):
    print(i)
'''
Output:
3
2
1
'''
#---------------------------------------------------------------
## 39.
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")
b = B()
'''
Output:
A init
B init
'''
#---------------------------------------------------------------
## 40.
try:
    1 / 0
except ZeroDivisionError:
    print("Cannot divide")
finally:
    print("Done")
'''
Output:
Cannot divide
Done
'''
#---------------------------------------------------------------
## 41.
from collections import defaultdict
d = defaultdict(int)
d['x'] += 1
print(d['x'])

#Output: 1
#---------------------------------------------------------------
## 42.
a = True
b = False
c = False

if not a or b:
    print (1)
elif not a or not b and c:
    print (2)
elif not a or b or not b and a:
    print (3)
else:
    print (4)

#Output: 3
#---------------------------------------------------------------
## 43.
#Given numbers 1 to N with one missing, write code to find the missing number.
#Input: [1, 2, 4, 5]

#Output: 3
#---------------------------------------------------------------
## 44.
#Given a sentence, print how many times each word occurs.
#Input: "the cat and the dog"

#Output: {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
#---------------------------------------------------------------
## 45.
#Remove duplicate characters from a string.
#Input: 'programming'

#Expected Output: 'progamin'
#---------------------------------------------------------------
## 46.
#Check if two strings are anagrams.
#Input: 'listen', 'silent'

#Expected Output: True
#---------------------------------------------------------------
## 47.
#Rotate a list to the right by k steps.
#Input: [1,2,3,4,5], k=2

#Expected Output: [4,5,1,2,3]
