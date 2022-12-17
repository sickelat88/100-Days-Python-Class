import datetime as dt
import smtplib
import pandas
import random

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

my_email = "sickelat@gmail.com"
password = "ctbrqxdxggyfpphz"

b_days = pandas.read_csv("birthdays.csv")

b_days_dict = {(row.month,row.day): row for (index, row) in b_days.iterrows()}
b_day_person = b_days_dict[today]["name"]
b_day_email = b_days_dict[today]["email"]

if today in b_days_dict:
    letter_num = random.randint(1, 3)
    with open(fr"C:\Users\Andrew\PycharmProjects\100-Days-Python-Class\Days-24-40\birthday-wisher-normal-start Day 32\letter_templates\letter_{letter_num}.txt") as letter:
        b_day_letter = letter.read()
        b_day_letter = b_day_letter.replace("[NAME]", b_day_person)
        print(b_day_letter)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr="sickelat@gmail.com",
                            to_addrs=b_day_email,
                            msg=f"Subject:Happy Birthday\n\n{b_day_letter}")



