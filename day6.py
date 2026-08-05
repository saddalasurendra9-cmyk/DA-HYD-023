'''
control statements --> control of Flow of execution of the program
                       --> conditional statements --> if,elif,else...
                        -->Repetition statements(Loop) --> for,while (for with else)
                                                               (while with else)
                       --> Jumping statements -->break,continue,pass

#Loops  --> Loops are helpful for repetition (Automative tasks)
#for ketword will be helpful to iterate over a sequence /range
#syntax for (for keyword):

for <temp_var> in sequence /range:
     statement(s)....
     .......

#range(stop)--> defalut 0 ends at stop-1
#range(start,stop,step)
#by defalut range picks 0 as start value
for i in range(10):
    print(i)
#In above case we got 10 iterations
for i in range(1,10):
    #if i > 5:
        #print(f'value of i is -->{i}')
    #Now i want to get only even numbers with above condition 
   if i > 5 and i%2 == 0:
       print(f'final value of i is --> {i}')
  
#Range(start,stop,step) -->here step -->interval..
for i in range(1,10,1):
    print(i)
    print("done")
       
for i in range(1,10,2):
    print(i)
    print("done")

for i in range(-1,-10,-1):
    print(i)
    print("done")

#[] -->we generally lists
names = ['saketh','sai kiran','surendra']
print(len(names))#len(obj) -->returns the number of items in a container
for name in names:
    #print(name)
    #print(f'student Name is {name}')
    if name == "sai kiran":
        print(f"student name is {name}")

  #calculate the sum of first 10 numbers
#first understand your input --> range(11) -->10 numbers 
#second understand your output --> sum (number)
 # third we need to map the logic
result  == 0 #target variable
for i in range(11):
    
    #print(i)
    #print(f'result is {i+i}')
    result =result + i#result+=i
    print(f'Now the result is {result}')
print(f'sum of 10 numbers is {result}')

result  == 0 #target variable
for i in range(21):
    if i %2 == 0:
        result = result + i#result+=i
print(f'sum of 10 numbers is {result}')
'''
#understand the loops usage with fitness streak example
#work_out -->1,work_out_missed -->

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
print(f'longest streak is {longest_streak}')
 
    
    











































