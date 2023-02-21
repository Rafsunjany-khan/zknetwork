from django.urls import path
from . import views
urlpatterns =[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('package/', views.package, name='package'),
    path('airlince/', views.airlince, name='airlince'),
    path('blog/', views.blog, name='blog'),
    path('carrier/', views.carrier, name='carrier'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('visa/', views.visa, name='visa'),
    path('airticket/', views.airticket, name='airticket'),
    path('hotel/', views.hotel, name='hotel'),
]