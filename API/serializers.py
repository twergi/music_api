from django.db import IntegrityError
from rest_framework import exceptions, serializers

from API import models as apim


class ArtistsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = apim.Artist
        fields = ['id', 'name']

class AlbumsSerializer(serializers.ModelSerializer):
    artist = ArtistsSerializer(source='artist_obj', read_only=True)
    artist_id = serializers.IntegerField(write_only=True)
    songs_count = serializers.SerializerMethodField()
    class Meta:
        model = apim.Album
        fields = ['id', 'year', 'songs_count', 'artist', 'artist_id']
    
    def get_songs_count(self, obj: apim.Album) -> int:
        return obj.album_songs.count()
    
    def create(self, validated_data):
        try:
            artist = apim.Artist.objects.get(pk=validated_data['artist_id'])
        except apim.Artist.DoesNotExist:
            raise exceptions.NotFound({'detail': f"Artist with id={validated_data['artist_id']} not found"})
        
        new_album = apim.Album.objects.create(
            year=validated_data['year'],
            artist_obj=artist
        )

        new_album.save()
        return new_album

class SongsSerializer(serializers.ModelSerializer):
    albums_count = serializers.SerializerMethodField()

    class Meta:
        model = apim.Song
        fields = ['id', 'name', 'albums_count']
    
    def get_albums_count(self, obj: apim.Song) -> int:
        return obj.album_songs.count()

class AlbumSongsSerializer(serializers.ModelSerializer):
    song = SongsSerializer(source='song_obj', read_only=True)
    song_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = apim.AlbumSong
        fields = ['song_number', 'song', 'song_id']
    
    def create(self, validated_data):
        try:
            song = apim.Song.objects.get(pk=validated_data['song_id'])
        except apim.Song.DoesNotExist:
            raise exceptions.NotFound({'detail': f"Song with id={validated_data['song_id']} not found"})

        album = apim.Album.objects.get(pk=self.context['view'].kwargs['album_pk'])

        song_number = validated_data['song_number']
    
        try:
            new_album_song = apim.AlbumSong.objects.create(
                song_number=song_number,
                song_obj=song,
                album_obj=album
            )
        except IntegrityError:
            raise exceptions.ValidationError({'detail': 'Uniqueness constraint violated'})

        new_album_song.save()
        song.album_songs.add(new_album_song)
        album.album_songs.add(new_album_song)
        return new_album_song

class AlbumSongSerializer(serializers.ModelSerializer):
    song = SongsSerializer(source='song_obj', read_only=True)
    song_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = apim.AlbumSong
        fields = ['song_number', 'song', 'song_id']

    def update(self, instance: apim.AlbumSong, validated_data: dict):
        try:
            song = apim.Song.objects.get(
                pk=validated_data.get('song_id', instance.song_obj.id)
            )
        except apim.Song.DoesNotExist:
            raise exceptions.NotFound({'detail': f"Song with id={validated_data['song_id']} not found"})
        prev_song = instance.song_obj

        try:
            instance.song_number=validated_data.get('song_number', instance.song_number)
            instance.song_obj=song
            instance.save()
        except IntegrityError:
            raise exceptions.ValidationError({'detail': 'Uniqueness constraint violated'})
        
        prev_song.album_songs.remove(instance)
        song.album_songs.add(instance)
        return instance

class SongAlbumsSerializer(serializers.ModelSerializer):
    album = AlbumsSerializer(source='album_obj')
    class Meta:
        model = apim.AlbumSong
        fields = ['song_number', 'album']

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumsSerializer(many=True, read_only=True)

    class Meta:
        model = apim.Artist
        fields = ['id', 'name', 'albums']

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistsSerializer(source='artist_obj', read_only=True)
    songs = AlbumSongsSerializer(source='get_album_songs', many=True, read_only=True)
    class Meta:
        model = apim.Album
        fields = ['id', 'year', 'artist', 'songs']

class SongSerializer(serializers.ModelSerializer):
    albums = SongAlbumsSerializer(source='get_album_songs', many=True, read_only=True)
    class Meta:
        model = apim.Song
        fields = ['id', 'name', 'albums']
