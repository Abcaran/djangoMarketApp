from django.urls import path
from . import views

urlpatterns = [
    path('purchase-list/', views.purchase_list, name='purchase_list'),
    path('product/new', views.product_new, name='product_new'),
    path('purchase/new', views.purchase_new, name='purchase_new'),
]