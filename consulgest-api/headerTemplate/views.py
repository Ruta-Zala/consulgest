from rest_framework import generics
from .serializers import TemplateSerializer, DefaultColumnsSerializer
from .models import Template, DefaultColumns
from django_filters.rest_framework import DjangoFilterBackend


class TemplateImportList(generics.ListAPIView):
    queryset = DefaultColumns.objects.all()
    serializer_class = DefaultColumnsSerializer
    
class TemplateView(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

class TemplateImportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
