from rest_framework import serializers
from inventory.models import Inventory


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = Inventory
        fields = "__all__"

class InventorySerializer(serializers.ModelSerializer):
   class Meta:
       model = Inventory
       fields = ('name', 'code', 'batch', 'stock', 'deal', 'free', 'mrp', 'rate', 'exp', 'company', 'supplier')