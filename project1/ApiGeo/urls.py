from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'ApiGeo'

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^index/$', views.index, name='index'),
    url(r'^filter/$', views.FilterListView.as_view(), name='filter'),
    url(r'^git/$', views.git, name='git')

]