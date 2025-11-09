from django import forms
from .models import Endpoints, TrafficLog


class registerendpoint(forms.ModelForm):
    class Meta:
        model = Endpoints
        fields = ['ip_address', 'mac_address', 'hostname']

class uploadpcap(forms.Form):
    file = forms.FileField()

