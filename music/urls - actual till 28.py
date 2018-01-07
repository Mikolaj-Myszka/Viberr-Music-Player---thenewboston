from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [

    # /music/
    url(r'^$', views.index, name='index'),
    # /music/712/
    url(r'^(?P<dupa>[0-9]+)/$', views.detail, name='detail'), #dupa to album_id
    # /music/712/favourite/
    url(r'^(?P<dupa>[0-9]+)/favourite/$', views.favourite, name='favourite'),

]