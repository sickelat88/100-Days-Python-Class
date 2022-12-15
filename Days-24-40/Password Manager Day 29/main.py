from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for item in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for item in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for item in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_email = email_entry.get()
    new_website = website_entry.get()
    new_password = password_entry.get()
    new_data = {
        new_website: {
            "email": new_email,
            "password": new_password,
        }
    }

    is_ok = messagebox.askokcancel(title=new_website, message=f"These are the details entered: \nEmail: {new_email} \nPassword: {new_password} \nIs it ok to save?")

    if is_ok:
        if len(new_website) == 0 or len(new_password) == 0 or len(new_email) == 0:
            messagebox.showerror(message="Please don't leave any fields empty!")
            return
        # file = open("data.txt", "a")
        # file.write(f"{new_website} | {new_email} | {new_password}\n")
        try:
            file = open("data.json", "r")
            ## reading old data
            data = json.load(file)
            ## updating old data with new
            data.update(new_data)

            file = open("data.json", "w")
            # saving the data
            json.dump(data, file, indent=4)

            file.close()
        except FileNotFoundError:
            file = open("data.json", "w")
            # saving the data
            json.dump(new_data, file, indent=4)
        else:
            email_entry.delete(0, END)
            email_entry.insert(0, "andrew@gmail.com")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_input = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            found = False
            for website in data:
                if website == website_input:
                    email = data[website]["email"]
                    password = data[website]["password"]
                    messagebox.showinfo(message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
                    found = True
            if not found:
                messagebox.showinfo(message=f"No details for {website_input} exists")
    except FileNotFoundError:
        messagebox.showinfo(message="No file found")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "andrew@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)



window.mainloop()
