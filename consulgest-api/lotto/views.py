from rest_framework import generics
from .serializers import LottoSerializer
from .models import Lotto
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
# Create your views here.

class LottoDetailsView(generics.ListCreateAPIView):
    queryset = Lotto.objects.all()
    serializer_class = LottoSerializer
    

class LottoByIDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lotto.objects.all()
    serializer_class = LottoSerializer
    
    def get(self, request, *args, **kwargs):
        
        #prendo id user loggato    
        user_logged = request.user.id
        
        #prendo l'id del lotto richiesto
        lotto_request = kwargs['pk']
    
        # #prendo lotto richiesto
        # queryset = Lotto.objects.filter(id = lotto_request)
        # serializer = self.get_serializer(queryset, many=True)
        
        # #estraggo dal lotto l'id_utente associato
        # user_request = queryset[0].utente.id
    
        
        # # confronto id utenti
        # if user_logged != user_request:
        #     return Response("Unauthorized access")
        
        # #caso in cui l'utente è autorizzato
        # return Response(serializer.data)
        
        try:
            # Prendo il lotto richiesto
            queryset = Lotto.objects.get(id=lotto_request)
            
            # Estraggo dall'oggetto lotto l'ID dell'utente associato
            user_request = queryset.utente.id

            # Confronto gli ID degli utenti
            if user_logged != user_request:
                return Response("Unauthorized access")

            # Caso in cui l'utente è autorizzato
            serializer = self.get_serializer(queryset)
            return Response(serializer.data)

        except Lotto.DoesNotExist:
            return Response("Lotto not found", status=404)
    
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']


# richiedo un lotto specifico
class LottoByIDUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LottoSerializer
    queryset = Lotto.objects.all()
    
    def get(self, request, *args, **kwargs):
        user_logged = request.user.id
        queryset = Lotto.objects.all().filter(utente =user_logged)
        serializer = self.get_serializer(queryset, many=True)
    
        return Response(serializer.data)
