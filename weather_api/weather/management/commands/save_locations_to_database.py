from django.core.management import BaseCommand
from django_pyowm.models import Location
from pyowm.webapi25.location import Location as LocationEntity

from weather_api.weather.singletons import owm


class Command(BaseCommand):
    help = 'Save all locations from file to database'

    def handle(self, *args, **options):
        if Location.objects.exists():
            self.stderr.write('You can save locations only to empty table')
            return

        city_registry = owm.city_id_registry()
        locations = []
        for line in city_registry._get_all_lines():
            tokens = line.strip().split(',')
            try:
                location_entity = LocationEntity(tokens[0], float(tokens[3]), float(tokens[2]), int(tokens[1]), tokens[4])
                location = Location.from_entity(location_entity)
                locations.append(location)
            except ValueError:
                pass
        Location.objects.bulk_create(locations, 10000)
        self.stdout.write(self.style.SUCCESS('{} locations saved to database'.format(len(locations))))
