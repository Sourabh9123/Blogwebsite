from django.urls import path
from App import views


urlpatterns = [
    path('', views.home,  name='home'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('terms/',views.terms, name='terms')
]
