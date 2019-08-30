#DAY 1 AND DAY 2 Python comments
print ("Day 1 and 2 Python Print function and Comments : \n\n")
#comment
#print("Hello,World")
"""
multiline comment is here 
"""
print("hi")#comment

#####################
print("\n***********************")

#DAY 3 Variables
print ("\nDay 3 Python Variables : \n\n")
x = 5
y = "john"
print(x)
print(y)

x = 4 #x1 is a type of int 
x = "sally" #x1 is a type of string
print(x)
x = "john"
#same as
x = 'john'
#double quotes is the same as single quotes
print(x)
x , y, z = "orange","banana" , "cherry"
print(x+" "+y+" "+z)


##################
x = y= z = "orange"
print(x+" "+y+" "+z)
##################


x="awesome"
print("python is "+x)

x = "python is "
y="awesome"
z= x+y
print(z)

##################
x = 5
y = 10
print(x+y)
##################

x = 5
y = "john"
#print(x + y)

##################
print("\n*********************")

#Day 4 Python Numbers
print ("\nDay 4 Python Numbers : \n\n")
x = 1   # int
y = 2.8 # float
z = 1j  # complex

print ("type of x " ) 
print (x) 
print(type(x)) 
print( "type of y ") 
print(y) 
print( type(y)) 
print("type of z ") 
print (z) 
print(type(z))

##################

x = 1
y = 3234543434345432
z = -2334556

print ("\ntype of x " ) 
print (x) 
print(type(x)) 
print("type of y ") 
print(y) 
print( type(y)) 
print("type of z ") 
print (z) 
print(type(z))

##################
x = 1.10
y = 1.0
z = -234.55

print ("\ntype of x " ) 
print (x) 
print(type(x)) 
print("type of y ") 
print(y) 
print( type(y)) 
print("type of z ") 
print (z) 
print(type(z))
##################
x = 35e3
y = 12E5
z = -234.e55

print ("\ntype of x " ) 
print (x) 
print(type(x)) 
print("type of y ") 
print(y) 
print( type(y)) 
print("type of z ") 
print (z) 
print(type(z))

##################

x = 3+5j
y = 5j
z = -3j

print ("\ntype of x " ) 
print (x) 
print(type(x)) 
print("type of y ") 
print(y) 
print( type(y)) 
print("type of z ") 
print (z) 
print(type(z))

##################

x = 1   # int
y = 2.8 # float
z = 1j  # complex

#convert from int to float :
a = float(x)

#convert from float to int :
b = int(y)

#convert from int to complex

c = complex (x)

print("\n type of a")
print(a)
print(type(a))

print("\n type of b")
print(b)
print(type(b))

print("\n type of c")
print(c)
print(type(c))
##################

import random 
print("\nrandom number : ")
print(random.randrange(1,10))

#Day 4 Python Numbers
print ("\nDay 5: \n\n")
x = "apple" 
y = "orange" 
z = "limon"
basket = x + y + z
print(basket)