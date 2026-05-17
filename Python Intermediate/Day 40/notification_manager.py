import requests
import  smtplib

from proto.marshal.compat import message

BOT_TOKEN ="YOUR TOKEN
CHAT_ID = "YOUR CHAT ID FROM GET UPDATES URL"         #https://api.telegram.org/bot12345:ABCXYZ/getUpdates

class NotificationManager:
    def send_message(self, message):

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        params =  {
            "chat_id":CHAT_ID,
            "text":message
        }

        response = requests.get(url=url, params=params)
        print(response.status_code)

    def send_email(self, user_email, sendemail_alert):
        my_email = "ml.technologia2026@gmail.com"
        password = "bhjf dtsl ieaj xgyx"

        with smtplib.SMTP("smtp.gmail.com") as connetion:
            connetion.starttls()
            connetion.login(my_email, password)
            connetion.sendmail(from_addr=my_email, to_addrs=user_email, msg=sendemail_alert.encode("utf-8"))
