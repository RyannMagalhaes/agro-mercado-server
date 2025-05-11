from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product
from .serializers import ProductSerializer
# Create your tests here.

class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.produto1 = Product.objects.create(name='Milho', price=10.00)
        self.produto2 = Product.objects.create(name='Soja', price=20.00)
        self.list_url = reverse('product-list')
        self.create_url = reverse('product-create')
        self.delete_url = reverse('product-delete', kwargs={'pk': self.product1.pk})

    def test_product_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = ProductSerializer([self.product1, self.product2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_product_create(self):
        data = {'name': 'New Product', 'price': 15.00}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 3)
        new_product = Product.objects.get(name='New Product')
        self.assertEqual(new_product.price, 15.00)

    def test_product_delete(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 1)
        self.assertFalse(Product.objects.filter(pk=self.product1.pk).exists())