from django.shortcuts import render
from rest_framework import viewsets
from fishtograph.models import DataPenangkapan
from .serializers import *

class DataPenangkapanViewSet(viewsets.ModelViewSet):
    queryset = DataPenangkapan.objects.all()
    serializer_class = DataPenangkapanSerializer
    http_method_names = ['get', 'options']

class NelayanViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Nelayan.objects.all()
    serializer_class = NelayanSerializer
    http_method_names = ['get', 'options']

class KapalViewset(viewsets.ModelViewSet):
    queryset = Kapal.objects.all()
    serializer_class = KapalSerializer
    http_method_names = ['get', 'options']

# Data For Post Method
# const postData = {
#   alat_tangkap: 'Jaring',
#   tanggal_penangkapan: '2023-10-18',
#   hasil_tangkapan: [
#     {
#       nama_ikan: 'Peperek',
#       harga: 2000,
#       volume: 30
#     }
#   ]
# };