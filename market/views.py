from django.shortcuts import render, redirect
from .models import Purchase
from .forms import ProductForm,PurchaseForm
from django.db.models import Q


# Create your views here.
def purchase_list(request):

	all_purchases = Purchase.objects.all()

	query = request.GET.get("nome_produto")
	if query:
		all_purchases = all_purchases.filter(Q(product__name__icontains=query))

	return render(request, 'purchase_list.html', {'all_purchases': all_purchases})

def product_new(request):

	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			product = form.save()
			return redirect(purchase_new)
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
			return redirect(purchase_list)
	else:
		form = PurchaseForm()
	return render(request, 'purchase_new.html', {'form':form})