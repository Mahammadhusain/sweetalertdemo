from django import forms
from .models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Price'}),
            'desc':forms.Textarea(attrs={'class':'form-control','placeholder':'Write Description'}),
        }