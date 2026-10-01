original_number=int(input("Enter number : "))
count=0
sum=0
temp=original_number
temp2=temp


while(temp>0):
    temp=temp//10
    count+=1

while(original_number>0):
    digit=temp%10
    sum+=(digit**count)
    temp=temp//10

if(sum==temp2):
    print("Number is Armstrong Number")
else:
    print("Number is not Armstrong Number")