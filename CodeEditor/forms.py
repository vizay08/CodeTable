from django import forms
from django_ace import AceWidget

'''
    not much documentation therefore ignored i...
'''
class CodeEditorForm(forms.Form):

    text =  forms.CharField(widget=AceWidget(mode='css', theme='twilight', wordwrap=False))