from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def main_dashboard(request):
    data = {
        'title' : 'Dashboard Admin',
        'total_data_nelayan' : Nelayan.objects.count(),
        'total_data_penangkapan' : DataPenangkapan.objects.count(),
        'total_data_ikan_ditangkap' : HasilTangkapan.objects.count(),
        'total_data_kapal' : Kapal.objects.count(),
    }
    return render(request, 'dashboard_admin.html', data)

def landing_page(request):
    data = {
        'title' : "Fishtograph"
    }
    return render(request, 'landing_page.html', data)

def handler404(request, exception):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')