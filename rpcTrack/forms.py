from django import forms
from . import models

class remotePCForm(forms.ModelForm):
	class Meta:
		model = models.remotePC 
		fields = [
			'displayName',
			'serverName',
			'username',
			'password',
			'domain',
			'bts',
			'ue'
		]

class addNewRPC(forms.Form):
	displayName = forms.CharField(max_length = 50)
	serverName = forms.GenericIPAddressField()
	username = forms.CharField(max_length = 50)
	password = forms. CharField(max_length = 50)
	domain = forms.CharField(max_length = 50)
	bts = forms.CharField(max_length = 50)
	ue = forms.CharField(max_length = 50)