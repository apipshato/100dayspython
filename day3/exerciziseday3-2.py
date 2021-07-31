print("welcome to rollercoster")
height=input("what is your tall? \n")

if height > 120:
    print("he can play rollercoster")
    age = int(input("what is your age "))
    if age <12:
        print("please pay $5")
    elif age <= 18:
        print("please play $7")
    else:
     print("pelase pay $12")
else:
 print("sorryy, you can ride")
