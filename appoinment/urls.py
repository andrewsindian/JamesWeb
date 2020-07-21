from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('index.html', views.home,name='home'),
    path('enquiry',views.enquiry,name='enquiry'),
    path('Thinfilm.html', views.Thinfilm,name='Thinfilm'),
    path('Microwave.html', views.microwave,name='microwave'),
    path('Members.html', views.Members,name='Members'),
    path('openings.html', views.openings,name='openings'),
    path('Alumni.html', views.Alumni,name='Alumni'),
    path('contact.html', views.contact,name='contact'),
    path('Publications.html', views.oldsite,name='oldsite'),
    path('Materials.html', views.material,name='material'),
    path('CentralFacilities.html', views.CIL,name='CentralFacilities'),
    path('Photos.html', views.photos,name='Photos'),

]
