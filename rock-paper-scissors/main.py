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

#Write your code below this line 👇

import random

selection = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

if selection == "0":
  print(rock)
if selection == "1":
  print(paper)
if selection == "2":
  print(scissors)
hand1 = selection
print("Computer chose:")

rpslist = [rock, paper, scissors]
hand2 = random.choice(rpslist)
print(hand2)

if (hand1 == "0" and hand2 == paper) or (hand1 == "1" and hand2 == scissors) or (hand1 == "2" and hand2 == rock):
  print("You lose!")
elif (hand1 == "0" and hand2 == scissors) or (hand1 == "1" and hand2 == rock) or (hand1== "2" and hand2 == paper):
  print("You win!")
elif (hand1 == "0" and hand2 == rock) or (hand1 == "1" and hand2 == paper) or (hand1== "2" and hand2 == scissors):
  print("It's a draw")
else:
  print("Invalid input, you lose.")

#print(random.choice(rpslist))

#print(rock)