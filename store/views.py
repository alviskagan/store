from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Produk, Kategori, Pelanggan
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms  import UserCreationForm
import locale
# from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
# Create your views here.

locale.setlocale(locale.LC_ALL, '')


def index(request):
    #select_related digunakan untuk memanggil foreign key
    all_produks = Produk.objects.all().select_related('kategori_produk').order_by('kategori_produk')
    all_kategori = Kategori.objects.all()
    
    produk = {
        "data_produk": all_produks,
        "kategori_produk": all_kategori
    }
    
    return render(request, 'store/index.html', produk)

def detail_produk(request, id_produk):

    #pashing data dari views index
    # if request.method == 'GET':
    # # blom fix
    # data_produk = request.GET.get("id_produk", "")
    all_produks = Produk.objects.filter( id_produk = id_produk ).select_related('kategori_produk')
    all_kategori = Kategori.objects.all()

    produk = {
        "data_produk": all_produks,
        "kategori_produk": all_kategori
    }

    return render(request, 'store/produk/detail_produk.html', produk)


@login_required
def home(request):
    return render(request, 'store/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('store/registration/login.html')
    else:
        form = SignUpForm()
    return render(request, 'store/registration/signup.html', {'form': form})
