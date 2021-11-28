from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
    path('signin/',views.signin),
    path('newplaces/',views.newplaces),
    path('gudier/',views.gudier),
    path('signin/',views.signin),
    path('viewdetails/',views.viewdetails),
    path('guider/',views.guiderdetails),
    path('gallery/',views.imagegallery),
    path('video/',views.videogallery),

]