from django.urls import path
from .views import (Home,ProductDetails,CategoryDetails,ProductList,SearchProducts)


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("product_details/<str:slug>/", ProductDetails.as_view(), name="product_details"),
    path("category_details/<str:slug>/", CategoryDetails.as_view(), name="category_details"),
    path("product_list/", ProductList.as_view(), name="product_list"),
    path("search_products/", SearchProducts.as_view(), name="search_products"),
    
    
]
