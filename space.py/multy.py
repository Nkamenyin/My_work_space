#!/usr/bin/python3

"""collecting a number from the user and multiplying the number"""

for i in range(1, 13):
    #enter number
    num = int(input("Enter a number: "))
    print(f"{num} x {i} = {num * i}")
