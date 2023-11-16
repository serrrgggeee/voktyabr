import datetime as dt 
from django.conf import settings
import requests

def send_to_vk_group(message, chatID):
    apiURL = f'https://api.vk.com/method/wall.post?owner_id=-{chatID}&message={message}&from_group=1&access_token={settings.API_TOCKEN_VK}&v=5.131'
    try:
        requests.get(apiURL)
    except Exception as e:
        pass # TO DO logs

def check_time():
    start = dt.time.fromisoformat('09:00')
    end = dt.time.fromisoformat('21:30')
    current_time = dt.datetime.now().time()
    if current_time < start: return
    if current_time > end : return
    return True



