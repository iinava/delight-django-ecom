from django.shortcuts import render
from django.views import generic
from typing import Any, Dict
from .models import Category, Product, Slider

class Home(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'featured_categories': Category.objects.filter(featured=True),
            'featured_products': Product.objects.filter(featured=True),
            'sliders': Slider.objects.filter(show=True),
        })
        return context

class ProductDetails(generic.DetailView):
    model = Product
    slug_url_kwarg = 'slug'
    template_name = 'product/product_details.html'

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.get_object().get_related_products()
        return context
    
class CategoryDetails(generic.DetailView):
    model = Category
    slug_url_kwarg = 'slug'
    template_name = 'product/category_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.get_object().products.all()
        return context
