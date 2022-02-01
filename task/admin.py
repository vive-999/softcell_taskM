from django.contrib import admin
from .models import User,Group,Task,Project,Incident

# Register your models here.
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Incident)