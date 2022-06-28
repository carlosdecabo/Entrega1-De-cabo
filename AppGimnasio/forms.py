from django import forms
from django.forms import ModelForm, fields_for_model
from .models import registro

class registroFormulario(ModelForm):
    class Meta:
        model = registro
        fields = ['nombre','apellido','edad','email','dni']
