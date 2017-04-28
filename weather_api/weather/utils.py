from django.db import transaction
from django_pyowm import models
from django_pyowm.models import Location

from .singletons import owm


def fetch_forecasts():
    begin = 0
    step = 50
    end = step
    iterate = True
    while iterate:
        locations = Location.objects.filter(users__isnull=False)[begin:end]
        for location in locations:
            fetch_forecast_for_location(location)
        iterate = len(locations) == step
        begin += step
        end += step


@transaction.atomic
def fetch_forecast_for_location(location):
    old_forecasts_ids = [forecast.id for forecast in models.Forecast.objects.filter(location=location)]
    forecast_entity = owm.three_hours_forecast_at_id(location.city_id).get_forecast()
    forecast = models.Forecast.from_entity(forecast_entity)
    forecast.location = location
    forecast.save()
    for weather_entity in forecast_entity.get_weathers():
        weather = models.Weather.from_entity(weather_entity)
        weather.save()
        forecast.weathers.add(weather)
    models.Weather.objects.filter(forecasts__id__in=old_forecasts_ids).delete()
    models.Forecast.objects.filter(id__in=old_forecasts_ids).delete()
