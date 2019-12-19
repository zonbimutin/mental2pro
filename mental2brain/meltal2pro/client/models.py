from django.db import models


class Coach(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    description = models.TextField()
    ville = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    longitud = models.FloatField()
    latitud = models.FloatField()
    zipe_code = models.IntegerField()



    
