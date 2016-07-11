from django.conf.urls import url
from dms import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
