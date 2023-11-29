from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def daftar_data_harga_ikan(request):
    data = {
        "title" : "Daftar Harga Ikan",
        "data_harga" : HargaIkan.objects.all()
    }
    return render(request, 'daftar_data_harga_ikan.html',data)

@login_required(login_url=settings.LOGIN_URL)
def edit_data_harga_ikan(request, id):
    instance_harga = HargaIkan.objects.get(id=id)
    if request.POST:
        form = HargaIkanForm(request.POST, instance=instance_harga)
        if form.is_valid():
            form.save()
            return redirect('daftar_data_harga_ikan')
    else:
        data = {
            "title" : "Edit Data Harga Ikan",
            "form" : HargaIkanForm(instance=instance_harga),
            "headingJudul" : "Edit",
            "ikan_edit" : instance_harga.nama_ikan
        }
    return render(request, 'form_data_harga_ikan.html', data)