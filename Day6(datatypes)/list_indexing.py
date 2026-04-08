list=[10,20,40,70,98,270]
print(list[0])
print(list[1])
print(list[3])
print(list[5])
print(list[-1])
print(list[-3])
# print(list[9]) output:IndexError: list index out of range

#nestedlist
list=[10,20,['smith',100,200],98,270]
print(list[2][0])
print(list[2][1])
print(list[2][2])
print(list[2][-1])
print(list[2][-2])
print(list[2][-3])
