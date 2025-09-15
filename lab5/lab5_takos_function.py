"""
antonios takos
function file
sep 15, 2025
lab 5, function
"""
# example 1: define a function that passes two numbers and return the product of it
def product(a=0,b=0):
    c = a*b
    return c

# Example 2: function to calculate the hypotenuse
def hypotenuse(side1, side2):
    return (side1**2 + side2**2)**0.5

# Example 3: function to check if the number is positive, negative or zero.
# the function returns a string
def check_number(num):
    if(num>0):
        return "POSITIVE"
    elif(num<0):
        return "NEGATIVE"
    else:
        return "ZERO"
    
    # Example 4: function to calculate the average of a list of grades and return 'true' of the average is greater than 60. otherwise, it returns 'false'.

def check_grades(grades):
        #initalize the average grade value
        avg = 0
        # sum the individual 'g' from list 'grades'into 'avg'
        for g in grades:
            avg += g
        # find the average grade
        avg /= len(grades)
        return avg

def check_pass(avg_grade):
        #check if the avg is greater than 60 
        if avg_grade >= 60:
            return True
        else:
            return False
        
# LAB EXERCISE
import random
guessing_num = 5
def random_num(minimum_number, maximum_number):
     return random.randint(minimum_number, maximum_number)

def guess_comparison(random_num, guessing_num):
     if random_num < guessing_num:
        print("Your number is too small!! Try guessing higher!~")
     elif random_num > guessing_num:
          print("Your number is too big!! Try guessing lower!~")
     else:
          print("You got it!! Good job!!")