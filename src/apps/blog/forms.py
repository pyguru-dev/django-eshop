from django import forms
from .models import Comment


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'user', 'article')
        widgets = {
            'article': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }
