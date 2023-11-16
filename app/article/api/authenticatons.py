from rest_framework import exceptions
from rest_framework import authentication
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext as _
from bot.models import TgUser


class RequestTgGetAuthentication(authentication.BaseAuthentication):
	def authenticate(self, request):
		# Get the username and password
		tg_id = request.GET.get('tg_id', None)
		password = request.GET.get('password', None)

		if not tg_id or not password:
			raise exceptions.AuthenticationFailed(_('No credentials provided.'))
		
		username = TgUser.objects.get(tg_id=tg_id)

		credentials = {
			get_user_model().USERNAME_FIELD: username,
			'password': password
		}
		user = authenticate(**credentials)

		if user is None:
			raise exceptions.AuthenticationFailed(_('Invalid username/password.'))

		if not user.is_active:
			raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

		return (user, None)  # authentication successful
