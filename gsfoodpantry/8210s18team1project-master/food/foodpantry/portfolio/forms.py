from django import forms
from .models import Volunteer, Inventory, Client, Donation, Visit, Donor

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ('vol_number', 'lname', 'fname','vol_dob', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone','vol_notes')


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('item_code', 'item_name', 'created_date',)

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_ID', 'fname', 'lname','age', 'client_dob', 'gender', 'mobile', 'address')

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('item', 'donor', 'quantity', 'received_date',)

class VisitForm(forms.ModelForm):
    class Meta:
        model= Visit
        fields = ('name','item','item_quantity','visit_date',)

class DonorForm(forms.ModelForm):
    class Meta:
        model= Donor
        fields = ('donor_name','notes','join_date','email')