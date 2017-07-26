from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^(?P<id>[0-9]+)/$', views.note, name='note'),
        url(r'^add/$', views.add, name='add')
        ]