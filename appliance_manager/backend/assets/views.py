from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Property, Flat, Appliance, ReplacementOption, Order
from .serializers import (
    PropertySerializer, FlatSerializer, ApplianceSerializer,
    ReplacementOptionSerializer, OrderSerializer, OrderCreateSerializer
)

class PropertyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class FlatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
    
    def get_queryset(self):
        queryset = Flat.objects.all()
        property_id = self.request.query_params.get('property_id')
        if property_id:
            queryset = queryset.filter(property_id=property_id)
        return queryset

class ApplianceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    
    def get_queryset(self):
        queryset = Appliance.objects.all()
        flat_id = self.request.query_params.get('flat_id')
        if flat_id:
            queryset = queryset.filter(flat_id=flat_id)
        return queryset

class ReplacementOptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReplacementOption.objects.all()
    serializer_class = ReplacementOptionSerializer
    
    def get_queryset(self):
        queryset = ReplacementOption.objects.all()
        appliance_type = self.request.query_params.get('appliance_type')
        if appliance_type:
            queryset = queryset.filter(appliance_type=appliance_type)
        return queryset

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return OrderCreateSerializer
        return OrderSerializer
    
    def get_queryset(self):
        queryset = Order.objects.all()
        flat_id = self.request.query_params.get('flat_id')
        if flat_id:
            queryset = queryset.filter(flat_id=flat_id)
        return queryset

@api_view(['GET'])
def get_replacement_options_for_appliance(request, appliance_id):
    try:
        appliance = Appliance.objects.get(id=appliance_id)
        replacement_options = ReplacementOption.objects.filter(
            appliance_type=appliance.type
        ).order_by('-matching_score')
        serializer = ReplacementOptionSerializer(replacement_options, many=True)
        return Response(serializer.data)
    except Appliance.DoesNotExist:
        return Response(
            {"error": "Appliance not found"},
            status=status.HTTP_404_NOT_FOUND
        )
