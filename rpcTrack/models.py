from django.db import models

# Create your models here.
class tm500PC(models.Model):
	serverName = models.GenericIPAddressField(primary_key = True)
	displayName = models.CharField(null=False, blank=False, max_length = 225)
	username = models.CharField(null = False, blank = False, max_length = 225)
	password = models. CharField(null = False, blank = False, max_length = 225)
	domain = models.CharField(null = False, blank = True, max_length = 225)
	fetch = models.IntegerField(default=0)
	pc_rack = models.IntegerField(default = 1)
	tm500_rack = models.IntegerField(default = 1)
	check = models.IntegerField(default = 1)

	def __str__(self):
		return '%s' % (self.serverName)

class tm500PCInfo(models.Model):
	serverName = models.OneToOneField(tm500PC, related_name = 'tm500_info', on_delete = models.CASCADE, primary_key = True)
	last_fetch = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s' % (self.serverName)

class UE_LIST(models.Model):
	ue = models.CharField(null=False, blank=False, max_length = 225)

	def __str__(self):
		return '%s' % (self.ue)

class BTS_INFO(models.Model):
	i_d = models.AutoField(primary_key=True)
	bts_type = models.CharField(null=True, blank=True, max_length = 225)
	bts_use = models.CharField(null=True, blank=True, max_length = 225)
	bts_name = models.CharField(null=True, blank=True, max_length = 225)
	rack = models.CharField(null=True, blank=True, max_length = 225)
	switch_port = models.CharField(null=True, blank=True, max_length = 225)
	notes = models.TextField(blank = True)

	def __str__(self):
		return '%s' % (self.bts_name)

class BTS_PC(models.Model):
	ip = models.GenericIPAddressField(primary_key = True)
	display_name = models.CharField(null=False, blank=False, max_length = 225)
	username = models.CharField(null = False, blank = False, max_length = 225)
	password = models. CharField(null = False, blank = False, max_length = 225)
	domain = models.CharField(null = True, blank = True, max_length = 225)
	bts_info_id = models.ForeignKey(BTS_INFO, related_name="bts_info_id_for", on_delete=models.PROTECT, blank=True, null=True)
	ue_type = models.CharField(null=False, blank=False, max_length = 225)
	fetch = models.IntegerField(default=0)
	rack = models.CharField(null=True, blank=True, max_length = 225)
	tt_info_id = models.ForeignKey(BTS_INFO, related_name="tt_info_id_for", on_delete=models.PROTECT, blank=True, null=True)
	tm500_pc_id = models.ForeignKey(tm500PC, related_name="new_tm", on_delete=models.PROTECT, blank=True, null=True)
	switch_port = models.CharField(null=True, blank=True, max_length = 225)
	check = models.IntegerField(default = 1)
	notes = models.TextField(blank = True)
	serial_number = models.CharField(null=True, blank=True, max_length = 225)
	product_number = models.CharField(null=True, blank=True, max_length = 225)
	asset_number = models.CharField(null=True, blank=True, max_length = 225)

	def __str__(self):
		return '%s' % (self.ip)

class BTS_MODULES(models.Model):
	ASSIGN_CHOICES =[
		("0", "0"),
		("1", "1")
	]
	i_d = models.AutoField(primary_key=True)
	bts_info_id = models.ForeignKey(BTS_INFO, related_name="new_mod", on_delete=models.PROTECT, blank=True, null=True)
	module_name = models.CharField(null=True, blank=True, max_length = 225)
	module_brand = models.CharField(null=True, blank=True, max_length = 225)
	serial_number = models.CharField(null=True, blank=True, max_length = 225)
	product_number = models.CharField(null=True, blank=True, max_length = 225)
	asset_number = models.CharField(null=True, blank=True, max_length = 225)
	notes = models.TextField(blank = True)
	assign = models.CharField(null=True, blank=True, max_length = 1, default="0", choices=ASSIGN_CHOICES)

	def __str__(self):
		return '%s' % (self.module_name)