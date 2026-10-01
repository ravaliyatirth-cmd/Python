import math
print("Qudraatic Eq is ax^2+bx+c")
print("Enter value of a,b,c respectivily : ")
a=int(input("Value of a :"))
b=int(input("Value of b :"))
c=int(input("Value of c :"))

print(f"Qudratic equation is : {a}x^2+{b}x+{c}")
d=b**2-4*a*c
print(d)

if(d>=0):
    x1=float((-b+math.sqrt(d))/(2*a))
    x2=float((-b-math.sqrt(d))/(2*a))
else:   
    print("Roots are imagnary")

print(f"roots are {x1} and {x2}")


