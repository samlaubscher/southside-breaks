from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_threads, name='threads'),
    path('<int:thread_id>/', views.view_thread, name='view_thread'),
    path('create_thread/', views.create_thread, name='create_thread'),
    path('edit/<int:thread_id>/', views.edit_thread, name='edit_thread'),
    path('delete/<int:thread_id>/', views.delete_thread,
         name='delete_thread'),
]
