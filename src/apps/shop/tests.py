from django.test import TestCase
from .models import Product, ProductCategory, Brand


class BrandModelTest(TestCase):
    def setUp(self) -> None:
        self.brand = Brand.objects.create(title='brand title', logo='')

    def test_brand_model_entry(self):
        data = self.brand
        self.assertTrue(isinstance(data, Brand))
        
    def test_brand_entry_equal(self):
        data = self.brand
        self.assertEqual(str(data), 'brand title')