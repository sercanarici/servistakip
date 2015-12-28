from django.shortcuts import render, redirect
from app.models import *


def index(request):
    #return render(request, "index.html", locals())
    return redirect('/admin/')


def anlasmalar(request):
    content = BakimAnlasma.objects.all()
    return render(request, "anlasmalar.html", locals())


def musteriler(request):
    #content = Musteri.objects.all()
    return render(request, "musteriler.html", locals())


def servisler(request):
    content = ServisForm.objects.all()
    return render(request, "servisler.html", locals())


def cihazservisler(request):
    content = CihazForm.objects.all()
    return render(request, "cihazservisler.html", locals())


def hostingler(request):
    content = Hosting.objects.all()
    return render(request, "hosting.html", locals())


def musteri_detay(request, musteri_id):
    musteri = Musteri.objects.get(pk=musteri_id)
    musteri_servisler = ServisForm.objects.filter(musteri__pk=musteri_id)
    musteri_anlasmalar = BakimAnlasma.objects.filter(musteri__id=musteri_id)
    musteri_cihazlar = CihazForm.objects.filter(musteri__id=musteri_id)
    musteri_hostingler = Hosting.objects.filter(musteri__id=musteri_id)
    return render(request, "musteri_detay.html", locals())





