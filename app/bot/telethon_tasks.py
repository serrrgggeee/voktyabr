from article.models import Article
from asgiref.sync import sync_to_async
from bot.models import TgUser
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files import File
from pathlib import Path
from telethon.sync import TelegramClient


try:
	client = TelegramClient('anon', settings.API_ID, settings.API_HASH)
except RuntimeError:
	pass

def parse_chat_user_messages():
	try:
		with client:
			client.loop.run_until_complete(chat_messages())
	except Exception as e:
		# logger.error(e)
		pass

		

async def chat_messages():
	participants = []
	for participant in  await client.get_participants(settings.CHAT_AVOSKA_OCTOBER):
		participant_data = {
			'id': participant.id,
			'username': participant.username,
			'phone': participant.phone,
			'first_name': participant.first_name,
			'last_name': participant.last_name,
		}
		username = get_user_name(participant_data)
		if not username: continue
		if username in ['avosykabot']: continue
		user_data = {}
		if participant_data['first_name']:
			user_data['first_name'] = participant_data['first_name']
		if participant_data['last_name']:
			user_data['last_name'] = participant_data['last_name']
		
		user, created = await save_user(username, user_data)
		tg_user, created = await save_tg_user(user, participant.id)
		participants.append(participant_data)

	async for message in client.iter_messages(settings.CHAT_AVOSKA_OCTOBER):
		name = f'{message.id}-{settings.CHAT_AVOSKA_OCTOBER}'
		if message.sender is None: continue
		participant_data = {
			'id': message.sender.id,
			'username': message.sender.username,
			'phone': message.sender.phone,
			'first_name': message.sender.first_name,
			'last_name': message.sender.last_name,
		}
		username = get_user_name(participant_data)

		if not username: continue
		if username in ['avosykabot']: continue
		if message.text is None: continue
		if len(message.text) < 1: continue
		description = message.text
		tg_user = await get_tg_user(message.sender_id)
		if message.media:
			image_path = await client.download_media(message.media, "/tmp")
			if image_path:
				path = Path(image_path)
				with path.open(mode="rb") as f:
					image = File(f, name=path.name)
					created = await save_article(name, tg_user, description, image)
			else:
				created = await save_article(name, tg_user, description)
		else:
			created = await save_article(name, tg_user, description)
		if not created: break
		

def get_user_name(participant_data):
	full_name = None
	last_name = None
	username = None
	if 'first_name' in participant_data:
		full_name = participant_data['first_name']
	
	if 'last_name' in participant_data:
		last_name = participant_data['last_name']
	
	if 'username' in participant_data:
		username = participant_data['username']

	if full_name or last_name:
		full_name = full_name or ''
		last_name = last_name or ''
		full_name =  f'{full_name} {last_name}'	
	return username if username else full_name


@sync_to_async
def save_tg_user(user, sender_id):
	return TgUser.objects.get_or_create(
		tg_id = sender_id,
		defaults = {"user": user}
	)
@sync_to_async
def get_tg_user(sender_id):
	return TgUser.objects.get(tg_id = sender_id)

@sync_to_async
def save_user(username, user_data={}):
	return User.objects.update_or_create(
		username=username,
		defaults=user_data
	)

@sync_to_async
def update_user(username):
	return User.objects.update_or_create(
		username=username
	)

@sync_to_async
def save_article(name, user, description, image=None):
	_, created = Article.objects.get_or_create(
		name=name,
		defaults = {
			'description':description,
			'user': user,
			'image': image,
			'site_sighn': "avoska_october_user"
		}
	)
	return created