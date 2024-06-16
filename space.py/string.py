#!/usr/bin/python3

"""working on string formating"""

#creating variables
name = input("what's your name: ")
phone_no = int(input("phone number: "))
city = input("city: ")

#outputing:


#1. OLD METHOD which uses place holders(%) and data type

print("Your name is %s, your phone number is %d and your city is %s" % (name, phone_no, city))

#2. STR.FORMAT() method
print("Your name is {}, your phone number is {} and your city is {}".format(name, phone_no, city))

#str.format() without type casting on the variables

print("Your name is {:s}, your phone number is {:d} and your city is :s{}".format(name, phone_no, city))

#str.format() using imdexing
print("Your name is {0}, your phone number is {1} and your city is {2}".format(name, phone_no, city))

#str.format() using key words to represent varables
print("Your name is {eyeng}, your phone number is {num} and your city is {cali}".format(eyeng = name, num = phone_no, cali = city))

#3. F-STRING fotmatting style (f"")
print(f"Your name is {name}, your phone number is {phone_no} and your city is {city}")

#f-string with data casting
print(f"Your name is {name:s}, your phone number is {phone_no:d} and your city is {city:s}")
