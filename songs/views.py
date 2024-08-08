from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView


class ListCreateSongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def perform_create(self, serializer):
        album_id = self.kwargs.get(self.lookup_field)
        album = Album.objects.get(pk=album_id)
        return serializer.save(album=album)
