from django.shortcuts import render,get_object_or_404,redirect
from .carts import Cart
from django.views import generic
from product.models import Product

# Create your views here.
class AddToCart(generic.View):
    
    def post(self, *args , **kwargs):
        # product = Product.objects.get(id=product.id)
        product = get_object_or_404(Product,id=kwargs.get('product_id'))
        cart = Cart(self.request)
        cart.update(product.id,1)
        return redirect('cart_items')


class  CartItems(generic.TemplateView):
    template_name = 'cart/cart.html'