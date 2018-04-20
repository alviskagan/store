from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Produk, Kategori, Pelanggan

# Class model in admin 
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('id_produk','nama_produk','kategori_produk','stok_produk','foto_produk','harga_produk','rating_produk')
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('id_kategori', 'nama_kategori')
# class PelangganAdmin(admin.ModelAdmin):
#     list_display = ('id_pelanggan','username_pelanggan','password_pelanggan', 'nama_pelanggan','email','alamat_pelanggan','no_hp')

class PelangganInline(admin.StackedInline):
    model = Pelanggan
    can_delete = False
    verbose_name_plural = 'Profil'
    fk_name = 'pelanggan'

class CustomUserAdmin(UserAdmin):
    inlines = (PelangganInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location','get_no_hp')
    def get_no_hp(self,instance):
        return instance.pelanggan.no_hp
    get_no_hp.short_description = 'Nomor HP'
    def get_location(self, instance):
        return instance.pelanggan.alamat_pelanggan
    get_location.short_description = 'Alamat'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register your models here.        
admin.site.register(Produk, ProdukAdmin)
admin.site.register(Kategori, KategoriAdmin)
# admin.site.register(Pelanggan, PelangganAdmin)