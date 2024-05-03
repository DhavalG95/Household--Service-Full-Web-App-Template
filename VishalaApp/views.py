from django.shortcuts import render , redirect
import random , string 
from .models import *
from django.contrib import messages
from django.views.decorators.cache import never_cache
from instamojo_wrapper import Instamojo
from django.conf import settings

api = Instamojo(api_key=settings.API_KEY,
                auth_token=settings.AUTH_TOKEN , endpoint="https://test.instamojo.com/api/1.1/")

# Create your views here.
@never_cache
def home(request):
    if request.session.has_key('session_key'):
        data = Service.objects.all().values()
        
        return render(request,'dashboard.html',context={"dat":data})
    else:
        return redirect("login")
    
def login(request):
    char_set=string.ascii_uppercase + string.digits
    session_key=''.join(random.sample(char_set * 20, 20))
    
    if request.method=="POST":
        uname = request.POST.get('username')
        pswrd = request.POST.get('password')
        
        obj = Login.objects.get(mobile=uname)
        if obj.password==pswrd:
            
            request.session['user_name']=obj.name
            request.session['user_id']=obj.id
            request.session['session_key']=session_key
            
            obj.save()
            
            response = {"status":True,"message":"student logged in  successfully"}
            
            return redirect('home')
        else:
            messages.error(request,"wrong password")
            response = {"status":False,"message":"student entered wrong password"}
            
            return redirect('login')

    return render(request,'login.html')


def logout(request):
    if request.session.has_key('session_key'):
        del request.session['session_key']
               
        return redirect('login')
    else:
        
        return redirect('login')
    
def service(request):
    return render(request,'services.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mob')
        message = request.POST.get('msg')

        con = Contact.objects.create(name=name,mobile=mobile,message=message)
        con.save()
        return redirect ('home')
    return render(request,'contact.html')

def payment(request,pk):
    data = Service.objects.get(id=pk)
    response = api.payment_request_create(
        amount=data.fees,
        purpose='Avail Service',
        send_email=False,
        send_sms=False,
        buyer_name = request.session.get("user_name"),
        email="dhavalgothi786@gmail.com",
        redirect_url="http://127.0.0.1:8000/success"
    )
    print(response)
    paymenturl = response['payment_request']['longurl']
    return render(request,'payment.html',context={"payment_url":paymenturl,"amount":data.fees})

def success(request):
    return render(request,'success.html')