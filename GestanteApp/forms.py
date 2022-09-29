from django.forms import * 
from .models import Gestante,Provincia, Distrito

class GestanteForm(Form):
    provincia = ModelChoiceField(queryset=Provincia.objects.all(), widget=Select(attrs={
        'class': 'form-control' 
        }))
    
    distrito = ModelChoiceField(queryset=Distrito.objects.none(), widget=Select(attrs={
        'class': 'form-control' 
        }))
    
