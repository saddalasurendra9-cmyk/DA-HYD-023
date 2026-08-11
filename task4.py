'''
#n no of times enter the password until correct guess
password = input("Enter the password: ")

if password == "123":
    print("Correct guess")
else:
    print("Not correct")

#otp enter 
otp = input("Enter the OTP: ")

correct_otp = "1234"

if otp == correct_otp:
    print("OTP verified successfully")
else:
    print("Invalid OTP")
 
#max attempts 7
pin = "2612"
max_attempts = 7
current_attempts = 0
while current_attempts <= max_attempts:
    entered_pin = input("enter the atm pin:")
    if entered_pin == pin:
        print("login succesful")
        break
    else:
         print("Entered PIN is wrong ..try again carefully")
         current_attempts +=1
else:
    print("Account Locked ,Try after 24..hours")

food = input("enter the food items:")
count = 0
while food != "exit":
    count+=1
    food = input("enter the food items:")
print("total no of itmes ordered:",count)

#no of attempts
secret = "python"
current = 0
max_attempts = 3
while current <max_attempts:
    a=input()
    if (a==secret):
        print("access ")
        break
    else:
        remaining = max_attempts-current
        print(f,"wrong guess you have only")
              count +=1
else:
     print("changes over")
'''
password =input("enter the value:")
if password =="123":
     print("you are enter greater num")
     if password >"123":
       print("you are enter smaller num")
     if password < 123:
         print("correct guess")
else:
    print("Not correct")




































    


























































































