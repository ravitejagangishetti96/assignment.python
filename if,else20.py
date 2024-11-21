balance=10000
print("welcome to AXIS Bank")
print("select options form Main Manu")
print("1.check the balance")
print("2.withdraw amount")
print("3.deposit the amount")

option=int(input("select from menu:"))
if option==1:
    print(f"avialable balance is: ${balance}")
elif option==2:
    amount=int(input("enter the amount you want to withdraw"))
    if amount<=balance:
        print("the amount is succesfully withdrawn")
        print(f"the remaing balance is {balance-amount}")
    elif amount>balance:
        print("Insufficient Funds")
elif option==3:
    print("deposit cash in machine")
else:
    print("Please select the correct option /n THANK YOU")

