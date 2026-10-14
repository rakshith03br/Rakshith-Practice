"""
__init__() — the constructor ?

__init__ is a special method that Python automatically runs whenever you create a new object from the class.
    It's short for "initialize" — its job is to set up the initial state of the object.
__init__ (simply meaning 'initialize') is a special method that is called immediately after an instance
    of a class is created. It's the equivalent of the constructor in other languages such as C#.
python
    emp1 = Employee(101, "Alice", 50000)
The moment you write this line, Python:
    1. Creates a new, empty Employee object
    2. Immediately calls __init__(emp1, 101, "Alice", 50000) behind the scenes
    3. Inside __init__, those values get stored onto the object
---------------------------------------------------------------------------------------------------------
self ?

In Python, 'self' represents the specific instance of the class that you are currently working with.
    It acts as a reference tool, allowing each object created from a class template to access, store,
    and manipulate its own unique data and methods independently.
How self Works
    When you define an instance method inside a class, you must explicitly include 'self' as the first
    parameter. However, when you actually call the method on an object, Python automatically passes
    the object into that parameter behind the scenes
---------------------------------------------------------------------------------------------------------
(self, id, name, salary) ?

All these are parameters in constructor
---------------------------------------------------------------------------------------------------------
What "inheritance" means here ?

Inheritance lets Developer reuse everything Employee already has (id, name, salary, and their getter methods)
    without rewriting that code, while also adding its own extra stuff (language, place).
Think of it like: "A Developer IS an Employee, plus a bit more."
---------------------------------------------------------------------------------------------------------
super() ?

In Python, super() is a built-in function used to access and call methods from a parent (or sibling) class
    from within a child class. It returns a temporary proxy object of the parent class, allowing you to reuse
    and extend inherited functionality instead of rewriting it
super() gives you a reference to the parent (base) class, so you can call its methods from inside
    the child class — most commonly its __init__.
super() isn't limited to __init__ — you can use it to call any method from the parent class, e.g. super().get_id().
It avoids code duplication and keeps things DRY (Don't Repeat Yourself).
In short: super() = "go ask the parent class to do this part for me."

---------------------------------------------------------------------------------------------------------
Summary of the concept ?

Concept	                    What it means in this code
--------------------        -----------------------------------------------------------------------------
Base class	                Employee — general, reusable code
Derived class	            Developer — specific, adds/extends behavior
super().__init__()	        Reuses the parent's setup logic instead of duplicating it
Inherited methods	        get_name(), get_salary() work on Developer objects without being rewritten
Method overriding	        get_id() is redefined in Developer to behave differently
"""

class Employee: # Base class

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    @property
    def get_salary(self):
        return self.salary


class Developer(Employee): # Derived class
    # Writing Employee inside the parentheses means "Developer inherits from Employee."

    def __init__(self, id, name, salary, language, place):
        super().__init__(id, name, salary) # super is used to call __init__ method of the base class
        '''
            super() refers to the base class (Employee). So super().__init__(id, name, salary) calls 
                Employee's __init__, which sets self.id, self.name, self.salary — exactly like it would for a plain Employee.
            Then the Developer.__init__ continues and adds two more attributes: self.language and self.place.
            So a Developer object ends up with 5 attributes total: id, name, salary (inherited) + language, place (new).
        '''
        self.language = language
        self.place = place

    def get_language(self):
        return self.language

    def get_place(self):
        return self.place

    def get_id(self):
        '''
            method overriding with same method name with different functionality
            Employee already has a get_id() method. Developer redefines it with different behavior. This is called method overriding.
            When you call d.get_id(), Python uses Developer's version (not Employee's), because Python always checks
                the most specific class first. So:
            python
                print(d.get_id())  # Developer: 1   ← uses Developer's overridden version
        '''
        return 'Developer: ' + str(self.id)


d = Developer(1, 'Rakshith', 5000, 'python', 'Bangalore')
print(d.get_id()) # Developer: 1   ← uses Developer's overridden version
print(d.get_language())
print(d.get_place())
print(d.get_name())
print(d.get_salary)


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION
## ==========================================================
# Your file covers inheritance, super(), and method overriding very well.
# The 4 pillars of OOP are: Encapsulation, Inheritance, Polymorphism, and
# Abstraction. Below fills in the pillars/mechanics not yet covered.

# -------------------------
# 1. isinstance() proving the "IS-A" relationship from inheritance
# -------------------------
print(isinstance(d, Developer))    # True
print(isinstance(d, Employee))      # True -> a Developer IS ALSO an Employee (inheritance chain)
print(isinstance(d, object))          # True -> EVERY class implicitly inherits from 'object'
print(Developer.__bases__)             # (<class '__main__.Employee'>,) -> shows direct parent(s)
print(Developer.__mro__)                # Method Resolution Order: (Developer, Employee, object)

print(f"{'*' * 70}")

# -------------------------
# 2. Encapsulation - protecting internal state (the pillar this file doesn't
#    cover yet) - public, protected (_), private (__) conventions
# -------------------------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner              # public - accessible from anywhere
        self._account_type = "savings"    # protected (convention) - "internal use", not enforced by Python
        self.__pin = "1234"                 # private (name-mangled) - harder to access from outside

    def verify_pin(self, pin):
        return pin == self.__pin              # accessible from INSIDE the class

acc = BankAccount("Alice", 1000)
print(acc.owner)              # Alice -> fine, public
print(acc._account_type)        # savings -> works, but convention says don't touch this externally
# print(acc.__pin)                # AttributeError! Python "name mangles" __pin to _BankAccount__pin
print(acc._BankAccount__pin)      # '1234' -> proves it's not TRUE privacy, just mangled
print(acc.verify_pin("1234"))       # True -> the PROPER way to check the private value

print(f"{'*' * 70}")

# -------------------------
# 3. Polymorphism - same method name, different behavior across classes
#    (your get_id() override IS polymorphism, but here's the classic "same
#    interface, different implementations" version too)
# -------------------------
class Manager(Employee):
    def get_id(self):
        return 'Manager: ' + str(self.id)

developer = Developer(1, "Rakshith", 5000, "Python", "Bangalore")
manager = Manager(2, "Priya", 9000)

for emp in [developer, manager]:        # same interface (get_id), different behavior per class
    print(emp.get_id())                   # Developer: 1 / Manager: 2 -> polymorphism in action

print(f"{'*' * 70}")

# -------------------------
# 4. Duck typing - Python's informal/dynamic take on polymorphism
# -------------------------
# "If it walks like a duck and quacks like a duck, it's a duck" - Python
# doesn't require a common base class or interface to treat two objects
# the same way, as long as they support the same method/attribute:
class Duck:
    def sound(self):
        return "Quack"

class Dog:
    def sound(self):
        return "Woof"

def make_it_speak(animal):
    print(animal.sound())   # doesn't care about the CLASS, only that .sound() exists

make_it_speak(Duck())   # Quack
make_it_speak(Dog())      # Woof -> Dog has NO inheritance relationship to Duck at all!

print(f"{'*' * 70}")

# -------------------------
# 5. Abstraction - hiding implementation details behind a simple interface,
#    enforced formally with the abc module
# -------------------------
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Every subclass MUST implement this - Shape itself can't be instantiated."""
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

# shape = Shape()          # TypeError: Can't instantiate abstract class Shape with abstract method area
rect = Rectangle(4, 5)
print(rect.area())          # 20 -> caller doesn't need to know HOW area is calculated, just that it IS

print(f"{'*' * 70}")

# -------------------------
# 6. Class variables vs instance variables (a common gotcha not shown yet)
# -------------------------
class Counter:
    total_employees = 0    # CLASS variable - shared across ALL instances

    def __init__(self, name):
        self.name = name       # INSTANCE variable - unique per object
        Counter.total_employees += 1   # modifies the SHARED class-level counter

e1 = Counter("Alice")
e2 = Counter("Bob")
print(Counter.total_employees)    # 2 -> shared across both instances

print(f"{'*' * 70}")

# -------------------------
# 7. @staticmethod and @classmethod - the other method types besides
#    instance methods (this file only shows instance methods so far)
# -------------------------
class MathHelper:
    @staticmethod
    def add(a, b):
        """No access to self/cls - just a plain function grouped in the class."""
        return a + b

    @classmethod
    def create_default(cls):
        """Alternative constructor pattern - receives the class itself (cls), not an instance."""
        return cls()

print(MathHelper.add(2, 3))   # 5 -> called directly on the class, no instance needed

print(f"{'*' * 70}")

# -------------------------
# 8. Multiple inheritance and the Diamond Problem (Python resolves this via
#    MRO / C3 linearization, unlike languages with no multiple inheritance)
# -------------------------
class Base:
    def who(self):
        return "Base"

class Left(Base):
    def who(self):
        return "Left"

class Right(Base):
    def who(self):
        return "Right"

class Diamond(Left, Right):   # inherits from BOTH Left and Right
    pass

print(Diamond().who())   # 'Left' -> Python's MRO picks Left first (declared first in Diamond(Left, Right))
print(Diamond.__mro__)     # shows the exact resolution order Python computed

print(f"{'*' * 70}")

# -------------------------
# 9. Operator overloading - customizing what +, ==, etc. do for your own
#    class (a form of polymorphism, via dunder/"magic" methods)
# -------------------------
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):          # defines behavior for the + operator
        return Money(self.amount + other.amount)

    def __eq__(self, other):             # defines behavior for the == operator
        return self.amount == other.amount

    def __repr__(self):                    # defines what shows up when you print() the object
        return f"Money({self.amount})"

m1 = Money(100)
m2 = Money(50)
print(m1 + m2)      # Money(150) -> uses __add__
print(m1 == Money(100))   # True -> uses __eq__, not default identity comparison

print(f"{'*' * 70}")

# -------------------------
# 10. Composition ("has-a") as an alternative to inheritance ("is-a")
# -------------------------
# Sometimes composition is a BETTER design choice than inheritance, especially
# when the relationship isn't a true "is-a" (e.g., an Employee HAS AN Address,
# rather than an Employee IS AN Address).
class Address:
    def __init__(self, city, pincode):
        self.city = city
        self.pincode = pincode

class EmployeeWithAddress:
    def __init__(self, name, address: Address):
        self.name = name
        self.address = address   # composition - EmployeeWithAddress "HAS-A" Address

emp_addr = EmployeeWithAddress("Alice", Address("Bangalore", 560001))
print(emp_addr.address.city)   # Bangalore

print(f"{'*' * 70}")

# -------------------------
# 11. property setter with validation (your file uses @property but only for
#     a read-only getter - here's the writable/validated version)
# -------------------------
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

p = Product(100)
print(p.price)         # 100 -> looks like an attribute, calls the getter method
p.price = 150             # calls the setter (with validation) - looks like plain assignment
print(p.price)              # 150
try:
    p.price = -10               # triggers validation
except ValueError as e:
    print("Validation error:", e)


## ==========================================================
## INTERVIEW QUESTIONS ON OOP CONCEPTS (INHERITANCE, POLYMORPHISM, etc.)
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What are the four pillars of Object-Oriented Programming? Briefly
#    describe what each one means using this file's Employee/Developer
#    example.
#
# 2. What does super().__init__(id, name, salary) actually do? Why is it
#    preferred over directly calling Employee.__init__(self, id, name, salary)?
#
# 3. What is method overriding? How is it different from method overloading,
#    and does Python support true method overloading like Java/C++?
#
# 4. What is polymorphism? How does the get_id() override in Developer
#    demonstrate polymorphism in practice?
#
# 5. What is "duck typing," and how does it relate to (but differ from)
#    traditional polymorphism achieved through inheritance?
#
# 6. What is encapsulation? What's the difference between a single
#    underscore (_var) and double underscore (__var) attribute naming
#    convention in Python?
#
# 7. Is Python's double-underscore "private" attribute truly private? What is
#    "name mangling," and how would you access a mangled attribute from
#    outside the class (even though you normally shouldn't)?
#
# 8. What is abstraction, and how does the `abc` module (ABC,
#    @abstractmethod) enforce it? What happens if you try to instantiate a
#    class with an unimplemented abstract method?
#
# 9. What is the difference between a class variable and an instance
#    variable? What happens if you modify a class variable through an
#    instance vs through the class itself?
#
# 10. What are @staticmethod and @classmethod used for? How is a classmethod
#     commonly used as an "alternative constructor"?
#
# 11. Can a Python class inherit from multiple base classes at once? What is
#     the "diamond problem," and how does Python's MRO (Method Resolution
#     Order) resolve it deterministically?
#
# 12. What does Class.__mro__ show you, and what algorithm does Python use to
#     compute it?
#
# 13. What is operator overloading? How would you make a custom class support
#     the + operator, and which dunder method would you implement?
#
# 14. What's the difference between composition ("has-a") and inheritance
#     ("is-a")? Give an example of when you'd prefer composition, even though
#     inheritance seems possible.
#
# 15. In this file's Developer class, why does self.language and self.place
#     need to be set AFTER calling super().__init__(...), rather than before?
#
# 16. What is the difference between isinstance(d, Employee) and
#     type(d) == Employee, given that d is a Developer object?
#
# 17. What does @property do, and how would you add validation logic when a
#     value is ASSIGNED to a property (not just read)?
#
# 18. If both a parent class and a child class define __init__, and the child
#     class's __init__ does NOT call super().__init__(), what happens to the
#     parent's initialization logic?
#
# 19. What is the difference between overriding __eq__ vs relying on Python's
#     default equality behavior for custom objects?
#
# 20. Why does every Python class implicitly inherit from `object`? What
#     built-in behavior does this give every class "for free" (hint: think
#     about __repr__, __hash__, __eq__ defaults)?