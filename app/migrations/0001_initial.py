# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BakimAnlasma',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('baslangic_tarihi', models.DateField()),
                ('bitis_tarihi', models.DateField()),
                ('notlar', models.TextField(blank=True)),
                ('anlasilan_fiyat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('para_birimi', models.CharField(max_length=2, choices=[('TL', 'Türk Lirası'), ('$', 'US Dolar')])),
                ('odendi', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Bakım Anlaşmaları',
                'verbose_name': 'Bakım Anlaşması',
                'ordering': ('musteri', 'bitis_tarihi'),
            },
        ),
        migrations.CreateModel(
            name='BakimAnlasmaTip',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('adi', models.CharField(max_length=100, unique=True)),
                ('devir', models.BooleanField()),
                ('uzak_baglanti', models.BooleanField()),
                ('telefon_Destek', models.BooleanField()),
                ('yerinde_servis', models.BooleanField()),
                ('install', models.BooleanField()),
                ('versiyon_gecis', models.BooleanField()),
                ('egitim_destek', models.BooleanField()),
                ('bulut_yedekleme', models.BooleanField()),
                ('rapor_destek', models.BooleanField()),
                ('fiyat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('para_birimi', models.CharField(max_length=2, choices=[('TL', 'Türk Lirası'), ('$', 'US Dolar')])),
            ],
            options={
                'verbose_name_plural': 'Bakım Anlaşma Tipleri',
                'verbose_name': 'Bakım Anlaşma Tipi',
                'ordering': ('fiyat',),
            },
        ),
        migrations.CreateModel(
            name='Cihaz',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('seri_no', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Cihazlar',
                'verbose_name': 'Cihaz',
                'ordering': ('marka', 'model', 'tip', 'seri_no'),
            },
        ),
        migrations.CreateModel(
            name='CihazForm',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('belge_no', models.CharField(max_length=10, unique=True)),
                ('verilis_tarihi', models.DateField()),
                ('ariza', models.TextField()),
                ('teslim_tarihi', models.DateField(blank=True, null=True)),
                ('yapilan_islemler', models.TextField(blank=True)),
                ('garanti_dahili', models.BooleanField()),
                ('ucret', models.DecimalField(default=0, decimal_places=2, max_digits=10)),
                ('cihaz', models.ForeignKey(to='app.Cihaz')),
            ],
            options={
                'verbose_name_plural': 'Cihaz Formları',
                'verbose_name': 'Cihaz Formu',
                'ordering': ('verilis_tarihi', 'musteri'),
            },
        ),
        migrations.CreateModel(
            name='CihazMarka',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('adi', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Cihaz Markaları',
                'verbose_name': 'Cihaz Markası',
                'ordering': ('adi',),
            },
        ),
        migrations.CreateModel(
            name='CihazModel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('model', models.CharField(max_length=255)),
                ('marka', models.ForeignKey(to='app.CihazMarka')),
            ],
            options={
                'verbose_name_plural': 'Cihaz Modelleri',
                'verbose_name': 'Cihaz Modeli',
                'ordering': ('marka', 'model'),
            },
        ),
        migrations.CreateModel(
            name='CihazTip',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('adi', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Cihaz Tipleri',
                'verbose_name': 'Cihaz Tipi',
                'ordering': ('adi',),
            },
        ),
        migrations.CreateModel(
            name='Hosting',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('aciklama', models.CharField(max_length=200)),
                ('baslangic_tarihi', models.DateField()),
                ('bitis_tarihi', models.DateField()),
                ('ucret', models.DecimalField(default=0, decimal_places=2, max_digits=10)),
                ('para_birimi', models.CharField(max_length=2, choices=[('TL', 'Türk Lirası'), ('$', 'US Dolar')])),
                ('odendi', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Hostingler',
                'verbose_name': 'Hosting',
                'ordering': ('bitis_tarihi', 'musteri'),
            },
        ),
        migrations.CreateModel(
            name='HostingTip',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('adi', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Hosting Tipleri',
                'verbose_name': 'Hosting tipi',
            },
        ),
        migrations.CreateModel(
            name='Lisans',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('lisans_no', models.CharField(max_length=6, unique=True)),
                ('kullanici_sayisi', models.IntegerField()),
                ('aciklama', models.TextField(blank=True, null=True)),
                ('tarih', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Lisanslar',
                'verbose_name': 'Lisans',
                'ordering': ('musteri', 'tarih', 'lisans_no'),
            },
        ),
        migrations.CreateModel(
            name='Musteri',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('firma_adi', models.CharField(max_length=255, unique=True)),
                ('telefon', models.CharField(max_length=100, null=True, blank=True)),
                ('telefon2', models.CharField(max_length=100, null=True, blank=True)),
                ('gsm_no', models.CharField(max_length=50, null=True, blank=True)),
                ('faks', models.CharField(max_length=50, null=True, blank=True)),
                ('yetkili', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('adres', models.TextField(blank=True, null=True)),
                ('notlar', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Müşteriler',
                'verbose_name': 'Müşteri',
                'ordering': ('firma_adi',),
            },
        ),
        migrations.CreateModel(
            name='Paket',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('adi', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Paketler',
                'verbose_name': 'Paket',
                'ordering': ('adi',),
            },
        ),
        migrations.CreateModel(
            name='ServisForm',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('belge_no', models.CharField(max_length=10, blank=True)),
                ('baslangic_tarihi', models.DateTimeField(default=datetime.datetime.now)),
                ('bitis_tarihi', models.DateTimeField()),
                ('yapilan_islemler', models.TextField()),
                ('notlar', models.TextField(blank=True)),
                ('musteri_adi', models.CharField(max_length=100)),
                ('servis_ucreti', models.DecimalField(default=0, decimal_places=2, max_digits=10)),
                ('para_birimi', models.CharField(max_length=2, blank=True, choices=[('TL', 'Türk Lirası'), ('$', 'US Dolar')])),
                ('tahsil_edildi', models.BooleanField(default=False)),
                ('bakim_anlasmasi', models.ForeignKey(blank=True, null=True, to='app.BakimAnlasma')),
                ('musteri', models.ForeignKey(related_name='servisler', to='app.Musteri')),
            ],
            options={
                'verbose_name_plural': 'Servis Formları',
                'verbose_name': 'Servis Formu',
                'ordering': ('-baslangic_tarihi', 'musteri'),
            },
        ),
        migrations.CreateModel(
            name='ServisIcerik',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('adi', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Servis İçerikleri',
                'verbose_name': 'Servis İçerik',
            },
        ),
        migrations.CreateModel(
            name='ServisSekli',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('adi', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Servis Şekilleri',
                'verbose_name': 'Servis Şekli',
            },
        ),
        migrations.CreateModel(
            name='ServisTip',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('adi', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Servis Tipleri',
                'verbose_name': 'Servis Tipi',
            },
        ),
        migrations.AddField(
            model_name='servisform',
            name='servis_icerik',
            field=models.ForeignKey(to='app.ServisIcerik'),
        ),
        migrations.AddField(
            model_name='servisform',
            name='servis_sekli',
            field=models.ForeignKey(to='app.ServisSekli'),
        ),
        migrations.AddField(
            model_name='servisform',
            name='servis_sorumlusu',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='servisform',
            name='servis_tip',
            field=models.ForeignKey(to='app.ServisTip'),
        ),
        migrations.AddField(
            model_name='lisans',
            name='musteri',
            field=models.ForeignKey(to='app.Musteri'),
        ),
        migrations.AddField(
            model_name='lisans',
            name='paket',
            field=models.ForeignKey(to='app.Paket'),
        ),
        migrations.AddField(
            model_name='hosting',
            name='hosting_tipi',
            field=models.ForeignKey(to='app.HostingTip'),
        ),
        migrations.AddField(
            model_name='hosting',
            name='musteri',
            field=models.ForeignKey(related_name='Hostingler', to='app.Musteri'),
        ),
        migrations.AddField(
            model_name='cihazform',
            name='musteri',
            field=models.ForeignKey(to='app.Musteri'),
        ),
        migrations.AddField(
            model_name='cihazform',
            name='teslim_alan',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cihaz',
            name='marka',
            field=models.ForeignKey(to='app.CihazMarka'),
        ),
        migrations.AddField(
            model_name='cihaz',
            name='model',
            field=models.ForeignKey(to='app.CihazModel'),
        ),
        migrations.AddField(
            model_name='cihaz',
            name='tip',
            field=models.ForeignKey(to='app.CihazTip'),
        ),
        migrations.AddField(
            model_name='bakimanlasma',
            name='anlasma_tip',
            field=models.ForeignKey(related_name='anlasma', to='app.BakimAnlasmaTip'),
        ),
        migrations.AddField(
            model_name='bakimanlasma',
            name='musteri',
            field=models.ForeignKey(to='app.Musteri'),
        ),
    ]
