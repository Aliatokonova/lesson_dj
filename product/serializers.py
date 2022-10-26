from rest_framework import serializers
from django.db.models import Avg
from .models import Product
from category.models import Category

class ProductListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Product
        fields = ('owner', 'title', 'price', 'image')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        print(instance, '\n'+'='*100)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        return repr

    
class ProductDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    category = serializers.PrimaryKeyRelatedField(required=True,
                                                    queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        print(instance, '\n'+'='*100)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        repr['rating_count'] = instance.reviews.count()
        return repr
