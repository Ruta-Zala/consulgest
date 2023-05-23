from rest_framework import generics
from .serializers import DossierSerializer
from .models import Dossier
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class DossierView(generics.ListAPIView):
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id']

class DossierCreate(generics.ListCreateAPIView):
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id']


class DossierViewQ(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer
    
    def get(self, request, *args, **kwargs):
        #prendo id user loggato    
        user_logged = request.user.id
        
        #prendo l'id del lotto richiesto
        dossier_request = kwargs['pk']
        
        try:
            # Prendo il lotto richiesto
            queryset = Dossier.objects.get(id=dossier_request)
            
            # Estraggo dall'oggetto lotto l'ID dell'utente associato
            user_request = queryset.id_lotto.utente.id

            # Confronto gli ID degli utenti
            if user_logged != user_request:
                return Response("Unauthorized access")

            # Caso in cui l'utente è autorizzato
            serializer = self.get_serializer(queryset)
            return Response(serializer.data)

        except Dossier.DoesNotExist:
            return Response("Dossier not found", status=404)
    
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

