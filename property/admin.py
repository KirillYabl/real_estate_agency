from django.contrib import admin

from .models import Flat
from .models import Complaint
from .models import Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    raw_id_fields = ('likes',)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    search_fields = ('flat__town', 'flat__address',)
    raw_id_fields = ('user', 'flat',)


@admin.register(Owner)
class ComplaintAdmin(admin.ModelAdmin):
    search_fields = ('flats__town', 'flats__address', 'owner', 'owner_phone_pure',)
    raw_id_fields = ('flats',)
