# -------------------- SEND TELEGRAM MESSAGE --------------------
import requests

def send_telegram_message(message):

    BOT_TOKEN = "8834938535:AAHRXKiLecPlxScReSr1BqPHSfEzcGG2fgg"
    CHAT_ID = "1439202338"

    telegram_endpoint = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    telegram_parameters = {
        "chat_id": CHAT_ID,
        "text": message
    }

    telegram_response = requests.get(
        telegram_endpoint,
        params=telegram_parameters
    )

    telegram_response.raise_for_status()


# Example Test
send_telegram_message("🚀 Test message from Python bot!")