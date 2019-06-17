from django.db import models

# Create your models here.
class remotePC(models.Model):
	serverName = models.GenericIPAddressField(primary_key = True)

	def __str__(self):
		return '%s' % (self.serverName)

class btsPC(models.Model):
	displayName = models.CharField(null=False, blank=False, max_length = 100)
	serverName = models.GenericIPAddressField(primary_key = True)
	username = models.CharField(null = False, blank = False, max_length = 50)
	password = models. CharField(null = False, blank = False, max_length = 50)
	domain = models.CharField(null = False, blank = False, max_length = 50)
	bts = models.CharField(null=False, blank=False, max_length = 50)
	ue = models.CharField(null=False, blank=False, max_length = 50)

	def __str__(self):
		return '%s' % (self.serverName)

class tm500PC(models.Model):
	displayName = models.CharField(null=False, blank=False, max_length = 100)
	serverName = models.GenericIPAddressField(primary_key = True)
	username = models.CharField(null = False, blank = False, max_length = 50)
	password = models. CharField(null = False, blank = False, max_length = 50)
	domain = models.CharField(null = False, blank = True, max_length = 50)
	bts = models.CharField(null=False, blank=True, max_length = 50)
	ue = models.CharField(null=False, blank=False, max_length = 50)
	tenv = models.CharField(null=False, blank=False, max_length = 50)

	def __str__(self):
		return '%s' % (self.serverName)

class btsList(models.Model):
	bts = models.CharField(null=False, blank=False, max_length = 50)

	def __str__(self):
		return '%s' % (self.bts)

class ueList(models.Model):
	ue = models.CharField(null=False, blank=False, max_length = 50)

	def __str__(self):
		return '%s' % (self.ue)

class tm500(models.Model):
	serverName = models.GenericIPAddressField(primary_key = True)
	# tm_username = models.CharField(null=False, blank=False, max_length = 100)
	# tm_password = models.CharField(null=False, blank=False, max_length = 100)
	tm_tenv = models.CharField(max_length = 100,)

	def __str__(self):
		return '%s' % (self.serverName)