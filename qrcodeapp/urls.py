from django.urls import path
from . import views

urlpatterns = [
    path('', views.qr_generator, name='qr_gen'),
    path('track/<str:order>/', views.track, name='track'),
]
