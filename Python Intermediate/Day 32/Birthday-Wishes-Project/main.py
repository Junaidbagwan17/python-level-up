import pandas
import smtplib
import random
import datetime as dt
import os

# Get today's date
now = dt.datetime.now()
today_month = now.month
today_day = now.day

# Get GitHub secrets
email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

# Read CSV file
data = pandas.read_csv("birthdays.csv")

# Default values
person_name = None
person_email = None

# Check birthdays
for index, row in data.iterrows():

    if row["day"] == today_day and row["month"] == today_month:
        person_name = row["name"]
        person_email = row["email"]

# Send email only if birthday found
if person_name is not None:

    # Choose random letter
    letter_digit = random.randint(1, 3)
    selected_letter = f"letter{letter_digit}.txt"

    # Read letter
    with open(selected_letter, "r") as letter_file:
        content = letter_file.read()

    # Replace placeholder
    letter_to_send = content.replace("[NAME]", person_name)

    print(letter_to_send)

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:

        connection.starttls()
        print(email)
        print(password)

        connection.login(
            user=email,
            password=password
        )

        connection.sendmail(
            from_addr=email,
            to_addrs=person_email,
            msg=f"Subject:Happy Birthday 🎉\n\n{letter_to_send}".encode("utf-8")
        )

    print("Birthday email sent successfully 🚀")

else:
    print("No birthdays today")
