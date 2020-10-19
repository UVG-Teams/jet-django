from rest_framework import serializers

from locations.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id',
            'name',
            'shortname',
            'postcode',
            'code',
            'location_type',
            'parent',
            'latitude',
            'longitude',
            'language',
        )