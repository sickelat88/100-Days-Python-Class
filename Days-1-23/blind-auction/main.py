from replit import clear

from art import logo

print(logo)

bid_dict = {}
new_bid = True

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = int(bidding_record[bidder])
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while new_bid == True:
  name = input("What is your name?: ")
  bid = input("What is your bid?: $")
  bid_dict[name] = bid
  ask = input("Are there any other bidders? Type yes or no ")
  clear()
  if ask == "no".lower():
    new_bid = False
    find_highest_bidder(bid_dict)

#
#print(bid_dict)
#print(f"The top bidder is none with a bid of ${top_bid}.")


# bid_amount_list = []
# bid_index = 0

# for bid in bid_list:
#   to_add = bid_list[bid_index]["bid_amount"]
#   bid_index = bid_index + 1
#   bid_amount_list.append(int(to_add))
  
# top_bid = (max(bid_amount_list))

# print(top_bid)
# print(bid_list)





