
from rest_framework import serializers
from .models import NatPark


class NatParkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'ntitle',
            'ndescription',
            'npicture',
            'nlocation',
        )
        model = NatPark
