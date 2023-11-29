from django import forms
from .models import *

class DataPenangkapanForm(forms.ModelForm):

    class Meta:
        model = DataPenangkapan
        fields = '__all__'

        widgets = {
            'alat_tangkap' : forms.Select(attrs={
                'class' : 'form-control'
            }),
            'tanggal_penangkapan' : forms.DateInput(attrs={
                'class' : 'form-control', 'type' : 'date'
            })
        }

        labels = {
            'alat_tangkap': 'Jenis Alat Tangkap',
        }

class HasilTangkapForm(forms.ModelForm):

    class Meta:
        model = HasilTangkapan
        fields = '__all__'
        widgets = {
            'volume': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Volume',
                'type' : 'number'
                }),
            'harga': forms.NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Harga Ikan/KG',
                'type' : 'number'
                }),
            'nama_ikan': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Nama Ikan'
                })
        }
        labels = {
            'volume': 'Volume Ikan Ditangkap (Kg)',
            'harga': 'Harga Ikan per Kg',
        }

class NelayanForm(forms.ModelForm):

    class Meta:
        model = Nelayan
        fields = '__all__'
        widgets = {
            'umur': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'width: 100%;',
                'placeholder': 'Umur Nelayan',
                'type' : 'number'
                }),
            'nama_nelayan': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 100%;',
                'placeholder': 'Nama nelayan'
                }),
            'alamat': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 100%;',
                'placeholder': 'Alamat'
                })
        }

class KapalForm(forms.ModelForm):
    class Meta:
        model = Kapal
        fields = '__all__'
        widgets = {
            'besar_gt': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'width: 100%;',
                'placeholder': 'Besar Kapal (GT)',
                'type' : 'number'
                }),
            'nama_kapal': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 100%;',
                'placeholder': 'Nama kapal'
                }),
            'alat_tangkap': forms.Select(attrs={
                'class': "form-control", 
                'style': 'width: 100%;',
                'placeholder': 'alat_tangkap'
                })
        }

class HargaIkanForm(forms.ModelForm):
    class Meta:
        model = HargaIkan
        fields = ['harga']
        widget = {
            'harga': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'width: 100%;',
                'placeholder': 'Harga Ikan per Kg',
                'type' : 'number'
            }),
        }