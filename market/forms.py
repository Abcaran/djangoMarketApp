from django import forms

from .models import Product,Purchase

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name',)

class PurchaseForm(forms.ModelForm):

	class Meta:
		model = Purchase
		fields = ('product','amount','total_price')



