from django import forms

from .models import contactus

class ContactForm(forms.ModelForm):
	class Meta:
		model = contactus
		fields = [
			"username",
			"message",
		]