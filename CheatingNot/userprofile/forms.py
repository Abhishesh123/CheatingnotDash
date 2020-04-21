from django import forms
from userprofile.models import Users, OTP,Anonymous

class OTPForm(forms.ModelForm):
    class Meta:
        model = OTP
        fields = '__all__'
        
class AnonymousForm(forms.ModelForm):
    class Meta:
        model = Anonymous
        fields = '__all__'
        


class UserForm(forms.ModelForm):
    def clean_name(self):
        return self.cleaned_data['name'].title()
        
    def clean_gender(self):
        return self.cleaned_data['gender'].title()
    
    def clean_dob(self):
        dob = self.cleaned_data['dob']
        return dob
        
        
    class Meta:
        model = Users
        fields =  ['name', 'dob', 'gender','user_type','latitude','longitude','referral_code',
                   'email','phone_no','app_version','device_id','device_type','fcm_token','country_code',
                   'body_type','about_me', 'height','weight','priority', 'profile_verified', 'active', 
                   ]


