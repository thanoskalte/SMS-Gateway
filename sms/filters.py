import django_filters as filters

from .models import *


class MessageFilter(filters.FilterSet):
    # msg = CharFilter(field_name='receiver_phone', lookup_expr='icontains')

    class Meta:
        model = Message
        fields = {
            'receiver_phone':['icontains'],
        }
        
    