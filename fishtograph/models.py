from django.db import models

# Create your models here.

# Alat Tangkap
LEMPURA = "Lempura Dasar"
PAYANG = "Payang"
BAGANBERPERAHU = "Bagan Berperahu"
JARINGINSANGTETAP = "Jaring Insang Tetap"
JARINGINSANGBERLAPIS = "Jaring Insang Berlapis"
BUBU = "Bubu (Pots)"
BUBUBERSAYAP = "Bubu Bersayap (Fyke Nets)"

AlatTangkapChoices = [
    (LEMPURA, "Lempura Dasar"),
    (PAYANG, "Payang"),
    (BAGANBERPERAHU, "Bagan Berperahu"),
    (JARINGINSANGTETAP, "Jaring Insang Tetap"),
    (JARINGINSANGBERLAPIS, "Jaring Insang Berlapis"),
    (BUBU, "Bubu (Pots)"),
    (BUBUBERSAYAP, "Bubu Bersayap (Fyke Nets)")
]
# Alat Tangkap

class DataPenangkapan(models.Model):
    alat_tangkap = models.CharField(choices=AlatTangkapChoices, default=LEMPURA, max_length=255)
    tanggal_penangkapan = models.DateField(null=True)

    def __str__(self):
        return self.alat_tangkap
    
class HasilTangkapan(models.Model):
    data_penangkapan = models.ForeignKey(DataPenangkapan, on_delete=models.CASCADE, related_name='hasil_tangkapan')
    nama_ikan = models.CharField(max_length=255)
    harga = models.IntegerField()
    volume = models.IntegerField()

    def __int__(self):
        return self.data_penangkapan
    
class Nelayan(models.Model):
    nama_nelayan = models.CharField(max_length=200)
    umur = models.IntegerField()
    alamat = models.TextField()

class Kapal(models.Model):
    nama_kapal = models.CharField(max_length=100)
    besar_gt = models.IntegerField()
    alat_tangkap_kapal = models.CharField(choices=AlatTangkapChoices, default=LEMPURA, max_length=255)

class HargaIkan(models.Model):
    nama_ikan = models.CharField(max_length=100)
    harga = models.IntegerField()
