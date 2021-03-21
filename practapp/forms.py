from django import forms
from .models import *
from django.core import validators


class DistrictForm(forms.ModelForm):
    class Meta:
        model = Discrict
       # fields='__all__'
        fields = ['name', 'division', 'description']

        widegts = {
            'name': forms.TextInput(attrs={'class': 'form-field'}),
            'division':forms.TextInput(attrs={'class':'form-field'}),
            'description':forms.Textarea(attrs={'class':'form-field'})
        }
def even_or_not(val):
    if val%2==0:
        raise forms.ValidationError("Please Enter Odd Number!")
class user_form(forms.ModelForm):
    user_name=forms.CharField(label="User Name", max_length=10, required=True,
    widget=forms.TextInput(attrs={'placeholder':'Enter Your Name','style':'width:300px'}),
    validators=[validators.MaxLengthValidator(10),validators.MaxLengthValidator(5)])
    
    user_dob=forms.DateField(label="Date Of Birth", widget=forms.TextInput(attrs={'type':'date'}))
    
    user_email=forms.EmailField(label="Email", max_length=50)
    # user_email2=forms.EmailField(label="Email", max_length=50)
    # def clean(self):
    #     all_clean_data=super().clean()
    #     u_email=all_clean_data['user_email']
    #     con_email=all_clean_data['user_email2']
    #     if u_email != con_email:
    #         raise forms.ValidationError("Password Not Match!")


    mobile=forms.IntegerField(validators=[validators.MaxValueValidator(11)])
    number_feild=forms.IntegerField(validators=[even_or_not])
    password=forms.PasswordInput()


    attendence=forms.BooleanField(label="Attendence", required=False)
    
    degree_choice=(('1','PSC'),('2','JSC'),('3','SSC'),('4','HSC'))
    
    degree=forms.ChoiceField(label="Educational Qualification",choices=degree_choice,widget=forms.CheckboxSelectMultiple)
    
    department=forms.ChoiceField(label="Department",choices=(('','Select Option'),('1','CSE'),('2','CE'),('3','EEE')))
    
    hobby_choice=(('0','Cricket'),('1','Football'),('2','Badminton'),('3','Kabadi'))
    
    Hobby=forms.ChoiceField(label="Hobby",choices=hobby_choice, widget=forms.RadioSelect)

# class MusicianForm(forms.ModelForm):
#     class Meta:
#         models=Musician
#         fields="__all__"
