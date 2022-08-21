from django.db import models


class services(models.Model):
    text = models.CharField(max_length=100)
    pic = models.CharField(max_length=100)

    def __str__(self):
        return self.text+' :    '+self.pic
