from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
# my imports
from sms.models import Message,SIM
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import MessageSerializer, MinimalMessageSerializer
from rest_framework.decorators import authentication_classes, permission_classes

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# -------------------------------------------
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response






class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
        })

# -----------------------------------------------------





# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/message-list/',
        'Detail View':'/message-list/<str:pk>/',
        'Minimal View':'message-list-minimal/<str:pk>/',
        'Create':'/message-create/',
        'Update':'/message-update/<str:pk>/',
        'Delete':'/message-delete/<str:pk>/',
    }

    return Response(api_urls)









# get all messages
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def MessageList(request):
    messages = Message.objects.filter(sender_id=request.user).all()
    serializer = MinimalMessageSerializer(messages, many=True)
    return Response(serializer.data)










# get detail view
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def messageDetail(request,pk):
    messages = Message.objects.get(message_id=pk)
    serializer = MessageSerializer(messages, many=False)
    return Response(serializer.data)












# get minimal detail view
@api_view(['GET'])
def messageMinimalDetail(request,pk):
    messages = Message.objects.get(message_id=pk)
    serializer = MinimalMessageSerializer(messages, many=False)
    return Response(serializer.data)








# create a view
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def MessageCreate(request):
    serializer = MinimalMessageSerializer(data = request.data)
    if serializer.is_valid():
        # so it doesn't ask for message id 
        serializer.save()
        success_dict = {
            'Status': 'message was created successfully'
            ,'message_id': serializer.data['message_id'],}

    return Response(success_dict)











# update a view
# @api_view(['PUT'])
# def MessageUpdate(request, pk):
#     message = Message.objects.get(message_id=pk)
#     serializer = MessageSerializer(instance=message, data = request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)











# delete a view
@api_view(['DELETE'])
def MessageDelete(request, pk):
    message = Message.objects.get(message_id=pk)
    message.delete()
    return Response("Item was deleted")


