from rest_framework import serializers
from apps.products.models import *

#Serializers - changes one format to another

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"