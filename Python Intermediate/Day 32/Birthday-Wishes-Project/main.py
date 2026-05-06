import pandas
import smtplib
import random
import datetime as dt
import os

now = dt.datetime.now()
year = now.year
today_month =  now.month
today_day = now.day

data = pandas.read_csv("birthdays.csv")

# loop through each row of the csv file
for index, row in data.iterrows():
    # check if today's month and day # matches birthday month and birthday day
    if row["day"]==today_day and row["month"] == today_month:
        person_name = row["name"]
        person_email = row["email"]

letter_digit = random.randint(1,3)
selected_letter = f"letter{letter_digit}.txt"

with open(selected_letter, "r") as letter_file:
    content = letter_file.read()
    # print(content)

to_replace = "[NAME]"
letter_to_sent = content.replace(to_replace, person_name)
print(letter_to_sent)

# Get email credentials from GitHub Secrets

email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=person_email,
                        msg=f"Subject:Happy Birthday 🎉\n\n{letter_to_sent}".encode("utf-8"))
    print("mailsend")
