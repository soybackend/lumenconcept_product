from rest_framework import serializers

from .models import (Category, MediaResource, Product)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class MediaResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaResource
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    id_category = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'code',
            'reference',
            'name',
            'description',
            'tecnical_descripcion',
            'id_category',
            'category',
            'score',
            'provider',
        )

    @classmethod
    def get_id_category(self, obj):
        try:
            return obj.category.id
        except:
            return None

    @classmethod
    def get_category(self, obj):
        try:
            return obj.category.name
        except:
            return None
