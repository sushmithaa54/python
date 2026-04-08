# STRING DATATYPE CONVERSION

s1 = "python"
print(list(s1))
print(tuple(s1))
print(set(s1))
print(bool(s1))

s1 = "education"
print(int(s1))       # ValueError
print(float(s1))     # ValueError
print(complex(s1))   # ValueError
print(dict(s1))      # ValueError