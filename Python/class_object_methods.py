class Calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b

# class_object = class_name
cal = Calculator()

# result = class_object.function_name
res1 = cal.add(10, 20)
print(res1)

# result = class_object.function_name
res2 = cal.sub(25, 7)
print(res2)

############################
# Extending classes
class class1:
    var1 = "Var1"

class class2:
    var2 = "Var2"

class class3(class1, class2):
    var3 = "Var3"

obj = class3()

print(obj.var1)
print(obj.var2)
print(obj.var3)


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION
## ==========================================================

# -------------------------
# 1. __init__ constructor - initializing objects with data
# -------------------------
# Your Calculator class has no state (no data specific to an instance).
# __init__ is the constructor, called automatically when you create an object.
class Employee:
    def __init__(self, name, salary):
        self.name = name        # instance attribute - unique to each object
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        return self.salary

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)
print(e1.name, e1.salary)   # Alice 50000
print(e2.name, e2.salary)   # Bob 60000
e1.give_raise(5000)
print(e1.salary, e2.salary) # 55000 60000 -> e2 unaffected, separate instance state

print(f"{'*' * 50}")

# -------------------------
# 2. Instance variables vs Class variables (COMMON interview gotcha)
# -------------------------
class Counter:
    total_count = 0    # CLASS variable - shared across ALL instances

    def __init__(self):
        self.id = Counter.total_count   # instance variable - unique per object
        Counter.total_count += 1        # modifies the class-level value

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(c1.id, c2.id, c3.id)          # 0 1 2 -> each instance got a different id
print(Counter.total_count)           # 3     -> shared counter tracks all instances

# DANGER: mutable class variables are shared and can cause bugs, similar to
# mutable default arguments!
class BuggyBasket:
    items = []   # class variable - SHARED list across all instances!
    def add(self, item):
        self.items.append(item)   # modifies the SHARED class list

b1 = BuggyBasket()
b2 = BuggyBasket()
b1.add("apple")
print(b2.items)   # ['apple'] -> BUG! b2 sees b1's item because items is shared

print(f"{'*' * 50}")

# -------------------------
# 3. self - what it actually is
# -------------------------
# 'self' refers to the instance the method is being called on.
# cal.add(10, 20) is really Calculator.add(cal, 10, 20) under the hood.
print(Calculator.add(cal, 10, 20))   # 30 -> proves 'self' is just the instance, passed explicitly

print(f"{'*' * 50}")

# -------------------------
# 4. Instance methods vs Class methods vs Static methods
# -------------------------
class MyMath:
    pi = 3.14159

    def instance_method(self):
        # takes 'self' - can access/modify instance state AND class state
        return f"instance method, self={self}"

    @classmethod
    def class_method(cls):
        # takes 'cls' - can access/modify CLASS state, not tied to any instance
        return f"class method, cls={cls}, pi={cls.pi}"

    @staticmethod
    def static_method(x, y):
        # takes neither self nor cls - just a regular function namespaced inside the class
        return x + y

m = MyMath()
print(m.instance_method())
print(MyMath.class_method())     # can call on the class directly, no instance needed
print(m.class_method())          # can also call on an instance
print(MyMath.static_method(2, 3))  # 5 -> no self/cls needed at all

# Common real-world use of classmethod: alternative constructors
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        """Alternative constructor - a factory method."""
        return cls(["mozzarella", "tomato"])

pizza = Pizza.margherita()
print(pizza.toppings)   # ['mozzarella', 'tomato']

print(f"{'*' * 50}")

# -------------------------
# 5. Inheritance - single inheritance and method overriding
# -------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):   # OVERRIDES the parent's speak() method
        return f"{self.name} says Woof!"

class Cat(Animal):
    pass   # no override -> inherits speak() from Animal as-is

dog = Dog("Rex")
cat = Cat("Whiskers")
print(dog.speak())   # Rex says Woof!
print(cat.speak())   # Whiskers makes a sound

print(f"{'*' * 50}")

# -------------------------
# 6. super() - calling the parent class's method (extend, don't fully replace)
# -------------------------
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)   # calls Vehicle.__init__ to set make/model
        self.doors = doors

    def describe(self):
        base = super().describe()        # reuse parent's logic
        return f"{base} with {self.doors} doors"

car = Car("Toyota", "Corolla", 4)
print(car.describe())   # Toyota Corolla with 4 doors

print(f"{'*' * 50}")

# -------------------------
# 7. Multiple inheritance and Method Resolution Order (MRO) - important for
#    understanding your class3(class1, class2) example
# -------------------------
print(class3.__mro__)
# (<class '__main__.class3'>, <class '__main__.class1'>, <class '__main__.class2'>, <class 'object'>)
# MRO uses the C3 linearization algorithm. In simple terms: Python searches
# left to right through the base classes as listed in the class definition.

class A:
    def greet(self):
        return "Hello from A"

class B:
    def greet(self):
        return "Hello from B"

class C(A, B):   # A is listed FIRST, so A's method wins on conflict
    pass

print(C().greet())    # Hello from A -> because A comes before B in class C(A, B)
print(C.__mro__)

print(f"{'*' * 50}")

# -------------------------
# 8. The Diamond Problem - classic multiple inheritance interview question
# -------------------------
class Base:
    def who_am_i(self):
        return "Base"

class Left(Base):
    def who_am_i(self):
        return "Left"

class Right(Base):
    def who_am_i(self):
        return "Right"

class Diamond(Left, Right):
    pass   # inherits from both Left and Right, which both inherit from Base

print(Diamond().who_am_i())   # 'Left' -> MRO resolves this deterministically via C3 linearization
print(Diamond.__mro__)
# (Diamond, Left, Right, Base, object) -> Base appears ONLY ONCE, even though
# it's a common ancestor of both Left and Right (avoids the classic diamond
# ambiguity seen in some other languages like C++).

print(f"{'*' * 50}")

# -------------------------
# 9. isinstance() vs type() vs issubclass()
# -------------------------
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True -> isinstance checks the WHOLE inheritance chain
print(type(dog) == Dog)          # True
print(type(dog) == Animal)       # False -> type() checks EXACT class only, not ancestors
print(issubclass(Dog, Animal))   # True
print(issubclass(Animal, Dog))   # False

print(f"{'*' * 50}")

# -------------------------
# 10. Encapsulation: public, protected (_), and private (__) conventions
# -------------------------
class BankAccount:
    def __init__(self, balance):
        self.balance = balance       # public - accessible from anywhere
        self._pin = "1234"           # protected (convention only) - "internal use", not enforced
        self.__secret_key = "XYZ"    # private - triggers name mangling

    def get_secret(self):
        return self.__secret_key     # accessible from INSIDE the class

acc = BankAccount(1000)
print(acc.balance)     # 1000 -> fine, public
print(acc._pin)         # "1234" -> works, but convention says "don't touch this from outside"
# print(acc.__secret_key)   # AttributeError! name mangling makes this inaccessible directly
print(acc._BankAccount__secret_key)   # "XYZ" -> name mangling: __secret_key becomes _ClassName__secret_key
print(acc.get_secret())                # "XYZ" -> proper way to access it

print(f"{'*' * 50}")

# -------------------------
# 11. @property - controlled attribute access (getters/setters, Pythonic way)
# -------------------------
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        """Looks like an attribute, but computed on access."""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Allows setting via the same 'attribute-like' syntax, with validation."""
        self._celsius = (value - 32) * 5 / 9

temp = Temperature(25)
print(temp.fahrenheit)    # 77.0 -> called like an attribute, no parentheses!
temp.fahrenheit = 100
print(temp._celsius)       # 37.77... -> setter converted and stored it

print(f"{'*' * 50}")

# -------------------------
# 12. Dunder (magic) methods - customize built-in behavior
# -------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Used by repr() and in the interactive shell/debugger - unambiguous."""
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        """Used by str()/print() - human-readable."""
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        """Defines behavior for == comparisons."""
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        """Defines behavior for the + operator."""
        return Point(self.x + other.x, self.y + other.y)

    def __len__(self):
        """Defines behavior for len()."""
        return 2

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)             # (1, 2)          -> uses __str__
print(repr(p1))        # Point(1, 2)     -> uses __repr__
print(p1 == Point(1, 2))  # True         -> uses __eq__, NOT default identity check
print(p1 + p2)          # Point(4, 6)    -> uses __add__
print(len(p1))           # 2             -> uses __len__

print(f"{'*' * 50}")

# -------------------------
# 13. Abstract classes - enforcing an interface (using the abc module)
# -------------------------
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Subclasses MUST implement this method."""
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

# shape = Shape()          # TypeError: Can't instantiate abstract class Shape
rect = Rectangle(4, 5)
print(rect.area())          # 20

print(f"{'*' * 50}")

# -------------------------
# 14. Composition over inheritance (design principle, often discussed at 4 YOE)
# -------------------------
# "has-a" relationship instead of "is-a" - generally more flexible than deep
# inheritance hierarchies.
class Engine:
    def start(self):
        return "Engine started"

class Car2:
    def __init__(self):
        self.engine = Engine()   # Car2 HAS an Engine, rather than inheriting from it

    def start(self):
        return self.engine.start()

print(Car2().start())   # Engine started

print(f"{'*' * 50}")

# -------------------------
# 15. Class attributes accessed/checked via __dict__ and vars()
# -------------------------
print(e1.__dict__)     # {'name': 'Alice', 'salary': 55000} -> instance's own attributes
print(Counter.__dict__.keys())  # shows class-level attributes/methods (and more)


## ==========================================================
## INTERVIEW QUESTIONS ON CLASSES, OBJECTS & OOP CONCEPTS
## ==========================================================

# 1. What is the difference between an instance variable and a class variable?
#    What happens if a class variable is mutable (e.g., a list) and shared across
#    instances?
#
# 2. What is 'self' in Python, and why must it be explicitly listed as the first
#    parameter of instance methods (unlike 'this' in Java/C++, which is implicit)?
#
# 3. What is the difference between an instance method, a classmethod (@classmethod),
#    and a staticmethod (@staticmethod)? Give a real use case for each.
#
# 4. What is a common use case for @classmethod as an "alternative constructor"?
#
# 5. Explain the Method Resolution Order (MRO) in Python. What algorithm does
#    Python use to compute it (C3 linearization), and how do you inspect it?
#
# 6. What is the "diamond problem" in multiple inheritance? How does Python's MRO
#    resolve it without ambiguity?
#
# 7. What does super() do, and why would you use it in __init__ instead of calling
#    the parent class directly (e.g., ParentClass.__init__(self, ...))?
#
# 8. What is the difference between isinstance(), type(), and issubclass()? When
#    would type() give a different answer than isinstance()?
#
# 9. What is name mangling in Python (double underscore prefix, e.g. __secret)?
#    Is it true "private" access like in Java, or just a convention?
#
# 10. What's the difference between a single underscore prefix (_var) and a
#     double underscore prefix (__var) for attributes?
#
# 11. What does the @property decorator do? How would you create a computed,
#     read-only attribute using it?
#
# 12. What is the difference between __str__ and __repr__? What's the convention
#     if a class doesn't define __str__ but does define __repr__?
#
# 13. How does Python decide what == does for custom objects? What happens if you
#     don't override __eq__?
#
# 14. What are abstract base classes (ABC) used for? What happens if you try to
#     instantiate a class with an unimplemented @abstractmethod?
#
# 15. What is the difference between composition and inheritance? When would you
#     prefer "has-a" over "is-a" in a design?
#
# 16. What is the purpose of __init__ vs __new__? Which one actually creates the
#     object, and which one initializes it?
#
# 17. Can a Python class inherit from multiple classes at once? What issues can
#     arise, and how does listing base classes in a particular order matter?
#
# 18. What is the difference between calling a method on the class itself
#     (e.g., Calculator.add(cal, 10, 20)) versus calling it on an instance
#     (cal.add(10, 20))? What is actually happening under the hood?
#
# 19. How would you make an attribute read-only from outside the class, but
#     still modifiable internally?
#
# 20. What does obj.__dict__ show you, and how is it different from
#     ClassName.__dict__?
#
# 21. What is a mixin class? How is it different from typical inheritance, and
#     when would you use one?
#
# 22. If a class doesn't define __eq__, what does `obj1 == obj2` compare by
#     default?
#
# 23. What's the difference between overriding a method and overloading a method?
#     Does Python support traditional method overloading like Java/C++?
#
# 24. How would you prevent a class from being subclassed, or prevent a specific
#     method from being overridden in Python?
