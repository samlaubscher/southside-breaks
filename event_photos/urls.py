from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_photos, name='event_photos'),
    path('<int:photo_id>/', views.view_photo, name='view_photo'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    path('delete/<int:photo_id>/', views.delete_photo,
         name='delete_photo'),
]
