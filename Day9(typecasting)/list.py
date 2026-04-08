# LIST TYPE CASTING

li = [10,20,30,40,98]
print(str(li))
print(tuple(li))
print(set(li))
print(bool(li))

li = [10,20,30,40,98]
print(int(li))       # TypeError
print(float(li))     # TypeError
print(complex(li))   # TypeError
print(dict(li))      # TypeError