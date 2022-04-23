from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='messages'),
    path('sent_messages/', views.sent_messages, name='sent_messages'),
    path('<int:direct_message_id>/', views.view_message, name='view_message'),
    path('send_message/', views.send_message, name='send_message'),
    path('reply_to_message/<int:direct_message_id>', views.reply_to_message, name='reply_to_message'),
]
