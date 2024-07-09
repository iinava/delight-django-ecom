from django.shortcuts import render,get_object_or_404,redirect
from .carts import Cart
from django.views import generic
from product.models import Product
from django.contrib import messages
from .models import Coupon
from django.utils import timezone
from datetime import datetime

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
        # print(cart.coupon)c
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
    
    
class Addcoupon(generic.View):
    def post(self, *args, **kwargs):
        code = self.request.POST.get('coupon')
        coupon= Coupon.objects.filter(code=code)
        cart = Cart(self.request)
        
        if coupon.exists():
            coupon=coupon.first()
            current_time= timezone.now().date()
            active_date = coupon.active_date
            expiry_date=coupon.expiry_date
            
            if current_time > expiry_date:
                messages.warning(self.request, 'Coupon expired')
                return redirect('cart_items')
            
            if current_time < active_date:
                messages.warning(self.request, 'Coupon is yet to be available')
                return redirect('cart_items')
            if cart.total() < coupon.required_amount_touse_coupon:
                messages.warning(self.request, f'You have to shop at least {coupon.required_amount_touse_coupon} to use this coupon')
                return redirect('cart_items')
            
            cart.add_coupon(coupon.id)
            messages.success(self.request, 'you coupon has been included')
            return redirect('cart_items')
        else:
            messages.warning(self.request, 'Invalid coupon')
            return redirect('cart_items')