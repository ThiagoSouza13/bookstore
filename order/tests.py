
# Create your tests here.
from django.test import TestCase
from order.factories import UserFactory, OrderFactory
from product.factories import ProductFactory
from order.models import Order

class FactoryTestCase(TestCase):
    def test_user_factory(self):
        user = UserFactory()
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.username)

    def test_order_factory(self):
        order = OrderFactory()
        self.assertIsNotNone(order.id)
        self.assertIsNotNone(order.user)

    def test_order_factory_with_products(self):
        products = ProductFactory.create_batch(3)
        order = OrderFactory(product=products)
        self.assertEqual(order.product.count(), 3)
        for product in products:
            self.assertIn(product, order.product.all())