from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    url(r'^auth/$', obtain_jwt_token),

    url(r'^register/', views.RegistrationView.as_view()),
    url(r'^confirm/(?P<confirmation_token>[0-9A-Za-z]+)/$', views.EmailConfirmationView.as_view()),
    url(r'^reset-password-send-email/$', views.ResetPasswordEmailView.as_view()),
    url(r'^reset-password/(?P<reset_password_token>[0-9A-Za-z]+)/$', views.ResetPasswordView.as_view()),
    url(r'^change-password/$', views.ChangePasswordView.as_view()),
    url(r'^me/$', views.UserView.as_view()),
]
