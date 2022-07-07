from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_releases, name='releases'),
    path('<int:release_id>/', views.view_release, name='view_release'),
    path('create_release/', views.create_release, name='create_release'),
    path('edit/<int:release_id>/', views.edit_release, name='edit_release'),
    path('delete/<int:release_id>/', views.delete_release,
         name='delete_release'),
]
