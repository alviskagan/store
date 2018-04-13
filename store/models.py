import uuid, os, time

from django.db import models
from djmoney.models.fields import MoneyField
from django.utils.deconstruct import deconstructible
import locale

# Create your models here.
class Pelanggan(models.Model):
    id_pelanggan = models.AutoField(primary_key = True)
    username_pelanggan = models.CharField(max_length = 250)
    password_pelanggan = models.CharField(max_length = 250)
    nama_pelanggan = models.CharField(max_length = 250, default = "Alviska Galuh")
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    alamat_pelanggan = models.CharField(max_length = 250, default = "Yogyakarta")
    no_hp = models.IntegerField(default="082")
'''
    def save(self, *args, **kwargs):
        # ... other things not important here
        self.email = self.email.lower().strip() # Hopefully reduces junk to ""
        if self.email != "": # If it's not blank
            if not email_re.match(self.email) # If it's not an email address
                raise ValidationError(u'%s is not an email address, dummy!' % self.email)
        if self.email == "":
            self.email = None
        super(Pelanggan, self.email).save(*args, **kwargs)

    def __str__(self):
         return self.nama_pelanggan
    # class Meta:
    #     ordering = ('id_keranjang',)
'''
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
    #harga_produk = MoneyField(max_digits=10, decimal_places = 2, default_currency='IDR')
    harga_produk = models.IntegerField()
    rating_produk = models.IntegerField() 

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
        related_name='pelanggan',
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

