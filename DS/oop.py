class Car:
    def __init__(self, brand, model):   # constructor
        self.brand = brand
        self.model = model

    def display(self):                  # method
        print(f"{self.brand} {self.model}")

c1 = Car("Tesla", "Model S")  # object
c2 = Car("BMW", "X5")

c1.display()  # Tesla Model S
c2.display()  # BMW X5


# Encapsulation

# Bundling data (attributes) and methods (functions) inside a class.

# You control access using:

# Public (self.var)

# Protected (_var) (convention)

# Private (__var)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # ✅ 1500
# print(acc.__balance)    ❌ Error (private)

2️⃣ Abstraction

Hiding implementation details, showing only what it does (not how).

In Python, done via abstract classes or just normal methods.

from abc import ABC, abstractmethod

class Shape(ABC):              # abstract class
    @abstractmethod
    def area(self): pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r

c = Circle(5)
print(c.area())  # 78.5

3️⃣ Inheritance

One class can reuse/extend another.

Promotes code reusability.

class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):    # inherits from Animal
    def sound(self):
        print("Woof!")

d = Dog()
d.sound()  # Woof!


4️⃣ Polymorphism

Same function name, different behavior.

Example 1: Method overriding

class Bird:
    def fly(self):
        print("Birds can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

b = Penguin()
b.fly()  # Penguins cannot fly


xample 2: Operator Overloading
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, other): return Point(self.x + other.x, self.y + other.y)

p1, p2 = Point(2, 3), Point(4, 5)
p3 = p1 + p2
print(p3.x, p3.y)  # 6 8











