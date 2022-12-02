#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_input = float(input("What was the total bill? $"))
tip_input = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_input = int(input("How many people to split the bill? "))

bill_per_person = tip_input / 100 + 1

#total_input_float = float(total_input)
#tip_input_int = int(tip_input)
#people_input_int = int(people_input)

result = round((total_input/ people_input) * bill_per_person, 2)
result = "{:.2f}".format(result)

print(f"Each person should pay: ${result}")