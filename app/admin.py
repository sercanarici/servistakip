from django.contrib import admin
from django.db.models import Count
from app.models import *

@admin.register(BakimAnlasmaTip)
class BakımAnlasmaTipAdmin(admin.ModelAdmin):
    list_display = ("adi", "fiyat")


@admin.register(BakimAnlasma)
class BakimAnlasmaAdmin(admin.ModelAdmin):
    list_display = ("musteri", "anlasma_tip", "baslangic_tarihi", "bitis_tarihi", "anlasilan_fiyat", "odendi")
    search_fields = ("musteri__firma_adi",)
    list_filter = ("anlasma_tip",)
    raw_id_fields = ("musteri",)


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
    list_display = ("firma_adi", "telefon", "yetkili" ,"adres","servis_sayisi", "bayi",)
    search_fields = ("firma_adi",)
    list_filter = ("firma_adi", "bayi",)
    inlines = [
        AnlasmaInline,
        ServisFormInline,
        LisansInline
    ]

    def get_queryset(self, request):
        return Musteri.objects.annotate(servis_count = Count('servisler'))

    def servis_sayisi(self, obj):
        return obj.servis_count
    servis_sayisi.admin_order_field = 'servis_count'


@admin.register(ServisForm)
class ServisFormAdmin(admin.ModelAdmin):
    list_display = ("musteri", "baslangic_tarihi", "servis_sorumlusu", "belge_no", "bayi",)
    raw_id_fields = ("musteri",)
    search_fields = ("musteri__firma_adi",)
    list_filter = ("servis_sorumlusu", "musteri__bayi",)

    def bayi(self,obj):
        return obj.musteri.bayi.bayi_adi
    bayi.admin_short_description = "Bayi Adı"
    bayi.admin_order_field = "bayi_adi"


class HostingAdmin(admin.ModelAdmin):
    list_display = ("musteri", "hosting_tipi", "baslangic_tarihi", "bitis_tarihi")
    raw_id_fields = ("musteri",)


@admin.register(Lisans)
class LisansAdmin(admin.ModelAdmin):
    list_display = ("musteri","paket", "lisans_no","tarih","aciklama",)
    search_fields = ("musteri__firma_adi",)
    list_filter = ("musteri",)


@admin.register(CihazModel)
class CihazModelAdmin(admin.ModelAdmin):
    list_display = ("model", "marka",)
    search_fields = ("marka", "model",)
    list_filter = ("marka",)


@admin.register(Cihaz)
class CihazAdmin(admin.ModelAdmin):
    list_display = ("marka", "model","tip","seri_no")
    search_fields = ("marka", "model",)
    list_filter = ("marka","model","tip",)


@admin.register(CihazMarka)
class CihazMarkaAdmin(admin.ModelAdmin):
    search_fields = ("adi",)


@admin.register(CihazTip)
class CihazTipAdmin(admin.ModelAdmin):
    search_fields = ("adi",)


@admin.register(CihazForm)
class CihazFormAdmin(admin.ModelAdmin):
    list_display = ("musteri" , "teslim_alan", "verilis_tarihi", "teslim_tarihi",)
    list_filter = ("musteri", "cihaz__marka", "teslim_alan__username", "teslim_tarihi",)
    search_fields = ("musteri",)
    raw_id_fields = ("musteri", "cihaz",)


@admin.register(Hosting)
class HostingAdmin(admin.ModelAdmin):
    raw_id_fields = ("musteri",)
    list_display = ("musteri", "hosting_tipi", "bitis_tarihi", "odendi",)



admin.site.register(ServisTip)
admin.site.register(ServisIcerik)
admin.site.register(ServisSekli)
admin.site.register(HostingTip)
admin.site.register(Paket)
admin.site.register(Bayi)

