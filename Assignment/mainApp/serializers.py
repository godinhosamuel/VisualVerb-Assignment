from rest_framework import serializers
from .models import *

class SupermarketSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupermarketSale
        fields = '__all__'