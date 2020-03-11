from django import forms
from .models import *

class UserfeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ['subject','feedback']