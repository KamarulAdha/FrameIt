from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework import filters
from rest_framework import generics
from rest_framework.response import Response

from .models import Element
from element import serializers
from element import models

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

#Testing
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import status


# Create your views here.

# class ElementViewSet(viewsets.ModelViewSet):
#     queryset = models.Element.objects.all()
#     serializer_class = serializers.ElementSerializer
#
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('element_name', 'element_tag', 'element_type',)

class ElementListAPIView(ListModelMixin, GenericAPIView):
    queryset = Element.objects.all()
    serializer_class = serializers.ElementSerializer

    #Testing
    permission_classes = [HasAPIKey]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('element_name', 'element_tag', 'element_type',)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs, status=status.HTTP_200_OK)
