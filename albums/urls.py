from django.urls import path
from .views import ListCreateAlbumView
from songs import views as song_views

urlpatterns = [
    path("albums/", ListCreateAlbumView.as_view()),
    path("albums/<int:pk>/songs/", song_views.SongView.as_view()),
]
