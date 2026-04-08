# BOOLEAN DATATYPE CONVERSION

a = True
print(int(a))        # 1
print(float(a))      # 1.0
print(complex(a))    # (1+0j)
print(str(a))        # True

print(list(a))       # TypeError
print(tuple(a))      # TypeError
print(set(a))        # TypeError
print(dict(a))       # TypeError