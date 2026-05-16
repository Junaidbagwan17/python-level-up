# f887f6b2cf61a15eeb90201551a1616b58df394056b80ad90563283dacca4f70
import requests

BOT_TOKEN = "8834938535:AAHRXKiLecPlxScReSr1BqPHSfEzcGG2fgg" #"8675380241:AAH01PZ9vmeY5ubtyI1qitlr3u-78cXeBvQ"
CHAT_ID = "1439202338"         #https://api.telegram.org/bot12345:ABCXYZ/getUpdates

class NotificationManager:
    def send_message(self, message):

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        params =  {
            "chat_id":CHAT_ID,
            "text":message
        }

        response = requests.get(url=url, params=params)
        print(response.status_code)


