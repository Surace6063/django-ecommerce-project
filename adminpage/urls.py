from django.urls import path
from . import views

urlpatterns = [
    path('category/add/',views.add_category, name="add_category"),
    path('product/add/',views.add_product, name="add_product"),
    path('product/lists/',views.products, name="dashboard_product_lists"),
]