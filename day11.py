'''
Lists,Tuples...

#list --> Mutable,ordered,Heterogenous
#index(),count(),copy(),sort(),reverse()

details = ['codegnan',7,2018,'Hyderabad']
print(len(details))
print(datails.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21))#it returns first occurance
print(details.index(21,6))
#print(details.index('python'))#valueError


print(details.count(21))
print(details.count('python'))#it returns 0as we dont have it

data = ['codegnan','saketh','python','java']#input

0 : codegnan
1 : surendra
2 : python
3 : java

for obj in data:
    print(data.index(),':',obj)

for obj in range(len(data)):
    print(obj,':',data[obj])

#copy() -->shallow copy of the given collection

new = data.copy()
print(new)
print(type(new))
print(len(data))

new[2] = 'Agentic AI'
print(new)
print(data)

data.append('saketh')
print(data)
print(new)

data = [1,4,5,[21,34,45],23]
print(data)
new = data.copy()
print(new)

new[3][2] = 'Agents' #whenever we make changes in nested list original will
#also be effected
print(new)
print(data)


new[1] = 'python'
print(new)
print(data)


marks = [14,24,-45,27,35]
print(marks)
marks.sort()
#print(marks.sort()) #returns none
#print(marks) #returns in ascending order
marks.sort(reverse = True) #returns in Decending order..
print(marks)
marks.insert(2,'code')
#marks.sort()
#reverse() --> returns in reverse order
marks.reverse()
print(marks)
print(marks[::-1])

#type(),len(),max(),min(),print()

print(sorted('codegnan'))#returns list in ascending order
#print(sorted(['code','23',34,45]))#raises Error

#tuples -->Tuples are Indexed,ordered,Heterogenous,Immutable collection
#dimensions,coordinates,database records,we prefer () for tuple notat

a = ()
print(type(a))
print(len(a))

dimensions = 1.5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))
'''
#operations -->Indexing,slicing,strinding,membership,merging,Repetition

courses = ('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,61])
'''
print(courses)
print(len(courses))

print(courses[-2][-2:])
#courses[2] = 23 Tuples are Immutable
courses[-1].append('codegnan') #we can make any modifications inside list
print(courses)

#create a nested tuple as above and work o slicing ,striding and list function
print('PFS' in courses)#Membership
d = courses * 2  #repetition
print(d)
e = courses + (2,3,4,5) #merging
print(e)

#Tuples Immutable -->count(),index()
print(courses.index('AgenticAI'))#returns first occurance
print(courses.count('Agents'))

#print(courses.sort())#Attributeerror  -->sort() is  in list not in tuple

print(sorted(courses[-1]))
#print(sorted(courses))# as we have mixted type


#TypeCasting
d = tuple(sorted((23,12,3,4,5)))
print(d)

#accept group of integers space separted
a,b = map(int,input("enter the values").split())
print(a,b)

a = tuple(map(int,input("enter the values ").split(',')))
print(a)
print('9+4')
#eval() function can take any kind of input
print(eval('9+4'))

a = eval(input("enter a list:"))# in this case u can exctantly enter data as
print(a)
print(type(a))
'''
#task:take a user input as string ,do this in two ways..
'''
1) give the count of each repeating charster
TEST case 1: programming

r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2)
r is repeting 2 times
index = [1,4]
g is repeating 2 times
index = [3,10]
m is repeating 2 times
index = [6,7]









































































































































































































































































































