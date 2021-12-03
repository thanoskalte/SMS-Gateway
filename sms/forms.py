from django import forms
from django.forms import ModelForm, models
from django.forms import widgets
from django.forms.widgets import TextInput, Widget
from django import forms
from .models import SIM, Message, Modem


class ModemForm(ModelForm):
    class Meta:
        model = Modem
        fields = '__all__'
        # gives you all those fields

class MessageForm(ModelForm):
    

    class Meta:
        model = Message
        fields = ['sender_phone','receiver_phone','text']
        labels = {
            "sender_phone":"Select SIM",
            "receiver_phone":"To:",
            "text":"Message"
        }
        
    

class SIMForm(ModelForm):
    class Meta:
        model = SIM
        fields = '__all__'
        # gives you all those fields
