from cmath import exp
from rest_framework import viewsets, generics
from django.shortcuts import render
from inventory.serializers import InventorySerializer, FileUploadSerializer, SaveFileSerializer
from inventory.models import Inventory
import io, csv, pandas as pd
from rest_framework.response import Response
from rest_framework import generics, status
from datetime import datetime
from rest_framework import filters


class CustomSearchFilter(filters.SearchFilter):
    search_param = "supplier"

class InventoryViewSet(viewsets.ModelViewSet):
   queryset = Inventory.objects.all()
   serializer_class = InventorySerializer
   name = "inventory-list"
   search_fields = ['supplier']
   filter_backends = [CustomSearchFilter]
#    filter_fields = (
#         'name',
#         'supplier',
#     )


class Unexpired(viewsets.ModelViewSet):
   queryset = Inventory.objects.all()
   serializer_class = InventorySerializer
   name = "inventory-list"
   search_fields = ['supplier']
   filter_backends = [CustomSearchFilter]
   current_date = datetime.now().date()
   queryset = Inventory.objects.filter(exp__gte=current_date)

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            expdate = datetime.strptime(row['exp'], "%d/%m/%Y").strftime('%Y-%m-%d')
            new_file = Inventory(
                name = row['name'],
                code = row['code'],
                batch = row['batch'],
                stock = row['stock'],
                deal = row['deal'],
                free = row['free'],
                mrp = row['mrp'],
                rate = row['rate'],
                exp = expdate,
                company = row['company'],
                supplier = row['supplier']
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)