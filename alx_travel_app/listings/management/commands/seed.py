from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = 'Seeds the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_listings = [
            {
                "title": "Beachside Villa",
                "description": "A beautiful villa with ocean views.",
                "price_per_night": 120.00,
                "location": "Malibu"
            },
            {
                "title": "Mountain Cabin",
                "description": "A cozy cabin in the mountains.",
                "price_per_night": 85.50,
                "location": "Aspen"
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the city center.",
                "price_per_night": 150.00,
                "location": "New York"
            }
        ]

        for item in sample_listings:
            Listing.objects.create(
                title=item["title"],
                description=item["description"],
                price_per_night=item["price_per_night"],
                location=item["location"],
                available=random.choice([True, False])
            )
        
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))