from django.db import models
from django.utils.timezone import now
from django.conf import settings

# Create your models here.
class Cap(models.Model):
    titulo = models.TextField(default='', blank=False)
    fecha = models.DateField(default=now)
    temporada = models.TextField(default='', blank=False)
    genero = models.TextField(default='', blank=False)
    capitulos = models.SmallIntegerField(default=0, blank=False)
    estudio = models.TextField(default='', blank=False)
    director = models.TextField(default='', blank=False)
    animacion = models.CharField(default='',max_length=2, blank=False)
    formato = models.TextField(default='', blank=False)
    adaptacion = models.TextField(default='', blank=False)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cap = models.ForeignKey('caps.Cap', related_name='caps', on_delete=models.CASCADE)