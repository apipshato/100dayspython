print("welcome to pizza Pyton delivers")
size= input("what size pizza do you want ? S M OR L ")
add_paperoni=input("do you want paperoni? y or n? ")
extra_chesse=input("do you want cheese? ")


bill=0
if size == "S":
  bill += 15
elif size == "M":
    bill+= 20
elif size == "L":
    bill += 25

if add_paperoni == "Y":
    if  size == "S":
        bill += 2
    else:
        bill +=3


