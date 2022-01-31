from .models import Product
from django import forms

class InsertFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'