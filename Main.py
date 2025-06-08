import requests
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        r = requests.post(url, json=payload)
        print("Message sent:", r.text)
    except Exception as e:
        print("Failed to send message:", e)

# Test poruka kad se pokrene bot
if __name__ == "__main__":
    send_message("✅ Bot je aktivan i radi na Render platformi!")
    while True:
        time.sleep(3600)  # Radi u petlji, da Render ne ugasi servis
