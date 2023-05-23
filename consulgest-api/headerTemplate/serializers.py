from rest_framework import serializers
from .models import Template , DefaultColumns


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class DefaultColumnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultColumns
        fields = '__all__'