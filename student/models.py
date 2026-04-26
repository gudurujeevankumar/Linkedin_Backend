from django.db import models

# Create your models here.


class StuDetails(models.Model):
    roll = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    branch = models.CharField(max_length=30)

    def __str__(self):
        return self.name 