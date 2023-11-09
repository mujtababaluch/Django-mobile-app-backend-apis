from rest_framework import serializers
from .models import User, products
from .models import Size
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('name',)

class ProductsSerializer(serializers.ModelSerializer):
    size_one = SizeSerializer()
    size_two = SizeSerializer()
    size_three = SizeSerializer()
    size_four = SizeSerializer()

    class Meta:
        model = products
        fields = (
            'id',
            'product_name',
            'product_desc',
            'price',
            'color',
            'product_picone',
            'product_pictwo',
            'product_picthree',
            'product_picfour',
            'Category_name',
            'size_one',
            'size_two',
            'size_three',
            'size_four',
        )
class ProductsearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'

# users/serializers.py


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
