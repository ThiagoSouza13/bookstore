from rest_framework import serializers

from product.models import Product
from product.models.categories import Category
from product.serializers.categories_serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False, many=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, many=True)

    class Meta:
        model = Product
        fields = [
            'title',  
            'price',
            'category_id',
            'category'
        ]
        extra_kwargs = { "category": {"required": False} }
    
    def create(self, validated_data):
        category_ids = validated_data.pop('category_id', [])
        product = Product.objects.create(**validated_data)
        for category_id in category_ids:
            product.category.add(category_id)
        return product