from rest_framework import serializers
from .models import Lotto


class LottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lotto
        fields = '__all__'