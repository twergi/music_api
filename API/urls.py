from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from API import views


urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('artists/', views.ArtistsView.as_view()),
    path('artists/<int:pk>/', views.ArtistView.as_view()),
    path('songs/', views.SongsView.as_view()),
    path('songs/<int:pk>/', views.SongView.as_view()),
    path('albums/', views.AlbumsView.as_view()),
    path('albums/<int:pk>/', views.AlbumView.as_view()),
    path('albums/<int:album_pk>/songs/', views.AlbumSongsView.as_view()),
    path('albums/<int:album_pk>/songs/<int:song_number>/', views.AlbumSongView.as_view()),
]