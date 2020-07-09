from django.contrib import admin

from element import models
# Register your models here.

class ElementModel(admin.ModelAdmin):
    list_display = ('id', 'element_tag', 'element_type', 'element_img', 'creator_tag', 'creator_link')

admin.site.register(models.Element, ElementModel)
