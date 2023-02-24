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
    
    # def get_sub_categories(self):
    #     sub_categories = []
    #     for sub_category in self.sub_categories.all():
    #         sub_categories.append(sub_category)
    #         sub_categories.extend(sub_category.get_sub_categories())
    #     return sub_categories