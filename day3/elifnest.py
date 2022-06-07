print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print('can ride')
  age=int(input("what is your age"))
  if age >= 12:
    print('$5')
  elif age <= 18:
    print('$12')
  else:
    print('$7')   
else:
  print('cannot ride')