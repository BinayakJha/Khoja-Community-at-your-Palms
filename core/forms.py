from django import forms
from .models import *


class EcaForm(forms.ModelForm):
    class Meta:
        model = Eca
        fields = ['name', 'email', 'phone', 'theme', 'message', 'questions','main_image', 'online_or_offline', 'happening_date','facebook', 'twitter', 'instagram', 'youtube', 'discord', 'website','user_id']

class EcaApplyForm(forms.ModelForm):
    class Meta:
        model = EcaApply
        fields = ['name', 'email', 'phone', 'eca', 'questions_answer']
        widgets = {
            'eca': forms.HiddenInput(),
        }