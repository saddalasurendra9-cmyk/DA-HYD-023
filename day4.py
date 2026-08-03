'''
Identity  operators --> checks the identity of an object -->

a = 5
b = a
print(id(a))
print(id(b))
c = 5
print(id(c))
print(a is c)
c = 5
print(id(c))
print(5 == 5)

a = [1,2,3,4,5]
b = a
print(id(a))
print(id(b))
c = [1,2,3,4,5]
print(id(c))
#as we have lists (mutual collection)
print(c is a) #output False
print(c == a) #output True
print(a is not c)

#Bitwise OPerators  --> we perform bitwise operators over oprands
#& (and), | (or),^(xor),shifting operators (<<,>>)
print(5& 3)# both 5 and 3 to be converted binary and bitwise and is performed
print(5|3) # bitwise OR
print(5^ 3) #bitwise XOR
print(5 and 3) #there and is logical operator checks for both existances

print(5 or 3)#returns 3 this case

#Leftshift operator  << ,Right shift operator>>
print(5 < 1) #False comparision
print(5 << 2)
print(5 >> 1)
print(5 << 2)

print(15 << 2) #convert  15 to binary and perform 2 times left shifiting
print(15 >>2) #same 2 times right shifting

#Input formatting -->input(),int(input()),float(input())
#you know -->single input
#2 or 3 inputs --> map()
#group of integers -->list(map(int,(input().spilit(','))

names = input("enter the names:").spilt(','))
print(name1,name2)

#Tokens -->Numeric Datatypes -->Opertors --.Flow of the program
#control block statements --
#conditional statements --> if,else,elif (rely on condition to be executed)
#repetion statemets (Loops) -->for,while

syntax :
     if  <condition>:
     statement(s)..
     .....
     
#age = 15
age = int(input("enter the age:"))
if age >=18:
    print('Your age is:',age)
    
age = int(input("Enter the age:"))
if age>=18 and age in [19,21,20]:
    print('your age is age',age)
    print(age)
    
#else keyword --> if-else
else:
    statement(s)..
          
#vote elibilty -->to check his/her voter elibility and give access..

age = int(input("enter the age:"))
if age>=18:
    print("you have voter elibilty and age is",age)
    print("access granted")
else:
              age = 18-age
              print("you dont have elibility as your age is",age,"years")
              print("you need to wait for more",age,"years")
              
#same case let's use only nested --> if,else
if age >0:
    if age>=18:
         print("you have voter elibilty and age is",age)
    print("access granted")
     else:
              age = 18-age
              #print("you dont have elibility as your age is",age,"years")
              print("you need to wait for more",age,"years")
else:
    print("you have enterted -ve values/Zero enter only +ve")
    
task :student marks and grade analayzer
90-100 -->'A'
80-89  -->'B'
70-79-->'c'
60-69 -->'D'
>60-->fail
# also -ve'''
# Student Marks and Grade Analyzer

marks = int(input("Enter student marks: "))

if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks <= 89:
    print("Grade: B")
elif 70 <= marks <= 79:
    print("Grade: C")
elif 60 <= marks <= 69:
    print("Grade: D")
elif 0 <= marks < 60:
    print("Result: Fail")
else:
    print("Invalid Marks! Please enter marks between 0 and 100.")
              




































































