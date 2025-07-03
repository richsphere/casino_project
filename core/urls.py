from django.urls import path
from .views import (
	GuideListAPIView, GuideDetailAPIView,
     CasinoListAPIView, BonusListAPIView, CasinoDetailAPIView
)


urlpatterns = [
    path('api/guides/', GuideListAPIView.as_view(), name='guide-list'),
    path('api/guides/<slug:slug>/', GuideDetailAPIView.as_view(), \
         name='guide-detail'),
    path('api/casinos/', CasinoListAPIView.as_view(), name='casino-list'),
    path('api/casinos/<slug:slug>/', CasinoDetailAPIView.as_view(), \
         name='casino-detail'),
    path('api/bonuses/', BonusListAPIView.as_view(), name='bonus-list'),
]
