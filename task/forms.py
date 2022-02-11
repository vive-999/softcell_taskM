from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [ 'title',
                   'description',
                   'start_date',
                   'end_date',
                   'assigned_to',
                   'created_by',
                   'project_id',
                   'group_id'
        ]
