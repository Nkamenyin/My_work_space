#!/usr/bin/python3

#a quiz program 
score = 0

#question
#1. 
ans = "calabar"
answr = input("what is the Capital of is Cross River State? ").lower()

if (answr == ans):
    print("correct answer")
    score += 2
else:
    print("wrong answer")

#.2 
ans = "habitat"
answr = input("A place where plants and animals live is called? ").lower()

if (answr == ans):
    print("correct answer")
    score += 2
else:
    print("wrong answer")
print(f"Your final score is {score}")
