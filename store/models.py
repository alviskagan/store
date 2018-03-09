from django.db import models

# Create your models here.
class pelanggan(models.Model):
    id_pelanggan = models.AutoField(primary_key = True)
    username_pelanggan = models.CharField(max_length = 250)
    password_pelanggan = models.CharField(max_length = 250)

class produk(models.Model):
    id_produk = models.AutoField(primary_key = True)
    nama_produk = models.CharField(max_length = 250)
    kategori_produk = models.CharField(max_length = 250)
    stok_produk = models.IntegerField(250)
    harga_produk = models.IntegerField(250)
    rating_produk = models.IntegerField(250)


class keranjang_pembelian(models.Model):
    id_keranjang = models.AutoField(primary_key = True)
    id_pelanggan = models.ForeignKey (
        pelanggan,
        null = True,
        related_name='id_pelanggan',
        on_delete=models.CASCADE
    )
    id_produk = models.ForeignKey(
        produk,
        null = True,
        related_name ='id_produk',
        on_delete=models.CASCADE
    )


    # def __str__(self):
    #     return self.id_keranjang
    # class Meta:
    #     ordering = ('id_keranjang',)

class rating (models.Model):
    id_rating = models.AutoField(primary_key=True)
    id_produk = models.ForeignKey(
        produk,
        on_delete=models.CASCADE
    )
    id_pelanggan = models.ForeignKey(
        pelanggan,
        on_delete=models.CASCADE
    )
    rating_pelanggan = models.FloatField(max_length= 250)

class prediksi (models.Model):
    id_prediksi = models.AutoField(primary_key=True)
    id_rating = models.ForeignKey(
        rating,
        on_delete=models.CASCADE
    )
    hasil_prediksi = models.FloatField(max_length= 250)

class detail_rekomendasi (models.Model):
    id_detail_rekomendasi = models.AutoField(primary_key= True)
    hasil_rekomendasi = models.FloatField(max_length= 250)

class rekomendasi (models.Model):
    id_rekomendasi = models.AutoField(primary_key= True)
    id_pelanggan = models.ForeignKey(
        pelanggan,
        on_delete= models.CASCADE
    )
    id_prediksi = models.ForeignKey(
        prediksi,
        on_delete=models.CASCADE
    )
    id_detail_rekomendasi = models.FloatField(max_length= 250)

class kategori (models.Model):
    id_kategori = models.AutoField(primary_key= True)
    id_produk = models.ForeignKey(
        produk,
        on_delete= models.CASCADE
    )
    kategori = models.CharField(max_length= 250)
