from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:blogs_id>/', views.view_blog, name='view_blog'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>/', views.delete_blog,
         name='delete_blog'),
]
