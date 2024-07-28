from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Advertisement
from .serializers import AdvertisementSerializer

class AdvertisementDetailAPIView(generics.RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    lookup_field = 'advertisement_id'
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        advertisement_id = kwargs.get(self.lookup_field)
        try:
            ad = Advertisement.objects.get(advertisement_id=advertisement_id)
        except Advertisement.DoesNotExist:
            raise NotFound("Advertisement not found")

        serializer = self.get_serializer(ad)
        return Response(serializer.data)



######################################################################
# Тут я ещё добавил дженерик на Список всех(в вашем ТЗ=10) объявлений (потому что там где "кокретный" там и "все")
class AdvertisementListView(generics.ListAPIView):
    queryset = Advertisement.objects.all()[:10]
    serializer_class = AdvertisementSerializer
