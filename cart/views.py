from django.shortcuts import render,get_object_or_404,redirect
from .carts import Cart
from django.views import generic
from product.models import Product
from django.contrib import messages

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
    
    def get(self,request, *args, **kwargs):
        product_id = request.GET.get('product_id',None)
        quantity = request.GET.get('quantity',None)
        clear=request.GET.get('clear',False)
        cart = Cart(request)
        if product_id and quantity:
            product = get_object_or_404(Product,id=product_id )
            if int(quantity) > 0:   
                if product.instock:
                    cart = Cart(request)
                    cart.update(int(product_id),int(quantity))
                    return redirect('cart_items')
                else:
                    messages.warning(request,"the product is not in stock anymore")
                    return redirect('cart_items')
            else:
                cart.update(int(product_id),int(quantity))
                return redirect('cart_items')
        
        
        if clear:
            cart.clear()
            return redirect('cart_items')
        
            
            
        return super().get(request,*args, **kwargs)