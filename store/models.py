import uuid, os, time

from django.db import models
#from djmoney.models.fields import MoneyField
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import locale

# Create your models here.
class Pelanggan(models.Model):
    pelanggan = models.OneToOneField(User, on_delete= models.CASCADE, null = True)
    id_pelanggan = models.AutoField(primary_key = True)
    tanggal_lahir = models.DateField(null = True, blank = True)
    alamat_pelanggan = models.CharField(max_length = 250, blank = True)
    no_hp = models.CharField(max_length= 30, blank = True)
    def __str__(self):
        return self.pelanggan.username
        
class Detail_rekomendasi (models.Model):
    id_detail_rekomendasi = models.AutoField(primary_key= True)
    hasil_rekomendasi = models.FloatField(max_length= 250)

class Kategori (models.Model):
    id_kategori = models.AutoField(primary_key= True)
    nama_kategori = models.CharField(max_length= 250)
    def __str__(self):
        return self.nama_kategori

class Produk(models.Model):
    id_produk = models.AutoField(primary_key = True)
    nama_produk = models.CharField(max_length = 250)
    kategori_produk = models.ForeignKey(
        Kategori,
        null = False,
        on_delete = models.CASCADE,
        related_name= 'kategori'
    )
    stok_produk = models.IntegerField()
    harga_produk = models.IntegerField()
    rating_produk = models.IntegerField() 

    #Untuk mengubah nama file yang diupload lalu disimpan ke dalam folder foto 
    def content_file_name(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s_%s.%s" % (instance.id_produk, instance.kategori_produk, instance.nama_produk, ext)
        return os.path.join('foto', filename)   
        
    foto_produk = models.FileField(upload_to= content_file_name ,null = True, blank = True)


    def __str__(self):
        return self.nama_produk

class Keranjang_pembelian(models.Model):
    id_keranjang = models.AutoField(primary_key = True)
    id_pelanggan = models.ForeignKey (
        Pelanggan,
        null = False,
        related_name='keranjang_pelanggan',
        on_delete=models.CASCADE
    )
    id_produk = models.ForeignKey(
        Produk,
        null = False,
        related_name ='produk',
        on_delete=models.CASCADE
    )

class Rating (models.Model):
    id_rating = models.AutoField(primary_key=True)
    id_produk = models.ForeignKey(
        Produk,
        on_delete=models.CASCADE
    )
    id_pelanggan = models.ForeignKey(
        Pelanggan,
        on_delete=models.CASCADE
    )
    rating_pelanggan = models.FloatField(max_length= 250)

class Prediksi (models.Model):
    id_prediksi = models.AutoField(primary_key=True)
    id_rating = models.ForeignKey(
        Rating,
        on_delete=models.CASCADE
    )
    hasil_prediksi = models.FloatField(max_length= 250)

class Rekomendasi (models.Model):
    id_rekomendasi = models.AutoField(primary_key= True)
    id_pelanggan = models.ForeignKey(
        Pelanggan,
        on_delete= models.CASCADE
    )
    id_prediksi = models.ForeignKey(
        Prediksi,
        on_delete=models.CASCADE
    )
    id_detail_rekomendasi = models.FloatField(max_length= 250)


@receiver(post_save, sender=User)
def create_or_update_user_pelanggan(sender, instance, created, **kwargs):
    if created:
        Pelanggan.objects.create(pelanggan=instance)
    instance.pelanggan.save()
