from django.shortcuts import render
from .models import Purchase

# Create your views here.
def purchase_list(request):

	all_purchases = Purchase.objects.all()

	return render(request, 'purchase_list.html', {'all_purchases': all_purchases})