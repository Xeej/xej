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
         b = gps.objects.get(packet=a)
         b.latitude =0
         b.longitude =255
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
            b.longitude =255
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
           a=packet.objects.get(token=token)
           b= gps.objects.get(packet=a)
           if b.longitude !=255:

               long = float(request.GET.get('longitude'))
               lat = float(request.GET.get('latitude'))
               alt=float(request.GET.get('alt'))

               llat1 = float(request.GET.get('latitude'))
               llong1 = float(request.GET.get('longitude'))

               llat2 = b.latitude
               llong2 = b.longitude

               # pi - число pi, rad - радиус сферы (Земли)
               rad = 6372795

               # координаты двух точек
               # в радианах
               lat1 = llat1 * math.pi / 180.
               lat2 = llat2 * math.pi / 180.
               long1 = llong1 * math.pi / 180.
               long2 = llong2 * math.pi / 180.

               # косинусы и синусы широт и разницы долгот
               cl1 = math.cos(lat1)
               cl2 = math.cos(lat2)
               sl1 = math.sin(lat1)
               sl2 = math.sin(lat2)
               delta = long2 - long1
               cdelta = math.cos(delta)
               sdelta = math.sin(delta)

               # вычисления длины большого круга
               y = math.sqrt(math.pow(cl2 * sdelta, 2) + math.pow(cl1 * sl2 - sl1 * cl2 * cdelta, 2))
               x = sl1 * sl2 + cl1 * cl2 * cdelta
               ad = math.atan2(y, x)
               dist = ad * rad

               d=a.Way
               a.Way=d+dist

               b.longitude=long
               b.latitude=lat
               b.alt=alt
               b.time = request.GET.get('time')
               b.save()
               a.save()
               return JsonResponse({'way': a.Way})
           else:
               b.longitude = request.GET.get('longitude')
               b.latitude = request.GET.get('latitude')
               b.time = request.GET.get('time')
               b.alt=request.GET.get('alt')
               b.save()
               return JsonResponse({'way':'zero'})
        else:
            return JsonResponse({'token':'BAD_AUTH'})
    else:
     return JsonResponse({'token':'ERROR_METHOOD'})


# Create your views here.
