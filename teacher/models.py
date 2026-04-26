from django.db import models

# Create your models here.
class Teacher(models.Model):
    Empid = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=30)

    def __str__(self):
        return self.name 