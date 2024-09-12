import json

from rest_framework import status

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from product.factories import ProductFactory, CategoryFactory
from order.factories import UserFactory
from product.models import Product


class TestProductviwSet(APITestCase):
    client = APIClient()


    def setUp(self):
        self.user = UserFactory()

        self.product = ProductFactory(title='pro controller', price=200.00)

    def test_get_all_products(self):
        response = self.client.get(reverse('product-list', kwargs={'version': 'v1'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)

        self.assertEqual(product_data[0]['title'], self.product.title)
        self.assertEqual(product_data[0]['price'], self.product.price)

    def test_create_product(self):
        category = CategoryFactory()
        data = {
            'title': 'notebook',
            'price': 800.00,
            'category_id': [category.id]  # Enviar como uma lista
        }

        response = self.client.post(reverse('product-list', kwargs={'version': 'v1'}), data=data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        created_product = Product.objects.get(title='notebook')
        self.assertEqual(created_product.price, 800.00)
        self.assertEqual(created_product.title, 'notebook')
        self.assertIn(category, created_product.category.all())  # Verificar se a categoria foi adicionada


            
        
