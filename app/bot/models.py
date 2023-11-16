from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class TgUser(models.Model):
    tg_id = models.CharField('Id телеграм пользователя',  max_length=15)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='tg_user', max_length=256, verbose_name='TgUser', null=True, blank=True)
    
    def __str__(self):
        return self.user and self.user.username or str(self.tg_id)