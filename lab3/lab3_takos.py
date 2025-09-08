"""
Antonios Takos
Lab 3, Python Conditional Statement and Loops
Sep 8, 2025
"""
#conditional statement
print("\n ----- Example 1: if, elif,..., else (EXERCISE)------")
"""
modify example 1:
- use while loop to validate if the user_number is between 1 and 9
- user can only guess three times. This can be done using a for loop or a while loop
"""
# guess a number between 1 and 9
guess_num = 8
# collect the number
user_num = int(input("Guess the number: "))

guess_attempt_amnt = 1

while 0 < user_num < 10:
    if(user_num == guess_num):
        print(f"Great job! {user_num} is the guess number")
        break
    elif (user_num>guess_num):
        guess_attempt_amnt += 1
        if(guess_attempt_amnt <=3):
            print(f"{user_num} should be lower! Try again!!")
            user_num = int(input("Try again: "))
        else:
            break
    elif(user_num<guess_num):
        guess_attempt_amnt += 1
        if(guess_attempt_amnt <=3):
            print(f"{user_num} should be higher! Try again!!")
            user_num = int(input("Try again: "))
        else:
            break
else:
    print(f"ERROR!")

print("End of guessing!")

print("\n ----- Example 2: Control Flow with logical operatiors ------")
# 'and', 'or' 'not' operators.
# 'and' operator returns TRUE ONLY if all statements are true
# 'or' operator returns TRUE if at least ONE of the statements are true.
# 'not' operator returns the invert of the logic. TRUE --> not operator --> false
"""
example 2: 
- children under the age of 9 are only given milk for breakfast
- children from 10 to 14 are given sandwich
- children from 15 to 17 are given a burger
"""
age_student = int(input("Enter an age: "))
lunch ="None"
if age_student <9 and age_student>=5:
    lunch = "milk"
elif age_student>=10 and age_student<=14:
    lunch = "sandwich"
elif age_student>=15 and age_student<=17:
    lunch = "burger"
else:
    lunch = "none"

print(f"At age {age_student} the food is {lunch}")

print("\n ----- Example 3: for loop as a counter ------")
# 'for' loops enables the program to execute a code block multiple times
for n in range(2,10):
    print(n)
print("\n ----- Example 4: for loop in a list ------")
years = [2011, 2005, 1998, 1980, 1973]
for y in years:
    print(y)

for index in range(len(years)):
    print(f"Year {index+1} = {years[index]}")

print("\n ----- Example 5: while loop as a counter ------")
count = 1
while count<=5:
    print(count)
    count += 1

print("\n ----- Example 6: while loop to validate a number ------")
# validate if a number is between -5 and 5 (inclucive)
num = int(input("Enter a number between -5 and 5: "))
# use a while to recollect if the number is not between -5 and 5
while num<-5 or num>5:
    num = int(input("ERROR! Enter a number between -5 and 5: "))
print(f"Entered number = {num}")