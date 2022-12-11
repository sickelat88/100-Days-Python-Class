
# pull list of names
with open("C:./Input/Names/invited_names.txt", mode="r") as name_list:
    names = name_list.readlines()

# new list of names after formatting
new_names = []

# format list of names
for i in names:
    updated_name = i.replace("\n", "")
    new_names.append(updated_name)

for each_name in new_names:
    # read the letter template
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        letter_data = letter.read()

    # replace the target name
    letter_data = letter_data.replace("[name]", each_name)

    # write the letter with new name to new letter
    with open(f"./Output/ReadyToSend/{each_name}.txt", mode="w") as letter:
        letter.write(letter_data)

