from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.remotePC)
admin.site.register(models.btsList)
admin.site.register(models.ueList)
admin.site.register(models.tm500)
admin.site.register(models.btsPC)
admin.site.register(models.tm500PC)

class btsInfoTime(admin.ModelAdmin):
    readonly_fields = ('last_fetch',)
    
admin.site.register(models.btsPCInfo, btsInfoTime)