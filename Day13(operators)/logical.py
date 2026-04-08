# and operator
a=98
b=10
print(a>b and b<a)

a=97
b=11
print(a>b and b>a)

a=100
b=90
c=60
print(a>b and b>c and c>a)

# or operator
a=11
b=97
print(a>b or b==a)

a=100
b=200
c=70
print(a>b or b>c or a>c)


# not opertor
a=98
b=10
print(not(a>b))

a=100
b=100
print(not(a!=b))

a=50
b=50
c=100
print(not(a!=b) and not (c>a))


