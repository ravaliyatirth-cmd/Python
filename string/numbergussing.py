import random

value= random.randint(1 , 100)
while(True):
    a=int(input("Enter number : "))
    if(value == a):
        print("You are win your number",a,"and gussing number",value,"is same")
        break
    elif(value>a):
        print("Too low..")
    else:
        print("Too high")