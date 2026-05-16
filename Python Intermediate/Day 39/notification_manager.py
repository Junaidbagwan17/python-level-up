import requests

BOT_TOKEN = "YOUR BOT TOKEN from BOTFATHER
CHAT_ID = "YOUR CHAT ID FROM GIVEN LINK"         #https://api.telegram.org/bot12345:ABCXYZ/getUpdates

class NotificationManager:
    def send_message(self, message):

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        params =  {
            "chat_id":CHAT_ID,
            "text":message
        }

        response = requests.get(url=url, params=params)
        print(response.status_code)


