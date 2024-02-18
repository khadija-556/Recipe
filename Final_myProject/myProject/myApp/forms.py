from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class customUserForm(UserCreationForm):
    username=forms.CharField(widget= forms.TextInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your name'
        }
    ))
 
    password1=forms.CharField(widget= forms.PasswordInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your password'
        }
    ))
    password2=forms.CharField(widget= forms.PasswordInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your confirm passsword'
        }
    ))
    email=forms.EmailField(widget= forms.EmailInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your email'
        }
    ))

    
  
    class Meta:
        model=Custom_User
        fields=UserCreationForm.Meta.fields + ('user_type','city','email')

class CustomerAutenticationForm(AuthenticationForm):
    username=forms.CharField(widget= forms.TextInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your name'
        }
    ))
 
    password=forms.CharField(widget= forms.PasswordInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your password'
        }
    ))
    class Meta:
        model=Custom_User
        fields=['username','passwoard']

class Recipi_catagoriesForm(forms.ModelForm):

    class Meta:
        model=Recipi_catagoriesModel
        fields=('__all__')

class RecipiForm(forms.ModelForm):

    class Meta:
        model=RecipiModel
        fields=('__all__')



