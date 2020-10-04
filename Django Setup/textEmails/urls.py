from django.conf.urls import url
from textEmails import views

app_name = 'textEmails'

urlpatterns = [
    url(r'^inbox/', views.InboxView.as_view(), name='inbox_view'),
    url(r'^contactus/', views.ContactUsView.as_view(), name='contact_view'),
]