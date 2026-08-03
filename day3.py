#Numeric  datatypes  --> int ,float ,complex along with boolean

#input fornatting  -->accepting input from the user --> input()

#accepting intger input from user
#by defalut int()accepts any input -->str
#input(input()) -->will accept only integers

age = input('Enetr the age:')
print(age)
print(type(age))

'''
#float of input -->
age =float(input('Enetr the age:'))
print(age)
print(type(age))

# accepting string input from user

name = input("enter the name:")
print(name)
print(type(name))

#accept group of value

marks = int(input("enter the marks:")).split()
print(marks)

a = input().split()#by default split()has space
print(a)

#space separted values
a = input().split() #now you enter apces in output
print(a)
#comma separted values
a = input("enter the values:").split()
print(a)

#Lists of intergers
marks = list(map(int,input("enter the values:").split(',')))
print(marks)

#now we want to accept 2 values fron user

age,salary = map(int,input("enter the values:").split(','))
print(age)
print(salary)

#single input --> int(input())
#two inputs -->a,b = map(int,input().spilt(',')
#any number results as list --> a= list(map(int,input().spilt(',')))
age,salary = map(float,input("enter the values:").split(','))
print(age)
print(salary)

marks = list(map(float,input("enter the values:").split(','))
print(marks)
#accepting input from user -->int,float --> input formatting
# opertaors perform perform between vaues (oprands)
#7 types --> arthimetic ,assignment,comparison,(relationship)
#Membership,identity,logical,bitwise
#arthimetic opertors -->a o
#+,-,*,\
print(5+1)
print(5-1)
print(5*1)
print(5/3)#float value
#floor division (integer division) -->returns qutionent
print(5//6)
#power (expotintial)
print(5**6)
#% modulus -->divisiable rules ->returns remainder
print(5%5)

#Task ->ArithmeticError Accept integer input as length ,breath -->find the area of rectangle
#area = length * breadth
length,breadth = map(int,input("enter the values").split(','))
area = length * breadth
print(area)

#Assignment operators -->assign the values
# =,+=,-=
a = 45
print(a)
#update the value of a
a = a+5 #a+= 5
print(a)
b = 35
b += a #b = b+a
print(b)
b -= 5 #b = b-5
print(b)
  
#Task : *=, /=,%=,** task

#comparison opertors --> we compare the values --> boolean
# ==equal to ,!= not equal to,

#<=,>=

age = 25
print(age == 25) #returns boolean output
print(age !=35)
print(-5 < -1)

#Membership oparetors --> in,not in -->boolean
#it checks for the existence of an object in acollection

marks = [56,75,45,85]
print(35 in marks )
#print(35 in 355 )#typeerror

print(25 not in marks)
print('code' in 'codegnan')
print('$' in 'abc$frg')

#logical opertors --> logical decision making ---> and or, not
#and -->all conditions to the be statifird
#or -->any one condition to be satisfied

a + (25 in [25,45,65]) and 45 < 56
print(a)
b = 45 > 56 or 25 <= 45
print(b)
c  = not(True)
print(c)


#identity opertors  --> check for identity of an object -->

a = 35
b = 35
print(id(a))
print(id(b))
print(a is b)
c = a
print(id(c))
print(c is a)
a = [1,2,3,4]
print(id(a))
c = a
print(id(c))
print(c is a)
b = [1,2,3,4]
print(id(b))'''



























