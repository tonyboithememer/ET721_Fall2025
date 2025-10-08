"""
Antonios Takos
Oct 8, 2025
Lab 9, test input and output data
"""
# function to collect student's grade and returns the average of the grade
def main():
    #collect the amount students
    while True:
        try:
            num_students = int(input("Enter number of students: "))
            if num_students <= 0:
                print("Number of students must be greater than 0. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive number.")
    
    # collect the grades for each student
    total_sum_grades =0
    for i in range(num_students):
        while True:
            try:
                grade = float(input(f"Enter grade for student {i+1}: "))
                if 0<=grade<=100:
                    total_sum_grades += grade
                    break
                else:
                    print("Invalid input. Enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input: Enter a numerical value!")

    # calculate for the average grade
    average = total_sum_grades / num_students
    #print results
    print(f"The class average is {average:.2f}")

if __name__ == "__main__":
    main()