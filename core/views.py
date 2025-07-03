from rest_framework import generics
from .models import Guide, Bonus, Casino
from .serializers import GuideSerializer, CasinoSerializer, BonusSerializer,\
     CasinoListSerializer
from django_filters.rest_framework import DjangoFilterBackend


class GuideListAPIView(generics.ListAPIView):
     queryset = Guide.objects.all()
     serializer_class = GuideSerializer
     
class GuideDetailAPIView(generics.RetrieveAPIView):
     queryset = Guide.objects.all()
     serializer_class = GuideSerializer
     lookup_field = 'slug'
     
class CasinoListAPIView(generics.ListAPIView):
     queryset = Casino.objects.all()
     serializer_class = CasinoListSerializer
     
class CasinoDetailAPIView(generics.RetrieveAPIView):
     queryset = Casino.objects.all()
     serializer_class = CasinoSerializer
     lookup_field = 'slug'
     
class BonusListAPIView(generics.ListAPIView):
     queryset = Bonus.objects.all()
     serializer_class = BonusSerializer
     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['bonus_type', 'casino']
