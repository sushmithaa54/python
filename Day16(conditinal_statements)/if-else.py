#1
n=int(input('enter a number:'))
if n>5:
    print(n**2)
else:
    print(n**3)
print('program ends')


#2
n=int(input('enter a number:'))
if 3<=n<=5:
    print(n,n,n,sep='\n')
else:
    print(n%10)
print('program ends')


#3
n=int(input('enter a number:'))
if n%3==0 and n%5==0:
    print(n+1)
else:
    print(n//10)
print('program ends')


#4
n=int(input('enter a number:'))
if 12%n==0 and 16%n==0:
    print(12+16)
else:
    print(16-n)
print('program ends')


#5
ch=eval(input('enter a charecter:'))
if 'a'<=ch<='z' or 'A'<='Z':
    print(ord(ch))
else:
    print(ch)
print('program ends')


#6
ch=input('enter a charecter:')
if ch not in 'aeiouAEIOU' and ('A'<=ch<='Z' or 'a'<=ch<='z'):
    print(ch)
else:
    print(ord(ch%10))
print('program ends')