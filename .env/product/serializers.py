from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.Serializer):
    pk=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=200)
    product_category=serializers.CharField(max_length=200)
    created_date=serializers.DateTimeField()
    available_items=serializers.IntegerField()

    def create(self,validated_data):
        return Product.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.product_category=validated_data.get('product_category',instance.product_category)
        instance.created_date=validated_data.get('created_date',instance.created_date)
        instance.available_items=validated_data.get('available_items',instance.available_items)

        instance.save()

        return instance