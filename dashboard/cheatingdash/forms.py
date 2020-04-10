from django import forms
from cheatingdash.models import UserProfile

class userForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"
