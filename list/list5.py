data=["ram","shyam","amit","Tirth","Raj","Kunal","yash"]

# data.sort()
# print(data)

# data.reverse()
# print(data)

data.sort(reverse=True)
print(data)

data.sort(key=len)
print(data)


data.sort(reverse=True,key=len)
print(data)