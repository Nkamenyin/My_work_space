#!/usr/bin/python3

"""Practing on an age calculator using the input function to create varibles"""

#creating the varables using input
yob = input("What's your year of birth? ")
mob = input("month of birth? (01-12) ")
dob = input("and the day? ")
currnt_yr = input("What's the current year? ")

#calculating the age
age = int(currnt_yr) - int(yob)

#displaying your date of birth
print("Your date of birth is", end=" ")
print(dob, "-", mob,"-", yob)

#displaying your actual age
print("You are", age, end=" ")
print("years old")
