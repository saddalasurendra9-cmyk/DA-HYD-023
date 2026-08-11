'''
#strings --> caseconversions,searching&finding,string testing methods,
#replace,space removal

#searching,finding,replacing,joining...
a = "Codegnan"
print(len(a))
print(min(a))
print(max(a))

b = a.index('g')#it returns the index position
print(b)
c = a.index('n')#it returns only the first occurance
print(c)
d = a.index('n',6) #it returns the next occurance
print(d)
#e = a.index('n',8)#valueError
#print(e)
#f = a.index('t')#valueError
#print(f)
g = a.index('n',1,4)
print(g)


#rindex() -->returns last occurance
b = a.rindex('g')
print(b)
c = a.rindex('n')#here 'n' is occuring at 7th index
print(c)
#d = a.rindex('n',8)#it returns valueerror
#print(d)

#count() -->returns the number of items object is repeating
print('codegnan'.count('n'))
print('code'.count('w'))#it returns 0 as we dont have 'w' in 'code'
print('cakshjasaksajs'.count('a'))

#find() -->first occcurance but it avoid error
#not found
print('codegnan'.find('r')) #it returns -1
print('codegnan'.find('n'))

a = "DataAnalysis"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))

#Replacing,splitting,Joining

#Strings are Immutuable
a = 'codegnan'
#a[4] = 's'
print(a)
a = a.replace('g','s')
print(a)
print('fghyujiki#jkasjkajska#nmasnam'.replace('#',''))
print(a.replace('x','saketh'))

a = 'code saketh python'
b = a.split() #by defalut if we have space it splits
print(b)
print(len(b))
c = 'code,saketh,python'
d = c.split()
print(d)
e = c.split(',')
print(e)
#join()
a = 'code'
b = 'gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('saketh'))
print(' '.join('sakketh'))

#string testing methods (boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()....

a = 'codegnan123'
print(a.isalnum())  #returns true for alphanumeric strings else false
b = 'codegnan'
print(b.isalnum())
print(a.isalnum()) #returns true only for alphabets
print(a.isdigit()) #returns true only for digit string
print('8106429771'.digit())
print('2345'.isnumeric()) #this has upper edge (number,fractions,romans)
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
#startswitch() -->how its starting
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endsswith('f'))
print('codegnan'.islower()) #returns true for all lowercase
print('c0degann'.isupper()) #returns true for all uppercase
print('codegnan python'.istitle())

#space removal --> strip() (removes leading and trailing spaces)
a = ' codegnan '
print(a.strip())
b = input("enter the string:").string().lower()
print(b)
'''
print('234'.zfill(4))
print('234'.zfill(7))

print('hai').center(6))
print('hai'.center(6,'#'))

print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))





















































































