from django_pyowm import models
from rest_framework import serializers

from weather_api.core.serializers import RawJSONField


class WeatherSerializer(serializers.ModelSerializer):
    rain = RawJSONField()
    snow = RawJSONField()
    wind = RawJSONField()
    pressure = RawJSONField()
    temperature = RawJSONField()

    class Meta:
        model = models.Weather
        fields = ('reference_time', 'sunrise_time', 'sunset_time', 'clouds', 'rain', 'snow', 'wind', 'humidity',
                  'pressure', 'temperature', 'status', 'detailed_status', 'weather_code', 'weather_icon_name',
                  'visibility_distance', 'dewpoint', 'humidex', 'heat_index')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('id', 'name', 'lat', 'lon', 'country')


class ForecastSerializer(serializers.ModelSerializer):
    weathers = WeatherSerializer(many=True)
    location = LocationSerializer()

    class Meta:
        model = models.Forecast
        fields = ('weathers', 'location')
