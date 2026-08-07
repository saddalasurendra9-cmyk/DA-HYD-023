'''#Task
num = int(input('enter the value:'))
a=0
b=1
for i in range(num):
    print(a, end=" ")
    c = a+b
    a=b
    b=c

m = int(input the enter the value'))
a=0
b=1
i=0
while i<m:
    print(a,)
    print(a, end=" ")
    c= a+b
    a=b
    b=c
    i+=1
#count run ,four,dotballs,and total score
runs = list(map(int,input("enter the value:").split(',')))
total_score,boundaries,dotballs=0
for i in runs:
    total_score+=i
    if i==4 or i==6:
        boundaries +=1
    elif i==0:
        dotballs+=1
print("total_score",total_score)
print("boundaries",boundaries)
print("dotballs",dotballs)


runs = list(map(int,input("Enter the runs (comma-separated): ").split(",")))

total_score = 0
boundaries = 0
dotballs = 0

for i in runs:
    total_score += i

    if i == 4 or i == 6:
        boundaries += 1
    elif i == 0:
        dotballs += 1

print("Total Score:", total_score)
 print("Boundaries:", boundaries)
print("Dot Balls:", dotballs)

pin = "1234"
max_attempts = 5
current_attempts = 0
while current_attempts <= max_attempt:
    entered_pin = input("enter the atm pin:")
    if entered_pin == pin:
        print("login succesful")
        break
        #continue# it holds for this condition and skips to the part
    else:
         print("Entered PIN is wrong ..try again carefully")
         current_attempts +=1
else:
    print("Account Locked ,Try after 24..hours")
          

'''




























          
