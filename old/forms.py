from django.forms import ModelForm
from django import forms
from .models import Product

class ProductImageForm(forms.ModelForm): 
    CHOICES = (('Academics', 'Academics'),('Novel', 'Novel'),('Self help', 'Self help'))
    category = forms.ChoiceField(choices=CHOICES)
    class Meta: 
        model = Product
        fields = ['product_name','author','price','category','image'] 
        
        widgets ={
            'product_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Book name','required':True}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Author name','required':True}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Price','required':True}),
            'image':forms.FileInput(attrs={'onchange':'previewFile()','required':True})
            }

        

        