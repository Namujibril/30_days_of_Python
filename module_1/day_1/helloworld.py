#Checking the python version
print("Python --version")    #will print the python version

#Arithmetic Operators
print( 4 + 3)                #will add two numbers
print( 4 - 3)                #will subtract two numbers
print( 3 * 4)                #will multiply two numbers
print( 4 % 3)                #will print the remainder of two numbers
print( 4 / 3)                #will divide two numbers
print( 4 ** 3)               #will print the power of two numbers
print( 4 // 3)               #will print the quotient of two numbers 

#writing strings in python
print("Nazifi")
print("Jibril")
print("Nigeria")
print("I am enjoying 30 days of python")

#Checking data types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Nazifi'))
print(type("Jibril"))
print(type("Nigeria"))

#python datatypes
print(6)                  #integer
print(3.14)               #float 
print(3+3j)               #complex
print("Nazifi")           #string 
print(True)               #boolean
print([1,2,3])            #list
print((1,2,3))            #tuple
print({1,2,3})            #set
print({"name":"Nazifi"})  #dictionary

#Euclidean distance
import math
x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance)