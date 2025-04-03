from django.contrib import admin
from .models import Property, Flat, Appliance, ReplacementOption, Order

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('property', 'number')
    list_filter = ('property',)
    search_fields = ('number', 'property__name')

@admin.register(Appliance)
class ApplianceAdmin(admin.ModelAdmin):
    list_display = ('type', 'brand', 'model_number', 'flat', 'usage', 'within_warranty')
    list_filter = ('type', 'brand', 'within_warranty', 'usage')
    search_fields = ('brand', 'model_number', 'flat__number', 'flat__property__name')

@admin.register(ReplacementOption)
class ReplacementOptionAdmin(admin.ModelAdmin):
    list_display = ('appliance_type', 'brand', 'model', 'price', 'efficiency', 'matching_score')
    list_filter = ('appliance_type', 'brand', 'efficiency')
    search_fields = ('brand', 'model')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'flat', 'old_appliance', 'replacement_option', 'status', 'delivery_date')
    list_filter = ('status', 'delivery_date')
    search_fields = ('flat__number', 'flat__property__name', 'replacement_option__brand')
    readonly_fields = ('created_at', 'updated_at')
