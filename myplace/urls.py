from django.conf.urls import url

from . import views
app_name='myplace'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<select_id>[0-9]+)$', views.details, name='details'),
    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^thefilter/(?P<typenaja>[A-Za-z ]+)$', views.thefilter, name='thefilter'),
    url(r'^about/$', views.about, name='about'),
]
