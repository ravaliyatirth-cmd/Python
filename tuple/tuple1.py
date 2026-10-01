tuple1=(1,2,3,4,5,6,7,7,8)
print(type(tuple1))

print(tuple1.__add__((4,5,6,"tirth",4.8987678)))
print(tuple1.count(7))
print(tuple1.index(5))

list1=list(tuple1)
print(list1)

tuple2=(i for i in range(1,10))
print(tuple(tuple2))