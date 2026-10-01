num=int(input("Enter number : "))


a=int(input("1 for 2 while"))

# fact=1
if(a==1):
    for i in range(1,num):
        num=num*i
    print(num)
elif(a==2):
    i=1
    fact=1
    while(i<=num):
        fact=fact*i
        i=i+1
else:
    print("Choose appropriate")


# print(fact)