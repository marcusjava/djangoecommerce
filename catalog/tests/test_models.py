from django.test import TestCase
from model_mommy import mommy
from .models import Category,Product
from django.core.urlresolvers import reverse

class CategoryTestCase(TestCase):

    def setUp(self):
        self.category = mommy.make(Category)

    def test_get_absolute_url(self):
        self.assertEquals(self.category.get_absolute_url,reverse('catalog:category',kwargs={'slug':self.category.slug}))
