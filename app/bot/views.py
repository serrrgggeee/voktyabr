from article.models import Article
from bot.models import TgUser
from bs4 import BeautifulSoup
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import requests


logger = logging.getLogger(__name__)


def check_user_in_group(userId, apiToken):
	chatID = 'avoska_october'
	apiURL = f'https://api.telegram.org/bot{apiToken}/getChatMember?chat_id=@{chatID}&user_id={userId}'
	return requests.get(apiURL)


keyboard = json.dumps({'inline_keyboard':[[{"text":"get_user_ads","callback_data":"clicked"}]]})
def send_menu(text, token, chatID, parse_mode="HTML", reply_markup=keyboard):
    data={'chat_id': chatID, 'text': text, 'parse_mode': parse_mode, 'reply_markup': reply_markup}
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    return requests.post(url=url,data=data)


@csrf_exempt
def search(request):
	body = json.loads(request.body)
	apiToken = getattr(settings, "BOT_API_TOCKEN", None)

	if 'message' in body:
		search_handler(body['message'], apiToken)

	if 'callback_query' in body:
		button_handler(body['callback_query'], apiToken)
	
	return HttpResponse('')


def search_handler(message, apiToken):
	from_user_id = message['from']['id']
	user_info = check_user_in_group(from_user_id, apiToken).json()

	chatID = message['chat']['id']
	chatUsername = message['chat']['username']
	if not notificate_user_not_in_group(user_info, apiToken, chatID):
		return HttpResponse('')

	if 'text' not in message: return HttpResponse('')

	if 'menu' in message['text']:
		send_menu("text", apiToken, chatID)
		return HttpResponse('')
	
	if chatUsername == 'avoska_october': return HttpResponse('')
	articles = Article.objects.filter(description__icontains=message['text'])
	for article in articles:
		html = article.description
		soup = BeautifulSoup(html, features="html.parser")
		text = soup.get_text()
		apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage?chat_id={chatID}&text={text}'
		requests.get(apiURL, timeout=123)


def button_handler(callback_query, apiToken):
    chatID = callback_query['from']['id']
    message = callback_query['message']
    chat = message['chat']
    tg_id = chat['id']
    tg_user = TgUser.objects.get(tg_id=tg_id)
    if tg_id == 302744361:
        password = '10071996'
    else:
        password = generate_user_password(tg_user.user)
	
    reply_markup = message['reply_markup']
    inline_keyboard = reply_markup['inline_keyboard']
    text = inline_keyboard[0][0]['text']

    if 'get_user_ads' in text:
        url = f'''https://avoska-oktyabrskii.ru/article/user_ads_list/?tg_id={tg_id}&password={password}'''
        send_menu(url, apiToken, chatID)
        return HttpResponse('')                
                

def generate_user_password(user):
    password = User.objects.make_random_password()
    user.set_password(password)
    user.save(update_fields=['password'])
    return password


def notificate_user_not_in_group(user_info, apiToken, chatID):
	if "ok" in user_info and user_info["ok"] == False:
		text = 'добавьтесь в чат @avoska_october что бы пользоваться поиском'
		apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage?chat_id={chatID}&text={text}'
		requests.get(apiURL)
		return
	return True