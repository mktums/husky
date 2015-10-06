"""husky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from doctors.views import index, get_excluded_dates_by_doctor, get_time_by_doctor_and_date

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^gedbd/(?P<doctor_id>\d+)/$', get_excluded_dates_by_doctor),
    url(r'^gatbdd/(?P<doctor_id>\d+)/(?P<date>\d{2}\.\d{2}\.\d{4})/$', get_time_by_doctor_and_date),
]
