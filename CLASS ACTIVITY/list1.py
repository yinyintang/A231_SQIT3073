
a=[1,2,3]
b='apple'

c=(a,b)

print(c)

# 
a=(12,'a')
b=(19,)

a+=b
print(a)

#
a=[]

b=9
c=8
d=12

a.append(b)
print(a)

#
a=[]

b=9
c=8
d=12

a+=b
print(a)

# not efficient 
a=[]

b=int(input("What is your name"))
c=list(b)

a+=b
print (a)

#may shorten by write this code
a=[]

b=int(input("What is your name"))

a.append(b)
print (a)