pin=2007
bal=20000
pin_a=int(input("Enter Pin : "))
if pin == pin_a:
    print("1.Withdraw")
    print("2.Deposite")
    print("3.Check Balance")
    ch=int(input("Enter your choice"))
    if(ch==1):
        amount=int(input("Enter Amount"))
        bal-=amount
        print(amount," is Withdraw Succesfully ",bal," Remaining Balance")
    elif(ch==2):
        depo=int(input("Enter Amount"))
        bal+=depo
        print(depo,"Deposite Succesfully",bal,"Remaining Balance")
    elif(ch==3):
        print("Available Balance is ",bal)

