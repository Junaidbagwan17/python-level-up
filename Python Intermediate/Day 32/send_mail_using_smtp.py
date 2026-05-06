import smtplib

my_email = "ml.technologia2026@gmail.com"
password = "bhjf dtsl ieaj xgyx"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)

connection.sendmail(from_addr=my_email,
                    to_addrs="miraroadauto@gmail.com",
                    msg="Subject:Hello\n\nThis is body of an mail!"
                    )

connection.close()