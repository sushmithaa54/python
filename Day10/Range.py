# exaple fro stop
r1=range(11)
print(r1)
print(list(r1))

r1=range(5)
print(r1)
print(list(r1))

r1=range(6)
print(r1)
print(list(r1))

#example for start and stop
r1=range(1,7)
print(r1)
print(list(r1))

r1=range(10,17)
print(r1)
print(list(r1))

#example fro start,stop and step
r1=range(1,7,1)
print(r1)
print(list(r1))

r1=range(1,11,2)
print(r1)
print(list(r1))

r1=range(2,10,2)
print(r1)
print(list(r1))

r1=range(10,101,10)
print(r1)
print(list(r1))

#example to generate the sequence of numbers in decending order
r1=range(10,0,-1)
print(r1)
print(list(r1))

r1=range(10,0,-2)
print(r1)
print(list(r1))

r1=range(10,0,-3)
print(r1)
print(list(r1))

#indexing using range datatype
r1=range(10,101,10)
print(r1)
print(r1[3])
r2=list(r1)
print(r2[0])
print(r2[2])
print(r2[3])
print(r2[4])
print(r2[6])
print(r2[8])
print(r2[1])
print(r2[5])
print(r2[-7])
print(r2[-3])
print(r2[-2])

#slicing on range datatype
#positive slicing

r1=range(10,101,10)
print(r1)
r2=list(r1)
print(r2)
print(r2[0:5])
print(r2[2:7])
print(r2[1:9:2])
print(r2[:5])
print(r2[5:])
print(r2[0:10:3])
print(r2[3:8])
print(r2[4:9:2])
print(r2[6:10])
print(r2[2:5])

#negative slicing
print(r2[-1])
print(r2[-3])
print(r2[-5:-1])
print(r2[-7:-2])
print(r2[-10:-5])
print(r2[-8:])
print(r2[:-3])
print(r2[-9:-4])
print(r2[-6:-3])
print(r2[-4:-1])

#reverse slicing
print(r2[::-1])
print(r2[6:2:-1])
print(r2[7::-1])
print(r2[3:-10:-1])
print(r2[5::-2])
print(r2[7:1:-3])
print(r2[9:-6:-1])
print(r2[-2:-9:-2])
print(r2[6:1:-1])
print(r2[-4::-3])



