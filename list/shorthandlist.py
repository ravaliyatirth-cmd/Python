data=[ i for i in range(1,100)]
print(data)
print()
even_number=[i for i in range(1,101) if i%2==0]
print(even_number)
print()

mark=['fail' if mark< 35 else 'pass' for mark in range(30,101)]
print(mark)

squre=[i**2 for i in range(1,100)]
print(squre)