from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.abc, name='abc'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home2/$', views.home2, name='home2'),
    url(r'^volunteer/$', views.volunteer_list, name='volunteer_list'),
    url(r'^volunteer/(?P<pk>\d+)/delete/$', views.volunteer_delete, name='volunteer_delete'),
    url(r'^volunteer/(?P<pk>\d+)/edit/$', views.volunteer_edit, name='volunteer_edit'),
    url(r'^volunteer/create/$', views.volunteer_new, name='volunteer_new'),

    url(r'^inventory/$', views.inventory_list, name='inventory_list'),
    url(r'^inventory2/$', views.inventory_list2, name='inventory_list2'),
    url(r'^inventory/(?P<pk>\d+)/delete/$', views.inventory_delete, name='inventory_delete'),
    url(r'^inventory2/(?P<pk>\d+)/delete/$', views.inventory_delete2, name='inventory_delete2'),
    url(r'^inventory/(?P<pk>\d+)/edit/$', views.inventory_edit, name='inventory_edit'),
    url(r'^inventory2/(?P<pk>\d+)/edit/$', views.inventory_edit2, name='inventory_edit2'),
    url(r'^inventory/(?P<pk>\d+)/itemstotal/$', views.itemstotal, name='itemstotal'),
    url(r'^inventory/(?P<pk>\d+)/itemstotal2/$', views.itemstotal2, name='itemstotal2'),
    url(r'^inventory/create/$', views.inventory_new, name='inventory_new'),
    url(r'^inventory2/create/$', views.inventory_new2, name='inventory_new2'),

    url(r'^client/$', views.client_list, name='client_list'),
    url(r'^client2/$', views.client_list2, name='client_list2'),
    url (r'^client/search/$', views.client_search, name='client_search'),
    url (r'^client/search2/$', views.client_search2, name='client_search2'),
    url(r'^client/(?P<pk>\d+)/delete/$', views.client_delete, name='client_delete'),
    url(r'^client2/(?P<pk>\d+)/delete/$', views.client_delete2, name='client_delete2'),
    url(r'^client/(?P<pk>\d+)/edit/$', views.client_edit, name='client_edit'),
    url(r'^client2/(?P<pk>\d+)/edit/$', views.client_edit2, name='client_edit2'),
    url(r'^client/(?P<pk>\d+)/trackvisits/$', views.trackvisits, name='trackvisits'),
    url(r'^client/(?P<pk>\d+)/trackvisits2/$', views.trackvisits2, name='trackvisits2'),
    url(r'^client/create/$', views.client_new, name='client_new'),
    url(r'^client2/create/$', views.client_new2, name='client_new2'),

    url(r'^donation/$', views.donation_list, name='donation_list'),
    url(r'^donation2/$', views.donation_list2, name='donation_list2'),
    url(r'^donation/(?P<pk>\d+)/delete/$', views.donation_delete, name='donation_delete'),
    url(r'^donation2/(?P<pk>\d+)/delete/$', views.donation_delete2, name='donation_delete2'),
    url(r'^donation/(?P<pk>\d+)/edit/$', views.donation_edit, name='donation_edit'),
    url(r'^donation2/(?P<pk>\d+)/edit/$', views.donation_edit2, name='donation_edit2'),
    url(r'^donation/(?P<pk>\d+)/trackdonations/$', views.trackdonations, name='trackdonations'),
    url(r'^donation/(?P<pk>\d+)/trackdonations2/$', views.trackdonations2, name='trackdonations2'),
    url (r'^donation/(?P<pk>\d+)/trackdonations/download/$', views.trackdonations_download,
         name='trackdonations_download'),
    url (r'^donation/(?P<pk>\d+)/trackdonations/download2/$', views.trackdonations_download2,
         name='trackdonations_download2'),
    url(r'^donation/create/$', views.donation_new, name='donation_new'),
    url(r'^donation2/create/$', views.donation_new2, name='donation_new2'),
    url(r'^donation/password_reset/$', views.password_reset, name='password_reset'),
    url(r'^donation2/password_reset/$', views.password_reset2, name='password_reset'),

    url(r'^visit/$', views.visit_list, name='visit_list'),
    url(r'^visit2/$', views.visit_list2, name='visit_list2'),
    url(r'^visit/(?P<pk>\d+)/delete/$', views.visit_delete, name='visit_delete'),
    url(r'^visit2/(?P<pk>\d+)/delete/$', views.visit_delete2, name='visit_delete2'),
    url(r'^visit/(?P<pk>\d+)/edit/$', views.visit_edit, name='visit_edit'),
    url(r'^visit2/(?P<pk>\d+)/edit/$', views.visit_edit2, name='visit_edit2'),
    url(r'^visit/create/$', views.visit_new, name='visit_new'),
    url(r'^visit2/create/$', views.visit_new2, name='visit_new2'),

    url(r'^donor/$', views.donor_list, name='donor_list'),
    url(r'^donor2/$', views.donor_list2, name='donor_list2'),
    url(r'^donor/(?P<pk>\d+)/delete/$', views.donor_delete, name='donor_delete'),
    url(r'^donor2/(?P<pk>\d+)/delete/$', views.donor_delete2, name='donor_delete2'),
    url(r'^donor/(?P<pk>\d+)/edit/$', views.donor_edit, name='donor_edit'),
    url(r'^donor2/(?P<pk>\d+)/edit/$', views.donor_edit2, name='donor_edit2'),
    url(r'^donor/create/$', views.donor_new, name='donor_new'),
    url(r'^donor2/create/$', views.donor_new2, name='donor_new2'),

    url(r'^password/$', views.change_password, name='change_password'),

    url(r'^send_pdf_email/(?P<pk>\d+)/$', views.send_pdf_email, name='send_pdf_email'),



    

    ]
