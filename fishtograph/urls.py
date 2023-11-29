from django.urls import path

from .views import *
from .nelayanViews import *
from .kapalViews import *
from .penangkapanViews import *
from .hargaIkanViews import *

urlpatterns = [
    path('data-tangkapan/', daftar_data_penangkapan, name='daftar_data_penangkapan'),
    path('data-tangkapan/tambah/', tambah_data_penangkapan, name='tambah_data_penangkapan'),
    path('data-tangkapan/hapus/<int:id>', hapus_data_penangkapan, name='hapus_data_penangkapan'),
    path('data-nelayan/', daftar_data_nelayan, name='daftar_data_nelayan'),
    path('data-nelayan/tambah/', tambah_data_nelayan, name='tambah_data_nelayan'),
    path('data-nelayan/edit/<int:id>', edit_data_nelayan, name='edit_data_nelayan'),
    path('data-nelayan/hapus/<int:id>', hapus_data_nelayan, name='hapus_data_nelayan'),
    path('data-kapal/', daftar_data_kapal, name='daftar_data_kapal'),
    path('data-kapal/tambah/', tambah_data_kapal, name='tambah_data_kapal'),
    path('data-kapal/edit/<int:id>', edit_data_kapal, name='edit_data_kapal'),
    path('data-kapal/hapus/<int:id>', hapus_data_kapal, name='hapus_data_kapal'),
    path('data-harga-ikan/', daftar_data_harga_ikan, name='daftar_data_harga_ikan'),
    path('data-harga-ikan/edit/<int:id>', edit_data_harga_ikan, name='edit_data_harga_ikan'),
    path('dashboard/', main_dashboard, name='dashboard'),
]
