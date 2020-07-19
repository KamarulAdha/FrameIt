from django.urls import path, include
from rest_framework.routers import DefaultRouter

from element import views

router = DefaultRouter()
# router.register('elements', views.ElementViewSet, basename='Elements')

urlpatterns = [
    # path('', include(router.urls)),
    path('elements/', views.ElementListAPIView.as_view())
]
