from django.contrib import admin
from.models import *
# Register your models here.


class HotelsAdmin(admin.ModelAdmin):
    fields = ('name_hotel', 'price_hotel')
    list_filter = ('name_hotel', 'price_hotel')
    list_display = ('name_hotel', 'price_hotel')
    search_fields = ('name_hotel', 'price_hotel')
    list_per_page = 10


class CountrysAdmin(admin.ModelAdmin):
    fields = ('cnt_name', 'hotel_name')
    list_filter = ('cnt_name', 'hotel_name')
    list_display = ('cnt_name', 'hotel_name')
    search_fields = ('cnt_name', 'hotel_name')
    list_per_page = 10


admin.site.register(Hotel, HotelsAdmin)
admin.site.register(Country, CountrysAdmin)