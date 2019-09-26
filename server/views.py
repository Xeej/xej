from django.shortcuts import render
from server.models import *
from django.shortcuts import get_object_or_404
import random
import string
from django.http import JsonResponse
from datetime import datetime
import math

def randomword(length):
   letters = string.ascii_letters
   return ''.join(random.choice(letters) for i in range(length))

def login(request):
    if request.method=='GET':
        log = request.GET.get('login')
        passw=request.GET.get('password')
        if packet.objects.filter(login=log,password=passw).exists():
         token=randomword(200)

         while packet.objects.filter(token=token).exists():
             token=randomword(200)
         a = packet.objects.get(login=log,password=passw)
         a.token=token
         a.Way = 0
         a.save()
         b = gps.objects.filter(packet=a)
         b.latitude =0
         b.longitude =0
         b.time =0
         b.alt =0
         b.save()
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
            a.Way = 0
            a.save()
            b=gps()
            b.packet = a
            b.latitude = 0
            b.longitude =0
            b.time = 0
            b.alt = 0
            b.save()
            return JsonResponse({'token':'REGISTER_SUCCESS'})
    else:
     return JsonResponse({'token':'ERROR_METHOOD'})
def GPS(request):
    if request.method == 'GET':
        token =request.GET.get('token')
        if packet.objects.filter(token=token).exists():
           a=packet.objects.filter(token=token)
           b= gps.objects.filter(packet=a)
           if b.alt !=0:

               long = request.GET.get('longitude')
               lat = request.GET.get('latitude')
               alt=request.GET.get('alt')

               x1 = alt * math.cos(lat) * math.sin(long)
               y1 = alt * math.sin(lat)
               z1 = alt * math.cos(lat) * math.cos(long)

               x2 = alt * math.cos(request.GET.get('latitude')) * math.sin(request.GET.get('longitude'))
               y2 = alt * math.sin(request.GET.get('latitude'))
               z2 = alt * math.cos(request.GET.get('latitude')) * math.cos(request.GET.get('longitude'))

               dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

               a.Way+=dist

               b.time = request.GET.get('time')
               b.save()
               a.save()
               return JsonResponse({'way': a.Way})
           else:
               b.longitude = request.GET.get('longitude')
               b.latitude = request.GET.get('latitude')
               b.time = request.GET.get('time')
               b.save()
               return JsonResponse({'way':'0'})
        else:
            return JsonResponse({'token':'BAD_AUTH'})
    else:
     return JsonResponse({'token':'ERROR_METHOOD'})


# Create your views here.
