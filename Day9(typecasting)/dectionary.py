# DICTIONARY DATATYPE TYPE CASTING

d1 = {'ename':'smith','salary':98000}
print(str(d1))
print(list(d1))
print(tuple(d1))
print(bool(d1))

d1 = {'ename':'smith','salary':98000}
print(int(d1))       # TypeError
print(float(d1))     # TypeError
print(complex(d1))   # TypeError