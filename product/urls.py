from django.urls import path
from .views import (Home,ProductDetails)


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("product_details/", ProductDetails.as_view(), name="product_details")
    
]
