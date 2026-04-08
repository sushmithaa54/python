# TUPLE DATATYPE CONVERSION

t1 = (10,20,30,40)
print(str(t1))
print(list(t1))
print(set(t1))
print(bool(t1))

print(int(t1))       # TypeError
print(float(t1))     # TypeError
print(complex(t1))   # TypeError
print(dict(t1))      # TypeError