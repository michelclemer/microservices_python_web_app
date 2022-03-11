from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):  # api/products

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/products
        serialize = ProductSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
