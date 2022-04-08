from rest_framework import serializers
from .models import AnnouncedPuResults, Lga

class PUSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncedPuResults
        fields = "__all__"

class LgaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lga
        fields = "__all__"