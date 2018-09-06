from django.urls import path
from . import views

urlpatterns = [
    path('purchase-list/', views.purchase_list, name='purchase_list'),
]