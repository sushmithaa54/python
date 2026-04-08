#1
a=98
b=48
if a>b:
    print(f'a:{a} is greater than b:{b}')

#2
n=eval(input('enter a number:'))
if n>0:
    print(f'{n} is positive')

n=98
if n>0:
    print(f'{n} is positive')

#3
n=46
if n%2==0:
    print(f'{n} is even')

#4
n=77
if n%2!=0:
    print(f'{n} is odd')
   
#5 
n=15
if n%3==0:
    print(f'{n} is divisible by 3')

#6
n=25
if n%5==0:
    print(f'{n} is divisible by 5')

#7 
n=15
if n%3==0 and n%5==0:
    print(f'{n} is divisible by 3 nd 5')

#8
char='apple'
if char[0] in 'aeiouAEIOU':
    print(f'{char} start whith vowel')

#9
char='microsoft'
if char[0] not in 'aeiouAEIOU':
    print(f'{char} start whith consonat')
    
#10
char='apple'
if char[-1] in 'aeiouAEIOU':
    print(f'{char} ends whith vowel')

#11
char='jaishreeram'
if char[-1] not in 'aeiouAEIOU':
    print(f'{char} ends whith consonat')
    
#12
char='Microsoft'
if char[0] >='A' and char[0]<='Z':
    print(f'{char} start whith uppercase')
    
char='Microsoft'
if 'A' <= char[0] <='Z':
    print(f'{char} start whith uppercase')

#13
char='e'
if 'a' <= char <='z':
    print(f'{char} is lower case')

#14
char='9'
if '0' <= char <='9':
    print(f'{char} is digit')

#15
char='$'
if not('0' <= char <='9' or 'a' <= char <='z' or 'A' <= char[0] <='Z'):
    print(f'{char} a is special symbol')










    

