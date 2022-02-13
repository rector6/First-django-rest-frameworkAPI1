from rest_framework import serializers
from .models import Category , Book ,products



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
        ]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'category', 
            'author',
            'isbn',
            'pages',
            'price',
            'stock' ,
            'imageurl',
            'status',
            'date_created',
         
        ]

class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = [
            'id',
            'product_tag',  
            'name',
            'category', 
            'price',
            'stock' ,
            'imageurl',
            'status',
            'date_created',
        ]
        