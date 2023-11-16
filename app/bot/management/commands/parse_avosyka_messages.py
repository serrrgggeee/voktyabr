from bot.telethon_tasks import parse_chat_user_messages
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Спарсить сообщения пользователей группы"

    def add_arguments(self, parser):
        parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        parse_chat_user_messages()

