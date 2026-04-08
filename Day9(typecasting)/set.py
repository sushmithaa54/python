# SET DATATYPE TYPE CASTING

s1 = {98,45,30,89,17}
print(str(s1))
print(list(s1))
print(tuple(s1))
print(bool(s1))

s1 = {98,45,30,89,17}
print(int(s1))       # TypeError
print(float(s1))     # TypeError
print(complex(s1))   # TypeError
print(dict(s1))      # TypeError