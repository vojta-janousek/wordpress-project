from django import forms
from ptvc_app.models import Contact


class AddQuestionForm(forms.ModelForm):
    '''
    '''
    class Meta():
        model = Contact
        fields = ('name', 'subject', 'email', 'question')
