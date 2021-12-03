# It will allow us to return any object-model in a jason response
from rest_framework import serializers

from sms.models import Message,SIM
# probably you will use our sms models

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class MinimalMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['receiver_phone', 'text', 'sender_id','sender_phone','message_id']


class SimSerializer(serializers.ModelSerializer):
    class Meta:
        model = SIM
        fields = '__all__'