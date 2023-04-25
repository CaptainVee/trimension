from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']


class ChickenUpdateForm(forms.ModelForm):
	class Meta:
		model= Profile
		fields = ['image']

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)
						