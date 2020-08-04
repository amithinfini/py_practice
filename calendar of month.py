# Write a Python program to print the calendar of a given month and year.
import calendar as cl
y = int(input('Enter the year: '))
# print(y, type(y))
m = int(input('Enter the month: '))
print(cl.month(y,m), '\n', cl.month(y,m+1))
input()
