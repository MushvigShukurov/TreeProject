from rest_framework import serializers
from Category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='category-detail')
    products = serializers.HyperlinkedRelatedField(many=True,view_name='product-detail',read_only=True)
    class Meta:
        model = Category
        fields = "__all__"

