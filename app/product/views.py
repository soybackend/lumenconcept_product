from product import urls

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import response, schemas
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes, permission_classes

from .models import (Category, MediaResource, Product)
from .serializers import (CategorySerializer, ProductDetailSerializer,
                          MediaResourceSerializer, ProductSerializer)

# Create your views here.
@api_view()
@permission_classes((AllowAny, ))
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='LumenConcept Product API Docs',
                                        patterns=urls.api_url_patterns,
                                        url='/api/v1/')
    return response.Response(generator.get_schema())


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class MediaResourceViewSet(viewsets.ModelViewSet):
    serializer_class = MediaResourceSerializer
    queryset = MediaResource.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def retrieve_code(self, request, code):
        queryset = Product.objects.filter(code=code, active=True)
        offer = get_object_or_404(queryset)
        serializer = ProductDetailSerializer(offer)
        return Response(serializer.data)
