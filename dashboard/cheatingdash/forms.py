from django import forms
from django.contrib.auth.models import User
from cheatingdash.models import Employee



class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    
    recipients = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


  
class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class empForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        