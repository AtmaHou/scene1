from django.conf.urls import patterns, include, url
from book.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^time/$', current_time),
    (r'^add_book/$', add_book),
    (r'^home/$', homepage),
    (r'^add_author/$', add_author),
    (r'^update/$', update)
)