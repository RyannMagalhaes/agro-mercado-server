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

        #Cria Produtos para testar
        self.produto1 = Product.objects.create(name='Milho', price=10.00)
        self.produto2 = Product.objects.create(name='Soja', price=20.00)
        self.produto3 = Product.objects.create(name='Arroz', price=5)
        self.produto4 = Product.objects.create(name='Sorgo', price=6.29)
        self.produto5 = Product.objects.create(name='Feijão', price=1.00)
        self.produto6 = Product.objects.create(name='Morango', price=0.91)
        self.produto7 = Product.objects.create(name='Uva', price=0.01)

        self.list_url = reverse('product-list')
        self.create_url = reverse('product-create')
        self.delete_url = reverse('product-delete', kwargs={'pk': self.produto1.pk})

    def test_listagem_produtos(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = ProductSerializer([self.produto1, self.produto2, self.produto3, self.produto4, self.produto5, self.produto6, self.produto7], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_criar_produto(self):
        data = {
            'name': 'Mirtilo',
            'price': 15.00
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 8)
        new_product = Product.objects.get(name='Mirtilo')
        self.assertEqual(new_product.price, 15.00)

    def test_invalido_criar_produto_preco_negativo(self):
        data = {
            'name': 'Chuchu',
            'price': -15.00
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 7)

    def test_invalido_criar_produto_nome_2_caracteres(self):
        data = {
            'name': 'ch',
            'price': 15.00
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 7)

    def test_invalido_criar_produto_mais_de_2_decimais(self):
        data = {
            'name': 'chuchu',
            'price': 15.9999
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 7)

    def test_invalido_criar_produto_nome_mais_de_20_caracteres(self):
        data = {
            'name': 'chuuuuuuchuuuuuuuuuuuuuuuuuuuuuuuuuuuuu',
            'price': 15.00
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Product.objects.count(), 7)

    def test_product_delete(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 6)
        self.assertFalse(Product.objects.filter(pk=self.produto1.pk).exists())