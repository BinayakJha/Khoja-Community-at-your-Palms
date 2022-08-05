from django import forms
from .models import *


class EcaForm(forms.ModelForm):
    class Meta:
        model = Eca
        fields = ['name', 'email', 'phone', 'theme', 'message', 'questions', 'online_or_offline', 'happening_date']

class EcaApplyForm(forms.ModelForm):
    class Meta:
        model = EcaApply
        fields = ['name', 'email', 'phone', 'eca', 'questions_answer']
        widgets = {
            'eca': forms.HiddenInput(),
        }