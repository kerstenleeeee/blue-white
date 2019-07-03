from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.UE_LIST)			# list of all ue types
admin.site.register(models.BTS_PC)			# list of all remote pcs
admin.site.register(models.tm500PC)			# list of all tm500 pcs
admin.site.register(models.BTS_INFO)	
admin.site.register(models.BTS_MODULES)	

'''class btsInfoTime(admin.ModelAdmin):
    readonly_fields = ('last_fetch',)
    
admin.site.register(models.btsPCInfo, btsInfoTime)'''