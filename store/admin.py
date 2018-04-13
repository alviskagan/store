from django.contrib import admin
from .models import Produk, Kategori, Pelanggan

# Class model in admin 
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('id_produk','nama_produk','kategori_produk','stok_produk','foto_produk','harga_produk','rating_produk')
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('id_kategori', 'nama_kategori')
class PelangganAdmin(admin.ModelAdmin):
    list_display = ('id_pelanggan','username_pelanggan','password_pelanggan', 'nama_pelanggan','email','alamat_pelanggan','no_hp')
# Register your models here.        
admin.site.register(Produk, ProdukAdmin)
admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Pelanggan, PelangganAdmin)