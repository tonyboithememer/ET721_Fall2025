"""
antonios takos
sep 17th, 2025
lab 6: objects and classes
"""
print("\n------ Example 1: create a class -----")
class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        self.balance = 20000

    #method
    def add_radius(self, r):
        self.radius += r
        return self.radius

class Rectangle(object):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

    # method to calculate the area
    def area(self):
        return self.width * self.height
    
    # method to calculate the perimiter
    def perimiter(self):
        return 2*self.width + 2*self.height

# creating an instance of the class, which is an object 
circle1 = Circle(4, "red")
circle2 = Circle(10, "green")

rectangle1 = Rectangle(2, 5, "magenta")
rectangle2 = Rectangle(7, 3, "blue")

# accessing information in an object
print(f"The color of circle 2 is = {circle2.color}")
print(f"The width of rectangle 1 is = {rectangle1.width}")

# updating data in an object
# change circle1 color from 'red' to 'yellow'
print(f"The color of circle 1 before the update is = {circle1.color}")
circle1.color = "yellow"
print(f"The color of circle 1 after the update is = {circle1.color}")

# accessing a method
print(f"Radius of circle 2 = {circle2.radius}")
# update the radius by adding 5
circle2.add_radius(5)
print(f"Radius of circle 2 after method add_radius = {circle2.radius}")

# accessing methods in Rectangle
print(f"The area of the rectangle 1 with width {rectangle1.width} and height {rectangle1.height} is {rectangle1.area()}")
print(f"The perimiter of rectangle 2 = {rectangle2.perimiter()}")

print("\n ------ EXERCISE -----")
class BankAccount(object):
    def __init__(self, account_number="14234234", account_holder="Antonios Takos", balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("ERROR. PLEASE ENTER A POSITIVE NUMBER.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"SUCCESSFULLY WITHDREW {amount}. NEW BALANCE: {self.balance}")
        else:
            print("INSUFFICENT FUNDS. PLEASE TRY AGAIN LATER.")

#EXAMPLE
useraccount = BankAccount(14234234, "Antonios Takos")
account = BankAccount(250.50)
account.withdraw(700)
account.deposit(1000)
print(f"Final balance {account .balance}")