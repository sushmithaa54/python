n=int(input())
res=n>5
print(res)

n=int(input())
res=n>10 and n<20
print(res)

n=int(input())
res=n%3==0
print(res)

n=int(input())
res=n%3==0 and n%5==0
print(res)

n=input()
res=n>'A' and n<'Z'
print(res)

n=input()
ascii=ord(n)
last=ascii%10
res=last%3==0
print(res)






