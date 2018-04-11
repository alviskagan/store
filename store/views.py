from django.shortcuts import render
from .models import Produk, Kategori
import locale
# Create your views here.

locale.setlocale(locale.LC_ALL, '')


def index(request):
    #select_related digunakan untuk memanggil foreign key
    all_produks = Produk.objects.all().select_related('kategori_produk').order_by('kategori_produk')
    produk = {
        "data_produk": all_produks
    }
    return render(request, 'store/index.html', produk)

# def produk(request):
#     all_produks = Produk.objects.all().select_related('kategori_produk').order_by('kategori_produk')
#     produk = {
#         "data_produk": all_produks
#     }
#     return render(request, 'store/produk.html', produk)