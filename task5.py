'''
#task1
name = input("enter the name:")
methods = ["upper","lower","title","capitalize","swapcase","isupper"]
for i in methods:
        if i == 'upper':
            print("upper  :",name.upper())
        elif i == 'lower':
            print("lower  :",name.lower())
        elif i   == 'title':
            print("title  :",name.title())
        elif i   == 'capitalize':
            print("capitalize  :",name.capitalize())
        elif i  == 'swapcase':
            print("swapcase  :",name.swapcase())
if name.isupper():
  print("Original text is uppercase",true)
else:
    print("Original text is uppercase",false)
if name.islower():
  print("Original text is lowercase",true)
else:
    print("Original text is uppercase",false)
if name.istitle():
  print("Original text is title case",true)
else:
    print("Original text is uppercase",false)
#task
print("STUDENT REPORT".center(40, "="))

students = []

for i in range(3):
    name = input("Enter student name: ")

    marks = int(input("Enter marks: "))

    while marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        marks = int(input("Enter marks: "))

    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    students.append((name, marks, grade))

print("=" * 40)
print("Name".ljust(20) + "Marks".rjust(8) + "Grade".rjust(10))
print("=" * 40)

for name, marks, grade in students:
    print(f"{name.ljust(20)}{str(marks).rjust(8)}{grade.rjust(10)}")

print("=" * 40)
 '''              


























































