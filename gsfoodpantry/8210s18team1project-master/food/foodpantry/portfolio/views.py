from io import StringIO
from django.http import HttpResponse
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Sum, Value as V
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.functions import Coalesce
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .utils import render_to_pdf
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return render(request, 'registration/password_reset_complete.html', {'portfolio': password_reset_complete})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

def password_reset(request):
    return render(request, 'registration/password_reset_form.html',
    {'portfolio': password_reset})


def password_reset_confirm(request):
    return render(request, 'registration/password_reset_confirm.html',
    {'portfolio': password_reset_confirm})

def password_reset_email(request):
    return render(request, 'registration/password_reset_email.html',
    {'portfolio': password_reset_email})

def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html',
    {'portfolio': password_reset_complete})


def abc(request):
    return render(request, 'portfolio/abc.html')

@login_required
def home(request):
   return render(request, 'portfolio/home.html',
                 {'home':home})

@staff_member_required
def home2(request):
   return render(request, 'portfolio/home2.html',
                 {'home2':home2})


@staff_member_required
def volunteer_list(request):
   volunteer = Volunteer.objects.filter(created_date__lte=timezone.now())
   return render(request, 'portfolio/volunteer_list.html',
                 {'volunteers': volunteer})

@login_required
def volunteer_new(request):
   if request.method == "POST":
       form = VolunteerForm(request.POST)
       if form.is_valid():
           volunteer = form.save(commit=False)
           volunteer.created_date = timezone.now()
           volunteer.save()
           volunteers = Volunteer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/volunteer_list.html',
                         {'volunteers': volunteers})
   else:
       form = VolunteerForm()
       # print("Else")
   return render(request, 'portfolio/volunteer_new.html', {'form': form})

@login_required
def volunteer_edit(request, pk):
   volunteer = get_object_or_404(Volunteer, pk=pk)
   if request.method == "POST":
       # update
       form = VolunteerForm(request.POST, instance=volunteer)
       if form.is_valid():
           volunteer = form.save(commit=False)
           volunteer.updated_date = timezone.now()
           volunteer.save()
           volunteer = Volunteer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/volunteer_list.html',
                         {'volunteers': volunteer})
   else:
       # edit
       form = VolunteerForm(instance=volunteer)
   return render(request, 'portfolio/volunteer_edit.html', {'form': form})


@login_required
def volunteer_delete(request, pk):
   volunteer = get_object_or_404(Volunteer, pk=pk)
   volunteer.delete()
   return redirect('portfolio:volunteer_list')



@login_required
def inventory_list(request):
   inventorys = Inventory.objects.filter(created_date__lte=timezone.now())
   return render(request, 'portfolio/inventory_list.html', {'inventorys': inventorys})

@staff_member_required
def inventory_list2(request):
   inventorys = Inventory.objects.filter(created_date__lte=timezone.now())
   return render(request, 'portfolio/inventory_list2.html', {'inventorys': inventorys})


@login_required
def inventory_new(request):
   if request.method == "POST":
       form = InventoryForm(request.POST)
       if form.is_valid():
           inventory = form.save(commit=False)
           inventory.created_date = timezone.now()
           inventory.save()
           inventorys = Inventory.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/inventory_list.html',
                         {'inventorys': inventorys})
   else:
       form = InventoryForm()
       # print("Else")
   return render(request, 'portfolio/inventory_new.html', {'form': form})

@staff_member_required()
def inventory_new2(request):
   if request.method == "POST":
       form = InventoryForm(request.POST)
       if form.is_valid():
           inventory = form.save(commit=False)
           inventory.created_date = timezone.now()
           inventory.save()
           inventorys = Inventory.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/inventory_list2.html',
                         {'inventorys': inventorys})
   else:
       form = InventoryForm()
       # print("Else")
   return render(request, 'portfolio/inventory_new2.html', {'form': form})


@login_required
def inventory_edit(request, pk):
   inventory = get_object_or_404(Inventory, pk=pk)
   if request.method == "POST":
       form = InventoryForm(request.POST, instance=inventory)
       if form.is_valid():
           inventory = form.save()
           inventory.updated_date = timezone.now()
           inventory.save()
           inventorys = Inventory.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/inventory_list.html', {'inventorys': inventorys})
   else:
       # print("else")
       form = InventoryForm(instance=inventory)
   return render(request, 'portfolio/inventory_edit.html', {'form': form})

@staff_member_required
def inventory_edit2(request, pk):
   inventory = get_object_or_404(Inventory, pk=pk)
   if request.method == "POST":
       form = InventoryForm(request.POST, instance=inventory)
       if form.is_valid():
           inventory = form.save()
           inventory.updated_date = timezone.now()
           inventory.save()
           inventorys = Inventory.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/inventory_list2.html', {'inventorys': inventorys})
   else:
       # print("else")
       form = InventoryForm(instance=inventory)
   return render(request, 'portfolio/inventory_edit2.html', {'form': form})


@login_required
def inventory_delete(request, pk):
   inventory = get_object_or_404(Inventory, pk=pk)
   inventory.delete()
   inventorys = Inventory.objects.filter(created_date__lte=timezone.now())
   return render(request, 'portfolio/inventory_list.html', {'inventorys': inventorys})

@staff_member_required
def inventory_delete2(request, pk):
   inventory = get_object_or_404(Inventory, pk=pk)
   inventory.delete()
   inventorys = Inventory.objects.filter(created_date__lte=timezone.now())
   return render(request, 'portfolio/inventory_list2.html', {'inventorys': inventorys})

@login_required
def client_list(request):
    client_ID = request.GET.get ('client_ID')
    lname = request.GET.get ('lname')
    clients = Client.objects.filter (created_date__lte=timezone.now ())

    if client_ID:
        clients = clients.filter (client_ID=client_ID)
    if lname:
        clients = clients.filter (lname__contains=lname)

    return render (request, 'portfolio/client_list.html', {'clients': clients})

@login_required
def client_search(request):
    return render(request, 'portfolio/client_search.html')


@login_required
def client_list2(request):
    client_ID = request.GET.get ('client_ID')
    lname = request.GET.get ('lname')
    clients = Client.objects.filter (created_date__lte=timezone.now ())
    if client_ID:
        clients = clients.filter (client_ID=client_ID)


    if lname:
        clients = clients.filter (lname__contains=lname)

    return render (request, 'portfolio/client_list2.html', {'clients': clients})



@login_required
def client_search2(request):
    return render(request, 'portfolio/client_search2.html')



@login_required
def client_new(request):
   if request.method == "POST":
       form = ClientForm(request.POST)
       if form.is_valid():
           client = form.save(commit=False)
           client.created_date = timezone.now()
           client.save()
           client = Client.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/client_list.html',
                         {'clients': client})
   else:
       form = ClientForm()
       # print("Else")
   return render(request, 'portfolio/client_new.html', {'form': form})

@staff_member_required()
def client_new2(request):
   if request.method == "POST":
       form = ClientForm(request.POST)
       if form.is_valid():
           client = form.save(commit=False)
           client.created_date = timezone.now()
           client.save()
           client = Client.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/client_list2.html',
                         {'clients': client})
   else:
       form = ClientForm()
       # print("Else")
   return render(request, 'portfolio/client_new2.html', {'form': form})

@login_required
def client_edit(request, pk):
   client = get_object_or_404(Client, pk=pk)
   if request.method == "POST":
       # update
       form = ClientForm(request.POST, instance=client)
       if form.is_valid():
           client = form.save(commit=False)
           client.updated_date = timezone.now()
           client.save()
           client = Client.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/client_list.html',
                         {'clients': client})
   else:
       # edit
       form = ClientForm(instance=client)
   return render(request, 'portfolio/client_edit.html', {'form': form})

@staff_member_required
def client_edit2(request, pk):
   client = get_object_or_404(Client, pk=pk)
   if request.method == "POST":
       # update
       form = ClientForm(request.POST, instance=client)
       if form.is_valid():
           client = form.save(commit=False)
           client.updated_date = timezone.now()
           client.save()
           client = Client.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/client_list2.html',
                         {'clients': client})
   else:
       # edit
       form = ClientForm(instance=client)
   return render(request, 'portfolio/client_edit2.html', {'form': form})

@login_required
def client_delete(request, pk):
   client = get_object_or_404(Client, pk=pk)
   client.delete()
   return redirect('portfolio:client_list')

@staff_member_required
def client_delete2(request, pk):
   client = get_object_or_404(Client, pk=pk)
   client.delete()
   return redirect('portfolio:client_list2')


@login_required
def donation_list(request):
   donations = Donation.objects.filter(received_date__lte=timezone.now())
   return render(request, 'portfolio/donation_list.html', {'donations': donations})

@staff_member_required
def donation_list2(request):
   donations = Donation.objects.filter(received_date__lte=timezone.now())
   return render(request, 'portfolio/donation_list2.html', {'donations': donations})


@login_required
def donation_new(request):
   if request.method == "POST":
       form = DonationForm(request.POST)
       if form.is_valid():
           donation = form.save(commit=False)
           donation.created_date = timezone.now()
           donation.save()
           donations = Donation.objects.filter(received_date__lte=timezone.now())
           return render(request, 'portfolio/donation_list.html',
                         {'donations': donations})
   else:
       form = DonationForm()
       # print("Else")
   return render(request, 'portfolio/donation_new.html', {'form': form})

@staff_member_required
def donation_new2(request):
   if request.method == "POST":
       form = DonationForm(request.POST)
       if form.is_valid():
           donation = form.save(commit=False)
           donation.created_date = timezone.now()
           donation.save()
           donations = Donation.objects.filter(received_date__lte=timezone.now())
           return render(request, 'portfolio/donation_list2.html',
                         {'donations': donations})
   else:
       form = DonationForm()
       # print("Else")
   return render(request, 'portfolio/donation_new2.html', {'form': form})


@login_required
def donation_edit(request, pk):
   donation = get_object_or_404(Donation, pk=pk)
   if request.method == "POST":
       form = DonationForm(request.POST, instance=donation)
       if form.is_valid():
           donation = form.save()
           donation.updated_date = timezone.now()
           donation.save()
           donations = Donation.objects.filter(received_date__lte=timezone.now())
           return render(request, 'portfolio/donation_list.html', {'donations': donations})
   else:
       # print("else")
       form = DonationForm(instance=donation)
   return render(request, 'portfolio/donation_edit.html', {'form': form})

@staff_member_required
def donation_edit2(request, pk):
   donation = get_object_or_404(Donation, pk=pk)
   if request.method == "POST":
       form = DonationForm(request.POST, instance=donation)
       if form.is_valid():
           donation = form.save()
           donation.updated_date = timezone.now()
           donation.save()
           donations = Donation.objects.filter(received_date__lte=timezone.now())
           return render(request, 'portfolio/donation_list2.html', {'donations': donations})
   else:
       # print("else")
       form = DonationForm(instance=donation)
   return render(request, 'portfolio/donation_edit2.html', {'form': form})


@login_required
def donation_delete(request, pk):
   donation = get_object_or_404(Donation, pk=pk)
   donation.delete()
   donations = Donation.objects.filter(received_date__lte=timezone.now())
   return render(request, 'portfolio/donation_list.html', {'donations': donations})

@staff_member_required
def donation_delete2(request, pk):
   donation = get_object_or_404(Donation, pk=pk)
   donation.delete()
   donations = Donation.objects.filter(received_date__lte=timezone.now())
   return render(request, 'portfolio/donation_list2.html', {'donations': donations})


@login_required
def visit_list(request):
   visits = Visit.objects.filter(visit_date__lte=timezone.now())
   return render(request, 'portfolio/visit_list.html', {'visits': visits})

@staff_member_required
def visit_list2(request):
   visits = Visit.objects.filter(visit_date__lte=timezone.now())
   return render(request, 'portfolio/visit_list2.html', {'visits': visits})


@login_required
def visit_new(request):
   if request.method == "POST":
       form = VisitForm(request.POST)
       if form.is_valid():
           visit = form.save(commit=False)
           visit.created_date = timezone.now()
           visit.save()
           visits = Visit.objects.filter(visit_date__lte=timezone.now())
           return render(request, 'portfolio/visit_list.html',
                         {'visits': visits})
   else:
       form = VisitForm()
       # print("Else")
   return render(request, 'portfolio/visit_new.html', {'form': form})

@staff_member_required()
def visit_new2(request):
   if request.method == "POST":
       form = VisitForm(request.POST)
       if form.is_valid():
           visit = form.save(commit=False)
           visit.created_date = timezone.now()
           visit.save()
           visits = Visit.objects.filter(visit_date__lte=timezone.now())
           return render(request, 'portfolio/visit_list2.html',
                         {'visits': visits})
   else:
       form = VisitForm()
       # print("Else")
   return render(request, 'portfolio/visit_new2.html', {'form': form})


@login_required
def visit_edit(request, pk):
   visit = get_object_or_404(Visit, pk=pk)
   if request.method == "POST":
       form = VisitForm(request.POST, instance=visit)
       if form.is_valid():
           visit = form.save()
           visit.updated_date = timezone.now()
           visit.save()
           visits = Visit.objects.filter(visit_date__lte=timezone.now())
           return render(request, 'portfolio/visit_list.html', {'visits': visits})
   else:
       # print("else")
       form = VisitForm(instance=visit)
   return render(request, 'portfolio/visit_edit.html', {'form': form})

@staff_member_required
def visit_edit2(request, pk):
   visit = get_object_or_404(Visit, pk=pk)
   if request.method == "POST":
       form = VisitForm(request.POST, instance=visit)
       if form.is_valid():
           visit = form.save()
           visit.updated_date = timezone.now()
           visit.save()
           visits = Visit.objects.filter(visit_date__lte=timezone.now())
           return render(request, 'portfolio/visit_list2.html', {'visits': visits})
   else:
       # print("else")
       form = VisitForm(instance=visit)
   return render(request, 'portfolio/visit_edit2.html', {'form': form})


@login_required
def visit_delete(request, pk):
   visit = get_object_or_404(Visit, pk=pk)
   visit.delete()
   visits = Visit.objects.filter(visit_date__lte=timezone.now())
   return render(request, 'portfolio/visit_list.html', {'visits': visits})

@staff_member_required
def visit_delete2(request, pk):
   visit = get_object_or_404(Visit, pk=pk)
   visit.delete()
   visits = Visit.objects.filter(visit_date__lte=timezone.now())
   return render(request, 'portfolio/visit_list2.html', {'visits': visits})

@login_required
def donor_list(request):
   donors = Donor.objects.filter(join_date__lte=timezone.now())
   return render(request, 'portfolio/donor_list.html', {'donors': donors})

@staff_member_required
def donor_list2(request):
   donors = Donor.objects.filter(join_date__lte=timezone.now())
   return render(request, 'portfolio/donor_list2.html', {'donors': donors})


@login_required
def donor_new(request):
   if request.method == "POST":
       form = DonorForm(request.POST)
       if form.is_valid():
           donor = form.save(commit=False)
           donor.created_date = timezone.now()
           donor.save()
           donors = Donor.objects.filter(join_date__lte=timezone.now())
           return render(request, 'portfolio/donor_list.html',
                         {'donors': donors})
   else:
       form = DonorForm()
       # print("Else")
   return render(request, 'portfolio/donor_new.html', {'form': form})

@staff_member_required
def donor_new2(request):
   if request.method == "POST":
       form = DonorForm(request.POST)
       if form.is_valid():
           donor = form.save(commit=False)
           donor.created_date = timezone.now()
           donor.save()
           donors = Donor.objects.filter(join_date__lte=timezone.now())
           return render(request, 'portfolio/donor_list2.html',
                         {'donors': donors})
   else:
       form = DonorForm()
       # print("Else")
   return render(request, 'portfolio/donor_new2.html', {'form': form})


@login_required
def donor_edit(request, pk):
   donor = get_object_or_404(Donor, pk=pk)
   if request.method == "POST":
       form = DonorForm(request.POST, instance=donor)
       if form.is_valid():
           donor = form.save()
           donor.updated_date = timezone.now()
           donor.save()
           donors = Donor.objects.filter(join_date__lte=timezone.now())
           return render(request, 'portfolio/donor_list.html', {'donors': donors})
   else:
       # print("else")
       form = DonorForm(instance=donor)
   return render(request, 'portfolio/donor_edit.html', {'form': form})

@staff_member_required
def donor_edit2(request, pk):
   donor = get_object_or_404(Donor, pk=pk)
   if request.method == "POST":
       form = DonorForm(request.POST, instance=donor)
       if form.is_valid():
           donor = form.save()
           donor.updated_date = timezone.now()
           donor.save()
           donors = Donor.objects.filter(join_date__lte=timezone.now())
           return render(request, 'portfolio/donor_list2.html', {'donors': donors})
   else:
       # print("else")
       form = DonorForm(instance=donor)
   return render(request, 'portfolio/donor_edit2.html', {'form': form})


@login_required
def donor_delete(request, pk):
   donor = get_object_or_404(Donor, pk=pk)
   donor.delete()
   donors = Donor.objects.filter(join_date__lte=timezone.now())
   return render(request, 'portfolio/donor_list.html', {'donors': donors})

@staff_member_required
def donor_delete2(request, pk):
   donor = get_object_or_404(Donor, pk=pk)
   donor.delete()
   donors = Donor.objects.filter(join_date__lte=timezone.now())
   return render(request, 'portfolio/donor_list2.html', {'donors': donors})


@login_required
def trackvisits(request, pk):
    visits = Visit.objects.filter(name=pk)
    return render(request, 'portfolio/trackvisits.html', {'visits': visits})

@staff_member_required
def trackvisits2(request, pk):
    visits = Visit.objects.filter(name=pk)
    return render(request, 'portfolio/trackvisits2.html', {'visits': visits})

@login_required
def itemstotal(request, pk):
    donations = Donation.objects.filter(item=pk)
    visits= Visit.objects.filter(item=pk)
    sum_items = Donation.objects.filter(item=pk).aggregate(quantity__sum=Coalesce(Sum('quantity'),0.0))
    sum_citems = Visit.objects.filter(item=pk).aggregate(item_quantity__sum=Coalesce(Sum('item_quantity'),0.0))
    difference= sum_items["quantity__sum"] - sum_citems["item_quantity__sum"]
    return render(request, 'portfolio/itemstotal.html', {'donations': donations,'visits':visits, 'sum_items':sum_items, 'sum_citems':sum_citems,
                                                         'difference':difference})

@staff_member_required
def itemstotal2(request, pk):
    donations = Donation.objects.filter(item=pk)
    visits= Visit.objects.filter(item=pk)
    sum_items = Donation.objects.filter(item=pk).aggregate(quantity__sum=Coalesce(Sum('quantity'),0.0))
    sum_citems = Visit.objects.filter(item=pk).aggregate(item_quantity__sum=Coalesce(Sum('item_quantity'),0.0))
    difference= sum_items["quantity__sum"] - sum_citems["item_quantity__sum"]
    return render(request, 'portfolio/itemstotal2.html', {'donations': donations,'visits':visits, 'sum_items':sum_items, 'sum_citems':sum_citems,
                                                         'difference':difference})
@login_required
def trackdonations(request, pk):
    donations = Donation.objects.filter(donor=pk)
    return render(request, 'portfolio/trackdonations.html', {'donations': donations, 'donorpk': pk})

@staff_member_required
def trackdonations2(request, pk):
    donations = Donation.objects.filter (donor=pk)
    return render (request, 'portfolio/trackdonations.html', {'donations': donations, 'donorpk': pk})

@login_required
def trackdonations_download(request, pk):
    donations = Donation.objects.filter(donor=pk)

    data = 'Item Name,Donor Name,Item Quantity,Received Date\n'
    for donation in donations:
        data += '%s,%s,%s,%s\n' % (donation.item, donation.donor, donation.quantity, donation.received_date)

    response = HttpResponse(data)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="donations.csv"'

    return response

@login_required
def trackdonations_download2(request, pk):
    donations = Donation.objects.filter(donor=pk)

    data = 'Item Name,Donor Name,Item Quantity,Received Date\n'
    for donation in donations:
        data += '%s,%s,%s,%s\n' % (donation.item, donation.donor, donation.quantity, donation.received_date)

    response = HttpResponse(data)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="donations.csv"'

    return response


@login_required
def password_reset(request):
   if request.method == "POST":
       form = VolunteerForm(request.POST)
       if form.is_valid():
           volunteer = form.save(commit=False)
           volunteer.created_date = timezone.now()
           volunteer.save()
           volunteers = Volunteer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/password_reset.html',
                         {'volunteers': volunteers})
   else:
       form = VolunteerForm()
       # print("Else")
   return render(request, 'portfolio/password_reset.html', {'form': form})

@login_required
def password_reset2(request):
   if request.method == "POST":
       form = VolunteerForm(request.POST)
       if form.is_valid():
           volunteer = form.save(commit=False)
           volunteer.created_date = timezone.now()
           volunteer.save()
           volunteers = Volunteer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/password_reset2.html',
                         {'volunteers': volunteers})
   else:
       form = VolunteerForm()
   return render(request, 'portfolio/password_reset2.html', {'form': form})


def send_pdf_email(request,pk):
    print ("testing")
    print(pk)
    donations_list = Donation.objects.filter(donor=pk)
    donor = get_object_or_404(Donor, pk=pk)
    message = 'Thank you for Donating to Good Shepherd Food Pantry. Your receipt is attached with this mail'
    subject = 'Donation Confirmation'
    print("Before generating PDF")
    donation_pdf = genrate_donation_pdf(request, pk)
    donation_FileName = 'donation_'+str(pk)+'.pdf'
    msg = EmailMessage(subject, message, from_email="donotreply@gsfp.com", to=[donor.email])
    msg.attach(donation_FileName, donation_pdf, 'application/pdf')
    msg.send()
    print("After sending PDF")
    return render(request, 'portfolio/trackdonations.html', {'donations': donations_list, 'donorpk': pk})



def genrate_donation_pdf(request,pk):
    donations_pdf = Donation.objects.filter(donor=pk)
    context = { 'donations': donations_pdf }
    pdf = render_to_pdf('portfolio/pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['content-Disposition'] = 'filename = "donations_{}.pdf"'
        return pdf
    return HttpResponse("Not Found")
