from rest_framework.serializers import ModelSerializer

from orders.models import SalesOrder


class OrderSerializer(ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ['user', 'name', 'description']
