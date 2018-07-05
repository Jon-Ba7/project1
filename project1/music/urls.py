from django.conf.urls import url
from . import views 
app_name = 'music'

urlpatterns = [
    #/music/
    #url(r'^$', views.index, name='index'),
    url(r'^album$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/music/<album_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='details'),

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    # /music/album/id/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/pk/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # Authenticate
    url(r'^register$', views.UserFormView.as_view(), name='register'),

];
