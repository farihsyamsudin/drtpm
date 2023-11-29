from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(DataPenangkapan)
admin.site.register(HasilTangkapan)
admin.site.register(Nelayan)
admin.site.register(Kapal)
admin.site.register(HargaIkan)