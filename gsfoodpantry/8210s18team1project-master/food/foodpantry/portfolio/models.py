from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Volunteer(models.Model):
    vol_number = models.IntegerField(unique=True,blank=False, null=False)
    lname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    vol_dob = models.DateTimeField(
        default=timezone.now)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    vol_notes = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)


    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.vol_number)


class Inventory(models.Model):
    item_code = models.IntegerField(unique=True,blank=False, null=False)
    item_name = models.CharField(unique=True,max_length=50)

    created_date = models.DateField(default=timezone.now)

    class Meta:
        unique_together= ('item_code','item_name')

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.item_name)

class Client(models.Model):
    client_ID = models.IntegerField(unique=True,blank=False, null=False)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField(blank=False, null=False)
    client_dob = models.DateField(
        default=timezone.now)
    gender = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    created_date = models.DateField(
        default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.fname)


class Visit(models.Model):
    name = models.ForeignKey(Client,related_name='visits')
    item= models.ForeignKey(Inventory,related_name='items')
    item_quantity= models.DecimalField(max_digits=10,decimal_places=1)
    visit_date=models.DateField(default=timezone.now)

    def created(self):
        self.visit_date=timezone.now()
        self.save()

    def __str__(self):
        return str(self.name)

class Donor(models.Model):
    donor_name= models.CharField(max_length=50)
    notes= models.CharField(max_length=50)
    join_date=models.DateField(default=timezone.now)
    email=models.EmailField(max_length=200)

    def created(self):
        self.join_date=timezone.now()
        self.save()

    def __str__(self):
        return str(self.donor_name)


class Donation(models.Model):
    item = models.ForeignKey(Inventory,related_name='donations')
    donor= models.ForeignKey(Donor, related_name='donorname')
    quantity = models.DecimalField(max_digits=10,decimal_places=1)
    received_date=models.DateField(default=timezone.now)

    def created(self):
        self.received_date=timezone.now()
        self.save()

    def __str__(self):
        return str(self.donor)
