from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDeleteView


urlpatterns = [
    path('products', ProductListView.as_view(), name="product-list"),
    path('products/create', ProductCreateView.as_view(), name="product-create"),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name="product-delete"),

]