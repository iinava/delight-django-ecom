from django.db import models

# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    discount = models.PositiveIntegerField(help_text="discount in percentage")
    active = models.BooleanField(default=True)
    active_date = models.DateField()
    expiry_date = models.DateField()
    required_amount_touse_coupon = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.code
    
    
