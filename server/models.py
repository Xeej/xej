from django.db import models

# Create your models here.
class packet(models.Model):
    login = models.CharField('Логин', max_length=255)
    password = models.CharField('Пароль', max_length=255)
    firstname = models.CharField('Имя', max_length=255)
    secondname = models.CharField('Фамилия', max_length=255)
    email = models.CharField('e-mail', max_length=255)
    token = models.CharField('token', max_length=255)
    date = models.DateField('Дата')
    Way = models.FloatField('Путь')
    objects = models.Manager()
    class Meta:
        unique_together = ('login', 'password',)

        def __str__(self):
            return self.packet_text


class gps(models.Model):
    packet = models.ForeignKey(packet, on_delete= models.CASCADE)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.gps_text
