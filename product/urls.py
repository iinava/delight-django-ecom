from django.urls import path
from .views import (Home,ProductDetails,CategoryDetails)


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("product_details/<str:slug>/", ProductDetails.as_view(), name="product_details"),
    path("category_details/<str:slug>/", CategoryDetails.as_view(), name="category_details")
    
]
