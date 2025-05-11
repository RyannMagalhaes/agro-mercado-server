from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDeleteView

urlpatterns = [
    path('products', ProductListView.as_view()),
    path('products/create', ProductCreateView.as_view()),
    path('products/delete/<int:pk>', ProductDeleteView.as_view()),
]