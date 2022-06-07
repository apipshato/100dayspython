print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0

if height >= 120:
  print('can ride')
  age=int(input("what is your age"))
  if age >= 12:
    bill=5
    print('child ticket all $5')
  elif age <= 18:
    bill=7
    print('adult ticekt all $7')
  else:
    bill=12
    print('$7')   
    
  wants_photo=input("do you wanna photos? Y or N")
  if wants_photo == 'Y':
    bill += 3
    print(f"your final {bill}")
else:
  print('cannot ride')