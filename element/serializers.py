from rest_framework import serializers
from element import models

class ElementSerializer(serializers.ModelSerializer):
    element_img = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = models.Element
        fields = ('id', 'element_name', 'element_tag', 'element_type', 'element_img', 'creator_tag', 'creator_link')
