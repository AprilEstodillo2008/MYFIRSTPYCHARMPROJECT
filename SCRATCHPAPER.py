#April Estodillo
#0123456789 10 11 12 13 14

myName = "April Estodillo"
LengthofmyName = len(myName)
print(myName)
print(LengthofmyName)

print(myName[7])
print(myName[14])
print(myName[10])

print(myName)
print(myName.upper())
print(myName.lower())
print(myName.capitalize())

#prac no.2


from time import sleep
'''
yourName = input("What is your name?")
print(f'Hi! {yourName}')

if yourName.upper() == "JOHN": #Condition
    print("I hate you")
'''
#sing line comment
#''' block comment '''

longString = "SuperManIsStrong"
#[START INDEX INCLUDED : END INDEX EXCLUDED: STEP/INTERVAL]
subString = longString[5 : 8 : 1]
print(subString)
subString = longString[0: 12 : 3]
print(subString)

longString = "Super"
#[START INDEX INCLUDED : END INDEX EXCLUDED: STEP/INTERVAL]
subString = longString[5 : 8 : 1]
print(subString)
subString = longString[0: 12 : 3]
print(subString)

print(longString [2])
print(longString [12])
#Magkaka index error

subString = longString[5 : 8]
print(subString)

myString = "I AM FLYING"
reverseMyString = myString[::-1]
print(reverseMyString)

'''
print("BS ECE 1-2 demo")
for i in range(10, -1, -1):
    print(i)
    sleep(1)
'''
#integer = (-,+,100)
#float = (23.2323)
#complex(imaginary) = 25+25j

'''
complexNum = 25 + 25j
print(complexNum)
'''

a = 5
b = 25
sum = a + b
print(sum)
#30

'''
a = ("5")
b = "25"
sum = a + b
print(sum)
#525 ang answer
'''

a = 2
b = 4
c = 3
d = 8
outut = d / b - a + c * d #pmdas
print(outut)

#modulo - % - to get the remainder
a = 55
b = 5
output = 55 % 5
print(output)

n = input("Give me a number")
if int(n) % 2 == 0:
    print('is even')
else:
    print('is odd')

n = input("Give me a number")
if int(n) % 2 == 0:
    print('is even')
else:
    print('is odd')

import math
#float
#complex number

a =25.5
b = 13.27
prod = a * b
print(prod)

a = 10
b = 3
qout = a / b
print(qout)
print(round(qout, 2))

a = 25 - 25j
b = 10 - 10j
# (25 - 25j)(10 - 10j) = 250 - 250j - 250j - 250 = -500j
c = a * b
print(c)

a = 5
b = 25
c = math.remainder(b , a)
print(c)
c = math.factorial(a)
print(c)
c = math.log(a, 10)
print(c)

#Boolean True or false 1 or 2(comparison)
#True not "True" not true
#False not "false" not false

#Comparison operator
# > greater than
# >= greater than or equal
# < less than
# <= less than or equal
# ==equal
# != not equal

a = 5
b = 7
#print( a <= b) = true
isCorrect = a == b
#print(isCorrect) = false

#logical operator
#AND, OR, NOT, NAND, NOR, XOR, XNOR

x = 5
y = 10
z = 15

isCorrect = z > y and y > x
print(isCorrect) #true and true = true
isCorrect = x > z and y > x
print(isCorrect) #true and false = false

isCorrect = not(x > z and x > y)
print("NAND " + str(isCorrect))
isCorrect = not(z > x and x > y)
print("NAND " + str(isCorrect))


isCorrect = z > y or y > x
print(isCorrect) #true and true = true
isCorrect = x > z or y > x
print(isCorrect) #true and false = true

#XOR
a = 5
b = 10
isCorrect = a != b
print("XOR " + str(isCorrect))

a = 13
b = 13
isCorrect = a != b
print("XOR " + str(isCorrect))

a = 5
b = 10
c = 15
isCorrect = (a > b) != (c > a)
print("XOR " + str(isCorrect))


#membership
# in, not in, is, is not

myName = "Bob April"
yourName = "Bob"

print(myName is yourName)
print(myName is not yourName)

print(yourName in myName)
print(yourName not in myName)
print(myName in yourName)

myFavoriteFruits = ('apple', 'banana', 'orange')
print("apple" in myFavoriteFruits)
print("mango" in myFavoriteFruits)
