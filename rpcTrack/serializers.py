from rest_framework import serializers
from . import models

class remotePCSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.remotePC 
		fields = ('displayName', 'serverName')