from rest_framework import serializers
from .models import DatiStandard

class DatiStandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatiStandard
        fields = '__all__'
