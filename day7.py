'''
#usage of else with
work_log = [0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak =0 #target variable
current_streak =0
for day in work_log:
    if day == 1:
    #print(day)
     current_streak = current_streak + 1
     if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
    else:
        current_streak = 0 #streak breaks
else:
print(f'longest streak is {longest_streak}')
#In this case when the entire loop execution is done we gets result of
#else block
work_log = [0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak =0 #target variable
current_streak =0
for day in work_log:
    if day == 1:
    #print(day)
     current_streak = current_streak + 1
     if current_streak > longest_streak:
            longest_streak = current_streak
            print(f'Longest streak is {longest_streak}')
            break
    else:
        current_streak = 0 #streak breaks
else:
    print(f'longest streak is {longest_streak}')

#for-else with notifications scenario
notifications = [0,0,0,0]
for notification in notifications:
    if  notification == 1:
        print('unread notification')
        break
else:
    print('all caught up')
  
notifications = [0,0,1,0]
notifications = list(map(int,input("enter the values -->0 or 1:").split(',')))
for notification in notifications:
    if  notification == 1:
        print('unread notification')
        break
else:
    print('all caught up')
'''
#while --> it replies on  condition ,it will be completely executed until the
#condition is satified..
'''
syntax while:

while <condition>:
      ststement(s)....
      ......
      ....

while True:
    print("no")
    
#It runs an infinite loop we need to press ctrl+c (keyboard interrupt)
i = 10#intialised statement
while i>=1:
    print(i)
    i=i-1 #counter

i = 0
while i<=10:
    print(10-i)
    i = i+1
'''
#banking scenario --> PIN authentication if more than 3 attempts
#Account locked..
pin = "2612"
max_attempts = 3
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
          






























    


    
    



























    



































