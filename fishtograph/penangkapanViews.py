from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def daftar_data_penangkapan(request):

    id_hasil_tangkapan = request.GET.get('hasil-tangkapan')

    data_penangkapan = DataPenangkapan.objects.all()

    data = {
        'title' : "PPN Karangantu",
        'data_penangkapan' : data_penangkapan
    }

    if id_hasil_tangkapan is not None :

        if not id_hasil_tangkapan.isdigit():
            return redirect('daftar_data_penangkapan')

        hasil_tangkapan = HasilTangkapan.objects.filter(data_penangkapan_id=id_hasil_tangkapan)
        
        if not hasil_tangkapan.exists():
            return redirect('daftar_data_penangkapan')

        data = {
            'title' : "PPN Karangantu",
            'data_penangkapan' : data_penangkapan,
            'hasil_tangkapan' : hasil_tangkapan
        }

    return render(request, 'daftar_data_penangkapan.html', data)

@login_required(login_url=settings.LOGIN_URL)
def tambah_data_penangkapan(request):

    extra_param = request.GET.get('extra')

    if not extra_param or not extra_param.isnumeric():
        return redirect('/fishtograph/data-tangkapan/tambah/?extra=1')

    extraValue=int(request.GET['extra'])

    if extraValue <= 0:
        extraValue = 1

    if extraValue >= 100:
        extraValue = 99


    HasilTangkapanFormSet = inlineformset_factory(
    DataPenangkapan, HasilTangkapan, form=HasilTangkapForm,
    extra=extraValue, can_delete=False
    )

    if request.method == 'POST':
        form = DataPenangkapanForm(request.POST)
        hasil_tangkapan_formset = HasilTangkapanFormSet(request.POST, prefix='hasil_tangkapan')

        if form.is_valid() and hasil_tangkapan_formset.is_valid():
            data_penangkapan = form.save()
            hasil_tangkapan_formset.instance = data_penangkapan
            hasil_tangkapan_formset.save()
            return redirect('daftar_data_penangkapan')

    else:
        form = DataPenangkapanForm()
        hasil_tangkapan_formset = HasilTangkapanFormSet(prefix='hasil_tangkapan')

    return render(request, 'tambah_data_penangkapan.html', {
        'form': form,
        'hasil_tangkapan_formset': hasil_tangkapan_formset,
        'extraValue' : extraValue
    })

@login_required(login_url=settings.LOGIN_URL)
def hapus_data_penangkapan(request, id):
    DataPenangkapan.objects.get(id=id).delete()
    return redirect("daftar_data_penangkapan")
