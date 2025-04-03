from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'properties', views.PropertyViewSet)
router.register(r'flats', views.FlatViewSet)
router.register(r'appliances', views.ApplianceViewSet)
router.register(r'replacement-options', views.ReplacementOptionViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('appliances/<int:appliance_id>/replacement-options/', 
         views.get_replacement_options_for_appliance, 
         name='appliance-replacement-options'),
]