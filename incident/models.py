from django.db import models
from accounts.models import Profile
from group.models import Group
from django import forms

class Incident(models.Model):
    date = models.DateField()
    Incident_number = models.IntegerField(blank=False)
    issue_subject = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.BooleanField()
    assigned_to = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    service_group = models.ForeignKey(Group,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.issue_subject
