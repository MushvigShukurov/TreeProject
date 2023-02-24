from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="sub_categories")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.category_name
    
