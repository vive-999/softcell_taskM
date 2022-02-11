from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=40,blank=False)
    description = models.CharField(max_length=240)

    def __str__(self):
        return self.name