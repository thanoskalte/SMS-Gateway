from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models import constraints
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.db.models.fields import CharField, IPAddressField
from django.forms import fields



class SIM(models.Model):
    # auto generated!
    sim_id = models.PositiveIntegerField(default=0)
    phone = models.PositiveBigIntegerField(primary_key=True,unique=True)
    pin = models.CharField(max_length=64)
    mychoices = [
        ('a','active'),
        ('n','nonactive'),
        ('l','locked'),
        ]
    status = models.CharField(choices=mychoices, max_length=1,null=True)
    is_used_by_modem = models.BooleanField(default=False)

    #timestamp when sim is created
    date_created = models.DateTimeField(auto_now=True,null=True)
    # whenever status changes timestamp, and action
    



class Modem(models.Model):
    imei = models.PositiveBigIntegerField(primary_key=True)
    sim_phone = models.OneToOneField(SIM, on_delete=CASCADE, null=True, unique=True) 
                            
    

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now=True)
    date_send = models.DateTimeField(auto_now=True)
    date_received = models.DateTimeField(auto_now=True)
    sender_id = models.ForeignKey(User, on_delete=CASCADE)
    sender_phone = models.ForeignKey(SIM,null=True, on_delete=SET_NULL)
    # SAME HERE
    receiver_phone = models.PositiveBigIntegerField()
    text = models.TextField()
    unicode = models.CharField(max_length=64, default='U+000A')
    # status
    message_choices = [
        ('r','received'),
        ('p','pending'),
        ]
    status = models.CharField(choices=message_choices, max_length=1,null=True, default='p')