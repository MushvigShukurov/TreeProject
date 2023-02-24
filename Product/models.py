from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from Category.models import Category
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100) # Mehsulun Adi
    product_image = models.ImageField(blank=True,null=True) # Mehsulun Şekli (Optional)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products") # Kategoriya
    price = models.FloatField(
        validators=[MinValueValidator(0)]
    ) # Qiymeti (AZN)
    description = models.TextField() # Aciqlamasi
    date_of_production = models.DateTimeField() # Istehsal Tarixi
    storage_period = models.PositiveIntegerField() # Saxlama Müddəti (Gün İlə)
    discount_rate = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0),MaxValueValidator(50)]
    ) # Endirim Faizi (min=0,max=50)
    created_at = models.DateTimeField(auto_now_add=True) # Əlavə edildiyi tarix
    updated_at = models.DateTimeField(auto_now=True) # Update edildiyi tarix

    def __str__(self) -> str:
        return self.product_name

