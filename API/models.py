from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ['id']

    def albums(self):
        return self.album_set.all()

    def __repr__(self):
        return f"[ARTIST] id: {self.id} - {self.name}"
    
    def __str__(self):
        return self.__repr__()

class Album(models.Model):
    artist_obj = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.IntegerField()

    album_songs = models.ManyToManyField('AlbumSong')

    class Meta:
        ordering = ['id']

    def get_album_songs(self):
        return self.album_songs.all()

    def __repr__(self):
        return f"[ALBUM] id: {self.id} - by {self.artist_obj.name}, {self.year}"
    
    def __str__(self):
        return self.__repr__()

class Song(models.Model):
    name = models.CharField(max_length=50, blank=False)
    album_songs = models.ManyToManyField('AlbumSong')

    class Meta:
        ordering = ['id']

    def get_album_songs(self):
        return self.album_songs.all()

    def __repr__(self):
        return f"[SONG] id: {self.id} - {self.name}"
    
    def __str__(self):
        return self.__repr__()

class AlbumSong(models.Model):
    album_obj = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_obj = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_number = models.IntegerField()

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=('album_obj', 'song_obj'),
                name='Unique together album and song constraint',
                violation_error_message='album and song must be unique together',
            ),
            models.UniqueConstraint(
                fields=('album_obj', 'song_number'),
                name='Unique together album and song_number constraint',
                violation_error_message='album and song_number must be unique together',
            ),
            models.UniqueConstraint(
                fields=('song_number', 'song_obj'),
                name='Unique together song_number and song constraint',
                violation_error_message='song_number and song must be unique together',
            )
        ]

    def __repr__(self) -> str:
        return f"[ALBUM_SONG] id: {self.id} - #{self.song_number} {self.song_obj.__repr__()} from {self.album_obj.__repr__()}"
    
    def __str__(self):
        return self.__repr__()
