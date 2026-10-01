a=input("Enter string ")
b=input("Enter charcter which do you want to find ?")

for i in range(len(a)):
    if(a[i]==b):
        break

print("charcter at position ",i+1)

