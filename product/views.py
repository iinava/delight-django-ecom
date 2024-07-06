from django.shortcuts import render
from django.views import generic
from typing import Any, Dict
from .models import Category, Product, Slider
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
    InvalidPage
)


class Home(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'featured_categories': Category.objects.filter(featured=True),
            'featured_products': Product.objects.filter(featured=True),
            'sliders': Slider.objects.filter(show=True),
        })
        print(context)
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

class CustomPagination:
    def __init__(self, request, queryset, paginated_by):
        self.paginated_by = paginated_by
        self.paginator = Paginator(queryset, paginated_by)
        self.queryset = queryset
        self.page = request.GET.get('page', 1)
        
    def get_queryset(self):
        try:
            queryset = self.paginator.page(self.page)
        except PageNotAnInteger:
            queryset = self.paginator.page(1)
        except EmptyPage:
            queryset = self.paginator.page(1)
        except InvalidPage:
            queryset = self.paginator.page(1)
        return queryset            
            
                         
                           
        

 
class ProductList(generic.ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'object_list'
    paginate_by = 8
    
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = CustomPagination(self.request,self.get_queryset(),self.paginate_by)
        paginator = page_obj.paginator
        queryset = page_obj.get_queryset()
        
        context['object_list'] = queryset
        context['paginator'] = paginator
        return context
        
     