from django.db import models

# Create your models here.

class Officer(models.Model):
    name = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    about = models.CharField(max_length=1024)
    image_url = models.CharField(max_length=512)
    order = models.SmallIntegerField()

    def __str__(self):
        return f"{self.name} ({self.position})"

class Player(models.Model):
    name = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    image_url = models.CharField(max_length=512)

    def __str__(self):
        return self.name