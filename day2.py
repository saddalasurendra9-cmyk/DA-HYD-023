'''
TOKENS --> variables,punctures

variaables --> Named memory locaton,its a placholder for data
#Rules are to be followed
'''
#MultiAssignment of variables
'''
name,age,place = 'Codegnan',7,'Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='---->')
'''


'''
#a,b = 2,4,5#value error as too many to pack
#Reassigning variables
name = "codegnan"
a,b = 45,1.5

print(a,b)
a,b = b,a #swapping
print(a,b,sep=',')

 #Deleting the variables -->
#del a
#print(a)
#del a,b
print(a,b)
'''
#punctuators -->{}(dict,sets),[](lists),()(tuples)
'''
name = "codegnan";age = 7;course = 'data analysis'

print(name,age,course)'''

 #datatypes -->Numeric  (int,float,complex),boolean,none,
                     #Sequences -->Lists,Tuples,Sets,strings,
                     #             Frozensets,mappings(dist)

#Numeric type -->int,float,complex
#int datatype  -->quantity,age
'''
age = 7
print(age)
print(type(age)) #type -->returns the datatype of object
print(type(234))
'''
#quantity = 03 it is not allow
#print(quantity)
                     
#float datatype  -->temp,salary,price
'''
price = 750.24;discount = 2.5
print(price,discount)
print(type(price))
'''
#complex -->combation of real and imag
'''
i2 = 4
data= 5+i2
print = (data)

data = 5+2j #j is  imag representation
print(data)
print(type(data))

#Boolean -->True / False

Valid = True
print(type(Valid))

error = False
print(type(error))

#typecasting  --> Converting one type to another type
#python by defalut follows implict type (we need mention the daatype)
#we go explict type
#every built-in datatype is a built-in function
int,float,complex,bool

#Typecasting --> int -->float,complex,bool

age = 35
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age)
print(d)
e = bool(0)
print(e)

#float -->typecasting
price = 35.11
print(type(price))
b = int(price)
print(b)
c = complex(price)
print(c)
d = bool(price)
print(d)
e = bool(0)
print(e)


#complex -->typecasting
data= 3+2j
print(type(data))
#b = int(data) #typeerror
#print(data)
#c = float(data)
#print(data)
#c = float(data)
#print(c)
d = bool(data)
print(d)
print(type(d))

d = 5+4.5
print(d)


e = int(float(bool(45)))
print(e)

f = 45+2.5+2+3j+False
print(f)
 '''                    


































