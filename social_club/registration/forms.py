from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ClubUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'} ))
    last_name  = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    email      = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email', 'password1', 'password2' )
        
        labels = {'first_name': ' ',
                  'last_name':' ',
                  'email':' ',
                  }
        
        #  widgets = {
        #     'username' : forms.TextInput(attrs={'class':'form-control'}),
        #     'first_name' : forms.TextInput(attrs={'class':'form-control'}),
        #     'last_name' : forms.TextInput(attrs={'class':'form-control'}),
        #     'email' : forms.EmailField(attrs={'class':'form-control'}),
        #     'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
        #     'password2' : forms.PasswordInput(attrs={'class':'form-control'}),
        # }  

    def __init__(self, *args, **kwargs):
        super(ClubUserForm,self). __init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['username'].widget.attrs['label']=' aaa '

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password'

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Confirm Password'