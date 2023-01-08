from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Teams(models.Model):
    tname = models.CharField(max_length=250)
    timg = models.ImageField(upload_to='photos')
    tdesc = models.TextField()

    def __str__(self):
        return self.tname
