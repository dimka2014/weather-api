from django.conf import settings
from pyowm import OWM

owm = OWM(API_key=settings.OWM_KEY, version='2.5')
