from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_members, name='team_members'),
    path('<int:team_member_id>/', views.view_member, name='view_member'),
    path('create_team_member/', views.create_member, name='create_member'),
    path('edit/<int:team_member_id>/', views.edit_member, name='edit_member'),
    path('delete/<int:team_member_id>/', views.delete_member,
         name='delete_member'),
]
