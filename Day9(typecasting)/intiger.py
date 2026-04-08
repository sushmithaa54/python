# IMPLICIT TYPE CASTING

a = 5
b = 4
c = a + b
print(type(c))   # <class 'int'>

a = 98.45
b = 10
c = a * b
print(type(c))   # <class 'float'>


# INTEGER DATATYPE CONVERSION

a = 98
print(float(a))      # 98.0
print(complex(a))    # (98+0j)
print(bool(a))       # True
print(str(a))        # '98'

print(list(a))       # TypeError
print(tuple(a))      # TypeError
print(set(a))        # TypeError
print(dict(a))       # TypeError