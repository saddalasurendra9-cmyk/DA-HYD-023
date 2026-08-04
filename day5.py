'''
students marks and grade analazer (if-else)
90 - 100 --> 'A'
80 - 89 --> 'B'
70 - 79 --> 'C'
60 - 69--> 'D'
<60 --> fail
#also -ve cases should not be allowed and marks should be greater  100
marks = int(input("enter the marks (1-100):"))
if marks > 0 and marks <=100:
  if marks >= 90:
      print("user has secured Grade A")
  if marks >=80 and marks <=89:
      print("user has secured Grade B")
  if marks >=70 and marks <=79:
      print("user has secured Grade c")
      if marks >=60 and marks <=69:
       print("user has secured Grade d")
      if marks <60:
       print("user has failed,study again")
else:
        print("enter only +ve values greater than 0 and less than 100")
        
        #elif keyword --> if-elif-else
if <condition>:
    statement(s)...
    elif <condition>:
        statement(s)...
    elif <condition>
        statement(s)...
    else:
        statement(s)....
        
marks = int(input("enter the student marks:"))
if marks >=100:
    print("enter values should be greaer than 1 and less than 100")
 elif marks >=90 and marks <=100:
     print("user has secured Grade A")
 elif marks >= 80 and marks <= 89:
     print("user has secured Grade B")
     elif marks >= 70 and marks <= 79:
     print("user has secured Grade c")
     elif marks >= 60 and marks <= 69:
     print("user has secured Grade D")
     elif marks >= 60 and marks >= 0:
       print("user has failed ,study again")
       else:
           print("no negative values '
 #Task --> same usecase tyr with if-elif-else usaage in other way
#voter eligibility checkcase --> make sure to satify all possible conditions
#>=18 and 100 -->Access
'''                 
   


































     
