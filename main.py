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


import random
our_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
computer_choice = random.randint (0,2)

if our_choice == 0:
  print(rock)
elif our_choice == 1:
  print (paper)
elif our_choice == 2:
  print (scissors)

if our_choice < 0 or our_choice > 3:
  print ("You type an invalid number, you lose!")
else:
  print ("Computer chose:")
  if computer_choice == 0:
    print(rock)
  elif computer_choice == 1:
    print (paper)
  elif computer_choice == 2:
    print (scissors)

if our_choice == 0:
  if computer_choice == 0:
    print ("It\'s a draw")
  elif computer_choice == 1:
    print ("You lose")
  elif computer_choice == 2:
    print ("You win!")

if our_choice == 1:
  if computer_choice == 0:
    print ("You win!")
  elif computer_choice == 1:
    print ("It\'s a draw")
  elif computer_choice == 2:
    print ("You lose")

if our_choice == 2:
  if computer_choice == 0:
    print ("You lose")
  elif computer_choice == 1:
    print ("You win!")
  elif computer_choice == 2:
    print ("It\'s a draw")
