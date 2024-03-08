from django.test import TestCase
from products.models import Product
from products.htmx_views import _pipe_price_validation

class CheckProductViewTest(TestCase):
    def setUp(self):
        Product.objects.create(name='Produto Teste', price=10.0)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/check_product/?product=Produto Teste')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/check_product/?product=Produto Teste')
        self.assertTemplateUsed(response, 'partials/htmlx_components/check_product.html')

    def test_product_is_in_context(self):
        response = self.client.get('/check_product/?product=Produto Teste')
        self.assertIn('products', response.context)
        product_names = [str(product) for product in response.context['products']]
        self.assertIn('Produto Teste', product_names)

class SaveProductViewTest(TestCase):
    def test_save_product_creates_new_product(self):
        response = self.client.post('/save_product/', {'product': 'Novo Produto', 'price': '20.0'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Product.objects.filter(name='Novo Produto').exists())

    def test_save_product_does_not_create_duplicate(self):
        Product.objects.create(name='Produto Existente', price=10.0)
        response = self.client.post('/save_product/', {'product': 'Produto Existente', 'price': '20.0'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Product.objects.filter(name='Produto Existente').count(), 1)

class DeleteProductViewTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Produto para Deletar', price=10.0)

    def test_delete_product_deletes_product(self):
        response = self.client.delete(f'/delete_product/{self.product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

class PipePriceValidationTest(TestCase):
    def test_valid_price_str(self):
        result = _pipe_price_validation('15.50')
        self.assertEqual(result, 15.50)

    def test_invalid_price_str(self):
        result = _pipe_price_validation('invalid_price')
        self.assertEqual(result, 10.0)

    def test_negative_price_str(self):
        result = _pipe_price_validation('-15.50')
        self.assertEqual(result, 10.0)
    
    def test_negative_price_str_msg(self):
        try:
            _pipe_price_validation('-15.50')
        except ValueError as e:
            self.assertEqual(str(e), "Número negativo não permitido")