import time
print("please insert your atm card")
time.sleep(7)
password=95734
pin=int(input("enter your pin number: "))
balance=1000
if pin==password:
    while True:
        print("""
          1 == balance
          2 == withdraw amount
          3 == deposit amount
          4 == pin change
          5 == transaction history
          6 == exit
          """)
        try:
            option=int(input("enter your choice: "))
        except:
            print("please enter the valid option")
        if option==1:
            print(f"your current balance is: {balance}")
            print("===================================")
        if option==2:
            withdraw_amount=int(input("enter your withdraw amount: "))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your current balance is: {balance}")
            print("===================================")
            print("===================================")
        if option==3:
            deposit_amount=int(input("enter your deposit amount:"))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited from your account")
            print(f"your current balance is: {balance}")
            print("=======================================")
            print("=======================================")
        if option==4:
            print(f"enter your old pin: {pin}")
            new_pin=int(input("enter your new pin number: "))
            print(f"sucessfully updated pin number")
            print("=======================================")
            print("=======================================")
        if option==5:
            deposit_amount=int(input("enter your deposit amount:"))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited from your account")
            print(f"your current balance is: {balance}")
            print(f"your transaction is completed")
            withdraw_amount=int(input("enter your withdraw amount: "))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your current balance is: {balance}")
            print(f"your transaction is completed")
        if option==6:
            break
else:
    print("wrong pin please enter your correct pin")