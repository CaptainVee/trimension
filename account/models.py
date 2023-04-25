from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class User(AbstractUser):
    pass


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, null=True)

	def __str__(self):
		return f'{ self.user.username } Profile'