from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def daftar_data_nelayan(request):
    data = {
        "title" : "Input Data Nelayan",
        "data_nelayan" : Nelayan.objects.all()
    }
    return render(request, 'daftar_data_nelayan.html',data)

@login_required(login_url=settings.LOGIN_URL)
def tambah_data_nelayan(request):
    if request.POST:
        form = NelayanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_data_nelayan')

    else:
        data = {
            "title" : "Input Data Nelayan",
            "form" : NelayanForm(),
            "headingJudul" : "Tambah"
        }
    return render(request, 'form_data_nelayan.html', data)

@login_required(login_url=settings.LOGIN_URL)
def edit_data_nelayan(request, id):
    instance_nelayan = Nelayan.objects.get(id=id)
    if request.POST:
        form = NelayanForm(request.POST, instance=instance_nelayan)
        if form.is_valid():
            form.save()
            return redirect('daftar_data_nelayan')

    else:
        data = {
            "title" : "Input Data Nelayan",
            "form" : NelayanForm(instance=instance_nelayan),
            "headingJudul" : "Edit"
        }
    return render(request, 'form_data_nelayan.html', data)

@login_required(login_url=settings.LOGIN_URL)
def hapus_data_nelayan(request, id):
    Nelayan.objects.get(id=id).delete()
    return redirect("daftar_data_nelayan")