from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Modem,Message,SIM
from .forms import MessageForm
from django.shortcuts import redirect
# Create your views here.
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.contrib import messages
from django.db.models import Q, query
from .filters import MessageFilter
from datetime import date
# tokens
from rest_framework.authtoken.models import Token








# list all modems and SIMs
@login_required(login_url='login')
def sim_preferences(request):
    
    # only sims that are used by modem
    sims = SIM.objects.filter(is_used_by_modem=True)
    sims_count = sims.count()
    modems = Modem.objects.all()

    context = {
        'modems':modems,
        'sims':sims,
        'sims_count':sims_count
    }
    return render(request, 'sms/sim-preferences.html', context)






# list all texts
# @login_required(login_url='login')
# def all_messages(request):
#     user = request.user
# # messages of each user
#     messages = user.message_set.all().order_by('-date_created')

#     # SEarch Functionality 2
#     q = request.GET.get('q') if request.GET.get('q') != None else ''
#     messages = messages.filter(
#         Q(text__contains=q)
#         ) 
#     # 
#     context = {
#         'messages':messages,

#         # 'myfilter':myfilter
#     }
#     return render(request, 'sms/all_messages.html', context)


# new all messages table
@login_required(login_url='login')
def send_messages(request):
    user = request.user
# messages of each user
    messages = user.message_set.all().order_by('-date_created')

    # SEarch Functionality 2
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    messages = messages.filter(
        Q(text__contains=q)|Q(receiver_phone__contains=q) 
        ) 
    # 
    context = {
        'messages':messages,

        # 'myfilter':myfilter
    }
    return render(request, 'sms/send_messages.html', context)





# create message
@login_required(login_url='login')
def compose_message(request):
    form = MessageForm()
    # load sims
    sims = SIM.objects.filter(is_used_by_modem=True)

    if request.method=='POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # save with snder being the user
            message = form.save(commit=False)
            message.sender_id = request.user
            message.save()
            return redirect('message-success') 
# -------------------------------------------------
    
    context ={
        
        'form':form,
        'sims':sims,
    }
    return render(request, 'sms/compose_message.html', context)








    # login user

def Login_view(request):
    if request.method=='POST':
        # --------------------------------
        # get values
        username = request.POST.get('username')
        password = request.POST.get('password')
        # -------------------------------------------
        # make sure a user exists
        
        # -------------------------------------------
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login user in our database
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Please try again')
    context = {

    }
    return render(request, 'sms/login.html', context)


# logout user
@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('home')



@login_required(login_url='login')
def message_success(request):
    my_context= {}
    return render(request, 'sms/message_success.html', my_context)


@login_required(login_url='login')
def dashboard(request):
    user = request.user

    # load the overall data
    sims = SIM.objects.all()
    messages = user.message_set.all()
    sims_count = sims.count()
    messages_count = messages.count()
    messages_queud = messages.filter(status='p')
    queued_count = messages_queud.count()
    phones = messages.values('receiver_phone').distinct().count()



    # load the today data
    today_msg = messages.filter(date_created__contains=date.today())
    today_msg_count = today_msg.count()
    today_messages_queud = today_msg.filter(status='p')
    today_queued_count = today_messages_queud.count()

    # activityrate = (today_msg_count/messages_count+1)*100
    activityrate = ((1+today_msg_count)/(1 + messages_count))*100
    activityrate = round(activityrate,2)

    my_context= {
        'sims_count':sims_count,
        'messages_count':messages_count,
        'today_msg_count':today_msg_count,
        'queued_count':queued_count,
        'today_queued_count':today_queued_count,
        'phones':phones,
        'activityrate':activityrate,
     
    }
    return render(request, 'sms/dashboard.html', my_context)




@login_required(login_url='login')
def ObtainToken(request):
    token = Token.objects.get(user=request.user)
    user = request.user
    my_context= {
        'token':token,
        'user':user,
        }
    return render(request, 'sms/obtain-token.html', my_context)




# home view
@login_required(login_url='login')
def home_view(request):
    # work on token verification    
    my_context= {
        
        }
    return render(request, "index.html", my_context)
