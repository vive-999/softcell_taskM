import email
from turtle import title
from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    group_member = models.ForeignKey(Group, on_delete=models.CASCADE)
    project_member = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.email

class Incident(models.Model):
    date = models.DateField()
    Incident_number = models.IntegerField(blank=False)
    issue_subject = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.BooleanField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    service_group = models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return self.issue_subject

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

