from datetime import datetime, time
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Musteri(models.Model):
    firma_adi = models.CharField(max_length=255, unique=True)
    telefon = models.CharField(max_length=100, blank=True, null=True)
    telefon2 = models.CharField(max_length=100, blank=True, null=True)
    gsm_no = models.CharField(max_length=50, blank=True, null=True)
    faks = models.CharField(max_length=50, blank=True, null=True)
    yetkili = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    adres = models.TextField(blank=True, null=True)
    notlar = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.firma_adi

    class Meta:
        verbose_name = "Müşteri"
        verbose_name_plural = "Müşteriler"
        ordering = ('firma_adi',)


class BakimAnlasmaTip(models.Model):
    adi = models.CharField(max_length=100, unique=True)
    devir = models.BooleanField()
    uzak_baglanti = models.BooleanField()
    telefon_Destek = models.BooleanField()
    yerinde_servis = models.BooleanField()
    install = models.BooleanField()
    versiyon_gecis = models.BooleanField()
    egitim_destek = models.BooleanField()
    bulut_yedekleme = models.BooleanField()
    rapor_destek = models.BooleanField()
    fiyat = models.DecimalField(decimal_places=2, max_digits=10)
    para_birimi = models.CharField(max_length=2, choices=settings.PARA_BIRIMI)

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Bakım Anlaşma Tipi"
        verbose_name_plural = "Bakım Anlaşma Tipleri"
        ordering =('fiyat',)


class BakimAnlasma(models.Model):
    musteri = models.ForeignKey(Musteri)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    anlasma_tip = models.ForeignKey(BakimAnlasmaTip, related_name="anlasma")
    notlar = models.TextField(blank=True)
    anlasilan_fiyat = models.DecimalField(decimal_places=2, max_digits=10)
    para_birimi = models.CharField(max_length=2, choices=settings.PARA_BIRIMI)
    odendi = models.BooleanField()

    def __str__(self):
        return ": %s | %s | Bitiş:%s" %(self.musteri.firma_adi, self.anlasma_tip.adi, self.bitis_tarihi)

    class Meta:
        verbose_name = "Bakım Anlaşması"
        verbose_name_plural = "Bakım Anlaşmaları"
        ordering = ('musteri','bitis_tarihi',)


class ServisTip(models.Model):
    adi = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Servis Tipi"
        verbose_name_plural = "Servis Tipleri"


class ServisIcerik(models.Model):
    adi = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Servis İçerik"
        verbose_name_plural = "Servis İçerikleri"


class ServisSekli(models.Model):
    adi = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Servis Şekli"
        verbose_name_plural = "Servis Şekilleri"


class ServisForm(models.Model):
    musteri = models.ForeignKey(Musteri, related_name="Servisler")
    belge_no = models.CharField(max_length=10, blank=True)
    servis_tip = models.ForeignKey(ServisTip)
    servis_icerik = models.ForeignKey(ServisIcerik)
    servis_sekli = models.ForeignKey(ServisSekli)
    baslangic_tarihi = models.DateTimeField(default=datetime.now)
    bitis_tarihi = models.DateTimeField()
    yapilan_islemler = models.TextField()
    notlar = models.TextField(blank=True)
    servis_sorumlusu = models.ForeignKey(User)
    musteri_adi = models.CharField(max_length=100)
    bakim_anlasmasi = models.ForeignKey(BakimAnlasma, blank=True, null=True)
    servis_ucreti = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    para_birimi = models.CharField(max_length=2, choices=settings.PARA_BIRIMI, blank=True)
    tahsil_edildi = models.BooleanField(default=False)


    def __str__(self):
        return ": %s | %s | %s" %(self.musteri.firma_adi, self.baslangic_tarihi.strftime('%Y-%m-%d'), self.servis_sorumlusu)

    class Meta:
        verbose_name = "Servis Formu"
        verbose_name_plural = "Servis Formları"
        ordering = ('-baslangic_tarihi', 'musteri')


class HostingTip(models.Model):
    adi = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Hosting tipi"
        verbose_name_plural ="Hosting Tipleri"


class Hosting(models.Model):
    musteri = models.ForeignKey(Musteri, related_name="Hostingler")
    aciklama = models.CharField(max_length=200)
    hosting_tipi = models.ForeignKey(HostingTip)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    ucret = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    para_birimi = models.CharField(max_length=2, choices=settings.PARA_BIRIMI,)
    odendi = models.BooleanField(default=False)

    def __str__(self):
        return self.aciklama

    class Meta:
        verbose_name = "Hosting"
        verbose_name_plural = "Hostingler"
        ordering = ('bitis_tarihi','musteri')


class CihazMarka(models.Model):
    adi = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Cihaz Markası"
        verbose_name_plural = "Cihaz Markaları"
        ordering = ('adi',)


class CihazModel(models.Model):
    marka = models.ForeignKey(CihazMarka)
    model = models.CharField(max_length=255)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "Cihaz Modeli"
        verbose_name_plural = "Cihaz Modelleri"
        ordering = ('marka','model')


class CihazTip(models.Model):
    adi = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Cihaz Tipi"
        verbose_name_plural = "Cihaz Tipleri"
        ordering =('adi',)


class Cihaz(models.Model):
    marka = models.ForeignKey(CihazMarka)
    model = models.ForeignKey(CihazModel)
    tip = models.ForeignKey(CihazTip)
    seri_no = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.seri_no

    class Meta:
        verbose_name = "Cihaz"
        verbose_name_plural = "Cihazlar"
        ordering = ('marka','model','tip', 'seri_no')


class CihazForm(models.Model):
    musteri = models.ForeignKey(Musteri)
    belge_no = models.CharField(max_length=10, unique=True)
    teslim_alan = models.ForeignKey(User)
    cihaz = models.ForeignKey(Cihaz)
    verilis_tarihi = models.DateField()
    ariza = models.TextField()
    teslim_tarihi = models.DateField(blank=True, null=True)
    yapilan_islemler = models.TextField(blank=True)
    garanti_dahili = models.BooleanField()
    ucret = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return self.cihaz.seri_no

    class Meta:
        verbose_name = "Cihaz Formu"
        verbose_name_plural = "Cihaz Formları"
        ordering = ('verilis_tarihi', 'musteri',)


class Paket(models.Model):
    adi = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.adi

    class Meta:
        verbose_name = "Paket"
        verbose_name_plural = "Paketler"
        ordering = ('adi',)


class Lisans(models.Model):
    musteri = models.ForeignKey(Musteri)
    paket = models.ForeignKey(Paket)
    lisans_no = models.CharField(max_length=6, unique=True)
    kullanici_sayisi = models.IntegerField()
    aciklama =models.TextField(blank=True, null=True)
    tarih = models.DateField()

    def __str__(self):
        return ": %s | %s | %s | %s" %(self.lisans_no, self.tarih, self.paket, self.aciklama)

    class Meta:
        verbose_name = "Lisans"
        verbose_name_plural = "Lisanslar"
        ordering = ('musteri','tarih', "lisans_no", )

