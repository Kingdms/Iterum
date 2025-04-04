from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Properties"

class Flat(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='flats')
    number = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.property.name} / Flat number #{self.number}"

class Appliance(models.Model):
    APPLIANCE_TYPES = [
        ('washing_machine', 'Washing Machine'),
        ('dishwasher', 'Dishwasher'),
        ('refrigerator', 'Refrigerator'),
        ('oven', 'Oven'),
        ('microwave', 'Microwave'),
    ]
    
    USAGE_LEVELS = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
        ('very_high', 'Very High'),
    ]
    
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='appliances')
    type = models.CharField(max_length=50, choices=APPLIANCE_TYPES)
    brand = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    usage = models.CharField(max_length=20, choices=USAGE_LEVELS)
    within_warranty = models.BooleanField(default=False)
    installation_date = models.DateField(null=True, blank=True)
    image = models.ImageField(
        upload_to='appliance_images/',
        blank=True,
        null=True,
        default='default_images/default_appliance.jpg'  # Default image
    )
    def __str__(self):
        return f"{self.get_type_display()} - {self.brand} {self.model_number}"

class ReplacementOption(models.Model):
    EFFICIENCY_LEVELS = [
        ('good', 'Good'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
        ('very_high', 'Very High'),
    ]
    
    appliance_type = models.CharField(max_length=50, choices=Appliance.APPLIANCE_TYPES)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    efficiency = models.CharField(max_length=20, choices=EFFICIENCY_LEVELS)
    matching_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    # image_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='orders')
    old_appliance = models.ForeignKey(Appliance, on_delete=models.SET_NULL, null=True, related_name='replacement_orders')
    replacement_option = models.ForeignKey(ReplacementOption, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    delivery_date = models.DateField()
    delivery_time_hour = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])
    delivery_time_minute = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)])
    notification_email = models.EmailField(blank=True, null=True)
    notification_phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return f"Order {self.id} - {self.flat} - {self.replacement_option}"

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(
        upload_to='user_profiles/',
        blank=True,
        null=True,
        default='default_images/default_profile.jpg'  # Default image
    )