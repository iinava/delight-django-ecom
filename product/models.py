from django.db import models

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['title']
        
    def __str__(self) -> str:
        return self.title
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE) 
    title=models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    thumbnail = models.URLField( )
    description = models.TextField(null=True,blank=True,default='N/A')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    
    
    class Meta:
        ordering = ['-id']
          
          
    def __str__(self) -> str:
        return self.title
    
    
    
class Slider(models.Model):
    title = models.CharField(max_length=50)
    banner= models.ImageField(upload_to='banners', height_field=None, width_field=None, max_length=None)
    show = models.BooleanField(default= True)
    created_at = models.DateTimeField(  auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.title
    

    
                  