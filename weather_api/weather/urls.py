from django.conf.urls import url

from . import views

locations_add_delete = views.UserLocationAddDeleteViewSet.as_view({
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^locations/all/$', views.LocationsView.as_view()),
    url(r'^locations/$', views.UserLocationsView.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/$', locations_add_delete),
    url(r'^forecasts/$', views.ForecastsView.as_view()),
]
