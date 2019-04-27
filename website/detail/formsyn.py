from django import forms

from .models import Detail

class PostForm(forms.ModelForm):
	class Meta:
		model = Detail
		fields = [
			"username",
			"firstname",
			"lastname",
			"dob",
			"contact",
			"gender",
			"address",
			"highschool",
			"intermediate",
			"schoolname",
			"schoolplace",
			"occupation"
		]