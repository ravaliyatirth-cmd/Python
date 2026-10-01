
inr_list=[]
while(1):
    ch=int(input("1--> go ahed"+" 0---> stop"))
    if(ch == 0):
            break
    else:
         movie=input("Enter movie : ")
         year=input("Enter year :")
         inr_list.append([movie,year])

print(inr_list)



