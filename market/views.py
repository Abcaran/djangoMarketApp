from django.shortcuts import render
from .models import Purchase
from .forms import ProductForm,PurchaseForm


# Create your views here.
def purchase_list(request):

	all_purchases = Purchase.objects.all()

	return render(request, 'purchase_list.html', {'all_purchases': all_purchases})

def product_new(request):
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			product = form.save()
	else:
		form = ProductForm()

	return render(request, 'product_new.html', {'form': form})


def purchase_new(request):
	if request.method == "POST":
		form = PurchaseForm(request.POST)
		if form.is_valid():
			purchase = form.save(commit=False)
			purchase.avrg_price = float(form.cleaned_data['total_price'])/float(form.cleaned_data['amount'])
			purchase.save()
	else:
		form = PurchaseForm()

	return render(request, 'purchase_new.html', {'form':form})