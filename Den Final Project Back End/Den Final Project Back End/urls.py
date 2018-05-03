"""DenLab3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# app's urls.py
from django.urls import url
from . import views
urlpatterns = [
	url(r'^(?P<id>[0-9]*)$', views.account_handler, name='contact')
]

# project's urls.py
from django.urls import include

urlpatterns = [
	url(r'^accounts/$', include('bank.urls'))
	
from .views import AccountView
urlpatterns = [
url(r'^(?P<id>[0-9]*)$'
, AccountView.as_view(), name='contact')
]
