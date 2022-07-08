from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_guest_mixes, name='guest_mixes'),
    path('create_guest_mix/', views.create_guest_mix, name='create_guest_mix'),
    path('edit/<int:guest_mix_id>/', views.edit_guest_mix, name='edit_guest_mix'),
    path('delete/<int:guest_mix_id>/', views.delete_guest_mix,
         name='delete_guest_mix'),
]
