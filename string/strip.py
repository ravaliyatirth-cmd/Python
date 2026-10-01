name=input("Enter your name : ")

print(len(name))
print(len(name.strip()))
print(len(name.lstrip()))
print(len(name.rstrip()))


print(name.swapcase())
print(name.startswith("t"))

#print(name.startwith(('a','b','t')))
print(name.endswith(("h","s","u")))

print(name.isalnum())
print(name.isdigit())
print(name.isalpha())
print(name.islower())
print(name.isupper())
print("isspace",name.isspace())
print("Title",name.istitle())
print("isPrintable",name.isprintable())