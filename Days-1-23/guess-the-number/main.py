#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

def make_guess(guess):
  """Function used to make a guess of the number."""
  if guess == random_number:
    print(f"You got it! The answer was {random_number}")
    return 0
  elif guess > random_number:
    print("Too high.\nGuess again.")
    return number_of_attempts - 1
  elif guess < random_number:
    print("Too low.\nGuess again.")
    return number_of_attempts - 1

print(logo)
print("Welcome to the Number Guessing Game!\nI'm Thinking of a number between 1 and 100")
random_number = random.randint(1,101)
print(f"Pssst, the correct answer is {random_number}") #remove

difficulty = "select"
number_of_attempts = 0

while difficulty != "easy" and difficulty != "hard":
  difficulty = input("Choose a difficulty.  Type easy or hard: ").lower()
  if difficulty == "hard":
    number_of_attempts = 5
  elif difficulty == "easy":
    number_of_attempts = 10
  else:
    print("Invalid selection, try again.")

while number_of_attempts > 0:
  print(f"You have {number_of_attempts} remaining to guess the number.")
  guessed_number = int(input("Make a guess: "))
  number_of_attempts = make_guess(guessed_number)
  if number_of_attempts == 0:
    print("You've run out of guesses, you lose.")
