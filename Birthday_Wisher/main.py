##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
import datetime as dt
import pandas
import random
import smtplib

my_email = "VinnyThePinny@gmail.com"
password = "ThePinny/300496"

now = dt.datetime.now()
today_month = now.month
today_day = now.day

today = (today_month, today_day)
print(today)


def generate_email(elem):
    num = random.randint(1, 3)
    with open(f"./letter_templates/letter_{num}.txt", "r") as file:
        letter = file.read()
        with open("final_letter.txt", "a") as final:
            final = letter.replace("[NAME]", elem["name"])
    with smtplib.SMTP("smtp.gmail.com") as mail:
        mail.starttls()
        mail.login(my_email, password)
        mail.sendmail(
            from_addr=my_email,
            to_addrs=elem["email"],
            msg=f"Subject: Happy Birthday\n\n{final}"
        )



birthday_list = pandas.read_csv("birthdays.csv")
print(birthday_list)
birthday_dict = [{"name": data_row[0], "email": data_row[1], "month": data_row[3], "day": data_row[4]}
                 for (index, data_row) in birthday_list.iterrows()]
print(birthday_dict)

for elem in birthday_dict:
    if elem["month"] == today[0] and elem["day"] == today[1]:
        generate_email(elem)



