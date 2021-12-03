from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='overview'),


    # message paths
    path('message-list/', views.MessageList, name='message-list' ),
    path('message-list/<str:pk>/', views.messageMinimalDetail, name='message-detail'),
    path('message-list-minimal/<str:pk>/', views.messageMinimalDetail, name='message-detail-minimal'),
    path('message-create/', views.MessageCreate, name='message-create'),
    # path('message-update/<str:pk>/', views.MessageUpdate, name='message-update'),
    path('message-delete/<str:pk>/', views.MessageDelete, name='message-delete'),
    path('get-token/', views.CustomAuthToken.as_view())
]
