from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    picture = models.FileField(upload_to="Pictures/")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title
