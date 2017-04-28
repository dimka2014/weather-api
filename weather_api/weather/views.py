from rest_framework import generics, filters, permissions, viewsets, mixins, serializers, status
from rest_framework.response import Response
from django_pyowm.models import Location, Forecast

from weather_api.weather.utils import fetch_forecast_for_location
from .serializers import LocationSerializer, ForecastSerializer


class LocationsView(generics.ListAPIView):
    """
    Search available locations 
    """
    queryset = Location.objects.order_by('name')
    serializer_class = LocationSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )


class UserLocationsView(generics.ListAPIView):
    """
    List of user locations
    """
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Location.objects.filter(users=self.request.user).order_by('name')


class ForecastsView(generics.ListAPIView):
    """
    List of user location forecasts
    """
    serializer_class = ForecastSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return (Forecast.objects
                .filter(location__users=self.request.user)
                .select_related('location')
                .prefetch_related('weathers')
                .order_by('-reception_time'))


class UserLocationAddDeleteViewSet(mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    update:
    Add location for track

    destroy:
    Remove location from track
    """
    queryset = Location.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.Serializer

    def perform_destroy(self, instance):
        self.request.user.locations.remove(instance)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        self.request.user.locations.add(instance)
        if not Forecast.objects.filter(location_id=instance.id).exists():
            fetch_forecast_for_location(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
