from django.urls import path
from .views import AddToCart,CartItems


urlpatterns = [
    path("add_to_cart/<int:product_id>",AddToCart.as_view(), name="add_to_cart"),
    path("cart_items/",CartItems.as_view(), name="cart_items"),
]
