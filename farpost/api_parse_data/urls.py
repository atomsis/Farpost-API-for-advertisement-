from django.urls import path
from .views import AdvertisementListView,AdvertisementDetailAPIView

app_name = 'api'

urlpatterns = [
    path('ad/<int:advertisement_id>/', AdvertisementDetailAPIView.as_view(), name='advertisement_detail'),
    path('ad/', AdvertisementListView.as_view(), name='advertisement_list'),
]
