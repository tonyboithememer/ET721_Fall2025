"""
antonios takos
Lab 7, accessing data in a file
Sep 29th, 2025
"""

from lab7_function import *


print("\n ---- example 1: reading file -----")
read_data("phrases.txt")

print("\n ---- example 2: reading specific portion of a file -----")
read_up("phrases.txt")

print("\n ---- example 3: reading specific portion using readline -----")
read_readline("phrases.txt")

print("\n ---- example 4: reading specific portion using readlines -----")
read_all("phrases.txt")

print("\n ---- example 5: loop through each line -----")
read_each("phrases.txt")

print("\n ---- example 6: creating a new file -----")
new_file("takos.txt")

print("\n ---- example 7: appending data into an existing file -----")
stamp_date("takos.txt")

print("\n ---- EXERCISE -----")
count_yahoo = email_read("user_email.txt", "@yahoo")
count_gmail = email_read("user_email.txt", "@gmail")
count_hotmail = email_read("user_email.txt", "@hotmail")
write_report("reportemail.txt", count_gmail, count_yahoo, count_hotmail)
