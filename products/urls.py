from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDeleteView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('products', ProductListView.as_view(), name="product-list"),
    path('products/create', ProductCreateView.as_view(), name="product-create"),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name="product-delete"),

    #Autenticação
    #Utilizando as views genéricas do simplejwt que autenticam com username e password
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]