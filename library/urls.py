from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^book_list/$', views.book_list, name='book_list'),
    url(r'^book_list/(?P<book_id>[0-9]+)/$', views.book_details, name='book_details'),
    url(r'^dvd_list/$', views.dvd_list, name='dvd_list'),
    url(r'^dvd_list/(?P<dvd_id>[0-9]+)/$', views.dvd_details, name='dvd_details'),
    url(r'^magazine_list/$', views.magazine_list, name='magazine_list'),
    url(r'^magazine_list/(?P<magazine_id>[0-9]+)/$', views.magazine_details, name='magazine_details'),
]
