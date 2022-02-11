from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from group.models import Group
from project.models import Project

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=120,null=True)
    group_member = models.ForeignKey(Group,on_delete=models.CASCADE,null=True)
    project_member = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return str(self.user.username)

    # def post_save_user_model_receiver(sender,instance,created,*args,**kwargs):
    #     if created:
    #         try:
    #             Profile.objects.create(user=instance)
    #         except:
    #             pass
    # post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)

    # user= models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    # firstname = models.CharField(max_length=125,null=False,blank=False)
    # lastname = models.CharField(max_length=125,null=False,blank=False)
    # group_id= models.ForeignKey(Group,on_delete=models.CASCADE)
    # project_id= models.ForeignKey(Project,on_delete=models.CASCADE)
    

    # def __str__(self):
    #     return self.firstname