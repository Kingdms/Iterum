from rest_framework import serializers
from .models import Property, Flat, Appliance, ReplacementOption, Order

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class FlatSerializer(serializers.ModelSerializer):
    property_name = serializers.ReadOnlyField(source='property.name')
    
    class Meta:
        model = Flat
        fields = ['id', 'property', 'property_name', 'number']

class ApplianceSerializer(serializers.ModelSerializer):
    flat_details = serializers.ReadOnlyField(source='flat.__str__')
    
    class Meta:
        model = Appliance
        fields = '__all__'

class ReplacementOptionSerializer(serializers.ModelSerializer):
    efficiency_display = serializers.ReadOnlyField(source='get_efficiency_display')
    
    class Meta:
        model = ReplacementOption
        fields = ['id', 'appliance_type', 'brand', 'model', 'price', 
                  'efficiency', 'efficiency_display', 'matching_score', 'image_url']

class OrderSerializer(serializers.ModelSerializer):
    flat_details = serializers.ReadOnlyField(source='flat.__str__')
    replacement_details = serializers.ReadOnlyField(source='replacement_option.__str__')
    status_display = serializers.ReadOnlyField(source='get_status_display')
    
    class Meta:
        model = Order
        fields = '__all__'
        
class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['flat', 'old_appliance', 'replacement_option', 'delivery_date', 
                  'delivery_time_hour', 'delivery_time_minute', 
                  'notification_email', 'notification_phone']