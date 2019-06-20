from django.db import models

# Create your models here.
class remotePC(models.Model):
	serverName = models.GenericIPAddressField(primary_key = True)

	def __str__(self):
		return '%s' % (self.serverName)

class btsPC(models.Model):
	displayName = models.CharField(null=False, blank=False, max_length = 225)
	serverName = models.GenericIPAddressField(primary_key = True)
	username = models.CharField(null = False, blank = False, max_length = 225)
	password = models. CharField(null = False, blank = False, max_length = 225)
	domain = models.CharField(null = False, blank = False, max_length = 225)
	bts = models.CharField(null=False, blank=False, max_length = 225)
	ue = models.CharField(null=False, blank=False, max_length = 225)
	fetch = models.IntegerField(default=0)

	def __str__(self):
		return '%s' % (self.serverName)

class btsPCInfo(models.Model):
	serverName = models.OneToOneField(btsPC, related_name = 'bts_info', on_delete = models.CASCADE, primary_key = True)
	last_fetch = models.DateTimeField(auto_now=True)
	WCDMAPilot = models.CharField(max_length = 225, default = "", blank = True)
	GTAPluginGiant = models.CharField(max_length = 225, default= "", blank = True)
	DSPExplorer = models.CharField(max_length = 225, default= "", blank = True)

	def __str__(self):
		return '%s' % (self.serverName)

class tm500PC(models.Model):
	displayName = models.CharField(null=False, blank=False, max_length = 225)
	serverName = models.GenericIPAddressField(primary_key = True)
	username = models.CharField(null = False, blank = False, max_length = 225)
	password = models. CharField(null = False, blank = False, max_length = 225)
	domain = models.CharField(null = False, blank = True, max_length = 225)
	bts = models.CharField(null=False, blank=True, max_length = 225)
	ue = models.CharField(null=False, blank=False, max_length = 225)
	tenv = models.CharField(null=False, blank=False, max_length = 225)

	def __str__(self):
		return '%s' % (self.serverName)

class tm500PCInfo(models.Model):
	serverName = models.OneToOneField(tm500PC, related_name = 'tm500_info', on_delete = models.CASCADE, primary_key = True)

	def __str__(self):
		return '%s' % (self.serverName)

class btsList(models.Model):
	bts = models.CharField(null=False, blank=False, max_length = 225)

	def __str__(self):
		return '%s' % (self.bts)

class ueList(models.Model):
	ue = models.CharField(null=False, blank=False, max_length = 225)

	def __str__(self):
		return '%s' % (self.ue)

class tm500(models.Model):
	serverName = models.GenericIPAddressField(primary_key = True)
	# tm_username = models.CharField(null=False, blank=False, max_length = 100)
	# tm_password = models.CharField(null=False, blank=False, max_length = 100)
	tm_tenv = models.CharField(max_length = 225, )

	def __str__(self):
		return '%s' % (self.serverName)