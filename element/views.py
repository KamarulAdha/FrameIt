from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters

from element import serializers
from element import models

# Create your views here.

class ElementViewSet(viewsets.ModelViewSet):
    queryset = models.Element.objects.all()
    serializer_class = serializers.ElementSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('element_name', 'element_tag', 'element_type',)
