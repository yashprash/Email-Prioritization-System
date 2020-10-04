"""emailPrioritization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from textEmails import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^contactus/', views.ContactUsView.as_view(), name='contact_view'),
    url(r'^about/', views.AboutView.as_view(), name='about_view'),
    url(r'^$', views.InboxView.as_view(), name='home'),
    url(r'^home/', views.HomeView, name='mailbox'),
    url(r'^priority1/', views.P1View, name='p1urls'),
    url(r'^priority2/', views.P2View, name='p2urls'),
    url(r'^priority3/', views.P3View, name='p3urls'),
    url(r'^new_mail/', views.sendmail, name='new_mail'),
    url(r'^inbox/', views.priority_select, name='selection_p'),



]
