from django.contrib import admin
from .models import Detail
from .models import contactus
from .models import stories
from .models import comment

class formadmin(admin.ModelAdmin):
	list_display = ["username","firstname","lastname","dob","contact","gender","address","highschool","intermediate","schoolname","schoolplace","occupation","updated","timestamp"]
	list_display_links = ["username"]
	list_filter = ["updated","timestamp"]
	search_fields = ["username","schoolname","schoolplace"]

	class Meta:
		model = Detail


class contactadmin(admin.ModelAdmin):
	list_display = ["username","message","timestamp","updated"]
	list_display_links = ["username"]
	list_filter = ["updated","timestamp"]
	search_fields = ["username"]

	class Meta:
		model = contactus

class storyadmin(admin.ModelAdmin):
	list_display = ["id","username","story","timestamp","updated"]
	list_display_links = ["username"]
	list_filter = ["updated","timestamp"]
	search_fields = ["username"]

	class Meta:
		model = stories

class commentadmin(admin.ModelAdmin):
	list_display = ["id","username","comment","timestamp","updated"]
	list_display_links = ["username"]
	list_filter = ["updated","timestamp"]
	search_fields = ["username"]

	class Meta:
		model = comment

admin.site.register(Detail,formadmin)
admin.site.register(contactus,contactadmin)
admin.site.register(stories,storyadmin)
admin.site.register(comment,commentadmin)