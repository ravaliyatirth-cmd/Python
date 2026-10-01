a=float(input("Enter first no : "))
b=float(input("Enter second no : "))
while True:
        print("1.Sum \n 2.Sub \n 3.Mul \n 4.Div \n 5.Rem")
        ch=int(input("Enter Choice : "))
        match ch:
            case 1:
                sum=a+b
                print("Sum = ",sum)
            case 2:
                sub=a-b
                print("Sub = ",sub)
            case 3:
                mul=a*b
                print("Mul =",mul)
            case 4:
                div=a/b
                print("div =  ",round(div,2))
            case 5:
                rem=a%b
                print("Rem = ",rem)
            case _:
                print("Invalid choice ....")
                exit(0)




