#testing urls using reverse and resolve method when passing variables

from django.test import TestCase
from django.urls import resolve, reverse
from shop.views import allproducts


class TestHome(TestCase):
    def test_url(self):
        url=reverse('product_by_category',args=['demo-slug'])
        print("url is: ", url)
        print("Resolve: ", resolve(url))
        self.assertEqual(resolve(url).func, allproducts)