from django.contrib import admin
from app.models import *

@admin.register(BakimAnlasmaTip)
class BakımAnlasmaTipAdmin(admin.ModelAdmin):
    list_display = ("adi", "fiyat")


@admin.register(BakimAnlasma)
class BakimAnlasmaAdmin(admin.ModelAdmin):
    list_display = ("musteri", "anlasma_tip", "baslangic_tarihi", "bitis_tarihi", "anlasilan_fiyat", "odendi")
    search_fields = ("musteri__firma_adi",)
    list_filter = ("anlasma_tip",)


class AnlasmaInline(admin.StackedInline):
    model = BakimAnlasma
    extra = 0
    classes = ('grp-collapse grp-open',)


class ServisFormInline(admin.StackedInline):
    model = ServisForm
    extra = 0
    classes = ('grp-collapse grp-open',)


class LisansInline(admin.StackedInline):
    model = Lisans
    extra = 0
    classes = ('grp-collapse grp-open',)


@admin.register(Musteri)
class MusteriAdmin(admin.ModelAdmin):
    list_display = ("firma_adi", "telefon", "yetkili" ,"adres",)
    search_fields = ("firma_adi",)
    list_filter = ("firma_adi",)
    inlines = [
        AnlasmaInline,
        ServisFormInline,
        LisansInline
    ]


@admin.register(ServisForm)
class ServisFormAdmin(admin.ModelAdmin):
    list_display = ("musteri", "baslangic_tarihi", "servis_sorumlusu")


class HostingAdmin(admin.ModelAdmin):
    list_display = ("musteri", "hosting_tipi", "baslangic_tarihi", "bitis_tarihi")

@admin.register(Lisans)
class LisansAdmin(admin.ModelAdmin):
    list_display = ("musteri","paket", "lisans_no","tarih","aciklama",)
    search_fields = ("musteri__firma_adi",)
    list_filter = ("musteri",)


admin.site.register(ServisTip)
admin.site.register(ServisIcerik)
admin.site.register(ServisSekli)
admin.site.register(HostingTip)
admin.site.register(Hosting)
admin.site.register(CihazMarka)
admin.site.register(CihazTip)
admin.site.register(CihazModel)
admin.site.register(Cihaz)
admin.site.register(CihazForm)
admin.site.register(Paket)

