"""
Antonios Takos
Oct 15, 2025
Lab 9: file operation test
"""


def write_file(filename, msg):
    with open(filename, "w") as file:
        file.write(msg)


def read_file(filename):
    with open(filename, "r") as file:
        file.readlines()


def append_file(filename):
    with open(filename, "a") as file:
        file.write("\nNew line added!")


# function from exercise lab 7 (yesterday)
"""
create a function, named email_read(), that reads a txt file and returns the number of users that have @gmail, @yahoo, and @hotmail email address. The function should have try-exception statement. You can test the function using the file user_email.txt file.
"""


def email_read(filename, email):
    count_email = 0
    with open(filename, "r") as file1:
        filelines = file1.readlines()
        # loop through each item in 'filelines'
        for eachline in filelines:
            if email in eachline:
                count_email += 1
        return count_email


def write_report(filename, count_gmail, count_yahoo, count_hotmail):
    with open(filename, "w") as report:
        report.write(f"gmail = {count_gmail}\n")
        report.write(f"yahoo = {count_yahoo}\n")
        report.write(f"hotmail = {count_hotmail}\n")
