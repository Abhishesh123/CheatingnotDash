from django import forms
from userprofile.models import Users


class userForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
