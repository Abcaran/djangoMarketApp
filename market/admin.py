from django.contrib import admin
from .models import Product, Purchase
from .forms import PurchaseForm

admin.site.register(Product)

class PurchaseAdmin(admin.ModelAdmin):
	form = PurchaseForm
	list_display = ['product', 'amount', 'total_price']

	def save_model(self, request, obj, form, change):
		obj.avrg_price = obj.total_price/obj.amount
		super().save_model(request, obj, form, change)

admin.site.register(Purchase, PurchaseAdmin)