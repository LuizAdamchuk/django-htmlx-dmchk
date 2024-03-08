from django.test import TestCase
from products.models import Product

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Test Product', price=19.99)

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_product_str(self):
        product = Product.objects.get(id=1)
        self.assertEqual(str(product), 'Test Product')

    def test_product_price_is_positive(self):
        product = Product.objects.get(id=1)
        self.assertTrue(product.price > 0)
