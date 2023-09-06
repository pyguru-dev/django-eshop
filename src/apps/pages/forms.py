from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):            
    
    class Meta:
        model = ContactModel
        fields = "__all__"
        widgets = {
            'email' : forms.TextInput(attrs={'class' : 'form-control'})
        }

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if mobile:
            if not mobile.isnumeric():
                raise forms.ValidationError('mobile must be numeric')
            else:
                return mobile
