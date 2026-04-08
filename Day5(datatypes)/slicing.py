# slicing is a multivalue datatype
msg='education'
print(msg[::])
print(msg[::1])
print(msg[::2])
print(msg[::3])
print(msg[::4])

print(msg[1:6:1])
print(msg[4:20:1])

print(msg[6:20:1])

#waptd the even charecters
print(msg[0::2])


#waptd the odd charecters
print(msg[1::2])


#waptd the revers of the given string
msg='python'
print(msg[::-1])
print(msg[-1:-9:-1])

#waptd the even digits in revers order of the given string
print(msg[-2::-2])

#waptd the odd digits in revers order of the given string
print(msg[-1::-2])



string='welcome to python class'

#---------
#part 1:positive slicing
#---------
print(string[0:7])   #welcome
print(string[8:10])  #to
print(string[11:17]) #python
print(string[18:23]) #class
print(string[0:11])  #welcome to
print(string[11:23]) #python class
print(string[3:9])   #come t
print(string[5:15])  #me t pyth
print(string[:7])    #welcome
print(string[8:])    #to python class

#---------
#part 2:negative slicing
#---------
print(string[-5::])     #class
print(string[-12:-6:])  #python
print(string[-23:-16])  #welcom
print(string[-15:-13])  #to
print(string[-11:-7])   #ytho
print(string[-23:-1])   #welcom to python class
print(string[:-6])      #welcom to python
print(string[-6:])      # class
print(string[-10:-5])   #thon

#---------
#part 3:reversing 
#---------
print(string[::-1])     #ssalc nohtyp ot emoclew
print(string[22::-1])   #ssalc nohtyp ot emoclew
print(string[16:10:-1]) #nohtyp
print(string[-1:-6:-1]) #ssalc
print(string[9::-1])    #ot emoclew



