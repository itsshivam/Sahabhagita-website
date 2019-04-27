from django import forms

from .models import stories

class StoryForm(forms.ModelForm):
	class Meta:
		model = stories
		fields = [
			"username",
			"story",
		]