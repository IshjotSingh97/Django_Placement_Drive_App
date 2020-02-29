from django import forms

class UserfeedbackForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput,max_length=100)
    subject = forms.CharField(widget=forms.Textarea) 