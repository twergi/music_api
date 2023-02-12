from django.db.models import Q
from rest_framework import exceptions
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from API import models as apim
from API import serializers as apis


class ArtistsView(ListCreateAPIView):
    queryset = apim.Artist.objects.all()
    serializer_class = apis.ArtistsSerializer

class ArtistView(RetrieveUpdateDestroyAPIView):
    queryset = apim.Artist.objects.all()
    serializer_class = apis.ArtistSerializer

class AlbumsView(ListCreateAPIView):
    queryset = apim.Album.objects.all()
    serializer_class = apis.AlbumsSerializer

class AlbumView(RetrieveUpdateDestroyAPIView):
    queryset = apim.Album.objects.all()
    serializer_class = apis.AlbumSerializer

class SongsView(ListCreateAPIView):
    queryset = apim.Song.objects.all()
    serializer_class = apis.SongsSerializer

class SongView(RetrieveUpdateDestroyAPIView):
    queryset = apim.Song.objects.all()
    serializer_class = apis.SongSerializer

class AlbumSongsView(ListCreateAPIView):
    serializer_class = apis.AlbumSongsSerializer

    def get_queryset(self):
        return apim.Album.objects.get(pk=self.kwargs['album_pk']).album_songs.all().order_by('song_number')

class AlbumSongView(RetrieveUpdateDestroyAPIView):
    serializer_class = apis.AlbumSongSerializer

    def get_object(self):
        try:
            return apim.AlbumSong.objects.get(
                Q(album_obj=self.kwargs['album_pk'])
                & Q(song_number=self.kwargs['song_number'])
            )
        except apim.AlbumSong.DoesNotExist:
            raise exceptions.NotFound({'detail': f"Song with song_number={self.kwargs['song_number']} and album id={self.kwargs['album_pk']} not found"})