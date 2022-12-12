from django import forms
from django.contrib.auth.forms import AuthenticationForm
from materias.models import DirectorioModel



class Directorio(forms.ModelForm):
    class Meta:
        model = DirectorioModel
        
        fields = '__all__'
        
        widgets = {
            #carpeta': forms.Input(attrs={'class': 'form-control'})
            'carpeta': forms.FileInput(attrs={'class': 'form-control'})
        }