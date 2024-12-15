from django import forms
from .models import contactClass

class contactForm(forms.ModelForm):
    class Meta:
        model=contactClass
        fields=['username','email','message']
        widgets={'username':forms.TextInput(attrs={'placeholder':"نام کاربری *",'class':"form-control"}),
            'email':forms.EmailInput(attrs={'placeholder':"ایمیل *",'class':"form-control"}),
            'message':forms.Textarea(attrs={'placeholder':"متن*",'class':"form-control"})
        }