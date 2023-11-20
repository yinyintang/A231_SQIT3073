# Chapter 3 Strings (Slide 3-8)

import os

os.system ("cls")

#String as Arrays
ayat= "Selamat Pagi"
print(ayat[0])

#Looping in a string
string_variable = "ayat"
for initial_variable in string_variable:
    print(initial_variable)

for i in ayat:
    print(i)


#String Manipulation (Length and Checking)

#String Length (keyword len)
print (len(ayat))

#String checking (keyword in) – Boolean output
ayat= "Selamat pagi cikgu"

print ("pagi" in ayat)

if "pagi" in ayat:
    print("ya, pagi di dalam ayat")

#String checking (keyword not) – Boolean output
ayat="selamat pagi cikgu"
print ("ayam" not in ayat)

if ("ayam" not in ayat):
    print("ayam" not in ayat)


#String Manipulation (Slicing)

#Return a set of characters 
ayat = "selamat pagi cikgu"
print (ayat[0])
print (ayat[4])
print (ayat[3:7])
print (ayat[:7])
print (ayat[3:])
print (ayat[-8:-4])


#String Manipulation (Modification)

#Convert to upper case
ayat="selamat pagi cikgu"
print (ayat.upper())

#Convert to lower case
print (ayat.lower())

#Remove space
print (ayat.strip())

#String replacement
print (ayat.replace("a","i"))


#String Manipulation (Combination)

# String can be combine using + symbol
ayat = "selamat pagi Cikgu"
cikgu = "Manisha"
ucapan = ayat + cikgu 
print (ucapan)

#The use of { } and format keyword (to combine string and numbers)
#Option 1 
umur = 40
cikgu = "Manisha"
umur_cikgu = "Umur Cikgu {} adalah {}".format(cikgu, umur)
print(umur_cikgu)

#Option 2
umur = 40
cikgu = "Manisha"
umur_cikgu = f"Umur Cikgu {cikgu} adalah {umur}"
print(umur_cikgu)
