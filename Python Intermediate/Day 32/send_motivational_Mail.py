import datetime as dt
import smtplib
import random

# GET A QUOTES from FILE txt
with open(file="quotes.txt",encoding="utf-8") as quotes_file:
    contents = quotes_file.readlines()
    # print(contents)

# GET A RANDOM QUOTES FROM contents list
random_quotes = random.choice(contents)
print(random_quotes)

# using DateTIME module class and method get weekday
now = dt.datetime.now()
current_day = now.weekday()
print(current_day)

# Mail the quote using smtp

my_email = "ml.technologia2026@gmail.com"
password = "bhjf dtsl ieaj xgyx"

if current_day == 2:
   with smtplib.SMTP("smtp.gmail.com") as connection:
       connection.starttls()
       connection.login(user = my_email, password=password)
       connection.sendmail(from_addr=my_email,
                           to_addrs="miraroadauto@gmail.com",
                           msg=f"Subject:Today\'s Motivation for You!\n\n{random_quotes}".encode("utf-8"))
       print("The email was sent successfully.")