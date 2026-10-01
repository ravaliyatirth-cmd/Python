name='Ravaliya Tirth'
print(len(name))


#convert char to ascii
print(ord(")"))

#convert ascii to char
print(chr(97))


#Task 1 print abcdef.....
A=ord("A")
B=ord("Z")
a=ord("a")
b=ord("b")
ch=int(input("Enter choice 1.Capital Abcd 2.SMall Abcd"))
match ch:
    case 1:
            print("Capital Abcd")
            for i in range(A,B):
                print(chr(i))
    case 2:
            print("Small Abcd")
            for i in range(a,b):
                  print(chr(i))
    



for i in range(97,123):
    print(chr(i))