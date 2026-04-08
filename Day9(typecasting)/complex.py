# COMPLEX DATATYPE CONVERSION

a = 10+5j
print(bool(a))       # True
print(str(a))        # (10+5j)

print(int(a))        # TypeError
print(float(a))      # TypeError
print(list(a))       # TypeError
print(tuple(a))      # TypeError
print(set(a))        # TypeError
print(dict(a))       # TypeError