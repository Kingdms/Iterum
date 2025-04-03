from django.core.management.base import BaseCommand
from django.utils import timezone
from assets.models import Property, Flat, Appliance, ReplacementOption
import datetime

class Command(BaseCommand):
    help = 'Populates the database with initial data for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database...')
        
        # Create property
        property_obj, created = Property.objects.get_or_create(
            name='Blackhorse Mills',
            defaults={'address': '1 Blackhorse Lane, London'}
        )
        self.stdout.write(f'{"Created" if created else "Found"} property: {property_obj.name}')
        
        # Create flat
        flat_obj, created = Flat.objects.get_or_create(
            property=property_obj,
            number='101'
        )
        self.stdout.write(f'{"Created" if created else "Found"} flat: {flat_obj}')
        
        # Create appliance
        appliance_obj, created = Appliance.objects.get_or_create(
            flat=flat_obj,
            type='washing_machine',
            defaults={
                'brand': 'Bosch',
                'model_number': '95I/LPQ',
                'usage': 'high',
                'within_warranty': True,
                'installation_date': timezone.now() - datetime.timedelta(days=365)
            }
        )
        self.stdout.write(f'{"Created" if created else "Found"} appliance: {appliance_obj}')
        
        # Create replacement options
        replacement_options = [
            {
                'appliance_type': 'washing_machine',
                'brand': 'Bosch',
                'model': '95I/LPQ',
                'price': 3456.00,
                'efficiency': 'moderate',
                'matching_score': 100,
                'image_url': 'https://example.com/images/bosch_95i_lpq.jpg'
            },
            {
                'appliance_type': 'washing_machine',
                'brand': 'Samsung',
                'model': 'LIK889',
                'price': 4078.00,
                'efficiency': 'high',
                'matching_score': 98,
                'image_url': 'https://example.com/images/samsung_lik889.jpg'
            },
            {
                'appliance_type': 'washing_machine',
                'brand': 'IFB',
                'model': 'IF778',
                'price': 4431.00,
                'efficiency': 'high',
                'matching_score': 70,
                'image_url': 'https://example.com/images/ifb_if778.jpg'
            },
            {
                'appliance_type': 'washing_machine',
                'brand': 'LG',
                'model': 'LG5677',
                'price': 3549.00,
                'efficiency': 'good',
                'matching_score': 90,
                'image_url': 'https://example.com/images/lg_lg5677.jpg'
            }
        ]
        
        for option_data in replacement_options:
            option, created = ReplacementOption.objects.get_or_create(
                appliance_type=option_data['appliance_type'],
                brand=option_data['brand'],
                model=option_data['model'],
                defaults={
                    'price': option_data['price'],
                    'efficiency': option_data['efficiency'],
                    'matching_score': option_data['matching_score'],
                    'image_url': option_data['image_url']
                }
            )
            self.stdout.write(f'{"Created" if created else "Found"} replacement option: {option}')
        
        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))