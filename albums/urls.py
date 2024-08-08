from django.urls import path
from .views import ListCreateAlbumView
from songs.views import ListCreateSongView

urlpatterns = [
    path("albums/", ListCreateAlbumView.as_view()),
    path("albums/<int:pk>/songs/", ListCreateSongView.as_view()),
]
