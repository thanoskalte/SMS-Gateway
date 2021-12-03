"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import urls, contrib
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

# added functions for urls
from sms import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # my base paths
    path('', views.dashboard, name='home'),
    path('api/', include('api.urls')),

    # Login path
    path('login/', views.Login_view, name='login'),
    path('logout/', views.logoutuser, name='logout'),

    

    # urls about our sms app
    path('sim-preferences/', views.sim_preferences, name='simlist'),
    path('all-messages2/', views.send_messages, name='send_messages'),

    path('compose-message/', views.compose_message,  name='compose'),
    path('message-success/', views.message_success, name='message-success'),
    path('mytoken/', views.ObtainToken, name='mytoken'),


]
