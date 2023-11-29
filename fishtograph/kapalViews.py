from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def tambah_data_kapal(request):
    if request.POST:
        form = KapalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_data_kapal')

    else:
        data = {
            "title" : "Input Data Kapal",
            "form" : KapalForm(),
            "headingJudul" : "Tambah"
        }
    return render(request, 'form_data_kapal.html', data)

@login_required(login_url=settings.LOGIN_URL)
def daftar_data_kapal(request):
    data = {
        "title" : "Daftar Data Kapal",
        "data_kapal" : Kapal.objects.all()
    }
    return render(request, 'daftar_data_kapal.html', data)

@login_required(login_url=settings.LOGIN_URL)
def edit_data_kapal(request, id):
    instanceKapal = Kapal.objects.get(id=id)
    if request.POST:
        form = KapalForm(request.POST, instance=instanceKapal)
        if form.is_valid():
            form.save()
            return redirect('daftar_data_kapal')

    else:
        data = {
            "title" : "Edit Data Kapal",
            "form" : KapalForm(instance=instanceKapal),
            "headingJudul" : "Edit"
        }
    return render(request, 'form_data_kapal.html', data)

@login_required(login_url=settings.LOGIN_URL)
def hapus_data_kapal(request, id):
    Kapal.objects.get(id=id).delete()
    return redirect("daftar_data_kapal")