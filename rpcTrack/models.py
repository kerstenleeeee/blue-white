from django.db import models

# Create your models here.
class remotePC(models.Model):
	displayName = models.CharField(null=False, blank=False, max_length = 100)
	serverName = models.GenericIPAddressField(primary_key = True)
	username = models.CharField(null = False, blank = False, max_length = 50)
	password = models. CharField(null = False, blank = False, max_length = 50)
	domain = models.CharField(null = False, blank = False, max_length = 50)
	bts = models.CharField(null=False, blank=False, max_length = 50)
	ue = models.CharField(null=False, blank=False, max_length = 50)

	def __str__(self):
		return '%s (IP: %s)' % (self.displayName, self.serverName)