"""
Oct 6, 2025
unit testing
Antonios Takos
"""
class Employee:
    raise_amt = 1.05

    def __init__(self, firstname, lastname, salary):
        self.first = firstname
        self.last = lastname
        self.salary = salary
    
    # The @property decorator indicates that the attached method will behave like an attribute.
    @property
    def emailemployee(self):
        return f"{self.first}.{self.last}@email.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)