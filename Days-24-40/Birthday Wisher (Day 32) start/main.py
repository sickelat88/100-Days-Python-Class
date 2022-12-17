import datetime as dt
import smtplib
import random

now = dt.datetime.now()
my_email = "sickelat@gmail.com"
password = "ctbrqxdxggyfpphz"

with open("quotes.txt") as file:
    quote_list = file.readlines()
    quote = random.choice(quote_list)

if now.weekday() == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr="sickelat@gmail.com",
                            to_addrs="sickelat@gmail.com",
                            msg=f"Subject:Motivational Quote\n\n{quote}")