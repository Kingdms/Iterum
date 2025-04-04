from django.contrib import admin
from .models import Property, Flat, Appliance, ReplacementOption, Order, User
from django.utils.html import format_html

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
    list_display = ('type', 'brand', 'model_number', 'flat', 'usage', 'within_warranty', 'image_preview')
    list_filter = ('type', 'brand', 'within_warranty', 'usage')
    search_fields = ('brand', 'model_number', 'flat__number', 'flat__property__name')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return format_html('<img src="/media/default_images/default_appliance.jpg" style="width: 50px; height: 50px;" />')
    image_preview.short_description = "Image Preview"

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

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'profile_picture_preview')
    readonly_fields = ('profile_picture_preview',)

    def profile_picture_preview(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.profile_picture.url)
        return format_html('<img src="/media/default_images/default_profile.jpg" style="width: 50px; height: 50px;" />')
    profile_picture_preview.short_description = "Profile Picture Preview"
