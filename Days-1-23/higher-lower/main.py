from art import logo, vs
from game_data import data
import random
from replit import clear

# Function to pull a new selection and format it
def selection():
  """Function to pull a new selection"""
  new_selection = random.choice(data)
  return new_selection

# Function to extract fields from selection dictionary
def dict_extract(selection_to_parse):
  """Function to extract fields from selection dictionary"""
  name = selection_to_parse["name"]
  description = selection_to_parse["description"]
  country = selection_to_parse["country"]
  return f"{name}, a {description}, from {country}"
  
# Function to extract number of followers
def dict_extract_followers(selection_to_parse):
  """Function to extract number of followers"""
  followers = selection_to_parse["follower_count"]
  return followers

#Function to compare and calculate score
def compare(the_users_selection,followers_a, followers_b):
  """Function to compare and calculate score"""
  global user_points
  global game_over
  if the_users_selection == "a":
    if followers_a > followers_b:
      user_points = user_points + 1
      return f"You're right! Current score: {user_points}"
    elif followers_a < followers_b:
      game_over = True
      return f"Sorry, that's wrong. Final score: {user_points}"
  elif the_users_selection == "b":
    if followers_b > followers_a:
      user_points = user_points + 1
      return f"You're right! Current score: {user_points}"
    elif followers_b < followers_a:
      game_over = True
      return f"Sorry, that's wrong. Final score: {user_points}"

#global variables
user_points = 0
game_over = False

# First Selections
selection_a = selection()
selection_b = selection()
# Ensure not the same selections
while selection_a == selection_b:
  selection_a = selection()
  selection_b = selection()
# Get followers counts
followers_count_a = int(dict_extract_followers(selection_a))
followers_count_b = int(dict_extract_followers(selection_b))
user_selection = "none"


# START GAME
print(logo)
while not game_over:
  
# Present game to user
  print("Compare A: " + dict_extract(selection_a))
  print(vs)
  print("Against B: " + dict_extract(selection_b))
  # print(followers_count_a) #remove
  # print(followers_count_b) #remove
  while user_selection != "a" and user_selection !="b":
    user_selection = input("Who has more followers? Type A or B: ").lower()

  clear()
  print(logo)
  outcome = compare(user_selection,followers_count_a,followers_count_b)
  print(outcome)
  
  # prep for next game
  selection_a = selection_b
  followers_count_a = followers_count_b
  selection_b = selection()
  while selection_a == selection_b:
    selection_b = selection()
  followers_count_b = int(dict_extract_followers(selection_b))
  user_selection = ""



