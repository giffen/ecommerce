from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.ForeignKey(User)
	stripe_id = models.CharField(max_length=300)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return str(self.user)

class Address(models.Model):
	user = models.ForeignKey(User)
	nickname = models.CharField(max_length=120, null=True, blank=True)
	address1 = models.CharField(max_length=300)
	address2 = models.CharField(max_length=300, null=True, blank=True)
	city = models.CharField(max_length=300)
	state = models.CharField(max_length=300)
	country = models.CharField(max_length=300)
	postal_code = models.CharField(max_length=300)
	default_address = models.BooleanField(default=False)
	billing_address = models.BooleanField(default=False)
	shipping_address = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.address1
