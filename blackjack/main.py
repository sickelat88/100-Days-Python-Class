import random
from replit import clear

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards."""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
  return sum(cards)

# Compare the two
def compare(user_score_comp,computer_score_comp):
  if user_score == computer_score:
    return "It's a draw!"
  elif computer_score == 0:
    return "You lose! Computer has Blackjack"
  elif user_score > 21:
    return "You lose! You went over"
  elif user_score == 0:
    return "You win! You got Blackjack"
  elif computer_score > 21:
    return "You win! Computer went over"
  elif user_score > computer_score:
    return "You win! You got the highest score"
  else:
    return "You lose! You got the lowest score"

new_game = input("Do you want to play a game of Blackjack? Y or N: ").lower()
while new_game == "y":
  from art import logo
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
      
  # User
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_deal = input("Draw another card? Y or N ")
      if user_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  # Computer
  while computer_score in range(1,17):
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"  You final hand: {user_cards}, final score: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, computer's score: {computer_score}")
  
  print(compare(user_score,computer_score))
  
  new_game = input("Do you want to play a game of Blackjack? Y or N: ").lower()
  clear()


