from rest_framework import serializers
from .models import Orders

class ordersSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Orders
        fields = ('OrderID', 'CustomerID', 'EmployeeID', 'OrderDate',"RequiredDate","ShippedDate","ShipVia","Freight")
        read_only_fields = ('date_created', 'date_modified')