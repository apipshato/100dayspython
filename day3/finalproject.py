print("welcome to treasure island")
print("your misson is to find the treasure")
choice1 = input(
    "your at crrosroad, where do you want to go? type left or right: \n")

if choice1 == "left":
   choice2= input('you come to lake , there is ilandin the middle lake . type "wait" to for boat,type "swim" to wim accross').lower()
   if choice2 == "wait":
       choice3=input("you arrive at islan unharmed,  there is house 3 doors one red, one yellow one blue").lower()
       if choice3 == "red":
            print("your room full of fire")
       elif choice3 == "yellow":
            print("ypu found the treasure you wins")
       elif choice3 =="blue":
            print("you enter room of beast you lose")
       else:
          print("you you choice a door doesnt exist game oveer")
else:
  print("you got attacked by an angry trout, game over")
 
 