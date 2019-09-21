from django.shortcuts import render
from server.models import *
from django.shortcuts import get_object_or_404
import random
import string
from django.http import JsonResponse
from datetime import datetime
def randomword(length):
   letters = string.ascii_letters
   return ''.join(random.choice(letters) for i in range(length))

def logins(request):
    if request.method=='GET':
        log = request.GET.get('login')
        passw=request.GET.get('password')
        if packet.objects.filter(login=log,password=passw).exists():
         token=randomword(200)
         while packet.objects.filter(token=token).exists():
             token=randomword(200)
         a = packet.objects.get(login=log,password=passw)
         a.token=token
         a.save()
         return JsonResponse({'token':token,'firstname':a.firstname,'secondname':a.secondname})
        else:
         return JsonResponse({'token':'LOG_ERROR'})
    else:
        return JsonResponse({'token':'ERROR_METHOOD'})


def register(request):
    if request.method == 'GET':
        log = request.GET.get('login')
        passw = request.GET.get('password')
        firstname = request.GET.get('firstname')
        secondname = request.GET.get('secondname')
        email = request.GET.get('email')
        dateTimeObj = datetime.now()
        date = dateTimeObj.strftime("%Y-%m-%d")

        if packet.objects.filter(login=log).exists():return JsonResponse({'token':'LOGIN_EXISTS'})
        else:
            a=packet()
            a.token='NONE'
            a.login=log
            a.password=passw
            a.date=date
            a.firstname=firstname
            a.secondname=secondname
            a.email=email
            a.save()
            return JsonResponse({'token':'REGISTER_SUCCESS'})
    else:
     return JsonResponse({'token':'ERROR_METHOOD'})


# Create your views here.
