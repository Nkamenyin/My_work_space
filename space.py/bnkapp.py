#!/usr/bin/python3
#banking app to deposit, withdraw and check balance

print("welcome!!!")

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
    print(f"Your account has been credited with ${amnt}")
    print(f"Your account balance is ${amnt} ")

elif (choice == '2'):#withdrawal
    balnce = int('3000')
    print(f"Your balance is ${balnce} ")
    amnt = int(input("\ninput withdraw  amount: "))

    if (balnce >= amnt):
        balance = int(balnce - amnt)
        print(f"Your account balance is ${balance}")

    else:
        print("insufficiant fund")

elif (choice == '3'):#check balance
    check_balance = int
    balnce = check_balance
    print(f"Your account balance is ${balnce} ")

elif (choice == '4'):#Exit
    print("\nBye bye")

else:
    print("invalid operation")
