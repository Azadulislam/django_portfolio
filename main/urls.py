from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('portfolio/', views.portfolio, name='portfolio'),
]


