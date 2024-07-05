from django.shortcuts import render
from django.views import generic
from typing import Any, Dict  # Import Any and Dict from typing
from .models import Category, Product, Slider  

# Create your views here.

class Home(generic.TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs) -> Dict[str, Any]:  # Use Dict from typing
        context = super().get_context_data(**kwargs)
        context.update({
            'featured_categories': Category.objects.filter(featured=True),
            'featured_products': Product.objects.filter(featured=True),
            'sliders': Slider.objects.filter(show=True),
        })
        return context
    
    
class ProductDetails(generic.TemplateView):
    template_name = 'product/product_details.html'
