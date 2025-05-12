from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import CreateAPIView, DestroyAPIView
from django.core.cache import cache


class ProductListView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer] 
    def get(self, request):
        productsList = cache.get('productsCache')
        if not productsList:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            productsList = serializer.data
            cache.set('productsCache', productsList, timeout=600)
        return Response(productsList)
    
class ProductCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    serializer_class = ProductSerializer  
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save()
            cache.delete('productsCache') 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
class ProductDeleteView(DestroyAPIView): 
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        cache.delete('productsCache')
        return Response(status=status.HTTP_200_OK)
    
    def perform_destroy(self, instance):
        instance.delete()