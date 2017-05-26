from django.conf.urls import url
from pizzas import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<pizza_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^conocenos/$', views.index, name="conocenos"),
    url(r'^fichero/$', views.fichero, name="fichero"),
    
]