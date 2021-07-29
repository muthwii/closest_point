from rest_framework import serializers
from .models import closest_point

class closest_point_serializer(serializers.ModelSerializer):
    class Meta:
        model = closest_point
        fields = ('points',)