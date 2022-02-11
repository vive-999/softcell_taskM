from django.db import models
from accounts.models import Profile
from group.models import Group
from project.models import Project

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_to = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='+')
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

