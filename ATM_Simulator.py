import time
print("Please Enter Your CARD")

time.sleep(1)

password=1234
print("----------------------------------------------------------------------------------------------------------------")
pin=int(input("Enter your ATM PIN "))
print("----------------------------------------------------------------------------------------------------------------")
balance=5000

if pin==password:
    print("\n")
    print("\n")
    print("     ::      ::      ::   :::::::   ::       ::          ::::      ::::          ::      ::       ::::::: ")
    print("      ::    ::::    ::    ::        ::       ::        ::        ::    ::       ::::    ::::      ::      ")
    print("       ::  ::  ::  ::     :::::::   ::       ::       ::        ::      ::     ::  ::  ::  ::     ::::::: ")
    print("        ::::    ::::      ::        ::       ::        ::        ::    ::     ::    ::::    ::    ::      ")
    print("         ::      ::       :::::::   ::::::   ::::::      ::::      ::::      ::      ::      ::   ::::::: ")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    while True:
        print("""
                1 == Balance
                2 == Withdraw Balance
                3 == Deposit Balance
                4 == Exit
        """)
        try:
            option=int(input("\t\tPlease Enter your choise "))
        except:
            print("Please Enter valid options !")
        
        if option==1:
            print("==========================================================================================================")
            print(f"\t\tYour Account Balance is {balance}")
            print("==========================================================================================================")
        if option==2:
            withdraw_amt=int(input("\t\tPlease Enter Withdraw Amount "))
            balance=balance-withdraw_amt
            print(f"\t\t{withdraw_amt} is debited from your Account")
            print("==========================================================================================================")
            print("\t\tYour current Balance is ",balance)
            print("==========================================================================================================")
        if option==3:
            deposit_amt=int(input("\t\tPlease Enter Deposit Amount "))
            balance=balance+deposit_amt
            print(f"\t\t{deposit_amt} is credited to your Account")
            print("==========================================================================================================")
            print("\t\tYour current Balance is ",balance)
            print("==========================================================================================================")
        if option==4:
            print("Exiting...")
            print("Please Remove Your Card...")
            break



else:
    print("Wrong PIN please try again...")
