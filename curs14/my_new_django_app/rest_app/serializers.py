from rest_framework import serializers
from rest_app.models import FancyCat, FluffyTiger

class FancyCatSerializer(serializers.ModelSerializer):

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError('Age cannot be less than 0')
        return value

    class Meta:
        model = FancyCat
        fields = ['id', 'name'] # sau ('__all__')


class FluffyTigerSerializer(serializers.ModelSerializer):

    class Meta:
        model = FluffyTiger
        fields = ['id', 'name']


class FluffyTigerAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = FluffyTiger
        fields = ('__all__')