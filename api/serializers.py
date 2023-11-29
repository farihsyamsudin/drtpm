# serializers.py
from rest_framework import serializers
from fishtograph.models import *

class HasilTangkapanSerializer(serializers.ModelSerializer):
    class Meta:
        model = HasilTangkapan
        fields = ['nama_ikan', 'harga', 'volume']

class DataPenangkapanSerializer(serializers.ModelSerializer):
    hasil_tangkapan = HasilTangkapanSerializer(many=True)

    class Meta:
        model = DataPenangkapan
        fields = ['id', 'alat_tangkap', 'tanggal_penangkapan', 'hasil_tangkapan']

class NelayanSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Nelayan
        fields = ['id', 'nama_nelayan', 'umur', 'alamat']

class KapalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kapal
        fields = ['id', 'nama_kapal', 'besar_gt', 'alat_tangkap_kapal']