from __future__ import unicode_literals
from django.db import models


class Detail(models.Model):
	username = models.CharField(max_length = 20)
	firstname = models.CharField(max_length = 20)
	lastname = models.CharField(max_length = 20)
	dob = models.CharField(max_length = 20)
	gender = models.CharField(max_length = 10)
	contact = models.CharField(max_length = 10)
	address = models.CharField(max_length = 30)
	highschool = models.CharField(max_length = 5)
	intermediate = models.CharField(max_length = 5)
	schoolname = models.CharField(max_length = 30)
	schoolplace = models.CharField(max_length = 20)
	occupation =  models.CharField(max_length = 20)
	updated = models.DateTimeField(auto_now  = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now  = False, auto_now_add = True)

	def __unicode__(self):
		return self.firstname

	def __str__(self):
		return self.firstname



class contactus(models.Model):
	username = models.CharField(max_length = 20)
	message = models.TextField(max_length = 1000)
	updated = models.DateTimeField(auto_now  = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now  = False, auto_now_add = True)

	def __unicode__(self):
		return self.username

	def __str__(self):
		return self.username

class stories(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length = 20)
	story = models.TextField(max_length = 1000)
	updated = models.DateTimeField(auto_now  = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now  = False, auto_now_add = True)

	def __unicode__(self):
		return self.username

	def __str__(self):
		return self.username

class comment(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length = 20)
	comment = models.TextField(max_length = 1000)
	updated = models.DateTimeField(auto_now  = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now  = False, auto_now_add = True)

	def __unicode__(self):
		return self.username

	def __str__(self):
		return self.username