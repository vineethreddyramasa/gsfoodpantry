from django.contrib import admin
from .models import Volunteer, Inventory, Client, Donation, Visit, Donor

class VolunteerList(admin.ModelAdmin):
    list_display = ('vol_number', 'fname', 'city', 'cell_phone')
    list_filter = ('vol_number', 'fname', 'city')
    search_fields = ('vol_number', 'fname')
    ordering = ['vol_number']

class InventoryList(admin.ModelAdmin):
    list_display = ('item_code', 'item_name')
    list_filter = ('item_code', 'item_name')
    search_fields = ('item_code', 'item_name')
    ordering = ['item_code']

class ClientList(admin.ModelAdmin):
    list_display = ('client_ID', 'fname', 'age', 'mobile')
    list_filter = ('client_ID', 'fname', 'age')
    search_fields = ('client_ID', 'fname')
    ordering = ['client_ID']

class DonationList(admin.ModelAdmin):
    list_display = ('item',  'donor', 'quantity')
    list_filter = ('item', 'donor')
    search_fields = ('item', 'donor')
    ordering = ['item']

class VisitList(admin.ModelAdmin):
    list_display = ('name','item','item_quantity')
    list_filter = ('name','item')
    search_fields = ('name','item')
    ordering = ['name']
class DonorList(admin.ModelAdmin):
    list_display = ('donor_name','notes')
    list_filter = ('donor_name','notes')
    search_fields = ('donor_name','notes')
    ordering = ['donor_name']


admin.site.register(Volunteer, VolunteerList)
admin.site.register(Inventory, InventoryList)
admin.site.register(Client, ClientList)
admin.site.register(Donation, DonationList)
admin.site.register(Visit, VisitList)
admin.site.register(Donor, DonorList)

