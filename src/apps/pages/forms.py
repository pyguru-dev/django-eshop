from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):    
    message = forms.CharField(max_length=255, widget=forms.Textarea)    
    
    class Meta:
        model = ContactModel
        fields = "__all__"
        # widgets = {}
    
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if mobile:
            if not mobile.isnumeric():
                raise forms.ValidationError('mobile must be numeric')
            else:
                return mobile
