from django.contrib import admin

# Register your models here.

from sms.models import SIM,Message,Modem
# Register your models here.
admin.site.register(SIM) 
admin.site.register(Modem)
admin.site.register(Message)