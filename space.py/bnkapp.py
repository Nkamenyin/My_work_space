#!/usr/bin/python3
#banking app to deposit, withdraw and check balance

print("welcome!!!")
balnce = float(input("Your balance: "))

#choosing options
print("\nPick your option:")
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Exit")

#deposit
choice = input()
if (choice == '1'):
    amnt = int(input("amount: "))
    balnce = (balnce + amnt)
    print(f"Your account has been credited with ${amnt}")
    print(f"Your account balance is ${balnce} ")

elif (choice == '2'):#withdrawal
    #balnce = float('3000.00')
    print(f"Your balance is ${balnce} ")
    amnt = float(input("\ninput withdraw  amount: "))

    if (balnce >= amnt):
        balance = float(balnce - amnt)
        print(f"Your account balance is ${balance}")

    else:
        print("insufficiant fund")

elif (choice == '3'):#check balance
    print(f"Your account balance is ${balnce} ")

elif (choice == '4'):#Exit
    print("\nBye bye")

else:
    print("invalid operation")
