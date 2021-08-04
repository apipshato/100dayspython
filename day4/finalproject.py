import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image=[rock, paper, scissors]

user_choice=int(input("what do you choose ? type 0 for rock , 1 for paper, 2 for sciccors \n"))
print(game_image[user_choice])

computer_choice=random.randint(0,2)
print("computer choice: ")
print(game_image[computer_choice])

if user_choice >= 3 or user_choice <0
