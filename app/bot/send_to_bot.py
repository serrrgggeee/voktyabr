import datetime as dt 
from django.conf import settings
import requests


BOT_API_TOCKEN = getattr(settings, "BOT_API_TOCKEN", None)

def send_to_telegram(message, chatID):
    apiURL = f'https://api.telegram.org/bot{BOT_API_TOCKEN}/sendMessage?chat_id=@{chatID}&text={message}'
    try:
        send_messages(apiURL)
    except Exception as e:
        pass

def check_sending_time():
    start = dt.time.fromisoformat('09:00')
    end = dt.time.fromisoformat('21:30')
    current_time = dt.datetime.now().time()
    if current_time < start: return
    if current_time > end : return 'late'
    return True

def get_chat_url(chatID, text):
    return f'https://api.telegram.org/bot{BOT_API_TOCKEN}/sendMessage?chat_id={chatID}&text={text}'


def send_messages(apiURL):
    requests.get(apiURL)

