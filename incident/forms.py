from django import forms
from .models import Incident


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = [
            'date',
            'Incident_number',
            'issue_subject',
            'description',
            'status',
            'assigned_to',
            'service_group',
        ]

