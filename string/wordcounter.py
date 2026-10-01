#word counter
str = input("Enter sentence: ")
count = 0
flag = 0
for i in str:
    if i != ' ':
        if flag == 0:
            count = count + 1
            flag = 1
    else:
        flag = 0

print("Total words are : ",count)
# 👍