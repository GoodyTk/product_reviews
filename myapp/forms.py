from django import forms
from .models import Review

class BaseForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["product", 'author', 'text', "rating"]