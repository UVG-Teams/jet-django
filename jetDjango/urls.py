"""jetDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

from rest_framework import routers
from rest_framework_jet.views import (
    generate_jet,
    verify_jet,
    refresh_jet,
)

from init import create_initial_data

from users.views import UserViewSet
from locations.views import LocationViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^admin/initial-data/', create_initial_data),
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^api/token-auth/', generate_jet),
    url(r'^api/token-verify/', verify_jet),
    url(r'^api/token-refresh/', refresh_jet),
]
